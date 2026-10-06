# 20394 schema fix, 2026-10-06

Live URL: https://delaguialuzon.com/en/blog/spanish-non-lucrative-visa/. Mode `builder`, no siblings (trid 2329).

## Body JSON-LD

None (`_elementor_data` MD5 13189b58ed9245f5624aae219227f14a, `post_content`: no `ld+json`). Not edited.

## Stored Rank Math schema meta (not output while the rich-snippet module is off)

`POST /rankmath/v1/updateMeta` on two keys, then verified with `get_schema` and a SQL readback of the serialisation.

- `rank_math_schema_Service`: `offers` (Offer, price 60, EUR, url /en/contact/) removed. The rest is unchanged (provider was already "Delaguía y Luzón").
- `rank_math_schema_ImageObject`: url `https://delaguialuzon.com/wp-content/uploads/2025/12/spanish-non-lucrative-visa.jpg` (HTTP 404) -> `https://delaguialuzon.com/wp-content/uploads/2025/12/spanish-non-lucrative-visa-application.png` (the featured image, media 20390).
- `rank_math_schema_BreadcrumbList`: unchanged.

Open point: the Service `@id` points to `/en/immigration-law/#service-non-lucrative`, not to this post. Harmless, left.
