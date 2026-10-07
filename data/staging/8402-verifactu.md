# 8402 (FR) Verifactu delay and e-invoicing order update, 2026-10-07

Status: **STAGED, NOT WRITTEN.** WPVibe returned Cloudflare 521 for every call to delaguialuzon.com from 2026-10-07 14:36 UTC
(and AISA could not connect on port 443), while the site answers normally from Mike's machine (DNS 31.170.100.185, no Cloudflare
headers). Nothing was changed on the site.

- Facts: `data/staging/verifactu-update-2026-10.md` (verified 2026-10-07). Rows: `data/factcheck/8402.csv`.
- Target: post_content (edit mode EMPTY, renders from post_content)
- Exact old to new replacements (each old snippet found exactly once in the live rendered / staged body): `data/staging/8402-verifactu.json`.
- What changes: TL;DR (6 bullets to 7: legal dates / announcement / e-invoicing), H3 hook, callout 'Repères au 7 octobre 2026' (+ Hacienda note and AEAT links, CTA), e-invoicing section (order now published, 6 Oct 2026, Oct 2027 / Oct 2028), autónomo sentence, FAQ 1 and 2, excerpt (had 'obligatoire au 1er janvier 2027' and the wrong decree date 24 March 2026; RD 238/2026 is dated 25 March). Title (H1) and title tag carry no year of obligation: unchanged.
- Notes: WPML: after the save set _elementor_edit_mode of 8402 back to EMPTY (content/edit builder to empty) if flipped, and restore ES 7717, EN 8398, RU 8407 to builder (`post meta update <id> _elementor_edit_mode builder --force`).
- Wording rule applied: legal dates stay 1 Jan 2027 / 1 Jul 2027 (BOE), October 2028 is "announced, legal text not yet published"
  (Ministerio de Hacienda press note of 5 Oct 2026), e-invoicing order in force 6 Oct 2026 so 12 and 24 months from that date
  (Oct 2027 / Oct 2028, computed). No dashes, no unverified figures, quotes avoided in favour of sourced paraphrase.
- After writing: SQL readback (MD5, `post_modified`), `cache purge`, curl live (new text present, no "2 octobre/на 2 октября" stale
  line, no "n'est pas publié"), WPML edit-mode table before and after, changelog row in `data/changelog/8402.csv`.
