# 7335 FR crowdfunding-immobilier-espagne: rewrite cleanup (2026-10-02)

**Version decision:** the May 2026 rewrite in `post_content` (base). The Elementor body is generic and unsourced, and it links to a third-party site (ooinvestir.fr). Nothing in it was worth porting.

**Written:** PUT /wp/v2/posts/7335 (content only), 2026-10-02 13:16:27. MD5 3b6a8151 -> 8e93a627 (= `data/staging/7335.html`). `_elementor_data` (MD5 592dd7e9) and `_elementor_edit_mode=builder` were not touched.

## Changes
- TL;DR: emoji `<p>` -> H2 "Crowdfunding immobilier en Espagne : les points essentiels" with 7 bullets. H3 hook added.
- ECSP facts checked against the Spanish OJ text (`DOUE-L-2020-81532`):
  - Art. 1.2.c: EUR 5M scope.
  - Art. 14: ESMA register.
  - Art. 18: cross-border provision by notification.
  - Art. 21: knowledge test and loss simulation; art. 21.7 warning above the *higher* of EUR 1,000 or 5 % of net worth.
  - Art. 22: 4 calendar days to withdraw.
  - Art. 23: KIIS.
  - Art. 25: bulletin board.
- Ley 18/2022 replaced Ley 5/2015 Title V from 10/11/2022. The post no longer calls it a "transposition".
- Tax table corrected:
  - EU/EEA residents: interest is IRNR-exempt (art. 14.1.c); gains on shares in a company that mainly holds Spanish real estate stay taxable at 19 %.
  - Non-EU residents: 19 %, not 24 % (art. 25.1.f).
  - IRPF savings scale verified: 19, 21, 23, 27 and 30 %.
- Removed (unverifiable or non-approved sources): +20 % volume in 2025, USD 1.07tn (Facts Factors), "27 plateformes", EUR 500 ticket, 8-12 % yields, 12-36 months lock-up, trends box, "retenue à la source".
- The art. 1 quote in French could not be verified (EUR-Lex blocks bots). It was replaced by the verified Spanish OJ text.
- CTA moved before the FAQ; FAQ items changed to H3 (10 kept). Brand, "depuis 1960", Valencia only; no emojis.
- Internal links (all 200): investir-en-espagne, convention-fiscale-franco-espagnole, la-fiscalite-espagnole-tout-savoir-avant-de-s-expatrier, investir-immobilier-espagne (3013, which still has the forbidden garrigues link: T-13), plus the droit-immobilier, contact and cabinet pages.

## Open points
- **No inbound FR links** to this post except 12930 (after its switch). Candidates to link from, not done because they are other live posts outside this task:
  - 3013 `investir-immobilier-espagne`
  - 2519 `rentabilite-locative-espagne`
  - 25839 `convention-fiscale-franco-espagnole`
- No trid siblings.
- Rank Math title (60) and description (153) are OK and left unchanged.
- Ready for the edit-mode switch: **yes**.
