# CLAUDE.md: Delaguía y Luzón legacy WordPress blog

## What this repo is

The working repo for the **blog section of the live WordPress site, delaguialuzon.com**, in all
four WPML locales (ES root, `/en/`, `/fr/`, `/ru/`). The scope covers style, bugs, NLP/entity
SEO, E-E-A-T and fact checking. The site itself lives in WordPress, so this repo holds the rules,
processes, audit tooling, audit outputs and task list, not the site code.

The process docs are adapted from `multilang2025/dlvibe` (the headless rebuild, which has its own
blog copy). Rules there that only make sense for the rebuild (Next.js components, Design 3
tokens, `/domaines/` silos, Payload CMS) were dropped. Rules about content, facts and brand were
kept. Where this repo and dlvibe disagree on WordPress content, this repo wins.

Read in this order before touching a post:

1. `TASKS.md`: what is open, in what order
2. `docs/01-SITE-AND-STACK.md`: how the WordPress install is built, and its known traps
3. `docs/02-STYLE-GUIDE-MASTER.md` + `docs/style-guides/STYLE-GUIDE-<LANG>.md`
4. `docs/03-FACT-CHECKING-PROTOCOL.md` and `docs/04-EEAT-STANDARD.md`
5. `docs/06-AUDIT-PROCESS.md` → `docs/07-EDIT-AND-PUBLISH-PROCESS.md` → `docs/09-REVIEW-QA-GATE.md`

Project agents in `.claude/agents/`: `dl-blog-auditor` (read-only audits), `dl-fact-checker`
(stages verified corrections), `dl-blog-editor` (writes to WordPress), `dl-qa-publisher` (final
live check). The blog rules Mike set on 2026-10-01 are in `docs/02-STYLE-GUIDE-MASTER.md`:
TL;DR first, sources as inline anchor links, unsure claims become a CTA, airy paragraphs,
same-language links and related posts, short URLs with 301s, no pasted HTML/CSS, realistic
featured images, no cannibalisation. The rebuild repo `multilang2025/dlvibe` mirrors these in
its own docs (PR #95).

**Team split (2026-10-01):** Mike FR and EN, Elena ES, Maral EN with Mike. RU on hold.

## Site facts

- WordPress 7.1, PHP 8.1, theme Hello Elementor Child, Elementor + Elementor Pro, WPML (+ String
  Translation, WP SEO Multilingual), Rank Math + Rank Math Pro, LiteSpeed Cache, Link Whisper
  Premium, Broken Link Checker, WP External Links, Imagify, Formidable Forms.
- DB prefix `dlg_`. Posts are built in Elementor (`_elementor_data`), rendered through the
  single-post theme template **4476**.
- Blog URLs: ES `/blog/<slug>/`, EN `/en/blog/<slug>/`, FR `/fr/blog/<slug>/`, RU `/ru/blog/<slug>/`
  (Cyrillic slugs).
- Published posts on 2026-10-01: **ES 84, EN 150, FR 104, RU 28 (366)**, plus drafts: ES 13,
  FR 9, RU 4. Inventory: `data/inventory.csv` (regenerate per `docs/06-AUDIT-PROCESS.md`).

## Connectors

- **WPVibe** (`mcp__441b67b9…`), site `https://delaguialuzon.com`, administrator. Writes go
  through `rest_api`, `/wpvibe/v1/content/edit` and `/wpvibe/v1/elementor/save-page`.
- **AISA** (`mcp__ae69f0d0…`), `site: delaguialuzon.com`, `chat_id` set per conversation:
  `db_query` (read-only SQL), `get_post`, `search_posts`, `fact_check` (Perplexity, web-grounded),
  `get_seo` / `set_seo`.
- Never type a WordPress password anywhere. Both connectors are already authorised.

## Hard rules

- **Scope Gate: posts only.** Programmatic writes are limited to `post_type=post`. Pages,
  theme-builder templates (including single-post template 4476), menus, WPML settings, Rank Math
  global settings and plugin settings are **not** changed by an agent. A fix that needs one of
  them becomes a task for Mike (`TASKS.md`, section "Needs Mike / wp-admin").
- **No silent URL changes.** A slug change needs Mike's explicit approval plus a 301 (Rank Math
  Redirections) recorded in `docs/DECISIONS.md`.
- **No invented legal or tax claims.** Every figure, rate, threshold, form number or deadline goes
  through `docs/03-FACT-CHECKING-PROTOCOL.md`. If it can't be verified, escalate it. Never soften it
  into something vague.
- **Never translate one locale's copy into another.** Each locale is written for its own reader
  (see the style guides). Fix a fact in every locale that carries it, but write each fix natively.
- **Stage, then publish.** Mike approves publishing per batch. "go" / "validated" means proceed.
- **Verify every write** by reading it back: SQL on `dlg_postmeta` / `dlg_posts`, then a live
  `curl` of the URL after a LiteSpeed purge. Never trust a write tool's JSON response alone. An old
  connector bug returned data from other sites.
- **No expiring approval links.** Write through `content/edit`, REST or Rank Math endpoints rather than
  raw SQL or protected WP-CLI deletes, whose WPVibe approval links expire within minutes (Mike,
  2026-10-02). See `docs/07-EDIT-AND-PUBLISH-PROCESS.md`.
- **Someone else may be editing.** Posts are being modified daily (2026-09-24 → 2026-10-01: 22
  posts). Re-read a post right before editing it, and never overwrite a newer `post_modified`.

## Team (people, route by owner)

Félix Delaguía and Sonia Gómez Luzón: partners, final say on legal claims and brand. Rola Tabech:
project lead. Paul Taranto: tone of voice. César Mallent: visuals. Paul Leclerq: firm IT. Mike:
captain, integrator, SEO/GEO, and the only approver for publishing.

## Working style

- Internal notes in English. Client-facing copy in the formal register of each locale.
- Prefer honesty over polish. Report what failed.
- Record decisions in `docs/DECISIONS.md` with the date and who decided. No `2026-xx-xx`
  placeholders.
