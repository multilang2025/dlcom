# 1571 RU: Реструктуризация предприятий в Испании (RU pass, 2026-10-02)

Live: https://delaguialuzon.com/ru/blog/кризисные-компании-испании/ (Elementor builder, body in `_elementor_data`).
Siblings (trid 195): FR 1557, EN 1563. Not touched.

## Write
- `POST /wpvibe/v1/elementor/save-page`: returned 400 `elementor_save_fatal` (WPML `array_filter` fatal) **but committed**. SQL readback equals `1571-ru-pass.elementor.json`.
- `_elementor_data` MD5 01e2faa6… -> **88421d0ab734efa848e6234865764cb0** (52 422 bytes). Rollback: `1571-ru-pass.orig-elementor.json`.
- Title via `PUT /wp/v2/posts/1571` (title only): HTTP 500 WPML fatal, committed. post_modified **2026-10-02 16:39:24**.
- Rank Math title/description via `/rankmath/v1/updateMeta`. `cache purge`, live verified.
- Live check needed a full `cache purge` (object cache): `litespeed-purge url` alone still served the old body.

## What changed
- Freshness: the old text had no law at all. Added the Ley 16/2022 / TRLC tools, reusing data/factcheck/18814.csv and re-reading each article on the BOE (arts 2, 5, 444, 456, 583, 584, 585, 600, 601, 605, 607, 614, 623, 629, 639, 654, 655, 685; ET 47/51).
- Naturalness: rewritten natively in formal Russian; "В этой статье мы рассмотрим" opener removed; «Вы» capitalised.
- Format: TL;DR H2 first (7 bullets), H3 hook, H2 sections in sentence case, lists for disguised enumerations, one verbatim BOE quote (art. 2.3). No FAQ existed, none added. CTA H2 at the end (no FAQ) plus a CTA in the director-liability section.
- Title: «Часть 1» removed. No Part 2 exists in RU, EN or FR (SQL search), so the series label was misleading. New H1: «Реструктуризация предприятий в Испании: переговоры с кредиторами и план реструктуризации». Slug unchanged.
- Links: RU only, all 200: 8407 (бухгалтер), трудовое право, коммерческое право, налоговое право, контакты.

## Dashes kept: 0

## Open points
- EN 1563 is still titled "Part 1" with no Part 2 (Maral/Mike).
- FR 1557 vs FR 18814 cannibalisation already flagged in 18814-rewrite.md.
- Rank Math stored schema (not output while the rich-snippet module is off) still has headline «…Часть 1…», author "Delaguía & Luzón Abogados" and a FAQPage with wrong claims ("статья 583", "защищает от исков и увольнений"). Clear or rewrite before T-02 re-enables rich snippets (Mike).
- Link Whisper related-posts block is RU but off-topic (Airbnb, rentals) and contains a 404 (/ru/blog/программа-постоянного-трудоустройст/) and a 301 (/ru/blog/subsidies-indefinite-hiring-unemployed/): re-scan in wp-admin (Mike).
- Inbound links: none added from other RU posts (outside this assignment). Candidates: 8407 (бухгалтер), 13927 (права иностранных работников).
- Félix/Sonia: optional review of the art. 639 / 654-655 summary.
