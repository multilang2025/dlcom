# 2823 FR location-bien-immobilier-espagne: rewrite cleanup (2026-10-02)

**Version decision:** the May 2026 rewrite in `post_content` (base) over the old Elementor body. The Elementor body is older, unsourced, has "Delaguía & Luzón", a "3 ans" renewal FAQ and IPC-based rent update advice. Nothing in it was worth porting, apart from internal links that the rewrite already covers.

**Written:** PUT /wp/v2/posts/2823 (content only), 2026-10-02 13:14:42. MD5 25c578b4 -> 5faa76c8 (= `data/staging/2823.html`). `_elementor_data` (MD5 c4576439) and `_elementor_edit_mode=builder` were not touched, so the page still renders Elementor until the switch.

## Changes
- TL;DR: emoji `<p>` -> H2 "Mise en location d'un bien immobilier en Espagne : les points essentiels" with 7 self-contained bullets. H3 hook added.
- Law updates: **RDL 26/2026** (BOE 30/09/2026, in force 01/10) and **RDL 27/2026** (BOE 01/10/2026, in force 02/10), both pending Congress validation (CE art. 86).
  - Renewal: successive 5/7-year periods plus a landlord indemnity of at least 12 months.
  - Temporary leases: cause required, over 31 days, 12 months as a rule.
  - Guarantees: 2 months, or 1 month for temporary leases; the tenant cannot be required to buy rent-default insurance.
  - New end-of-lease document; rents in successive temporary leases are capped by IRAV; room-by-room rents are capped by the whole-flat rent.
  - DF6 2 % default cap until 31/12/2027; new LIRPF art. 23.2 reductions (15 % to 100 %); VAT on rentals of 30 nights or less from 01/12/2026; eviction suspension until 2030.
- Wrong or outdated content fixed:
  - "RDL 8/2026 keeps 2 %": it was repealed in April 2026.
  - Tensioned-zone criteria and gran tenedor definition corrected.
  - Modelo 210: annual since the 2024 accrual year (Orden HAC/623/2026).
  - SL tax rates corrected.
  - The fake LAU art. 18 quote was replaced by the verbatim text.
- Removed (unverifiable): IRAV 2.16 % monthly figure, 2 %/3 % history, "BOE 17 avril 2026", yield box (idealista).
- Sources are inline on BOE, INE and AEAT links (`nofollow noopener`, `_blank`). No reference list.
- CTA moved before the FAQ. FAQ items changed from h4 with emoji to H3; the 10 questions are kept.
- House style:
  - Brand written "Delaguía y Luzón", "depuis 1960".
  - Valencia office only: the Madrid/Barcelone/Alicante/... office list is removed.
  - No emojis; FR non-breaking spaces as `&nbsp;`.
- Internal links (all 200, FR): loi-12-2023-du-24-mai-pour-le-droit-au-logement, impots-sur-le-revenu-en-espagne, bien-immobilier-non-loue-en-espagne, rentabilite-locative-espagne, investir-en-espagne, convention-fiscale-franco-espagnole, locations-courte-duree-espagne, decret-logements-touristiques-communaute-valencienne, plus the /fr/droit-immobilier/, /fr/contact/ and /fr/cabinet-international-avocats/ pages.

## Open points
- **Félix/Sonia:** how the new art. 23.2 reductions apply to leases signed before 01/10/2026. The post gives a CTA instead of an answer.
- **Félix/Sonia:** the RDL 27/2026 transitional regime. The post gives a CTA.
- **Re-check after the Congress vote** on RDL 26/2026 and 27/2026 (deadline 30 days from promulgation, around late October 2026). If either decree is repealed, rewrite the TL;DR bullets 3 and 4, card 1, the art. 10 paragraphs, Conseil 7 and FAQ 1, 2, 6, 8 and 10.
- EN sibling 2869 (`renting-property-in-spain`) probably carries the same outdated claims (Modelo 210 quarterly, RDL 8/2026, renewal of 3 years). Not checked.
- Inbound: 9 FR posts already link here. No change.
- Rank Math title (58) and description (146) are OK and left unchanged. Focus keyword "bien immobilier" is weak; that is Mike's call.
- Ready for the edit-mode switch: **yes**.
