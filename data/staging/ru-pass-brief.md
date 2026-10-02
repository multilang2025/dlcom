Task: RU pass on delaguialuzon.com blog posts (Russian locale /ru/blog/): **freshness, naturalness, format and CTA**. Mike asked for it on 2026-10-02; this request is the go to write. Your posts are listed at the end.

Read first in C:\Users\Mike\Documents\DealguiaLuzonLegacy: CLAUDE.md, docs/02-STYLE-GUIDE-MASTER.md, docs/style-guides/STYLE-GUIDE-RU.md, docs/03-FACT-CHECKING-PROTOCOL.md, docs/07-EDIT-AND-PUBLISH-PROCESS.md, docs/09-REVIEW-QA-GATE.md, and the agent briefs .claude/agents/dl-blog-editor.md and dl-fact-checker.md (they hold today's lessons and the 2025-2026 law watch list). Reuse today's FR fact-checks for sibling topics: data/factcheck/<fr_id>.csv and data/staging/<fr_id>-rewrite.md (FR ids given per post). Facts there are verified; still write the Russian natively, never translate the FR text.

Connectors: WPVibe rest_api / run_wp_cli (site_url https://delaguialuzon.com), AISA db_query (site delaguialuzon.com, chat_id "dl-legacy-blog"). AISA fact_check is unavailable: verify on official sources with WebFetch/WebSearch (boe.es consolidated act.php, sede.agenciatributaria.gob.es, seg-social.es, extranjeros.inclusion.gob.es, dogv.gva.es, eur-lex.europa.eu). Open every link you cite.

## Where the body lives
- `_elementor_edit_mode = builder` → the live body is `_elementor_data`. Do NOT edit post_content and do NOT switch rendering.
- mode empty or missing → the live body is `post_content`.
- Elementor JSON may store Cyrillic as \uXXXX escapes, so exact-snippet `content/edit` can be awkward. For many edits, read `_elementor_data`, json-decode locally, change widget `settings` text (editor/title/etc.), keep every section/column/widget id and structure, and save with `POST /wpvibe/v1/elementor/save-page` `{"id":ID,"post_type":"post","data":[...]}`. A new widget needs a fresh 8-hex id. For small edits `content/edit` on meta `_elementor_data` is fine if the snippet matches the stored bytes.
- post_content posts: `content/edit` (field post_content) or `PUT /wp/v2/posts/<id>` with content.
- Writes can return HTTP 500 (WPML fatal) and still commit: read back via SQL (MD5 / LIKE). Never raw mutating SQL and nothing that creates a WPVibe approval link (Mike: no expiring links). Posts only; never pages, templates, WPML or Rank Math settings.
- Re-read each post right before writing; never overwrite a newer post_modified.
- After writing: `run_wp_cli "litespeed-purge url <url>"`, curl the live URL, check your changes are there.

## What to do per post
1. **Freshness**: fact-check every figure, rate, threshold, deadline, form number, legal reference and "2025/2026" claim. Correct, or replace unverifiable specifics with a short CTA (contact the firm to confirm the case). Never guess. Law announced or decree-laws pending validation in Congress are written as pending. Expired deadlines are not presented as open. Log every claim in data/factcheck/<id>.csv (post_id,lang,claim,verdict,evidence,source_url,checked,siblings,action).
2. **Naturalness**: native, formal Russian for a Russian-speaking resident or buyer in Spain. Fix machine-translation calques, clumsy word order, wrong case government, English/French syntax, inconsistent terms. Formal «Вы» capitalised when addressing the reader. Terms: «вид на жительство без права на работу» (never «ненасыщенный»), NIE, TIE, empadronamiento etc. in Latin with a Russian explanation at first use. Don't rewrite good passages for the sake of it.
3. **Format** (house rules):
   - TL;DR first: H2 «<ключевая тема>: главное» with 4-7 self-contained factual bullets.
   - Short paragraphs (2-4 sentences); disguised lists become real lists.
   - Sentence-case headings, no meta openers («В этой статье мы расскажем…»), no "Заключение" H2, no emojis.
   - **Dashes, RU exception (pending D-5)**: rephrase to avoid —/– where it stays natural (colon, restructure). Where the dash is grammatically required and rephrasing would sound wrong, keep it and count it in your report. Never leave a broken sentence.
   - Sources as inline anchor links on descriptive text, target=_blank rel="nofollow noopener". No [n] markers, no bottom list. No competitor law-firm or agency sources.
   - FAQ questions as H3 (keep the existing FAQ length). CTA before the FAQ.
   - No pasted <html>/<head>/<body>/<style>.
4. **CTA**: one clear CTA block before the FAQ (plus a short closing line if the post has none) in formal Russian. Link to the RU contact page (find the /ru/ contact URL on the site and check it returns 200). Contact = the firm's Russian-speaking agent (Mike, 2026-10-02): «Свяжитесь с Olesia Davidova: o.davidova@delaguialuzon.com или +34 96 352 32 91» (tel:+34963523291). Never Félix on RU posts.
   - No «бесплатная консультация».
   - Brand «Delaguía y Luzón» (never "&"), «с 1960 года» (never "65 лет"/a year count, except in the two anniversary news posts where the 65th anniversary is the event itself), one office in Valencia, no Golden Visa as an available route.
   - Sanctions: never suggest services for entities established in Russia or Belarus; the reader is an individual resident in Spain.
5. **Links**: internal links /ru/ only (or remove the link and keep the text), current URLs (no redirects, no self-links), each checked with curl. Related posts (Link Whisper block) should already be RU: just confirm.
6. **Rank Math**: rank_math_title ≤ 60 chars, rank_math_description ≤ 155, Russian, no "&". Fix via `POST /rankmath/v1/updateMeta` if broken or contradicting the corrected body.
7. Logs: data/changelog/<id>.csv (date,post_id,lang,change,verified) and data/staging/<id>-ru-pass.md (what changed, facts corrected, open points). Do not git commit.

Don't touch other locales (flag sibling facts in your report). Cyrillic slugs stay as they are.

## Report back (concise)
Per post:
- what changed (freshness / naturalness / format / CTA);
- facts corrected and CTA'd;
- dashes kept (count);
- open points for Félix/Sonia or Mike;
- final MD5 + post_modified;
- live verified yes/no.
