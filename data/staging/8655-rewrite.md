# 8655 (FR) travailler-en-espagne-en-tant-que-francais: post_content cleanup for the rendering switch

- URL: https://delaguialuzon.com/fr/blog/travailler-en-espagne-en-tant-que-francais/ (200; no WPML siblings, trid 1336)
- Before: post_modified 2026-09-12 11:55:17, post_content MD5 d39cb2a7db21e5bf3e4c2fb1d1b0aee6 (44 627 bytes), `_elementor_data` MD5 5c6a21bab635c80fbed26fcd7eff109a (48 496 bytes), mode builder.
- After (2026-10-02): post_modified 2026-10-02 13:14:31, post_content MD5 **e97beeb92aeebf27b949c504f14ecccc** (44 324 bytes, identical to `8655-post_content.html`). `_elementor_data` and `_elementor_edit_mode` untouched (MD5 re-checked). Written with `PUT /wp/v2/posts/8655` (content only). No HTTP 500 this time.

## Version decision

**post_content is the newer version.** Both versions have the same 12 H2 / 10 FAQ outline. A section-by-section text diff shows that post_content is the Elementor text with dashes removed, disguised lists split, two sentences added (private health insurance link, Beckham audit link) and the stat boxes renamed. Elementor had no newer facts. It only held three link changes, which were ported:
- SMI link updated on 2026-10-01 to `/fr/blog/smi-espagne/` (post_content still pointed at the 301 URL);
- NIE guide link (`/fr/blog/pourquoi-comment-obtenir-nie-espagne/`, was wrapped around "NIE" inside an H2, so it was moved into body text);
- IRPF guide link (`/fr/blog/impots-sur-le-revenu-en-espagne/`, was wrapped around "IRPF" inside "LIRPF", now on a descriptive anchor).

## Changes

- TL;DR: was a `<p>` titled "l'essentiel en 60 secondes" with an emoji. It is now an H2, "Travailler en Espagne en 2026 : les points essentiels", in the house style (#f5f5f5, #007BB3 border), with 7 self-contained bullets.
- H3 hook and an intro rewritten, plus a link to `/fr/blog/s-installer-en-espagne/`.
- Headings put in noun form ("Statut de salarié…", "Statut d'autónomo…", "Secteurs où…", "Durée du travail…").
- All emojis removed: flags, 📌📊❓💰🎯🔄📍📞📧🕑🌐👉📖.
- CTA moved before the FAQ, with a new H2 "Accompagnement juridique de votre projet professionnel en Espagne". In the CTA: "Depuis 1960", "Delaguía y Luzón", one office (Valencia), and hours checked against /fr/contact/. The office list (Madrid · Barcelone · Alicante · …) and "Siège" were removed.
- FAQ: the 10 questions were kept and moved from H4 to H3, with the answers corrected.
- Removed unsourced blocks: the French-community stats box, the average-salary box, the purchasing-power claims, the foreign minimum and average wages, and the sector salary bands, the 21 % figure and the company names.
- Sources: generic "Sources :" lines (boe.es and sepe.es homepages) were replaced by inline links on descriptive anchors (BOE, EUR-Lex, AEAT, CGPJ, Congreso, La Moncloa, Service-Public, Légifrance, Commission). All external links have target=_blank rel="nofollow noopener".
- Two disguised lists turned into real lists (autónomo pitfalls, Ley 10/2021 obligations).
- French typography: non-breaking spaces before : ; ? ! and inside « », and in amounts.
- Internal links: 19, all /fr/, all HTTP 200, no self-link, no redirect.
- Rank Math: %currentyear% replaced by 2026 in the title (49 chars) and the description (146 chars).

## Fact-check summary (data/factcheck/8655.csv, 56 rows: 14 OK, 25 corrected (9 WRONG, 12 UPDATE, 4 OUTDATED), 17 UNVERIFIABLE removed or CTA)

- Corrected (WRONG / UPDATE / OUTDATED), among others:
  - Swiss nationals get a TIE (wrong: RD 240/2007 DA 3a gives them the certificado de registro);
  - "40 jours/an avant 2012" (wrong: 45 days);
  - a 12-day indemnity on the substitution contract (wrong: none, art. 49.1.c ET);
  - "arrêt 1250/2024" (wrong ruling: replaced by the 2025 Supremo plenary note from the CGPJ);
  - RDL 16/2025 freezing autónomo quotas (it was not validated, so RDL 3/2026 and Orden PJC/297/2026 now apply);
  - quotas of 200 to 590 € (now 205,88 to 607,35 € for 2026);
  - employer and employee rates (now 30,65 % and 6,50 %);
  - French SMIC 1 823,03 € (now 1 867,02 €);
  - 37,5 h bill "blocked in April 2026" (it was returned to the Government on 10/09/2025);
  - nomad visa "up to 5 years" (now 1 + 3 + 2-year renewals);
  - renewal "60 jours" (now two months, art. 80);
  - quotes of art. 73.5 RD 1155/2024 and art. 11.1 LETA made literal;
  - "article 71" removed;
  - the INAMI and Cleiss attributions removed;
  - the pluriactividad 50 % first-year cut replaced by the verified 2026 refund rule.
- Removed or turned into a CTA (UNVERIFIABLE): tarifa plana amount for 2026, regional cuota cero list, telework permanent-establishment threshold, Beckham eligibility details, 2042-NR details, the ECOVUL programme, treaty dates for Belgium and Switzerland, and the 1957 social security convention.

## Open points

1. **Tarifa plana 2026 amount (Félix/Sonia).** Art. 38 ter LETA leaves the amount to the budget law. Seguridad Social only confirms 80 € for 2023 to 2025, there is no 2026 budget law, and RDL 3/2026 says nothing. The post now gives the rule and a CTA. Can the partners confirm the amount being applied in 2026?
2. **Rank Math schema of 8655 (do at switch time).** The custom schemas carry wrong data:
   - `rank_math_schema_LegalService`: "Delaguía &amp; Luzón" and `founder: "Cabinet fondé il y a 65 ans"`;
   - `rank_math_schema_Article`: "&amp;" in author and publisher, and a description that mentions the 1957 convention;
   - `rank_math_schema_FAQPage`: mirrors the OLD FAQ, including the wrong 200 to 590 €, "TIE régime UE", ECOVUL and "1 826 h".

   The replacement FAQPage (10 Q/A mirroring the new FAQ) is ready in `data/staging/8655-faq-schema.json`. It was not applied, because the live page still renders the old Elementor FAQ. Fix the brand and "65 ans" in all three schemas when the switch happens.
3. FR typography: the phone number reads "+34 963 74 16 57" with a non-breaking space after +34 (side effect of the typography pass, harmless).
4. The H1 and focus keyword "travailler en Espagne" are a verb phrase (FR noun-form rule): flag for Mike, not changed.
5. Inbound links: 8655 already gets links from 14 FR posts. None added.

**Ready for the rendering switch: yes**, after Mike's approval. Apply the FAQ schema in the same step.
