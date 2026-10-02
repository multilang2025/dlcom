# 9220 (RU) Декларация криптовалюты в Испании: RU pass, 2026-10-02

- URL (unchanged): /ru/blog/декларировать-криптовалюту-в-испани/ · trid 1330, source FR 8615 (switched to post_content today).
- Body: `_elementor_data`, one container (c71be53) + one text-editor (15a82f7); ids kept, saved with `elementor/save-page`.
- Exact stored HTML: `data/staging/9220-ru-pass.html` (editor MD5 f4820360a694957819889d4e82c8f24c). Rollback: revision 24488.
- H1 changed: «Криптовалюта в Испании: новости рынка и регулирование 2026» -> «Декларация криптовалюты в Испании: налоги и Modelo 721 в 2026 году» (focus keyword in H1; the post was never market news). Slug unchanged.
- Rank Math: title 54, description 143 (both rewritten; the old description had the typo «криптовавалюту»).

## What changed
- Freshness: savings rates 19-26 % -> 19/21/23/27/30 % (Ley 7/2024); Modelo 720 -> 721 for crypto abroad; sanction «20 000 евро или 15 %» -> art. 198 LGT (20 €/item, 300 to 20 000 €); added FIFO and permuta (AEAT manual), art. 49 losses, art. 191 and 305; DAC8 dated and pending transposition; MiCA transition ended 1 July 2026. Mining-as-autónomo claim removed -> CTA.
- Naturalness: written natively (old text: «Нам грустно сообщать Вам эту новость», «Эта обеспечивает», «включая биткоинов», «Hacienda (Казначейства)»).
- Format: TL;DR H2 + 7 bullets, H3 hook, sentence-case H2s, rate table, lists, inline sources, CTA box. 0 dashes kept. No FAQ in body (none before).
- Links: RU only, all 200 and no redirect: 11848, 10376, /ru/налоговое-право-и-бухгалтерский-учет/, /ru/контакты/. Inbound from 11848 and 10376 (same pass). Related posts block: RU only.

## Open points
- **WPML copies `_elementor_edit_mode` from FR 8615** (empty since the switch). Every save of 9220 (or of 8615) flips 9220 to post_content rendering. Restored to `builder` twice with `post meta update --force`. post_content now holds Elementor's mirror of the new text, so a flip would show the new text without the TL;DR box styling. Mike: WPML custom-field setting for `_elementor_edit_mode` (copy -> don't translate/ignore) before more switches.
- Rank Math schema (not output while the rich-snippet module is off): FAQPage carries wrong facts («20 000 € или 15 %», 721 «среднее значение в последнем квартале», mining as autónomo, Beckham/721 claim), Article headline «Новости рынка…», author «Delaguía & Luzón Abogados», Logo-65 image. Fix when T-02 is resolved.
- Staking (V1766-22) and airdrop (V0648-24) rulings are cited by number without a link: petete ruling text can't be opened by automation; facts from the FR 8615 check.
- DAC8 transposition: re-check BOE (TASKS).
