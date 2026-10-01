# Style guide: cross-locale master rules for blog posts

Applies to ES, EN, FR and RU blog posts unless a locale file overrides a rule. Source: dlvibe
`docs/03-STYLE-GUIDE-MASTER.md` plus Mike's rules of 2026-09-15, 09-23, 09-24, adapted to
WordPress posts. Rules marked **(open)** have a conflict logged in `DECISIONS.md`.

## Firm identity

- Brand in running text: **Delaguía y Luzón** ("De la Guía Luzón Abogados" as the legal name).
  Never `&`, `&amp;` or "Delaguía & Luzón", including in schema and image alt text.
- Founded 1960: write "since 1960" / "desde 1960" / "depuis 1960" / «с 1960 года». **Never a year
  count** ("65 years", "65 años", "65 ans d'expérience").
- Team of 25. One office: Avinguda Regne de Valencia, 6, 1º-2º, 46005 Valencia. The Mulhouse office
  is retired, so remove any mention of it.
- Phone +34 963 74 16 57. Emails felix.delaguia@delaguialuzon.com,
  sonia.gomezluzon@delaguialuzon.com (`.com`, never `.fr`).
- Languages served: French, Spanish, English, Russian, German, Arabic (each locale lists its own
  language first).

## Banned everywhere

- Emojis, in body, title tag and meta description (the ES title tags carry ⚖️ today).
- Em dashes and en dashes (`—` `–`). Use a comma, colon, parentheses, full stop or hyphen. A run
  of "label – description" lines is a disguised list, so make it a real list.
- "By + gerund" openings ("By understanding…").
- Meta-textual openers: "Découvrez", "Descubre/Descubra", "Discover", "Ce guide", "This guide",
  "Cet article explique", "Chez Delaguía y Luzón".
- Filler framing: "il est important de", "es importante", "it is important to", "dans le cadre de".
- "Conclusion" (or "Conclusión", «Заключение») as a heading.
- **Any free-consultation claim**, in any locale ("consultation gratuite", "consulta gratuita",
  "sin coste", "free consultation", «бесплатная консультация»). The firm is moving to a paid first
  consultation.
- Golden Visa as an available route. Spain stopped granting it on 3 April 2025. Historical mentions
  are fine if dated.
- Vague marketing and academic padding. AI tells: "navigating the complexities", "in today's
  ever-changing landscape", "a myriad of", "delve", "robust", "seamless", "unlock".

## Titles, H1 and headings

- One H1 per page (the template prints the post title as H1, so the body must have no H1).
- The H1 contains the focus keyword. Sentence case in every locale (EN included), never all caps
  and never `text-transform: uppercase`.
- Title-tag separator is a colon, never a pipe.
- No numbered headings ("1) …"), no "The importance of …".
- H2s reinforce the H1's core topic. H3 for subtopics, H4 for definitions and detail.
- FR: noun form in headings ("Obtention du NIE", not "Obtenir le NIE"). If the focus keyword is a
  verb phrase, flag it to Mike.

## Structure of a long-form post

1. **TL;DR summary box first** (Mike, 2026-10-01: "section résumée en début d'article pour
   l'indexation par l'IA"), before any intro prose: an H2 in sentence case containing the primary
   keyword ("<keyword> : les points essentiels" / "<keyword>: key points" / "<keyword>: lo
   esencial"), then 4 to 7 bullets. Each bullet is one complete, self-contained factual sentence
   (amount, deadline, condition, who it applies to) that an AI answer engine can quote on its own,
   with no "see below" or pronouns that need the article. Style: inline
   `background:#f5f5f5;border-left:4px solid #007BB3;padding:20px 24px;border-radius:8px`.
   FR: "Les points essentiels" must be an `<h2>`, never a `<p>`.
2. An H3 hook, then the intro (2 or 3 short paragraphs).
3. 6 to 10 H2 sections. Paragraphs of 3 or 4 sentences, one idea each. No walls of text.
4. At least 2 bullet lists and, where the topic has numbers (rates, deadlines, regions), one
   comparison table.
5. Step-by-step sequences for procedures (numbered list).
6. Sourced blockquotes from named institutions (BOE, AEAT, Seguridad Social…), spread through the
   article. Target 4 on pillar posts (2,000+ words) and 2 on shorter posts.
7. **CTA before the FAQ**: one H2, phone and email, formal register, no free-consultation wording.
8. **FAQ (open)**: questions as H3 headings, no `<details>`, mirrored 1:1 in FAQPage schema. The
   count is not settled: 8 to 10 (WordPress-era blog rule) or exactly 5 (Mike, 2026-09-24, rebuild).
   Until it is decided, do not add or remove FAQ items just to hit a count.
9. **No reference list at the bottom** (Mike, 2026-10-01). Sources are embedded where the claim is
   made, as descriptive anchor text: "le [Real Decreto 126/2026 publié au BOE](https://www.boe.es/…)
   fixe…", never "[1]" and never "cliquez ici". See "Citations format" below.
10. **Unsure claims → CTA, not a guess** (Mike, 2026-10-01). When the law or its application is
    unclear (e.g. what silence means after a deadline, which appeal applies), do not state it. Say
    only what the official source says, then add a short call to action inviting the reader to
    contact the firm for confirmation of their own case (phone + email).

**Markup hygiene.** Never paste a standalone HTML page into a post: no `<html>`, `<head>`, `<body>`,
and no `<style>` blocks with global selectors (`*`, `body`, `h2`, `p`, `a`, `ul`, `ol`, `table`).
WordPress adds `<p>` tags inside them, which breaks the CSS and leaks resets onto the whole page
(found on 26678 and 27692: lists lost their indentation, header and footer restyled). Use inline
styles on the block itself or the theme's styles.

Word count: 2,000+ for pillar posts (one per topic cluster per locale). Supporting posts are as
long as the question needs. Don't pad.

## Freshness

- Year in the title/H1 only when the content is genuinely year-specific (tax year, rates). Then the
  whole post must be current for that year: figures, examples, "this year" statements.
- **Slugs never contain a year** (`/impuesto-sucesiones-2024/` is a defect, but don't fix it
  without a redirect and approval).
- Expired deadlines: a post about a deadline that has passed (e.g. the regularisation deadline of
  30 June 2026) says so in its first paragraph and summary box.

## Linking

- Internal links: same tab, same locale only (never link an FR post to an ES URL), never to the post
  itself. Vary the anchor text, so the same target never gets the same exact-match anchor twice.
- 3 to 8 contextual internal links per long-form post, including at least one to the relevant
  practice-area page in the same locale and one to a sibling post in the same cluster.
- External links: new tab, `rel="nofollow noopener"`, only to sources approved in
  `03-FACT-CHECKING-PROTOCOL.md`. Never link to competing law firms, legal-service providers or
  real-estate agencies.
- **Related posts block** (Link Whisper, bottom of each post): all 6 must be in the post's own
  language and on a related topic. Audit with the related-posts check in `06-AUDIT-PROCESS.md`;
  a post showing another language needs a Link Whisper re-scan (wp-admin), not a content edit.
- **Maillage interne:** when working a post, also add links *to* it from 2 or 3 relevant posts in
  the same locale (inbound), not only links out of it.
- Full method: `08-INTERNAL-LINKING.md`.

## URLs

- Short slug built from the focus keyword, no stop-word padding, no year, no `-2` suffix:
  `/fr/blog/s-installer-en-espagne/`, not `/fr/blog/sinstaller-en-espagne-depuis-letranger-les-demarches-des-90-premiers-jours/`.
- The URL is set in **Permalink Manager** (`permalink-manager-uris`), not by the WordPress slug.
- Every URL change gets a 301 in Rank Math redirections, verified with `curl -I`, and internal links
  pointing to the old URL are updated to the new one (no redirect hops).
- A `-2` slug means a duplicate or an old draft holding the clean slug: check before publishing.

## Meta

- Title tag ≤ 60 characters after `%currentyear%` resolves. Keyword first, colon, angle. No emoji,
  no pipe, no brand suffix if it pushes past 60.
- Meta description ≤ 155 characters (FR's tighter number applied everywhere). Lead with the most
  useful fact, end with an action. No emoji.
- Excerpt ≤ 255 characters, two sentences.

## Images

- Every content image has alt text written natively in the post's language, about the topic. Never
  translated from another locale, never empty (purely decorative images: `alt=""` plus a reason).
- WebP preferred. Check whether Imagify already serves WebP before re-uploading anything.
- File names in the post's language. Don't rename existing media (it breaks other references).
- **Featured images must look real** (Mike, 2026-10-01, on 26678). Prefer real photos. A
  generated image is allowed only if it is documentary-style: natural light, realistic people, and
  no readable text, logos, insurer or bank brands, or made-up landmark mashups (e.g. the City of
  Arts and Sciences next to the old-town towers by the sea). Replace any image that looks fake.
  Upload with a French/Spanish/English title (it becomes the file name) and native alt text.

## Citations format

**Inline anchor links only** (Mike, 2026-10-01, replaces the old numbered `[1]` + reference list
rule). Every specific figure, rate, threshold, form number or deadline links to its official source
right where it is stated. The anchor text names the source and what it says: "[Real Decreto 126/2026
(BOE-A-2026-3815)](https://www.boe.es/…)", "[the AEAT guide to Modelo 720](https://sede.agenciatributaria.gob.es/…)".
External source links: `target="_blank" rel="nofollow noopener"`. No "Références" / "References"
section at the bottom. When editing an older post that has one, move each source into the sentence
it supports, then delete the list.
