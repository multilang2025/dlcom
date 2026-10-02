# 18814 FR restructuration d'entreprise: rewrite cleanup (2026-10-02)

Live URL: https://delaguialuzon.com/fr/blog/restructuration-entreprise-espagne/
Focus keyword: "restructuration d'entreprise en Espagne". Title (H1): "Restructuration d'entreprise en Espagne
2026 : Ley 16/2022, plan préventif et insolvabilité" (unchanged).

## Version decision

Keep the 2026-05-28 rewrite in `post_content` (newer, built on Ley 16/2022) over the live Elementor version
(Nov 2025; question headings, a "Delaguía & Luzón" heading, no TL;DR box). The rewrite needed
heavy legal correction: it was cleaned in place. Invisible until the orchestrator removes
`_elementor_edit_mode`. `_elementor_edit_mode` and `_elementor_data` were not touched.

## Write

- PUT /wp/v2/posts/18814 (content only), HTTP 200.
- post_content MD5 e29e3189a6c1f7c6f70055b524fac6e3 -> **fe475543b9126fcba25679b52fc76b51** (29 576 bytes),
  post_modified 2026-05-28 11:27:04 -> **2026-10-02 13:06:46**.
- Exact content: `data/staging/18814-rewrite.html`; readable source `data/staging/18814-rewrite.src.html`.

## Changes

- House rules: brand, "depuis 1960", fake offices and hours removed, emojis removed (incl. the coloured
  circles in the insolvency cards), no dashes.
- TL;DR: H2 "Restructuration d'entreprise en Espagne : les points essentiels" + 7 bullets.
- Structure: H3 hook + intro; noun-form H2s; "Plan de paiement : de 5 ans à 3 ans" rebuilt as H2 "Seconde
  chance : exonération et plan de paiement des personnes physiques"; third stat box (notarial route,
  AEAT scrutiny) deleted; CTA before FAQ; FAQ H4 -> H3 (10 kept).
- Sources inline: BOE TRLC article anchors (2, 5, 45, 226, 442/444, 456, 486, 489, 497, 583, 584, 585,
  600/601, 605, 607, 614, 623/625, 629, 635, 639, 654/655, 685), Ley 16/2022, Estatuto de los
  Trabajadores arts 47/51, EUR-Lex Directive 2019/1023. Both blockquotes are now verbatim BOE text.
- Internal links (FR only, all 200): /fr/audit/, /fr/audit-du-travail-pour-les-entreprises/,
  /fr/droit-du-travail/, 16177 indemnité licenciement, 8402 obligations comptables. Removed: the anchor
  "droit du travail ... ERE et ERTE" pointing to 8655 (that post is a general work guide).

## Fact-check summary (data/factcheck/18814.csv, 24 rows)

- Corrected: article numbers (plans 614+, communication 585, not 583 / 616-732), scope of the 3-month
  protection (necessary assets only, public creditors excluded, +3 months max), class majorities 2/3 and
  3/4 (not 60/75 %), cram-down conditions (art. 639) and challenge grounds (654/655), 5 -> 3 year plan
  re-attributed to natural-person exoneration with the art. 497 grounds, special procedure limited to
  microempresas with thresholds, competent court (COMI), ERE/ERTE inside vs outside concurso.
- Removed: "9 000 faillites en 2024" (INE no longer publishes it), 2026 trend forecast, notarial route,
  AEAT-scrutiny paragraph.
- CTA added where the outcome depends on facts: class formation/homologation, director exposure,
  restructuring vs concurso choice, non-exonerable debts.

## Open points

- **Cannibalisation:** FR 1557 `/fr/blog/restructuration-entreprises-espagne/` ("Restructuration
  d'entreprises en difficulté en Espagne") targets the same intent as 18814 (one letter apart in the URL).
  Merge/301 decision for Mike (not done, not linked).
- **Orphan:** no published post links to 18814. Proposed inbound links (same locale, not done, outside this
  task): from 1691 (section on company structures/difficulties), 10023 (holding), 2297 (contrôle fiscal) or
  17410 (audit de contrats commerciaux).
- Félix/Sonia: no legal interpretation was added; please review the summary of arts 639/654/655 and the
  ERE/ERTE sentence (TRLC 169+) before the switch if desired.
- Rank Math title (57 chars) and description (148 chars) within limits; the description mentions
  "implications fiscales", which the rewrite barely covers: optional rewrite for Mike.
- FR typography: regular spaces before ":" / "?" (13243 precedent).

## QA gate

Scope posts only ✔ · post_modified unchanged before write ✔ · banned items 0 ✔ · TL;DR H2 first ✔ · CTA
before FAQ ✔ · FAQ H3 ✔ · sources inline, no list ✔ · links same-locale 200 ✔ · no `<style>` ✔ · trid
siblings: none ✔ · inbound links: 0 (open) · live verification after switch: pending.
