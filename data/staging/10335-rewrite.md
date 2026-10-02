# 10335 (FR) reglement-eidas: post_content cleanup for the rendering switch

- URL: https://delaguialuzon.com/fr/blog/reglement-eidas/ (200). WPML trid 1444: ES 10318 `autenticacion-eidas`, EN 10351 `eidas-authentication`, RU 10376.
- Before: post_modified 2026-05-28 11:15:41, post_content MD5 8003b56230c6728269746a6ef766e8cb (30 198 bytes), `_elementor_data` MD5 c021ec1039e246cf808eccc20d8a0a30 (10 463 bytes), mode builder.
- After (2026-10-02): post_modified 2026-10-02 13:10:59, post_content MD5 **6eac1327cf64c5a2ca20e04b1dbf5fe0** (29 471 bytes). `_elementor_data` and `_elementor_edit_mode` were not touched (MD5 re-checked). Written with `PUT /wp/v2/posts/10335` (content only, no 500). The readback equals `10335-post_content-as-sent.html` except for 4 internal `href` attributes: a plugin rewrote their single quotes as double quotes on save, which is harmless.

## Version decision

**post_content (the 2026 eIDAS 2.0 rewrite) kept.** The Elementor version is an older, shorter article (10 KB) on AEAT access with eIDAS since 2 October 2024. It is not newer, but it held one useful verified fact that the rewrite had lost, so that fact was ported natively as a new H2, "Démarches fiscales en ligne : l'accès eIDAS à l'Agencia Tributaria", with the AEAT source. The H2 covers the list of procedures and the requirement for a Spanish identifier (DNI, NIE, NIF L or NIF M). The old claim that AEAT will drop the identifier requirement was not ported, because the AEAT source doesn't say it.

## Changes

- TL;DR rebuilt: H2 "Règlement eIDAS : les points essentiels" with 7 self-contained bullets. Then an H3 hook and the intro.
- Emojis removed. CTA moved before the FAQ. FAQ items moved from H4 to H3, 10 kept.
- CTA: "depuis 1960", "Delaguía y Luzón", the Valencia office only, no "65 ans d'expertise" and no office list.
- Art. 5 bis: the false "quote" became a sourced paraphrase box (paras 1, 13 and 15).
- Art. 25: the quote was put in the official wording.
- Timeline and stat box: the 80 % 2030 target was replaced by the Digital Decade target (100 % access to eID, Decision 2022/2481). The speculative "hybrid period of 5 to 10 years" and "end 2025" milestones were removed. Rows were added for the 24/12/2024 implementing acts and for AEAT (02/10/2024).
- Property: the claim that a qualified signature gives "full legal value" for property contracts was corrected. The notarial escritura is still required for registration, and a CTA was added.
- VLOPs no longer get the 2027 deadline: art. 5f(3) sets none.
- Generic eur-lex.europa.eu homepage links were replaced by specific BOE (OJ copy), EUR-Lex 910/2014, AEAT and Decision links. BOE carries the official OJ text, and EUR-Lex blocks automated fetching.
- Internal links: 8, all /fr/ and all HTTP 200. Added /fr/blog/impots-sur-le-revenu-en-espagne/ and /fr/droit-fiscal-et-comptabilite/.
- Rank Math: the title (60 chars) and the description (149 chars) were rewritten, because the old ones described only the AEAT article.
- Inbound links (the post had 0): added from 2678 (Modelo 720, anchor "règlement eIDAS") and 2645 (fiscalité expatriés, anchor "identité numérique eIDAS"). Both are live in `_elementor_data` and verified.

## Fact-check summary (data/factcheck/10335.csv, 17 rows: 7 OK, 6 corrected (2 WRONG, 4 UPDATE), 4 UNVERIFIABLE removed)

- Corrected:
  - the 80 % target (WRONG);
  - the art. 5 bis pseudo-quote;
  - the scope and deadline of private-sector acceptance (micro and small enterprises excluded, user's request, no deadline for VLOPs);
  - the property and bank claims;
  - the art. 25 wording.
- Removed as unverifiable: the 26/03/2024 adoption date, the "end 2025" milestone, the hybrid period, PID availability and delays.
- OK: the 2024/1183 dates (signed 11/04, OJ 30/04, in force 20/05/2024), the 24-month wallet deadline through the implementing acts of 24/12/2024, voluntary and free use, the new trust services, the AEAT facts.

## Open points

1. **Propagation to siblings.** ES 10318, EN 10351 and RU 10376 are versions of the old AEAT article. Check them for the unverified "AEAT will drop the Spanish identifier requirement" claim. Each locale owner should do this natively.
2. **Rank Math schema (do at switch time):**
   - `rank_math_schema_WebPage`: "Découvrez" and "Delaguía &amp; Luzón";
   - `rank_math_schema_Article`: "Delaguía &amp; Luzón" with an author of type Person, and a "Logo-65" image;
   - `rank_math_schema_LegalService`: "&amp;".
   - There is no FAQPage schema. A 10-question FAQPage that mirrors the new FAQ is ready in `data/staging/10335-faq-schema.json`.
3. Until the switch, the live title and description (eIDAS 2.0) sit on top of the old AEAT body. The mismatch is minor, because the old body is about eIDAS too.
4. Post 2678 still uses "Delaguía & Luzón" elsewhere in its body. This is out of scope here: it should go on the brand-sweep task.

**Ready for the rendering switch: yes**, after Mike's approval.
