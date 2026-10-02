# 12942 RU инвестиции-в-недвижимость-испании: RU pass (2026-10-02)

Final MD5 36c5a2faa3a558aa6f4e402c27bf47bd, post_modified 2026-10-02 16:55:17. Live verified.

## Changed
- Golden Visa: "stopped at the end of 2024" was wrong; now: all investor routes ended 3 Apr 2025 (LO 1/2025),
  DT1/DT2 stated, renewal scope CTA. Never presented as available; the section heading says it is no longer issued.
- Purchase and ownership taxes from FR 12930 checks (Valencia ITP 9/11 %, VAT 10 %, AJD 1.4 %, 3 % withholding,
  IRNR, imputed income, Modelo 210 annual), RDL 26/2026 investor items (pending), SL/IS.
- Removed: market forecasts, euronews/CBRE figures, the announced 100 % tax, macro and mortgage stats, investor-visa
  service. Excerpt rewritten.

## Open points
- The audit regex flags «золот… виз» in this post: the mention is historical (ended route), as on FR 12930.
- Félix/Sonia: DT2 Ley 14/2013 scope (heading "inmuebles" vs text "inversores"), already escalated with 27307.
- Possible addition for Félix/Sonia to decide: EU sanctions limits relevant to Russian nationals (not added).
- Siblings EN 12852 and ES 12947 (T-10 list) not edited.

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
