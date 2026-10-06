# Brief: UK/US audience work (EN), 2026-10-06

Mike approved: "Start with the upgrades, then draft N-1, N-2 and N-3". Plan: `data/content-ideas-uk-us-2026-10.md`
(read it, especially sections 1 to 4). Verified legal facts: `data/staging/uk-us-legal-checks.md` and
`data/factcheck/uk-us-plan.csv` (59 claims, dated 2026-10-06). Reuse those facts, quote their sources inline,
and verify anything else you add on official pages (BOE, AEAT, DGT, HMRC, gov.uk, IRS, SSA, EUR-Lex, DOGV).
AISA `fact_check` is unavailable. Open every page you cite. Quoted legal text must be verbatim.

Read first in `C:\Users\Mike\Documents\DealguiaLuzonLegacy`: CLAUDE.md, docs/02-STYLE-GUIDE-MASTER.md,
docs/style-guides/STYLE-GUIDE-EN.md, docs/03-FACT-CHECKING-PROTOCOL.md, docs/07-EDIT-AND-PUBLISH-PROCESS.md,
docs/09-REVIEW-QA-GATE.md and `.claude/agents/dl-blog-editor.md` (it carries the 2026-10-02 lessons).

## Rules for EN posts (the reader: UK and US people moving to or owning property in Spain)
- UK spelling, sentence-case H1 and headings, no dashes (em or en), no emojis, no banned phrases ("discover",
  "genuinely", "honestly", "straightforward", "it is important to", "navigate the complexities", "65 years").
  Brand "Delaguía y Luzón" (never "&"). "since 1960" (never a year count). One office, Valencia.
  No free-consultation wording.
- **TL;DR first**: H2 "<keyword>: key points" with 4 to 7 self-contained factual bullets.
- Short paragraphs (2 to 4 sentences). Disguised lists become lists. Sentences that need a dash get rephrased.
- **Sources inline** on descriptive anchors, `target="_blank" rel="nofollow noopener"`. No [n] markers and no
  reference list at the bottom. No competitor law firms or agencies as sources.
- **Unsure = CTA**: say what the source says, then invite the reader to contact the firm to confirm their case.
  Never guess and never soften into something vague. EN contact: Félix Delaguía,
  felix.delaguia@delaguialuzon.com, +34 963 74 16 57. CTA block before the FAQ.
- FAQ questions as H3. Keep the FAQ length of an existing post. New drafts: 6 to 8 questions.
- **Scope note** (proposal D-11, Mike's call later): in each new draft and in each new section of an upgraded
  post that touches US or UK tax, say once near the top that the post covers Spanish law and the Valencian
  angle, and that readers should coordinate US or UK filing with their home-country adviser. Keep it to one
  sentence so it is easy to remove. We do not give US or UK tax advice.
- Internal links: EN only (`/en/blog/...`), current URLs, no self-links, no redirects; check each with curl.
  **Link only to published posts.** Never link to a draft (it 404s for readers). If a link to a new post would
  be useful, list it in your report as "add on publication".
- No pasted `<html>/<head>/<body>/<style>`. Inline-styled TL;DR div as in other posts is fine.
- Legal wording that is announced or pending is written as pending, with "as at 6 October 2026" style dating.

## Writing to WordPress (posts only)
- Site `https://delaguialuzon.com`. WPVibe `rest_api` / `run_wp_cli` (site_url above) and AISA `db_query`
  (site `delaguialuzon.com`, chat_id `dl-legacy-uk-us`). **No raw mutating SQL and nothing that creates a
  WPVibe approval link** (Mike: they expire and annoy). Use `POST /wpvibe/v1/content/edit`,
  `POST /wpvibe/v1/elementor/save-page`, `PUT /wp/v2/posts/<id>`, `POST /rankmath/v1/updateMeta`.
- Existing EN posts: re-read right before editing (`post_modified`); never overwrite a newer edit.
  Elementor posts (`_elementor_edit_mode = builder`): the live body is `_elementor_data`. Keep every
  container, column and widget id; you may add new text-editor content inside existing widgets or add a
  widget with a fresh 8-hex id. Do not touch `_elementor_edit_mode`.
- Writes can return HTTP 400/500 (WPML `array_filter` fatal) and still commit. Always read back by SQL
  (MD5 or LIKE). After writing run `run_wp_cli "cache purge"` (a url-only purge may leave the old body), then
  curl the live URL and check your text is there.
- **WPML copies `_elementor_edit_mode` across a post's translations on save.** Before your first save, look up
  the post's trid siblings (`dlg_icl_translations`) and their `_elementor_edit_mode`; after your last save,
  check they are unchanged and say so in your report. Never save a sibling of another locale yourself.
- Do not edit posts outside your assignment. Other agents are working in parallel on other EN posts. Use your
  own scratchpad subfolder named after your posts.
- Staging and logs: `data/staging/<id>-uk-us.md` (what changed, facts used, open points), exact stored body in
  `data/staging/<id>-uk-us.html` or `.json`, `data/factcheck/<id>.csv` (post_id,lang,claim,verdict,evidence,
  source_url,checked,siblings,action), `data/changelog/<id>.csv` (date,post_id,lang,change,verified).
  For drafts use the new post id. Do not git commit.

## Upgrades (existing posts)
Keep the post's angle and URL. Update title tag, meta description and excerpt only if a change makes them
wrong; Rank Math title at most 60 characters, description at most 155. Also fact-check the existing sentences in
the sections you touch and the Modelo 720, IRNR, tax-rate and date statements anywhere in the post, correcting
or CTA-ing what is wrong or outdated (2025 and 2026 changes). Add a TL;DR if the post has none, convert a
bottom reference list to inline links if present, and add the 3 most useful links to published EN posts.

## New drafts
- Create as a **draft** (`status: draft`), language **EN** in WPML (verify in `dlg_icl_translations`:
  `language_code = 'en'`, `element_type = 'post_post'`, no accidental translation links to ES/FR/RU posts), author
  the same as other recent EN posts, category as the closest existing EN posts. Body in `post_content` (no
  Elementor; `_elementor_edit_mode` empty) using the same HTML conventions as RU 24774 or FR 8655 (inline-styled
  TL;DR div, H2/H3, tables, lists, CTA block). Slug from the focus keyword, short (4 to 6 words).
- Title (H1) at most about 60 characters, sentence case, focus keyword near the start. Rank Math title,
  description (at most 155), focus keyword (a noun phrase) via `updateMeta`. Excerpt written.
- 1,800 to 2,800 words, UK spelling, 6 to 8 FAQs, at least 3 inline official sources per major section, at
  least 3 internal links to published EN posts.
- No featured image yet (Mike decides; realistic images only). Say so in the report.
- Do not publish. Do not set a future date.

## Report back (concise)
Per post: what changed (or the draft's id, URL slug, title, word count), facts verified or CTA'd, open points
for Félix/Sonia, links to add on publication, final MD5 + `post_modified`, WPML sibling check result, live
verified yes/no (upgrades), and anything you could not do.
