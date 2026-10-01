# Review and QA gate (nothing is published without it)

A single chokepoint, carried over from the dlcom/dlvibe "QA/Publisher" role. A post change is
publishable only when every box is ticked in its `data/staging/<id>.md`.

## Checklist

- [ ] Scope: `post_type=post` only, no template/page/settings change
- [ ] Re-read right before writing, and `post_modified` unchanged since staging
- [ ] Style: zero banned phrases, zero em/en dashes, zero emojis, no free-consultation, brand
      written "Delaguía y Luzón", "since 1960", sentence-case headings, one H1
- [ ] Structure: summary box H2 first, CTA before FAQ, FAQ as H3 and mirrored in schema, no wall of text
- [ ] Facts: every checkable claim has a verdict row and a citation, and no `UNVERIFIABLE` claim is left
      in the text
- [ ] Translations: the same fact is checked in every `trid` sibling
- [ ] Links: same-locale internal links, varied anchors, external links nofollow/noopener/_blank to
      approved sources only, no self-links, no redirects
- [ ] NLP: focus keyword in H1, title, description and first 100 words, no cannibalisation
- [ ] Meta: title ≤ 60, description ≤ 155, no emoji, no pipe
- [ ] Locale: written for that locale's reader, not translated, register per locale guide (RU calque
      check)
- [ ] TL;DR box first (H2 with keyword, 4 to 7 self-contained factual bullets)
- [ ] Sources linked inline on descriptive anchors, no reference list at the bottom
- [ ] No claim the source doesn't support; unclear points end in a "contact us to confirm" CTA
- [ ] No pasted `<html>/<head>/<body>/<style>` markup in the content
- [ ] Featured image looks real (no text, logos or fake landmarks), native alt text
- [ ] Short slug (Permalink Manager) + 301 if the URL changed, old internal links updated
- [ ] Related-posts block shows only same-language posts
- [ ] Verified live after the cache purge, and the audit row re-run with no regressions
- [ ] Logged in `data/changelog.csv`

## Escalation

- Legal interpretation, new regime, contested point: Félix/Sonia via Mike.
- Anything outside posts: `TASKS.md` → "Needs Mike / wp-admin".
- Tone of voice disputes: Paul Taranto via Mike.
