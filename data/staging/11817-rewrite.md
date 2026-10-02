# 11817 (FR) Cryptomonnaies et entreprises en Espagne: post_content rewrite cleanup, 2026-10-02

- URL: https://delaguialuzon.com/fr/blog/cryptomonnaies-et-entreprises-en-espagne/ (unchanged; a shorter slug such as
  `crypto-entreprises-espagne` is possible but needs Mike's approval + 301, not done)
- Focus keyword: "Cryptomonnaies et entreprises en Espagne". Title tag 54 chars OK. Description was 157 chars and off-topic:
  replaced (150 chars) via `/rankmath/v1/updateMeta`.

## Version decision
The rewrite in `post_content` (newer, 2026) is the base; the Elementor version is a short 2024-era text (SL capital 1 €,
"Conclusion" H2) with nothing the rewrite lacked. `_elementor_data` / `_elementor_edit_mode` untouched.

## Cannibalisation with 8615
- 11817 now covers companies only: IS rates, ICAC accounting, VAT (payments, exchange, mining), Modelo 721 for legal
  entities (exemption when crypto is recorded individually), 172/173 from the company side, capital contributions, MiCA.
- Individual IRPF rates, staking, FIFO, 721 sanctions, residence and treaty were removed or reduced to a link to 8615.
- Residual overlap (acceptable, different angle): both mention Modelo 721, Modelos 172/173 and DAC8.

## Changes
- TL;DR H2 "Cryptomonnaies et entreprises en Espagne : les points essentiels" + 7 bullets; FAQ H4 -> 9 H3 (was 10; the
  removed one duplicated the 721 sanctions FAQ that now lives in 8615).
- Removed: emojis, "&" brand, "65 ans", offices list incl. Madrid/Barcelone, hours, unverifiable statistics (Banco de
  España, 721 campaign, CNMV application counts), named exchanges, English quotes (Hedqvist, MiCA art. 59).
- Corrected facts: see `data/factcheck/11817.csv` (24 rows).
- Internal links: 8615, 3496 (/impot-societes-espagne/), 8402, 1691 (/creer-une-entreprise-en-espagne/), 2362,
  /fr/droit-fiscal-et-comptabilite/. All 200, no redirect.
- Inbound after the switch: 2505, 8615, 8402. Note: 12930 links to 11817 only in its Elementor version; its rewrite
  (also queued for the switch) has no such link.

## Result
- post_content MD5 `bc92849fcf14d678e33e074665b010cf`, post_modified 2026-10-02 13:12:10. The revision (28023) matches the
  staged file (`cccbd30c...`); a save filter then re-quoted the 3 CTA page links (`href='...'` -> `href="..."`). No other
  difference.
- Rollback: revision 27492.

## Open points (Félix/Sonia)
- "Une société qui se limite à recevoir des paiements ou à placer sa trésorerie n'est pas un prestataire de services sur
  crypto-actifs": reasonable reading of MiCA's CASP definition, worth a partner check.
- Intangible measurement "au coût et dépréciation" comes from general PGC rules, not from the ICAC consulta itself.
- Siblings ES 11788, EN 11830, RU 11848 not fact-checked (SQL spot check found none of the wrong figures).
