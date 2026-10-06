# 892 Beckham Law Spain: US citizens upgrade (U-3), 2026-10-06

Written: `POST /wpvibe/v1/elementor/save-page` (single container 6cef0f89, single text-editor widget 8c8357f, ids kept).
Exact stored widget HTML: `data/staging/892-uk-us.html` (newlines added for reading only; the stored string has none).
Stored editor MD5 `68b5bdc5501cf5eb661b85cf61e58c44` (22 841 chars). `_elementor_data` MD5 `2c96c60a0fa05b679500e640a66ddebe`.
Rollback: previous `_elementor_data` MD5 `01400961e55b9bca4f066b73d6614b90` (post_modified 2026-09-12 11:41:59). Old body not kept in the repo;
revision history in WordPress has it.

## What changed
- TL;DR H2 "Beckham Law: key points", 6 self-contained bullets (the old box and the "Key 2026 insight" boxes removed).
- Facts re-checked against LIRPF art. 93 (consolidated, last change Ley 7/2024) and RIRPF arts 113 to 119. See `data/factcheck/892.csv`.
  Fixed: savings scale (19 to 28 % became 19 to 30 % since 1 Jan 2025), "digital nomads" and "primarily in Spain" (not in the law),
  "foreign income generally not taxed" (employment income during the regime is Spanish-source, art. 93.2.b), "missing the 6-month deadline
  loses eligibility entirely" (not stated by the source), wealth tax "limited exposure" (real obligation, Valencian 2 M EUR does not apply),
  generic AEAT/BOE/MINECO home page links replaced by specific sources.
- Removed: "over 90 treaties", "Did you know", "Final Insight", income-structuring bullets that were generic, "foreign investment income is a
  reason not to use the regime" (backwards).
- New H2 "Beckham Law for US citizens" (scope note in one sentence, H3: how it works for an American, no change to US taxation, treaty and
  regime, Modelo 720/721 and US reporting, working with a US adviser) and 3 FAQ as H3 after the CTA.
- Links added: 8633, 21544, 15116, 20275, plus 22034 (US funds). All EN, all published, all HTTP 200 (curl 2026-10-06).
- Rank Math description (150 chars) replaced: the old one said the regime reduces IRPF "on global income".
  Title tag (50 chars) and excerpt unchanged (still accurate).

## Open points for Felix and Sonia
1. Treaty benefits for a US citizen under the regime. The AEAT manual says regime taxpayers are not treated as residents for DTT purposes.
   The post states only that and sends the reader to the firm. What may we publish on the tie-breaker (art. 4) and credits (art. 24)?
2. Modelo 720 and 721 for the spouse and children who opt in under art. 93.3 (the AEAT FAQ predates the family option and says the regime does
   not extend to the family unit). No AEAT statement found on Modelo 721 for regime taxpayers.
3. Do years under the regime count for the exit tax (art. 95 bis LIRPF, 10 of 15 periods)?
4. Self-employed teleworkers (not employees) are not listed in art. 93.1.b. The post says so and invites contact.
5. Wealth tax for a regime taxpayer living in Valencia: 700 000 EUR (state, real obligation) per LIP art. 28 Tres, not the Valencian 2 000 000 EUR.
   Confirm wording.

## Siblings (trid 814)
FR 888 and RU 1772, both `_elementor_edit_mode = builder` before and after (checked by SQL after the last save). Not edited.
Facts they probably share: look-back 5 periods, six tax periods, 24 % up to 600 000 EUR and 47 % above, savings scale top 30 %,
wealth tax by real obligation, no Modelo 720. FR 888 meta description still says "loi Beckham de 2004".

## Schema
The post has no in-body JSON-LD. The 3 FAQ are not mirrored in FAQPage schema (Rank Math schema left alone). Rank Math Service schema
(schema-515934) carries an Offer with price 60 EUR: for Mike.
