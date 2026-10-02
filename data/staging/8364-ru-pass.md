# 8364 RU: Финансирование стартапов (RU pass, 2026-10-02)

Live: https://delaguialuzon.com/ru/blog/стратегии-финансирование-стартапы/ (Elementor builder, single text-editor widget af72226).
WPML: own trid 1328 (RU only). The same article exists in trid 1310 (ES 7708, EN 8357, FR 8361), but 8364 is not linked to it.

## Write
- `POST /wpvibe/v1/elementor/save-page`: HTTP 200. SQL readback equals `8364-ru-pass.elementor.json`.
- `_elementor_data` MD5 d44f8332… -> **69263ecd64a62f3405a450da1f8f6880** (46 231 bytes), post_modified **2026-10-02 16:48:34**. Rollback: `8364-ru-pass.orig-elementor.json`.
- Rank Math description via `/rankmath/v1/updateMeta`. `cache purge`, live verified.

## What changed
- Freshness:
  - Investor deduction under LIRPF art. 68.1 as amended by Ley 28/2022: 50 % on a base of up to 100 000 EUR, own funds of 400 000 EUR at most, investment within 5 years (7 for startups), holding of 3 to 12 years, 40 % limit (founders of a startup exempt), company certificate, and no overlap with regional deductions. Verified on the BOE consolidated text.
  - Participative loans: RDL 7/1996 art. 20 (BOE).
  - ENISA conditions (no guarantee; own funds at least equal to the amount requested), taken from the ENISA site on 2026-10-02 and dated. Loan amounts were not used because they change.
  - Crowdfunding under Reg. (EU) 2020/1503, reusing 7335.csv and re-reading the DOUE text (arts 2, 21.7, 22.3).
  - Ley 22/2014 on venture capital.
  - Non-resident investor NIF (Ley 28/2022 art. 9).
- Removed: Kickstarter link and the reward-platform list (outside the ECSP scope), «В заключение следует отметить», «Delaguía&amp;Luzón».
- Angle: financing only. Setup and the startup tax regime are left to 14460, and the two posts cross-link.
- Format: TL;DR H2 (7 bullets), H3 hook, lists, stage table. No FAQ existed. CTA H2 at the end, plus a CTA after the deduction conditions.
- Links: RU only, all 200: 14460, коммерческое право, налоговое право, контакты.

## Dashes kept: 0

## Open points
- WPML: link 8364 to trid 1310 (ES 7708 / EN 8357 / FR 8361) so that the language switcher and hreflang work. This is a WPML task (Mike). The investor deduction and ECSP facts are probably shared with those siblings.
- The stored Rank Math FAQPage schema (not output) lists unsourced figures: "CDTI до 70%", "ENISA 25 000-1,5 млн €", "IVF", "Avalmadrid". Fix before T-02 (Mike).
- The Link Whisper related posts link to the post itself and include a 404 (/ru/blog/программа-постоянного-трудоустройст/). Needs a re-scan (Mike).
- Félix/Sonia: no interpretation was added. The deduction conditions are a direct summary of art. 68.1.
