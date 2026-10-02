# 8615 (FR) Déclarer ses cryptomonnaies en Espagne: post_content rewrite cleanup, 2026-10-02

- URL: https://delaguialuzon.com/fr/blog/declarer-crypto-en-espagne/ (unchanged, short, keyword-based)
- Focus keyword: "déclarer crypto en espagne". Title tag 50 chars, description 149 chars: OK, not changed.
- Scope: individuals (IRPF, Modelo 721, sanctions, residence). Business side lives in 11817.

## Version decision
The May 2026 `<!-- wp:html -->` rewrite in `post_content` is kept as the base: it is newer and far more complete than
the Elementor version (last edited 2026-02-02, still says "2025", 26 % top rate, 20 000 € / 15 % sanctions). One
Elementor fact the rewrite lacked was carried over after checking: delito fiscal above 120 000 € (art. 305 CP).
`_elementor_data` and `_elementor_edit_mode` were NOT touched: the live page still shows the old version until the
orchestrator removes `_elementor_edit_mode`.

## Changes
- TL;DR box: `<p>` title replaced by H2 "Déclarer ses cryptomonnaies en Espagne : les points essentiels", 7 quotable bullets.
- H3 hook, intro, 8 content H2s in noun form, CTA before FAQ, FAQ as 10 H3 (count unchanged, D-2 open).
- Removed: emojis, "Delaguía &amp; Luzón", "65 ans", offices list (Madrid, Barcelone, Alicante, Castellón, ...), office
  hours (unverified), two fabricated Spanish "quotes", generic source footers. Sources now inline on descriptive anchors.
- Disguised lists (2-column flex boxes, calendar paragraph) turned into real lists; 5-step method as `<ol>`.
- Corrected facts: see `data/factcheck/8615.csv` (19 rows).
- Internal links (FR, 200, no redirect): 11817, 2678 (Modelo 720), 4580 (IRPF), 4812 (CJEU ruling), 2297 (contrôle
  fiscal), 25839 (convention), 27325 (calendrier), /fr/droit-fiscal-et-comptabilite/. No self-link.
- Inbound links already exist from 2505 and 25839 (live), plus 11817 after the switch. None added.

## Result
- post_content MD5 `5b6dcadba66d2a22ddd95cc3db904cf8` (= staged `8615-rewrite.html`), post_modified 2026-10-02 13:10:34.
- Rollback: revision 25585 (pre-edit content, MD5 12c97502...).

## Open points
- Mining for individuals: no DGT IRPF ruling found; text states only V3625-16 (VAT/IAE) and sends to the CTA. Félix/Sonia
  may want to state the IRPF treatment.
- DAC8 transposition and the draft Modelo 175 order: re-check BOE before/after the switch; text is dated "au 2 octobre 2026".
- Art. 199 LGT amounts for incorrect 721 filings not stated (only referenced).
- RU sibling 9220 not reviewed (RU on hold).
