# Fact-checking protocol (blog, all locales)

The firm's blog makes specific legal and tax claims. A wrong rate or an expired deadline is a
reputational and regulatory problem, not an SEO one. Source: dlvibe
`docs/04-FACT-CHECKING-PROTOCOL.md`, adapted to the existing posts.

## What counts as a checkable claim

Tax rates and brackets, thresholds (Modelo 720's €50,000…), deadlines and campaign dates, fees
(tasas: 790-012 amounts…), form numbers (EX-15 vs EX-18, Modelo 210/720/721/100), article numbers
(Ley, Real Decreto, BOE references), minimum wage (SMI), IPREM, residency income requirements,
processing times, statistics, named rulings, "since/from <date>" statements, and anything
introduced by "currently", "now", "this year", "en 2026".

## Approved sources

- BOE (boe.es), the primary source for laws, royal decrees and orders
- AEAT (sede.agenciatributaria.gob.es, agenciatributaria.es)
- Seguridad Social and the Inclusion/Migration ministry (seg-social.es, inclusion.gob.es,
  mites.gob.es), plus extranjeros.inclusion.gob.es for immigration procedures
- INE (ine.es), La Moncloa, the European Commission and EUR-Lex
- Generalitat Valenciana: hisenda.gva.es, atv.gva.es (cite DOGV for Valencian regional tax law),
  labora.gva.es
- Catastro (sede.catastro.gob.es)
- HMRC / gov.uk for UK-side claims. Service-public.fr / impots.gouv.fr for France-side claims (FR
  posts on double taxation). For RU readers, Spanish official sources only unless Mike approves more.
- PwC, Deloitte and KPMG reports for comparative/market claims only. idealista.com and fotocasa.es
  for property-market data only, never for legal claims.

## Forbidden sources

garrigues.com, jacheteenespagne.com, any real-estate agency, and any competing law firm or
legal-service provider anywhere. Existing links to them are removed (keep the claim and re-source it).

## Known landmines

- **Golden Visa**: abolished, last applications 3 April 2025 (Ley Orgánica 1/2025). Never present
  it as available.
- **RU terminology**: "residencia no lucrativa" = «вид на жительство без права на работу». The
  machine-translation calque «ненасыщенный вид на жительство» is wrong every time it appears.
  Correct it, don't just flag it.
- **"65 years"**: replace with "since 1960".
- **Beckham Law, Modelo 720/721, IRPF brackets, Valencian inheritance tax relief, SMI, IPREM,
  autónomo quotas**: values change yearly. Always check them against the current year.
- **Short-term rental rules** (EU regulation 2024/1028, the Spanish single registry since
  1 July 2025, Valencian decree on tourist housing) change often. Date every statement.

## Process per post

1. **Extract** every checkable claim into the post's audit record (`data/factcheck/<id>.csv`:
   claim, location in the post, current wording, locale).
2. **Verify** each claim with `fact_check` (AISA), then open the official source it cites and
   confirm that the source says the same thing for the right year. A Perplexity verdict on its own
   isn't enough.
3. **Verdict per claim**: `OK` (keep, add a citation if missing) · `UPDATE` (correct value plus
   source) · `OUTDATED` (true at the time, now superseded, so rewrite it with a date) · `UNVERIFIABLE`
   (escalate to Mike/the firm, never soften it into a vague statement) · `WRONG` (fix it in every
   locale that carries the claim).
4. **Propagate**: look up the post's `trid` translations and check the same claim in every locale.
   A fix in ES and not in FR is a defect.
5. **Cite inline**: link the official source directly on descriptive anchor text in the sentence
   that makes the claim (`rel="nofollow noopener" target="_blank"`). No numbered markers, no
   reference list at the bottom (Mike, 2026-10-01).
6. **Legal judgement calls** (an interpretation, a new regime, a contested ruling) go to Félix/Sonia
   through Mike. The agent does not decide them. In the post, state only what the source says and
   add a call to action to contact the firm for confirmation (Mike, 2026-10-01). Never guess.

## Output

One row per claim in `data/factcheck/<id>.csv` with columns
`post_id, lang, claim, verdict, correct_value, source_url, checked_on, propagated_to`.
