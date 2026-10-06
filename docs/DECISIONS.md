# Decisions log (legacy WordPress blog)

Add the date and who decided. Move an item to "Decided" once it's settled.

## Open

- **D-1: Blog freeze vs this work (raised 2026-10-01).** dlvibe records "Don't touch the blog posts
  yet" (Mike, 2026-09-25). On 2026-10-01 Mike scoped this repo to the WordPress blog (style, bugs,
  NLP, EEAT, fact checking), and 22 WP posts were edited between 2026-09-24 and 10-01. Assumption:
  the freeze applies to the rebuild's copy, not to the live WP blog. Mike to confirm.
- **D-2: FAQ length.** WordPress-era blog rule: 8 to 10 questions as H3. Rebuild rule (2026-09-24):
  exactly 5. Which applies to WP blog posts?
- **D-3: Authors and reviewers (EEAT).** Which partner or lawyer signs and reviews which practice
  area. Can Félix's desk photo (dlvibe `docs/photo-library/felix-delaguia-lecture-code-bureau.jpg`)
  be used as the author photo? Colegiado numbers to publish?
- **D-4: Spanish register.** Usted throughout, or nuanced by audience.
- **D-5: RU conventions.** Banned openers and heading capitalisation, plus a native reviewer.
- **D-6: EN "two line breaks after every full stop".** Proposal: drop it (formatting quirk).
- **D-7: Legacy WP vs rebuild.** Which fixes are worth doing on WordPress before migration? Proposal:
  facts and EEAT first (they carry over to the rebuild's copy), template/schema fixes only if
  cut-over is more than about 2 months away.
- **D-8: Expired posts.** News-pegged posts whose subject has passed (e.g. regularisation deadline
  30 June 2026): update in place, add an "expired" notice, or noindex?
- **D-9: The four posts whose canonical points elsewhere** (24988, 24989, 13644, 9988). 9988 is an
  English slug in the ES section, possibly mistagged like 24445 in April.

- **D-10: Year-specific posts with a year in the slug** (calendario-laboral-2026,
  salaire-minimum-interprofessionnel-2025, 9 others). Options: (a) keep the URL and update the content
  yearly (the slug looks stale); (b) move to a timeless slug with a 301 (equity kept, one-time
  risk); (c) a new post per year (splits equity). Proposal: (b) for SMI, and for the calendar decide
  before the 2027 BOE publication (October).

- **D-11: Scope of UK and US tax content (raised 2026-10-06).** Proposal: new UK/US-audience posts cover
  Spanish law and the Valencian angle, say so at the top, and send US or UK filing questions to the
  reader's home-country adviser (compliance, and it serves IFAs and foreign firms). Existing EN posts 20275
  and 22034 already comment on US or UK tax: keep them as they are, or add the same scope note? Mike to decide.

## Decided

- 2026-09-24 (Mike): "since 1960", never a year count. No free-consultation claim anywhere. Six
  languages served.
- 2026-09-23 (Mike): firm emails on `.com`. FR headings in noun form. Images WebP with native alt.
- 2026-09-22 (Mike): one office (Valencia). Golden Visa removed as an available route.
- 2026-09-15 (Mike): no em or en dashes. No walls of text. Varied anchors.
- 2026-05 (Mike): agent writes limited to `post_type=post` (Scope Gate).

- 2026-10-01 (Mike): freeze applies to the rebuild only; the WP blog is in scope (closes D-1).
- 2026-10-01 (Mike): regularisation posts make no claim about silence/refusal/appeals after the
  3-month mark; a CTA invites readers to contact the firm for confirmation instead.
- 2026-10-01 (Mike): featured image of 26678 replaced by a generated documentary-style photo
  (doctor's consultation, attachment 27910), no text, no logos, no landmarks.
- 2026-10-01 (Mike): D-10 for FR SMI: 13243 moved to /fr/blog/smi-espagne/ (Permalink Manager),
  301 from /fr/blog/salaire-minimum-interprofessionnel-2025/ (Rank Math), internal links in 8655 and
  13923 updated. Same method used for 27316 (-2 removed) and 27692 (/fr/blog/s-installer-en-espagne/).
- 2026-10-02 (Mike): the 11 FR posts stuck on old Elementor versions (11817, 8655, 12930, 8615, 8402,
  2687, 18814, 2823, 7335, 10335, 10629) switched to their cleaned, fact-checked 2026 rewrites in
  post_content. Method: `_elementor_edit_mode` set to empty via `/wpvibe/v1/content/edit` (meta), not
  raw SQL (WPVibe approval links expire in minutes; Mike asked to avoid them). `_elementor_data` kept as
  rollback. Nobody should open these posts with "Edit with Elementor": it would reload the old version.
- 2026-10-02 (Mike): RU blog CTAs name the firm's Russian-speaking agent, Olesia Davidova
  (o.davidova@delaguialuzon.com, +34 96 352 32 91), as on the RU service pages, never Félix. Applied
  to all 28 RU posts the same day (content/edit replace_all on the rendered body).
- 2026-10-02 (Mike): RU pass (freshness, naturalness, format, CTA) on all 28 RU posts. Dashes: rephrased
  everywhere (0 kept), so the master no-dash rule holds for RU without a D-5 exception so far.
- 2026-10-01 (Mike): duplicate drafts merged: 26979 into 27307 (then trashed), 27304 into 26642 (27304
  trashed, 26642 kept as draft with featured image 28012).
