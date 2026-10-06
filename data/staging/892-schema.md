# 892 schema fix, 2026-10-06

Live URL: https://delaguialuzon.com/en/blog/beckham-law-spanish-tax-regime/. Mode `builder`. WPML trid 814: FR 888 and RU 1772.

## Body JSON-LD

None. `_elementor_data` (23557 chars, MD5 2c96c60a0fa05b679500e640a66ddebe) and `post_content` contain no `ld+json` or `schema.org`. The live page shows only the site-wide LegalService block. Not edited.

## Stored Rank Math schema meta (not output while the rich-snippet module is off)

`POST /rankmath/v1/updateMeta`, key `rank_math_schema_Service` replaced.

Before: Service with `offers` = Offer (url /en/contact/, price 60, EUR, InStock) plus `priceSpecification` (price 60, minPrice 60).
After: the same node without `offers`. `@id`, name, serviceType, description, provider, areaServed, availableLanguage, url and image are unchanged.

ImageObject (Beckam_law.jpg) already equals the featured image 963, so it was left. BreadcrumbList is unchanged. This post's meta has no FAQPage or author node.

Readback: the endpoint returned 200 with the schemas. The SQL or `get_schema` readback was blocked by the permission classifier, so it is not verified here. `_elementor_data` is untouched, so the post body and the siblings (FR 888 modified 2026-09-12, RU 1772 modified 2026-10-02, both `builder`) are unchanged.
