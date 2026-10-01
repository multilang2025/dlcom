# NLP and entity SEO for blog posts

Goal: each post is unambiguous to search engines and AI answer engines about **which legal
entities, procedures and places** it covers, and answers the reader's questions in extractable
form. Adapted from dlvibe's "entity-level SEO integration" list, extended for the blog.

## Core entities to name precisely (in the locale's own wording)

- Institutions: AEAT, BOE, Seguridad Social (TGSS), Oficina de Extranjería, Policía Nacional
  (TIE/NIE), Registro Civil, Registro de la Propiedad, Notaría, Catastro, Generalitat Valenciana,
  ATV, LABORA, SEPE, Ayuntamiento de València.
- Laws and regimes: Ley de Extranjería (LO 4/2000) and its Reglamento (RD 1155/2024), Ley 28/2022
  (Startups, Digital Nomad Visa), Beckham regime (art. 93 LIRPF), IRPF, IRNR, Impuesto de
  Sucesiones y Donaciones, Plusvalía municipal, IBI, IVA, Impuesto de Sociedades, ETVE, Modelo
  720/721/210/100/303/111/190, Estatuto de los Trabajadores, Código Civil, the Spain-UK/-France/
  -Belgium double tax treaties, EU Succession Regulation 650/2012.
- Places: Valencia (Comunitat Valenciana), the Valencian province towns used in the posts, the
  readers' countries (UK, France, Belgium, Russia/CIS, Ukraine).

Use the official name at first mention, then the common short form. Give the acronym's expansion
once per post. Use the same term consistently across a cluster (don't alternate "TIE", "residence
card" and "foreigner card" without explaining that they're the same document).

## Per-post NLP checks

1. **Focus keyword** (`rank_math_focus_keyword`) is in the H1, the first 100 words, at least one H2,
   the title tag, the meta description and the slug, inflected naturally (FR/RU/ES grammar first).
2. **Search intent match**: the first screen answers the query directly (definition, amount,
   deadline, yes/no). The summary box does this.
3. **Question coverage**: compare the H2/H3 set with the People-Also-Ask and AI-answer questions
   for the keyword in that locale's market (google.es for ES/FR/EN residents, google.fr for France
   readers, google.co.uk for UK). Add missing sub-questions as H2/H3 or FAQ entries.
4. **Entity coverage**: list the entities a complete answer needs (from the list above plus top-3
   SERP results). Each missing one is either added or consciously skipped.
5. **Extractable answers**: each H2 opens with a 1 or 2 sentence direct answer before the detail
   (for AI Overviews and LLM citations). Use tables for comparisons and numbered lists for
   procedures.
6. **No keyword stuffing**: the exact-match keyword appears at most about 1% of the time. Use
   synonyms and inflections.
7. **Cannibalisation**: no two posts in the same locale target the same focus keyword. Check with
   `SELECT post_id, meta_value FROM dlg_postmeta WHERE meta_key='rank_math_focus_keyword'`
   grouped by language. Duplicates go to `TASKS.md` as merge/differentiate candidates.
8. **Locale market fit**: EN is written for UK readers (post-Brexit, HMRC, ISAs, pensions), FR for
   French/Belgian readers (impôts.gouv, convention fiscale franco-espagnole), RU for
   Russian-speaking residents (non-lucrative residency, property, banking constraints), ES for
   Spanish-resident and LatAm readers. A post that answers the wrong reader gets **fresh copy**, not
   a translation.

## Tools

- AISA `fact_check` for claims. Ahrefs/Semrush MCP (`keywords-explorer-*`, `serp-overview`,
  `organic_research`) for SERP questions and competing pages. GSC via Ahrefs `gsc-*` for the queries
  each URL already ranks for (start with those, not new keywords).
- Ahrefs project 2552491 = delaguialuzon.com.
