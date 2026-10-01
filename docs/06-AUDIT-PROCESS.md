# Audit process (per post, all locales)

Two passes. The automated pass runs on every post and is cheap. The manual pass runs per batch, in
the priority order in `TASKS.md`.

## 1. Inventory (refresh before each campaign)

Public REST, no auth, per locale (`lang` = es|en|fr|ru, ES returns ≤100 per page):

```
curl "https://delaguialuzon.com/wp-json/wp/v2/posts?lang=fr&per_page=100&page=1&_fields=id,slug,link,date,modified,author,title"
```

Saved as `data/inventory.csv` (`lang,id,slug,url,published,modified,author_id,title`). Translation
groups (`trid`) and focus keywords come from SQL (AISA `db_query`):

```sql
SELECT t.trid, t.language_code, p.ID, p.post_name
FROM dlg_posts p JOIN dlg_icl_translations t ON t.element_id=p.ID AND t.element_type='post_post'
WHERE p.post_type='post' AND p.post_status='publish' ORDER BY t.trid;
```

## 2. Automated pass: `python tools/audit_blog.py`

Read-only. Fetches the live HTML and writes `data/audit_baseline.csv`. Checks: HTTP status, title
length/emoji/pipe, description length/emoji, canonical, hreflang count, H1 count, H2 count,
"Conclusion" headings, numbered headings, word count, TOC count, dashes, emoji in body, `&` brand,
banned phrases per locale (incl. free consultation, Golden Visa, RU calque, year counts), year in
slug, `-2` slugs, years mentioned, internal/self/external links, external links without nofollow
or `_blank`, forbidden domains, images without alt or not WebP, blockquotes, tables, lists,
numbered citations, schema types, Article author type and dates, FAQ schema count, visible
author/reviewer/date.

Run per locale with `--lang fr`, or a sample with `--limit 10`.

## 3. Manual pass (one post at a time, with the post open)

Fill one row in `data/review/<lang>.csv`:

| Column | Check | Doc |
|---|---|---|
| style | banned phrases, structure, headings, summary box, CTA, FAQ, no walls of text | 02 + locale guide |
| bugs | broken layout, empty widgets, stray shortcodes, broken/redirecting links (Broken Link Checker list), wrong-locale links, mojibake, duplicated blocks, wrong-language strings (e.g. Spanish heading in an FR post) | 01 |
| nlp | keyword placement, intent, question/entity coverage, cannibalisation | 05 |
| eeat | 5 questions, 0 to 2 each | 04 |
| facts | claims extracted and verdicts in `data/factcheck/<id>.csv` | 03 |
| links | internal links in/out, anchors varied, orphan status | 08 |
| priority | P1 (wrong/expired legal fact, broken page) / P2 (EEAT, NLP gaps on a post with traffic) / P3 (style only) | |
| action | `fix-in-place` / `rewrite` / `merge→<id>` / `noindex` / `escalate` | |

## 4. Prioritising

Order by: **(a)** fact risk (expired deadlines, figures from past years, Golden Visa, immigration
rules), **(b)** traffic and leads (GSC clicks over the last 90 days; FR brings 47% of form
enquiries; immigration > tax > property), **(c)** locale tier (FR, EN, then ES, then RU), **(d)**
effort.
