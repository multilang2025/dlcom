"""Lead analysis for delaguialuzon.com contact forms (Formidable Forms, 9 forms, Oct 2024 -> Oct 2026).

Input : a pickle produced from the AISA db_query extracts (raw rows with the message text stay OUTSIDE the repo):
        (rows, journeys) as built by the scratchpad loader; plus data/leads/manual_form10_coding.json.
Output: data/leads/leads_<lang>.csv (derived fields only: no names, e-mails, phones or message text),
        data/leads/leads_stats.json (all numbers used by the report), data/leads/topic_article_map.csv.

Usage : python -X utf8 tools/leads_analysis.py <raw.pkl>
"""
import csv
import html
import json
import pickle
import re
import sys
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import leads_geo as G  # noqa: E402
import leads_taxonomy as X  # noqa: E402
from leads_taxonomy import T, LEAVES, AREAS, norm  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "leads"

WEAK = {"lab_contrato", "lab_salario", "ext_banca", "mer_contratos", "inm_obras", "inm_general", "ext_estudios",
        "suc_litigio", "ext_visado", "ext_instalacion", "mer_autonomo", "fis_inspeccion", "mer_inversion_ext"}
AUX = {"ext_visado", "ext_denegacion", "inm_registro", "mer_contratos", "fis_inspeccion", "suc_litigio", "ext_banca"}  # modifiers: do not make an enquiry "multi-topic" on their own
PRICE = re.compile(r"honorarios|presupuesto|cuanto cuesta|cuanto cobran|precio|tarifa|\bfees?\b|\bprice|\bcost\b|\bcosts\b|\bquote\b|how much|combien|\btarifs?\b|devis|honoraires|\bcout|budget|coste|cobran|cuanto vale")
APPT = re.compile(r"\bcita\b|reunion|llamada|videollamada|videoconferencia|consulta (con|para|online)|una consulta|appointment|meeting|\bcall\b|video ?call|consultation|schedule|rendez.vous|\brdv\b|entretien|disponibilit|availability|disponibilidad|contactar|contact me|contactez|me contacter|ponerse en contacto|llamarme|rappel|rappeler|\bphone\b|whatsapp|zoom|teams")
URGENT = re.compile(r"urgente|urgent|lo antes posible|asap|as soon as|plazo|deadline|cuanto antes|des que possible|le plus tot|expire|caduca|vence|\bdelai|date limite|immediately|inmediat|tomorrow|manana|demain|aujourd|this week|esta semana|cette semaine|time.?sensitive|rapidement|pronto|quickly|rapido")
INFO = re.compile(r"\?|como puedo|como se|how can|how do|how to|what is|what are|que es\b|cuales son|quels sont|quelles sont|comment\b|quiero saber|me gustaria saber|quisiera saber|informacion (sobre|acerca)|information (about|on|regarding)|renseignement|informations? sur|"
                  r"requisitos|requirements|conditions pour|documents (needed|required)|documentos necesarios|pieces (a fournir|necessaires)|dudas?\b|question|puede(n)? (ayudarme|informarme)|could you (please )?(let me know|tell me|advise|inform)|savoir si|saber si|wondering|me preguntaba|i would like to know|j.aimerais savoir|aimerais connaitre")
CLIENT = re.compile(r"necesito un abogado|busco (un )?abogado|quiero contratar|looking for (a |an )?(lawyer|attorney|law firm)|need (a |an )?(lawyer|attorney)|cherche un avocat|besoin d.un avocat|nous cherchons un cabinet|we are seeking (a )?(law|legal)|seeking professional")


def pload(path):
    return pickle.load(open(path, "rb"))


def cleanpath(u):
    u = urllib.parse.unquote((u or "").replace("\\/", "/")).replace("https://delaguialuzon.com", "")
    return u.split("?")[0].rstrip("/") or "/"


AREA_URL = [("EXT", r"immigration|etrangers|extranjeria|иностранц|foreigner|nie\b"), ("FIS", r"tax|fiscal|налог|impot|accounting|contabilidad|fiscalite"),
            ("INM", r"real-estate|immobilier|inmobiliario|недвиж|property"), ("LAB", r"labor|labour|travail|laboral|трудов|employment"),
            ("MER", r"commercial|mercantil|коммерч|business-law|corporate|company"), ("SUC", r"inheritance|succession|sucesion|наследов|civil")]


def page_kind(p):
    if p in ("/", "/en", "/fr", "/ru") or re.fullmatch(r"/(en|fr|ru)", p):
        return "home"
    if re.search(r"contact|контакт", p):
        return "contact"
    if "/blog/" in p or re.search(r"/blog$", p):
        return "blog"
    for a, rx in AREA_URL:
        if re.search(rx, p):
            return "area:" + a
    if re.search(r"equipo|team|equipe|about|nosotros|qui-sommes|cabinet|abogados|avocats", p):
        return "about"
    return "other"


def journey_info(j):
    pages = []
    if j:
        for k in sorted(j):
            v = j[k]
            if isinstance(v, dict) and "url" in v and "wp-admin" not in v["url"]:
                pages.append((cleanpath(v["url"]), v.get("title", ""), v.get("duration") or 0))
    kinds = [page_kind(p[0]) for p in pages]
    blog = [p[0] for p in pages if page_kind(p[0]) == "blog"]
    area = ""
    for k in kinds:
        if k.startswith("area:"):
            area = k[5:]
            break
    first = pages[0][0] if pages else ""
    return dict(n=len(pages), first=first, first_kind=kinds[0] if kinds else "", blog=blog, area=area,
                seconds=sum(int(p[2]) for p in pages if str(p[2]).isdigit()))


def quarter(d):
    return f"{d[:4]}-Q{(int(d[5:7]) - 1) // 3 + 1}"


def classify(text, dd_area, generic_default=None):
    """Return (tags ordered, primary tag). text already normalised."""
    hits = {}
    for code, (leaf, es, fr, rx) in T.items():
        ms = list(rx.finditer(text))
        if not ms:
            continue
        area = LEAVES[leaf][0]
        if code in WEAK and not (len(ms) >= 2 or area == dd_area):
            continue
        score = len(ms) * (0.4 if code in X.BROAD else 1.0) + (0.5 if area == dd_area else 0)
        hits[code] = (score, ms[0].start())
    specific = {c: v for c, v in hits.items() if c not in X.STOP_TAGS and not c.startswith("x_")}
    nonlegal = {c: v for c, v in hits.items() if c.startswith("x_")}
    generic = {c: v for c, v in hits.items() if c in X.STOP_TAGS}
    chosen = specific or generic
    if not chosen and nonlegal:
        chosen = nonlegal
    tags = sorted(chosen, key=lambda c: (-chosen[c][0], chosen[c][1]))
    # drop generic when something specific of the same leaf exists is handled above; keep non-legal tags only if alone
    return tags


def nature(flags, tags, msg_len, has_msg):
    if any(t.startswith("x_comercial") or t.startswith("x_empleo") or t.startswith("x_traduccion") for t in tags[:1]):
        return "ajeno"
    if tags and tags[0] == "x_cliente_actual":
        return "cliente_actual"
    if not has_msg:
        return "sin_mensaje"
    if flags["u"]:
        return "urgente"
    if flags["p"]:
        return "presupuesto"
    if flags["a"]:
        return "cita"
    if flags["i"]:
        return "informacion"
    return "caso_detallado" if msg_len > 500 else "otro"


def main():
    raw, J = pload(sys.argv[1])
    for r in raw:  # strip query strings (ad click ids) from the page; keep a coarse traffic hint
        q = r["page"].partition("?")[2]
        r["traffic_hint"] = ("google_ads" if re.search(r"gclid|gad_source|gbraid|wbraid", q) else "chatgpt" if "chatgpt" in q else "other_utm" if "utm_" in q else "")
        r["page"] = r["page"].partition("?")[0]
    manual = json.load(open(OUT / "manual_form10_coding.json", encoding="utf-8"))["rows"]
    recs = []
    for r in raw:
        text_raw = ((r.get("subject") or "") + " . " + (r.get("message") or "")).strip(" .")
        has_msg = bool(r.get("message"))
        t = norm(text_raw)
        dd = r.get("topic_dropdown") or ""
        dd_area = X.area_of_dropdown(dd) if dd else ("EXT" if r["form_kind"] == "extranjeria" else "")
        if r["form_id"] == 4:
            dd_area = X.area_of_dropdown(dd) or {"auditing and corporate restructuring": "MER"}.get(dd.lower(), "")
        tags = classify(t, dd_area) if has_msg else []
        if r["form_kind"] == "extranjeria" and has_msg and not tags:
            tags = ["ext_general"]
        selfn, famn, ment = G.nationality(text_raw) if has_msg else ([], [], [])
        res = G.residence(text_raw) if has_msg else ""
        pc, conf = G.phone_country(r["phone_prefix"], r["form_lang"])
        flags = dict(p=int(bool(PRICE.search(t))), a=int(bool(APPT.search(t))), u=int(bool(URGENT.search(t))), i=int(bool(INFO.search(t)) or bool(re.search(r"\?", text_raw))))
        recs.append(dict(r, tags=tags, nat=selfn, fam=famn, ment=ment, res=res, pc=pc, pconf=conf, flags=flags, dd_area=dd_area,
                         msg_len=len(r.get("message") or ""), has_msg=has_msg, mlang=G.msg_lang(text_raw) if has_msg else "",
                         client_hint=int(bool(CLIENT.search(t)))))
    # manual form 10
    ex_dates = {m["id"]: m for m in manual}
    for m in manual:
        recs.append(dict(id=m["id"], form_id=10, form_lang="en", form_kind="extranjeria", date=m["date"], page="/en/contact", ctype=None,
                         phone_prefix="", topic_dropdown=None, location_dropdown=m["loc"], subject=None, message="x",
                         tags=m["tags"], nat=m["nat"], fam=m["fam"], ment=[], res=m["res"], pc=m["phone"], pconf="manual" if m["phone"] else "",
                         flags=dict(p=m["p"], a=m["a"], u=m["u"], i=m["i"]), dd_area="EXT", msg_len=0, has_msg=True, mlang=m["lang"], client_hint=0, manual=True))
    # journeys
    for rec in recs:
        rec["jn"] = journey_info(J.get(rec["id"])) if rec["id"] in J else None
    # derive
    for rec in recs:
        tags = rec["tags"]
        leaves = list(dict.fromkeys(T[c][0] for c in tags))
        spec = [c for c in tags if c not in X.STOP_TAGS and not c.startswith("x_")]
        spec_core = [c for c in spec if c not in AUX]
        spec_leaves = list(dict.fromkeys(T[c][0] for c in spec_core))
        rec["leaves"] = leaves
        rec["primary_tag"] = tags[0] if tags else ""
        rec["primary_leaf"] = T[tags[0]][0] if tags else ""
        areas = list(dict.fromkeys(LEAVES[l][0] for l in leaves))
        rec["areas"] = areas
        rec["primary_area"] = LEAVES[rec["primary_leaf"]][0] if rec["primary_leaf"] else (rec["dd_area"] or "")
        rec["multi"] = int(len(spec_leaves) >= 2 or len(spec_core) >= 3)
        rec["multi_area"] = int(len(areas) >= 2)
        # lead country: explicit residence in text > specific dropdown > phone
        loc = rec.get("location_dropdown") or ""
        locmap = {"maroc": "MA", "france": "FR", "canada": "CA", "mali": "ML", "usa": "US", "united states": "US", "albania": "AL", "reino unido": "GB"}
        loc_country = locmap.get(norm(loc).strip(), "")
        if norm(loc).startswith("united states"):
            loc_country = "US"
        country, source = "", ""
        if rec["res"]:
            country, source = rec["res"], "texto"
        elif loc_country:
            country, source = loc_country, "desplegable"
        elif rec["pc"]:
            country, source = rec["pc"], "teléfono"
        rec["country"], rec["country_src"] = country, source
        rec["nature"] = nature(rec["flags"], tags, rec["msg_len"], rec["has_msg"])
        f = rec["flags"]
        commit = f["p"] or f["a"] or f["u"] or rec["client_hint"]
        rec["blog_candidate"] = ""
        if rec["has_msg"] and rec["primary_leaf"] and not rec["primary_leaf"].startswith("OTR"):
            rec["blog_candidate"] = int((f["i"] and not commit) or (rec["msg_len"] and rec["msg_len"] < 180 and not commit))
        if rec.get("manual"):
            rec["blog_candidate"] = int(f["i"] and not (f["p"] or f["a"] or f["u"]))
    write_csv(recs)
    stats = build_stats(recs)
    (OUT / "leads_stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=1), encoding="utf-8")
    article_map()
    print(len(recs), "records;", {k: v for k, v in stats["coverage"].items()})


LANG_FILE = {"es": "leads_es.csv", "en": "leads_en.csv", "fr": "leads_fr.csv", "ru": "leads_ru.csv"}
COLS = ["entry_id", "date", "quarter", "form", "form_language", "form_kind", "client_type", "dropdown_topic", "dropdown_area",
        "page_where_submitted", "traffic_hint", "location_dropdown", "phone_country", "phone_country_confidence", "country_residence_text",
        "lead_country", "lead_country_source", "nationality_stated", "family_nationality", "message_language", "message_chars",
        "primary_area", "primary_leaf", "primary_subtopic", "all_leaves", "all_subtopics", "multi_topic", "combo_label",
        "asks_price", "asks_appointment", "urgent", "information_seeking", "lead_nature", "blog_candidate",
        "journey_pages", "journey_first_page", "journey_area", "blog_posts_read", "analysis_level"]
FORM_NAME = {2: "Form general ES", 4: "General Enquiries", 5: "Formulaire général FR", 6: "Form general RU", 7: "Form pop up RU",
             8: "Form Extranjería", 9: "Форма по вопросам иммиграции", 10: "Immigration Form", 11: "Formulaire d'immigration"}


def write_csv(recs):
    OUT.mkdir(parents=True, exist_ok=True)
    by = defaultdict(list)
    for r in recs:
        by[r["form_lang"]].append(r)
    for lang, rs in by.items():
        rs.sort(key=lambda r: (r["date"], r["id"]))
        with open(OUT / LANG_FILE[lang], "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.writer(fh)
            w.writerow(COLS)
            for r in rs:
                jn = r["jn"] or {}
                combo = ""
                spec = [c for c in r["tags"] if c not in X.STOP_TAGS and not c.startswith("x_")]
                if len(spec) >= 2:
                    combo = " + ".join(T[c][1] for c in spec[:3])
                level = "texto del mensaje" if (r["has_msg"] and (r["message"] or r.get("manual"))) else "solo campos estructurados"
                if r.get("manual"):
                    level = "texto del mensaje (codificado a mano)"
                w.writerow([r["id"], r["date"], quarter(r["date"]), FORM_NAME[r["form_id"]], r["form_lang"], r["form_kind"],
                            r.get("ctype") or "", r.get("topic_dropdown") or "", r["dd_area"], r["page"], r.get("traffic_hint", ""), r.get("location_dropdown") or "",
                            r["pc"], r["pconf"], r["res"], r["country"], r["country_src"], "|".join(r["nat"]), "|".join(r["fam"]),
                            r["mlang"], r["msg_len"] or "", r["primary_area"], r["primary_leaf"], r["primary_tag"], "|".join(r["leaves"]),
                            "|".join(r["tags"]), r["multi"], combo, r["flags"]["p"] if r["has_msg"] else "", r["flags"]["a"] if r["has_msg"] else "",
                            r["flags"]["u"] if r["has_msg"] else "", r["flags"]["i"] if r["has_msg"] else "", r["nature"], r["blog_candidate"],
                            jn.get("n", ""), jn.get("first", ""), jn.get("area", ""), "|".join(jn.get("blog", [])), level])


def top(counter, n=12):
    return [[k, v] for k, v in counter.most_common(n)]


def build_stats(recs):
    S = {}
    langs = ["es", "en", "fr", "ru"]
    S["generated"] = "2026-10-08"
    S["total"] = len(recs)
    S["by_lang"] = {l: sum(1 for r in recs if r["form_lang"] == l) for l in langs}
    S["by_form"] = {FORM_NAME[f]: sum(1 for r in recs if r["form_id"] == f) for f in sorted(FORM_NAME)}
    S["first"], S["last"] = min(r["date"] for r in recs), max(r["date"] for r in recs)
    S["by_quarter"] = {l: dict(sorted(Counter(quarter(r["date"]) for r in recs if r["form_lang"] == l).items())) for l in langs}
    S["by_month"] = dict(sorted(Counter(r["date"][:7] for r in recs).items()))
    # coverage
    text_recs = [r for r in recs if r["has_msg"] and (r["message"] or r.get("manual"))]
    S["coverage"] = dict(text_analysed=len(text_recs), structured_only=len(recs) - len(text_recs),
                         with_phone_country=sum(1 for r in recs if r["pc"]), with_country=sum(1 for r in recs if r["country"]),
                         with_nationality=sum(1 for r in text_recs if r["nat"]), with_journey=sum(1 for r in recs if r["jn"]),
                         with_tags=sum(1 for r in text_recs if r["tags"]))
    S["text_by_lang"] = {l: sum(1 for r in text_recs if r["form_lang"] == l) for l in langs}
    # client type
    S["client_type"] = {l: dict(Counter((r.get("ctype") or "n/d") for r in recs if r["form_lang"] == l and r["form_kind"] == "general")) for l in langs}
    # dropdown area vs reclassified (text-analysed)
    S["dropdown_area"] = {l: dict(Counter(r["dd_area"] or "n/d" for r in recs if r["form_lang"] == l)) for l in langs}
    S["primary_area_text"] = {l: dict(Counter(r["primary_area"] or "n/d" for r in text_recs if r["form_lang"] == l)) for l in langs}
    conf = Counter((r["dd_area"], r["primary_area"]) for r in text_recs if r["form_kind"] == "general" and r["dd_area"])
    S["dropdown_vs_text"] = [[a, b, n] for (a, b), n in conf.most_common(40)]
    # other reclassified
    oth = [r for r in text_recs if r["form_kind"] == "general" and r["dd_area"] == "OTR"]
    S["other_reclassified"] = dict(total=len(oth), by_area=dict(Counter(r["primary_area"] or "n/d" for r in oth)))
    # leaves per language (text analysed + manual) and also with dropdown-only
    S["leaf_by_lang"] = {l: dict(Counter(r["primary_leaf"] or "n/d" for r in text_recs if r["form_lang"] == l)) for l in langs}
    S["leaf_by_lang_all_mentions"] = {l: dict(Counter(lf for r in text_recs if r["form_lang"] == l for lf in r["leaves"])) for l in langs}
    S["tag_by_lang"] = {l: dict(Counter(c for r in text_recs if r["form_lang"] == l for c in set(r["tags"]))) for l in langs}
    S["tag_primary_by_lang"] = {l: dict(Counter(r["primary_tag"] for r in text_recs if r["form_lang"] == l and r["primary_tag"])) for l in langs}
    # tag lift vs overall
    tot_text = len(text_recs)
    overall = Counter(c for r in text_recs for c in set(r["tags"]))
    S["tag_overall"] = dict(overall)
    # multi-topic
    S["multi_topic"] = {l: dict(n=sum(r["multi"] for r in text_recs if r["form_lang"] == l), of=S["text_by_lang"][l],
                                multi_area=sum(r["multi_area"] for r in text_recs if r["form_lang"] == l)) for l in langs}
    combos = Counter()
    combos_l = defaultdict(Counter)
    for r in text_recs:
        sp = [c for c in r["tags"] if c not in X.STOP_TAGS and not c.startswith("x_")]
        for i in range(len(sp)):
            for j in range(i + 1, len(sp)):
                pair = tuple(sorted((sp[i], sp[j])))
                combos[pair] += 1
                combos_l[r["form_lang"]][pair] += 1
    S["combos"] = [[a, b, n] for (a, b), n in combos.most_common(25)]
    S["combos_by_lang"] = {l: [[a, b, n] for (a, b), n in combos_l[l].most_common(10)] for l in langs}
    # country and nationality
    S["country_by_lang"] = {l: top(Counter(r["country"] for r in recs if r["form_lang"] == l and r["country"]), 15) for l in langs}
    S["country_all"] = top(Counter(r["country"] for r in recs if r["country"]), 25)
    S["country_src"] = dict(Counter(r["country_src"] or "none" for r in recs))
    S["country_none_by_lang"] = {l: sum(1 for r in recs if r["form_lang"] == l and not r["country"]) for l in langs}
    S["phone_country_by_lang"] = {l: top(Counter(r["pc"] for r in recs if r["form_lang"] == l and r["pc"]), 12) for l in langs}
    S["nat_by_lang"] = {l: top(Counter(n for r in text_recs if r["form_lang"] == l for n in r["nat"]), 15) for l in langs}
    S["nat_all"] = top(Counter(n for r in text_recs for n in r["nat"]), 30)
    S["fam_nat"] = top(Counter(n for r in text_recs for n in r["fam"]), 15)
    S["nat_stated_n"] = {l: sum(1 for r in text_recs if r["form_lang"] == l and r["nat"]) for l in langs}
    S["msg_lang_by_form_lang"] = {l: dict(Counter(r["mlang"] or "n/d" for r in text_recs if r["form_lang"] == l)) for l in langs}
    S["location_dropdown"] = {l: dict(Counter(r["location_dropdown"] for r in recs if r["form_lang"] == l and r.get("location_dropdown"))) for l in langs}
    # nature
    S["nature_by_lang"] = {l: dict(Counter(r["nature"] for r in recs if r["form_lang"] == l)) for l in langs}
    S["flags_by_lang"] = {l: {k: sum(r["flags"][k] for r in text_recs if r["form_lang"] == l) for k in ("p", "a", "u", "i")} for l in langs}
    S["blog_candidate_by_lang"] = {l: dict(n=sum(1 for r in text_recs if r["form_lang"] == l and r["blog_candidate"] == 1),
                                          of=sum(1 for r in text_recs if r["form_lang"] == l and r["blog_candidate"] != "")) for l in langs}
    bc_leaf = defaultdict(lambda: [0, 0])
    for r in text_recs:
        if r["blog_candidate"] != "":
            bc_leaf[r["primary_leaf"]][1] += 1
            bc_leaf[r["primary_leaf"]][0] += r["blog_candidate"]
    S["blog_candidate_by_leaf"] = {k: v for k, v in bc_leaf.items()}
    S["blog_candidate_by_tag"] = {}
    bc_tag = defaultdict(lambda: [0, 0])
    for r in text_recs:
        if r["blog_candidate"] != "" and r["primary_tag"]:
            bc_tag[r["primary_tag"]][1] += 1
            bc_tag[r["primary_tag"]][0] += r["blog_candidate"]
    S["blog_candidate_by_tag"] = {k: v for k, v in bc_tag.items()}
    # message length
    S["msg_len_median"] = {}
    import statistics
    for l in langs:
        L = [r["msg_len"] for r in recs if r["form_lang"] == l and r["msg_len"]]
        S["msg_len_median"][l] = int(statistics.median(L)) if L else 0
    # trends: tag shares by period (2024-25 vs 2026) among text-analysed, per language
    def period(d):
        return "2024-10..2025-09" if d < "2025-10-01" else ("2025-10..2026-03" if d < "2026-04-01" else "2026-04..2026-10")
    S["periods"] = ["2024-10..2025-09", "2025-10..2026-03", "2026-04..2026-10"]
    S["area_by_period_lang"] = {}
    for l in langs:
        S["area_by_period_lang"][l] = {p: dict(Counter(r["primary_area"] or r["dd_area"] or "n/d" for r in recs if r["form_lang"] == l and period(r["date"]) == p)) for p in S["periods"]}
    S["tag_by_period"] = {p: dict(Counter(c for r in text_recs if period(r["date"]) == p for c in set(r["tags"]))) for p in S["periods"]}
    S["text_by_period"] = {p: sum(1 for r in text_recs if period(r["date"]) == p) for p in S["periods"]}
    # journeys
    jr = [r for r in recs if r["jn"]]
    S["journey"] = dict(n=len(jr), of=len(recs), first_kind=dict(Counter(r["jn"]["first_kind"] or "n/d" for r in jr)),
                        with_blog=sum(1 for r in jr if r["jn"]["blog"]),
                        by_lang={l: dict(n=sum(1 for r in jr if r["form_lang"] == l), blog=sum(1 for r in jr if r["form_lang"] == l and r["jn"]["blog"]),
                                         area=dict(Counter(r["jn"]["area"] or "none" for r in jr if r["form_lang"] == l))) for l in langs})
    bl = Counter(p for r in jr for p in set(r["jn"]["blog"]))
    S["blog_read_top"] = top(bl, 40)
    blk = defaultdict(Counter)
    for r in jr:
        for p in set(r["jn"]["blog"]):
            for c in r["tags"][:2]:
                blk[c][p] += 1
    S["blog_read_by_tag"] = {c: top(cnt, 4) for c, cnt in blk.items()}
    S["first_pages_top"] = top(Counter(r["jn"]["first"] for r in jr), 25)
    S["submit_page"] = {l: top(Counter(r["page"] for r in recs if r["form_lang"] == l), 6) for l in langs}
    # journey area vs dropdown area
    S["journey_area_vs_primary"] = [[a or "none", b or "n/d", n] for (a, b), n in Counter((r["jn"]["area"], r["primary_area"] or r["dd_area"]) for r in jr).most_common(30)]
    # taxonomy for the report
    S["leaves"] = {k: dict(area=v[0], es=v[1], fr=v[2], url=v[3]) for k, v in LEAVES.items()}
    S["areas"] = {k: dict(es=v[0], fr=v[1]) for k, v in AREAS.items()}
    S["tags"] = {c: dict(leaf=v[0], es=v[1], fr=v[2]) for c, v in T.items()}
    S["countries"] = {k: dict(es=G.country_name(k), fr=G.country_name(k, True)) for k in set([r["country"] for r in recs if r["country"]] + [n for r in recs for n in r["nat"] + r["fam"]])}
    # per leaf stats
    leaf_stats = {}
    for lf in LEAVES:
        rs = [r for r in text_recs if lf in r["leaves"]]
        if not rs:
            continue
        leaf_stats[lf] = dict(n=len(rs), primary=sum(1 for r in rs if r["primary_leaf"] == lf),
                              langs=dict(Counter(r["form_lang"] for r in rs)),
                              subtopics=top(Counter(c for r in rs for c in set(r["tags"]) if T[c][0] == lf), 12),
                              blog_candidate=sum(1 for r in rs if r["blog_candidate"] == 1), price=sum(r["flags"]["p"] for r in rs),
                              appt=sum(r["flags"]["a"] for r in rs), urgent=sum(r["flags"]["u"] for r in rs),
                              top_nat=top(Counter(n for r in rs for n in r["nat"]), 4), top_country=top(Counter(r["country"] for r in rs if r["country"]), 4))
    S["leaf_stats"] = leaf_stats

    # ---- derived: lift per language, period shares, coverage gaps
    def share(rs, tag):
        return sum(1 for r in rs if tag in r["tags"]) / len(rs) if rs else 0
    lift = {}
    for l in ("es", "fr"):
        mine = [r for r in text_recs if r["form_lang"] == l]
        other = [r for r in text_recs if r["form_lang"] != l and r["form_lang"] in ("es", "fr")]
        rows_ = []
        for c in T:
            if c.startswith("x_") or c in X.STOP_TAGS:
                continue
            n = sum(1 for r in mine if c in r["tags"])
            if n < 8:
                continue
            s1, s2 = share(mine, c), share(other, c)
            rows_.append([c, n, round(100 * s1, 1), round(100 * s2, 1), round(s1 / s2, 2) if s2 else None])
        lift[l] = sorted(rows_, key=lambda x: -(x[4] or 99))[:10]
    S["lift"] = lift
    S["period_share"] = {}
    for p in S["periods"]:
        rs = [r for r in text_recs if period(r["date"]) == p and r["form_lang"] in ("es", "fr")]
        S["period_share"][p] = {"n": len(rs), "tags": {c: round(100 * share(rs, c), 1) for c in T if not c.startswith("x_") and share(rs, c) > 0}}
    inv = list(csv.DictReader(open(ROOT / "data" / "inventory.csv", encoding="utf-8")))
    posts = defaultdict(dict)
    for code, (leaf, es, fr, rx) in T.items():
        for lang in ("es", "en", "fr"):
            posts[code][lang] = sum(1 for p in inv if p["lang"] == lang and rx.search(norm(html.unescape(p["title"]) + " " + p["slug"].replace("-", " "))))
    S["posts_by_tag"] = posts
    S["tag_langs"] = {c: {l: S["tag_by_lang"][l].get(c, 0) for l in ("es", "fr", "en")} for c in T}
    # sample check: how many text records got no tag
    S["untagged_text"] = {l: sum(1 for r in text_recs if r["form_lang"] == l and not r["tags"]) for l in langs}
    return S


def article_map():
    inv = list(csv.DictReader(open(ROOT / "data" / "inventory.csv", encoding="utf-8")))
    rows = []
    for code, (leaf, es, fr, rx) in T.items():
        if code.startswith("x_"):
            continue
        for lang in ("es", "en", "fr"):
            ms = []
            for p in inv:
                if p["lang"] != lang:
                    continue
                txt = norm(html.unescape(p["title"]) + " " + p["slug"].replace("-", " "))
                if rx.search(txt):
                    ms.append(p)
            ms.sort(key=lambda p: p["modified"], reverse=True)
            rows.append([code, leaf, es, fr, lang, len(ms), " | ".join(f"{p['url']}" for p in ms[:3])])
    with open(OUT / "topic_article_map.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["subtopic", "leaf", "label_es", "label_fr", "blog_language", "matching_posts", "top3_urls"])
        w.writerows(rows)


if __name__ == "__main__":
    main()
