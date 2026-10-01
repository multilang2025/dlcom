"""Read-only baseline audit of every published blog post on delaguialuzon.com (all locales).

Fetches the public HTML of each URL in data/inventory.csv and writes data/audit_baseline.csv
with one row per post and one column per automated check (see docs/06-AUDIT-PROCESS.md).
Nothing is written to WordPress.

Usage:  python tools/audit_blog.py [--limit N] [--lang fr]
"""
import argparse
import concurrent.futures as cf
import csv
import json
import re
import sys
import urllib.request
from html import unescape
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "data" / "inventory.csv"
OUT = ROOT / "data" / "audit_baseline.csv"
UA = "Mozilla/5.0 (DL blog audit; read-only)"
HOST = "delaguialuzon.com"

BANNED = {
    "all": [r"\bgolden visa\b", r"visa dorad", r"visa d'or", r"золот\w* виз"],
    "fr": [r"\bce guide\b", r"\bchez dela ?gu[ií]a", r"il est important de", r"dans le cadre de",
           r"\bdécouvrez\b", r"consultation gratuite", r"première consultation offerte", r"\b6\d ans d'expérience"],
    "es": [r"\bdescubre\b", r"\bdescubra\b", r"es importante", r"consulta gratuita", r"sin coste", r"\b6\d años de experiencia"],
    "en": [r"\bdiscover\b", r"it is important to", r"free consultation", r"\bgenuinely\b", r"\bhonestly\b",
           r"\bstraightforward\b", r"^by \w+ing\b", r"\b6\d years of experience"],
    "ru": [r"ненасыщенн\w* вид на жительство", r"бесплатн\w* консультац"],
}
FORBIDDEN_DOMAINS = ["garrigues.com", "jacheteenespagne.com"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅]")
TAG = re.compile(r"<[^>]+>")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, r.read().decode("utf-8", errors="ignore")


def text(s):
    return re.sub(r"\s+", " ", unescape(TAG.sub(" ", s))).strip()


def post_body(html):
    """The post's own Elementor document (data-elementor-type="wp-post"), nested inside the
    single-post theme template (id 4476), cut before the template's trailing widgets."""
    marker = html.find('data-elementor-type="wp-post"')
    if marker < 0:
        # Non-Elementor post (block/classic content) rendered by the template's post-content widget
        m = re.search(r'<div[^>]*class="[^"]*elementor-widget-theme-post-content', html)
        marker = m.start() + 1 if m else -1
    if marker < 0:
        return ""
    start = html.rfind("<div", 0, marker)
    depth = 0
    for m in re.finditer(r"<div\b|</div>", html[start:]):
        depth += 1 if m.group(0) == "<div" else -1
        if depth == 0:
            return html[start: start + m.end()]
    return html[start:]


def schema(html):
    types, art = [], {}
    for blob in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', html, re.S):
        try:
            d = json.loads(blob)
        except Exception:
            types.append("PARSE_ERROR")
            continue
        for node in d.get("@graph", [d]) if isinstance(d, dict) else d:
            t = node.get("@type")
            types.extend(t if isinstance(t, list) else [t])
            if t in ("BlogPosting", "Article", "NewsArticle"):
                art = node
            if t == "FAQPage":
                art.setdefault("_faq_n", len(node.get("mainEntity", [])))
    return types, art


def audit(row):
    lang, url, slug = row["lang"], row["url"], unquote(row["slug"])
    r = {"lang": lang, "id": row["id"], "url": url, "modified": row["modified"]}
    try:
        status, html = fetch(url)
    except Exception as e:
        r["http"] = f"ERR {e}"[:80]
        return r
    r["http"] = status
    head_title = text((re.search(r"<title>(.*?)</title>", html, re.S) or [None, ""])[1])
    desc = unescape((re.search(r'<meta name="description" content="([^"]*)"', html) or [None, ""])[1])
    canon = (re.search(r'<link rel="canonical" href="([^"]+)"', html) or [None, ""])[1]
    hreflangs = re.findall(r'<link rel="alternate" hreflang="([^"]+)"', html)
    body = post_body(html)
    btxt = text(body)
    low = btxt.lower()
    h1s = [text(h) for h in re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S)]
    h2s = [text(h) for h in re.findall(r"<h2[^>]*>(.*?)</h2>", body, re.S)]
    types, art = schema(html)
    links = re.findall(r"<a\s[^>]*href=\"([^\"]+)\"[^>]*>", body)
    a_tags = re.findall(r"<a\s[^>]*>", body)
    ext = [a for a in a_tags if re.search(r'href="https?://', a) and HOST not in a]
    imgs = re.findall(r"<img\s[^>]*>", body)
    words = len(btxt.split())
    banned = [p for p in BANNED["all"] + BANNED.get(lang, []) if re.search(p, low, re.M)]

    r.update({
        "title_tag": head_title, "title_len": len(head_title),
        "title_emoji": bool(EMOJI.search(head_title)), "title_pipe": "|" in head_title,
        "desc_len": len(desc), "desc_emoji": bool(EMOJI.search(desc)),
        "canonical_ok": canon.rstrip("/") == url.rstrip("/"),
        "hreflang_n": len(hreflangs),
        "h1_n": len(h1s), "h1": h1s[0] if h1s else "",
        "h1_title_case": bool(h1s) and lang == "en" and sum(w[:1].isupper() for w in h1s[0].split()[1:]) > len(h1s[0].split()) / 2,
        "h2_n": len(h2s), "h2_conclusion": any(re.match(r"(conclusi|заключ)", h, re.I) for h in h2s),
        "h2_numbered": any(re.match(r"^\d+[\.\)]", h) for h in h2s),
        "words": words,
        "toc_n": len(re.findall(r'data-widget_type="table-of-contents|<div[^>]*class="wp-block-rank-math-toc-block', html)),
        "toc_in_body": len(re.findall(r'data-widget_type="table-of-contents|<div[^>]*class="wp-block-rank-math-toc-block', body)),
        "dashes": btxt.count("—") + btxt.count("–"),
        "emoji_body": len(EMOJI.findall(btxt)),
        "ampersand_brand": len(re.findall(r"dela ?gu[ií]a\s*(?:&|&amp;)\s*luz[oó]n", html, re.I)),
        "banned_hits": "; ".join(banned),
        "year_in_slug": bool(re.search(r"(19|20)\d\d", slug)),
        "dup_slug_suffix": bool(re.search(r"-\d$", slug)),
        "years_mentioned": ",".join(sorted(set(re.findall(r"\b20(?:1\d|2[0-6])\b", btxt)))),
        "internal_links": sum(1 for l in links if HOST in l or l.startswith("/")),
        "self_links": sum(1 for l in links if l.split("#")[0].rstrip("/") == url.rstrip("/")),
        "external_links": len(ext),
        "ext_missing_nofollow": sum(1 for a in ext if "nofollow" not in a),
        "ext_missing_blank": sum(1 for a in ext if "_blank" not in a),
        "forbidden_domains": ",".join(d for d in FORBIDDEN_DOMAINS if d in body),
        "imgs": len(imgs),
        "img_no_alt": sum(1 for i in imgs if not re.search(r'alt="[^"]+"', i)),
        "img_not_webp": max(0, len(imgs) - len(re.findall(r"<source[^>]+\.webp", body))
                            - sum(1 for i in imgs if ".webp" in i)),
        "blockquotes": len(re.findall(r"<blockquote", body)),
        "tables": len(re.findall(r"<table", body)),
        "lists": len(re.findall(r"<(?:ul|ol)[\s>]", body)),
        "cites_numbered": len(re.findall(r"\[\d+\]", btxt)),
        "schema_types": "|".join(t for t in types if t),
        "has_article_schema": bool(art),
        "article_author_type": (art.get("author") or {}).get("@type", "") if isinstance(art.get("author"), dict) else "",
        "article_dates": bool(art.get("datePublished")) and bool(art.get("dateModified")),
        "faq_schema_n": art.get("_faq_n", 0) if art else ("FAQPage" in types) * -1,
        "visible_author": bool(re.search(r'rel="author"|elementor-author-box|author-box|class="[^"]*byline', html)),
        "visible_reviewer": bool(re.search(r"(reviewed by|revisado por|relu par|révisé par|проверено)", low)),
        "visible_date": bool(re.search(r"<time[\s>]|elementor-post-info__item--type-date", html)),
    })
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int)
    ap.add_argument("--lang")
    a = ap.parse_args()
    rows = list(csv.DictReader(open(INVENTORY, encoding="utf-8")))
    if a.lang:
        rows = [r for r in rows if r["lang"] == a.lang]
    rows = rows[: a.limit] if a.limit else rows
    out = []
    with cf.ThreadPoolExecutor(6) as ex:
        for i, res in enumerate(ex.map(audit, rows), 1):
            out.append(res)
            if i % 25 == 0:
                print(f"{i}/{len(rows)}", file=sys.stderr, flush=True)
    keys = list(dict.fromkeys(k for r in out for k in r))
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(out)
    print(f"wrote {OUT} ({len(out)} rows)")


if __name__ == "__main__":
    main()
