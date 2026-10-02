# 8402 (FR) Engager un comptable à Valencia: post_content rewrite cleanup, 2026-10-02

- URL: https://delaguialuzon.com/fr/blog/engager-comptable-valencia/ (unchanged)
- Focus keyword "engager un comptable à Valencia" is a verb phrase (FR noun-form rule): flag to Mike. The H1 ("Comptable
  qualifié à Valence 2026 : ...") does not contain it; not changed (outside this task). Title tag 56, description 155: OK.

## Version decision
The 2026 rewrite in `post_content` is the base (Verifactu, e-invoicing, obligations); the Elementor version is older and
generic. `_elementor_data` / `_elementor_edit_mode` untouched.

## Changes
- TL;DR H2 "Engager un comptable à Valencia : les points essentiels" + 6 bullets; FAQ H4 -> 10 H3 (count unchanged).
- Removed: emojis, "&" brand, "65 ans", offices list incl. Madrid/Barcelone, hours, Valencia marketing claim, flex boxes
  turned into lists.
- Corrected facts: see `data/factcheck/8402.csv` (17 rows). Main ones: RD 238/2026 date and trigger (12/24 months after a
  ministerial order not yet in BOE, exact dates sent to the CTA), spreadsheet nuance, 80-day delay replaced by Banco de
  España data, INE 2025, autónomo books (art. 68 RIRPF).
- Internal links: 4844, 27325, 3496, 3100, 11817, /fr/droit-fiscal-et-comptabilite/ (200, no redirect).
- Inbound links already exist: 2297, 3496, 20166, 15202 (+11817 after the switch).

## Result
- post_content MD5 `5496e311cfdeaa089790dcd0718de316`, post_modified 2026-10-02 13:14:45. Revision 28026 = staged
  (`ae40c8a6...`); the save filter re-quoted the 3 CTA page links. Rollback: revision 25578.

## Open points
- E-invoicing start dates: re-check BOE for the Hacienda order (draft: entry into force 1 Oct 2026, which would give
  1 Oct 2027 / 1 Oct 2028). Update the post when it is published.
- Siblings ES 7717, EN 8398, RU 8407 not fact-checked.
