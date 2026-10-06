# 25233 schema fix, 2026-10-06

Live URL: https://delaguialuzon.com/en/blog/writing-spanish-will/ (REST `link`). Mode `builder`, no siblings (trid 2927).

## Body JSON-LD (in `_elementor_data`, one text-editor widget, wrapped in `<p><script type="application/ld+json">`)

Edited with 4 `POST /wpvibe/v1/content/edit` snippet replacements. The old snippets were generated from the live block and checked by MD5 first (stored block 8075 chars, MD5 0168d693f5c6d27161f8f11cd85d1752).

| Item | Before | After |
|---|---|---|
| WebPage, Article, Image, Breadcrumb, Service, FAQ `@id`, `url`, `item`, `mainEntityOfPage` | `/en/blog/spanish-will-uk-nationals/` | `/en/blog/writing-spanish-will/` |
| Name and headline | "How to Write a Spanish Will: A 2026 Guide for UK Nationals" | live H1 "How to write a Spanish will for UK nationals" |
| ImageObject | middle-aged-woman-...-scaled.jpg 2560x1707 (not the featured image) | featured image spanish-will.jpg 795x447 (media 25238) |
| Service `offers` | Offer price 60 EUR, url /en/inheritance-law/ | removed (Service node kept, no price) |
| author, publisher | `@id` reference only | Organization, name "Delaguía y Luzón" |
| Organization, WebSite name | "Delaguía y Luzón Abogados" | "Delaguía y Luzón" |
| dates | none | datePublished 2026-05-15, dateModified 2026-10-06 (WebPage and Article) |
| FAQPage | 6 shorter answers that differed from the page | the 6 visible FAQs, tags stripped, paragraphs joined |

Final block 8381 chars, MD5 0c05c1b06b4fbd41e0498e0ce578c97f (SQL readback equals the expected string). Live: 2 ld+json blocks parse, the graph equals the expected JSON, 0 hits for the old slug, `Offer` and `"price"`.

`dateModified` in the block is static text and will not follow later saves.

## Stored Rank Math schema meta

None on this post (no `rank_math_schema_*` rows).
