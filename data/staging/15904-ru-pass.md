# 15904 RU ндс-квартиры-туристы-испания: RU pass (2026-10-02)

Final MD5 96b768281138f8012d4d0f88b25c779f, post_modified 2026-10-02 16:49:00. Live verified.

## Changed
- Current rule (LIVA art. 20.Uno.23, AEAT lists) and RDL 26/2026 art. 7 (10 % on furnished stays of 30 nights or
  less, not the lessor's habitual residence, from 1 Dec 2026, pending validation by Congress, art. 86 CE) + CTA.
- Wrong facts fixed: "two or more services", IAE 861.1 (is group 685), Modelo 037 (abolished 3 Feb 2025),
  "EU makes VAT mandatory from 1 Jul 2028" (ViDA deemed-supplier rule, 2028 or 2030), July 2025 registry code.
- Unverifiable removed: 21 % ancillary rate, 4-year retention, prorrata method (CTA instead).

## Open points
- Re-check after the Congress vote on RDL 26/2026 (TL;DR bullets 4-5 and the 1 Dec 2026 section).
- Spain's transposition of ViDA (2028/2030) to watch.
- Siblings EN 15852, FR 15895 probably carry the same wrong claims.

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
