# E-E-A-T standard for the blog

New for the legacy WordPress blog. dlvibe has no equivalent doc, only the "author photo of Félix"
item in its `16-FLAGGED-FOR-LATER.md`. Legal and tax content is YMYL, so Google and AI answer
engines weight who wrote it, who checked it, and when.

## State on 2026-10-01 (sample of 3 posts, EN/FR/ES, confirmed site-wide by `data/audit_baseline.csv`)

- No visible author name, author box, reviewer or bar membership on posts.
- No visible publish/updated date.
- EN `BlogPosting` schema exists, but `author` is the Organization and there is no
  `datePublished`/`dateModified`. FR/RU posts output only `LegalService` (no Article at all).
- WordPress authors are "Michael", "Maral", "Elena", "cari": marketing accounts, not the lawyers.

## Target per post

| Signal | Visible on page | In schema |
|---|---|---|
| Author | Named lawyer or economist with role: "Félix Delaguía, abogado, socio" | `BlogPosting.author` = `Person` with `name`, `jobTitle`, `url` (author page), `sameAs` (Colegio de Abogados listing, LinkedIn) |
| Legal review | "Revisado por Sonia Gómez Luzón, abogada, el 12/10/2026" | `reviewedBy` on `WebPage` + `lastReviewed` |
| Dates | "Publicado … · Actualizado …" under the H1 | `datePublished`, `dateModified` (true update date, not a bump) |
| Publisher | footer already carries it | `publisher` = `LegalService`/`Organization` "Delaguía y Luzón" with logo, address, phone |
| Experience | at least one first-hand element: a case pattern the firm sees ("en el despacho vemos con frecuencia…"), a worked example with real numbers, a procedural tip only a practitioner would know | n/a |
| Sources | numbered references to official sources | `citation` (optional) |

## Who signs what (to be confirmed by Félix/Sonia, see `DECISIONS.md` D-3)

Proposal: tax, accounting and inheritance by the economist/tax partner; immigration, labour, property
and corporate by the lawyer partners. Every author needs an author page in each locale (bio,
qualifications, colegiado number, photo, languages) before their name goes on posts.

## How it gets built (split by Scope Gate)

- **Template (Mike / wp-admin)**: add the Elementor author-box and the post-info date items to
  single-post template 4476. Re-enable the Rank Math rich-snippet module (after updating Rank Math
  Pro), set the default Article type to `BlogPosting` and author to the post author.
- **Users (Mike)**: create or rename WordPress users for the real authors, fill bio, avatar and
  social profiles, then reassign posts.
- **Per post (agents)**: experience paragraph, reviewer line, sources, updated date only when the
  content really changed.

## Audit questions per post (score 0 to 2 each, 10 max)

1. Is the author a qualified, named professional, visible and in schema?
2. Is there a review line and date?
3. Does the post show first-hand experience (case pattern, worked example, practitioner tip)?
4. Are all checkable claims cited to approved official sources?
5. Is it current: no expired deadlines presented as open, no outdated figures?
