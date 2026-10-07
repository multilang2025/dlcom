# FR 25840: cotisations-autonomos-2026-baremes-reta (full rewrite, 2026-10-06)

Mike approved "rewrite 25840" on 2026-10-06. Model: FR 10629. Facts: `data/staging/25840-factcheck.md` and
`data/factcheck/25840.csv`. Exact stored HTML: `data/staging/25840-rewrite.html`. Nothing git-committed.

## State

- post_content MD5 `23abee85399ddad0d4a7f32492cce4ea` -> **`02a9dd1f09f8892b2c6d7378a05de5b8`** (39 806 -> 41 035 bytes),
  identical to the local file (SQL read-back). post_modified 15:38:57 -> **2026-10-06 18:41:29** (body), 18:41:57 (title/excerpt).
- Revisions: **28303** = previous version (rollback source, contains the old CSS and old claims), **28314** = new body,
  28315 = title/excerpt save.
- Rendering: no Elementor (`_elementor_edit_mode` empty), content wrapped in `<!-- wp:html -->`. No WPML siblings (trid 3076).
- URL: BEFORE and AFTER identical. REST `link` https://delaguialuzon.com/fr/blog/cotisations-autonomos-2026-baremes-reta/,
  `permalink-manager-uris[25840]` = `blog/cotisations-autonomos-2026-baremes-reta` (read only), live 200, 0 redirects.
- H1 changed (only "80 €" removed): "Cotisations autonomos 2026 en Espagne : 15 tranches RETA, tarifa plana et régularisation TGSS".
- Rank Math title (58): "Cotisations autonomos 2026 : tranches RETA et tarifa plana". Description (144) without "&" and without "80 €".
  Excerpt 239 chars. Focus keyword unchanged.

## What changed

- Removed: both `<style>` blocks (scoped + the inert `media="not all"` one), all `article-wrapper` classes, the `<details>` FAQ,
  the glyph decorations, the "Correction factuelle" footer, the "Delaguía y Luzón — ..." em dash, the marketing section about
  Valencia, the political narrative, "88,64 €", "6 à 46 €", the expired "30 avril 2026" date, "30 jours", the recurso de
  alzada claim, "dernière décennie", the cumulation claim, the cuota cero list of regions, "plus d'un million et demi".
- New structure: TL;DR H2 (7 bullets) first, H3 hook, 8 noun-form H2 sections (system, 15 tranches, tarifa plana,
  regularisation, change of base, examples, errors and practices, Valencian aid), grey CTA box before a 9-question H3 FAQ,
  dated footer. 5 inline-styled tables/box blocks, 3 lists with `margin:0 0 1em 1.4em`, 3 blockquotes with verbatim Spanish
  law (RDL 3/2026 art. 3.4 last sentence; DT 5a RDL 13/2022, two sentences). Quotes copied from the raw BOE text, not from a summary.
- Links: 16 distinct official sources on descriptive anchors (`target="_blank" rel="nofollow noopener"`) and 7 FR-only
  internal links (3100, 1691, 8655, 13243, 3213, 4371, 25839) plus /fr/contact/, /fr/cabinet-international-avocats/,
  /fr/droit-fiscal-et-comptabilite/. All 200, no redirect.
- `&nbsp;` before `: ; ? !`, inside « », in amounts and thousands.

## Facts corrected or CTA'd

Corrected (all re-opened on official pages today): 3 reduced + 12 general tramos; 15 cuotas at 31,50 % (205,88 to 607,35 €,
own arithmetic, labelled); max base of tramos 11 and 12 = 5 101,20 € (4 909,50 € in 2025); MEI 0,80 -> 0,90 % = +0,65 to
+5,10 €; RDL 3/2026 official reasons + validation of 26/02/2026; regularisation (pay by the last day of the month after the
notification, 10 natural days to read, refund before 30 April of the following year, regla 3, regla 5 = group 7 minimum base);
maintaining a higher base (Importass); art. 30 and 38 LETA bonuses; art. 38 ter.4, .6, .10; SMI 1 221 € / 17 094 €; TRRETA
2025 closed. Examples recomputed: 1 800 € = tranche 7 = 360,29 €; 3 000 € = tranche 11 = 452,94 €.

CTA "contactez le cabinet": tarifa plana amount and conditions for an alta in 2026 (TL;DR 5, section 3, examples, FAQ 3), cumulation
with art. 30 and 38 bonuses (FAQ 9), appeal route against a regularisation resolution, pension effect of a higher base,
regional aid and cuota cero (no statement either way for Valencia), which 3 % / 7 % deduction applies.

The only "80 €" in the body (3 mentions) are dated "2023 à 2025", in TL;DR 5, section 3 and FAQ 3. None in H1, headings,
boxes, examples, Rank Math or the excerpt.

## Open points for Félix / Sonia (via Mike)

1. Does the firm have a TGSS confirmation that 80 € applies to altas of 2026? Secondary sites say yes; the official texts say
   2023 to 2025 only. Also whether the MEI is added on top of the reduced cuota.
2. Valencian cuota cero announced 28/09/2026: left out (no official GVA text). Add once a DOGV text exists.
3. Appeal route against a TGSS regularisation resolution (the old recurso de alzada claim is gone).
4. Pension effect of a higher base (art. 209 LGSS and transitional rules): left as a CTA.
5. "Societarios" 3 % wording (administrator >= 25 %, partner >= 33 %, from the Seguridad Social page): confirm they want it published.
6. Cumulation of tarifa plana with the art. 30 and 38 bonuses.
7. The 0,10 % extra (no AT/EP cover) and the 0,055 coefficient (IT covered elsewhere) are stated from art. 18.2 of the Orden; confirm the firm wants them.

## For Mike

- Slug still carries the year (house rule: never). Not changed: needs a 301 and your approval.
- Siblings not edited (other owners): ES 27855 (80 €, "15 tramos 200 a ~590 €", 88,56 €, cuota cero in Valencia), ES 24717,
  FR 24773 ("80 € en vigor", FR link target for a future "aides" cross-link), EN 4160, EN 25362. They likely share the same
  80 € / 15-tranche errors.
- Inbound links already exist from FR 2687 and 13243. A third (for example from 24773 once corrected, or 3100) would meet the
  "2 or 3" rule; not added (not requested, other posts).
- Not done: FAQPage JSON-LD (house rule says mirror the FAQ; no schema on this page, same as 10629), the site-wide
  "Delaguía & Luzón" in the LegalService schema (Rank Math, outside the Scope Gate), featured image check.
- Re-check (already in TASKS.md): tarifa plana 2026/2027 amount (LPGE or royal decree-law), 2027 contribution order (MEI 1,00 %),
  Valencian cuota cero text.
- If rollback is needed: restore revision 28303 (then neutralise its style blocks again).

## QA gate

| Check | Result |
|---|---|
| Scope | post only; no page, template or plugin setting |
| Re-read before write | yes, MD5 and post_modified unchanged since staging |
| Dashes, emojis, glyphs, "&", 65 ans, free consultation | 0 (checked in stored and live body) |
| TL;DR first, CTA before FAQ, FAQ as H3 | ok (9 questions) |
| Inline sources, no list at bottom | ok |
| `<style`, `<details`, `<h1` in body | 0 |
| Live | 200, 1 H1 (new title), new TL;DR present, old claims absent, list items measured 22 px from their container (disc), no horizontal overflow |
| Links | 23 distinct, all 200, 0 redirects |
| WPVibe calls | 5 writes/reads: GET (state), PUT body, PUT title/excerpt, updateMeta, cache purge; everything else via AISA `db_query` and curl |
