# 1824 RU аренды-в-валенсии: RU pass (2026-10-02)

Final MD5 f528f0cfdd9541d90013faa4a5a8dd11, post_modified 2026-10-02 16:52:03. Live verified.

## Changed
- Angle: long-term residential rental in Valencia (tenant and landlord). Tourist rentals and the registry go to 1135.
- H1 changed from "...2026: правовая база, новый Реестр и обязанности сторон" to "Аренда в Валенсии в 2026 году:
  права арендатора и собственника" (registry framing outdated after STS 19 May 2026); slug unchanged. Excerpt and
  Rank Math description rewritten.
- LAU arts 9/10/11/20/36, RDL 26/2026 and 27/2026 (pending), IRAV, 2 % cap, tensioned zones, Valencian fianza
  deposit (GVA Hisenda), documents, taxes.
- save-page returned HTTP 400 `elementor_save_fatal` (WPML array_filter) but the data committed (SQL + live
  verified). `_elementor_version` meta stayed 3.35.4. The title/excerpt PUT returned HTTP 500 (same WPML fatal,
  class-wpml-element-translation-package.php:354) and committed.

## Open points
- Félix/Sonia: transitional regime of RDL 27/2026 for existing leases; how the new art. 23.2 percentages apply to
  leases signed before 1 Oct 2026 (CTA in text).
- Re-check after the Congress votes on RDL 26/2026 and 27/2026 (TL;DR bullets 6-7, sections on renewal, rent update,
  temporary leases, guarantees, IRPF).
- Whether any Valencian municipality is a declared tensioned zone: not verified (CTA).
- FR 1819 not edited.

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
