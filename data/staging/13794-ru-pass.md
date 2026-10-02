# 13794 RU решение-верховного-суда-туристическ: RU pass (2026-10-02)

Final MD5 c5a3abe9f413e663c8aeb2d464013496, post_modified 2026-10-02 16:46:43. Live verified.

## Changed
- The ruling the post covered is STS 264/2025 of 18 Feb 2025 (CGPJ note 6 Mar 2025, the post's publication date):
  generic residential description does not ban tourist use. "Madrid" removed (not in the official note).
- Added context: Dec 2023 rulings (economic activity bans cover tourist rentals), Oct 2024 Pleno (3/5 can prohibit),
  LO 1/2025 (LPH 7.3 verbatim, 17.12), and the 2026 ruling annulling the national registry (relevant, verified).
- FAQ: 8 H3 questions kept; answers 1 and 3 were wrong after the 2025 reform and are rewritten.
- The Elementor nested-accordion (FAQ in <details> with faq_schema) is replaced by an H3 FAQ in a text-editor, so
  the live FAQPage JSON-LD that Elementor emitted is gone. Ready-to-apply schema: `data/staging/13794-faq-schema.json`.

## Open points
- Mike: apply the FAQ schema when the Rank Math schema module is back (or decide to keep Elementor's accordion).
- EN 13755 cites STS 1025/2025 and 642/2026 (not verified here); FR 13762 still has the "Madrid case" text.

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
