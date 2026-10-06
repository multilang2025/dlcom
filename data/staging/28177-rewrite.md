# 28177 (EN, DRAFT) non-resident-income-tax-spain: N-1 plus U-8, 2026-10-06

- Title (H1): **Non-resident income tax in Spain: Modelo 210 for owners** (55 chars). Slug `non-resident-income-tax-spain`.
- Not published. Preview: `https://delaguialuzon.com/en/?p=28177` (logged-in only). Intended URL: `/en/blog/non-resident-income-tax-spain/`.
- Created with `POST /wp/v2/posts?lang=en` (status draft, author 5 like the other recent EN posts, categories Tax Law 47 and Housing and Urban Planning 53 like 27052). HTTP 200, no WPML fatal.
- Stored body: `data/staging/28177-rewrite.html`. SQL `MD5(post_content)` = `07398b5877a49b7b56f4c3ed3e4735c9` = local file (29 861 bytes). No Elementor meta. 2 818 words by script, WPML word count 2 578. 6 FAQ (H3), CTA before the FAQ, TL;DR H2 first with 6 bullets.
- WPML: `language_code = en`, `element_type = post_post`, trid 3491, no other element in the trid (no accidental ES/FR/RU link).
- Rank Math (via `updateMeta`): title "Non-resident income tax in Spain: Modelo 210 for owners" (55), description 152 chars, focus keyword "non-resident income tax in Spain", excerpt 219 chars.
- No featured image (Mike decides, realistic images only).

## What the draft covers
Who is a non-resident (art. 5 and 6 IRNR, art. 9 LIRPF); rent (24 % gross for UK/US, 19 % with expenses for EU/EEA, art. 25.1.a, 24.1, 24.6, AEAT Brexit note); imputed income (art. 85 LIRPF, 2 % or 1.1 %, 2026 percentage as CTA); sale (19 % for every non-resident, 3 % buyer withholding with art. 25.2 quote, Modelo 211, plusvalía arts. 104, 106, 110 TRLRHL); Modelo 210 deadline table after Orden HAC/623/2026; who files and the art. 10 representative; penalties (art. 27, 191, 26 LGT, art. 10.4 IRNR); treaty outline (UK art. 6(1) quote, art. 13(1), art. 22(2)(a) quote; US art. 6, 13, 24(2), 1(3)); Modelo 720 (residents only), IBI, wealth tax (EUR 700 000 state minimum, Valencian EUR 2 000 000 for residents of the Comunitat only); worked example (UK owner, round numbers, illustration). Scope sentence (Spanish law and Valencian angle, home-country adviser) is a single sentence in the second intro paragraph, easy to remove if D-11 is rejected.

Quotes (all verified by string match against the source text): art. 25.2 IRNR (Spanish extract), UK-Spain convention art. 6(1) and 22(2)(a) (HMRC English synthesised text), "residan habitualmente en la Comunitat Valenciana" (Ley 5/2026 art. 19).

## Facts verified, CTA'd, left out
- 30 rows in `data/factcheck/28177.csv`. Everything in the post was opened on the official page on 2026-10-06 (BOE open data API for consolidated texts, AEAT pages, HMRC gov.uk).
- **CTA, not stated as fact:** the imputed-income percentage for 2026 (see open point 1), whether a non-resident may combine regional wealth tax rules with the EUR 700 000 minimum, whether the AEAT will require a representative in a given case, whether a permanent establishment arises, the art. 191 LGT percentage for a given case, how treaty credit works on the UK or US return.
- **Left out:** Modelo 720 penalties, UK ISA/pension points, US Social Security, any US or UK filing detail (forms, credit mechanics).

## Open points for Felix and Sonia (via Mike)
1. **Imputed income 2026 (1.1 % or 2 %).** The AEAT page says the 1.1 % rule (revised values in force from 1 Jan 2012) applies to 2023, 2024 and 2025. The BOE consolidated text of DA 55 LIRPF now reads "durante el periodo impositivo 2023" and marks the later extensions as "sin efecto" (they came through decree-laws that Congress derogated). RDL 26/2026 (29 Sep 2026) would have extended it to 2026 and changed art. 85 from 1 Jan 2027; Congress derogated it on 2 Oct 2026 (BOE 245). Which percentage applies for 2024 to 2026 needs the partners' reading. The post states only what each source says and ends in a CTA.
2. Art. 10.1 IRNR: does the firm advise UK/US owners to appoint a representative as a rule, or only on AEAT request? The post says "when the tax office requires it" (the text of the law).
3. Wealth tax for non-residents with Valencian property: the AEAT 2025 manual reads EUR 700 000 only. The post says what the sources say and gives a CTA.
4. D-11 scope note: one sentence in the second intro paragraph and the "home-country adviser" lines near the treaty section.

## Add on publication
- Links to add to this post: none (no draft linked).
- Inbound links to add from published EN posts (2 or 3): 27052 (selling as a non-resident), 24445 (buying in Valencia), 18877 (regional property taxes), 20275 (UK Spain double taxation). Not done here (other agents own several of these posts).
- After publishing: check Permalink Manager created `blog/non-resident-income-tax-spain` (drafts have no URI entry yet, like every other draft), `curl -I` the URL, run `python tools/related_posts_audit.py en`, and add FAQPage schema (not added, 6 Q/A).
- Re-check list (not written to TASKS.md, which another session edits): (a) 2027-01-01: Modelo 210 new annex and boxes apply to returns filed from 1 Jan 2027, first April filings 1 to 20 April 2027 (Orden HAC/623/2026); (b) imputed-income percentage 2026 and any new decree-law replacing RDL 26/2026 (check monthly); (c) AEAT deadline page before publication, since the table says "as at 6 October 2026".

## Problems found on live EN posts (not edited here)
- **27052** (selling as a non-resident) says "Non-EU and non-EEA sellers pay 24% on the gain" and shows "19% EU/EEA, 24% others" in its table. Wrong: gains are 19 % for every non-resident (art. 25.1.f.3). N-1 links to 27052, so fix it before publishing N-1. Its other statements (3 % on Modelo 211, Modelo 210 four months after the sale) agree with the AEAT.
- **2175** (fraud by false non-residents): its body still calls IRNR "flat" rates and cites the 19 % EU/EEA rate; consistent with the law, nothing changed.
- 5083, 20275, 18877 and 24445 state the IRNR rates in the same way as the law (19 % EU/EEA, 24 % others, 19 % gains), no conflict found. The savings-rate scale quoted in 5083 (28 % top) and 20275 (26 % top) was not checked here.
- **Drafts 28169, 28170, 28171** ("PLAN: ..." placeholders created today by user 29, language ES in WPML, no slug): 28171 is the placeholder for this same topic and duplicates N-1. Left untouched. Suggest Mike trashes 28171 (and sets 28169 and 28170 to EN or trashes them) so they do not turn up as ES drafts.

## U-8 (post 2175)
Rank Math focus keyword "non-resident income tax in spain" changed to "false non-residents Spain". Title and description rewritten to match (same claims): see `data/changelog/2175.csv` for old and new values and the rollback. Body, `_elementor_data`, `_elementor_edit_mode` and the ES sibling (2162) untouched; `post_modified` unchanged; live title and description verified.
