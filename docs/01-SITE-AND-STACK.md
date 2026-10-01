# Site and stack: what an agent needs to know before editing a post

## How a blog post is built

- Each post is an Elementor document (`_elementor_edit_mode = builder`, template type `wp-post`).
  Its body lives in post meta **`_elementor_data`** (JSON), not in `post_content`. `post_content`
  is a stale mirror. Editing it does not change the page.
- Some posts also contain Gutenberg block comments in `post_content` (ES 11, EN 11, FR 22, RU 3 on
  2026-10-01). Elementor still renders them, so edit `_elementor_data` anyway.
- The page chrome comes from the Elementor Pro **single-post template 4476**: title widget,
  post-info widget, featured image, a table-of-contents widget, post-navigation and share buttons.
  The template is out of scope for agents (Scope Gate). Anything that has to change site-wide on
  every post (author box, dates, TOC duplication) is a template task for Mike.
- Inside the post body, content usually sits in `text-editor` widgets holding raw HTML (summary box
  with `background-color:#f5f5f5`, H2/H3, lists, tables, FAQ).

## SEO layer

- Rank Math Pro handles titles, descriptions, focus keyword (`rank_math_focus_keyword`),
  `rank_math_title`, `rank_math_description` and schema (`rank_math_schema_*` meta).
- Known 2026-05 issue: a Rank Math Pro 3.0.112 fatal was worked around by **disabling the
  rich-snippet module**. That probably explains why FR/RU posts output only `LegalService`
  JSON-LD with no `BlogPosting`. Check before acting (`TASKS.md` T-02).
- The `/rankmath/v1/updateMeta` endpoint wrote meta cleanly even while REST `save_post` was
  failing (see below).

## Multilingual layer (WPML)

- Translations are linked through `dlg_icl_translations` (`element_type = 'post_post'`, `trid`
  groups a post with its translations, `language_code` es/en/fr/ru).
- On 2026-10-01 the blog posts emit **no `hreflang` alternates at all** (checked in the live HTML).
  This is a site-level WPML / WP SEO Multilingual setting, so it goes to Mike.
- Post 24445 was English content tagged as ES (2026-04). Check whether it was reassigned.
- Slugs ending in `-2` (`regroupement-familial-espagne-2`, `alquiler-de-infravivienda-…-2`) point
  to a duplicate or a re-created post. Each one is a merge/redirect candidate. Never rename one
  without approval.

## Known traps (from the April to May 2026 programme)

| Trap | What to do |
|---|---|
| WPML fatal `array_filter() on bool` in `class-wpml-element-translation-package.php:484` blocked REST `save_post` and `_elementor_data` writes (May 2026) | Test on one post first. If it fails, use `/rankmath/v1/updateMeta` for meta and report the body edit as blocked |
| WPVibe semicolon filter blocked some schema writes | Schema via Rank Math meta or an MU plugin (Mike) |
| Writing `_elementor_data` with raw SQL or `post meta update` | Never. It leaves `_elementor_element_cache` stale. Use `/wpvibe/v1/content/edit` (snippet replace) or `/wpvibe/v1/elementor/save-page` |
| LiteSpeed serves cached HTML after a correct write | Purge the URL (`wp litespeed-purge url <url>` or `cache purge`) before verifying live |
| Double table of contents (template TOC widget + in-body Rank Math TOC block) | Remove the in-body block per post, or switch the template's TOC off (Mike) |
| Posts touched by someone else the same day | Re-read `post_modified` right before writing |

## Plugins that matter for blog work

Link Whisper Premium (internal link suggestions and reports), Broken Link Checker (broken links
list in wp-admin), WP External Links (may force `target`/`rel` on external links, so check its
settings before fixing links one by one), Imagify (WebP generation, which may serve WebP through
`<picture>` or rewrite rules even when the `<img src>` is a JPG), Simple History (who changed what).
