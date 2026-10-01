# Internal linking (blog, per locale)

## Rules

- Same locale only. ES posts link to ES URLs, FR to `/fr/…`, and so on. A cross-locale link is a bug.
- Every blog post links **up** to its practice-area page in the same locale, **across** to 1 or 2
  sibling posts in the same cluster, and gets at least 2 links **in** from other posts (no orphans).
- Anchors: descriptive, varied, natural in the sentence. Never the same exact-match anchor twice for
  one target. Never "click here" / "aquí" / "ici".
- Never link to the post itself, to drafts, or to URLs that redirect (link straight to the final URL).
- Contextual links in the body come first. "Related posts" blocks don't count toward the minimum.
- 3 to 8 contextual links per long-form post.

## Clusters (practice areas)

Immigration and residency · Tax (IRPF, IRNR, Modelo 720/721, Beckham, double tax treaties) ·
Inheritance and estate planning · Property (purchase, rentals, short-term lets, squatters) ·
Labour and HR (contracts, dismissal, SMI, payroll) · Company and self-employed (autónomo, SL,
accounting, audit) · Living in Valencia (NIE, banking, healthcare, festivals). Known gaps (2026
audit): RU has no blog support in 6 of 8 clusters, ES has no posts under Recursos Humanos, EN has
no Inheritance/Audit supporting posts, and there is no Family Law content anywhere.

## Method

1. Build the link graph from the live HTML (`tools/audit_blog.py` already counts links out; inbound
   links come from inverting the out-links across all posts). Link Whisper's report in wp-admin is
   a cross-check.
2. For each post: missing up-link, missing sibling, orphan (0 inbound), cross-locale links, links to
   redirects or 404s (Broken Link Checker list).
3. Propose insertions as anchor + sentence + target in `data/staging/<id>.md`. Write them via
   `content/edit` (07-EDIT-AND-PUBLISH).
4. Re-run the graph and confirm no orphans remain in the batch's cluster.
