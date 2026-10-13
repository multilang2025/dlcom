"""Taxonomy for the lead analysis: areas and leaves of https://dlvibe.delaguialuzon.fr/ (read 2026-10-08),
plus finer sub-topics ("micro-topics") that match each leaf. Used by tools/leads_analysis.py.

Each micro-topic: code -> (leaf, label_es, label_fr, regex). The regex is applied to accent-stripped, lower-case
text (subject + message), in ES / FR / EN. Russian messages were not read (see the report).
"""
import re
import unicodedata

def norm(s):
    s = (s or "").replace("’", "'").replace("‘", "'").replace("’", "'")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s.lower())


AREAS = {
    "SUC": ("Derecho de sucesiones y litigios", "Droit des successions et contentieux"),
    "INM": ("Derecho inmobiliario", "Droit immobilier"),
    "LAB": ("Derecho laboral y RRHH", "Droit du travail et RH"),
    "MER": ("Derecho mercantil y emprendimiento", "Droit commercial et entrepreneuriat"),
    "FIS": ("Fiscalidad y contabilidad", "Fiscalité et comptabilité"),
    "EXT": ("Instalación y vida en España (extranjería)", "Installation et vie en Espagne (droit des étrangers)"),
    "OTR": ("Otros / no jurídico", "Autres / hors périmètre juridique"),
}

# leaf code -> (area, ES label, FR label, URL path on dlvibe or "" if the leaf does not exist yet)
LEAVES = {
    "SUC-1": ("SUC", "Mediación y resolución de litigios", "Médiation et résolution des litiges", "/derecho-de-sucesiones/mediacion-resolucion-litigios/"),
    "SUC-0": ("SUC", "Herencias y testamentos (propuesta: hoy sin hoja propia)", "Successions et testaments (proposé : pas de page dédiée)", ""),
    "SUC-2": ("SUC", "Derecho de familia: divorcio, custodia (propuesta)", "Droit de la famille : divorce, garde (proposé)", ""),
    "INM-1": ("INM", "Adquisición inmobiliaria y derecho de la propiedad", "Acquisition immobilière et droit de la propriété", "/derecho-inmobiliario/adquisicion-inmobiliaria-derecho-propiedad/"),
    "LAB-1": ("LAB", "Asesoría en derecho laboral y contratación", "Conseil en droit du travail et recrutement", "/derecho-laboral/asesoria-y-contratacion/"),
    "LAB-2": ("LAB", "Asesoramiento en recursos humanos", "Conseil en ressources humaines", "/derecho-laboral/consultoria-de-recursos-humanos/"),
    "LAB-3": ("LAB", "Compliance laboral", "Compliance social", "/derecho-laboral/compliance-laboral-para-empresas/"),
    "LAB-4": ("LAB", "Asesoramiento laboral para empresas", "Conseil social pour entreprises", "/derecho-laboral/asesoramiento-laboral-empresas/"),
    "MER-1": ("MER", "Creación de empresa en España", "Création d'entreprise en Espagne", "/derecho-mercantil/creacion-empresa-espana/"),
    "MER-2": ("MER", "Derecho mercantil y contratos comerciales", "Droit commercial et contrats commerciaux", "/derecho-mercantil/contratos-comerciales/"),
    "MER-3": ("MER", "Auditoría y reestructuración empresarial", "Audit et restructuration d'entreprise", "/derecho-mercantil/auditoria/"),
    "MER-4": ("MER", "Desarrollo de redes de franquicia", "Développement de réseaux de franchise", "/derecho-mercantil/desarrollo-redes-franquicia/"),
    "FIS-1": ("FIS", "Fiscalidad franco-española", "Fiscalité franco-espagnole", "/derecho-fiscal-y-contabilidad/fiscalidad-franco-espanola/"),
    "FIS-2": ("FIS", "Asesoría fiscal en Valencia", "Conseil fiscal à Valence", "/derecho-fiscal-y-contabilidad/servicios-asesoria-fiscal-valencia/"),
    "FIS-3": ("FIS", "Sucesiones y planificación patrimonial", "Successions et planification patrimoniale", "/derecho-fiscal-y-contabilidad/planificacion-patrimonial/"),
    "EXT-1": ("EXT", "Acompañamiento en la instalación administrativa", "Accompagnement à l'installation administrative", "/derecho-de-extranjeria/acompanamiento-instalacion-administrativa/"),
    "EXT-2": ("EXT", "Protección social y jubilación en España", "Protection sociale et retraite en Espagne", "/derecho-de-extranjeria/proteccion-social-jubilacion-espana/"),
    "EXT-3": ("EXT", "Asesoramiento bancario y financiero", "Conseil bancaire et financier", "/derecho-de-extranjeria/asesoramiento-bancario-financiero/"),
    "EXT-4": ("EXT", "Extranjería: residencia, nacionalidad, reagrupación", "Droit des étrangers : résidence, nationalité, regroupement", "/derecho-de-extranjeria/residencia-nacionalidad-reagrupacion/"),
    "OTR-0": ("OTR", "Sin tema jurídico / comercial / empleo", "Hors sujet / démarchage / emploi", ""),
}

# code: (leaf, label_es, label_fr, regex)
T = {}


def _t(code, leaf, es, fr, rx):
    T[code] = (leaf, es, fr, re.compile(rx))


# ---------------------------------------------------------------- EXT-4 extranjería
_t("ext_nie_tie", "EXT-4", "NIE y TIE (tarjeta)", "NIE et TIE (carte)",
   r"\bnie\b|\btie\b|n\.i\.e|tarjeta de identidad de extranjero|numero de identidad de extranjero|numero d.identification")
_t("ext_nomada", "EXT-4", "Nómada digital / teletrabajo internacional", "Nomade numérique / télétravail international",
   r"nomadas? digital(es)?|digital nomads?|nomades? numeriques?|teletrabajo internacional|teletravail international|nomade numerique|remote work visa|\bdnv\b|ley de startups|"
   r"visa.{0,15}teletrabaj|trabajo remoto|remote(ly)? work|travail a distance|teletravail")
_t("ext_no_lucrativa", "EXT-4", "Residencia no lucrativa", "Résidence non lucrative",
   r"no lucrativ|non.?lucrativ|non lucratif|\bnlv\b|sin actividad lucrativa")
_t("ext_inversor", "EXT-4", "Inversor / Golden visa", "Investisseur / Golden visa",
   r"golden visa|visa dorado|visado de inversor|investor visa|visa investisseur|residence par l.investissement|residencia por inversion")
_t("ext_trabajo", "EXT-4", "Residencia y trabajo (cuenta ajena, cualificado)", "Résidence et travail (salarié, qualifié)",
   r"permiso de trabajo|autorizacion de (residencia y )?trabajo|work permit|work visa|permis de travail|autorisation de travail|cuenta ajena|"
   r"highly.qualified|alta cualificacion|hautement qualifie|haute qualification|blue card|tarjeta azul|oferta de trabajo|job offer|offre d.emploi|shortage occupation|"
   r"catalogo de ocupaciones|labour market test|situacion nacional de empleo")
_t("ext_emprendedor", "EXT-4", "Emprendedor / ENISA / startups", "Entrepreneur / ENISA / startups",
   r"emprendedor|entrepreneur|\benisa\b|autorisation entrepreneur|startup|start-up")
_t("ext_estudios", "EXT-4", "Estancia por estudios", "Séjour d'études",
   r"estancia por estudios|visado de estudiante|student visa|student permit|visa etudiant|titre de sejour etudiant|\bestudiante\b|\betudiant|\bstudent\b|master|grado superior|\bmir\b")
_t("ext_arraigo", "EXT-4", "Arraigo (social, laboral, familiar)", "Arraigo (enracinement)", r"arraigo")
_t("ext_reagrupacion", "EXT-4", "Reagrupación familiar / pareja / familiar de comunitario", "Regroupement familial / conjoint / famille d'européen",
   r"reagrupaci|reagrup|regroupement familial|family reunif|reunificacion|reunification|\bdependent|pareja de hecho|unmarried partner|"
   r"familiar de (ciudadano )?(comunitario|ue|europeo)|tarjeta de familiar|ascendiente|descendiente|ressortissant europeen|"
   r"membre de (la )?famille|conjoint d.un|partner.{0,25}(visa|residen)|(visa|residen).{0,25}partner|spouse visa|visa conjoint|bring my (wife|husband|partner|family)")
_t("ext_nacionalidad", "EXT-4", "Nacionalidad española", "Nationalité espagnole",
   r"nacionalidad espanola|(obtener|solicitar|adquirir|acceder a) la nacionalidad|spanish (citizenship|nationality)|citizenship application|"
   r"nationalite espagnole|acquerir la nationalite|acces a la nationalite|naturalisation|naturalizacion|ley de memoria|nietos|demande de nationalite|"
   r"obtain (spanish )?citizenship|obtenir la nationalite|ciudadania espanola")
_t("ext_regularizacion", "EXT-4", "Regularización extraordinaria 2026 (masiva)", "Régularisation extraordinaire 2026 (massive)",
   r"regularizacion (extraordinaria|colectiva|masiva|general|de 2026)|regularisation (extraordinaire|massive|collective|generale|2026)|extraordinary regulari|migrant amnesty|amnest|1 de abril|1er avril|regularizacion extraord|proceso de regularizacion")
_t("ext_asilo", "EXT-4", "Asilo / protección internacional / humanitaria", "Asile / protection internationale / humanitaire",
   r"\basilo|asylum|proteccion internacional|refugi|humanitari|violencia de genero|domestic violence|\basile\b|demandeur d.asile")
_t("ext_renovacion_larga", "EXT-4", "Renovación / residencia de larga duración", "Renouvellement / résident de longue durée",
   r"larga duracion|long.?term residen|renovacion (de )?(la |mi |mis |su )?(tarjeta|tie|residencia|autorizacion|permiso|nie)|renovar (la |mi |mis |su )?(tarjeta|tie|residencia|autorizacion|permiso)|"
   r"renouvellement (de )?(mon |ma |la |du |de )?(titre|carte|sejour|residence)|renouveler (mon |ma |la )?(titre|carte|sejour)|renew(ing|al)? (my |the |our )?(tie|residen|permit|card|visa)|"
   r"prorroga de estancia|residencia permanente|permanent residen|residence permanente|resident de longue duree")
_t("ext_brexit", "EXT-4", "Brexit / Acuerdo de Retirada", "Brexit / Accord de retrait",
   r"brexit|acuerdo de retirada|withdrawal agreement|accord de retrait|article 50|art\.? 50 tue")
_t("ext_visado", "EXT-4", "Visado consular", "Visa consulaire",
   r"visado|\bvisa\b|\bvisas\b|consulat|consulate|embajada|embassy|ambassade|cita previa.{0,20}consul")
_t("ext_denegacion", "EXT-4", "Denegación, recurso, requerimiento", "Refus, recours",
   r"denegaci|denegad|\bdenied\b|\bdenial\b|refus|\brecurso|recours|\bappeal|requerimiento|recurso contencioso|subsanacion")
_t("ext_irregularidad", "EXT-4", "Estancia irregular / overstay / 90 días", "Séjour irrégulier / dépassement / 90 jours",
   r"overstay|exceeded.{0,20}(stay|90)|90 dias|90 days|90 jours|sin papeles|sans papiers|sans titre|expulsion|orden de salida|oqtf|obligation de quitter|irregular|situation irreguliere|ilegal|"
   r"regulariser (ma|sa|mon|notre|leur|ma mere|mon frere|son)|regularisation (de (la |ma |mon |sa )?(situation|titre|carte|sejour|residence)|situation|sejour|residence|administrative)|regularizar (mi |su |la )?situacion|regularizacion (en espana|de (mi |su )?situacion|de residencia)|regularizar mi|regulariser pour|regularisation en espagne")
_t("ext_general", "EXT-4", "Extranjería (consulta general)", "Droit des étrangers (général)",
   r"extranjeria|immigration|inmigracion|inmigrante|immigrer|immigr|residencia|residence permit|residency|titre de sejour|carte de sejour|permis de sejour|permiso de residencia|"
   r"autorisation de sejour|carte de resident|resident permit")
# ---------------------------------------------------------------- EXT-1 instalación
_t("ext_empadronamiento", "EXT-1", "Empadronamiento", "Inscription au padrón",
   r"empadron|\bpadron\b|padron municipal|\bpardon\b|certificat d.inscription|registro municipal|inscription au padron")
_t("ext_sanidad_ss", "EXT-1", "Tarjeta sanitaria / nº Seguridad Social", "Carte de santé / n° de Sécurité sociale",
   r"tarjeta sanitaria|health card|carte vitale|\bsip\b|numero de (la )?seguridad social|numero de securite sociale|social security number|numero de afiliacion|affiliation|"
   r"carte sanitaire|cobertura medica|couverture sante")
_t("ext_carnet", "EXT-1", "Canje del carnet de conducir", "Échange du permis de conduire",
   r"carnet de conducir|permiso de conducir|driving licen|permis de conduire|canje del carnet|echange du permis")
_t("ext_homologacion", "EXT-1", "Homologación / convalidación de títulos", "Équivalence de diplômes",
   r"homologaci|convalidaci|recognition of (my )?(degree|diploma|qualification)|reconnaissance (de|du) diplome|equivalence de diplome")
_t("ext_instalacion", "EXT-1", "Traslado e instalación en España", "Déménagement et installation en Espagne",
   r"relocat|moving to spain|move to spain|move to valencia|moving to valencia|trasladarme|mudarme|instalarme|traslado a espana|me instalo|"
   r"s.installer en espagne|m.installer|installation en espagne|demenager en espagne|venir vivre|venir habiter|vivre en espagne|vivir en espana|"
   r"settle in spain|live in spain|relocation|cambio de residencia a espana|llegada a espana|arrival in spain|set(ting)? up (ourselves|myself)")
# ---------------------------------------------------------------- EXT-2 protección social y jubilación
_t("ext_jubilacion", "EXT-2", "Jubilación, pensiones y prestaciones", "Retraite, pensions et prestations",
   r"jubilaci|jubilad|pension(es)? (de|del|publica|contributiv)|pensionista|retraite|retire(d|ment| to)|\bretiring\b|prestacion(es)? (por|de) desempleo|desempleo|chomage|"
   r"unemployment benefit|convenio de seguridad social|totalizacion|seguridad social espanola|\bcpam\b|\bcnav\b|carriere longue|pension plan|invalidez|incapacidad permanente")
_t("ext_seguro_salud", "EXT-2", "Seguro médico y sanidad", "Assurance santé",
   r"seguro (medico|de salud|privado)|health insurance|private (health )?insurance|assurance (maladie|sante)|mutuelle|\bcmu\b|\bsanidad\b|cobertura sanitaria|\bs1\b|\bef106\b|\bs2\b")
# ---------------------------------------------------------------- EXT-3 banca
_t("ext_banca", "EXT-3", "Cuenta bancaria, transferencias, financiación", "Compte bancaire, virements, financement",
   r"cuenta bancaria|bank account|compte bancaire|abrir una cuenta|open an account|ouvrir un compte|transferencia internacional|international transfer|virement international|"
   r"apertura de cuenta|banco espanol|spanish bank|banque espagnole|iban|financiacion|financement|prestamo|loan\b|pret personnel|transferir dinero|transfer (my )?(money|funds)")
# ---------------------------------------------------------------- INM-1
_t("inm_compra", "INM-1", "Compra de vivienda / inmueble", "Achat de bien immobilier",
   r"comprar (una |un |la |el )?(casa|piso|vivienda|apartamento|inmueble|propiedad|terreno|parcela|local|villa|finca|chalet)|compra de (una |un |la |el )?(casa|piso|vivienda|apartamento|inmueble|propiedad|terreno|parcela|local|villa|finca|chalet)|"
   r"buy(ing)? (a |an |the |my )?(property|house|home|apartment|flat|villa|land|plot|house)|purchase of (a |the )?(property|house|apartment|flat)|property purchase|"
   r"acheter (un |une |le |la )?(bien|maison|appartement|villa|terrain|logement|studio|local|immeuble)|achat (d.un |d.une |de |du |immobilier)|acquisition (immobiliere|d.un bien|d.un appartement|d.une maison)|"
   r"adquisicion (de|del) (inmueble|vivienda|propiedad)|comprar en espana|buy in spain|buying property|compraventa de (vivienda|inmueble)|compromis de vente|arras|contrato de arras|reserva de compra")
_t("inm_venta", "INM-1", "Venta de inmueble", "Vente de bien immobilier",
   r"vender (mi |una |un |la |el )?(casa|piso|vivienda|apartamento|inmueble|propiedad|terreno|local|finca|chalet)|venta de (mi |una |un |la |el )?(casa|piso|vivienda|apartamento|inmueble|propiedad|terreno|local|finca|chalet)|"
   r"sell(ing)? (my |a |the )?(property|house|home|apartment|flat|villa)|vendre (mon |ma |un |une |le |la )?(bien|maison|appartement|villa|terrain|logement)|vente de (mon |ma |ce |cette |un |une |l.)(bien|maison|appartement|villa|terrain|logement|immeuble)|mise en vente")
_t("inm_alquiler", "INM-1", "Alquiler y contrato de arrendamiento", "Location et bail",
   r"alquiler|arrendamiento|arrendador|inquilino|\btenant\b|landlord|\blease\b|rental (contract|agreement)|\brent\b|\bbail\b|locataire|bailleur|louer|locatif|location (meublee|longue|de)|contrato de alquiler|lau\b")
_t("inm_conflicto_arrend", "INM-1", "Impago, desahucio, ocupación ilegal", "Impayés, expulsion, squat",
   r"desahucio|impago|\beviction|unpaid rent|loyers? impaye|moroso|okupa|squatt|ocupacion ilegal|ocupantes|occupation illegale|expulsion du locataire|inquiokupa")
_t("inm_comunidad", "INM-1", "Comunidad de propietarios", "Copropriété",
   r"comunidad de propietarios|community of owners|copropri|syndic\b|junta de propietarios|homeowners|derrama|cuota de comunidad|charges de copropriete")
_t("inm_turistico", "INM-1", "Vivienda turística / alquiler vacacional", "Location touristique",
   r"vivienda turistica|alquiler turistico|licencia turistica|tourist (rental|licen|let)|airbnb|location saisonniere|meuble de tourisme|\bvut\b|alquiler vacacional|holiday (let|rental)|short.?term rental|registro unico de alquileres|alquiler de temporada")
_t("inm_hipoteca", "INM-1", "Hipoteca / crédito inmobiliario", "Crédit immobilier / hypothèque",
   r"hipotec|mortgage|pret immobilier|credit immobilier|emprunt immobilier|cancelacion de hipoteca")
_t("inm_obras", "INM-1", "Obras, licencias y urbanismo", "Travaux, permis et urbanisme",
   r"licencia de obra|urbanis|building permit|permis de construire|reforma de|renovation|construccion|construction|defecto|promotor|constructor|cedula de habitabilidad|catastro|cadastre|ibi\b|planning permission|licencia de primera ocupacion|\bobras\b|travaux")
_t("inm_registro", "INM-1", "Escritura, notaría y registro de la propiedad", "Acte notarié et registre foncier",
   r"escritura|notari|registro de la propiedad|land registry|title deed|acte notarie|titre de propriete|nota simple|cargas|embargo|servidumbre|lindero|due diligence inmobiliaria|verificacion (de )?titulo|conservation des hypotheques")
_t("inm_general", "INM-1", "Inmobiliario (consulta general)", "Immobilier (général)",
   r"appartements?|appart|maison|villa|inmobiliari|inmueble|vivienda|propiedad en espana|property in spain|real estate|immobilier|bien en espagne|villa|apartment in|apartamento en|piso en|casa en|maison en espagne|appartement en espagne|\bterreno\b|parcela|finca")
# ---------------------------------------------------------------- SUC
_t("suc_herencia", "SUC-0", "Herencia, testamento y declaración de herederos", "Succession, testament et dévolution",
   r"herencia|heredero|testamento|sucesion|inheritance|\bprobate\b|\bsuccession|heritage|heritier|testament|legs\b|declaracion de herederos|usufructo|usufruit|quotite|reserve hereditaire|"
   r"reglamento .{0,15}sucesiones|reglement .{0,10}successions|notaire.{0,20}succession|fallecimiento|fallecido|deces|decede|deceased|heir\b|last will|my will\b|a will\b|the will\b|will and testament|estate of|partage|particion|legitima|\bcausante|fallecio|murio|falleci|died|passed away|le defunt|defunt")
_t("suc_litigio", "SUC-1", "Litigio, reclamación y mediación", "Litige, réclamation et médiation",
   r"demanda\b|litigio|litige|tribunal|juzgado|procedimiento judicial|lawsuit|\bsue\b|dispute|disputa|reclamacion|reclamation|arbitraje|arbitrage|mediaci|mediation|conflicto|"
   r"avocat pour un proces|proces\b|court case|legal action|accion legal|demandar|poursuites|assignation|huissier|\bprocurador|monitorio|sentencia|jugement|recouvrement|impagado|unpaid invoice|facture impayee|cobro de deuda|debt recovery|recuperar (el )?dinero|scam|estafa|arnaque|fraud|fraude")
_t("suc_familia", "SUC-2", "Familia: divorcio, custodia, régimen matrimonial", "Famille : divorce, garde, régime matrimonial",
   r"divorcio|divorce|separacion matrimonial|custodia|pension alimenticia|pension alimentaire|garde (des |de l.)?enfant|regimen economico matrimonial|regime matrimonial|capitulaciones|prenup|matrimonio|marriage|mariage|child custody|hijos menores")
_t("suc_penal", "SUC-1", "Penal / penal económico", "Pénal / pénal des affaires",
   r"derecho penal|penal economico|criminal (law|case|charge|record)|delito|infraction penale|plainte|denuncia|police report|detenido|arrest|garde a vue|casier judiciaire|antecedentes penales(?! de)|lavado de dinero|blanchiment|money laundering")
# ---------------------------------------------------------------- FIS
_t("fis_sucesiones_impuesto", "FIS-3", "Impuesto de sucesiones y donaciones", "Droits de succession et donation",
   r"impuesto de sucesiones|inheritance tax|droits de succession|impuesto de donaciones|gift tax|droits de donation|impuesto sobre sucesiones|donacion|donation|plusvalia mortis|\bisd\b")
_t("fis_planificacion", "FIS-3", "Planificación patrimonial y holding", "Planification patrimoniale et holding",
   r"planificacion patrimonial|estate planning|wealth planning|planification patrimoniale|gestion de patrimoine|holding|pacto sucesorio|trust\b|fideicomiso|assurance.vie|seguro de vida|optimisation fiscale|optimizacion fiscal|tax planning|planificacion fiscal|patrimonio familiar|societe patrimoniale|sociedad patrimonial")
_t("fis_convenio_doble", "FIS-1", "Convenio de doble imposición / residencia fiscal", "Convention fiscale / résidence fiscale",
   r"doble imposicion|double taxation|double imposition|convenio (fiscal|de doble)|convention fiscale|tax treaty|residencia fiscal|tax residen|residence fiscale|residente fiscal|centro de intereses|foyer fiscal|domicile fiscal|exit tax|"
   r"183 d|183 days|183 jours|residente en francia|resident en france|impots en france|impuestos en francia|fiscalite franco|franco.?espagnol|franco.?espanol|france et espagne|francia y espana")
_t("fis_irpf", "FIS-2", "Declaración de la renta (IRPF)", "Déclaration de revenus (IRPF)",
   r"declaracion de la renta|\birpf\b|income tax|impot sur le revenu|declaration (de )?revenus?|modelo 100|tax return|declaration fiscale|declaration d.impots|declarar (mis )?ingresos|declarar la renta|declarar mis|presentar (la )?declaracion|file (my )?taxes|tax filing")
_t("fis_no_residente", "FIS-2", "No residentes (Modelo 210 / IRNR)", "Non-résidents (Modèle 210 / IRNR)",
   r"no residente|non.?resident|nonresident|modelo 210|\bmodelo210\b|\birnr\b|propietario no residente|rentas de no residentes|impot des non.?residents|non-residents tax")
_t("fis_beckham", "FIS-2", "Régimen Beckham (impatriados)", "Régime Beckham (impatriés)",
   r"beckham|impatriad|regimen especial de desplazados|inbound (expatriate|regime)|expatriate regime|regime des impatries|regimen de impatriados|ley beckham")
_t("fis_patrimonio_720", "FIS-2", "Patrimonio, Modelo 720/721, bienes en el extranjero", "Patrimoine, Modèle 720/721, avoirs à l'étranger",
   r"modelo 720|\b720\b|modelo 721|bienes en el extranjero|assets abroad|biens a l.etranger|impuesto sobre el patrimonio|wealth tax|impot sur la fortune|\bisf\b|\bifi\b|solidaridad de las grandes fortunas|\bigf\b|foreign asset|declaracion de bienes|cuentas en el extranjero|comptes a l.etranger")
_t("fis_plusvalia", "FIS-2", "Plusvalías y retención del 3 %", "Plus-values et retenue de 3 %",
   r"plusvalia|capital gain|plus.?value|ganancia patrimonial|retencion (del )?3|retenue de 3|3% (withholding|retention)|impuesto de plusvalia municipal|gain en capital")
_t("fis_cripto", "FIS-2", "Criptomonedas", "Cryptomonnaies",
   r"cripto|crypto|bitcoin|ethereum|\bnft\b|binance|coinbase")
_t("fis_inspeccion", "FIS-2", "Requerimiento, inspección o sanción de Hacienda", "Contrôle, requête ou pénalité fiscale",
   r"regularisation fiscale|regularizacion fiscal|regularizar.{0,30}(hacienda|impuestos|fiscal)|regulariser.{0,30}(impots|fiscal|revenus)|requerimiento de hacienda|notificacion de hacienda|inspeccion (de )?hacienda|inspeccion fiscal|sancion tributaria|agencia tributaria|\baeat\b|\bhacienda\b|redressement|controle fiscal|tax audit|\bcarta de hacienda|recargo|prescripcion tributaria|paralela|declaracion complementaria|tax authorit|fisc\b|\bdgfip\b|impots\.gouv|tax notice")
_t("fis_iva_conta", "FIS-2", "IVA, contabilidad, gestoría e impuesto de sociedades", "TVA, comptabilité, gestion et IS",
   r"\biva\b|\bvat\b|\btva\b|contabilidad|comptabilit|accounting|bookkeeping|gestoria|modelo 303|modelo 130|libros contables|cuentas anuales|impuesto (de|sobre) sociedades|corporate tax|impot sur les societes|facturaci|facturation|\binvoic|verifactu|expert.?comptable|accountant|contable|contador|annual accounts|\bcomptes annuels|bilan")
_t("fis_general", "FIS-2", "Fiscalidad (consulta general)", "Fiscalité (général)",
   r"\bimpuestos?\b|\btax(es|ation)?\b|fiscal|fiscalidad|fiscalite|tributa|\bimpots?\b|tributar|asesoria fiscal|conseil fiscal|taxation|taxable|haciendas?\b")
# ---------------------------------------------------------------- MER
_t("mer_creacion", "MER-1", "Crear una sociedad / abrir un negocio", "Créer une société / ouvrir une activité",
   r"crear (una |mi |nuestra )?(empresa|sociedad|compania|negocio)|constituir|constitucion de (una |la )?sociedad|abrir (una |mi )?(empresa|sociedad|negocio|sucursal|local)|company (formation|creation|setup|set up|registration)|"
   r"(set up|setting up|open|opening|start|starting|form|forming|register|registering|incorporate|incorporating) (a |an |my |our )?(new )?(company|business|llc|limited|ltd|entity|corporation|subsidiary|branch|firm)|"
   r"creation d.(une )?(entreprise|societe)|creer (une |ma |notre )?(societe|entreprise|sas|sarl|activite)|immatriculation|sociedad limitada|\bs\.?l\.?u?\b|\bsarl\b|\bsas\b|\bsasu\b|start.?up|creation de societe|"
   r"monter (une |ma |notre )?(societe|entreprise)|ouvrir (une |ma |notre )?(societe|entreprise|activite|succursale)|ouverture de (societe|compte professionnel)|apertura de negocio|capital social|objeto social|negocio en espana|empresa en espana|entreprise en espagne|business in spain|company in spain|societe en espagne")
_t("mer_autonomo", "MER-1", "Alta de autónomo / freelance / auto-entrepreneur", "Statut d'autónomo / indépendant / auto-entrepreneur",
   r"autonomo|self.?employed|freelanc|auto.?entrepreneur|micro.?entrepreneur|travailleur independant|trabajador por cuenta propia|\breta\b|tarifa plana|cuota de autonomo|alta de autonomo|alta en hacienda|modelo 036|modelo 037|\biae\b|\bllc\b|sole (proprietor|trader)|independent contractor|liberal profession|profesional liberal|profession liberale|\bcontractor\b")
_t("mer_inversion_ext", "MER-1", "Implantación / inversión extranjera en España", "Implantation / investissement en Espagne",
   r"inversion extranjera|foreign investment|investissement etranger|invest in spain|invertir en espana|investir en espagne|establecimiento permanente|permanent establishment|sucursal|succursale|filial|subsidiary|market entry|implantation|desarrollar (mi |nuestro )?negocio en espana|expand(ing)? to spain|expansion en espagne|expandir")
_t("mer_contratos", "MER-2", "Contratos mercantiles y de distribución", "Contrats commerciaux et de distribution",
   r"contrato (mercantil|comercial|de distribucion|de agencia|de suministro|de servicios|de colaboracion|de franquicia)|contrat (commercial|de distribution|d.agent|de fourniture|de prestation|de collaboration)|commercial contract|distribution agreement|agencia comercial|"
   r"pacto de socios|shareholder.?s? agreement|pacte d.associes|condiciones generales|terms and conditions|conditions generales|\bcgv\b|\bcgu\b|\bnda\b|confidentialidad")
_t("mer_compraventa_empresa", "MER-2", "Compraventa de empresa / participaciones / due diligence", "Cession d'entreprise / parts / due diligence",
   r"compraventa de (una )?(empresa|sociedad|participaciones|acciones)|acquisition of (a )?(company|business|shares)|share purchase|cession de (parts|titres|fonds)|cesion de participaciones|due diligence|rachat d.entreprise|reprise d.entreprise|comprar (una )?empresa|vender (mi |una )?empresa|fusion|merger|\bm&a\b|traspaso")
_t("mer_pi_rgpd", "MER-2", "Marca, propiedad intelectual, RGPD", "Marque, propriété intellectuelle, RGPD",
   r"\bmarca\b|trademark|propiedad intelectual|intellectual property|brevet|\bpatent|rgpd|gdpr|proteccion de datos|data protection|protection des donnees|copyright|derechos de autor|droit d.auteur|\bmarque\b|\blopd")
_t("mer_concurso", "MER-3", "Insolvencia, concurso y reestructuración", "Insolvabilité, redressement et restructuration",
   r"concurso de acreedores|insolvenc|bankruptcy|faillite|liquidation|redressement judiciaire|pre.?concurso|reestructuraci|restructuring|restructuration|\bauditor|\baudit\b|auditoria|disolucion|dissolution|cierre de (la )?(empresa|sociedad)|liquidar|segunda oportunidad|second chance|redressement|cessation de paiements|dissoudre")
_t("mer_franquicia", "MER-4", "Franquicia", "Franchise", r"franquicia|franchis")
# ---------------------------------------------------------------- LAB
_t("lab_despido", "LAB-1", "Despido, finiquito e indemnización", "Licenciement, solde de tout compte et indemnités",
   r"despido|despedid|dismissal|licenciement|licencie|\bfired\b|rupture conventionnelle|finiquito|indemnizacion por despido|severance|preaviso|carta de despido|dimision|resignation|demission|\bere\b|\berte\b|redundan|indemnite de licenciement|termination of (my )?(employment|contract)|terminated")
_t("lab_contrato", "LAB-1", "Contrato de trabajo, convenio, jornada y vacaciones", "Contrat de travail, convention, temps de travail",
   r"contrato de trabajo|employment contract|contrat de travail|contratar|contratacion|\bhiring\b|\bhire\b|embauche|embaucher|empleado|employee|salarie|periodo de prueba|trial period|periode d.essai|convenio colectivo|collective agreement|convention collective|jornada|horas extra|overtime|heures supplementaires|vacaciones|conges payes|labor law|derecho laboral|droit du travail|employment law|employer|empleador|employeur")
_t("lab_salario", "LAB-1", "Nóminas, impago de salarios, reclamaciones", "Salaires impayés, réclamations",
   r"nomina|payroll|paie\b|impago de salario|salario|salary|sueldo|salaire|reclamar (mi )?(salario|sueldo)|atrasos|unpaid wages|wages")
_t("lab_accidente_baja", "LAB-1", "Accidente laboral, baja médica, incapacidad", "Accident du travail, arrêt maladie, invalidité",
   r"accidente de trabajo|accident du travail|baja medica|incapacidad temporal|arret maladie|sick leave|work accident|enfermedad profesional|maladie professionnelle|\bmutua\b|incapacite|baja laboral")
_t("lab_acoso", "LAB-1", "Acoso o discriminación laboral", "Harcèlement ou discrimination au travail",
   r"acoso laboral|acoso|harassment|harcelement|mobbing|discrimin")
_t("lab_rrhh", "LAB-2", "Recursos humanos (reclutamiento, políticas de personal)", "Ressources humaines (recrutement, politiques)",
   r"recursos humanos|human resources|ressources humaines|\brrhh\b|\brh\b|\bhr\b|reclutamiento|recruitment|recrutement|politica de personal|plan de carrera|evaluacion de desempeno|teletrabajo en la empresa|remote work policy")
_t("lab_compliance", "LAB-3", "Compliance laboral (igualdad, canal de denuncias, registro horario)", "Compliance social (égalité, alerte, temps de travail)",
   r"plan de igualdad|equality plan|registro horario|time tracking|canal de denuncias|whistleblow|lanceur d.alerte|prevencion de riesgos|riesgos laborales|protocolo de acoso|compliance|cumplimiento normativo|code de conduite")
_t("lab_empresa", "LAB-4", "Asesoría laboral para empresas (altas, desplazados, inspecciones)", "Conseil social entreprise (affiliations, détachés, inspections)",
   r"asesoria laboral|labour advice|labor advice|conseil social|inspeccion de trabajo|labour inspection|inspection du travail|trabajador extranjero|contratar a un extranjero|hire a foreign|embaucher un etranger|trabajadores desplazados|travailleur detache|detache|posted worker|certificado a1|formulario a1|\ba1\b|seguridad social de (la )?empresa|alta de trabajador|cotizaciones de (los )?trabajadores|entreprise.{0,20}salaries.{0,20}espagne|empresa.{0,25}empleados")
# ---------------------------------------------------------------- non-legal
_t("x_comercial", "OTR-0", "Oferta comercial / publicidad recibida", "Démarchage commercial reçu",
   r"\bseo\b|posicionamiento web|we offer|nous proposons|ofrecemos|our services|digital agency|web design|diseno web|backlink|guest post|link building|propuesta comercial|business proposal|webinar|sponsor|publicidad|advertis|loan offer|\bvpn\b|software|app development|lead generation|marketing digital|growth hacking|redes sociales")
_t("x_empleo", "OTR-0", "Candidatura / búsqueda de empleo en el despacho", "Candidature / recherche d'emploi au cabinet",
   r"oferta de empleo|\bjob\b|busco trabajo|trabajar en su despacho|trabajar con ustedes|practicas|internship|\bstage\b|curriculum|\bcv\b|candidature|candidatura|vacante|looking for a job|work (for|at) your (firm|company)|travailler (chez vous|dans votre cabinet)|posicion abierta|offre de stage")
_t("x_traduccion", "OTR-0", "Traducciones (jurada, documentos)", "Traductions (assermentée, documents)",
   r"traduccion jurada|sworn translation|traduction assermentee|traductor|translator|traducteur|traduccion de|translation of|traduction de|apostilla|apostille|legalizacion de documentos|legalisation")
_t("x_cliente_actual", "OTR-0", "Seguimiento de expediente / cliente actual", "Suivi de dossier / client existant",
   r"mi expediente|numero de expediente|expediente\b|mon dossier|suivi|follow.?up|status of my|estado de mi|ya soy cliente|ya somos clientes|deja client|existing client|current client|already (a )?client|nuestro expediente|our case file|my case file")

# ---------------------------------------------------------------- extra alternatives found while checking untagged messages
# (RU stems are written in normalised form: lower case, no diacritics, "й" -> "и")
EXTRA = {
    "ext_nie_tie": r"\bcue\b|certificado de registro de ciudadano|cita previa|rendez.vous (a la )?prefecture|nie\b.{0,20}cita",
    "ext_nomada": r"teletrabajo|teletravaill|travail a distance|remote worker|trabajar en remoto|для удаленной|удаленн\w+ работ",
    "ext_regularizacion": r"регуляриз|regularisation generale|regularisation massive",
    "ext_nacionalidad": r"nacionalidad (francesa|britanica|inglesa|alemana|italiana)|nationalite (francaise|britannique|italienne|allemande)|гражданств|naturalisation francaise|double nationalite",
    "ext_visado": r"виз[аыуе]\b|визов",
    "ext_general": r"residence en espagne|une residence|residir en|resident en espagne|residente\b|resident\b|residencia en espana|вид на жительство|внж|резиденц|иммиграц|иностранц|permis de sejour|sejour en espagne|sejour d|ma situation administrative|situacion administrativa|papeles",
    "ext_renovacion_larga": r"пмж|постоянн\w+ вид на жительство|постоянн\w+ проживан",
    "ext_instalacion": r"expatri|passer .{0,12}annees? en espagne|passer .{0,12}ans en espagne|vivre a valence|vivre a valencia|s.etablir en espagne|etablir en espagne|переезд|переехать",
    "ext_jubilacion": r"pension (de )?(viud|jubil|reversion|vejez)|viudedad|reversion|pensione|пенси",
    "ext_banca": r"cuenta en un banco|prelevement|banco\b|bancaire",
    "ext_sanidad_ss": r"\bcaf\b|allocations? familiales|prestations? sociales|pole emploi|france travail|securite sociale francaise|\bcpam\b|\bmsa\b",
    "inm_compra": r"projet d?.?achat|achat appart|achat d.appart|achat maison|achat terrain|acquerir|acquisition d.un|investir (dans|en) (un|une)|offre d.achat|residence secondaire|offer on|comprar un piso|piso (visto )?para comprar|tengo un piso|купить|покупк\w+ (квартир|дом|недвижим)|achete (un|une)|j.ai (achete|trouve) (un|une)|promesse de vente|compromiso de compra",
    "inm_venta": r"vente d.un|продаж\w+ (квартир|дом|недвижим)|продать",
    "inm_comunidad": r"plaza de garaje|plaza de aparcamiento|vecin[oa]s?\b|voisin|garaje|trastero|ruidos|goteras|filtracion",
    "inm_general": r"недвижим|квартир|\bдом\b",
    "inm_registro": r"procedimiento judicial.{0,30}piso|piso.{0,40}proceso judicial",
    "suc_herencia": r"наследств|завещан|heredar|hereditaire|succession",
    "suc_litigio": r"contentieux|amendes?\b|\bmultas?\b|echeancier|diffamation|calomnia|abus de pouvoir|menace[sr]?\b|amenaza|\bsuite a un accident|accident de la route|accidente de trafico|peritaje|cese colectivo|судебн|\bиск\b|спор",
    "suc_familia": r"adoption|adopcion|filiation|paternidad|pacs\b|union libre|nous marier|me marier|casarme|nos casamos|boda|get(ting)? married|разво",
    "fis_irpf": r"declaraciones? de (la )?renta|declarations? (de )?(renta|revenus|impots)|renta francesa|declaracion francesa|declaraciones atrasadas|annees anterieures|ejercicios anteriores|prior.year returns|декларац",
    "fis_no_residente": r"formulaire 210|formulario 210|form 210|\b210\b|modele 210",
    "fis_general": r"налог",
    "fis_iva_conta": r"cuentas de la empresa|bilan comptable|liasse fiscale|expert comptable|ooo\b",
    "mer_creacion": r"creacion de (una )?(empresa|sociedad)|constitucion de (una )?empresa|creer .{0,25}(entreprise|societe)|creation d.entreprise|nominee|nominal director|open an? (company|business)|sociedad en espana|dvp de mon entreprise|developper mon entreprise|developpement de mon entreprise|eurl|открыт\w+ (фирм|компани|бизнес)|создан\w+ (фирм|компани)|регистраци\w+ (компани|фирм)|фирм\w+ в испании|ouvrir une societe|monter une affaire|abrir una sociedad|abrir un negocio",
    "mer_contratos": r"sales agreement|purchase agreement|contrat de vente|contrato de compraventa|contrato de venta|draft(ing)? (a|an) (contract|agreement)|redactar un contrato|rediger un contrat|contrat de prestation|договор",
    "mer_franquicia": r"franchis",
    "lab_accidente_baja": r"baja por|de baja\b|en baja\b|arret de travail|arret maladie|bajas? medic|больничн",
    "lab_contrato": r"droits? (au|du) travail|droit social|derechos laborales|mes droits en tant que salarie|nos droits au travail|труд|работодател|увольн|prud.?hom",
    "lab_despido": r"cese colectivo|despidos? colectivo|увольн",
    "x_empleo": r"ser parte de su equipo|equipo juridico|unirme a su equipo|join your team|joindre votre equipe|integrer votre equipe|travailler dans une entreprise|demande de travail|demande d.emploi|cherche un emploi|chercher du travail|busco empleo|busco trabajo|je cherche (un )?(travail|emploi)|asistente juridico|paralegal|looking for work|find work in spain|trouver du travail|pasantia|becario|stagiaire",
    "x_cliente_actual": r"suite a votre mail|suite a votre appel|votre mail du|su correo del|your email of|following your email|segun nuestra conversacion|following our (call|conversation)|as discussed",
    "x_comercial": r"search results|keywords|top of (google|search)|first page of google|google ranking|traffic|backlinks?|we help (companies|businesses)|boost your|increase your (sales|traffic|revenue)|mejorar su posicionamiento|primera pagina de google|nous sommes une (entreprise|societe|agence)|we are a (company|agency)|somos una (empresa|agencia)|sourcing|fournisseur|proveedor|supplier|exportation|importation|import.export|cotizacion de",
}
for _code, _extra in EXTRA.items():
    _leaf, _es, _fr, _rx = T[_code]
    T[_code] = (_leaf, _es, _fr, re.compile(_rx.pattern + "|" + norm(_extra)))
# Tags too broad to be the *primary* topic when something more specific is present (score x0.4)
BROAD = {"ext_visado", "ext_denegacion", "suc_litigio", "fis_iva_conta", "fis_inspeccion", "mer_contratos", "inm_registro", "ext_instalacion",
         "ext_empadronamiento", "ext_renovacion_larga", "ext_banca", "ext_seguro_salud", "ext_sanidad_ss"}

STOP_TAGS = {"ext_general", "fis_general", "inm_general"}  # generic fall-backs, only used when nothing specific matches

DROPDOWN_AREA = {
    # ES
    "derecho fiscal": "FIS", "derecho de extranjeria": "EXT", "derecho inmobiliario": "INM", "derecho laboral": "LAB",
    "derecho civil y sucesiones": "SUC", "derecho penal economico": "SUC", "derecho mercantil": "MER", "otro(s)": "OTR",
    # FR
    "droit des etrangers": "EXT", "autre(s)": "OTR", "droit fiscal": "FIS", "droit immobilier": "INM",
    "droit civil et droit des successions": "SUC", "audit et restructuration des entreprises": "MER",
    "audit et restructuration d'entreprise": "MER", "droit commercial": "MER", "droit du travail": "LAB",
    "droit penal economique": "SUC", "developpement de reseaux de franchise": "MER", "gestion des ressources humaines": "LAB",
    # EN
    "tax law": "FIS", "immigration law": "EXT", "real estate law": "INM", "civil and inheritance law": "SUC",
    "labour law": "LAB", "labor law": "LAB", "employment law": "LAB", "commercial law": "MER", "business law": "MER",
    "corporate law": "MER", "other(s)": "OTR", "other": "OTR", "criminal law": "SUC", "economic criminal law": "SUC",
    "audit and restructuring": "MER", "franchise development": "MER", "human resources": "LAB",
    "audit and business restructuring": "MER", "franchise network development": "MER", "human resources management": "LAB",
}
DROPDOWN_RU = {"налоговое право": "FIS", "иммиграционное право": "EXT", "трудовое право": "LAB", "коммерческое право": "MER",
               "законодательство о недвижимости": "INM", "гражданское и наследственное право": "SUC", "другое (-ие)": "OTR"}


def area_of_dropdown(v):
    n = norm(v).strip()
    if n in DROPDOWN_AREA:
        return DROPDOWN_AREA[n]
    return DROPDOWN_RU.get((v or "").strip().lower(), "")
