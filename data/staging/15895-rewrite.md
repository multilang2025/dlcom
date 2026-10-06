# FR 15895 tva-sur-les-locations-touristiques-en-espagne: full rewrite (2026-10-06)

Mike asked for it on 2026-10-06 ("same standard as FR 10629"). Written natively in French from BOE, AEAT and EUR-Lex pages opened
the same day. Method: `_elementor_edit_mode` stays `builder` (no switch); the body was written into the Elementor widgets with
`POST /wpvibe/v1/elementor/save-page` (`{"id":15895,"post_type":"post","data":[...]}`). Facts: `data/factcheck/15895.csv`. Log:
`data/changelog/15895.csv`. Exact stored widget HTML: `data/staging/15895-rewrite.html` (the full data array that was posted:
`data/staging/15895-rewrite.json`).

## State
- `_elementor_data` MD5 `89a6161ea0d33cc3bb4dfd6a60670de5` (32 370 chars, post_modified 2026-10-06 13:10:35) -> **`078509977e14d65d85944a033c9c8d95`**
  (34 929 chars, JSON_VALID 1), post_modified **2026-10-06 15:53:05** (after the excerpt PUT; the save-page call was 15:51:59).
- Widget 67c57be (container babf283, main body) MD5 `8e2ba96f013574dadfcfdfddb7412ce7`; widget f15a95c3 (container d2d48c9, FAQ) MD5
  `ab93ba0eef873fed46bdee53aac4e78f`. Both equal the local files byte for byte.
- Rollback: the previous `_elementor_data` is in the Elementor revisions (MD5 89a6161e...). Not kept in the repo.
- Live: 200, one H1, TL;DR H2 first, 12 H2 and 13 H3, no `<br>`, no empty `<p>`, old claims 0 hits (the only "&" / dash hits are the
  site-wide LegalService JSON-LD, CSS and the language switcher).
- WPML trid 1891 (ES 15812, EN 15852, FR 15895, RU 15904): `_elementor_edit_mode` = builder before, after the save-page and after the
  excerpt PUT. Sibling post_modified unchanged (15812 2026-08-25 15:34:35, 15852 2026-10-06 13:09:14, 15904 2026-10-06 11:01:24). Not edited.

## What changed
- TL;DR H2 "TVA sur les locations touristiques : les points essentiels" with 7 bullets, then H3 hook, intro, 9 noun-form H2 sections,
  a recap table, 3 verbatim quotes (LIVA art. 20.Uno.23 e'), TRLIRNR art. 25.1.a, Directive 2025/516 art. 28 bis), CTA box (grey #f5f5f5,
  Félix Delaguía) before the FAQ, 10 FAQ as H3. About 3 300 words. Sources inline (`target="_blank" rel="nofollow noopener"`), no list.
- Corrected: "TVA 21 %" for ancillary services (now: general rate 21 % per art. 90, classification of extras sent to a CTA); FAQ "taux normal 21 %";
  IRNR "19 % UE/EEE/Suisse" (24 % without deductions for non-EU/EEA such as Swiss; 19 % with deductions for EU/EEA); quarterly Modelo 210
  (annual grouped return, 1 to 20 April 2027 for 2026 rents, per the AEAT note on Orden HAC/623/2026); prorata example by nights (the prorata is
  annual turnover, art. 104.Dos); Verifactu "from 2026" (1 Jan 2027 IS taxpayers, 1 Jul 2027 others, with a further extension announced on
  5 Oct 2026); "conservation 4 ans" removed (unsourced).
- Removed: emojis, "plus de 65 ans", "Delaguía &" (4 places), 3 unsourced stat boxes (340 000, +27 %, 4 200 sanctions), the old CTA with the
  second email, the "Delaguía & Luzón : votre partenaire" section, the "Optimiser la fiscalité" accordion answer (promotional).
- Kept from earlier today: IAE group 685 and Modelo 036 (037 abolished 3 Feb 2025), Modelo 238, STS of 19 May 2026, Ley 15/2018 art. 19.1.b and
  92.16, ViDA (now with the verbatim definition and the "unless the supplier gave its VAT number" exception), RDL 26/2026 repealed on 2 Oct 2026.
- FAQ: the nested accordion 474e0c8 (5 items, `<details>`) and the 5 H3 of the old body (10 in all) are now 10 H3 in one text-editor widget
  f15a95c3 placed in the existing container d2d48c9 (house rule: FAQ as H3, as done on RU 13927). No FAQPage schema exists on the post
  (rank_math_rich_snippet off, no `rank_math_schema_FAQPage`), so there is nothing to mirror.
- Rank Math description rewritten (142 characters, via AISA `set_seo`); title kept ("TVA sur les locations touristiques : guide propriétaires",
  56 characters, no old claim); excerpt rewritten (245 characters, `PUT /wp/v2/posts/15895` excerpt only). Slug and URL unchanged. H1 (post title,
  "...tout ce que vous devez savoir si vous êtes propriétaire") unchanged: Mike to decide whether to shorten it.
- Internal links (all FR, published, HTTP 200, no redirect, checked with curl): 10629, 2823, 12930, 2678, 4371 (assujetti-irpf-espagne, the
  `qui-est-assujetti-...` slug 301s), 25839, 15720, 1130 (location-airbnb-a-valence), controle-fiscal, sci, holding, droit-fiscal, droit-immobilier,
  cabinet, contact. Inbound links already exist from 1130, 3243, 4345, 10629, 15720 and 24989, so none were added.

## Open points for Félix and Sonia
1. Classification of separately billed extras (parking, spa, bikes, airport transfers) under the 10 % or 21 % rate: neither the LIVA text nor the AEAT
   page rules on it, so the post sends it to a CTA.
2. Non-resident landlord whose rental is subject to VAT: registration and any representative in Spain. Not stated; CTA.
3. IAE for non-resident individuals: TRLRHL art. 82.1.c says "las personas físicas" but has a specific paragraph for IRNR taxpayers. CTA.
4. How the VAT deemed-supplier rule of Directive 2025/516 will apply to an exempt Spanish rental, and the Spanish application date
   (1 Jul 2028 to 1 Jan 2030). The post states only what the directive says.
5. Personal use of the flat and the deduction limits of LIVA arts. 95 and 96 (CTA).

## For Mike (not touched)
- Rank Math schema of 15895 (Article, Organization, Service) is stale: brand "Delaguía &amp; Luzón", Article headline "TVA sur les locations ..." (71 chars). It is
  not printed (rich snippet off). A schema write needs the Rank Math route with the semicolon risk.
- The `post_content` mirror was not refreshed (not rendered; refreshing it needs another write and the page is in `builder` mode). Nobody should open
  15895 in "Edit with Elementor" with the old accordion in mind: the accordion no longer exists.
- Siblings (not edited, facts they probably share): ES 15812 (Elena), EN 15852 (Mike/Maral), RU 15904: the "TVA 21 %" extras claim, IRNR 19 % with Swiss
  residents, Modelo 210 quarterly, Verifactu "2026", the prorata example, and the registry paragraphs (RD 1312/2024 annulled).
- Re-check on 7 and 8 Oct 2026 for new housing decree-laws (already in TASKS.md): if a decree again changes LIVA art. 20 or 91, this post needs a new pass.
- EUR-Lex blocks curl: the Directive 2025/516 and Regulation 2024/1028 texts were read in the Browser pane (FR HTML). AISA `fact_check` was not used.

## Writes (posts only, no raw SQL, no approval links)
`POST /wpvibe/v1/elementor/save-page` (HTTP 200, no warnings), AISA `set_seo` (description), `PUT /wp/v2/posts/15895` (excerpt only), `wp cache purge` +
AISA `flush_caches`. WPVibe calls used in this task: 3 (save-page, PUT excerpt, cache purge). All reads went through AISA `db_query` and the BOE/AEAT/EUR-Lex pages.
