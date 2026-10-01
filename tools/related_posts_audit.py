"""Read-only check: are the Link Whisper related posts on each blog post in the post's own language?

Usage:  python tools/related_posts_audit.py es en ru     (default: all four locales)
Writes data/related_posts_<lang>_audit.csv per locale and prints the non-OK posts.
"""
import collections
import concurrent.futures as cf
import csv
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (DL related-posts audit; read-only)"


def lang_of(url):
    for code in ("fr", "en", "ru"):
        if f"delaguialuzon.com/{code}/" in url:
            return code
    return "es"


def check(row):
    try:
        req = urllib.request.Request(row["url"] + "?rp=1", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as resp:
            html, final = resp.read().decode("utf-8", "ignore"), resp.geturl()
    except Exception as e:
        return row, "ERROR", {}, [], str(e)[:80]
    i = html.find("lwrp-list-container")
    if i < 0:
        return row, "NO BLOCK", {}, [], final
    links = re.findall(r'href="(https://delaguialuzon\.com[^"]+)"', html[i:i + 20000])[:6]
    wrong = [h for h in links if lang_of(h) != row["lang"]]
    status = "OK" if not wrong else ("ALL WRONG" if len(wrong) == len(links) else "MIXED")
    return row, status, collections.Counter(lang_of(h) for h in links), wrong, final


def main():
    langs = sys.argv[1:] or ["es", "en", "fr", "ru"]
    rows = list(csv.DictReader(open(ROOT / "data" / "inventory.csv", encoding="utf-8")))
    for lang in langs:
        subset = [r for r in rows if r["lang"] == lang]
        out, stats = [], collections.Counter()
        with cf.ThreadPoolExecutor(4) as ex:
            for row, status, mix, wrong, final in ex.map(check, subset):
                stats[status] += 1
                out.append([row["id"], final, status, dict(mix),
                            " ".join(h.replace("https://delaguialuzon.com", "") for h in wrong)])
        path = ROOT / "data" / f"related_posts_{lang}_audit.csv"
        with open(path, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["id", "url", "status", "langs", "wrong_lang_links"])
            w.writerows(out)
        print(f"\n[{lang.upper()}] {dict(stats)} of {len(subset)} -> {path.name}")
        for o in out:
            if o[2] != "OK":
                print(f"  {o[2]:9} {o[0]:>6} {o[1].replace('https://delaguialuzon.com', '')[:70]} {o[3]}")


if __name__ == "__main__":
    main()
