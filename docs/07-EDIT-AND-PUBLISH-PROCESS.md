# Edit and publish process (WordPress write path)

Posts only (Scope Gate). One post per change set. Read, stage, approve, write, verify.

## 0. Before writing

- Re-read the post: `get_post` (AISA) or `GET /wp/v2/posts/<id>?context=edit` (WPVibe), and note
  `modified`. If it changed since the audit, re-audit first.
- Check `_elementor_edit_mode`. If `builder`, the body is `_elementor_data`.
- First write of a session: run a harmless test on one post (a no-op `content/edit` round trip, or
  a Rank Math meta write) to confirm the WPML `save_post` fatal (01-SITE-AND-STACK) is gone.

## 1. Stage

Write the proposed change into `data/staging/<id>.md`: for each change, the exact current snippet,
the replacement, and the reason (rule or fact-check row). Mike approves a batch ("go" / "validated").

## 2. Write

| What | How |
|---|---|
| Text inside the body (a sentence, a heading, a link) | `POST /wpvibe/v1/content/edit` with `{"target_type":"meta","post_id":ID,"meta_key":"_elementor_data","old_content":"<exact snippet>","new_content":"<replacement>"}`. The snippet must be unique and JSON-escaped exactly as stored (`\"`, `\/`, `\n`, `é`…). Get it with `/wpvibe/v1/content/search` first |
| Structural body change (add or remove a widget, new FAQ block, reorder) | Read `_elementor_data`, modify locally, `POST /wpvibe/v1/elementor/save-page` with `{"id":ID,"post_type":"post","data":[…]}`. Keep Section/Column structures as they are and generate fresh 8-hex ids |
| Title tag, meta description, focus keyword | AISA `set_seo`, or `POST /rankmath/v1/updateMeta` (`objectType: post`, `objectID`, `meta: {rank_math_title, rank_math_description, rank_math_focus_keyword}`) |
| FAQ / Article schema per post | Rank Math schema meta (`rank_math_schema_*`). Test on one post, because the WPVibe semicolon filter blocked this before |
| Post title (H1), excerpt | `PUT /wp/v2/posts/<id>` with `title` / `excerpt` only |
| Slug | **Only with Mike's approval** + Rank Math redirect 301 old→new + entry in DECISIONS.md |
| Full rewrite of a non-Elementor body | `PUT /wp/v2/posts/<id>` with `content`, then SQL MD5 readback (may return 500 and still commit) |
| Switch an Elementor post to its `post_content` rewrite | Clean `post_content` first, then `content/edit` on meta `_elementor_edit_mode` `"builder"` → `""`. `_elementor_data` stays as rollback. `cache purge`. Never reopen with "Edit with Elementor" |

Never: raw SQL writes to `_elementor_data`, `post_content` edits on Elementor posts (except to
prepare a switch, as above), edits to template 4476, menus, pages, or WPML/Rank Math settings.

**No expiring approval links (Mike, 2026-10-02).** Raw mutating SQL and protected WP-CLI deletes
generate WPVibe approval links that expire within minutes. Prefer `content/edit`, REST and Rank Math
endpoints, with the approval given in chat. When raw SQL is unavoidable (Rank Math redirection rows),
say so first and send the link only when Mike is ready.

## 3. Verify (mandatory)

1. SQL readback: `SELECT meta_value LIKE '%<new snippet>%' FROM dlg_postmeta WHERE post_id=ID AND meta_key='_elementor_data'`.
2. Purge cache: `run_wp_cli "litespeed-purge url <url>"` (or `cache purge`).
3. Live check: `curl` the URL and grep the new text; rerun `python tools/audit_blog.py` on that
   locale; confirm the row improved and nothing else regressed.
4. Log it in `data/changelog.csv`: `date, post_id, lang, change, verified(Y/N), by`.

## 4. Translations

After fixing a fact or bug, open the post's `trid` siblings and apply the equivalent fix, written
natively for each locale. Log each one separately.

## 5. Dates

Bump `dateModified` (via a real save) only when the content materially changed: fact, section,
structure. Never bump it for a typo or for the sake of "freshness".
