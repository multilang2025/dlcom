# 1135 RU airbnb-валенсия: RU pass (2026-10-02)

Final `_elementor_data` MD5 f3fe743c88ed9fa0cd4603f97646a20b, post_modified 2026-10-02 16:43:10. Live verified.

## Changed
- Freshness: registration regime (Ley 15/2018, DL 9/2024, Ley 3/2026), LPH reform 2025, RD 1312/2024 annulled,
  Reg. 2024/1028, Modelo 210 annual, fines. Unverified district list removed.
- Naturalness/format: rewritten natively; TL;DR 7 bullets; 9 H2; numbered procedure; fines table; LPH verbatim
  blockquote; meta opener and «Вывод» removed; no FAQ added (post had none).
- CTA box before the end + dated closing line.

## Open points
- Félix/Sonia: national registry numbers already issued and the Orden VAU/1560/2025 return after STS 19 May 2026
  (CTA in text); scope of LPH DA 2ª for flats operating before 3 Apr 2025; pre-2018 Valencian registrations.
- City of Valencia municipal VUT rules: only the January 2025 draft is documented officially; post gives no figures.
- Re-check after the Congress vote on RDL 26/2026 (VAT bullet in the tax section).
- Siblings EN 991, FR 1130 not edited.

## Common to the five RU property posts (2026-10-02)

- Write path: `POST /wpvibe/v1/elementor/save-page`, existing container and text-editor widget ids kept; old
  heading/text widgets collapsed into one text-editor (same as 12942/15904 already were). `_elementor_edit_mode`
  stays `builder`; rendering not switched.
- Rollback: WordPress revisions hold the previous `_elementor_data` (1135: rev 24485; 1824: rev 25170, also the May
  post_content rewrite; 12942/13794/15904: latest pre-2026-10-02 revisions). Staged JSON as sent:
  `data/staging/<id>-ru-pass.elementor.json`; rendered HTML: `data/staging/<id>-ru-pass.html`.
- Side effect: an Elementor save rewrites `post_content` with a mirror of the new body. For 1824 this replaced the
  unused May 2026 rewrite (27 432 B -> 19 073 B); the May text is in revision 25170. Nothing in it was worth keeping
  as is (3-year renewal, 60 %/90 % IRPF, RAU registry, "65-летним опытом", Olesia Davidova contacts).
- Dashes: 0 em/en dashes kept in the five bodies (all copula dashes rephrased).
- Sources: inline anchors, `target="_blank" rel="nofollow noopener"`, Spanish official sources (BOE, AEAT, INE,
  GVA Hisenda, poderjudicial.es, valencia.es) plus EUR-Lex and the European Commission ViDA page for EU rules.
  EUR-Lex answered 202 (bot challenge) to curl; the regulation link is the standard ELI and was verified by FR.
- Internal links: RU only, all 200 (the tax practice URL /ru/налоговые-услуги/ 301s to a non-RU URL, so the
  200 URL /ru/налоговое-право-и-бухгалтерский-учет/ is used). The five posts cross-link each other, so each
  gets 2 to 4 inbound RU links. Related-posts block: all RU.
- CTA: +34 963 74 16 57, felix.delaguia@delaguialuzon.com, /ru/контакты/ (200). The live contact page also shows
  +34 96 352 32 91.
- Rank Math schema (stored, NOT output while the rich-snippet module is off) is stale on 1135, 13794, 1824, 12942,
  15904: Article author "Delaguía & Luzón Abogados", image Logo-65, and custom FAQPage items with wrong facts
  (13794: "STS 1671/2024"; 12942: "AJD 1,5%"; 1135: "постановление 2024 г."). Not edited (schema out of scope).
- audit_blog.py --lang ru rewrote data/audit_baseline.csv with RU rows only; the HEAD rows of other locales were
  merged back and only RU rows changed.
