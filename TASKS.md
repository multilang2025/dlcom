# Pending tasks: delaguialuzon.com blog (ES / EN / FR / RU)

Baseline: `data/audit_baseline.csv` (automated audit of all 366 published posts, 2026-10-01).
Counts below come from that file. Order = priority. IDs are WordPress post IDs.

## GSC-driven first batches (GSC 2026-06-30 → 09-28, 90 days)

Rule of thumb: large impressions at positions 4 to 10 with CTR under 1% means the snippet doesn't
answer the query, or the post looks out of date. Fix facts first, then title/meta/summary box, then
structure. Each row runs the full chain (audit → fact-check → stage → approve → write → verify) in
every `trid` sibling.

| # | Post | Impr. | Clicks | CTR | Pos. | Why / angle |
|---|---|---|---|---|---|---|
| G-1 | EN `/en/blog/minimum-interprofessional-salary/` | 256,744 | 521 | 0.20% | 5.9 | Queries are "minimum wage spain", "… per hour 2026", "… per month". Put the 2026 SMI monthly (14 and 12 payments), daily and hourly figures in the title, meta and summary box, fact-checked against the BOE royal decree. Its TOC anchors get 40–47K impressions each as jump links |
| G-2 | ES `/blog/calendario-laboral-2026/` | 232,989 | 2,282 | 0.98% | 5.2 | ES's top post. The 2027 calendar is published in the BOE in October, so prepare the 2027 update now. Slug contains a year: decide between a new post and a timeless slug + 301 (D-10) |
| G-3 | FR `/fr/blog/salaire-minimum-interprofessionnel-2025/` (13243) | 139,810 | 826 | 0.59% | 5.2 | Same SMI fix as G-1, written natively. Slug says 2025, title says 2026 (D-10). Edited 2026-10-01 by someone else, so re-read first |
| G-4 | FR `/fr/blog/regularisation-exceptionnelle-etrangers-espagne/` | 62,933 | 1,089 | 1.73% | 5.4 | FR's #1 click driver, and the deadline (30 June 2026) has passed. Facts and status first (T-12). Same for EN (35,176 impr, 214 clicks) |
| G-5 | EN `/en/blog/spanish-tax-deadlines/` | 54,934 | 11 | 0.02% | 9.9 | Near-zero CTR, so the snippet or year is stale. Rebuild around the current-year calendar (Modelo 100/720/210/303 dates) |
| G-6 | EN `/en/blog/empadronamiento-spain/` | 58,148 | 249 | 0.43% | 6.6 | Snippet: what the padrón is, documents, Valencia appointment steps |
| G-7 | EN `/en/blog/self-employed-spain-reduce-your-taxes/` | 50,482 | 117 | 0.23% | 6.3 | 2026 autónomo quotas and deductions, fact-checked |
| G-8 | EN `/en/blog/overstaying-visa-spain/` | 54,524 | 598 | 1.10% | 5.1 | Best EN post: protect it (facts, EEAT, 2026 sanctions/EES) |
| G-9 | ES `/blog/impuesto-sucesiones-comunidad-valenciana/` | 47,897 | 529 | 1.10% | 5.2 | 2026 Valencian relief rules, DOGV citations. FR sibling 35 clicks at pos 4.0 |
| G-10 | EN `/en/blog/children-born-spain-to-foreign-parents/` | 37,022 | 136 | 0.37% | 5.9 | Nationality rules (Código Civil art. 17), registration steps |

**Page-2 pushes** (position 9 to 20, impressions above 10K; content depth + internal links):
EN international-inheritances-in-spain (31K, pos 13.9), types-taxes-spain (23K, 16.2),
buying-property-spain (19K, 15.4, 3 clicks), beckham-law-spanish-tax-regime (13K, 18.0),
why-how-obtain-nie-in-spain (11.9K, 26.4: FR sibling ranks 9.4, so check cannibalisation with
green-card-nie-and-tie), residency-in-spain (23K, 10.9), everything-know-capital-gains-tax (16.6K, 14.7),
becoming-self-employed-in-spain (11.6K, 15.9). FR convention-fiscale-franco-espagnole (12.3K, 14.3).

**Low CTR, decent position (snippet rewrites, cheap)**: EN spain-corporate-tax (28K, 0.08%),
spain-regional-property-taxes (25.6K, 0.09%), apply-digital-nomad-visa-spain (25K, 0.20%),
long-term-residence-in-spain (22.5K, 0.18%), family-reunification-visa-in-spain (28K, 0.35%).
FR pourquoi-comment-obtenir-nie-espagne (27.4K, 0.56%), fiscalite-retraite-espagne (18.5K, 0.75%).

**Gaps in the GSC data**: the connector's per-property filter returned mixed results, and no RU URL
appeared in any top-100 list. Pull RU separately (Ahrefs `gsc-pages` or the GSC UI). ES posts beyond
the three above weren't in the top lists either.

## Done 2026-10-01 (live, verified)

- G-1 EN SMI 13250: 30 of 31 changes (change 11 on HOLD), SEO meta. Excerpt pending.
- G-2 ES calendario 16608: Option A content + 2027 section, title/meta/H1/excerpt (no slug change).
- G-3 FR SMI 13243: clean 2026 rewrite now rendered (Elementor flag removed).
- G-4 regularisation FR/EN/ES/RU: facts, no silence/appeal claims, CTA added, schema meta.
- 26678 health insurance: pasted CSS reset disabled, TL;DR box, new featured image (27910).
- 27316 regroupement familial: URL without `-2` + 301, 8 EN links localised.
- 27692: URL shortened to /fr/blog/s-installer-en-espagne/ + 301 (paragraphs/links: agent run).

## Content plan from enquiries (forms 2026-09-10 → 10-01, 53 entries)

Details, counts and cannibalisation notes: `data/content-ideas-2026-10.md` (aggregates only, no
personal data). Upgrades first, new posts last. Each item runs the full chain.

- [ ] **C-1 EN Beckham 892**: application after arrival, foreign income, spouse, changing employer/EOR (4 enquiries, pos 18).
- [ ] **C-2 FR year of departure**: reposition 2573 (not a 5th FR income-tax post). Link from 25839 (5 enquiries).
- [ ] **C-3 FR company pillar**: upgrade 1691, merge 3594 into it + 301 (**approval needed**) (5 enquiries).
- [ ] **C-4 EN DNV 8633**: broaden beyond UK, apply from inside Spain, family (3 enquiries, 25K impr 0.20% CTR).
- [ ] **C-5 FR bar/restaurant**: new post (planned topic, confirmed).
- [ ] **C-6 FR 2781**: employer-side section, French employer with a worker in Spain (2 enquiries).
- [ ] **C-7 EN 20998 (G-8)**: staying past 90 days legally, return after overstay (2 enquiries).
- [ ] **C-8 EN 17990**: arras + off-plan deposit H2s, linked from 25444.
- [ ] **C-9 ES** tarjeta familiar ciudadano UE (new, Elena). **C-10 ES** reclamación de cantidades (new, merge 4626 + 301, **approval needed**). **C-11 ES** baja IT larga (new). **C-12 ES** compra de vivienda (new).
- [ ] **Quick wins**: FR 1207 (EX-18 refusals), FR 4844 (changing gestor, late quarterly returns),
      EN 26847 (TIE after arrival, switch to self-employment), EN 649/2618 (expired NIE/TIE FAQ),
      FR 25839 FAQ, EN 20275 FAQ, CTA copy on fees/booking (7 enquiries ask the price).
- [ ] **Mike**: FR/RU immigration forms (11, 9) and Contact Us forms (1, 3) got 0 entries. Check they're still embedded.

## Related posts in the wrong language (Link Whisper, wp-admin re-scan)

39 posts: FR 10, ES 7, EN 11, RU 8. Lists: `data/related_posts_{fr,es,en,ru}_audit.csv`
(re-run `python tools/related_posts_audit.py`). ES "9988" is an English post tagged ES in WPML.

## Needs Mike / wp-admin (site-level, outside the posts-only Scope Gate)

- [ ] **T-01 hreflang missing on every post (366/366).** WPML / WP SEO Multilingual is not printing
      alternates. Check WPML → SEO options and the Rank Math + WPML integration.
- [ ] **T-02 Article schema.** 286 posts have no `BlogPosting` (FR 100/104, ES 82/84). Where it
      exists, 32 EN use an Organization author and 29 have no dates. Re-enable the Rank Math
      rich-snippet module (update Rank Math Pro first, since a 3.0.112 fatal is why it was disabled)
      and set the default schema to BlogPosting with the post author.
- [ ] **T-03 Brand in site schema.** `LegalService.name` = "Delaguía & Luzón" on every page →
      "Delaguía y Luzón" (Rank Math → Titles & Meta → Local SEO, plus site title
      "Delaguía&amp;Luzón").
- [ ] **T-04 "Première consultation gratuite" in the FR single-post template** (sidebar/CTA). Remove
      it from the template (FR variant). Check the ES/EN/RU variants for the same wording.
- [ ] **T-05 Two table-of-contents widgets in the single-post template** on every post. Keep one.
      Also remove the in-body TOC blocks on posts 636 (ES) and 14405 (FR) (agent task, after T-05).
- [ ] **T-06 EEAT template.** Add an author box and published/updated dates to template 4476 in
      ES/EN/FR (RU already shows the date). Create real author users (D-3).
- [ ] **T-07 Confirm decisions D-1 to D-9** in `docs/DECISIONS.md` (D-1 blog freeze first).
- [ ] **T-08 Security.** A plaintext wp-admin password sits in an old Claude memory file
      (`~/.claude/projects/c--Users-Mike-Dropbox-SEO-DelaguiaLuzon-DL-ANTI/memory/project_delaguialuzon.md`).
      Rotate the password and delete the line.

## P1: facts and legal accuracy (agents, posts only)

- [ ] **T-10 Golden Visa mentions** (20 posts). Keep only dated historical mentions.
      EN 26128, 23650, 21656, 23645, 10247, 17990, 20439, 18119, 12852, 3452, 4854 · ES 27107,
      20603, 12947 · FR 27307, 12930, 3455, 3243 · RU 12942, 3459.
- [ ] **T-11 Outdated years.** 109 posts mention only 2025 or earlier (ES 34, EN 22, FR 41, RU 12).
      Fact-check rates, thresholds and deadlines per `docs/03-FACT-CHECKING-PROTOCOL.md`, starting
      with tax (IRPF, Modelo 720/721, Beckham, sucesiones) and immigration.
- [ ] **T-12 Expired-deadline posts.** Regularisation of 30 June 2026 (21398 ES, 21452 EN, 21471 FR,
      23581 RU): check that each says the deadline has passed and what applies now (D-8).
- [ ] **T-13 Forbidden sources.** FR 3013 (garrigues.com) and FR 4413 (jacheteenespagne.com): remove
      the links and re-source the claims.
- [ ] **T-14 "Years of experience" wording → "since 1960"** (11 posts): EN 25362, 20432, 20394,
      20439 · ES 25946, 26290, 26306, 25908, 25881, 20515 · FR 20558.
- [ ] **T-15 RU calque check** («ненасыщенный») across all 28 RU posts (0 automated hits, so confirm by
      reading).
- [ ] **T-16 Citations.** 356/366 posts have no numbered citations and 281 have no sourced
      blockquote. Add official-source citations as part of each fact-check (no bulk insert).

## P2: bugs and technical (agents, posts only)

- [ ] **T-20 Canonical mismatch** (4): EN 24988, FR 24989, FR 13644, ES 9988 (English slug in ES, so
      check the WPML language) (D-9).
- [ ] **T-21 Duplicate `-2` slugs** (2): ES 27823, FR 27316. Find the originals and propose a merge
      plus 301 (approval needed).
- [ ] **T-22 Years in slugs** (11 posts). List only, no change without approval and redirects.
- [ ] **T-23 Self-links** (6 posts) and **thin internal linking**: 96 posts with fewer than 3
      contextual internal links (ES 32, FR 31, RU 22, EN 11). See `docs/08-INTERNAL-LINKING.md`.
- [ ] **T-24 Images not served as WebP** (61 posts): check Imagify coverage, then regenerate.
- [ ] **T-25 Manual bug pass** (layout, empty widgets, wrong-language strings, e.g. post 6359
      Spanish heading, mojibake) during the per-post review.

## P2: EEAT and NLP

- [ ] **T-30 Per-post EEAT score** (5 questions, `docs/04-EEAT-STANDARD.md`) during the manual pass.
- [ ] **T-31 Focus keyword audit and cannibalisation** per locale (SQL on `rank_math_focus_keyword`).
- [ ] **T-32 Thin posts.** 97 posts under 800 words (ES 32, FR 27, RU 21, EN 17): expand, merge or
      noindex, decided per post with GSC data.
- [ ] **T-33 Cluster gaps.** RU: 6 of 8 clusters empty. ES: Recursos Humanos 0 posts. EN: inheritance
      and audit. Family Law: nothing in any locale. Needs a plan, no writing until D-1 is settled.

## P3: style (agents, posts only)

- [ ] **T-40 Em/en dashes** in 163 posts (EN 75, FR 54, ES 19, RU 15).
- [ ] **T-41 Emojis in body** (59 posts: ES 29, FR 24, EN 6) and **title tags** (ES 27823, 23447).
- [ ] **T-42 Banned phrases** (112 posts). Top hits: "straightforward" 22, "ce guide" 12,
      "discover" 11, "it is important to" 11, "es importante" 11, "Chez Delaguía" 11, "genuinely" 10,
      "dans le cadre de" 7, "découvrez" 6, "il est important de" 5.
- [ ] **T-43 "Conclusion" H2** (17): ES 18894, 18685, 13716, 13529 · FR 27325, 2186, 18283, 13243,
      12930, 11817, 1130, 1557, 3274 · RU 13927, 13540, 11848, 3459.
- [ ] **T-44 Title tags.** 18 with a pipe (EN 13), 4 over 60 characters, 20 descriptions over 155,
      6 EN Title Case H1s, 6 numbered H2s.

## Suggested order of work

1. Mike: T-07 (D-1 first), T-08, then T-01/T-02/T-03/T-04/T-05 in wp-admin.
2. Agents: **G-1 to G-4 first** (SMI EN/FR, regularisation FR/EN, calendario laboral), through the
   full chain: audit → fact-check → stage → approve → write → verify. These carry the most traffic
   and the most fact risk, and they prove the write path (WPML fatal check) before scaling. Then
   G-5 to G-10.
3. Then EN, ES, RU batches. P1 items get handled inside each batch, and the P3 sweeps run per
   locale once the write path is proven.
