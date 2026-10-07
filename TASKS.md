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
      cinq ans", 34 188 € (DNV threshold). Verify or replace with a CTA. RU 24295 research (2026-10-02): the
      law says 200 % of the SMI, the consulates publish 2 442 €/month for 2026, and 2 849 € / 34 188 € is on no
      official source (the visa lasts at most 1 year, then a 3-year permit renewed in 2-year periods).
- [ ] **Re-check FR 2823, 10629, 12930 for new housing decree-laws (from 2026-10-07).** The press (Infobae
      2026-10-05, El Correo Gallego 2026-10-06) says the Government will re-submit decrees like RDL 26/2026
      and 27/2026 to the Consejo de Ministros on 6 Oct, to be validated by the Diputación Permanente (the Cortes
      were dissolved by RD 806/2026, BOE 2026-10-06, elections 29 Nov). The BOE of 6 Oct has none. The three
      FR posts say so in one sentence ("Cette page sera mise à jour…" on 2823). If a new RDL is published, rewrite
      the same passages again. Owner: Mike.
- [ ] **RDL 26/2026 and 27/2026 were repealed by Congress on 2 Oct 2026** (BOE-A-2026-20526 and
      BOE-A-2026-20527). FR 2823, 10629, 12930 and RU 1824, 12942, 15904 were corrected on 2026-10-06 (old LAU,
      LIVA, IRPF and IBI rules apply again). Still to check, owners Mike/Maral/Elena: sibling posts that may
      state the VAT rule for stays of 30 nights or less or other decree measures: EN 15852, 991, 25415, 2869,
      ES 15812, FR 15895. Leases signed or extended on 1 or 2 Oct 2026: left as a CTA (Félix/Sonia).
- [ ] **Siblings of the 11 switched FR posts** probably carry the facts fixed in FR (Golden Visa scope,
      quarterly Modelo 210, registry, VAT speculation, AEAT eIDAS claim): EN 2869, 12852, 10659, 10351,
      11830, 8398 · ES 12947, 10615, 10318, 11788, 7717 · RU 12942, 10376. Elena (ES), Maral + Mike (EN).
- [ ] **Follow-ups from the 11 FR rewrites** (details in `data/staging/<id>-rewrite.md`):
      10629 H1 still says "NRA" (title proposed) · 18814 orphan (link from 1691, 10023, 2297, 17410) and
      competes with 1557 (merge = 301, see section 3) · 7335 few inbound links (3013, 2519, 25839) ·
      focus keywords are verb phrases on 8402, 8655, 12930 · FAQ schema JSON for 8655/10335 ready in
      staging, apply when the Rank Math schema module is back · 2678 body still has "Delaguía & Luzón" ·
      24989 canonical 404 + "&", "depuis 1994", emojis · 15720 [n] markers + Références list.
- [ ] **Link Whisper related posts** show the news post "Delaguía & Luzón fête son 65e anniversaire"
      (and event posts like "CDRC – Paris 2025") as related posts on topical articles. Rename that
      post's title to the house brand or exclude news/events from related posts (Link Whisper settings: Mike).
- [ ] **EN SMI 13250**: excerpt not written (needs a REST save); FAQ answer on offsetting carries the same
      claim as HOLD change 11; propagate verified SMI fixes to ES 25913.
- [ ] **Golden Visa mentions** (T-10): EN 26128, 23650, 21656, 23645, 10247, 17990, 20439, 18119, 12852,
      3452, 4854 · ES 27107, 20603, 12947 · FR 12930, 3455, 3243 · RU 12942, 3459 (27307 done).
- [ ] **Outdated years** (T-11): 109 posts mention only 2025 or earlier. Tax and immigration first.
- [ ] **Forbidden sources** (T-13): FR 3013 (garrigues.com), FR 4413 (jacheteenespagne.com).
- [ ] **"Years of experience" → "since 1960"** (T-14): EN 25362, 20432, 20394, 20439 · ES 25946, 26290,
      26306, 25908, 25881, 20515 · FR 20558.
- [ ] **Re-check monthly from Nov 2026 (RU pass 2026-10-02)**: BOE for (a) (a, DONE 2026-10-07: Orden HAC/1028/2026, in force 6 Oct 2026) and (b) the DAC8 transposition law
      and the Modelo 175 order (RU 9220, 11848; FR 8615, 11817). Update the "на 2 октября 2026 года" lines.
- [ ] **URGENT, Mike (wp-admin): WPML copies `_elementor_edit_mode` across translations** (found
      2026-10-02). Saving any post in a trid copies the field from the trid source to every translation.
      Both directions hurt: (a) RU 9220 (source FR 8615, switched) fell to its stale post_content and was
      restored to `builder` twice; (b) RU saves of 8407, 10376, 11848, 12942 copied `builder` from their
      ES/EN sources onto **FR 8402, 10335, 11817, 12930**, which went back to their old Elementor versions
      until reset to empty at about 17:10. Any save of a sibling will do it again. Fix: WPML → Settings →
      Custom Fields Translation → `_elementor_edit_mode` → "Don't translate". Until then, after any save
      of a sibling of the 12 switched FR posts (13243 + the 11), re-check the FR mode and reset it.
      It happened again on 2026-10-06: FR 10629 (old Elementor body live for about 3 minutes), FR 12930 (twice)
      and FR 8402 flipped to `builder`; EN 2869 flipped to empty twice. All reset and checked. Saving an FR post
      with an empty mode also pushes "empty" onto its EN/ES translations: check them after every save.
- [ ] **Follow-ups from the RU pass (2026-10-02)**, details in `data/staging/<id>-ru-pass.md`:
      Link Whisper re-scan for RU (404s `/ru/blog/program-permanent-hiring-qualified-young-people/`,
      `/ru/blog/программа-постоянного-трудоустройст/`, `/ru/blog/продление-ненасыщенного-вида-на-жите/`;
      a 301 `/ru/blog/subsidies-indefinite-hiring-unemployed/`; self-links on 7869, 8364) · WPML: RU 8364
      alone in trid 1328 while ES 7708 / EN 8357 / FR 8361 sit in trid 1310 · RU 26964 was a published
      duplicate carrying the Ukraine residence offer (295 €): body replaced, decide if the offer gets its own
      post (rollback in revision 26965) · stale Rank Math FAQ/Article schemas on most RU posts (not output
      while the module is off) · 13794 lost its Elementor FAQ JSON-LD (JSON staged) · RU contact page and
      site LegalService schema still use "&" · /ru/налоговые-услуги/ 301s to a non-RU URL (page, Mike).
      Félix/Sonia: DNV threshold 2 442 € vs 2 849 € (200 % SMI basis), 183-day counting, Beckham + Valencian
      wealth-tax minimum, MiCA "payments-only" company, registry numbers after the STS, RDL 27/2026
      transitional regime, Russia DTT status.
- [ ] **Siblings flagged by the RU pass** (owners: Elena ES, Maral + Mike EN, Mike FR): EN 892 / FR 888
      (Beckham 45 % → 47 %), EN 13538 / FR 13539 (inheritance region, "treaty"), EN 3452 / FR 3455 (Golden Visa
      "only real estate"), EN 649 / FR 1207 (NIE "valid 3 months", EX-19), EN 25993 / FR 26023 (STS
      "731/2023"), EN 13919 / FR 13923, EN 991 / FR 1130, EN 15852 / FR 15895 (VAT claims), FR 13762
      ("Madrid case"), FR 1819, EN 8126 / 8130 / 24772, FR 7837 / 7911 / 24773 / 11969, ES 26737 / EN 26740 /
      FR 26760 ("65 años"), EN 1563 ("Part 1"), ES 10318 / EN 10351 (eIDAS plan stated as fact).
- [ ] **Re-check on 16 Oct 2026 (RU pass 2026-10-02)**: LABORA ECOVUL 2026 and ECOGJU 2026 close on
      15 Oct 2026. Rewrite RU 7869, 7928 and the LABORA section of RU 24774 as "closed" and point to the 2027
      calls once published in DOGV. Siblings still on the 2024 calls (11.113 €): EN 8126, 8130 · FR 7837,
      7911 (FR 7911 also says "15 juin" and 22 000 €) · ES 7816, 7885. Tarifa plana 2026 amount: same open
      point as FR 8655 (Félix/Sonia); RU 24774 carries a CTA instead of a figure.
- [ ] **Re-check monthly from Nov 2026 (FR 25840 fact check, 2026-10-06, `data/staging/25840-factcheck.md`)**:
      (a) BOE for a Ley de Presupuestos 2026/2027 or a decree-law fixing the cuota reducida amount from 2026
      (art. 38 ter LETA, DT 5a RDL 13/2022); until then the 80 € is stated for 2023 to 2025 only (FR 25840,
      8655, EN 2564, RU 24774); non-linked posts that still say "80 € in force in 2026": ES 27855, ES 24717,
      FR 24773, EN 25362; (b) the bill derived from RDL 3/2026 (Congress, urgent procedure) for amendments to
      art. 3.4 (autónomo tables); (c) the 2027 contribution order (MEI 1,00 % in 2027, LGSS DT 43a) and 2027
      tables; (d) the Valencian "cuota cero" announced on 28/09/2026 (2 years, 4 for young people): wait for
      DOGV text before any statement; (e) TRRETA 2026 call (sede.gva.es id_proc 18856). Also ES 27855 carries
      the same errors as FR 25840 (15 tramos "200 a ~590 €", 88,56 €, cuota cero in Valencia): needs its own pass.

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
- [ ] **UK and US audience plan (2026-10-06)**: `data/content-ideas-uk-us-2026-10.md`. Upgrades first:
      U-1 rebuild EN 15116 Modelo 720 (+ Modelo 721, which no EN post mentions), U-2 refresh 10247, U-3 US
      section in 892, U-4 25233, U-5 UK retirees in 20394, U-6 American buyers in 24445, U-7 Valencian wealth
      tax section in 22409 (2 M€ from 2026), U-8 move the "non-resident income tax" focus keyword off 2175,
      U-9 2564, U-10 soften the unsourced ISA claim in 27449 (CTA). Then new drafts: N-1 non-resident tax / Modelo 210, N-2 UK inheritance tax (long-term
      residence), N-3 US-Spain treaty, N-4 taxation of UK pensions, N-5 Valencian wealth tax, N-6 401(k)/IRA
      (specialist review), N-7 selling or renting the UK home, N-8 US Social Security, N-9 estate planning
      for Americans. Owners: Mike + Maral. Reconnect Search Console first to re-rank on demand.
      Legal checks done 2026-10-06 (`data/staging/uk-us-legal-checks.md`). N-2, N-4 and N-6 wait for
      Félix/Sonia (UK State Pension art. 17 or 18(2), UK lump sum, SIPPs, ISA income, 401(k)/IRA).
- [ ] **Re-checks for the UK/US posts**: ITSGF for tax year 2026 before N-5 (monthly from Nov 2026) · on
      1 Jan 2027 the new Modelo 210 expenses annex applies and the first April filings are 1 to 20 April 2027
      (Orden HAC/623/2026) · HMRC IHTM47 and legislation.gov.uk s.6A at publication of N-2, N-3, N-4, N-9 ·
      DGT database for a ruling on the UK State Pension and UK lump sums before N-4.
- [ ] **UK/US work done 2026-10-06** (`data/staging/uk-us-brief.md`, notes `data/staging/<id>-uk-us.md`):
      upgrades live on EN 15116 (Modelo 720 + 721), 10247, 20394, 27449, 892, 25233, 24445, 22409, 2564, and the
      Rank Math keyword/title of 2175; drafts 28177 (N-1 non-resident tax), 28176 (N-2 UK inheritance tax),
      28172 (N-3 US-Spain treaty). Before publishing a draft: Félix/Sonia review of the points in its staging
      note (N-2 and N-3), then `dl-qa-publisher`, FAQ schema when the
      module is back, a `curl -I` on the Permalink Manager URL, and `python tools/related_posts_audit.py en`.
      Add inbound links on publication: N-1 from 27052, 24445, 18877, 20275; N-2 from 10247, 25233, 13538, 20275;
      N-3 from 20275, 22034, 26126, 21544, 892, 15116; and from 27449, 892, 10247, 20275, 22034 to 15116.
- [x] 2026-10-06: featured images generated (nano_banana_pro, 16:9, documentary, no text/logos/flags) and set on
      28177 (attachment 28239), 28176 (28240), 28172 (28241), with native alt text. Handoff sent to Maral on Slack
      (DM, 2026-10-06). Roles: Maral = English copywriting only; Elena = mostly ES and supervises all languages with
      Mike; Elena's `PLAN:` drafts 28169, 28170, 28171 are briefs for Maral (keep; Elena trashes them after publication).
- [x] 2026-10-06 "fix everything" round, live and verified: EN 27052 (24 % to 19 % on gains, deadlines,
      plusvalía), EN 25207 (ETIAS 20 €, EES dates, unofficial link), EN 22409 excerpt, EN 15116 H1 (URL unchanged),
      body JSON-LD on EN 25233 and 24445 (slugs, placeholder image, unsourced price), FR 888 (Beckham) and FR 2678
      (Modelo 720 + 721), and the repealed-decree claims in EN 15852, 991, 2869, 13755, 4734, 1815 and FR 13762,
      15895. Notes in `data/staging/<id>-fix.md`, `-schema.md`, `-rdl-siblings.md`.
- [ ] **Still open from that round**:
      Mike, wp-admin: check Rank Math > Schema on EN 892 and 24445 (the stored schema was rewritten but the
      read-back was blocked) · stored schema still stale on FR 888 and 2678 ("&" brand, old FAQ, "Modelo 030") and
      "price 60 EUR" on EN 27052 and 25207 · site-wide LegalService JSON-LD still "Delaguía & Luzón" with the
      Logo-65 image · EN 27052 Rank Math title has "&" · do not reopen 27052 and 25207 in Elementor (stale mirrors).
      Agents/Mike: FR 15895 DONE 2026-10-06 (full rewrite in the Elementor widgets, see data/staging/15895-rewrite.md; its
      Rank Math schema is still stale) · EN 991 "no-obligation consultation" wording
      and "&" brand · FR 13762 unsourced "320 000 logements" box · EN 25444 (quarterly non-resident filing,
      "Royal Legislative Decree 1/2004" cited as the Land Law) · EN 2869 title typo "Porperty" and banned
      "Navigating the complexities" · EN 1815 fines "from 6,000 €" (minor fines go up to 10,000 €) and the
      Valencia moratorium date · EN 13755 two overlapping FAQ blocks (after D-2).
      Elena (ES): 15812, 907, 4757, 13730 likely carry the same VAT/ViDA, "2 services", IAE 861.1, registry and
      repealed-decree claims.
      STS 1025/2025 and 642/2026 could not be verified and were removed from EN 13755; bring them back only after
      someone reads the full text on CENDOJ.
- [ ] **Related lists with broken items (found 2026-10-06 on FR 25839)**: 31 posts (FR 13, ES 17, EN 1) show an item
      without an image: a deleted post id (25668 on FR 25839, saved by Link Whisper in June with a URL now owned by the
      page itself), legal or office-landing pages (`/fr/mentions-legales/`, `/despacho-abogados-...`, `/en/thanks/`) and
      posts with no featured image. `python tools/related_posts_audit.py` now also flags self-links and image-less
      items; `python tools/related_posts_repair.py` keeps the good items and replaces only the broken ones
      (`data/related_posts_repair.csv`, three UPDATE statements in `data/related_posts_repair.batch.sql.txt`). Needs one
      WPVibe approval per statement (raw SQL on the Link Whisper table). Also: give featured images to the FR/ES posts
      that have none (`impot-successions-espagne`, `droits-de-succession-en-espagne`,
      `nouvelles-revisions-aux-indemnites-kilometriques`, ...) and keep Link Whisper from listing pages (its settings).
- [x] 2026-10-06: FR 25840 list indentation fixed (WordPress auto-paragraph filter had inserted `<p>` tags into the
      pasted `<style>`, so the browser dropped the list rules). Stylesheet now scoped to `.article-wrapper`; a full
      rewrite into inline-styled HTML like FR 10629 is still the clean long-term fix. Same pasted-CSS pattern: 27692,
      24609, 20515, 25653, 5190, 23647, 21606, 25966, 25993 (check each for broken list/heading styles).
- [ ] **BLOCKER 2026-10-07: WPVibe and AISA cannot reach the site** (Cloudflare 521 from WPVibe, "connection refused"
      from AISA, since about 14:36 UTC). The site itself loads normally from Mike's machine, so the origin or its
      firewall is probably refusing the connectors' IP ranges (heavy traffic today: crawls, 40-50 KB SQL calls, 100+
      writes). Mike: check the host firewall / WAF / rate limit and allowlist WPVibe (static-IP relay) and AISA, or
      contact WPVibe support with the hostname. Until then nothing can be written.
- [ ] **Verifactu update staged, NOT applied** (facts and exact old-to-new edits in `data/staging/verifactu-update-2026-10.md`
      and `data/staging/{8402,28307,8407,8175,15895}-verifactu.json`). Finding: on 5 Oct 2026 Hacienda's press note
      announced postponing the pending RD 1007/2023 obligations to October 2028 (alignment with e-invoicing for businesses
      up to 8 M€), but **no legal text is published yet**: the dates in force on 7 Oct are still 1 Jan 2027 (corporate tax
      filers) and 1 Jul 2027 (others). E-invoicing: Orden HAC/1028/2026 (BOE 5 Oct, in force 6 Oct 2026) starts the RD 238/2026
      clocks: 12 months (turnover above 8 M€) and 24 months (others), so about Oct 2027 and Oct 2028 (computed). Apply when
      the connectors work: FR 8402 (post_content; WPML trap with RU 8407, ES 7717, EN 8398), FR 15895, RU 8407, RU 8175, ES
      28307. ES 28307 (created 2026-10-06 by user 29) was built around 2026/2027 dates: Elena to review its other
      problems (Excel claim, fines per ejercicio, unsourced 10 000 € fine, Facturae 3.2.2 vs UBL, tú/usted mix).
- [ ] **Verifactu re-checks**: from 2026-10-08 and weekly (after the Consejo de Ministros) for the instrument that carries the
      2028 date (Cortes dissolved: a decree-law would go through the Diputación Permanente); then change "announced" to the
      legal wording in FR 8402, 15895, RU 8407, 8175, ES 28307. 6 Oct 2027 and 6 Oct 2028: confirm e-invoicing start dates.
      Check the Rank Math FAQ schema of RU 8407 and 8175 for old Verifactu dates.
- [ ] **New housing decree-laws published 7 Oct 2026**: RDL 28/2026 and 29/2026 (BOE 7 Oct). Re-read them and re-check the
      pages corrected on 6 Oct (FR 2823, 10629, 12930, 15895 · EN 15852, 991, 2869, 1815, 4734, 13755 · RU 1824, 12942, 15904).
- [ ] **Related-posts repair (31 posts)**: EN 13755 applied 2026-10-07 (approval op_5859cf3d89b945f2). FR (13 posts) and ES
      (17 posts) statements still to submit (`data/related_posts_repair.batch.sql.txt`); needs the connectors back.
      FR 25839's dead first item (post 25668) is fixed in that FR statement.
- [ ] **Re-check 7 and 8 Oct 2026**: press (Infobae 5 Oct) says the Government plans to re-approve the housing
      decrees on 7 Oct. If new decree-laws appear in the BOE, the pages corrected today need another pass: FR 2823,
      10629, 12930, 15895 · EN 15852, 991, 2869, 1815, 4734, 13755 · RU 1824, 12942, 15904.
- [ ] **WPVibe quota**: the account showed 405 of 500 calls used in the rolling 24 hours during today's batch.
      Check https://mcp.wpvibe.ai/account before the next large batch (AISA `update_post` and `flush_caches`
      are a fallback for post-modified bumps and cache purges).
- [x] **Draft clash resolved**: the "PLAN" drafts 28169, 28170, 28171 are Elena's briefs for the writer (Maral).
      Keep them until the articles are published, then Elena trashes them. 28170 (Spanish income tax return for
      Americans, Modelo 100) is the brief for the next EN draft.
- [ ] **For Félix/Sonia from this work**: UK State Pension art. 17 or 18(2) (the ruling V1380-25 cited by the
      first checker could not be found in the DGT database, so only V2460-21 is cited) · UK 25 % lump sum, SIPPs,
      ISA income · 401(k)/IRA and US Social Security benefits · treaty benefits for Beckham holders ·
      Modelo 720 for Beckham family members · Valencian succession bonus for non-resident heirs and UK IHT
      credit · imputed income 2026 (1.1 % or 2 %, repealed with RDL 26/2026) · whether a non-resident can combine
      regional wealth-tax rules with the 700 000 € minimum · non-lucrative visa renewal amount (art. 62(2)).
- [ ] **Re-check monthly from Nov 2026**: the final order creating Modelo 721 (a draft of 10 March 2026 exists)
      and DAC8 transposition · AEAT 2027 filing-window page (Dec 2026) · any DGT or AEAT ruling on ISAs, SIPPs and
      401(k)/IRA.
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
- 2026-10-02: 11 FR posts (11817, 8655, 12930, 8615, 8402, 2687, 18814, 2823, 7335, 10335, 10629)
  switched from old Elementor versions to cleaned, fact-checked 2026 rewrites (TL;DR, inline sources,
  brand/1960/Valencia, FR links); live QA passed. Logs in `data/changelog`, `data/factcheck`, `data/staging`.
- 2026-10-02: RU pass on all 28 RU posts (freshness, naturalness, format, CTA; calque «ненасыщенный»
  removed, T-15 closed). Live QA: 28/28 TL;DR, 1 H1, 0 dashes/emojis/"&", RU-only links and related
  posts. CTAs use Olesia Davidova (Mike). Logs in `data/factcheck`, `data/changelog`, `data/staging`.
- Drafts: 26979 and 27304 trashed; 26642 merged, fact-checked, featured image.
- Related posts: 35 posts fixed; all locales now 100% same-language (9988 fixed by its WPML re-tag).
- Repos: rules + agents in `dlcom`; `dlvibe` PR #95 (not merged). Slack handoff sent to Elena and Maral.
