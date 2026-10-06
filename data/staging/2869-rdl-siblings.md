# EN 2869 renting-property-in-spain: RDL 26/27 sibling check (2026-10-06)

Final `_elementor_data` MD5 31d9e5c457f3f6c0523da5a1c8236b8c (before edac9392f0fad01c966bc192ed4b5c58), post_modified 2026-04-29 20:46:23 -> 2026-10-06 13:09:32.
WPML trid 1072 (FR 2823): before builder / empty, after builder / empty. The AISA update_post save copied the empty mode onto EN 2869; restored with `wp post meta update 2869 _elementor_edit_mode builder --force`, cache purged, live checked (Elementor text present: "Rent updates: article 18"). FR 2823 untouched (content MD5 9f95e769fc85eafde20669a14a132894, post_modified 2026-10-06 11:15:47).

## Found (mirrors FR 2823 pre-correction)
- "Annual increases capped at 2.14 % (IRAV)" plus a 2024/2025/2026 cap table: unsupported (art. 18.1 still CPI, DA 11 INE index; 2 % cap repealed).
- Deposit "maximum 2 months (1 unfurnished, 2 furnished)": wrong (art. 36.1 and 36.5).
- "60 % net income reduction": wrong (90/70/60/50 %, art. 23.2 LIRPF).
- "Quarterly filings for non-residents": outdated (AEAT note on Orden HAC/623/2026).
- "New annual reporting requirements from February 2026" with an unverified data list: Orden VAU/1560/2025 rests on art. 10.4 RD 1312/2024, annulled on 19 May 2026.
- Stressed-zone paragraph named Barcelona, Madrid, Malaga and parts of Valencia (not verifiable; EN 1815 and 4734 say Valencia has none) and a wrong large-landlord definition and price-cap wording.

## Changed
TL;DR bullets 4 and 7, IRAV section (now "Rent updates: article 18 and the IRAV index" with CTA), table removed, checklist items, deposit paragraph, IRPF and Modelo 210 bullets, short-term return section (status plus CTA), stressed-zone sentences, price-cap bullet.

## Open points
- Felix/Sonia: IRAV vs CPI limit (same open point as FR 2823); acts done on 1 and 2 Oct 2026.
- Not edited: "Mandatory registration: all rental properties must be registered with local authorities" (unverified), 632,000 expiring contracts, Idealista figures and yields, deposit "within 30 days", SEO title typo "Porperty" and "Dicover" in the description, "Navigating the complexities" (banned phrase) at the start of the tips section, no TL;DR H2 in the required form. Maral may fix those; legal items go to Mike/Felix/Sonia.

## Common context (2026-10-06)
Congress did not validate Real Decreto-ley 26/2026 (BOE 30 Sep) nor 27/2026 (BOE 1 Oct) and repealed both on 2 Oct 2026 (BOE-A-2026-20526 and BOE-A-2026-20527). RDL 8/2026 was repealed in April 2026. The consolidated LAU, LIRPF, LIVA and TRLRHL (updated 2 Oct 2026) show the pre-decree wording. Spanish press (Infobae, 5 Oct 2026) says the Government plans to approve the housing decrees again (Council of Ministers of 7 Oct); nothing is law unless validated, so re-check the BOE on 7 and 8 Oct (see TASKS.md re-check item).
Write path: POST /wpvibe/v1/content/edit on meta `_elementor_data` (snippet replace, no raw SQL, no approval links). post_modified bumped with AISA update_post (no field change), which copied the empty edit mode onto EN 2869 (restored). Facts: data/factcheck/<id>.csv (rows dated 2026-10-06). Log: data/changelog/<id>.csv. Exact stored body: not exported (Elementor JSON, 11 to 54 kB); the readback MD5 is given below and rollback is the Elementor revision of the previous save.
