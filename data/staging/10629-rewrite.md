# FR 10629: decret-logements-touristiques-communaute-valencienne (rewrite cleanup, 2026-10-02)

Mike "go" 2026-10-02. Same plan as FR 13243: post_content is cleaned now, and the orchestrator removes
`_elementor_edit_mode` for the 11 posts after Mike approves. `_elementor_data` and `_elementor_edit_mode`
were not touched.

## Version decision

The **2026 rewrite (post_content) is kept** as the base. It was modified on 2026-05-11, and the old
Elementor body (7 KB, Nov 2025) is a 2024 news piece with "Delaguía&Luzón", a "Chez" opener and a
speculative "possible TVA 10 % → 21 %" line. The rewrite needed a substantial fact rework (see
`data/factcheck/10629.csv`) because the law changed after 2026-05-11:

- the Tribunal Supremo annulled the RD 1312/2024 registry on 19 May 2026;
- Regulation (EU) 2024/1028 has applied since 20 May 2026;
- Ley 3/2026 (in force 3 July 2026) amended Decreto 10/2021;
- RDL 26/2026 (BOE 30 September 2026) changes VAT from 1 December 2026.

## State

- post_content MD5 3ad4395e → **e30f4974c3d2ea46a1c1712ca56b72e0** (30 598 bytes). post_modified
  **2026-10-02 13:05:50**. Final HTML: `data/staging/10629.html`.
- post_excerpt replaced (the old one was factually wrong and is live on archive cards).
- Rank Math title (48 chars) and description (149 chars) were checked and left as they are: within
  limits and not contradicting the rewrite. Focus keyword: "logements touristiques à Valencia".
- Live: 200. The old Elementor body still renders, as expected until the switch.

## Changes

- TL;DR first: H2 "Logements touristiques à Valencia : les points essentiels", with 7 self-contained bullets.
- Removed: emojis, "Delaguía &amp; Luzón", "65 ans", the offices list (Madrid, Barcelone, Alicante,
  Castellón, Torrevieja, Betera, La Eliana, Calpe, Peñíscola), opening hours, the unsourced statistics box,
  the unverifiable before/after table, the tax table, unsourced timelines, and the 48-hour removal claim.
- New structure: 11 H2 sections in noun form, a 3-level comparison table, a sanctions table, a numbered
  procedure, 2 sourced blockquotes (verbatim art. 65.1 and the BOE annulment note), CTA before the FAQ,
  and an FAQ of 10 H3 questions (the count is unchanged, per D-2).
- Sources are inline on descriptive anchors (target=_blank rel="nofollow noopener"). There is no
  reference list.
- Internal links are FR only and all return 200: /fr/droit-immobilier/, /fr/contact/,
  /fr/cabinet-international-avocats/, /fr/droit-fiscal-et-comptabilite/, and the blog posts
  audit-immobilier-en-espagne, logements-touristiques-en-espagne (13762), locations-courte-duree-espagne
  (15720), tva-sur-les-locations-touristiques-en-espagne (15895) and hebergements-touristiques-valence (24989).
- Inbound links already exist from 1130, 2823, 13762, 15895, 15720 and 24989, so none were added.
- French typography: non-breaking spaces before : ; ? ! and inside « », and in amounts.

## Cannibalisation check with 24989

24989 covers the **City of Valencia's 2026 municipal zoning** (saturation indicators, 8 % threshold).
10629 covers the **regional, national and EU framework**. They do not overlap in intent. 10629 now
sends readers to 24989 for the city rules, and 24989 already links to 10629. Focus keywords differ
("Hébergements touristiques" vs "logements touristiques à Valencia").

## Open points

1. **For Félix/Sonia (legal):**
   - What happens to national NRUA numbers already issued and to the annual return under Orden
     VAU/1560/2025 after the STS of 19 May 2026 (its basis, art. 10.4, was annulled). The post states
     only that it is unresolved and adds a CTA.
   - Scope of LPH DA 2ª for flats already operating before 3 April 2025.
   - Effect of RDL 26/2026 if Congress validates it (VAT at 10 % for stays of 30 nights or less from
     1 December 2026, IBI surcharge). Its validation is due within 30 days of 29 September 2026.
     **Re-check this post after the vote.**
2. **City of Valencia:** final approval of the municipal VUT rules (Pleno, 31 March 2026) is confirmed
   only by the press. The official valencia.es page found documents the January 2025 draft. The post
   avoids dates and thresholds and links to 24989.
3. **24989 (not edited, flag for Mike):**
   - Its Rank Math canonical (`/fr/blog/nouvelles-regles-hebergements-touristiques-valence-2026/`)
     returns **404** (D-9).
   - The body has "Delaguía & Luzón", "depuis 1994", em dashes, numbered H2s, emojis and a "Ce guide" opener.
4. **15720** still uses [n] markers and a Références list (old citation format).
5. **Title (H1)** "Logements touristiques Communauté Valencienne 2026 : Décret 9/2024, NRA et règlement UE"
   still says "NRA". Suggest: "Logements touristiques à Valencia en 2026 : Décret-loi 9/2024, copropriété
   et règlement UE". That needs Mike's decision; the title was not changed.
6. **Siblings:** ES 10615 (Elena) and EN 10659 (Mike/Maral) are the short 2024 versions. They likely
   still carry the "IVA 10 % → 21 %" speculation, which now needs the RDL 26/2026 wording. EN has an
   ampersand brand. The fact fixes were not propagated (other owners).
7. AISA `fact_check` was unavailable (no OpenRouter key), so every claim was checked directly against
   boe.es / EUR-Lex / AEAT.

## QA gate

| Check | Result |
|---|---|
| Scope | post only |
| Re-read before write | yes, unchanged |
| Banned phrases, dashes, emojis | 0 |
| Brand / since 1960 / one office | ok |
| TL;DR first | ok |
| CTA before FAQ | ok |
| FAQ as H3 | ok (schema mirroring is not in scope here) |
| Inline sources, no list | ok |
| Same-locale links, 200 | ok |
| No `<html>`/`<style>` | ok |
| Unverifiable claims | removed or turned into a CTA |
| Verified by SQL + purge + live | yes |
| Ready for the `_elementor_edit_mode` switch | yes |
