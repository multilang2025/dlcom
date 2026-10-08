"""Country / nationality detection for the lead analysis (heuristic, ES / FR / EN text, phone prefixes).

Nothing here stores a name, e-mail or phone number: phone numbers are reduced to a calling code -> country.
"""
import re

from leads_taxonomy import norm

# key: (ES, FR, EN, demonym regex, country-name regex)   (patterns are applied to accent-stripped lower-case text)
C = {
    "ES": ("España", "Espagne", "Spain", r"espanol[ae]?s?|spanish|espagnol[e]?s?", r"espana|spain|espagne"),
    "FR": ("Francia", "France", "France", r"frances(a|es)?|french|francais[e]?s?", r"francia|france"),
    "GB": ("Reino Unido", "Royaume-Uni", "United Kingdom", r"britanic[oa]s?|british|brit\b|ingles(a|es)?|english|anglais[e]?s?|britannique[s]?|escoces|scottish|irlandes del norte|welsh|gales(a)?", r"reino unido|royaume.uni|united kingdom|\buk\b|\bu\.k\.|great britain|inglaterra|england|angleterre|scotland|ecosse"),
    "US": ("Estados Unidos", "États-Unis", "United States", r"estadounidense|norteamericano|north american|american\b|americain[e]?s?|americano", r"estados unidos|etats.unis|united states|\busa\b|\bu\.s\.a?\b|\beeuu\b|\bee\.uu\b|\bus\b(?! to)|florida|california|texas|new york|nueva york"),
    "CA": ("Canadá", "Canada", "Canada", r"canadiense|canadian|canadien[ne]?s?|quebecois[e]?", r"canada|quebec"),
    "RU": ("Rusia", "Russie", "Russia", r"ruso|rusa|rusos|russian|russe[s]?", r"rusia|russia|russie"),
    "UA": ("Ucrania", "Ukraine", "Ukraine", r"ucraniano|ucraniana|ukrainian|ukrainien[ne]?s?", r"ucrania|ukraine"),
    "BY": ("Bielorrusia", "Biélorussie", "Belarus", r"bielorruso|belarusian|belarusse|bielorusse", r"bielorrusia|belarus|bielorussie"),
    "KZ": ("Kazajistán", "Kazakhstan", "Kazakhstan", r"kazajo|kazakh|kazakhstani|kazakhe", r"kazajistan|kazakhstan"),
    "GE": ("Georgia", "Géorgie", "Georgia", r"georgiano|georgian|georgien", r"georgia(?! del)|georgie|tbilis"),
    "AM": ("Armenia", "Arménie", "Armenia", r"armenio|armenian|armenien", r"armenia|armenie"),
    "AZ": ("Azerbaiyán", "Azerbaïdjan", "Azerbaijan", r"azerbaiyano|azerbaijani|azeri", r"azerbaiyan|azerbaijan|azerbaidjan"),
    "MA": ("Marruecos", "Maroc", "Morocco", r"marroqui(es)?|moroccan|marocain[e]?s?", r"marruecos|morocco|maroc"),
    "DZ": ("Argelia", "Algérie", "Algeria", r"argelino|algerian|algerien[ne]?s?", r"argelia|algeria|algerie"),
    "TN": ("Túnez", "Tunisie", "Tunisia", r"tunecino|tunisian|tunisien[ne]?s?", r"tunez|tunisia|tunisie"),
    "SN": ("Senegal", "Sénégal", "Senegal", r"senegales|senegalese|senegalais[e]?", r"senegal"),
    "ML": ("Mali", "Mali", "Mali", r"maliense|malian|malien[ne]?", r"\bmali\b"),
    "CI": ("Costa de Marfil", "Côte d'Ivoire", "Ivory Coast", r"marfilen[oa]|ivorian|ivoirien[ne]?", r"costa de marfil|ivory coast|cote d.ivoire"),
    "CM": ("Camerún", "Cameroun", "Cameroon", r"camerunes|cameroonian|camerounais[e]?", r"camerun|cameroon|cameroun"),
    "EG": ("Egipto", "Égypte", "Egypt", r"egipcio|egyptian|egyptien[ne]?", r"egipto|egypt\b|egypte"),
    "LB": ("Líbano", "Liban", "Lebanon", r"libanes|lebanese|libanais[e]?", r"libano|lebanon|liban"),
    "PS": ("Palestina", "Palestine", "Palestine", r"palestino|palestinian|palestinien[ne]?", r"palestina|palestine|gaza"),
    "SY": ("Siria", "Syrie", "Syria", r"sirio|syrian|syrien[ne]?", r"siria|syria|syrie"),
    "IR": ("Irán", "Iran", "Iran", r"irani\b|iranian|iranien[ne]?", r"\biran\b"),
    "IL": ("Israel", "Israël", "Israel", r"israeli|israelien[ne]?", r"israel"),
    "TR": ("Turquía", "Turquie", "Turkey", r"turco|turkish|turc\b|turque", r"turquia|turkey|turquie"),
    "IN": ("India", "Inde", "India", r"indio\b|indian\b|indien[ne]?s?", r"\bindia\b|\binde\b"),
    "PK": ("Pakistán", "Pakistan", "Pakistan", r"pakistani|paquistani|pakistanais[e]?", r"pakistan|paquistan"),
    "CN": ("China", "Chine", "China", r"chino|chinese|chinois[e]?", r"\bchina\b|chine"),
    "JP": ("Japón", "Japon", "Japan", r"japones|japanese|japonais[e]?", r"japon|japan"),
    "PH": ("Filipinas", "Philippines", "Philippines", r"filipino|filipina|philippine\b|philippin[e]?s?\b", r"filipinas|philippines"),
    "TH": ("Tailandia", "Thaïlande", "Thailand", r"tailandes|thai\b|thailandais[e]?", r"tailandia|thailand|thailande"),
    "VE": ("Venezuela", "Venezuela", "Venezuela", r"venezolan[oa]s?|venezuelan|venezuelien[ne]?", r"venezuela"),
    "CO": ("Colombia", "Colombie", "Colombia", r"colombian[oa]s?|colombien[ne]?", r"colombia|colombie"),
    "PE": ("Perú", "Pérou", "Peru", r"peruan[oa]s?|peruvian|peruvien[ne]?", r"\bperu\b|perou"),
    "AR": ("Argentina", "Argentine", "Argentina", r"argentin[oa]s?|argentinian|argentine\b", r"argentina|argentine"),
    "BR": ("Brasil", "Brésil", "Brazil", r"brasilen[oa]s?|brazilian|bresilien[ne]?", r"brasil|brazil|bresil"),
    "MX": ("México", "Mexique", "Mexico", r"mexican[oa]s?|mexicain[e]?", r"mexico|mexique"),
    "CL": ("Chile", "Chili", "Chile", r"chilen[oa]s?|chilean|chilien[ne]?", r"\bchile\b|\bchili\b"),
    "EC": ("Ecuador", "Équateur", "Ecuador", r"ecuatorian[oa]s?|ecuadorian|equatorien[ne]?", r"ecuador|equateur"),
    "CU": ("Cuba", "Cuba", "Cuba", r"cuban[oa]s?|cubain[e]?", r"\bcuba\b"),
    "DO": ("Rep. Dominicana", "Rép. dominicaine", "Dominican Republic", r"dominican[oa]s?|dominicain[e]?", r"republica dominicana|dominican republic|republique dominicaine"),
    "BO": ("Bolivia", "Bolivie", "Bolivia", r"boliviano|bolivian|bolivien[ne]?", r"bolivia|bolivie"),
    "UY": ("Uruguay", "Uruguay", "Uruguay", r"uruguay[oa]s?|uruguayan|uruguayen[ne]?", r"uruguay"),
    "DE": ("Alemania", "Allemagne", "Germany", r"aleman(es|a)?|german\b|allemand[e]?s?", r"alemania|germany|allemagne"),
    "IT": ("Italia", "Italie", "Italy", r"italian[oa]s?|italien[ne]?s?", r"italia|italy|italie"),
    "PT": ("Portugal", "Portugal", "Portugal", r"portugues(a|es)?|portuguese|portugais[e]?", r"portugal"),
    "BE": ("Bélgica", "Belgique", "Belgium", r"belga[s]?|belgian|belge[s]?", r"belgica|belgium|belgique"),
    "NL": ("Países Bajos", "Pays-Bas", "Netherlands", r"holandes(a|es)?|neerlandes(a)?|dutch|neerlandais[e]?|hollandais[e]?", r"holanda|paises bajos|netherlands|pays.bas|holland"),
    "CH": ("Suiza", "Suisse", "Switzerland", r"suiz[oa]s?|swiss|suisse[s]?", r"suiza|switzerland|suisse"),
    "SE": ("Suecia", "Suède", "Sweden", r"sueco|swedish|suedois[e]?", r"suecia|sweden|suede"),
    "NO": ("Noruega", "Norvège", "Norway", r"noruego|norwegian|norvegien[ne]?", r"noruega|norway|norvege"),
    "DK": ("Dinamarca", "Danemark", "Denmark", r"danes\b|danish|danois[e]?", r"dinamarca|denmark|danemark"),
    "FI": ("Finlandia", "Finlande", "Finland", r"finland[eé]s|finnish|finlandais[e]?", r"finlandia|finland|finlande"),
    "IE": ("Irlanda", "Irlande", "Ireland", r"irlandes(a)?|irish|irlandais[e]?", r"irlanda|ireland|irlande"),
    "AT": ("Austria", "Autriche", "Austria", r"austriac[oa]s?|austrian|autrichien[ne]?", r"austria|autriche"),
    "PL": ("Polonia", "Pologne", "Poland", r"polac[oa]s?|polish|polonais[e]?", r"polonia|poland|pologne"),
    "CZ": ("Rep. Checa", "Rép. tchèque", "Czech Republic", r"checo|czech|tcheque", r"republica checa|czech|tchequie|chequia"),
    "HU": ("Hungría", "Hongrie", "Hungary", r"hungaro|hungarian|hongrois[e]?", r"hungria|hungary|hongrie"),
    "RO": ("Rumanía", "Roumanie", "Romania", r"rumano|romanian|roumain[e]?", r"rumania|romania|roumanie"),
    "BG": ("Bulgaria", "Bulgarie", "Bulgaria", r"bulgaro|bulgarian|bulgare", r"bulgaria|bulgarie"),
    "LT": ("Lituania", "Lituanie", "Lithuania", r"lituano|lithuanian|lituanien[ne]?", r"lituania|lithuania|lituanie"),
    "LV": ("Letonia", "Lettonie", "Latvia", r"leton|latvian|letton[e]?", r"letonia|latvia|lettonie"),
    "EE": ("Estonia", "Estonie", "Estonia", r"estonio|estonian|estonien[ne]?", r"estonia|estonie"),
    "MD": ("Moldavia", "Moldavie", "Moldova", r"moldavo|moldovan|moldave", r"moldavia|moldova|moldavie"),
    "RS": ("Serbia", "Serbie", "Serbia", r"serbio|serbian|serbe\b", r"serbia|serbie"),
    "AL": ("Albania", "Albanie", "Albania", r"albanes|albanian|albanais[e]?", r"albania|albanie"),
    "ME": ("Montenegro", "Monténégro", "Montenegro", r"montenegrino|montenegrin", r"montenegro"),
    "HR": ("Croacia", "Croatie", "Croatia", r"croata|croatian|croate", r"croacia|croatia|croatie"),
    "GR": ("Grecia", "Grèce", "Greece", r"griego|greek|grec\b|grecque", r"grecia|greece|grece"),
    "LU": ("Luxemburgo", "Luxembourg", "Luxembourg", r"luxemburgues|luxembourgeois[e]?", r"luxemburgo|luxembourg"),
    "AU": ("Australia", "Australie", "Australia", r"australian[oa]s?|australien[ne]?", r"australia|australie|sydney"),
    "NZ": ("Nueva Zelanda", "Nouvelle-Zélande", "New Zealand", r"neozelandes|new zealander|neo.?zelandais[e]?", r"nueva zelanda|new zealand|nouvelle.zelande"),
    "ZA": ("Sudáfrica", "Afrique du Sud", "South Africa", r"sudafricano|south african|sud.africain[e]?", r"sudafrica|south africa|afrique du sud"),
    "NG": ("Nigeria", "Nigeria", "Nigeria", r"nigeriano|nigerian|nigerian[e]?", r"nigeria"),
    "AE": ("Emiratos Árabes", "Émirats arabes unis", "UAE", r"emirati", r"emiratos|emirates|dubai|dubai|abu dhabi|\buae\b"),
    "SA": ("Arabia Saudí", "Arabie saoudite", "Saudi Arabia", r"saudi|saudita", r"arabia saudi|saudi arabia|arabie saoudite"),
}

# calling code -> key. +1 is shared (US/CA); +7 shared (RU/KZ).
CALLING = {
    "1": "US/CA", "7": "RU/KZ", "20": "EG", "27": "ZA", "30": "GR", "31": "NL", "32": "BE", "33": "FR", "34": "ES", "36": "HU",
    "39": "IT", "40": "RO", "41": "CH", "43": "AT", "44": "GB", "45": "DK", "46": "SE", "47": "NO", "48": "PL", "49": "DE",
    "51": "PE", "52": "MX", "54": "AR", "55": "BR", "56": "CL", "57": "CO", "58": "VE", "61": "AU", "64": "NZ", "81": "JP", "86": "CN",
    "90": "TR", "91": "IN", "92": "PK", "98": "IR", "212": "MA", "213": "DZ", "216": "TN", "221": "SN", "223": "ML", "225": "CI",
    "237": "CM", "351": "PT", "352": "LU", "353": "IE", "354": "IS", "355": "AL", "357": "CY", "358": "FI", "359": "BG", "370": "LT",
    "371": "LV", "372": "EE", "373": "MD", "374": "AM", "375": "BY", "380": "UA", "381": "RS", "382": "ME", "385": "HR", "420": "CZ",
    "505": "NI", "506": "CR", "507": "PA", "591": "BO", "593": "EC", "595": "PY", "598": "UY", "809": "DO", "971": "AE", "972": "IL",
    "961": "LB", "963": "SY", "966": "SA", "970": "PS", "994": "AZ", "995": "GE", "996": "KG", "998": "UZ", "53": "CU",
}
EXTRA_NAMES = {"US/CA": ("EE. UU. / Canadá (+1)", "États-Unis / Canada (+1)"), "RU/KZ": ("Rusia / Kazajistán (+7)", "Russie / Kazakhstan (+7)"),
               "IS": ("Islandia", "Islande"), "CY": ("Chipre", "Chypre"), "NI": ("Nicaragua", "Nicaragua"), "CR": ("Costa Rica", "Costa Rica"),
               "PA": ("Panamá", "Panama"), "PY": ("Paraguay", "Paraguay"), "KG": ("Kirguistán", "Kirghizistan"), "UZ": ("Uzbekistán", "Ouzbékistan")}


def country_name(key, fr=False):
    if key in C:
        return C[key][1 if fr else 0]
    if key in EXTRA_NAMES:
        return EXTRA_NAMES[key][1 if fr else 0]
    return key


def phone_country(raw, form_lang):
    """raw: first 5-8 characters of the phone field. Returns (country key or '', confidence 'sure'/'probable'/'')."""
    s = (raw or "").strip()
    if not s:
        return "", ""
    digits = re.sub(r"\D", "", s)
    if s.startswith("+") or s.startswith("00"):
        d = digits[2:] if s.startswith("00") else digits
        for n in (3, 2, 1):
            if d[:n] in CALLING:
                return CALLING[d[:n]], "sure"
        return "", ""
    if not digits:
        return "", ""
    # no prefix
    if digits[0] == "0" and len(digits) >= 2 and digits[1] in "1234567":
        if form_lang == "fr":
            return "FR", "probable"
        return "", ""
    if digits[0] in "69" or (digits[0] == "7" and len(digits) > 1 and digits[1] in "1234"):
        return "ES", "probable"
    if digits[:3] in CALLING and len(digits) >= 5:
        return CALLING[digits[:3]], "probable"
    if digits[:2] in CALLING and digits[:2] not in ("34",) and len(digits) >= 5:
        return CALLING[digits[:2]], "probable"
    if digits[:2] == "34" and len(digits) >= 5:
        return "ES", "probable"
    if digits[0] == "1":
        return "US/CA", "probable"
    return "", ""


_SELF = (r"(soy|somos|and i |et moi |y yo |both |ambos |nous deux |tous les deux |i am|i'm|we are|we're|je suis|nous sommes|ma nationalite|my nationality|mi nacionalidad|nacionalidad|nationalite|nationality|"
         r"ciudadan[oa]s?|citizen|citoyen|passport|pasaporte|passeport|ressortissant|national of|natural de|originaire|nacido en|born in|ne en|nee en|"
         r"de nationalite|de nacionalidad|of nationality|con nacionalidad|titular de|doble nacionalidad|double nationalite)")
_THIRD = r"(husband|wife|partner|spouse|esposa|esposo|marido|mujer|pareja|novi[oa]|hijo|hija|son\b|daughter|mari\b|epouse|femme|conjoint|compagn|mother|father|madre|padre|brother|hermano|sister|friend|amig[oa]|ami\b|employer|fiance|boyfriend|girlfriend|children|kids|famil|parents|cliente|mon fils|ma fille|my son|my daughter|su pareja)"
_RES = (r"(live in|living in|lives in|reside in|resid(e|ing) in|based in|resido en|vivo en|viviendo en|vivimos en|vivir en|habite (en|au|a)|j'habite|nous habitons|je vis (en|au|a)|resident in|currently in|actuellement (en|au|a)|"
        r"estoy en|estamos en|me encuentro en|se encuentra en|i am in|i'm in|we are in|located in|moved from|vengo de|came from|coming from|from|desde|resident de|residente en|residant en|residant au|domicilie (en|au|a)|"
        r"se trouve (en|au|a)|situe (en|au|a)|currently residing in|currently living in|currently reside in|moving from|relocating from|leaving)")
SPAIN_CITIES = r"valencia|alicante|madrid|barcelona|malaga|torrevieja|denia|javea|benidorm|castellon|murcia|ibiza|mallorca|marbella|sevilla|bilbao|zaragoza|gandia|calpe|altea|moraira|peniscola|oliva|cullera|sagunto|elche|lleida|tarragona|girona|granada|cadiz|valencia"


def _find_all(text, key):
    dem, cty = C[key][3], C[key][4]
    for m in re.finditer(dem, text):
        yield m, "dem"
    for m in re.finditer(cty, text):
        yield m, "cty"


def _closest_cue(pre):
    """Which cue is nearest to the end of `pre`: 'self' (I am / citizen / passport), 'third' (husband, wife...) or ''."""
    best, who = -1, ""
    for m in re.finditer(_SELF, pre):
        if m.end() > best:
            best, who = m.end(), "self"
    for m in re.finditer(_THIRD, pre):
        if m.end() > best:
            best, who = m.end(), "third"
    # a sentence break after the cue cancels it
    if who and re.search(r"[.;!?]", pre[best:]):
        return ""
    return who


def nationality(text, first_person=True):
    """Return (own nationalities, family-member nationalities, all mentioned) as lists of country keys."""
    t = norm(text)
    selfn, fam, ment = [], [], []
    for key in C:
        dem, cty = C[key][3], C[key][4]
        for m in re.finditer(dem, t):
            ment.append(key)
            pre = t[max(0, m.start() - 45):m.start()]
            who = _closest_cue(pre)
            if who == "third":
                fam.append(key)
            elif who == "self":
                selfn.append(key)
        for m in re.finditer(cty, t):
            ment.append(key)
            pre = t[max(0, m.start() - 40):m.start()]
            if re.search(r"(nationalite|nacionalidad|nationality|citizen|ciudadan[oa]|citoyen|ressortissant|passport|pasaporte|passeport|natural de|originaire|national of|nacido en|born in|ne en|nee en)\s*(de |del |of |du |d'|des |:)?\s*$", pre):
                if _closest_cue(pre) == "third":
                    fam.append(key)
                else:
                    selfn.append(key)
    u = lambda x: list(dict.fromkeys(x))
    return u(selfn), u(fam), u(ment)


def residence(text):
    """Country key the writer says they live in / are in (first match), '' if none."""
    t = norm(text)
    for m in re.finditer(_RES + r"\s+(the |a |an |la |le |l'|el |los |les |in |en |au |aux )?", t):
        tail = t[m.end():m.end() + 28]
        if re.match(SPAIN_CITIES, tail):
            return "ES"
        for key in C:
            if re.match(C[key][4], tail):
                return key
    return ""


STOP = {
    "es": r"\b(el|la|los|las|de|que|y|en|un|una|para|con|por|mi|su|soy|estoy|quiero|tengo|buenos|dias|hola|gracias|saludos|necesito|esposa|casa)\b",
    "fr": r"\b(le|la|les|des|de|et|en|un|une|pour|avec|je|mon|ma|suis|bonjour|merci|cordialement|nous|vous|est|dans|sur|que|qui|besoin|souhaite)\b",
    "en": r"\b(the|and|of|to|in|for|with|my|we|our|is|are|am|hello|dear|thank|regards|would|like|have|need|please|that|which|from)\b",
}


def msg_lang(text):
    t = norm(text)
    if re.search(r"[Ѐ-ӿ]", text or ""):
        return "ru"
    if len(t) < 12:
        return ""
    sc = {k: len(re.findall(v, t)) for k, v in STOP.items()}
    best = max(sc, key=sc.get)
    return best if sc[best] >= 2 else ""
