# 15895 (FR) Verifactu delay and e-invoicing order update, 2026-10-07

Status: **APPLIED 2026-10-08** (content/edit, see `data/changelog/15895.csv`). Facts re-checked on 2026-10-08: no new BOE instrument on 7 or 8 Oct.

- Facts: `data/staging/verifactu-update-2026-10.md` (verified 2026-10-07). Rows: `data/factcheck/15895.csv`.
- Target: _elementor_data (Elementor), one paragraph
- Exact old to new replacements (each old snippet found exactly once in the live rendered / staged body): `data/staging/15895-verifactu.json`.
- What changes: The Verifactu paragraph: the vague 'prévision de nouvelle prolongation' becomes the dated announcement (5 Oct 2026, report to October 2028, not published at 7 Oct 2026) with the Hacienda note linked and a CTA.
- Notes: WPML trid 1891 (15812, 15852, 15895, 15904) must stay builder before and after.
- Wording rule applied: legal dates stay 1 Jan 2027 / 1 Jul 2027 (BOE), October 2028 is "announced, legal text not yet published"
  (Ministerio de Hacienda press note of 5 Oct 2026), e-invoicing order in force 6 Oct 2026 so 12 and 24 months from that date
  (Oct 2027 / Oct 2028, computed). No dashes, no unverified figures, quotes avoided in favour of sourced paraphrase.
- After writing: SQL readback (MD5, `post_modified`), `cache purge`, curl live (new text present, no "2 octobre/на 2 октября" stale
  line, no "n'est pas publié"), WPML edit-mode table before and after, changelog row in `data/changelog/15895.csv`.
