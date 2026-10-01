"""Build same-language Link Whisper related-post lists for posts whose cached list is in the wrong language.

Reads data/inventory.csv and data/related_posts_<lang>_audit.csv, picks 6 published posts in the
same language ranked by title/slug topic overlap (TF-IDF cosine), and writes:
  data/related_posts_fix.csv        review table (post -> chosen related posts)
  data/related_posts_fix.sql.txt    one UPDATE per post (UNHEX payload: no quoting issues)
Nothing is written to WordPress.

Usage:  python tools/related_posts_fix.py [post_id ...]   (default: every non-OK post in the audits)
"""
import csv
import math
import re
import sys
import unicodedata
from collections import Counter
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"9988"}  # English post tagged ES in WPML: fix the language first (DECISIONS D-9)

# Hand-picked lists (Mike's FR scope, 2026-10-01). They take precedence over the automatic ranking.
OVERRIDES = {
    "27692": ["2396", "27307", "900", "20166", "26678", "8655"],     # s'installer en Espagne
    "27316": ["27322", "27307", "21471", "2396", "5190", "27692"],   # regroupement familial
    "27322": ["27316", "27307", "2396", "1207", "27310", "27692"],   # résidence par mariage
    "27307": ["25663", "27322", "27316", "21471", "26023", "27692"], # résidence : voies d'accès
    "27310": ["27322", "27316", "14405", "16140", "27307", "5190"],  # divorce expatriés
    "27325": ["4371", "2573", "25839", "4345", "905", "25840"],      # calendrier fiscal
    "26760": ["2505", "27325", "4371", "2573", "20558", "25839"],    # se protéger face au fisc
    "24989": ["15720", "10629", "13762", "15895", "1130", "1819"],   # hébergements touristiques Valence
    "21471": ["27307", "27316", "2396", "13923", "25663", "27692"],  # régularisation exceptionnelle
    "2505": ["26760", "4371", "25839", "905", "2573", "19975"],      # faux non-résidents
}
STOP = set("""
a au aux avec ce ces dans de des du en et la le les leur lui mais ne nos notre ou par pas pour qu que qui
sa se ses son sur un une vos votre vous est sont tout tous faut savoir guide comment quels quelles quel
the of and to in for on with your you what how is are a an by from at as be it its this that need know
el la los las de del y en para por con que como su sus un una al lo es son guia todo sobre
espagne espana spain espagnol espanol spanish 2024 2025 2026 2027 blog
""".split())


def norm(text):
    text = unicodedata.normalize("NFKD", unescape(text).lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return [w for w in re.findall(r"[a-zЀ-ӿ0-9]+", text) if w not in STOP and len(w) > 2]


def tfidf(docs):
    df = Counter(w for d in docs.values() for w in set(d))
    n = len(docs)
    vecs = {}
    for k, d in docs.items():
        tf = Counter(d)
        v = {w: (c / len(d)) * math.log((n + 1) / (df[w] + 1)) for w, c in tf.items()} if d else {}
        norm_ = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vecs[k] = {w: x / norm_ for w, x in v.items()}
    return vecs


def cos(a, b):
    return sum(x * b.get(w, 0.0) for w, x in a.items())


def php_serialize(items):
    def s(v):
        b = v.encode("utf-8")
        return f's:{len(b)}:"{v}";'
    out = f"a:{len(items)}:{{"
    for i, it in enumerate(items):
        out += (f'i:{i};a:4:{{s:7:"post_id";i:{it["post_id"]};s:3:"url";{s(it["url"])}'
                f's:6:"anchor";{s(it["anchor"])}s:9:"thumb_url";s:0:"";}}')
    return out + "}"


def url_lang(url):
    for code in ("fr", "en", "ru"):
        if f"delaguialuzon.com/{code}/" in url:
            return code
    return "es"


def fetch_meta(lang):
    """Public REST: categories + excerpt per post (no auth)."""
    import json
    import urllib.request
    meta, page = {}, 1
    while True:
        url = (f"https://delaguialuzon.com/wp-json/wp/v2/posts?lang={lang}&per_page=100&page={page}"
               "&_fields=id,categories,excerpt")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (DL related-posts fix; read-only)"})
            data = json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8"))
        except Exception:
            break
        if not isinstance(data, list) or not data:
            break
        for p in data:
            meta[str(p["id"])] = (set(p.get("categories") or []), re.sub(r"<[^>]+>", " ", p["excerpt"]["rendered"]))
        page += 1
    return meta


def main():
    inv = [r for r in csv.DictReader(open(ROOT / "data" / "inventory.csv", encoding="utf-8"))
           if r["id"] not in SKIP and url_lang(r["url"]) == r["lang"]]
    by_id = {r["id"]: r for r in inv}
    targets = sys.argv[1:]
    if not targets:
        for lang in ("fr", "es", "en", "ru"):
            p = ROOT / "data" / f"related_posts_{lang}_audit.csv"
            if p.exists():
                targets += [r["id"] for r in csv.DictReader(open(p, encoding="utf-8")) if r["status"] != "OK"]
    targets = [t for t in dict.fromkeys(targets) if t not in SKIP and t in by_id]

    rows, sql = [], []
    for lang in ("fr", "es", "en", "ru"):
        meta = fetch_meta(lang)
        # Title and slug count double; the excerpt adds topical vocabulary.
        pool = {r["id"]: norm((r["title"] + " " + unescape(r["slug"]).replace("-", " ")) * 2
                              + " " + meta.get(r["id"], (set(), ""))[1])
                for r in inv if r["lang"] == lang}
        vecs = tfidf(pool)

        def score(t, o):
            ct, co = meta.get(t, (set(),))[0], meta.get(o, (set(),))[0]
            cat = len(ct & co) / len(ct | co) if ct and co else 0.0
            return 0.65 * cos(vecs[t], vecs[o]) + 0.35 * cat

        for t in [t for t in targets if by_id[t]["lang"] == lang]:
            ranked = sorted((score(t, o), o) for o in pool if o != t)
            picks = [o for o in OVERRIDES.get(t, []) if o in pool and o != t] or [o for _, o in reversed(ranked)][:6]
            items = [{"post_id": int(o), "url": by_id[o]["url"], "anchor": unescape(by_id[o]["title"]).strip()} for o in picks]
            payload = php_serialize(items)
            rows.append([t, lang, by_id[t]["url"], " | ".join(f'{i["post_id"]}: {i["anchor"][:60]}' for i in items)])
            sql.append(
                f"db query \"UPDATE {{prefix}}wpil_related_posts SET related_post_data = CONVERT(UNHEX('{payload.encode('utf-8').hex()}') USING utf8mb4), "
                f"processed = 1, manual_process = 1, process_time = UNIX_TIMESTAMP() WHERE post_id = {t}\"")
    with open(ROOT / "data" / "related_posts_fix.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["post_id", "lang", "url", "new_related_posts"])
        w.writerows(rows)
    (ROOT / "data" / "related_posts_fix.sql.txt").write_text("\n".join(sql) + "\n", encoding="utf-8")
    print(f"{len(rows)} posts -> data/related_posts_fix.csv, data/related_posts_fix.sql.txt")


if __name__ == "__main__":
    main()
