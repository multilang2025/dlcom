# TODO: delaguialuzon.com blog (ES / EN / FR / RU)

Updated 2026-10-01 (end of day). IDs are WordPress post IDs. Owners: **Mike** (FR + EN, approvals,
wp-admin), **Elena** (ES), **Maral** (EN with Mike), **agents** (`.claude/agents/dl-*`, posts only).
RU on hold. Anything that needs a URL change / 301 is parked in "Later: needs a 301" (Mike, 2026-10-01).

## 1. Needs Mike in wp-admin (outside the posts-only Scope Gate)

- [ ] **WPML `array_filter()` fatal** on `save_post` (`class-wpml-element-translation-package.php:354`,
      `add_custom_field_contents`). API saves of some posts write but return 500 (13243, 26678).
      Fix: WPML → Settings → Custom Fields Translation (set empty/non-array fields, often `_elementor_*`
      or Rank Math meta, to "Don't translate"/"Copy once"), update WPML + Translation Management, test on
      staging, else send the stack trace to WPML support.
- [ ] **Rank Math schema module**: enabling it causes a site fatal (Rank Math Pro 3.0.112 bug). Update
      Rank Math Pro on staging first, then re-enable and set default Article type = BlogPosting with the
      post author. Until then no Rank Math JSON-LD is output (FAQ schema saved on 21452/21471/21398/23581
      stays invisible).
- [ ] **hreflang** missing on most posts (WPML / WP SEO Multilingual alternates). 9988 now prints them
      after its WPML fix: compare its settings with a post that has none.
- [ ] **Brand in site schema**: `LegalService.name` "Delaguía & Luzón" → "Delaguía y Luzón" (Rank Math
      Local SEO + site title "Delaguía&amp;Luzón").
- [ ] **FR single-post template**: remove "Première consultation gratuite" (check ES/EN/RU variants).
- [ ] **Two TOC widgets** in single-post template 4476: keep one. Then agents remove in-body TOC blocks
      on 636 (ES) and 14405 (FR).
- [ ] **EEAT template**: author box + published/updated dates in template 4476 (ES/EN/FR). Create real
      author users (D-3).
- [ ] **Forms with 0 entries in 3 weeks**: FR/RU immigration forms (ids 11, 9) and Contact Us (1, 3).
      Check they are still embedded and sending.
- [ ] **Attachment 16617 alt** ("Delaguía&Luzón" + zero-width space) on the calendario post.
- [ ] **Review draft 26642** (visa non lucratif, merged + fact-checked, featured image 28012) before publishing.
- [ ] **Connectors**: reconnect Google Search Console in AISA settings; add an OpenRouter key if AISA
      `fact_check` should work.
- [ ] **Security**: rotate the wp-admin password that sat in an old Claude memory file
      (`~/.claude/projects/c--Users-Mike-Dropbox-SEO-DelaguiaLuzon-DL-ANTI/memory/project_delaguialuzon.md`)
      and delete that line.
- [ ] **Repo**: `AGENTS.md` + `.codex/agents/*.toml` were added outside the Claude session and are now
      pushed. Keep or remove.

## 2. Decisions for Mike / Félix and Sonia

- [ ] D-2 FAQ length (8 to 10 vs exactly 5). D-3 authors and reviewers. D-4 Spanish register.
      D-5 RU conventions. D-6 EN double line breaks. D-7 which fixes are worth doing before migration.
      D-10 calendario laboral slug (Option B: timeless slug + 301, decide before the 2027 BOE list).
- [ ] **Félix/Sonia, legal**: UGE positive silence (mention or not, Ley 14/2013 art. 76.1); Golden Visa
      transitional provision heading says "inmuebles" but text covers all investors; regularisation RU/
      FR/EN/ES keep or drop "a refusal ends the provisional permission"; EN SMI change 11 (absorption
      reform) on HOLD; EN SMI open points (withholding at SMI level, 2026 tarifa plana amount, DNV
      threshold basis used by UGE).

## 3. Later: needs a 301 (parked, approval per item)

- [ ] ES calendario laboral 16608 → timeless slug (D-10).
- [ ] FR company pillar: merge 3594 into 1691 (C-3).
- [ ] ES reclamación de cantidades: merge 4626 into the new post (C-10).
- [ ] FR purchase pillar: rebuild 4413, consolidate 2146 + 4687 (purchase vs sale taxes); merge 905 into
      the Modelo 210 post 25665 once published.
- [ ] ES 27823 `-2` slug (duplicate check first).
- [ ] 10 remaining posts with a year in the slug (list in `data/audit_baseline.csv`, `year_in_slug`).
- [ ] EN SMI 13250: slug lacks the keyword ("minimum wage").

## 4. Agents, P1 (facts and broken rendering)

- [ ] **27307 unsourced figures** still in the text: the 90-day entry window, "renouvelable jusqu'à
      cinq ans", 34 188 € (DNV threshold). Verify or replace with a CTA.
- [ ] **11 FR posts still show the old Elementor version** while a 2026 rewrite sits unused in
      post_content: 11817, 8655, 12930, 8615, 8402, 2687, 18814, 2823, 7335, 10335, 10629. Per post:
      decide which version is newer, clean the rewrite (emojis, "&", "65 ans", fake offices, unverified
      claims, inline sources, TL;DR), then switch rendering (remove `_elementor_edit_mode`) as for 13243.
- [ ] **EN SMI 13250**: excerpt not written (needs a REST save); FAQ answer on offsetting carries the same
      claim as HOLD change 11; propagate verified SMI fixes to ES 25913.
- [ ] **Golden Visa mentions** (T-10): EN 26128, 23650, 21656, 23645, 10247, 17990, 20439, 18119, 12852,
      3452, 4854 · ES 27107, 20603, 12947 · FR 12930, 3455, 3243 · RU 12942, 3459 (27307 done).
- [ ] **Outdated years** (T-11): 109 posts mention only 2025 or earlier. Tax and immigration first.
- [ ] **Forbidden sources** (T-13): FR 3013 (garrigues.com), FR 4413 (jacheteenespagne.com).
- [ ] **"Years of experience" → "since 1960"** (T-14): EN 25362, 20432, 20394, 20439 · ES 25946, 26290,
      26306, 25908, 25881, 20515 · FR 20558.
- [ ] **RU calque check** «ненасыщенный» across the 28 RU posts (T-15).

## 5. Agents, GSC-driven upgrades (FR + EN first)

Remaining from the first GSC batch (G-1 to G-4 are done):
- [ ] G-5 EN `/en/blog/spanish-tax-deadlines/` (55K impr, 0.02% CTR): rebuild on the current-year calendar.
- [ ] G-6 EN empadronamiento (58K, 0.43%). G-7 EN self-employed taxes (50K, 0.23%).
- [ ] G-8 EN overstaying-visa (54K, 1.1%): protect (facts, EEAT, EES). G-9 ES sucesiones Valencia (Elena).
- [ ] G-10 EN children born in Spain (37K, 0.37%).
- [ ] Page-2 pushes and cheap snippet rewrites: see `data/content-ideas-2026-10.md` and the GSC list
      (EN international inheritances, types of taxes, buying property, Beckham, NIE, residency, capital
      gains, becoming self-employed; FR convention fiscale; EN corporate tax, regional property taxes,
      DNV, long-term residence, family reunification; FR NIE, fiscalité retraite).

## 6. Content plan (from 3 weeks of enquiries + FR topic list)

Details and cannibalisation notes: `data/content-ideas-2026-10.md`. Upgrades first, new posts last.
- [ ] C-1 EN Beckham 892 · C-2 FR year of departure (reposition 2573) · C-4 EN DNV 8633 (beyond UK)
- [ ] C-5 FR bar/restaurant (new) · C-6 FR 2781 employer side · C-7 EN 20998 staying past 90 days
- [ ] C-8 EN 17990 arras / off-plan · C-9, C-11, C-12 ES new posts (Elena)
- [ ] FR topic list: new "Acheter un terrain en Espagne", new "Vendre un bien immobilier en Espagne",
      NIE from France as a section in 2396, finish Modelo 210 draft 25665 with "comment payer".
- [ ] Quick wins: FR 1207 (EX-18 refusals), FR 4844, EN 26847, EN 649/2618, FR 25839 FAQ, EN 20275 FAQ,
      CTA copy on fees/booking (7 enquiries ask the price).

## 7. Agents, site-wide sweeps (rules of 2026-10-01)

- [ ] **TL;DR box** at the top of every post (start with the GSC top posts per locale).
- [ ] **Inline sources**: convert every bottom reference list / `[n]` markers into inline anchor links.
- [ ] **Pasted HTML/CSS**: 10 other posts carry `<style>` blocks (27692, 25840, 24609, 20515, 25653,
      5190, 23647, 21606, 25966, 25993, 27307 done). 25840 has the global reset; 27692 has a broken
      unclosed block. Neutralise or remove.
- [ ] **Internal links**: same-locale only, hub links (inbound links to 27692 from 900, 2396, 1207,
      20166, 26678), 96 posts with fewer than 3 internal links, 6 self-links.
- [ ] **27692 leftovers**: Agencia Tributaria link without target/rel; broken `<style>` block.
- [ ] **Style**: dashes (163 posts), emojis (59), banned phrases (112), "Conclusion" H2 (17), title tags
      (18 pipes, 20 long descriptions), canonical mismatches (EN 24988, FR 24989, FR 13644).
- [ ] **Featured images**: replace AI-looking images (text, logos, landmark mashups) with realistic ones.
- [ ] **Related posts**: re-run `python tools/related_posts_audit.py` after new posts are published
      (Link Whisper may assign the wrong language to new posts again).

## Done 2026-10-01 (live, verified)

- SMI: FR 13243 rewrite live + inline sources + URL /fr/blog/smi-espagne/ (301); EN 13250 30/31 changes.
- ES calendario 16608: facts + 2027 section, title/meta/H1/excerpt.
- Regularisation FR/EN/ES/RU: facts, CTA instead of silence/appeal claims, inline sources, schema meta.
- 26678 health insurance: CSS leak fixed, TL;DR, realistic featured image.
- 27316 regroupement familial: `-2` removed + 301, EN links localised.
- 27692: URL /fr/blog/s-installer-en-espagne/ + 301, paragraphs, FR links, betranslated link removed.
- 27307: merged with draft 26979, cleanup pass (TL;DR, FAQ, sources, FR focus, title tag "6 voies"),
  fact-check fixes (Golden Visa transitional rule, legal processing maximums, driving licence rule,
  TIE obligation + fine, TIE exemption for Ley 14/2013 art. 75.4 visas).
- Drafts: 26979 and 27304 trashed; 26642 merged, fact-checked, featured image.
- Related posts: 35 posts fixed; all locales now 100% same-language (9988 fixed by its WPML re-tag).
- Repos: rules + agents in `dlcom`; `dlvibe` PR #95 (not merged). Slack handoff sent to Elena and Maral.
