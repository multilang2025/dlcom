# 12930 FR investir-en-espagne: rewrite cleanup (2026-10-02)

**Version decision:** the 2026 rewrite in `post_content` (base).
- The Elementor body (edited 2026-01-27) is weaker. It has the "Golden Visa supprimé depuis fin 2024" error, "Delaguía & Luzón", a "Conclusion" H2 and a link to maisonreno.fr.
- It also has sector paragraphs on renewables, tourism, crypto and agriculture with unsourced stats.
- Only the crypto angle was kept: one sentence with a link to FR 11817 `/fr/blog/cryptomonnaies-et-entreprises-en-espagne/` (orchestrator request).

**Written:** PUT /wp/v2/posts/12930 (content only), 2026-10-02 13:18:13. MD5 988f2f57 -> 793f3c8c (= `data/staging/12930.html`).
- WordPress rewrote the 3 page links (cabinet, contact, droit-immobilier) from `href='…'` to `href="…"`. That is the only difference from the submitted file.
- `_elementor_data` (MD5 229f63f0) and `_elementor_edit_mode=builder` were not touched.

## Changes
- TL;DR: emoji `<p>` -> H2 "Investir en Espagne : les points essentiels" with 7 bullets. H3 hook added.
- **Golden Visa:**
  - LO 1/2025 DF 21.1 emptied Ley 14/2013 arts. 63 to 67 from 03/04/2025, so *all* investor routes ended, not only real estate.
  - DT1 and DT2 are stated; the fabricated "Quedan derogados…" quote was replaced by the verbatim DT2.
  - The FAQ claim "financial routes remain" was removed.
  - The EUR 500k threshold is kept as historical.
- Purchase costs: Valencia ITP 9 % (11 % above EUR 1M) from 01/06/2026, AJD 1.4 % (0.1 % for a habitual residence), VAT 10 % (LIVA art. 91). Other regions differ, so the post gives a CTA. The 10-14 % total was removed.
- IRNR:
  - Rents taxed at 19 % or 24 %; gains at 19 % for all non-residents.
  - Buyer withholds 3 % when the seller is non-resident.
  - Modelo 210 is annual, with the Orden HAC/623/2026 deadlines.
  - Imputed income kept, with a CTA on the RDL 26/2026 scale change from 2027.
- Company: SL from 1 EUR. The "formation successive" regime was abolished; the 20 % reserve and EUR 3,000 liability rules are stated. IS 15 % made precise.
- NIE: RD 1155/2024 art. 205.
- RDL 26/2026 investor items added (all pending validation):
  - VAT on rentals of 30 nights or less;
  - IBI surcharge option for tourist flats;
  - limit on entity purchases below 70 % of appraisal value until 2028;
  - SOCIMI regime change.
- Removed (unverifiable):
  - Market prices, the Eurostat figure and yields.
  - Mortgage LTV and rate figures.
  - The claim that Madrid, Barcelona and Palma issue no new licences (replaced by RD 1312/2024 and LPH art. 7.3).
  - The Swiss and 183-day claims.
  - The 8-12 % crowdfunding yield and EUR 500 ticket.
- CTA moved before the FAQ; FAQ items changed to H3 (10 kept, the "tendance du marché" question became "nouveautés 2026"). Brand, "depuis 1960", Valencia only; no emojis.
- Internal links (all 200, FR): acheter-maison-communaute-valencienne, location-bien-immobilier-espagne, decret-logements-touristiques-communaute-valencienne, crowdfunding-immobilier-espagne, convention-fiscale-franco-espagnole, tout-savoir-de-limpot-sur-la-plus-value-immobiliere-en-espagne, statut-juridique-entreprise, cryptomonnaies-et-entreprises-en-espagne, visa-nomade-digital-espagne, residence-en-espagne-voies-acces, rentabilite-locative-espagne, pourquoi-comment-obtenir-nie-espagne, creer-une-entreprise-en-espagne.

## Open points
- **Flag for Mike:** the focus keyword "investir en espagne" is a verb phrase, so the TL;DR H2 and an H2 keep the verb.
- **Félix/Sonia:** DT2 scope (heading says "inmuebles", text says all investors). Already escalated with 27307; the post follows the text.
- **Siblings EN 12852, ES 12947 and RU 12942** (T-10 Golden Visa list) are not edited. They probably carry the same Golden Visa scope error and the quarterly Modelo 210 claim.
- **Re-check after the Congress vote** on RDL 26/2026 (repeal would affect the "Repères" box, the SOCIMI card and FAQ 9).
- Rank Math title (58) and description (152) are OK and left unchanged.
- Ready for the edit-mode switch: **yes**.
