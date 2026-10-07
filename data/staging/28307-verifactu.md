# 28307 (ES) Verifactu delay and e-invoicing order update, 2026-10-07

Status: **STAGED, NOT WRITTEN.** WPVibe returned Cloudflare 521 for every call to delaguialuzon.com from 2026-10-07 14:36 UTC
(and AISA could not connect on port 443), while the site answers normally from Mike's machine (DNS 31.170.100.185, no Cloudflare
headers). Nothing was changed on the site.

- Facts: `data/staging/verifactu-update-2026-10.md` (verified 2026-10-07). Rows: `data/factcheck/28307.csv`.
- Target: _elementor_data (Elementor), widget(s) with the codebox and body
- Exact old to new replacements (each old snippet found exactly once in the live rendered / staged body): `data/staging/28307-verifactu.json`.
- What changes: TL;DR (+3 bullets: dates in force, announcement, e-invoicing dates), intro 'adaptarse en 2026', calendar section (it said 1 Jan / 1 Jul 2026, which has been wrong since Dec 2025; e-invoicing 'pendiente de desarrollo' replaced), 'estás expuesto a sanción' sentence, 'dentro de un año', PDF FAQ, sanctions FAQ ('señal de alerta... en 2026', unsourced, replaced by LGT art. 201 bis + CTA). Title/H1/slug carry no year: unchanged.
- Notes: Created 2026-10-06 by author id 29, modified again 2026-10-07 11:34:10: re-read before writing. Elena owns ES. Flagged but not edited: Excel statement, 'por programa', 10.000 EUR B2B fine, Facturae 3.2.2, 'Asuntos Económicos', FAQ as <details>, tu/usted mix.
- Wording rule applied: legal dates stay 1 Jan 2027 / 1 Jul 2027 (BOE), October 2028 is "announced, legal text not yet published"
  (Ministerio de Hacienda press note of 5 Oct 2026), e-invoicing order in force 6 Oct 2026 so 12 and 24 months from that date
  (Oct 2027 / Oct 2028, computed). No dashes, no unverified figures, quotes avoided in favour of sourced paraphrase.
- After writing: SQL readback (MD5, `post_modified`), `cache purge`, curl live (new text present, no "2 octobre/на 2 октября" stale
  line, no "n'est pas publié"), WPML edit-mode table before and after, changelog row in `data/changelog/28307.csv`.
