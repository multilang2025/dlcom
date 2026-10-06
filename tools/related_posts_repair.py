"""Repair Link Whisper related lists that contain a broken item (no image, a page instead of a post, a
deleted post, the post itself). Keeps every good item, replaces only the broken ones with the closest
published same-language posts that have a featured image.

Reads data/related_posts_<lang>_audit.csv (column items_without_image) and the live pages. Writes
  data/related_posts_repair.csv       review table (post -> kept / replaced)
  data/related_posts_repair.sql.txt   one UPDATE per post (UNHEX payload)
Nothing is written to WordPress.

Usage:  python tools/related_posts_repair.py [post_id ...]     (default: every post flagged in the audits)
"""
import csv
import json
import re
import sys
import urllib.request
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from related_posts_fix import cos, norm, php_serialize, tfidf, url_lang  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0 (DL related-posts repair; read-only)"}
SKIP = {"9988"}  # English post still tagged ES in the inventory (D-9)


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode("utf-8", "ignore")


def rest_meta(lang):
    """id -> (featured_media, categories, excerpt text) via the public REST API."""
    meta, page = {}, 1
    while True:
        try:
            data = json.loads(get(f"https://delaguialuzon.com/wp-json/wp/v2/posts?lang={lang}&per_page=100&page={page}"
                                  "&_fields=id,featured_media,categories,excerpt"))
        except Exception:
            break
        if not isinstance(data, list) or not data:
            break
        for p in data:
            meta[str(p["id"])] = (int(p.get("featured_media") or 0), set(p.get("categories") or []),
                                  re.sub(r"<[^>]+>", " ", p["excerpt"]["rendered"]))
        page += 1
    return meta


def live_items(url):
    html = get(url + ("&" if "?" in url else "?") + "rpr=1")
    i = html.find('<div id="link-whisper-related-posts-widget"')
    out = []
    for it in html[i:i + 30000].split('<div class="lwrp-list-item">')[1:7]:
        it = it.split("</a></div>")[0]
        m = re.search(r'href="(https://delaguialuzon\.com[^"]+)"', it)
        if m:
            out.append(m.group(1).split("?")[0].rstrip("/") + "/")
    return out


def main():
    inv = [r for r in csv.DictReader(open(ROOT / "data" / "inventory.csv", encoding="utf-8"))
           if url_lang(r["url"]) == r["lang"] and r["id"] not in SKIP]
    by_url = {r["url"].split("?")[0].rstrip("/") + "/": r for r in inv}
    targets = sys.argv[1:]
    if not targets:
        for lang in ("fr", "en", "es", "ru"):
            p = ROOT / "data" / f"related_posts_{lang}_audit.csv"
            if p.exists():
                targets += [r["id"] for r in csv.DictReader(open(p, encoding="utf-8")) if r["items_without_image"]]
    targets = [t for t in dict.fromkeys(targets) if t not in SKIP]
    review, sql = [], []
    for lang in ("fr", "en", "es", "ru"):
        mine = [t for t in targets if any(r["id"] == t and r["lang"] == lang for r in inv)]
        if not mine:
            continue
        meta = rest_meta(lang)
        pool_ids = [r["id"] for r in inv if r["lang"] == lang and meta.get(r["id"], (0,))[0] > 0]
        docs = {r["id"]: norm((r["title"] + " " + unescape(r["slug"]).replace("-", " ")) * 2 + " " + meta[r["id"]][2])
                for r in inv if r["id"] in pool_ids}
        by_id = {r["id"]: r for r in inv}
        vecs = tfidf(docs)
        for t in mine:
            row = by_id[t]
            current = live_items(row["url"])
            good, dropped = [], []
            for u in current:
                r = by_url.get(u)
                if r and r["id"] != t and r["lang"] == lang and meta.get(r["id"], (0,))[0] > 0 and r["id"] not in good:
                    good.append(r["id"])
                else:
                    dropped.append(u.replace("https://delaguialuzon.com", ""))
            need = 6 - len(good)
            if need <= 0:
                continue
            ct = meta.get(t, (0, set(), ""))[1]
            tv = vecs.get(t) or vecs.get(next(iter(vecs)))
            if t not in vecs:  # target itself has no featured image: build its vector separately
                d = norm((row["title"] + " " + unescape(row["slug"]).replace("-", " ")) * 2)
                single = tfidf({**docs, t: d})
                tv = single[t]
            ranked = sorted(
                ((0.65 * cos(tv, vecs[o]) + 0.35 * (len(ct & meta[o][1]) / len(ct | meta[o][1]) if ct and meta[o][1] else 0.0), o)
                 for o in pool_ids if o != t and o not in good), reverse=True)
            added = [o for _, o in ranked[:need]]
            final = good + added
            items = [{"post_id": int(o), "url": by_id[o]["url"], "anchor": unescape(by_id[o]["title"]).strip()} for o in final]
            payload = php_serialize(items)
            review.append([t, lang, row["url"], " | ".join(dropped), " | ".join(by_id[o]["slug"] for o in good),
                           " | ".join(f"{o}: {unescape(by_id[o]['title'])[:55]}" for o in added)])
            sql.append(
                f"db query \"UPDATE {{prefix}}wpil_related_posts SET related_post_data = CONVERT(UNHEX('{payload.encode('utf-8').hex()}') USING utf8mb4), "
                f"processed = 1, manual_process = 1, process_time = UNIX_TIMESTAMP() WHERE post_id = {t}\"")
    with open(ROOT / "data" / "related_posts_repair.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["post_id", "lang", "url", "dropped_items", "kept_slugs", "added_posts"])
        w.writerows(review)
    (ROOT / "data" / "related_posts_repair.sql.txt").write_text("\n".join(sql) + "\n", encoding="utf-8")
    print(f"{len(review)} posts -> data/related_posts_repair.csv, data/related_posts_repair.sql.txt")


if __name__ == "__main__":
    main()
