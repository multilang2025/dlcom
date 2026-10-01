"""Build report/index.html: one local page showing the task list, the audit matrix and every doc.

Usage:  python tools/build_report.py   (then open report/index.html)
"""
import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ["es", "en", "fr", "ru"]
DOCS = ["TASKS.md", "CLAUDE.md", "docs/DECISIONS.md", "docs/01-SITE-AND-STACK.md",
        "docs/02-STYLE-GUIDE-MASTER.md", "docs/style-guides/STYLE-GUIDE-ES.md",
        "docs/style-guides/STYLE-GUIDE-EN.md", "docs/style-guides/STYLE-GUIDE-FR.md",
        "docs/style-guides/STYLE-GUIDE-RU.md", "docs/03-FACT-CHECKING-PROTOCOL.md",
        "docs/04-EEAT-STANDARD.md", "docs/05-NLP-ENTITY-SEO.md", "docs/06-AUDIT-PROCESS.md",
        "docs/07-EDIT-AND-PUBLISH-PROCESS.md", "docs/08-INTERNAL-LINKING.md",
        "docs/09-REVIEW-QA-GATE.md"]

rows = list(csv.DictReader(open(ROOT / "data" / "audit_baseline.csv", encoding="utf-8")))
i = lambda r, k: int(r.get(k) or 0)
CHECKS = [
    ("No hreflang alternates", "bug", lambda r: i(r, "hreflang_n") == 0),
    ("No Article/BlogPosting schema", "eeat", lambda r: r["has_article_schema"] == "False"),
    ("No visible author", "eeat", lambda r: r["visible_author"] == "False"),
    ("No visible date", "eeat", lambda r: r["visible_date"] == "False"),
    ("No numbered citations", "facts", lambda r: i(r, "cites_numbered") == 0),
    ("Only mentions years ≤ 2025", "facts", lambda r: bool(r["years_mentioned"]) and "2026" not in r["years_mentioned"]),
    ("Golden Visa mention", "facts", lambda r: "golden" in r["banned_hits"] or "золот" in r["banned_hits"]),
    ("Forbidden source linked", "facts", lambda r: bool(r["forbidden_domains"])),
    ("Banned phrase", "style", lambda r: bool(r["banned_hits"])),
    ("Em/en dashes", "style", lambda r: i(r, "dashes") > 0),
    ("Emoji in body", "style", lambda r: i(r, "emoji_body") > 0),
    ("'Conclusion' H2", "style", lambda r: r["h2_conclusion"] == "True"),
    ("Title tag with pipe", "nlp", lambda r: r["title_pipe"] == "True"),
    ("Meta description > 155", "nlp", lambda r: i(r, "desc_len") > 155),
    ("Under 800 words", "nlp", lambda r: i(r, "words") < 800),
    ("< 3 internal links", "nlp", lambda r: i(r, "internal_links") < 3),
    ("Canonical mismatch", "bug", lambda r: r["canonical_ok"] == "False"),
    ("Year in slug", "bug", lambda r: r["year_in_slug"] == "True"),
    ("Images not WebP", "bug", lambda r: i(r, "img_not_webp") > 0),
]
tot = {l: sum(r["lang"] == l for r in rows) for l in LANGS}
trs = []
for name, cat, f in CHECKS:
    counts = [sum(1 for r in rows if r["lang"] == l and f(r)) for l in LANGS]
    cells = "".join(
        f'<td class="num" style="--p:{c / tot[l] if tot[l] else 0:.2f}"><span>{c}</span></td>'
        for c, l in zip(counts, LANGS))
    trs.append(f'<tr><td><span class="tag {cat}">{cat}</span> {html.escape(name)}</td>{cells}'
               f'<td class="num total">{sum(counts)}</td></tr>')

docs = {d: (ROOT / d).read_text(encoding="utf-8") for d in DOCS if (ROOT / d).exists()}
nav = "".join(f'<button data-doc="{html.escape(d)}">{html.escape(Path(d).stem)}</button>' for d in docs)

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>DL Blog Workbench</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<style>
:root{{--bg:#f7f8f6;--card:#fff;--ink:#1a1f24;--mute:#5b6b7d;--line:#dfe4df;--acc:#5c6f5e;--heat:103,147,105}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#14181b;--card:#1c2226;--ink:#e8ece9;--mute:#9aa8b5;--line:#2c3439;--acc:#9fbfa1}}}}
:root[data-theme=dark]{{--bg:#14181b;--card:#1c2226;--ink:#e8ece9;--mute:#9aa8b5;--line:#2c3439;--acc:#9fbfa1}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
header{{padding:28px 16px 8px;max-width:1150px;margin:auto}}h1{{margin:0 0 4px;font-size:24px}}.sub{{color:var(--mute)}}
main{{max-width:1150px;margin:auto;padding:0 16px 48px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:18px 0}}
.kpi{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px}}.kpi b{{font-size:22px;display:block}}.kpi span{{color:var(--mute);font-size:13px}}
section{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin:16px 0;overflow-x:auto}}
h2{{font-size:18px;margin:0 0 10px}}table{{border-collapse:collapse;width:100%;font-size:14px}}
th,td{{padding:6px 8px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}}th{{color:var(--mute);font-weight:600}}
td.num{{text-align:right;font-variant-numeric:tabular-nums;background:rgba(var(--heat),calc(var(--p)*.55))}}td.total{{font-weight:700;background:none}}
.tag{{font-size:11px;padding:1px 6px;border-radius:8px;border:1px solid var(--line);color:var(--mute);text-transform:none}}
.tag.facts{{border-color:#b5523b;color:#b5523b}}.tag.eeat{{border-color:#5b6b7d}}.tag.bug{{border-color:#a07a1f;color:#a07a1f}}
nav{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}}nav button{{background:none;border:1px solid var(--line);color:var(--ink);border-radius:16px;padding:4px 10px;cursor:pointer;font:inherit;font-size:13px}}
nav button.on{{background:var(--acc);color:#fff;border-color:var(--acc)}}
#doc{{max-width:900px}}#doc h1{{font-size:22px}}#doc h2{{font-size:18px;margin-top:22px}}#doc code{{background:rgba(127,127,127,.15);padding:1px 4px;border-radius:4px;font-size:13px}}
#doc pre{{background:rgba(127,127,127,.12);padding:10px;border-radius:8px;overflow-x:auto}}#doc table{{font-size:13px}}
.note{{color:var(--mute);font-size:13px}}
</style></head><body>
<header><h1>Delaguía y Luzón blog workbench</h1>
<div class="sub">Legacy WordPress blog · ES / EN / FR / RU · baseline audit and GSC of 2026-10-01 · nothing written to WordPress yet</div></header>
<main>
<div class="kpis">
<div class="kpi"><b>{len(rows)}</b><span>published posts audited</span></div>
{''.join(f'<div class="kpi"><b>{tot[l]}</b><span>{l.upper()} posts</span></div>' for l in LANGS)}
<div class="kpi"><b>16</b><span>process docs adapted from dlvibe</span></div>
</div>
<section><h2>Audit matrix: posts affected per locale</h2>
<table><thead><tr><th>Check</th>{''.join(f'<th class="num">{l.upper()}</th>' for l in LANGS)}<th class="num">All</th></tr></thead>
<tbody>{''.join(trs)}</tbody></table>
<p class="note">Source: <code>data/audit_baseline.csv</code> from <code>tools/audit_blog.py</code> (read-only crawl of live HTML). Cell shading = share of that locale's posts.</p></section>
<section><h2>Documents</h2><nav>{nav}</nav><article id="doc"></article></section>
</main>
<script>
const DOCS = {json.dumps(docs, ensure_ascii=False).replace("</", "<\\/")};
const el = document.getElementById("doc"), btns = document.querySelectorAll("nav button");
function show(d){{ btns.forEach(b=>b.classList.toggle("on", b.dataset.doc===d));
  el.innerHTML = window.marked ? marked.parse(DOCS[d]) : "<pre>"+DOCS[d].replace(/[<&]/g,c=>({{"<":"&lt;","&":"&amp;"}})[c])+"</pre>";
  try{{ localStorage.setItem("dl-doc", d) }}catch(e){{}} }}
btns.forEach(b=>b.onclick=()=>show(b.dataset.doc));
let start="TASKS.md"; try{{ start = localStorage.getItem("dl-doc") || start }}catch(e){{}}
show(DOCS[start] ? start : "TASKS.md");
</script></body></html>"""
out = ROOT / "report" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding="utf-8")
print(f"wrote {out}")
