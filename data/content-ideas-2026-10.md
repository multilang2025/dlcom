# Content ideas from website enquiries: 2026-09-10 → 2026-10-01

Source: Formidable Forms entries (`dlg_frm_items`, `is_draft = 0`, `created_at >= 2026-09-10`),
read on 2026-10-01 through AISA `db_query` (read only). Messages were classified by hand in session.
This file holds **aggregates and paraphrased patterns only**: no names, emails, phone numbers,
addresses, companies or quotes. Coverage compared with `data/inventory.csv` (366 published posts),
Rank Math focus keywords and the GSC notes in `TASKS.md`. Nothing was written to WordPress.

## (a) Request volume

**Total: 53 enquiries** in 3 weeks (about 18 per week). 30 private clients, 13 companies, 10 from
the two immigration forms, which have no client-type field.

### Per form

| Form (id) | Locale | Entries |
|---|---|---|
| Formulaire général FR (5) | FR | 18 |
| General Enquiries (4) | EN | 13 |
| Form general ES (2) | ES | 9 |
| Form Extranjeria (8) | ES | 6 |
| Immigration Form (10) | EN | 4 |
| Form general RU (6) | RU | 3 |
| Contact Us (1, 3), Form pop up RU (7), RU immigration form (9), FR immigration form (11) | — | 0 |

**Per locale:** EN 17 (32%), FR 18 (34%), ES 15 (28%), RU 3 (6%). By message language, FR rises to
19, because one French-language enquiry came through the ES form. Six enquiries were written in a
different language from their form: FR in the ES form, Dutch and Spanish in the EN form, English in
the RU form, and English twice in the ES immigration form. The FR style guide says FR brings 47% of
form enquiries. In this window it brought 34 to 36%, behind EN once both EN forms are counted.

### Per week (ISO weeks)

| Week | Dates | ES | EN | FR | RU | Total |
|---|---|---|---|---|---|---|
| W37 | 10–13 Sep (partial) | 2 | 2 | 3 | 0 | 7 |
| W38 | 14–20 Sep | 5 | 10 | 8 | 1 | 24 |
| W39 | 21–27 Sep | 7 | 3 | 5 | 1 | 16 |
| W40 | 28 Sep–1 Oct (partial) | 1 | 2 | 2 | 1 | 6 |

### Enquiry-type dropdowns (as selected by the sender)

- ES general: Derecho laboral 5, Derecho inmobiliario 2, Derecho de extranjería 2.
- EN general: Immigration law 5, Tax law 5, Real estate law 3.
- FR général: Autre(s) 7, Droit fiscal 4, Audit et restructuration 2, Droit civil et successions 2,
  Droit commercial 2, Droit des étrangers 1. "Autre(s)" is the top FR choice, and most of those
  turned out to be company set-up or gestor requests.
- RU: tax 1, immigration 1, labour 1.
- Immigration forms (location field): Spain 6, abroad 4.

### Per topic (one primary topic per enquiry, from the message text)

| Topic | Total | EN | FR | ES | RU | Recurring sub-topics |
|---|---|---|---|---|---|---|
| **Immigration** | **17** | 9 | 2 | 6 | 0 | DNV / international telework 3; EU-citizen family card (EX-19), spouse or registered partner 2; EU-citizen registration (EX-18) / settling as EU retirees 2; overstay / staying past 90 days 2; student visa → long-term stay or self-employment 2; NIE/TIE renewal or TIE appointment 2; nationality (Ley 20/2022) 1; work visa / shortage-occupation list 1; vague relocation 2 |
| **Tax** | **13** | 5 | 5 | 1 | 2 | Moving tax residence / double-tax treaty (FR–ES 3, UK–ES 1, RU-linked 1) 5; Beckham regime 4; non-resident withholding / fiscal representative 2; ongoing compliance via a gestor (IRPF return, missed autónomo quarterly returns) 2 |
| **Labour / payroll** | **6** | 0 | 1 | 5 | 0 | Employee disputes 4 (dismissal and SMAC conciliation, wrong professional category, unpaid travel allowances for a displaced worker, long sick leave); cross-border employment, French employer with someone working from Spain 2 |
| **Company set-up** | **5** | 0 | 5 | 0 | 0 | Trading SL, holding above existing companies, food-service business, registration plus founder residence, selling a French company and reinvesting after the move |
| **Property** | **5** | 3 | 0 | 2 | 0 | Arras deposit not returned 1; off-plan purchase contract review 1; buying out a co-owner's 50% 1; purchase funded by a family gift from foreign accounts 1; licence to rent a room in one's own home 1 |
| Inheritance / donation | 1 | 0 | 1 | 0 | 0 | Revoking a donation received (plus 3 secondary mentions: gift-funded purchase, succession planning on arrival, foreign gift/inheritance) |
| Family law | 1 | 0 | 1 | 0 | 0 | Children placed in care |
| Commercial dispute | 1 | 0 | 0 | 0 | 1 | Dispute with a former contractor |
| Off-topic / unclear | 4 | 0 | 3 | 1 | 0 | Two requests to open a bank account, one insurance account, one vague "financial law" |

Secondary mentions across all 53: tax comes up in 17 enquiries, company or autónomo in 10, fees or
price in 7, inheritance or gift in 4, a WhatsApp or call request in 3. Probable duplicate: one
family seems to have written twice (ES general and ES immigration form, same situation). Counts keep
both entries.

**Plain read:** EN enquirers want a route into Spain (DNV, Beckham, TIE, overstay). FR enquirers
are settling or setting up businesses (company, tax residence change, gestor). ES enquiries are
mainly employment disputes, plus immigration from Latin American and family-member cases. RU is too
small to read.

## (b) Top recurring questions (paraphrased, 2 or more occurrences)

1. **Beckham regime (4):** "I've just moved for a job. Can I still apply, and how do I do it once I
   have my NIE?" "What happens to my other income (a family company abroad, investments)?" "Does my
   self-employed spouse qualify?" "If I change employer or go remote for a foreign company, through
   an EOR or as a contractor, do I keep the regime and my residence permit?"
2. **Moving tax residence to Spain (5):** "How is the year of the move taxed in France/the UK and in
   Spain?" "I was posted to Spain under French withholding and now have a Spanish contract. Where do
   I declare what?" "How do I treat freelance invoices issued before the move but paid after?"
   "What should a newly resident couple set up: status, tax, social security, succession?"
3. **Setting up a company in Spain from France (5):** "What are the steps and the tax for an SL?"
   "Can I put a Spanish holding above my existing companies?" "Should we move our French company or
   create a new one after selling up?" "How do I register a business and get residence at the same
   time?"
4. **Digital nomad / telework visa (3):** "Can I apply from inside Spain, and with my spouse and
   children?" "Which suits me better as a non-EU founder running a company abroad: DNV or the
   entrepreneur route?" Plus the tax set-up that goes with it.
5. **Employee disputes in Spain (4, ES):** "I was dismissed for low performance: how do I challenge
   it at the SMAC?" "My contract category is lower than the job I actually do." "My employer doesn't
   pay travel allowances and prorates my extra pay." "My partner is on long sick leave. What happens
   next, and how do we prepare?"
6. **EU-citizen family members (2, ES):** "What does a residence card for my non-EU spouse or
   registered partner involve, and what does it cost?"
7. **Overstay and the 90-day rule (2, EN):** "I overstayed. Can I come back, and when?" "I'm a
   tourist with an EU passport pending. How can I legally stay past 90 days?"
8. **TIE / NIE after arrival (2, EN):** "My NIE/TIE lapsed, can it be fixed?" "I'm a student going
   round in circles trying to get the TIE appointment."
9. **Student visa → long-term stay (2, ES, probably one family):** "We have student visas and have
   bought a franchise. How do we switch to self-employment and stay?"
10. **French employer, worker in Spain (2, FR):** "Our employee will live in Spain for more than 6
    months on a French contract: who runs the Spanish payroll?" "I work from Spain on a Spanish
    contract for a French company and have a dispute. Can you help?"
11. **EU registration certificate and settling as EU citizens (2, FR):** "My EX-18 was refused twice:
    can you handle it?" "We're retiring here permanently and own a flat. Which papers do we need?"
12. **Ongoing compliance (2, FR):** "Our gestor vanished and Q1/Q2 autónomo returns weren't filed"
    or "we're newly resident and need someone for the tax return."
13. **Non-resident withholding (2, B2B):** artist fees paid by a foreign company; acting as fiscal
    representative for a foreign non-profit receiving a prize.
14. **Cross-cutting: "How much does it cost?" (7)** and "Can we talk on WhatsApp or by phone?" (3).

## (c) Content plan (prioritised)

Priority = enquiry volume × locale order (FR/EN, then ES) × GSC upside × fact risk. Every item runs
the full chain (`docs/06` → `03` fact-check → stage → Mike approves → write → verify) and follows
the 2026-10-01 rules: TL;DR first, inline sources, unsure claims become a CTA. Only 3 of the 12 are
new posts. The rest upgrade or merge existing posts, to avoid adding to cannibalisation.

| # | Locale | Working title | Target query | Intent | New / upgrade | Link to | Cannibalisation note |
|---|---|---|---|---|---|---|---|
| 1 | EN | Beckham Law Spain 2026: eligibility, application steps and changing employer | beckham law spain; beckham law application | Informational → consult | **Upgrade 892** `/en/blog/beckham-law-spanish-tax-regime/` (pos 18.0, 13K impr) | 26587, 20275, 15116, 8633, 27449 | Keep 892 as the only Beckham pillar. 26740, 25591 and 25592 mention Beckham: anchor "Beckham Law" to 892, no new Beckham post. New sections: application after arrival (NIE/NIF → affiliation → Modelo 149 window), foreign income under the regime, spouse and children, changing employer / EOR / contractor. **High fact risk** (Ley 28/2022 changes). Unsure points become a CTA |
| 2 | FR | Année du départ de France vers l'Espagne : résidence fiscale, déclarations et double imposition | année de départ impôts France Espagne; changement de résidence fiscale Espagne | Informational → consult | **Upgrade + reposition 2573** `/fr/blog/declarer-les-impots-en-espagne/` (thin, overlaps 4580/4371/2645) | 25839, 2645, 4371, 8655, 25840 | FR income-tax cluster already has 4 overlapping posts (2573 "déclarer les impôts", 4580 "impôts sur le revenu", 4371 "IRPF", 2645 "fiscalité espagnole"). Give 2573 the year-of-departure angle instead of adding a 5th. 25839 keeps the treaty query and links here for the transition year. Covers posting → local contract, micro-entrepreneur invoices paid after the move, newly resident couple checklist. French-side rules need impots.gouv / BOFiP sources. **High fact risk** |
| 3 | FR | Création de société en Espagne depuis la France : étapes, coûts et fiscalité | créer une société en Espagne; ouvrir une entreprise en Espagne | Commercial | **Upgrade 1691** `/fr/blog/creer-entreprise-en-espagne/` + **merge 3594** (607 words) with 301 | 2687, 2362, 10023, 15202, 3496, 27307 | 1691 ("entreprise en Espagne") and 3594 ("ouvrir une entreprise") compete. Merge 3594 into 1691 (slug/301 needs Mike's approval, `docs/DECISIONS.md`). Add H2s: transfer of an existing French company vs new SL, holding above existing companies (summary + link to 10023), founder residence for non-EU founders (link 27307). 5 FR enquiries this window |
| 4 | EN | Digital Nomad Visa Spain 2026: requirements, applying from inside Spain and bringing family | digital nomad visa spain | Informational → consult | **Upgrade 8633** `/en/blog/apply-digital-nomad-visa-spain/` (25K impr, 0.20% CTR) | 21544, 892, 27337, 18119, 26130 | Broaden from a "UK citizen's guide" to all non-EU nationals (enquirers came from non-UK countries). Keep 21544 (US W-2) as the niche page and link both ways. Add "from inside Spain (UGE) vs consulate", "DNV vs entrepreneur route". ES 27107 and FR 25663 are separate native posts: don't translate. Title/meta rewrite also covers the low-CTR item in `TASKS.md` |
| 5 | FR | Ouverture d'un bar ou d'un restaurant en Espagne : licences, local et structure juridique | ouvrir un restaurant en Espagne; licence bar Espagne | Commercial | **New post** (one of the 8 planned FR topics) | 1691, 2687, 15202, 25840, 3496 | No FR post on hospitality. 15202 (franchise) is a different intent: link to it, don't overlap. Activity licences depend on the municipality (Valencia: declaración responsable vs licencia ambiental). Name the city and source it, or route it to a CTA. Takeaway vs on-site cooking matters for the licence |
| 6 | FR | Salarié en Espagne d'une entreprise française : contrat, paie espagnole et cotisations | salarié en télétravail en Espagne entreprise française; paie salarié Espagne | B2B commercial | **Upgrade 2781** `/fr/blog/teletravail-en-espagne/` (new employer-side H2) | 8655, 7650, 25839, ES sibling 20930 | 2781 already touches A1 / employer, but from the teleworker's side. Add the employer section rather than a new post, so 2781 and 8655 ("travailler en Espagne") don't compete. Fact-check: Reg. 883/2004 art. 13, cross-border telework framework agreement, Spanish employer registration without an establishment |
| 7 | EN | What happens if you overstay your visa in Spain (new H2s: staying past 90 days legally; returning after an overstay) | overstay visa spain; stay in spain more than 90 days | Informational → consult | **Upgrade 20998** `/en/blog/overstaying-visa-spain/` (G-8, best EN post) | 25381, 25207, 25589, 26124 | Fold into G-8 rather than a new "extend stay" post, which would compete with 25381 (tourist visa). EES, Schengen 90/180 and entry-ban rules (LO 4/2000) need official sources |
| 8 | EN | Buying property in Spain (new H2s: arras contracts and getting a deposit back; off-plan deposit guarantees) | arras contract spain; off-plan property spain deposit | Informational → consult | **Upgrade 17990** `/en/blog/buying-property-spain/` (19K impr, pos 15.4, 3 clicks) | 25444, 20430, 24445, 27052 | 25444 (conveyancing) also mentions arras. Make 17990 the home for arras/off-plan detail and link to it from 25444. FR purchase pillar via 4413 (planned) and ES item 12 are separate native pieces. Off-plan guarantees (Ley 38/1999 DA 1ª) need a source |
| 9 | ES | Tarjeta de familiar de ciudadano de la UE: cónyuge y pareja de hecho | tarjeta familiar comunitario; tarjeta familiar UE pareja de hecho | Informational → consult | **New post** (Elena) | 27755, 25966 | No ES post on this (ES has 6 immigration-form enquiries but almost no immigration content). EN 26124 and FR 27322 cover marriage natively. RD 240/2007 as amended by RD 1155/2024 (partner requirements changed): **high fact risk** |
| 10 | ES | Reclamación de cantidades al empresario: categoría profesional, dietas y pagas extra | reclamar diferencias salariales categoría; dietas impagadas | Informational → consult | **New post + merge 4626** (old dietas news post) with 301 | 21973, 27733, 13716, 22166 | One piece instead of three (category, allowances, prorated pay all came up). 4626 ("gastos de locomoción") is outdated news, so absorb it. Statutory deadlines (one year, ET art. 59) need sources |
| 11 | ES | Baja por incapacidad temporal de larga duración: plazos, alta médica e incapacidad permanente | baja larga duración; baja por depresión cuánto dura | Informational | **New post** (lower priority) | 21973, 13716 | No ES post on IT/sick leave. Check ES drafts (13) first in case one covers it. 365/545-day limits need sources |
| 12 | ES | Compra de vivienda en España: arras, contrato privado y obra nueva sobre plano | contrato de arras; comprar vivienda sobre plano | Commercial | **New post** (lower priority, ES has no purchase post) | 27714, 4757 | ES has zero purchase content (5 property enquiries, 2 in ES). Cover co-owner buy-outs (extinción de condominio) and gift-funded purchases (donation tax) as H2s here rather than separate posts |

Planned FR topics reconciled with the enquiries: **bar/restaurant** confirmed (item 5). **Purchase
pillar via 4413**: no FR property enquiries this window, but EN/ES property demand (item 8/12) backs
it. Keep it, and remove the forbidden jacheteenespagne.com source first (T-13). **NIE from France as a
section in 2396**: weakly supported (1 FR enquiry mentions holding an NIE). Keep it as a section, no
new post. **Modelo 210 draft 25665**: no FR enquiry, but the two B2B non-resident withholding
enquiries (EN/ES) show demand. Keep it. **Terrain** and **vente**: no enquiry signal this window.

## (d) Quick wins (existing posts where readers still have questions)

| Post | Locale | Gap shown by enquiries | Fix |
|---|---|---|---|
| 1207 `/fr/blog/differences-carte-verte-nie-et-tie/` | FR | EX-18 refused twice; retirees settling | H2 « Refus du certificat d'enregistrement : motifs fréquents et recours » (resources, health cover). Recourse routes need a source, else CTA |
| 4844 `/fr/blog/comment-trouver-un-bon-gestor-en-espagne/` | FR | Gestor disappeared, quarterly autónomo returns not filed | H2 « Changement de gestor et régularisation des déclarations trimestrielles » (Modelo 130/303, late-filing surcharges: LGT art. 27, sourced) |
| 26847 `/en/blog/spain-student-visa/` | EN (+ ES demand) | TIE appointment after arrival; switching to self-employment | Expand "After your studies" with the switch to cuenta propia, plus a TIE-after-arrival step (30-day rule, cita previa) |
| 649 / 2618 (NIE/TIE EN) | EN | NIE/TIE lapsed | FAQ "My NIE certificate or TIE has expired: what now?". Also settle the 649 vs 2618 overlap already flagged in `TASKS.md` |
| 25839 `/fr/blog/convention-fiscale-franco-espagnole/` | FR | Posted worker → Spanish contract | FAQ entry linking to item 2. Page-2 push already listed (pos 14.3) |
| 20275 `/en/blog/uk-spain-double-taxation/` | EN | UK investments for a Spanish resident | Short H2 or FAQ on UK investment income, linking 27449 (ISAs) |
| All CTAs (ES/EN/FR) | all | 7 enquiries ask the price, 3 ask for WhatsApp/phone | CTA copy: say how a first consultation is booked and that fees are quoted per case. No "free consultation" (T-04), no invented prices. Contact channels are Mike's call |
| 20166 `/fr/blog/ouvrir-un-compte-en-banque-en-espagne/` | FR | 2 FR enquiries asked the firm to open a bank account | Hypothesis (form entries carry no referrer): make clear in the TL;DR that the firm advises but doesn't open accounts. Check GA4 landing pages before acting |

## Notes and limits

- RU (3 enquiries) is on hold. For the record: RU has two Beckham posts (1772, 26964), and 26964's
  focus keyword is « вид на жительство в Испании », which doesn't match its topic.
- The FR and RU immigration forms (11, 9) and the "Contact Us" forms (1, 3) got 0 entries. Check
  whether they're still embedded anywhere (site-level, Mike).
- Family law (children in care) shows up once. It matches the cluster gap T-33 (no Family Law posts
  in any locale) and is blocked by D-1.
- Classification is manual, on 53 short messages. Treat counts under 3 as signals, not trends.
- GSC figures come from `TASKS.md` (90 days to 2026-09-28), not from a fresh pull.
