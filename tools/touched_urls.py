"""List every live URL touched by agents in this workbench, from data/changelog/*.csv.

Writes data/touched_urls.csv and data/touched_urls.md (grouped by locale and kind of change).
Read-only: uses the public REST API to confirm each post's live URL and status.

Usage:  python tools/touched_urls.py
"""
import csv
import json
import re
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0 (DL touched-urls report; read-only)"}


def lang_of(url):
    for code in ("fr", "en", "ru"):
        if f"delaguialuzon.com/{code}/" in url:
            return code
    return "es"


def rest(pid):
    try:
        d = json.loads(urllib.request.urlopen(urllib.request.Request(
            f"https://delaguialuzon.com/wp-json/wp/v2/posts/{pid}?_fields=link,status,modified,title", headers=UA), timeout=40).read())
        return d["link"], "live", d["modified"]
    except Exception:
        return "", "not public (draft, trashed or private)", ""


NOEDIT = re.compile(r"nothing (was )?(edited|to change)|no statement found|not edited|no change", re.I)


# Posts whose body was rewritten or substantially rebuilt in this workbench (explicit list, not guessed from wording).
RU_PASS = set()  # filled from the RU inventory in main()
REWRITTEN = {
    # FR: 11 switched to their cleaned 2026 rewrites, plus the other full rewrites
    "2687", "2823", "7335", "8402", "8615", "8655", "10335", "10629", "11817", "12930", "18814", "13243", "15895",
    "2678", "888", "27307", "26678", "27692", "27316", "25840",
    # EN: rebuilt or substantially rewritten
    "15116", "27052", "25207", "10247", "20394", "27449", "892", "25233", "24445", "13250", "13755", "4734", "15852", "991",
    "2869", "1815",
    # ES
    "16608", "21398", "23581", "21471", "21452",
}


def kind(entries, pid=""):
    """entries: list of change texts. Order of precedence: rewrite > correction > meta > checked."""
    real = [e for e in entries if not NOEDIT.search(e)]
    if not real:
        return "checked, not edited"
    if pid in REWRITTEN:
        return "REWRITTEN / rendering switched"
    t = " ".join(real).lower()
    if pid in RU_PASS:
        return "REWRITTEN / rendering switched"
    if re.search(r"fact|correct|fix|updated|removed|replaced|added|restor|tldr|tl;dr|link", t):
        return "facts / text corrected"
    if re.search(r"rank math|meta|schema|json-ld|excerpt|focus keyword|description", t):
        return "meta / schema only"
    return "other edit"


def main():
    rows = defaultdict(list)
    for p in sorted((ROOT / "data" / "changelog").glob("*.csv")):
        try:
            for r in csv.reader(open(p, encoding="utf-8")):
                if not r or r[0].lower() == "date" or not re.match(r"20\d\d-\d\d-\d\d", r[0]):
                    continue
                if len(r) >= 4:
                    rows[r[1].strip() or p.stem].append((r[0], r[2], r[3], r[4] if len(r) > 4 else ""))
        except Exception:
            continue
    # posts whose related lists were rewritten (no page change)
    related = set()
    for name in ("related_posts_fix.csv",):
        f = ROOT / "data" / name
        if f.exists():
            related |= {r["post_id"] for r in csv.DictReader(open(f, encoding="utf-8"))}
    out = []
    for pid in sorted(set(rows) | related, key=lambda x: int(x) if x.isdigit() else 0):
        if not pid.isdigit():
            continue
        link, status, modified = rest(pid)
        entries = rows.get(pid, [])
        dates = sorted({e[0] for e in entries})
        real = [e for e in entries if not NOEDIT.search(e[2])]
        last = (real or entries)[-1][2] if entries else "Link Whisper related list only (2026-10-01)"
        k = kind([e[2] for e in entries], pid) if entries else "related list only"
        lang = lang_of(link) if link else (entries[0][1].lower() if entries and entries[0][1] else "")
        if lang == "ru" and k != "checked, not edited":
            k = "REWRITTEN / rendering switched"
        out.append({"post_id": pid, "lang": lang, "status": status, "url": link, "kind": k,
                    "dates": " ".join(dates) or "2026-10-01", "changes_logged": len(entries),
                    "last_change": re.sub(r"\s+", " ", last)[:200]})
    with open(ROOT / "data" / "touched_urls.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    md = ["# Live URLs touched in this workbench (2026-10-01 to 2026-10-06)", "",
          f"{len(out)} posts. Source: `data/changelog/*.csv` and `data/related_posts_fix.csv`. Regenerate with `python tools/touched_urls.py`.", ""]
    for lang, title in (("fr", "FR"), ("en", "EN"), ("es", "ES"), ("ru", "RU"), ("", "Not public")):
        group = [o for o in out if (o["lang"] == lang and o["status"] == "live") or (lang == "" and o["status"] != "live")]
        if not group:
            continue
        order = {"REWRITTEN / rendering switched": 0, "facts / text corrected": 1, "meta / schema only": 2, "other edit": 3,
                 "related list only": 4, "checked, not edited": 5}
        group.sort(key=lambda o: (order.get(o["kind"], 9), int(o["post_id"])))
        md += [f"## {title} ({len(group)})", "", "| Post | Kind | Dates | Last change |", "|---|---|---|---|"]
        for o in group:
            u = o["url"] or f"post {o['post_id']}"
            md.append(f"| [{o['post_id']}]({o['url']}) | {o['kind']} | {o['dates'].replace(' ', ', ')} | {o['last_change'].replace('|', '/')} |"
                      if o["url"] else f"| {o['post_id']} | {o['kind']} | {o['dates'].replace(' ', ', ')} | {o['last_change'].replace('|', '/')} |")
        md.append("")
    (ROOT / "data" / "touched_urls.md").write_text("\n".join(md), encoding="utf-8", newline="\n")
    print(len(out), "posts ->", "data/touched_urls.csv, data/touched_urls.md")


if __name__ == "__main__":
    main()
