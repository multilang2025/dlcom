# 2687 FR statut juridique: rewrite cleanup (2026-10-02)

Live URL: https://delaguialuzon.com/fr/blog/statut-juridique-entreprise/ (Permalink Manager; old slug URL 301s here).
Focus keyword: "statut juridique". Title (H1): "Statut juridique d'entreprise en Espagne 2026 : autónomo, SL, SA, le guide comparatif" (unchanged).

## Version decision

Keep the 2026-05-28 rewrite in `post_content` (newer, TL;DR, comparison table, FAQ) over the live Elementor
version (last revision Nov 2025; it still presents the SLNE and has no sources). The rewrite was cleaned
in place. It stays invisible until the orchestrator removes `_elementor_edit_mode` for the 11-post batch.
`_elementor_edit_mode` and `_elementor_data` were not touched.

## Write

- PUT /wp/v2/posts/2687 (content only), HTTP 200 (no WPML 500 this time).
- post_content MD5 ccdeb089fad089fd60f2be8a3fb355b4 -> **e79369baf5b09d8634f4e53f9e737266** (29 772 bytes),
  post_modified 2026-05-28 11:29:42 -> **2026-10-02 13:05:00**.
- Exact content: `data/staging/2687-rewrite.html` (single line, as stored). Readable source:
  `data/staging/2687-rewrite.src.html`. The original rewrite is in the WP revision created by the PUT.

## Changes

- House rules: "Delaguía y Luzón" (was "Delaguía &amp; Luzón"), "depuis 1960" (was "65 ans d'expertise"),
  office list Madrid/Barcelone/Alicante/etc. removed, office hours removed, all emojis removed, no dashes.
- TL;DR: `<p>` with emoji -> H2 "Statut juridique d'entreprise en Espagne : les points essentiels",
  7 self-contained bullets, house box style.
- Structure: H3 hook + 3 short intro paragraphs; new H2 "Impôt sur les sociétés : les taux applicables en
  2026" with rate table; threshold box replaced by H2 "Passage de l'autónomo à la SL : critères de
  décision" (bullet list + CTA); steps as `<ol>` with a link to pillar 1691 instead of duplicating it
  (C-3); CTA moved before the FAQ; FAQ questions H4 -> H3 (10 kept, D-2 open); headings in noun form.
- Sources inline (target=_blank rel=nofollow noopener): BOE LSC arts 4, 62, 79, 210, 263, 274, 279; LIS
  art. 29 and DT 44; TRLIRNR art. 19; RD 1065/2007 arts 20, 23; Código Civil art. 1911; Ley 14/2013
  art. 8; Ley 18/2022; Ley 7/2024; INE SM note 11/02/2026; Seguridad Social; AEAT IRPF manual. The
  fake "Ley 18/2022" quote was replaced by the verbatim LSC art. 4.1.
- Internal links (FR only, all 200, no self-link, no redirect): 3100 devenir-auto-entrepreneur, 25840
  cotisations RETA, 4371 assujetti-irpf, 2362 SARL/SL, 10023 holding, 1691 créer une entreprise,
  2396 NIE, pages /fr/droit-commercial/, /fr/cabinet-international-avocats/, /fr/contact/.
  No link to 3594 (to be merged into 1691, C-3).

## Fact-check summary (data/factcheck/2687.csv, 27 rows)

- Corrected: SL capital regime (1 € for all; "formation successive" abolished), legal reserve for SL ≥ 3 000 €,
  capital deposit rule, SA governance/audit, IS 2026 rates (19/21 % micro, 23 % ERD; old 23 % claim
  outdated), branch taxation (IRNR), CIF -> NIF, INE figure updated to 2025 (127 533, +7,9 %).
- Removed / CTA: 50 000-60 000 € autónomo/SL threshold, "2 à 6 semaines", IRPF "19-47 %", SL share,
  France comparison, name-certificate count, office hours.

## Open points

- Félix/Sonia: should the firm endorse a profit threshold for the autónomo -> SL switch? It was removed
  (no official source) and replaced by criteria + CTA.
- Rank Math title "Choisir un statut juridique pour votre entreprise en Espagne" (60 chars) and
  description (145 chars) are within limits and do not contradict the rewrite: left unchanged. The title
  does not lead with the keyword (rule "keyword first"): optional tweak for Mike.
- FR typography: regular spaces before ":" / "?" (same as the 13243 precedent), not non-breaking spaces.
- Live old Elementor version still mentions the SLNE until the switch.
- Featured image not reviewed (out of this task).

## QA gate

Scope posts only ✔ · re-read before write, post_modified unchanged ✔ · banned phrases/dashes/emojis/&/65 ans/
offices/free consultation: 0 ✔ · TL;DR H2 first ✔ · CTA before FAQ ✔ · FAQ H3 ✔ (schema mirror: rich-snippet
module off, Mike task) · sources inline, no reference list ✔ · same-locale links 200 ✔ · no `<style>`/`<html>` ✔ ·
trid siblings: none ✔ · live verification after switch: pending (orchestrator).
