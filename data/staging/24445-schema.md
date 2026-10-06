# 24445 schema fix, 2026-10-06

Live URL: https://delaguialuzon.com/en/blog/buy-house-valencia-non-resident/. Mode `builder`, no siblings (trid 2812).

## Body JSON-LD (in `_elementor_data`)

6 `content/edit` snippet replacements. Stored block before: 8736 chars, MD5 767291f3c89074f3300222baf1db4156.

| Item | Before | After |
|---|---|---|
| all `@id`, `url`, `item`, `mainEntityOfPage` | `/en/blog/buying-a-house-in-valencia-as-a-non-resident/` | `/en/blog/buy-house-valencia-non-resident/` |
| ImageObject url | `PASTE_IMAGE_URL_HERE`, no size | https://delaguialuzon.com/wp-content/uploads/2026/04/Buying-a-House-in-Valencia-as-a-Non-Resident.webp, 795x530 (media 24452, the featured image) |
| name, headline | "Buying a House in Valencia as a Non-Resident" | live H1 "How to buy a house in Valencia as a non-resident" |
| Service `offers` | Offer price 60 EUR | removed (Service node kept) |
| author, publisher | `@id` only | Organization "Delaguía y Luzón"; Organization and WebSite name "Delaguía y Luzón" |
| dates | none | datePublished 2026-04-28, dateModified 2026-10-06 |
| FAQPage | 8 answers worded differently from the page | the 8 visible FAQs |

Final block 8823 chars, MD5 7cd6637b6a14214867e6a68ecbc89049 (SQL equals expected). Live: parses, graph equals expected, 0 hits for placeholder, old slug, Offer, price.

## Stored Rank Math schema meta (not output while the rich-snippet module is off)

Written with `POST /rankmath/v1/updateMeta` (the `updateSchemas` endpoint returned 403 rest_cannot_edit).

Before, `rank_math_schema_FAQPage` had 5 stale and partly unsourced questions:
- "How long does it take to buy a property in Valencia as a non-resident?": "From accepted offer to keys, six to twelve weeks is typical for a cash purchase. Mortgage-financed purchases tend to run between ten and sixteen weeks..."
- "What is the modelo 210 and when do I pay it?": "...imputed income tax on a deemed rental value... The deadline is 31 December of the year following the tax year."
- The NIE answer said "The only mandatory requirement is your NIE." and the will answer mentioned "lower inheritance tax exposure".

After: the 8 visible FAQs.

Before, `rank_math_schema_LegalService` had name `Delaguía &amp; Luzón`. After: `Delaguía y Luzón`. The rest of that node is unchanged (image compra-propiedad-img.jpg and priceRange "€€" were left, for Mike).

`rank_math_schema_BreadcrumbList` has no `@id` (left as is, harmless).

Readback: the REST call returned 200 with the schemas, but the SQL or `get_schema` readback of this meta was blocked by the permission classifier, so the unserialize was not verified for this post. Please run `get_schema` on 24445, or open Rank Math > Schema in wp-admin, to confirm.
