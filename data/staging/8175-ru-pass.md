# 8175 RU: Онлайн-бизнес в Испании (RU pass, 2026-10-02)

Live: https://delaguialuzon.com/ru/blog/онлайн-бизнес/ (Elementor builder, single text-editor widget faf9f0a).
Siblings (trid 1253): ES 8179, EN 8552, FR 6658. Not touched.

## Write
- `POST /wpvibe/v1/elementor/save-page`: HTTP 200. SQL readback equals `8175-ru-pass.elementor.json`.
- `_elementor_data` MD5 3467f665… -> **9d46c77a81ff9cba015dcc241990b7aa** (47 652 bytes), post_modified **2026-10-02 16:49:45**. Rollback: `8175-ru-pass.orig-elementor.json`.
- Rank Math description via `/rankmath/v1/updateMeta`. `cache purge`, live verified.

## What changed
- Freshness, checked on the BOE and AEAT:
  - autónomo vs SL (LSC art. 4, CC art. 1911);
  - declaración censal (RD 1065/2007 art. 23);
  - RETA on real income (Seguridad Social);
  - IVA 21 % (LIVA art. 90) and the EU B2C 10 000 EUR threshold (art. 73);
  - OSS union regime and form 369 (art. 163 duovicies, AEAT G420);
  - LSSI-CE arts 10, 21 and 22.2;
  - RGPD and LOPDGDD;
  - 14-day withdrawal right (TRLGDCU arts 102-104);
  - Verifactu: 1 Jan 2027 for IS taxpayers, 1 Jul 2027 for others (RD 1007/2023 DF 4 as amended).
- Removed: marketing and HR filler, brand lists (SEUR, Correos, Shopify, WooCommerce, PrestaShop, Facebook, Twitter), exclamation-mark sales tone, the editor's inline `<span style>` leftovers and "Delaguía&amp;Luzón" (twice).
- Format: TL;DR H2 (7 bullets), H3 hook, IVA table, lists, short practical section. No FAQ existed. CTA H2 at the end.
- Links: RU only, all 200: 14460, 8364, 24774 (субсидии для самозанятых), 8407 (бухгалтер), трудовое право, коммерческое право, налоговое право, контакты.
- "бесплатный доступ" in the LSSI paragraph quotes the law's requirement ("acceso gratuito"). It is not a free-consultation claim.

## Dashes kept: 0

## Open points
- The stored Rank Math FAQPage schema (not output) is wrong. It presents the SLNE as current, mentions a "Реестр LSSICE" that does not exist and states an autónomo threshold of "~30 000 €". Fix before T-02 (Mike).
- Sibling facts probably shared (ES 8179, EN 8552, FR 6658): OSS 10 000 EUR, Verifactu dates, LSSI.
- The Link Whisper related posts are off-topic, with a 404. Needs a re-scan (Mike).
