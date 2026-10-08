"""Compact data set for the bilingual lead report (reads data/leads/leads_stats.json + the per-language CSVs).
Writes data/leads/report_data.json. Contains aggregates only.

Usage: python -X utf8 tools/leads_report_data.py
"""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data" / "leads"
S = json.loads((D / "leads_stats.json").read_text(encoding="utf-8"))
L = ["es", "en", "fr", "ru"]

rows = []
for l in L:
    for r in csv.DictReader(open(D / f"leads_{l}.csv", encoding="utf-8-sig")):
        r["lang"] = l
        rows.append(r)


def cnt(f, pred=lambda r: True):
    return Counter(f(r) for r in rows if pred(r))


R = {}
R["meta"] = dict(total=S["total"], first=S["first"], last=S["last"], by_lang=S["by_lang"], text_by_lang=S["text_by_lang"],
                 by_form=S["by_form"], coverage=S["coverage"], generated=S["generated"])
R["quarters"] = S["by_quarter"]
# client type normalised
norm_ct = {"Particular": "p", "Private": "p", "Particulier": "p", "Частный клиент": "p", "Empresa": "c", "Company": "c", "Entreprise": "c", "Компания": "c"}
R["client"] = {l: dict(Counter(norm_ct.get(k, "n") for k, v in S["client_type"][l].items() for _ in range(v))) for l in L}
R["nature"] = S["nature_by_lang"]
R["flags"] = S["flags_by_lang"]
R["blog_candidate"] = S["blog_candidate_by_lang"]
R["blog_candidate_leaf"] = S["blog_candidate_by_leaf"]
R["multi"] = S["multi_topic"]
R["msg_len_median"] = S["msg_len_median"]
R["msg_lang"] = S["msg_lang_by_form_lang"]
# countries
cn = S["countries"]
R["country_names"] = cn
abroad = {}
for l in L:
    c = Counter(r["lead_country"] for r in rows if r["lang"] == l and r["lead_country"])
    tot = sum(c.values())
    es = c.get("ES", 0)
    abroad[l] = dict(with_country=tot, spain=es, other=tot - es, none=sum(1 for r in rows if r["lang"] == l and not r["lead_country"]))
R["country_split"] = abroad
R["country_by_lang"] = S["country_by_lang"]
R["country_src"] = S["country_src"]
R["nat_by_lang"] = S["nat_by_lang"]
R["nat_n"] = S["nat_stated_n"]
R["nat_all"] = S["nat_all"]
R["fam_nat"] = S["fam_nat"]
R["location_dd"] = S["location_dropdown"]
# areas
R["areas"] = S["areas"]
R["dropdown_area"] = S["dropdown_area"]
R["text_area"] = S["primary_area_text"]
R["other_reclassified"] = S["other_reclassified"]
R["dropdown_vs_text"] = S["dropdown_vs_text"]
R["area_period"] = S["area_by_period_lang"]
R["periods"] = S["periods"]
# tags
R["tags"] = S["tags"]
R["tag_langs"] = S["tag_langs"]
R["tag_overall"] = S["tag_overall"]
R["tag_primary"] = S["tag_primary_by_lang"]
R["lift"] = S["lift"]
R["period_share"] = S["period_share"]
R["posts_by_tag"] = S["posts_by_tag"]
R["leaves"] = S["leaves"]
R["leaf_stats"] = S["leaf_stats"]
R["combos"] = S["combos"]
R["combos_by_lang"] = S["combos_by_lang"]
R["journey"] = S["journey"]
R["blog_read_top"] = S["blog_read_top"]
R["first_pages_top"] = S["first_pages_top"]
R["submit_page"] = S["submit_page"]
R["journey_area_vs_primary"] = S["journey_area_vs_primary"]
R["untagged"] = S["untagged_text"]

# ---------------------------------------------------------------- intents for the 4-step form
import html as _html
import sys as _sys
_sys.path.insert(0, str(ROOT / "tools"))
from leads_taxonomy import T as _T, norm as _norm  # noqa: E402

INTENTS = {
    "residencia": ["ext_nomada", "ext_no_lucrativa", "ext_inversor", "ext_trabajo", "ext_emprendedor", "ext_estudios", "ext_arraigo", "ext_reagrupacion",
                   "ext_nacionalidad", "ext_regularizacion", "ext_asilo", "ext_renovacion_larga", "ext_brexit", "ext_visado", "ext_denegacion", "ext_irregularidad", "ext_general"],
    "llegada": ["ext_nie_tie", "ext_empadronamiento", "ext_sanidad_ss", "ext_carnet", "ext_homologacion", "ext_instalacion", "ext_banca"],
    "inmueble": [c for c in _T if c.startswith("inm_")],
    "empresa": [c for c in _T if c.startswith("mer_")],
    "impuestos": [c for c in _T if c.startswith("fis_") and c not in ("fis_sucesiones_impuesto", "fis_planificacion")],
    "herencia": ["suc_herencia", "fis_sucesiones_impuesto", "fis_planificacion"],
    "trabajo": [c for c in _T if c.startswith("lab_")],
    "jubilacion": ["ext_jubilacion", "ext_seguro_salud"],
    "conflicto": ["suc_litigio", "suc_familia", "suc_penal"],
}
intent_of = {}
for k, v in INTENTS.items():
    for c in v:
        intent_of.setdefault(c, k)
ist = {k: dict(n=0, langs=Counter(), primary=0, bc=0, bc_of=0, price=0, appt=0, urgent=0) for k in INTENTS}
pair = Counter()
for r in rows:
    tags = [t for t in r["all_subtopics"].split("|") if t]
    if not tags or not r["analysis_level"].startswith("texto"):
        continue
    ints = list(dict.fromkeys(intent_of[t] for t in tags if t in intent_of))
    for k in ints:
        ist[k]["n"] += 1
        ist[k]["langs"][r["lang"]] += 1
        if r["asks_price"] == "1":
            ist[k]["price"] += 1
        if r["asks_appointment"] == "1":
            ist[k]["appt"] += 1
        if r["urgent"] == "1":
            ist[k]["urgent"] += 1
    if r["primary_subtopic"] in intent_of:
        k = intent_of[r["primary_subtopic"]]
        ist[k]["primary"] += 1
        if r["blog_candidate"] != "":
            ist[k]["bc_of"] += 1
            ist[k]["bc"] += int(r["blog_candidate"])
    for i in range(len(ints)):
        for j in range(i + 1, len(ints)):
            pair[tuple(sorted((ints[i], ints[j])))] += 1
for k in ist:
    ist[k]["langs"] = dict(ist[k]["langs"])
R["intents"] = dict(tags=INTENTS, stats=ist, pairs=[[a, b, n] for (a, b), n in pair.most_common(20)])
inv = list(csv.DictReader(open(ROOT / "data" / "inventory.csv", encoding="utf-8")))
sug = {}
for k, tags in INTENTS.items():
    sug[k] = {}
    for lang in ("es", "en", "fr"):
        scored = []
        for p in inv:
            if p["lang"] != lang:
                continue
            txt = _norm(_html.unescape(p["title"]) + " " + p["slug"].replace("-", " "))
            n = sum(1 for c in tags if _T[c][3].search(txt))
            if n:
                scored.append((n, p["modified"], p["url"], _html.unescape(p["title"]).strip()))
        scored.sort(reverse=True)
        sug[k][lang] = [dict(url=u, title=t) for _, _, u, t in scored[:3]]
R["suggest"] = sug

R["traffic"] = {l: dict(Counter(r["traffic_hint"] or "none" for r in rows if r["lang"] == l)) for l in L}
# EN dropdown shares and RU
(D / "report_data.json").write_text(json.dumps(R, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("report_data.json", (D / "report_data.json").stat().st_size, "bytes")
