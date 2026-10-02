# 14460 RU: Как учредить стартап в Испании (RU pass, 2026-10-02)

Live: https://delaguialuzon.com/ru/blog/как-учредить-стартап-в-испании/ (Elementor builder, single text-editor widget 0781e6f).
Siblings (trid 1769): ES 14344, EN 14384, FR 14416. Not touched.

## Write
- `POST /wpvibe/v1/elementor/save-page`: HTTP 200. SQL readback equals `14460-ru-pass.elementor.json`.
- `_elementor_data` MD5 86116da7… -> **e2a4fbbba4d7f1981f1cfc3b2cb534aa** (52 540 bytes), post_modified **2026-10-02 16:46:52**. Rollback: `14460-ru-pass.orig-elementor.json`.
- Rank Math via `/rankmath/v1/updateMeta`. `cache purge`, live verified.

## What changed
- Angle: the title promised a step-by-step 2026 guide but the body was a translated legal-form comparison. It is now a setup guide: legal form, SL incorporation steps, empresa emergente status, startup tax regime, entrepreneur residence. Financing is left to 8364 and cross-linked (8364 links back).
- Freshness, all on the BOE:
  - Ley 28/2022 arts 3-9;
  - LIS art. 29;
  - LIRPF arts 42.3.f and 93;
  - Ley 14/2013 arts 69-70;
  - LSC arts 4, 12, 62, 79;
  - RD 1065/2007 art. 23;
  - Ley 27/1999 arts 8 and 15;
  - CC art. 1911.
- Corrected: cooperative "минимум 2 или 3, капитал от 3000 евро" (state law says at least 3 members; capital figure unsourced, removed). The SL "double taxation" disadvantage was reworded neutrally.
- Not added: notary/registry fees of 60/40 EUR (art. 12 Ley 28/2022 depends on model statutes whose approval was not verified).
- Format: TL;DR H2 (7 bullets), H3 hook, two tables, numbered procedure, lists. No FAQ existed. CTA H2 at the end. Brand "Delaguía y Luzón", «с 1960 года», Valencia.
- Links: RU only, all 200: 8364, 2003 (NIE/TIE), 1772 (Beckham), налоговое право, миграционное право, коммерческое право, контакты.
- Rank Math: title «Как учредить стартап в Испании: Закон 28/2022» (45), description 142. Focus keyword «финансирование стартапа в испании» removed (8364's topic).

## Dashes kept: 0

## Open points
- Sibling facts probably shared (EN 14384, ES 14344, FR 14416): 15 % for 4 years (art. 7), ENISA certification, SL 1 EUR, entrepreneur residence (Ley 14/2013 arts 69-70). EN/ES may still carry the old legal-form-only text.
- The stored Rank Math FAQPage schema (not output while rich snippets are off) contains unsourced claims: notary "~150 €", registry "~80 €", and "освобождение от двойной отчётности". Also "Delaguía & Luzón Abogados" as author. Fix before T-02 (Mike).
- The Link Whisper related posts are off-topic and include a 404 (/ru/blog/program-permanent-hiring-qualified-young-people/). Needs a re-scan (Mike).
- Félix/Sonia: whether to add the RETA 100 % bonus for startup founders in pluriactivity (LETA art. 38 quinquies, Ley 28/2022 DF4). It was not added.
