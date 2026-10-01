# Regularisation posts (trid 2491): fact-check and staged fixes

Staged 2026-10-01, read-only. Nothing has been written to WordPress. Posts: FR 21471, EN 21452, ES 21398, RU 23581. Raw `post_content` read via `GET /wp/v2/posts/<id>?context=edit`; local copies verified byte-identical to the DB (`MD5(post_content)`). Every `old` snippet below occurs exactly once in the current `post_content`, and the changes were applied in order to a local copy (each still unique at its turn) to confirm they compose. Apply in the listed order with `POST /wpvibe/v1/content/edit` `{"target_type":"post","post_id":ID,"field":"post_content","old_content":…,"new_content":…}`. Before applying, re-check `MD5(post_content)` against the value given per post; if it differs, re-stage.

Fact-check CSVs: `data/factcheck/21471.csv`, `21452.csv`, `21398.csv`, `23581.csv`.

## Legal facts (verified 2026-10-01)

| Topic | Fact | Source |
|---|---|---|
| Instrument | Real Decreto 316/2026, de 14 de abril, modifying the Reglamento de Extranjería approved by RD 1155/2024. BOE núm. 92, 15 Apr 2026, BOE-A-2026-8284; in force 16 Apr 2026 (DF 2.ª). It adds two additional provisions: DA 20.ª (international protection applicants) and DA 21.ª (arraigo extraordinario). | [BOE-A-2026-8284](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8284) |
| Window | Applications until 30 Jun 2026 (DA 20.6/21.6). Online from 16 Apr, in person by appointment from 20 Apr (Extranjería, Seguridad Social, Correos offices). Closed 30 Jun with no extension: 1,174,978 applications, 609,737 already tramitadas, 79.6% arraigo extraordinario / 20.4% protection applicants, 83.2% online. | [Moncloa 14 Apr](https://www.lamoncloa.gob.es/consejodeministros/resumenes/Paginas/2026/140426-rueda-prensa-ministros.aspx), [Moncloa 2 Jul](https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/020726-balance-regularizacion-extraordinaria.aspx) |
| Correos subsanación | Selected Correos offices kept for in-person subsanación 'hasta el 30 de septiembre' (2026). As of 1 Oct this has passed; no official extension found (the Correos convention BOE-A-2026-14221 can be extended by agreement). | [Moncloa 2 Jul](https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/020726-balance-regularizacion-extraordinaria.aspx), [BOE-A-2026-14221](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-14221) |
| Eligibility (both) | Adult; in Spain at application; presence before 1 Jan 2026 (DA 21) or protection application lodged before 1 Jan 2026 (DA 20); 5 months uninterrupted stay immediately before applying; no criminal record (art. 126.d RD 1155/2024; origin country and countries of residence in the 5 years before entry); no threat to public order/security/health; no entry ban; fee (Orden PJC/617/2025). | BOE DA 20.1, 21.1, 21.9 |
| Extra condition (DA 21 only) | At least one of: (a) past work in Spain or intention to work (job offer, or self-employment declaration); (b) living with family unit (minor children, dependent adult children, first-degree ascendants); (c) vulnerability certified by competent social services. | BOE DA 21.2; [Moncloa 21 Apr](https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/proceso-regularizacion-migratoria.aspx) |
| Status granted | Autorización de residencia temporal por circunstancias excepcionales (arraigo), 1 year, residence and work (employed and self-employed) anywhere in Spain. TIE to be requested within one month of the grant. In the 2 months before expiry: modification to other authorisations (art. 191). | BOE DA 20.7/20.10, 21.7/21.10; Moncloa 21 Apr |
| Processing / silence | Max 3 months from the day after entry in the register; silence = refusal (negative). Notice of start of processing grants provisional residence and work nationwide; refusal ends it automatically. Subsanación requests: max 15 days, else desistimiento. Foreign criminal records requested via diplomatic channels: up to 3 months suspension, then 15 days to provide the certificate or desistimiento. | BOE DA 20.3/21.4, 20.6/21.6, 20.9/21.9 |
| Protection applicants | Compatible with the pending asylum claim; if the regularisation is granted, the person must desist from the protection application or appeal (the decree does not tie this to the TIE). | BOE DA 20.4 |
| Ordinary routes now | RD 1155/2024 (in force 20 May 2025): arraigo de segunda oportunidad, sociolaboral, social, socioformativo, familiar. Two years' stay for all except arraigo familiar. | [BOE-A-2024-24099](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099) |

**Cross-locale summary.** The four posts carry the same claims and the same five references, so every fact fix applies to all four. WRONG in all four: 'RD 316/2026 added *an* additional provision' (it added two) and references [4] Civislex and [5] Martínez Caballero Abogados (forbidden sources), which back the silence, three-month and recourse claims. OUTDATED in all four: the Correos subsanación date written in the present/future tense, the excerpts (still say the process is open) and the Rank Math FAQPage schema (pre-approval 'current proposals' text that does not match the visible FAQ). RU schema is WRONG on substance (2-3 years' stay, 30-hour contract, applications from August 2026, EX-10/EX-11, 1-2 year permit). Locale differences: ES lacks most inline citations; FR has 3 contextual internal links, EN/ES/RU 1; RU CTA has no contact-page link; RU excerpt has an em dash.

## FR 21471

- URL: https://delaguialuzon.com/fr/blog/regularisation-exceptionnelle-etrangers-espagne/
- `post_modified` at read time: 2026-09-30 23:04:19; `MD5(post_content)` = `41bbe5b640dedb0fc1ed4a309360a674` (13986 bytes)
- `_elementor_edit_mode`: no `_elementor_edit_mode` row (legacy `_elementor_data` still present, `_elementor_template_type=wp-post`). Body renders from `post_content`.
- Post title (H1): Régularisation exceptionnelle en Espagne : le délai du 30 juin 2026 est clos, et maintenant ?
- Title tag: Régularisation 2026 en Espagne : délai clos, que faire ? (56); meta description: 143 chars, OK

### Fact-check (non-OK rows; full list in CSV)

| Claim | Verdict | Correct value |
|---|---|---|
| In-person subsanación at post offices 'ends' on 30 September 2026 (present tense; intro, steps list, FAQ) | OUTDATED | Date has passed as of 1 Oct 2026: 'was scheduled to run until 30 September 2026' (Moncloa: 'se alargará hasta el 30 de septiembre'); any later extension unconfirmed |
| RD 316/2026 added 'an additional provision' to the RD 1155/2024 regulation | WRONG | It added two additional provisions: DA 20 (international protection applicants) and DA 21 (arraigo extraordinario) |
| Requirement: no criminal record in Spain and, 'depending on the case', previous countries of residence | UPDATE | No criminal record (art. 126.d RD 1155/2024) incl. country of origin and countries of residence in the 5 years before entry; plus no threat to public order, public security or public health |
| Requirements list (3 bullets) presented as complete | UPDATE | Omits DA 21.2: arraigo extraordinario applicants also needed at least one of (a) past work or intention to work (job offer / self-employment declaration), (b) living with family unit (minor or dependent children, first-degree ascendants), (c) certified vulnerability |
| (omitted) Provisional right to reside and work from notice of start of processing | UPDATE | Add: admission notice grants provisional residence and work authorisation nationwide; refusal ends it automatically (DA 20.3 / DA 21.4) |
| As of 8 September 2026 favourable decisions still being notified, plus requests and pending files | UNVERIFIABLE | Only source is a competing law firm (martinezcaballeroabogados.com); remove |
| A refusal can be challenged (recurso) | UNVERIFIABLE | Generally true under administrative law but not stated in RD 316/2026; remedy type and deadline to be confirmed by Félix/Sonia; currently cited to forbidden sources |
| After favourable decision applicant must withdraw protection claim/appeal 'to obtain the TIE' | UPDATE | DA 20.4: must desist from the protection application or appeal once resolved favourably; the decree does not make this a TIE condition |
| After grant, TIE must be requested 'under the conditions set by the authorities' | UPDATE | Within one month of the grant (DA 20.7 / DA 21.7) |
| Initial authorisation has a 'limited duration' | UPDATE | One year; residence and work (employed and self-employed) anywhere in Spain; modification to other authorisations (art. 191) in the 2 months before expiry |
| No job contract was required to apply | UPDATE | True but incomplete: a work link (past work, job offer or self-employment declaration) was one of three alternative DA 21.2 conditions; not required for protection applicants |
| Source [2] CEAR (NGO legal-assistance provider, not on approved list) | UPDATE | Replace with BOE RD 316/2026 |
| Source [4] Civislex (legal-services provider: forbidden) | WRONG | Remove; replace with La Moncloa 21 Apr 2026 explainer and BOE |
| Source [5] Martínez Caballero Abogados (competing law firm: forbidden) | WRONG | Remove |
| Excerpt presents the regularisation as open/current | OUTDATED | Rewrite excerpt: closed 30 Jun 2026, no extension; in-time files processing; ordinary routes |
| Rank Math FAQPage schema: 5 pre-approval Q&As ('current proposals', 'subject to the final Royal Decree', 'dates may change') that do not mirror the 6 visible FAQs | OUTDATED | Replace schema mainEntity with the 6 visible FAQ questions/answers (see staging) |

20 further claims verified OK (figures, dates, requirements cut-off, silence rule, arraigo list).

### Style issues

- Meta-textual opener « Cet article fait le point… » (change 1).
- No summary box / « Les points essentiels » H2; expired deadline not in a summary box (change 1).
- FAQ questions are H4, master rule says H3 (change 10).
- Heading not in noun form: « Ce que vous pouvez faire à ce stade » (change 5); CTA H2 « Contactez notre équipe juridique » also verb form (not staged, see open questions).
- Forbidden sources linked: civislex.com (legal-services provider), martinezcaballeroabogados.com (law firm); CEAR not on approved list (change 11).
- French typography: no non-breaking spaces before « : ; ? ! », inside « », or in 1 174 978 (whole post; not staged as str_replace).
- 0 blockquotes (target 2); no H3 hook after the summary (not staged).
- Clean: no emoji, no em/en dash, no &/&amp; brand, no '65 ans', no free consultation, no Golden Visa, no 'Conclusion', no false office claims, single H1 (template).

### Proposed `post_content` changes (apply in order)

**1.** Summary box, dated update, expired-deadline intro (subsanación window now past), meta-textual opener removed, forbidden-source markers dropped. (count in current content: 1)

Old:
```html
<p><strong>Mise à jour du 30 septembre 2026</strong></p>

<p>Le délai de dépôt des demandes de régularisation exceptionnelle des étrangers en Espagne a pris fin le 30 juin 2026.</p>

<p>Aucune prolongation n'a été accordée. [1][4]</p>

<p>Les dossiers déposés dans les temps sont désormais en cours d'instruction, et la période de subsanation (correction des dossiers incomplets) en bureau de poste se termine le 30 septembre 2026. [1][5]</p>

<p>Cet article fait le point sur la situation actuelle, sur le traitement des dossiers déposés et sur les voies ordinaires qui restent ouvertes à ceux qui n'ont pas pu déposer de demande.</p>
```
New:
```html
<div style="background-color:#f5f5f5;padding: 24px 28px;margin: 0 0 24px 0">
<h2>Les points essentiels de la régularisation exceptionnelle</h2>
<ul>
<li>Le délai de dépôt des demandes a pris fin le 30 juin 2026, sans prolongation. [1]</li>
<li>Les dossiers déposés à temps (1 174 978 demandes) sont en cours d'instruction. [1]</li>
<li>Le délai de résolution est de trois mois et le silence de l'administration vaut rejet. [2]</li>
<li>L'autorisation accordée est valable un an et permet de résider et de travailler dans toute l'Espagne. [2]</li>
<li>Sans demande déposée, il faut passer par les voies ordinaires, notamment l'arraigo. [3]</li>
</ul>
</div>

<p><strong>Mise à jour du 1er octobre 2026</strong></p>

<p>Le délai de dépôt des demandes de régularisation exceptionnelle des étrangers en Espagne a pris fin le 30 juin 2026.</p>

<p>Aucune prolongation n'a été accordée. [1]</p>

<p>Les dossiers déposés dans les temps sont en cours d'instruction. La période de subsanation (correction des dossiers incomplets) en présentiel dans les bureaux de poste habilités était prévue jusqu'au 30 septembre 2026. [1]</p>

<p>Les personnes qui n'ont pas déposé de demande doivent désormais passer par les voies ordinaires du règlement d'immigration, en premier lieu les différentes formes d'arraigo.</p>
```

**2.** RD 316/2026 added TWO additional provisions (20th and 21st); BOE date and entry into force; in-person start 20 April; re-sourced to BOE/Moncloa. (count in current content: 1)

Old:
```html
<p>La régularisation exceptionnelle reposait sur le <strong>Real Decreto 316/2026</strong>, du 14 avril 2026, qui a introduit une disposition additionnelle dans le règlement d'immigration issu du <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">Real Decreto 1155/2024</a>. [3][4]</p>

<p>Les demandes ont pu être déposées du 16 avril au 30 juin 2026. [2]</p>
```
New:
```html
<p>La régularisation exceptionnelle reposait sur le <strong>Real Decreto 316/2026</strong>, du 14 avril 2026 (BOE du 15 avril 2026, en vigueur le 16 avril), qui a ajouté deux dispositions additionnelles (vigésima et vigesimoprimera) au règlement d'immigration approuvé par le <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="nofollow noopener">Real Decreto 1155/2024</a>. [2][3]</p>

<p>Les demandes ont pu être déposées par voie électronique du 16 avril au 30 juin 2026, et en présentiel sur rendez-vous à partir du 20 avril 2026. [2][4]</p>
```

**3.** Requirements incomplete: criminal-record scope, public-order condition and the arraigo extraordinario 'at least one of' condition (DA 21.2) were missing; protection cut-off worded as in DA 20.1. (count in current content: 1)

Old:
```html
<li><strong>Absence d'antécédents pénaux</strong>, en Espagne et, selon les cas, dans les pays de résidence antérieurs.</li>
</ul>

<p>Les demandeurs de protection internationale pouvaient également déposer une demande, sous condition d'une manifestation de volonté antérieure au 1er janvier 2026. [2][4]</p>
```
New:
```html
<li><strong>Absence d'antécédents pénaux</strong> en Espagne, dans le pays d'origine et dans les pays de résidence des cinq années précédant l'arrivée en Espagne, et absence de menace pour l'ordre public, la sécurité publique ou la santé publique.</li>
<li><strong>Pour l'arraigo extraordinaire, au moins une condition supplémentaire</strong> : avoir travaillé en Espagne ou justifier d'une intention de travailler (offre d'emploi ou déclaration d'activité indépendante), vivre en Espagne avec sa famille (enfants mineurs ou à charge, ascendants au premier degré), ou être en situation de vulnérabilité attestée par les services sociaux compétents.</li>
</ul>

<p>Les personnes qui avaient présenté une demande de protection internationale avant le 1er janvier 2026 pouvaient également déposer une demande, sans avoir à remplir cette condition supplémentaire. [2][4]</p>
```

**4.** Three-month period counted from registry entry; silence re-sourced to BOE; law-firm-sourced 8 Sept status removed; provisional right to reside and work added. (count in current content: 1)

Old:
```html
<p>Le Real Decreto 316/2026 prévoit un délai maximal de trois mois pour résoudre et notifier la demande. [4][5]</p>

<p>Le silence de l'administration au terme de ce délai vaut rejet de la demande (silence administratif négatif). [4]</p>

<p>Un dossier sans réponse après trois mois n'est donc pas une autorisation accordée.</p>

<p>À la date du 8 septembre 2026, des résolutions favorables continuaient d'être notifiées, mais aussi des demandes de complément et des dossiers encore en attente. [5]</p>
```
New:
```html
<p>Le Real Decreto 316/2026 prévoit un délai maximal de trois mois, à compter du lendemain de l'entrée de la demande au registre, pour résoudre et notifier la demande. [2]</p>

<p>Le silence de l'administration au terme de ce délai vaut rejet de la demande (silence administratif négatif). [2]</p>

<p>Un dossier sans réponse après trois mois n'est donc pas une autorisation accordée.</p>

<p>Dès la communication du début de l'instruction, la personne est autorisée à titre provisoire à résider et à travailler, comme salariée ou indépendante, dans toute l'Espagne. Un refus met fin automatiquement à cette habilitation provisoire. [2]</p>
```

**5.** Heading in noun form (FR guide); 15-day subsanación cap; 30 Sept Correos date is now past; forbidden-source markers removed. (count in current content: 1)

Old:
```html
<h3>Ce que vous pouvez faire à ce stade</h3>

<ol>
<li>Consultez l'état de votre dossier sur la sede electrónica et vérifiez vos notifications électroniques.</li>
<li>Répondez sans attendre à toute demande de subsanation, dans le délai indiqué dans la notification.</li>
<li>Si la période de subsanation en bureau de poste vous concerne, tenez compte de la date du 30 septembre 2026. [1][5]</li>
<li>Conservez l'accusé de dépôt et toutes les pièces transmises.</li>
<li>En cas de refus, demandez une analyse du dossier rapidement, car la décision peut faire l'objet d'un recours. [4][5]</li>
```
New:
```html
<h3>Démarches possibles à ce stade</h3>

<ol>
<li>Consultez l'état de votre dossier sur la sede electrónica et vérifiez vos notifications électroniques.</li>
<li>Répondez sans attendre à toute demande de subsanation, dans le délai indiqué dans la notification (15 jours au maximum). [2]</li>
<li>La subsanation en présentiel dans les bureaux de poste habilités était prévue jusqu'au 30 septembre 2026 : suivez le canal de réponse indiqué dans votre notification. [1]</li>
<li>Conservez l'accusé de dépôt et toutes les pièces transmises.</li>
<li>En cas de refus, demandez une analyse du dossier rapidement, car la décision peut faire l'objet d'un recours.</li>
```

**6.** CEAR (not an approved source) replaced by BOE (DA 21.9); 'desist' is required after a favourable decision, the TIE link is not in the decree. (count in current content: 1)

Old:
```html
<p>Selon CEAR, lorsque l'administration espagnole ne reçoit pas de réponse des autorités étrangères sur les antécédents pénaux dans un délai de trois mois, l'Unité des étrangers demande à la personne de fournir le certificat concerné sous 15 jours. [2]</p>

<p>À défaut, la demande de résidence peut être considérée comme abandonnée. [2]</p>

<h3>Demandeurs de protection internationale</h3>

<p>La demande de protection internationale en cours reste compatible avec la demande de régularisation jusqu'à la résolution favorable de cette dernière. [2]</p>

<p>Après une résolution favorable, le demandeur doit renoncer à sa demande de protection internationale, ou au recours correspondant, pour pouvoir obtenir la Tarjeta de Identidad de Extranjero (TIE). [2]</p>
```
New:
```html
<p>Lorsque les autorités étrangères ne transmettent pas le certificat d'antécédents pénaux dans un délai de trois mois, l'administration demande à la personne de le fournir sous 15 jours. [2]</p>

<p>À défaut, la personne est réputée s'être désistée de sa demande. [2]</p>

<h3>Demandeurs de protection internationale</h3>

<p>La demande de protection internationale en cours reste compatible avec la demande de régularisation jusqu'à la résolution favorable de cette dernière. [2]</p>

<p>Si la régularisation est accordée, la personne doit se désister de sa demande de protection internationale ou du recours qu'elle a pu former. [2]</p>
```

**7.** Two years applies to all arraigos except arraigo familiar; regulation in force since 20 May 2025. (count in current content: 1)

Old:
```html
<p>Pour les arraigos sociaux, la durée de présence continue exigée est en règle générale de deux ans. [3]</p>
```
New:
```html
<p>Ce règlement est en vigueur depuis le 20 mai 2025. À l'exception de l'arraigo familial, ces autorisations exigent en règle générale deux ans de présence continue en Espagne. [3]</p>
```

**8.** TIE within one month; authorisation valid one year, residence and work; art. 191 modification in last two months. (count in current content: 1)

Old:
```html
<p>Une fois l'autorisation accordée, la personne doit demander sa TIE dans les conditions fixées par l'administration. [2]</p>

<p>L'autorisation initiale est valable pour une durée limitée, ensuite le titulaire doit préparer la transition vers un titre de séjour ordinaire. [2]</p>
```
New:
```html
<p>Une fois l'autorisation accordée, la personne doit demander sa TIE dans le mois qui suit. [2][4]</p>

<p>L'autorisation initiale est valable un an et permet de résider et de travailler, comme salarié ou indépendant, dans toute l'Espagne. Dans les deux mois qui précèdent son expiration, le titulaire peut demander à passer vers une autre autorisation du règlement d'immigration (article 191). [2][4]</p>
```

**9.** Desist requirement worded as in DA 20 (no TIE condition). (count in current content: 1)

Old:
```html
<li>Oublier de renoncer à la demande d'asile ou au recours lorsque cette renonciation est requise pour la TIE. [2]</li>
```
New:
```html
<li>Oublier de se désister de la demande de protection internationale ou du recours après l'octroi de la régularisation. [2]</li>
```

**10.** FAQ questions as H3 (master rule); answers re-sourced; Correos window now past; job-contract answer made precise; question wording unchanged so FAQ schema still mirrors. (count in current content: 1)

Old:
```html
<h4>Peut-on encore déposer une demande de régularisation exceptionnelle ?</h4>

<p>Non, le délai de dépôt a pris fin le 30 juin 2026 et aucune prolongation n'a été accordée. [1][4]</p>

<h4>Que se passe-t-il si mon dossier n'a pas de réponse après trois mois ?</h4>

<p>Le délai maximal de résolution est de trois mois et le silence de l'administration vaut rejet. [4]</p>

<p>Il convient alors de faire analyser votre dossier et d'examiner les recours possibles.</p>

<h4>Jusqu'à quand peut-on corriger un dossier incomplet ?</h4>

<p>La période de subsanation en présentiel dans les bureaux de poste habilités se termine le 30 septembre 2026. [1][5]</p>

<h4>Un contrat de travail était-il nécessaire pour déposer la demande ?</h4>

<p>Aucun contrat de travail n'était exigé au moment du dépôt de la demande.</p>

<h4>Que faire si je n'ai pas déposé de demande à temps ?</h4>

<p>Il faut étudier les voies ordinaires du règlement d'immigration, en particulier les différents arraigos, selon votre date d'arrivée, votre situation familiale et votre activité. [3]</p>

<h4>Une demande de protection internationale est-elle compatible avec la régularisation ?</h4>

<p>Oui, elle reste compatible jusqu'à la résolution favorable de la régularisation, après quoi une renonciation est requise pour obtenir la TIE. [2]</p>
```
New:
```html
<h3>Peut-on encore déposer une demande de régularisation exceptionnelle ?</h3>

<p>Non, le délai de dépôt a pris fin le 30 juin 2026 et aucune prolongation n'a été accordée. [1]</p>

<h3>Que se passe-t-il si mon dossier n'a pas de réponse après trois mois ?</h3>

<p>Le délai maximal de résolution est de trois mois et le silence de l'administration vaut rejet. [2]</p>

<p>Il convient alors de faire analyser votre dossier et d'examiner les recours possibles.</p>

<h3>Jusqu'à quand peut-on corriger un dossier incomplet ?</h3>

<p>La subsanation en présentiel dans les bureaux de poste habilités était prévue jusqu'au 30 septembre 2026. Pour toute nouvelle demande de subsanation, respectez le délai (15 jours au maximum) et le canal indiqués dans la notification. [1][2]</p>

<h3>Un contrat de travail était-il nécessaire pour déposer la demande ?</h3>

<p>Non. Pour l'arraigo extraordinaire, un lien avec le travail (activité passée, offre d'emploi ou projet d'activité indépendante) n'était qu'une des trois conditions possibles, avec la vie familiale en Espagne et la situation de vulnérabilité. Les demandeurs de protection internationale n'avaient pas à remplir cette condition. [2][4]</p>

<h3>Que faire si je n'ai pas déposé de demande à temps ?</h3>

<p>Il faut étudier les voies ordinaires du règlement d'immigration, en particulier les différents arraigos, selon votre date d'arrivée, votre situation familiale et votre activité. [3]</p>

<h3>Une demande de protection internationale est-elle compatible avec la régularisation ?</h3>

<p>Oui, jusqu'à la résolution favorable de la régularisation. La personne doit ensuite se désister de sa demande de protection internationale ou de son recours. [2]</p>
```

**11.** Forbidden/unapproved sources removed (CEAR NGO, Civislex legal-services site, Martínez Caballero Abogados law firm); replaced by BOE RD 316/2026 and La Moncloa. (count in current content: 1)

Old:
```html
<li>CEAR, « Regularización extraordinaria de personas migrantes : toda la información » : <a href="https://www.cear.es/sections-post/regularizacion-extraordinaria-2026/" target="_blank" rel="noopener">https://www.cear.es/sections-post/regularizacion-extraordinaria-2026/</a></li>
<li>BOE, Real Decreto 1155/2024, du 19 novembre 2024 : <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">https://www.boe.es/eli/es/rd/2024/11/19/1155</a></li>
<li>Civislex, « Regularización extraordinaria 2026 : guía completa », mise à jour du 1er septembre 2026 : <a href="https://www.civislex.com/regularizacion-extraordinaria-2026-guia-completa/" target="_blank" rel="noopener">https://www.civislex.com/regularizacion-extraordinaria-2026-guia-completa/</a></li>
<li>Martínez Caballero Abogados, « Regularización 2026 sin resolver : por qué tarda y qué hacer » : <a href="https://martinezcaballeroabogados.com/antecedentes-penales/regularizacion-extraordinaria-2026-sin-resolver/" target="_blank" rel="noopener">https://martinezcaballeroabogados.com/antecedentes-penales/regularizacion-extraordinaria-2026-sin-resolver/</a></li>
```
New:
```html
<li>BOE, Real Decreto 316/2026, du 14 avril 2026, modifiant le Real Decreto 1155/2024 (BOE-A-2026-8284) : <a href="https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8284" target="_blank" rel="nofollow noopener">https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8284</a></li>
<li>BOE, Real Decreto 1155/2024, du 19 novembre 2024 : <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">https://www.boe.es/eli/es/rd/2024/11/19/1155</a></li>
<li>La Moncloa, ministère de l'Inclusion, de la Sécurité sociale et des Migrations, « Proceso de regularización migratoria extraordinaria: plazos y requisitos », 21 avril 2026 : <a href="https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/proceso-regularizacion-migratoria.aspx" target="_blank" rel="nofollow noopener">https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/proceso-regularizacion-migratoria.aspx</a></li>
```

### Other fields

- **Title tag**: Optional: `Régularisation exceptionnelle en Espagne : délai clos` (53) puts the focus keyword first. FR's top post (pos 5.4, 1,089 clicks): Mike to decide, low priority.
- **Excerpt** via `PUT /wp/v2/posts/21471` `excerpt` (242 chars): `La régularisation exceptionnelle en Espagne (Real Decreto 316/2026) a pris fin le 30 juin 2026, sans prolongation. Les dossiers déposés à temps sont en cours d'instruction ; les autres doivent passer par les voies ordinaires, comme l'arraigo.`
- **FAQPage schema** (`rank_math_schema_FAQPage`): replace `mainEntity` with the 6 visible questions so schema mirrors the page. Write path to be tested first (doc 07).

```json
[
 {
  "@type": "Question",
  "name": "Peut-on encore déposer une demande de régularisation exceptionnelle ?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Non, le délai de dépôt a pris fin le 30 juin 2026 et aucune prolongation n'a été accordée."
  }
 },
 {
  "@type": "Question",
  "name": "Que se passe-t-il si mon dossier n'a pas de réponse après trois mois ?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Le délai maximal de résolution est de trois mois et le silence de l'administration vaut rejet. Il convient alors de faire analyser votre dossier et d'examiner les recours possibles."
  }
 },
 {
  "@type": "Question",
  "name": "Jusqu'à quand peut-on corriger un dossier incomplet ?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "La subsanation en présentiel dans les bureaux de poste habilités était prévue jusqu'au 30 septembre 2026. Pour toute nouvelle demande de subsanation, respectez le délai (15 jours au maximum) et le canal indiqués dans la notification."
  }
 },
 {
  "@type": "Question",
  "name": "Un contrat de travail était-il nécessaire pour déposer la demande ?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Non. Pour l'arraigo extraordinaire, un lien avec le travail (activité passée, offre d'emploi ou projet d'activité indépendante) n'était qu'une des trois conditions possibles, avec la vie familiale en Espagne et la situation de vulnérabilité. Les demandeurs de protection internationale n'avaient pas à remplir cette condition."
  }
 },
 {
  "@type": "Question",
  "name": "Que faire si je n'ai pas déposé de demande à temps ?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Il faut étudier les voies ordinaires du règlement d'immigration, en particulier les différents arraigos, selon votre date d'arrivée, votre situation familiale et votre activité."
  }
 },
 {
  "@type": "Question",
  "name": "Une demande de protection internationale est-elle compatible avec la régularisation ?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Oui, jusqu'à la résolution favorable de la régularisation. La personne doit ensuite se désister de sa demande de protection internationale ou de son recours."
  }
 }
]
```

## EN 21452

- URL: https://delaguialuzon.com/en/blog/extraordinary-regularisation-foreigners-spain/
- `post_modified` at read time: 2026-10-01 00:18:53; `MD5(post_content)` = `12a35ee257de73b50b6ab6d2b4b31b84` (12311 bytes)
- `_elementor_edit_mode`: no `_elementor_edit_mode` row (legacy `_elementor_data` still present). Body renders from `post_content`.
- Post title (H1): Extraordinary Regularisation in Spain: The 30 June 2026 Deadline Has Closed, What Now?
- Title tag: Spain Regularisation 2026: Deadline Closed, What Next? (54, Title Case); meta description: 143 chars, OK

### Fact-check (non-OK rows; full list in CSV)

| Claim | Verdict | Correct value |
|---|---|---|
| In-person subsanación at post offices 'ends' on 30 September 2026 (present tense; intro, steps list, FAQ) | OUTDATED | Date has passed as of 1 Oct 2026: 'was scheduled to run until 30 September 2026' (Moncloa: 'se alargará hasta el 30 de septiembre'); any later extension unconfirmed |
| RD 316/2026 added 'an additional provision' to the RD 1155/2024 regulation | WRONG | It added two additional provisions: DA 20 (international protection applicants) and DA 21 (arraigo extraordinario) |
| Requirement: no criminal record in Spain and, 'depending on the case', previous countries of residence | UPDATE | No criminal record (art. 126.d RD 1155/2024) incl. country of origin and countries of residence in the 5 years before entry; plus no threat to public order, public security or public health |
| Requirements list (3 bullets) presented as complete | UPDATE | Omits DA 21.2: arraigo extraordinario applicants also needed at least one of (a) past work or intention to work (job offer / self-employment declaration), (b) living with family unit (minor or dependent children, first-degree ascendants), (c) certified vulnerability |
| (omitted) Provisional right to reside and work from notice of start of processing | UPDATE | Add: admission notice grants provisional residence and work authorisation nationwide; refusal ends it automatically (DA 20.3 / DA 21.4) |
| As of 8 September 2026 favourable decisions still being notified, plus requests and pending files | UNVERIFIABLE | Only source is a competing law firm (martinezcaballeroabogados.com); remove |
| A refusal can be challenged (recurso) | UNVERIFIABLE | Generally true under administrative law but not stated in RD 316/2026; remedy type and deadline to be confirmed by Félix/Sonia; currently cited to forbidden sources |
| After favourable decision applicant must withdraw protection claim/appeal 'to obtain the TIE' | UPDATE | DA 20.4: must desist from the protection application or appeal once resolved favourably; the decree does not make this a TIE condition |
| After grant, TIE must be requested 'under the conditions set by the authorities' | UPDATE | Within one month of the grant (DA 20.7 / DA 21.7) |
| Initial authorisation has a 'limited duration' | UPDATE | One year; residence and work (employed and self-employed) anywhere in Spain; modification to other authorisations (art. 191) in the 2 months before expiry |
| No job contract was required to apply | UPDATE | True but incomplete: a work link (past work, job offer or self-employment declaration) was one of three alternative DA 21.2 conditions; not required for protection applicants |
| Source [2] CEAR (NGO legal-assistance provider, not on approved list) | UPDATE | Replace with BOE RD 316/2026 |
| Source [4] Civislex (legal-services provider: forbidden) | WRONG | Remove; replace with La Moncloa 21 Apr 2026 explainer and BOE |
| Source [5] Martínez Caballero Abogados (competing law firm: forbidden) | WRONG | Remove |
| Excerpt presents the regularisation as open/current | OUTDATED | Rewrite excerpt: closed 30 Jun 2026, no extension; in-time files processing; ordinary routes |
| Rank Math FAQPage schema: 5 pre-approval Q&As ('current proposals', 'subject to the final Royal Decree', 'dates may change') that do not mirror the 6 visible FAQs | OUTDATED | Replace schema mainEntity with the 6 visible FAQ questions/answers (see staging) |
| Post title, title tag and 16 headings in Title Case | UPDATE | Sentence case (EN guide) |

20 further claims verified OK (figures, dates, requirements cut-off, silence rule, arraigo list).

### Style issues

- Title Case: post title (H1), title tag and 16 headings (H2/H3 incl. CTA). All fixed in changes 2-3, 4, 6-13, 15, 17 plus title/title tag below.
- Meta-textual opener 'This article sets out…' (change 1).
- No summary box (change 1). FAQ questions are H4 (change 15).
- Only 1 contextual internal link (practice page); target 3-8. Changes 8-10 add arraigo-spain, criminal-record-certificate-spain, residency-in-spain, residency-marriage-spanish-citizen.
- Forbidden sources: civislex.com, martinezcaballeroabogados.com; CEAR not approved (change 16).
- 0 blockquotes (not staged). Clean otherwise: no emoji, dashes, &amp; brand, '65 years', free consultation, Golden Visa, 'Conclusion', office claims.

### Proposed `post_content` changes (apply in order)

**1.** Summary box, dated update, expired-deadline intro (subsanación window now past), meta-textual opener removed, forbidden-source markers dropped. (count in current content: 1)

Old:
```html
<p><strong>Update of 30 September 2026</strong></p>

<p>The deadline to submit applications under Spain's extraordinary regularisation of foreign nationals ended on 30 June 2026.</p>

<p>No extension was granted. [1][4]</p>

<p>Applications submitted in time are now being processed, and the in-person rectification period (subsanación) at post offices ends on 30 September 2026. [1][5]</p>

<p>This article sets out the current position, how pending applications are handled and the ordinary routes that remain open to those who could not apply.</p>
```
New:
```html
<div style="background-color:#f5f5f5;padding: 24px 28px;margin: 0 0 24px 0">
<h2>Extraordinary regularisation in Spain: key points</h2>
<ul>
<li>The application deadline ended on 30 June 2026 and no extension was granted. [1]</li>
<li>Applications filed in time (1,174,978 in total) are being processed. [1]</li>
<li>The decision period is three months and silence from the authorities means refusal. [2]</li>
<li>The authorisation is valid for one year and allows the holder to live and work anywhere in Spain. [2]</li>
<li>Anyone who did not apply must use the ordinary routes, mainly arraigo. [3]</li>
</ul>
</div>

<p><strong>Update of 1 October 2026</strong></p>

<p>The deadline to submit applications under Spain's extraordinary regularisation of foreign nationals ended on 30 June 2026.</p>

<p>No extension was granted. [1]</p>

<p>Applications submitted in time are being processed. The in-person rectification period (subsanación) at designated post offices was scheduled to end on 30 September 2026. [1]</p>

<p>Anyone who did not apply must now rely on the ordinary routes under the immigration regulations, first and foremost the different forms of arraigo.</p>
```

**2.** Sentence-case H2; RD 316/2026 added TWO additional provisions; BOE date and entry into force; in-person start 20 April; re-sourced. (count in current content: 1)

Old:
```html
<h2>Extraordinary Regularisation in Spain: Review of the Closed Procedure</h2>

<p>The extraordinary regularisation was based on <strong>Royal Decree 316/2026</strong> of 14 April 2026, which added an additional provision to the immigration regulations approved by <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">Royal Decree 1155/2024</a>. [3][4]</p>

<p>Applications could be submitted from 16 April to 30 June 2026. [2]</p>
```
New:
```html
<h2>Extraordinary regularisation in Spain: review of the closed procedure</h2>

<p>The extraordinary regularisation was based on <strong>Royal Decree 316/2026</strong> of 14 April 2026 (published in the BOE on 15 April and in force from 16 April), which added two additional provisions (the twentieth and twenty-first) to the immigration regulations approved by <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="nofollow noopener">Royal Decree 1155/2024</a>. [2][3]</p>

<p>Applications could be filed online from 16 April to 30 June 2026, and in person by appointment from 20 April 2026. [2][4]</p>
```

**3.** Sentence-case H3. (count in current content: 1)

Old:
```html
<h3>Timeline of the Procedure</h3>
```
New:
```html
<h3>Timeline of the procedure</h3>
```

**4.** Sentence-case H2. (count in current content: 1)

Old:
```html
<h2>Requirements That Applied to the Extraordinary Regularisation</h2>
```
New:
```html
<h2>Requirements that applied to the extraordinary regularisation</h2>
```

**5.** Requirements incomplete: criminal-record scope, public-order condition and the arraigo extraordinario 'at least one of' condition (DA 21.2) were missing. (count in current content: 1)

Old:
```html
<li><strong>No criminal record</strong>, in Spain and, depending on the case, in previous countries of residence.</li>
</ul>

<p>International protection applicants could also apply, provided they had lodged their claim before 1 January 2026. [2][4]</p>
```
New:
```html
<li><strong>No criminal record</strong> in Spain, in the country of origin or in the countries of residence during the five years before arriving in Spain, and no threat to public order, public security or public health.</li>
<li><strong>For arraigo extraordinario, at least one further condition</strong>: having worked in Spain or showing an intention to work (a job offer or a self-employment declaration), living in Spain with one's family (minor or dependent children, or first-degree ascendants), or being in a situation of vulnerability certified by the competent social services.</li>
</ul>

<p>People who had applied for international protection before 1 January 2026 could also apply, without having to meet that further condition. [2][4]</p>
```

**6.** Sentence-case headings; three-month period counted from registry entry; silence re-sourced to BOE; law-firm-sourced 8 Sept status removed; provisional right to reside and work added. (count in current content: 1)

Old:
```html
<h2>Application Submitted in Time: Processing and Next Steps</h2>

<h3>Decision Period and Administrative Silence</h3>

<p>Royal Decree 316/2026 sets a maximum period of three months to decide and notify the application. [4][5]</p>

<p>If the authorities remain silent once that period expires, the effect is a refusal (negative administrative silence). [4]</p>

<p>A file without a reply after three months is therefore not the same as an approved authorisation.</p>

<p>As of 8 September 2026, favourable decisions were still being notified, alongside requests for further information and pending files. [5]</p>
```
New:
```html
<h2>Application submitted in time: processing and next steps</h2>

<h3>Decision period and administrative silence</h3>

<p>Royal Decree 316/2026 sets a maximum period of three months, counted from the day after the application entered the register, to decide and notify the application. [2]</p>

<p>If the authorities remain silent once that period expires, the effect is a refusal (negative administrative silence). [2]</p>

<p>A file without a reply after three months is therefore not the same as an approved authorisation.</p>

<p>Once the start of processing has been notified, the applicant may provisionally live and work, as an employee or self-employed, anywhere in Spain. A refusal automatically ends this provisional permission. [2]</p>
```

**7.** Sentence-case H3; 15-day subsanación cap; 30 Sept Correos date is now past; forbidden-source markers removed. (count in current content: 1)

Old:
```html
<h3>What You Can Do Now</h3>

<ol>
<li>Check the status of your file on the electronic portal and review your electronic notifications.</li>
<li>Reply promptly to any rectification request, within the period stated in the notification.</li>
<li>If the in-person rectification period at post offices concerns you, note the date of 30 September 2026. [1][5]</li>
<li>Keep the proof of submission and every document you filed.</li>
<li>If your application is refused, have the file reviewed as soon as possible, because the decision can be challenged. [4][5]</li>
```
New:
```html
<h3>What you can do now</h3>

<ol>
<li>Check the status of your file on the electronic portal and review your electronic notifications.</li>
<li>Reply promptly to any rectification request, within the period stated in the notification (15 days at most). [2]</li>
<li>In-person rectification at designated post offices was scheduled to end on 30 September 2026: use the reply channel stated in your notification. [1]</li>
<li>Keep the proof of submission and every document you filed.</li>
<li>If your application is refused, have the file reviewed as soon as possible, because the decision can be challenged.</li>
```

**8.** Sentence-case H3s; CEAR (not an approved source) replaced by BOE (DA 21.9); desist required after a favourable decision, TIE link not in the decree; internal link to sibling post. (count in current content: 1)

Old:
```html
<h3>Criminal Records and Additional Documents</h3>

<p>According to CEAR, if the Spanish authorities receive no reply from foreign authorities about criminal records within three months, the Immigration Office asks the applicant to provide the certificate within 15 days. [2]</p>

<p>If the applicant fails to do so, the residence application may be treated as withdrawn. [2]</p>

<h3>International Protection Applicants</h3>

<p>A pending international protection claim is compatible with regularisation until the latter is granted. [2]</p>

<p>After a favourable decision, the applicant must withdraw the international protection claim, or the related appeal, in order to obtain the Foreigner Identity Card (TIE). [2]</p>
```
New:
```html
<h3>Criminal records and additional documents</h3>

<p>If the foreign authorities do not send the criminal record certificate within three months, the Spanish authorities ask the applicant to provide it within 15 days. [2]</p>

<p>If the applicant fails to do so, the application is treated as withdrawn. [2] Our article on the <a href="https://delaguialuzon.com/en/blog/criminal-record-certificate-spain/">criminal record certificate for Spanish residence</a> explains how to obtain one.</p>

<h3>International protection applicants</h3>

<p>A pending international protection claim is compatible with regularisation until the latter is granted. [2]</p>

<p>If regularisation is granted, the applicant must withdraw the international protection claim, or any appeal lodged. [2]</p>
```

**9.** Sentence-case headings; two years applies to all arraigos except family arraigo; regulation in force since 20 May 2025; internal link to arraigo post. (count in current content: 1)

Old:
```html
<h2>Application Not Submitted: Ordinary Routes in Spain</h2>

<p>After 30 June 2026, the extraordinary regularisation is no longer available.</p>

<p>Those who did not apply must look to the ordinary routes under the immigration regulations (Royal Decree 1155/2024). [3]</p>

<h3>The Roots-Based Authorisations (Arraigo)</h3>

<p>The regulations in force provide several residence authorisations for exceptional circumstances based on roots: social, employment-based, training-based, family and second chance. [3]</p>

<p>For social roots, the continuous stay required is, as a general rule, two years. [3]</p>

<p>Each route has its own documentation, its own financial means or job contract requirements and its own evidential standards. [3]</p>
```
New:
```html
<h2>Application not submitted: ordinary routes in Spain</h2>

<p>After 30 June 2026, the extraordinary regularisation is no longer available.</p>

<p>Those who did not apply must look to the ordinary routes under the immigration regulations (Royal Decree 1155/2024). [3]</p>

<h3>The roots-based authorisations (arraigo)</h3>

<p>The regulations in force provide several residence authorisations for exceptional circumstances based on roots: social, employment-based, training-based, family and second chance. [3]</p>

<p>These regulations have applied since 20 May 2025. Except for family arraigo, these routes generally require two years of continuous stay in Spain. [3]</p>

<p>Each route has its own documentation, its own financial means or job contract requirements and its own evidential standards. [3] Our article on <a href="https://delaguialuzon.com/en/blog/arraigo-spain/">the arraigo routes in Spain</a> covers each one in detail.</p>
```

**10.** Sentence-case H3; internal links to sibling posts (EN had only 1 contextual internal link). (count in current content: 1)

Old:
```html
<h3>Other Residence Routes</h3>

<p>Depending on your profile, other routes may apply: family reunification, residence through marriage, a work authorisation or a specific visa.</p>
```
New:
```html
<h3>Other residence routes</h3>

<p>Depending on your profile, other routes may apply: family reunification, residence through marriage, a work authorisation or a specific visa.</p>

<p>Our overview of the <a href="https://delaguialuzon.com/en/blog/residency-in-spain/">pathways to residency in Spain</a> compares them, and spouses of Spanish nationals can read about <a href="https://delaguialuzon.com/en/blog/residency-marriage-spanish-citizen/">residency through marriage to a Spanish citizen</a>.</p>
```

**11.** Sentence-case H3. (count in current content: 1)

Old:
```html
<h3>Comparison: Extraordinary Regularisation and Ordinary Routes</h3>
```
New:
```html
<h3>Comparison: extraordinary regularisation and ordinary routes</h3>
```

**12.** Sentence-case H2; TIE within one month; one-year validity, residence and work; art. 191 modification. (count in current content: 1)

Old:
```html
<h2>After Authorisation: TIE, Work and Renewal</h2>

<p>Once the authorisation is granted, the person must apply for the TIE under the conditions set by the authorities. [2]</p>

<p>The initial authorisation has a limited duration, so the holder should prepare the move towards ordinary residence. [2]</p>
```
New:
```html
<h2>After authorisation: TIE, work and renewal</h2>

<p>Once the authorisation is granted, the holder must apply for the TIE within one month. [2][4]</p>

<p>The initial authorisation is valid for one year and allows the holder to live and work, as an employee or self-employed, anywhere in Spain. During the two months before it expires, the holder can apply to move to another authorisation under the regulations (Article 191). [2][4]</p>
```

**13.** Sentence-case H2. (count in current content: 1)

Old:
```html
<h2>Common Mistakes to Avoid</h2>
```
New:
```html
<h2>Common mistakes to avoid</h2>
```

**14.** Withdrawal requirement worded as in DA 20 (no TIE condition). (count in current content: 1)

Old:
```html
<li>Forgetting to withdraw an asylum claim or appeal when it is required to obtain the TIE. [2]</li>
```
New:
```html
<li>Forgetting to withdraw an international protection claim or appeal once regularisation is granted. [2]</li>
```

**15.** Sentence-case H2; FAQ questions as H3; answers re-sourced; Correos window now past; job-contract answer made precise; question wording unchanged. (count in current content: 1)

Old:
```html
<h2>Frequently Asked Questions on Extraordinary Regularisation</h2>

<h4>Can I still apply for extraordinary regularisation?</h4>

<p>No, the application period ended on 30 June 2026 and no extension was granted. [1][4]</p>

<h4>What happens if my file receives no reply after three months?</h4>

<p>The maximum decision period is three months and the authorities' silence amounts to a refusal. [4]</p>

<p>You should then have your file reviewed and consider the available remedies.</p>

<h4>Until when can an incomplete file be rectified?</h4>

<p>The in-person rectification period at the designated post offices ends on 30 September 2026. [1][5]</p>

<h4>Was a job contract required to apply?</h4>

<p>No job contract was required at the time of application.</p>

<h4>What should I do if I missed the deadline?</h4>

<p>You should review the ordinary routes under the immigration regulations, in particular the different arraigo authorisations, according to your date of arrival, family situation and activity. [3]</p>

<h4>Is international protection compatible with regularisation?</h4>

<p>Yes, until regularisation is granted, after which a withdrawal is required to obtain the TIE. [2]</p>
```
New:
```html
<h2>Frequently asked questions on extraordinary regularisation</h2>

<h3>Can I still apply for extraordinary regularisation?</h3>

<p>No, the application period ended on 30 June 2026 and no extension was granted. [1]</p>

<h3>What happens if my file receives no reply after three months?</h3>

<p>The maximum decision period is three months and the authorities' silence amounts to a refusal. [2]</p>

<p>You should then have your file reviewed and consider the available remedies.</p>

<h3>Until when can an incomplete file be rectified?</h3>

<p>In-person rectification at designated post offices was scheduled to end on 30 September 2026. For any new rectification request, follow the deadline (15 days at most) and the channel stated in the notification. [1][2]</p>

<h3>Was a job contract required to apply?</h3>

<p>No. For arraigo extraordinario, a link to work (past work, a job offer or a self-employment plan) was only one of three possible conditions, alongside family life in Spain and certified vulnerability. International protection applicants did not have to meet that condition. [2][4]</p>

<h3>What should I do if I missed the deadline?</h3>

<p>You should review the ordinary routes under the immigration regulations, in particular the different arraigo authorisations, according to your date of arrival, family situation and activity. [3]</p>

<h3>Is international protection compatible with regularisation?</h3>

<p>Yes, until regularisation is granted. The applicant must then withdraw the international protection claim or appeal. [2]</p>
```

**16.** Forbidden/unapproved sources removed (CEAR, Civislex, Martínez Caballero Abogados); replaced by BOE RD 316/2026 and La Moncloa. (count in current content: 1)

Old:
```html
<li>CEAR, "Regularización extraordinaria de personas migrantes": <a href="https://www.cear.es/sections-post/regularizacion-extraordinaria-2026/" target="_blank" rel="noopener">https://www.cear.es/sections-post/regularizacion-extraordinaria-2026/</a></li>
<li>BOE, Royal Decree 1155/2024 of 19 November 2024: <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">https://www.boe.es/eli/es/rd/2024/11/19/1155</a></li>
<li>Civislex, "Regularización extraordinaria 2026: guía completa", updated 1 September 2026: <a href="https://www.civislex.com/regularizacion-extraordinaria-2026-guia-completa/" target="_blank" rel="noopener">https://www.civislex.com/regularizacion-extraordinaria-2026-guia-completa/</a></li>
<li>Martínez Caballero Abogados, "Regularización 2026 sin resolver": <a href="https://martinezcaballeroabogados.com/antecedentes-penales/regularizacion-extraordinaria-2026-sin-resolver/" target="_blank" rel="noopener">https://martinezcaballeroabogados.com/antecedentes-penales/regularizacion-extraordinaria-2026-sin-resolver/</a></li>
```
New:
```html
<li>BOE, Royal Decree 316/2026 of 14 April 2026 amending Royal Decree 1155/2024 (BOE-A-2026-8284): <a href="https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8284" target="_blank" rel="nofollow noopener">https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8284</a></li>
<li>BOE, Royal Decree 1155/2024 of 19 November 2024: <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">https://www.boe.es/eli/es/rd/2024/11/19/1155</a></li>
<li>La Moncloa, Ministry of Inclusion, Social Security and Migration, "Proceso de regularización migratoria extraordinaria: plazos y requisitos", 21 April 2026: <a href="https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/proceso-regularizacion-migratoria.aspx" target="_blank" rel="nofollow noopener">https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/proceso-regularizacion-migratoria.aspx</a></li>
```

**17.** Sentence-case H2 (CTA). (count in current content: 1)

Old:
```html
<h2 style="margin: 0 0 14px 0">Contact Our Legal Team</h2>
```
New:
```html
<h2 style="margin: 0 0 14px 0">Contact our legal team</h2>
```

### Other fields

- **Post title (H1)** via `PUT /wp/v2/posts/21452` `title`: `Extraordinary regularisation in Spain: the 30 June 2026 deadline has closed, what now?` (sentence case).
- **Title tag**: Required (sentence case): `Spain regularisation 2026: deadline closed, what next?` (54). Alternative with focus keyword first: `Extraordinary regularisation in Spain: deadline closed` (54).
- **Excerpt** via `PUT /wp/v2/posts/21452` `excerpt` (236 chars): `Spain's extraordinary regularisation under Royal Decree 316/2026 closed on 30 June 2026 with no extension. Applications filed in time are being processed, and anyone who missed the deadline must use the ordinary routes, such as arraigo.`
- **FAQPage schema** (`rank_math_schema_FAQPage`): replace `mainEntity` with the 6 visible questions so schema mirrors the page. Write path to be tested first (doc 07).

```json
[
 {
  "@type": "Question",
  "name": "Can I still apply for extraordinary regularisation?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "No, the application period ended on 30 June 2026 and no extension was granted."
  }
 },
 {
  "@type": "Question",
  "name": "What happens if my file receives no reply after three months?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "The maximum decision period is three months and the authorities' silence amounts to a refusal. You should then have your file reviewed and consider the available remedies."
  }
 },
 {
  "@type": "Question",
  "name": "Until when can an incomplete file be rectified?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "In-person rectification at designated post offices was scheduled to end on 30 September 2026. For any new rectification request, follow the deadline (15 days at most) and the channel stated in the notification."
  }
 },
 {
  "@type": "Question",
  "name": "Was a job contract required to apply?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "No. For arraigo extraordinario, a link to work (past work, a job offer or a self-employment plan) was only one of three possible conditions, alongside family life in Spain and certified vulnerability. International protection applicants did not have to meet that condition."
  }
 },
 {
  "@type": "Question",
  "name": "What should I do if I missed the deadline?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "You should review the ordinary routes under the immigration regulations, in particular the different arraigo authorisations, according to your date of arrival, family situation and activity."
  }
 },
 {
  "@type": "Question",
  "name": "Is international protection compatible with regularisation?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Yes, until regularisation is granted. The applicant must then withdraw the international protection claim or appeal."
  }
 }
]
```

## ES 21398

- URL: https://delaguialuzon.com/blog/regularizacion-extraordinaria/
- `post_modified` at read time: 2026-10-01 12:22:30; `MD5(post_content)` = `6b6445e6a6a65ff84a4515ce43cb6e12` (13364 bytes)
- `_elementor_edit_mode`: `_elementor_edit_mode` = '' (empty string; legacy `_elementor_data` still present). Body renders from `post_content`.
- Post title (H1): Regularización extraordinaria en España: el plazo del 30 de junio de 2026 ha terminado, ¿y ahora qué?
- Title tag: Regularización 2026 en España: plazo cerrado, ¿qué hacer? (57); meta description: 138 chars, OK

### Fact-check (non-OK rows; full list in CSV)

| Claim | Verdict | Correct value |
|---|---|---|
| In-person subsanación at post offices 'ends' on 30 September 2026 (present tense; intro, steps list, FAQ) | OUTDATED | Date has passed as of 1 Oct 2026: 'was scheduled to run until 30 September 2026' (Moncloa: 'se alargará hasta el 30 de septiembre'); any later extension unconfirmed |
| RD 316/2026 added 'an additional provision' to the RD 1155/2024 regulation | WRONG | It added two additional provisions: DA 20 (international protection applicants) and DA 21 (arraigo extraordinario) |
| Requirement: no criminal record in Spain and, 'depending on the case', previous countries of residence | UPDATE | No criminal record (art. 126.d RD 1155/2024) incl. country of origin and countries of residence in the 5 years before entry; plus no threat to public order, public security or public health |
| Requirements list (3 bullets) presented as complete | UPDATE | Omits DA 21.2: arraigo extraordinario applicants also needed at least one of (a) past work or intention to work (job offer / self-employment declaration), (b) living with family unit (minor or dependent children, first-degree ascendants), (c) certified vulnerability |
| (omitted) Provisional right to reside and work from notice of start of processing | UPDATE | Add: admission notice grants provisional residence and work authorisation nationwide; refusal ends it automatically (DA 20.3 / DA 21.4) |
| As of 8 September 2026 favourable decisions still being notified, plus requests and pending files | UNVERIFIABLE | Only source is a competing law firm (martinezcaballeroabogados.com); remove |
| A refusal can be challenged (recurso) | UNVERIFIABLE | Generally true under administrative law but not stated in RD 316/2026; remedy type and deadline to be confirmed by Félix/Sonia; currently cited to forbidden sources |
| After favourable decision applicant must withdraw protection claim/appeal 'to obtain the TIE' | UPDATE | DA 20.4: must desist from the protection application or appeal once resolved favourably; the decree does not make this a TIE condition |
| After grant, TIE must be requested 'under the conditions set by the authorities' | UPDATE | Within one month of the grant (DA 20.7 / DA 21.7) |
| Initial authorisation has a 'limited duration' | UPDATE | One year; residence and work (employed and self-employed) anywhere in Spain; modification to other authorisations (art. 191) in the 2 months before expiry |
| No job contract was required to apply | UPDATE | True but incomplete: a work link (past work, job offer or self-employment declaration) was one of three alternative DA 21.2 conditions; not required for protection applicants |
| Source [2] CEAR (NGO legal-assistance provider, not on approved list) | UPDATE | Replace with BOE RD 316/2026 |
| Source [4] Civislex (legal-services provider: forbidden) | WRONG | Remove; replace with La Moncloa 21 Apr 2026 explainer and BOE |
| Source [5] Martínez Caballero Abogados (competing law firm: forbidden) | WRONG | Remove |
| Excerpt presents the regularisation as open/current | OUTDATED | Rewrite excerpt: closed 30 Jun 2026, no extension; in-time files processing; ordinary routes |
| Rank Math FAQPage schema: 5 pre-approval Q&As ('current proposals', 'subject to the final Royal Decree', 'dates may change') that do not mirror the 6 visible FAQs | OUTDATED | Replace schema mainEntity with the 6 visible FAQ questions/answers (see staging) |
| ES body lacks inline citations that FR/EN/RU carry (no-extension, Moncloa statistics, protection cut-off, three-month period, Correos date, FAQ answers) | UPDATE | Add [1]/[2] markers as staged; locale divergence |

20 further claims verified OK (figures, dates, requirements cut-off, silence rule, arraigo list).

### Style issues

- Meta-textual opener 'Este artículo resume…' (change 1). No summary box (change 1). FAQ questions are H4 (change 11).
- Locale divergence: ES carries far fewer inline citations than FR/EN/RU (no [1] anywhere in the body although the reference list has it); changes 1, 3, 4, 5, 6, 11 add them. ES was modified ~12 h after the other three (12:22, user 29): re-read before applying.
- Only 1 contextual internal link; no ES arraigo/residency sibling exists. Change 9 adds the ES NIE post (weak relevance). Content gap flagged.
- Forbidden sources: civislex.com, martinezcaballeroabogados.com; CEAR (change 12).
- Register: usted throughout, OK. Clean: no emoji, dashes, &amp;, '65 años', consulta gratuita, Golden Visa, 'Conclusión', office claims.

### Proposed `post_content` changes (apply in order)

**1.** Resumen inicial, fecha de actualización, entrada con plazo vencido (subsanación en Correos ya pasada), sin frase metatextual; citas añadidas. (count in current content: 1)

Old:
```html
<p><strong>Actualización del 30 de septiembre de 2026</strong></p>

<p>El plazo para presentar solicitudes de regularización extraordinaria de personas extranjeras en España terminó el 30 de junio de 2026.</p>

<p>No se concedió ninguna prórroga.</p>

<p>Los expedientes presentados en plazo están en tramitación, y el periodo de subsanación presencial en oficinas de Correos finaliza el 30 de septiembre de 2026.</p>

<p>Este artículo resume la situación actual, la tramitación de los expedientes presentados y las vías ordinarias que siguen abiertas para quien no pudo presentar su solicitud.</p>
```
New:
```html
<div style="background-color:#f5f5f5;padding: 24px 28px;margin: 0 0 24px 0">
<h2>Regularización extraordinaria: puntos clave</h2>
<ul>
<li>El plazo de presentación terminó el 30 de junio de 2026, sin prórroga. [1]</li>
<li>Las solicitudes presentadas en plazo (1.174.978 en total) siguen en tramitación. [1]</li>
<li>El plazo de resolución es de tres meses y el silencio administrativo es desestimatorio. [2]</li>
<li>La autorización concedida tiene una vigencia de un año y permite residir y trabajar en toda España. [2]</li>
<li>Quien no presentó la solicitud debe acudir a las vías ordinarias, principalmente el arraigo. [3]</li>
</ul>
</div>

<p><strong>Actualización del 1 de octubre de 2026</strong></p>

<p>El plazo para presentar solicitudes de regularización extraordinaria de personas extranjeras en España terminó el 30 de junio de 2026.</p>

<p>No se concedió ninguna prórroga. [1]</p>

<p>Los expedientes presentados en plazo están en tramitación. El periodo de subsanación presencial en las oficinas de Correos habilitadas estaba previsto hasta el 30 de septiembre de 2026. [1]</p>

<p>Quien no presentó su solicitud debe acudir ahora a las vías ordinarias del reglamento de extranjería, en primer lugar a las distintas modalidades de arraigo.</p>
```

**2.** El RD 316/2026 introdujo DOS disposiciones adicionales; fecha BOE y entrada en vigor; atención presencial desde el 20 de abril; fuentes oficiales. (count in current content: 1)

Old:
```html
<p>La regularización extraordinaria se basó en el <strong>Real Decreto 316/2026</strong>, de 14 de abril de 2026, que introdujo una disposición adicional en el reglamento de extranjería aprobado por el <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">Real Decreto 1155/2024</a>. [3][4]</p>

<p>Las solicitudes pudieron presentarse del 16 de abril al 30 de junio de 2026. [2]</p>
```
New:
```html
<p>La regularización extraordinaria se basó en el <strong>Real Decreto 316/2026</strong>, de 14 de abril de 2026 (BOE de 15 de abril, en vigor desde el 16 de abril), que introdujo dos disposiciones adicionales (vigésima y vigesimoprimera) en el reglamento de extranjería aprobado por el <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="nofollow noopener">Real Decreto 1155/2024</a>. [2][3]</p>

<p>Las solicitudes pudieron presentarse por vía telemática del 16 de abril al 30 de junio de 2026, y de forma presencial con cita previa desde el 20 de abril de 2026. [2][4]</p>
```

**3.** Cifras del Ministerio sin cita en ES (FR/EN/RU sí la llevan): se añade [1]. (count in current content: 1)

Old:
```html
<p>Según el Ministerio de Inclusión, Seguridad Social y Migraciones, el plazo se cerró con 1.174.978 solicitudes recibidas.</p>

<p>A fecha de 2 de julio de 2026 se habían tramitado 609.737 expedientes.</p>

<p>Aproximadamente el 79,6 % de las solicitudes correspondía a autorizaciones por circunstancias excepcionales por arraigo extraordinario, y el 20,4 % a solicitantes de protección internacional.</p>

<p>Alrededor del 83,2 % de las solicitudes se presentó por vía telemática, y el resto de forma presencial.</p>
```
New:
```html
<p>Según el Ministerio de Inclusión, Seguridad Social y Migraciones, el plazo se cerró con 1.174.978 solicitudes recibidas. [1]</p>

<p>A fecha de 2 de julio de 2026 se habían tramitado 609.737 expedientes. [1]</p>

<p>Aproximadamente el 79,6 % de las solicitudes correspondía a autorizaciones por circunstancias excepcionales por arraigo extraordinario, y el 20,4 % a solicitantes de protección internacional. [1]</p>

<p>Alrededor del 83,2 % de las solicitudes se presentó por vía telemática, y el resto de forma presencial. [1]</p>
```

**4.** Requisitos incompletos: alcance de los antecedentes penales, orden público y el requisito alternativo del arraigo extraordinario (DA 21.ª.2). (count in current content: 1)

Old:
```html
<li><strong>Ausencia de antecedentes penales</strong>, en España y, según los casos, en los países de residencia anteriores.</li>
</ul>

<p>Los solicitantes de protección internacional también podían presentar solicitud, siempre que hubieran manifestado su voluntad antes del 1 de enero de 2026.</p>
```
New:
```html
<li><strong>Ausencia de antecedentes penales</strong> en España, en el país de origen y en los países de residencia de los cinco años anteriores a la entrada en España, y no representar una amenaza para el orden público, la seguridad pública o la salud pública.</li>
<li><strong>En el arraigo extraordinario, al menos un requisito adicional</strong>: haber trabajado en España o acreditar la intención de trabajar (oferta de empleo o declaración responsable de actividad por cuenta propia), permanecer en España con la unidad familiar (hijos menores o con discapacidad, o ascendientes de primer grado), o encontrarse en situación de vulnerabilidad acreditada por los servicios sociales competentes.</li>
</ul>

<p>Las personas que habían presentado solicitud de protección internacional antes del 1 de enero de 2026 también podían solicitarla, sin tener que cumplir ese requisito adicional. [2][4]</p>
```

**5.** Plazo de tres meses desde la entrada en registro; fuentes BOE; se elimina el estado a 8 de septiembre (fuente: despacho competidor); habilitación provisional para residir y trabajar. (count in current content: 1)

Old:
```html
<p>El Real Decreto 316/2026 fija un plazo máximo de tres meses para resolver y notificar la solicitud.</p>

<p>El silencio de la Administración al vencer ese plazo tiene efecto desestimatorio (silencio administrativo negativo). [4]</p>

<p>Un expediente sin respuesta pasados tres meses no equivale, por tanto, a una autorización concedida.</p>

<p>A fecha de 8 de septiembre de 2026 seguían notificándose resoluciones favorables, pero también requerimientos y expedientes pendientes. [5]</p>
```
New:
```html
<p>El Real Decreto 316/2026 fija un plazo máximo de tres meses, a contar desde el día siguiente a la entrada de la solicitud en el registro, para resolver y notificar. [2]</p>

<p>El silencio de la Administración al vencer ese plazo tiene efecto desestimatorio (silencio administrativo negativo). [2]</p>

<p>Un expediente sin respuesta pasados tres meses no equivale, por tanto, a una autorización concedida.</p>

<p>Con la comunicación de inicio de la tramitación, la persona solicitante queda habilitada de forma provisional para residir y trabajar, por cuenta ajena o propia, en todo el territorio nacional. La denegación supone la pérdida automática de esa habilitación provisional. [2]</p>
```

**6.** Plazo máximo de subsanación de 15 días; la fecha del 30 de septiembre ya ha pasado; citas. (count in current content: 1)

Old:
```html
<li>Conteste sin demora a cualquier requerimiento de subsanación, dentro del plazo indicado en la notificación.</li>
<li>Si le afecta el periodo de subsanación presencial en Correos, tenga en cuenta la fecha del 30 de septiembre de 2026.</li>
```
New:
```html
<li>Conteste sin demora a cualquier requerimiento de subsanación, dentro del plazo indicado en la notificación (como máximo, 15 días). [2]</li>
<li>La subsanación presencial en las oficinas de Correos habilitadas estaba prevista hasta el 30 de septiembre de 2026: utilice el cauce de respuesta que indique su notificación. [1]</li>
```

**7.** CEAR (fuente no aprobada) sustituida por el BOE (DA 21.ª.9); el desistimiento se exige tras la resolución favorable, el vínculo con la TIE no figura en el decreto. (count in current content: 1)

Old:
```html
<p>Según CEAR, si la Administración española no recibe respuesta de las autoridades extranjeras sobre los antecedentes penales en tres meses, la Unidad de Extranjería requiere a la persona el certificado en un plazo de 15 días. [2]</p>

<p>Si no lo aporta, la solicitud de residencia puede entenderse desistida. [2]</p>

<h3>Solicitantes de protección internacional</h3>

<p>La solicitud de protección internacional en trámite es compatible con la regularización hasta la resolución favorable de esta. [2]</p>

<p>Tras la resolución favorable, el solicitante debe renunciar a su solicitud de protección internacional, o al recurso correspondiente, para poder tramitar la Tarjeta de Identidad de Extranjero (TIE). [2]</p>
```
New:
```html
<p>Si las autoridades extranjeras no remiten el certificado de antecedentes penales en tres meses, la Administración requiere a la persona que lo aporte en un plazo de 15 días. [2]</p>

<p>Si no lo aporta, se la tiene por desistida de su solicitud. [2]</p>

<h3>Solicitantes de protección internacional</h3>

<p>La solicitud de protección internacional en trámite es compatible con la regularización hasta la resolución favorable de esta. [2]</p>

<p>Si la resolución es favorable, la persona debe desistir de su solicitud de protección internacional o del recurso que hubiera interpuesto. [2]</p>
```

**8.** Los dos años se aplican a todos los arraigos salvo el familiar; reglamento vigente desde el 20 de mayo de 2025. (count in current content: 1)

Old:
```html
<p>En los arraigos sociales, la permanencia continuada exigida es, por regla general, de dos años. [3]</p>
```
New:
```html
<p>Este reglamento está en vigor desde el 20 de mayo de 2025. Salvo el arraigo familiar, estas autorizaciones exigen por regla general dos años de permanencia continuada en España. [3]</p>
```

**9.** TIE en el plazo de un mes; vigencia de un año, residencia y trabajo; modificación del artículo 191; enlace interno. (count in current content: 1)

Old:
```html
<p>Concedida la autorización, la persona debe solicitar su TIE en las condiciones que fije la Administración. [2]</p>

<p>La autorización inicial tiene una duración limitada, por lo que el titular debe preparar la transición hacia una residencia ordinaria. [2]</p>
```
New:
```html
<p>Concedida la autorización, la persona debe solicitar su TIE en el plazo de un mes. [2][4] Puede consultar la diferencia entre ambos documentos en nuestro artículo sobre <a href="https://delaguialuzon.com/blog/nie-en-espana-que-es-como-obtenerlo-y-para-que-lo-necesita/">el NIE en España y cómo obtenerlo</a>.</p>

<p>La autorización inicial tiene una vigencia de un año y permite residir y trabajar, por cuenta ajena o propia, en todo el territorio nacional. En los dos meses previos a su expiración, el titular puede solicitar la modificación a otra autorización del reglamento (artículo 191). [2][4]</p>
```

**10.** Desistimiento redactado como en la DA 20.ª. (count in current content: 1)

Old:
```html
<li>Olvidar renunciar a la solicitud de asilo o al recurso cuando es necesario para tramitar la TIE. [2]</li>
```
New:
```html
<li>Olvidar desistir de la solicitud de protección internacional o del recurso una vez concedida la regularización. [2]</li>
```

**11.** Preguntas del FAQ como H3; respuestas con fuentes oficiales; la subsanación en Correos ya ha pasado; respuesta sobre el contrato más precisa; preguntas sin cambios. (count in current content: 1)

Old:
```html
<h4>¿Se puede presentar todavía una solicitud de regularización extraordinaria?</h4>

<p>No, el plazo de presentación terminó el 30 de junio de 2026 y no se concedió prórroga.</p>

<h4>¿Qué ocurre si mi expediente no tiene respuesta a los tres meses?</h4>

<p>El plazo máximo de resolución es de tres meses y el silencio de la Administración es desestimatorio. [4]</p>

<p>Conviene entonces analizar su expediente y estudiar los recursos posibles.</p>

<h4>¿Hasta cuándo se puede subsanar un expediente incompleto?</h4>

<p>El periodo de subsanación presencial en las oficinas de Correos habilitadas finaliza el 30 de septiembre de 2026.</p>

<h4>¿Era necesario un contrato de trabajo para presentar la solicitud?</h4>

<p>No se exigía contrato de trabajo en el momento de presentar la solicitud.</p>

<h4>¿Qué hacer si no presenté la solicitud a tiempo?</h4>

<p>Hay que estudiar las vías ordinarias del reglamento de extranjería, en particular los distintos arraigos, según su fecha de llegada, su situación familiar y su actividad. [3]</p>

<h4>¿Es compatible la protección internacional con la regularización?</h4>

<p>Sí, es compatible hasta la resolución favorable de la regularización, tras la cual se exige una renuncia para obtener la TIE. [2]</p>
```
New:
```html
<h3>¿Se puede presentar todavía una solicitud de regularización extraordinaria?</h3>

<p>No, el plazo de presentación terminó el 30 de junio de 2026 y no se concedió prórroga. [1]</p>

<h3>¿Qué ocurre si mi expediente no tiene respuesta a los tres meses?</h3>

<p>El plazo máximo de resolución es de tres meses y el silencio de la Administración es desestimatorio. [2]</p>

<p>Conviene entonces analizar su expediente y estudiar los recursos posibles.</p>

<h3>¿Hasta cuándo se puede subsanar un expediente incompleto?</h3>

<p>La subsanación presencial en las oficinas de Correos habilitadas estaba prevista hasta el 30 de septiembre de 2026. Ante un nuevo requerimiento, respete el plazo (como máximo, 15 días) y el cauce que indique la notificación. [1][2]</p>

<h3>¿Era necesario un contrato de trabajo para presentar la solicitud?</h3>

<p>No. En el arraigo extraordinario, el vínculo laboral (trabajo previo, oferta de empleo o declaración de actividad por cuenta propia) era solo uno de los tres requisitos posibles, junto con la unidad familiar en España y la situación de vulnerabilidad. Los solicitantes de protección internacional no tenían que cumplirlo. [2][4]</p>

<h3>¿Qué hacer si no presenté la solicitud a tiempo?</h3>

<p>Hay que estudiar las vías ordinarias del reglamento de extranjería, en particular los distintos arraigos, según su fecha de llegada, su situación familiar y su actividad. [3]</p>

<h3>¿Es compatible la protección internacional con la regularización?</h3>

<p>Sí, hasta la resolución favorable de la regularización. Después, la persona debe desistir de su solicitud de protección internacional o de su recurso. [2]</p>
```

**12.** Fuentes prohibidas o no aprobadas eliminadas (CEAR, Civislex, Martínez Caballero Abogados); sustituidas por BOE RD 316/2026 y La Moncloa. (count in current content: 1)

Old:
```html
<li>CEAR, «Regularización extraordinaria de personas migrantes: toda la información»: <a href="https://www.cear.es/sections-post/regularizacion-extraordinaria-2026/" target="_blank" rel="noopener">https://www.cear.es/sections-post/regularizacion-extraordinaria-2026/</a></li>
<li>BOE, Real Decreto 1155/2024, de 19 de noviembre de 2024: <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">https://www.boe.es/eli/es/rd/2024/11/19/1155</a></li>
<li>Civislex, «Regularización extraordinaria 2026: guía completa», actualización del 1 de septiembre de 2026: <a href="https://www.civislex.com/regularizacion-extraordinaria-2026-guia-completa/" target="_blank" rel="noopener">https://www.civislex.com/regularizacion-extraordinaria-2026-guia-completa/</a></li>
<li>Martínez Caballero Abogados, «Regularización 2026 sin resolver: por qué tarda y qué hacer»: <a href="https://martinezcaballeroabogados.com/antecedentes-penales/regularizacion-extraordinaria-2026-sin-resolver/" target="_blank" rel="noopener">https://martinezcaballeroabogados.com/antecedentes-penales/regularizacion-extraordinaria-2026-sin-resolver/</a></li>
```
New:
```html
<li>BOE, Real Decreto 316/2026, de 14 de abril, por el que se modifica el Real Decreto 1155/2024 (BOE-A-2026-8284): <a href="https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8284" target="_blank" rel="nofollow noopener">https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8284</a></li>
<li>BOE, Real Decreto 1155/2024, de 19 de noviembre de 2024: <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">https://www.boe.es/eli/es/rd/2024/11/19/1155</a></li>
<li>La Moncloa, Ministerio de Inclusión, Seguridad Social y Migraciones, «Proceso de regularización migratoria extraordinaria: plazos y requisitos», 21 de abril de 2026: <a href="https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/proceso-regularizacion-migratoria.aspx" target="_blank" rel="nofollow noopener">https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/proceso-regularizacion-migratoria.aspx</a></li>
```

### Other fields

- **Title tag**: Optional: `Regularización extraordinaria: plazo cerrado, ¿qué hacer?` (57) puts the focus keyword first.
- **Excerpt** via `PUT /wp/v2/posts/21398` `excerpt` (238 chars): `La regularización extraordinaria del Real Decreto 316/2026 terminó el 30 de junio de 2026, sin prórroga. Las solicitudes presentadas en plazo siguen en tramitación y quien no la presentó debe acudir a las vías ordinarias, como el arraigo.`
- **FAQPage schema** (`rank_math_schema_FAQPage`): replace `mainEntity` with the 6 visible questions so schema mirrors the page. Write path to be tested first (doc 07).

```json
[
 {
  "@type": "Question",
  "name": "¿Se puede presentar todavía una solicitud de regularización extraordinaria?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "No, el plazo de presentación terminó el 30 de junio de 2026 y no se concedió prórroga."
  }
 },
 {
  "@type": "Question",
  "name": "¿Qué ocurre si mi expediente no tiene respuesta a los tres meses?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "El plazo máximo de resolución es de tres meses y el silencio de la Administración es desestimatorio. Conviene entonces analizar su expediente y estudiar los recursos posibles."
  }
 },
 {
  "@type": "Question",
  "name": "¿Hasta cuándo se puede subsanar un expediente incompleto?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "La subsanación presencial en las oficinas de Correos habilitadas estaba prevista hasta el 30 de septiembre de 2026. Ante un nuevo requerimiento, respete el plazo (como máximo, 15 días) y el cauce que indique la notificación."
  }
 },
 {
  "@type": "Question",
  "name": "¿Era necesario un contrato de trabajo para presentar la solicitud?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "No. En el arraigo extraordinario, el vínculo laboral (trabajo previo, oferta de empleo o declaración de actividad por cuenta propia) era solo uno de los tres requisitos posibles, junto con la unidad familiar en España y la situación de vulnerabilidad. Los solicitantes de protección internacional no tenían que cumplirlo."
  }
 },
 {
  "@type": "Question",
  "name": "¿Qué hacer si no presenté la solicitud a tiempo?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Hay que estudiar las vías ordinarias del reglamento de extranjería, en particular los distintos arraigos, según su fecha de llegada, su situación familiar y su actividad."
  }
 },
 {
  "@type": "Question",
  "name": "¿Es compatible la protección internacional con la regularización?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Sí, hasta la resolución favorable de la regularización. Después, la persona debe desistir de su solicitud de protección internacional o de su recurso."
  }
 }
]
```

## RU 23581

- URL: https://delaguialuzon.com/ru/blog/%D1%8D%D0%BA%D1%81%D1%82%D1%80%D0%B0%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%80%D0%BD%D0%B0%D1%8F-%D0%BB%D0%B5%D0%B3%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/ (/ru/blog/экстраординарная-легализация/)
- `post_modified` at read time: 2026-10-01 00:19:36; `MD5(post_content)` = `929d4c5a46f47c830e79f260564c9bd7` (19294 bytes)
- `_elementor_edit_mode`: no `_elementor_edit_mode` row (legacy `_elementor_data` still present). Body renders from `post_content`.
- Post title (H1): Экстраординарная легализация в Испании: срок 30 июня 2026 года истёк, что дальше?
- Title tag: Легализация в Испании 2026: срок истёк, что делать? (51); meta description: 147 chars, OK

### Fact-check (non-OK rows; full list in CSV)

| Claim | Verdict | Correct value |
|---|---|---|
| In-person subsanación at post offices 'ends' on 30 September 2026 (present tense; intro, steps list, FAQ) | OUTDATED | Date has passed as of 1 Oct 2026: 'was scheduled to run until 30 September 2026' (Moncloa: 'se alargará hasta el 30 de septiembre'); any later extension unconfirmed |
| RD 316/2026 added 'an additional provision' to the RD 1155/2024 regulation | WRONG | It added two additional provisions: DA 20 (international protection applicants) and DA 21 (arraigo extraordinario) |
| Requirement: no criminal record in Spain and, 'depending on the case', previous countries of residence | UPDATE | No criminal record (art. 126.d RD 1155/2024) incl. country of origin and countries of residence in the 5 years before entry; plus no threat to public order, public security or public health |
| Requirements list (3 bullets) presented as complete | UPDATE | Omits DA 21.2: arraigo extraordinario applicants also needed at least one of (a) past work or intention to work (job offer / self-employment declaration), (b) living with family unit (minor or dependent children, first-degree ascendants), (c) certified vulnerability |
| (omitted) Provisional right to reside and work from notice of start of processing | UPDATE | Add: admission notice grants provisional residence and work authorisation nationwide; refusal ends it automatically (DA 20.3 / DA 21.4) |
| As of 8 September 2026 favourable decisions still being notified, plus requests and pending files | UNVERIFIABLE | Only source is a competing law firm (martinezcaballeroabogados.com); remove |
| A refusal can be challenged (recurso) | UNVERIFIABLE | Generally true under administrative law but not stated in RD 316/2026; remedy type and deadline to be confirmed by Félix/Sonia; currently cited to forbidden sources |
| After favourable decision applicant must withdraw protection claim/appeal 'to obtain the TIE' | UPDATE | DA 20.4: must desist from the protection application or appeal once resolved favourably; the decree does not make this a TIE condition |
| After grant, TIE must be requested 'under the conditions set by the authorities' | UPDATE | Within one month of the grant (DA 20.7 / DA 21.7) |
| Initial authorisation has a 'limited duration' | UPDATE | One year; residence and work (employed and self-employed) anywhere in Spain; modification to other authorisations (art. 191) in the 2 months before expiry |
| No job contract was required to apply | UPDATE | True but incomplete: a work link (past work, job offer or self-employment declaration) was one of three alternative DA 21.2 conditions; not required for protection applicants |
| Source [2] CEAR (NGO legal-assistance provider, not on approved list) | UPDATE | Replace with BOE RD 316/2026 |
| Source [4] Civislex (legal-services provider: forbidden) | WRONG | Remove; replace with La Moncloa 21 Apr 2026 explainer and BOE |
| Source [5] Martínez Caballero Abogados (competing law firm: forbidden) | WRONG | Remove |
| Excerpt presents the regularisation as open/current | OUTDATED | Rewrite excerpt: closed 30 Jun 2026, no extension; in-time files processing; ordinary routes |
| Rank Math FAQPage schema: 5 pre-approval Q&As ('current proposals', 'subject to the final Royal Decree', 'dates may change') that do not mirror the 6 visible FAQs | OUTDATED | Replace schema mainEntity with the 6 visible FAQ questions/answers (see staging) |
| FAQPage schema Q1: must be in Spain more than 2 years (social arraigo) or 3 years (labour arraigo), job contract min 30 h/week | WRONG | Regularisation required presence before 1 Jan 2026 and 5 months continuous stay; no 30-hour contract (DA 21); also contains an em dash |
| FAQPage schema Q2: applications started in August 2026 and run for a year | WRONG | 16 April to 30 June 2026 |
| FAQPage schema Q3: forms EX-10 or EX-11 | WRONG | Not the regularisation forms (specific models under RD 316/2026); remove form numbers unless confirmed |
| FAQPage schema Q5: residence and work for 1-2 years | WRONG | One year initial validity |
| Excerpt contains an em dash | UPDATE | Rewrite without dash (style rule) |
| Body uses lowercase 'вас/ваш' addressing the reader (4x) | UPDATE | Capitalised «Вы/Ваш» per RU guide |

20 further claims verified OK (figures, dates, requirements cut-off, silence rule, arraigo list).

### Style issues

- Banned meta-textual opener «В этой статье мы описываем…» (change 1). No summary box (change 1). FAQ questions are H4 (change 12).
- Lowercase «вас/ваш» addressing the reader 4x; RU guide requires «Вы» (changes 5, 8, 10, 14).
- Excerpt contains an em dash and is outdated (excerpt below).
- CTA lacks the 'contact the firm' page link that FR/EN/ES have (not staged: RU contact URL to confirm).
- Only 1 contextual internal link; change 9 adds the RU NIE/TIE post. Few RU siblings exist.
- Forbidden sources: civislex.com, martinezcaballeroabogados.com; CEAR (change 13).
- Terminology: no «ненасыщенный» calque, no «Золотая виза», no «бесплатная консультация». No emoji, no dash in body.

### Proposed `post_content` changes (apply in order)

**1.** Блок ключевых фактов, дата обновления, истёкший срок в первом абзаце (период subsanación в почте уже прошёл), убран метатекстовый зачин «В этой статье». (count in current content: 1)

Old:
```html
<p><strong>Обновление от 30 сентября 2026 года</strong></p>

<p>Срок подачи заявлений на экстраординарную легализацию иностранных граждан в Испании истёк 30 июня 2026 года.</p>

<p>Продление не предоставлялось. [1][4]</p>

<p>Заявления, поданные в срок, находятся на рассмотрении, а период очного устранения недостатков (subsanación) в отделениях почты заканчивается 30 сентября 2026 года. [1][5]</p>

<p>В этой статье мы описываем текущую ситуацию, порядок рассмотрения уже поданных дел и обычные пути получения вида на жительство для тех, кто не успел подать заявление.</p>
```
New:
```html
<div style="background-color:#f5f5f5;padding: 24px 28px;margin: 0 0 24px 0">
<h2>Экстраординарная легализация в Испании: главное</h2>
<ul>
<li>Срок подачи заявлений истёк 30 июня 2026 года, продления не было. [1]</li>
<li>Заявления, поданные в срок (всего 1 174 978), находятся на рассмотрении. [1]</li>
<li>Срок принятия решения составляет три месяца, молчание администрации означает отказ. [2]</li>
<li>Выданное разрешение действует один год и даёт право жить и работать на всей территории Испании. [2]</li>
<li>Тем, кто не подал заявление, доступны обычные пути, прежде всего arraigo. [3]</li>
</ul>
</div>

<p><strong>Обновление от 1 октября 2026 года</strong></p>

<p>Срок подачи заявлений на экстраординарную легализацию иностранных граждан в Испании истёк 30 июня 2026 года.</p>

<p>Продление не предоставлялось. [1]</p>

<p>Заявления, поданные в срок, находятся на рассмотрении. Период очного устранения недостатков (subsanación) в уполномоченных отделениях почты был предусмотрен до 30 сентября 2026 года. [1]</p>

<p>Тем, кто не подал заявление, теперь необходимо обращаться к обычным процедурам иммиграционного регламента, прежде всего к различным видам arraigo.</p>
```

**2.** Декрет 316/2026 добавил ДВА дополнительных положения; дата публикации в BOE и вступления в силу; очный приём с 20 апреля; официальные источники. (count in current content: 1)

Old:
```html
<p>Экстраординарная легализация основывалась на <strong>Королевском декрете 316/2026</strong> от 14 апреля 2026 года, который добавил дополнительное положение в иммиграционный регламент, утверждённый <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">Королевским декретом 1155/2024</a>. [3][4]</p>

<p>Заявления принимались с 16 апреля по 30 июня 2026 года. [2]</p>
```
New:
```html
<p>Экстраординарная легализация основывалась на <strong>Королевском декрете 316/2026</strong> от 14 апреля 2026 года (опубликован в BOE 15 апреля, вступил в силу 16 апреля), который добавил два дополнительных положения (двадцатое и двадцать первое) в иммиграционный регламент, утверждённый <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="nofollow noopener">Королевским декретом 1155/2024</a>. [2][3]</p>

<p>Заявления принимались в электронной форме с 16 апреля по 30 июня 2026 года, а очно по предварительной записи с 20 апреля 2026 года. [2][4]</p>
```

**3.** Неполные требования: объём проверки судимости, общественный порядок и дополнительное условие для arraigo extraordinario (DA 21.2). (count in current content: 1)

Old:
```html
<li><strong>Отсутствие судимости</strong> в Испании и, в зависимости от случая, в прежних странах проживания.</li>
</ul>

<p>Заявители, ходатайствующие о международной защите, также могли подать заявление при условии, что обратились за защитой до 1 января 2026 года. [2][4]</p>
```
New:
```html
<li><strong>Отсутствие судимости</strong> в Испании, в стране происхождения и в странах проживания за пять лет до въезда в Испанию, а также отсутствие угрозы общественному порядку, общественной безопасности или здоровью населения.</li>
<li><strong>Для arraigo extraordinario хотя бы одно дополнительное условие</strong>: работа в Испании или намерение работать (предложение о работе или декларация о самозанятости), проживание в Испании вместе с семьёй (несовершеннолетние дети или дети на иждивении, родители), либо уязвимое положение, подтверждённое компетентными социальными службами.</li>
</ul>

<p>Лица, подавшие ходатайство о международной защите до 1 января 2026 года, также могли подать заявление без выполнения этого дополнительного условия. [2][4]</p>
```

**4.** Трёхмесячный срок считается со дня регистрации; источник BOE; убрано состояние на 8 сентября (источник: конкурирующая юрфирма); добавлено временное право жить и работать. (count in current content: 1)

Old:
```html
<p>Королевский декрет 316/2026 устанавливает максимальный срок в три месяца для вынесения и уведомления о решении. [4][5]</p>

<p>Если по истечении этого срока администрация молчит, это означает отказ (отрицательное административное молчание). [4]</p>

<p>Отсутствие ответа через три месяца, таким образом, не равнозначно выданному разрешению.</p>

<p>По состоянию на 8 сентября 2026 года по-прежнему поступали положительные решения, а также запросы дополнительных документов и дела в ожидании. [5]</p>
```
New:
```html
<p>Королевский декрет 316/2026 устанавливает максимальный срок в три месяца, считая со дня, следующего за регистрацией заявления, для вынесения решения и уведомления о нём. [2]</p>

<p>Если по истечении этого срока администрация молчит, это означает отказ (отрицательное административное молчание). [2]</p>

<p>Отсутствие ответа через три месяца, таким образом, не равнозначно выданному разрешению.</p>

<p>После уведомления о начале рассмотрения заявитель временно получает право проживать и работать по найму или как самозанятый на всей территории Испании. Отказ автоматически прекращает это временное право. [2]</p>
```

**5.** Срок устранения недостатков не более 15 дней; дата 30 сентября уже прошла; обращение на «Вы»; убраны ссылки на запрещённые источники. (count in current content: 1)

Old:
```html
<li>Незамедлительно отвечайте на любой запрос об устранении недостатков в срок, указанный в уведомлении.</li>
<li>Если вас касается период очного устранения недостатков в отделениях почты, учтите дату 30 сентября 2026 года. [1][5]</li>
<li>Сохраняйте подтверждение подачи и все представленные документы.</li>
<li>В случае отказа как можно скорее организуйте анализ дела, поскольку решение можно обжаловать. [4][5]</li>
```
New:
```html
<li>Незамедлительно отвечайте на любой запрос об устранении недостатков в срок, указанный в уведомлении (не более 15 дней). [2]</li>
<li>Очное устранение недостатков в уполномоченных отделениях почты было предусмотрено до 30 сентября 2026 года: используйте способ ответа, указанный в Вашем уведомлении. [1]</li>
<li>Сохраняйте подтверждение подачи и все представленные документы.</li>
<li>В случае отказа как можно скорее организуйте анализ дела, поскольку решение можно обжаловать.</li>
```

**6.** CEAR (неутверждённый источник) заменён на BOE (DA 21.9); отказ от ходатайства требуется после положительного решения, связь с TIE в декрете отсутствует. (count in current content: 1)

Old:
```html
<p>По данным CEAR, если испанские власти не получают ответ от иностранных органов о судимости в течение трёх месяцев, Управление по делам иностранцев требует от заявителя представить справку в срок 15 дней. [2]</p>

<p>Если заявитель этого не делает, заявление о проживании может быть признано отозванным. [2]</p>

<h3>Заявители, ходатайствующие о международной защите</h3>

<p>Рассматриваемое ходатайство о международной защите совместимо с легализацией до вынесения по ней положительного решения. [2]</p>

<p>После положительного решения заявитель должен отказаться от ходатайства о международной защите или от соответствующего обжалования, чтобы получить карточку иностранца (TIE). [2]</p>
```
New:
```html
<p>Если иностранные органы не направят справку о несудимости в течение трёх месяцев, испанская администрация требует от заявителя представить её в срок 15 дней. [2]</p>

<p>Если заявитель этого не делает, считается, что он отказался от заявления. [2]</p>

<h3>Заявители, ходатайствующие о международной защите</h3>

<p>Рассматриваемое ходатайство о международной защите совместимо с легализацией до вынесения по ней положительного решения. [2]</p>

<p>После положительного решения заявитель должен отозвать ходатайство о международной защите или поданную жалобу. [2]</p>
```

**7.** Два года требуются для всех видов arraigo, кроме семейного; регламент действует с 20 мая 2025 года. (count in current content: 1)

Old:
```html
<p>Для социальной укоренённости требуемый срок непрерывного пребывания, как правило, составляет два года. [3]</p>
```
New:
```html
<p>Регламент действует с 20 мая 2025 года. Все виды укоренённости, кроме семейной, как правило, требуют двух лет непрерывного пребывания в Испании. [3]</p>
```

**8.** Обращение на «Вы» (RU guide). (count in current content: 1)

Old:
```html
<p>В зависимости от вашего профиля могут применяться другие пути:
```
New:
```html
<p>В зависимости от Вашей ситуации могут применяться другие пути:
```

**9.** TIE в течение месяца; срок действия один год, право жить и работать; переход по статье 191; внутренняя ссылка. (count in current content: 1)

Old:
```html
<p>После выдачи разрешения необходимо подать заявление на TIE на условиях, установленных администрацией. [2]</p>

<p>Первоначальное разрешение действует ограниченное время, поэтому владельцу следует заранее подготовить переход к обычному виду на жительство. [2]</p>
```
New:
```html
<p>После выдачи разрешения необходимо подать заявление на TIE в течение одного месяца. [2][4] Чем TIE отличается от NIE, мы объясняем в статье о <a href="https://delaguialuzon.com/ru/blog/%D0%B7%D0%B5%D0%BB%D0%B5%D0%BD%D0%BE%D0%B9-%D0%BA%D0%B0%D1%80%D1%82%D0%BE%D0%B9-nie-%D0%B8-tie/">разнице между «зелёной картой», NIE и TIE</a>.</p>

<p>Первоначальное разрешение действует один год и даёт право жить и работать по найму или как самозанятый на всей территории Испании. В течение двух месяцев до окончания срока владелец может подать заявление о переходе на другое разрешение по регламенту (статья 191). [2][4]</p>
```

**10.** Обращение на «Вы». (count in current content: 1)

Old:
```html
от вашей трудовой или семейной ситуации.</p>
```
New:
```html
от Вашей трудовой или семейной ситуации.</p>
```

**11.** Отказ от ходатайства сформулирован как в DA 20 (без условия о TIE). (count in current content: 1)

Old:
```html
<li>Забыть отказаться от ходатайства об убежище или обжалования, когда это необходимо для получения TIE. [2]</li>
```
New:
```html
<li>Забыть отозвать ходатайство о международной защите или жалобу после предоставления легализации. [2]</li>
```

**12.** Вопросы FAQ как H3; ответы с официальными источниками; период в почте уже прошёл; точный ответ о трудовом договоре; формулировки вопросов не изменены. (count in current content: 1)

Old:
```html
<h4>Можно ли ещё подать заявление на экстраординарную легализацию?</h4>

<p>Нет, срок подачи истёк 30 июня 2026 года, продление не предоставлялось. [1][4]</p>

<h4>Что произойдёт, если по моему делу нет ответа через три месяца?</h4>

<p>Максимальный срок принятия решения составляет три месяца, а молчание администрации означает отказ. [4]</p>

<p>В этом случае следует проанализировать дело и рассмотреть возможные способы обжалования.</p>

<h4>До какого числа можно устранить недостатки в неполном деле?</h4>

<p>Период очного устранения недостатков в назначенных отделениях почты заканчивается 30 сентября 2026 года. [1][5]</p>

<h4>Требовался ли трудовой договор для подачи заявления?</h4>

<p>Трудовой договор на момент подачи заявления не требовался.</p>

<h4>Что делать, если я не успел подать заявление?</h4>

<p>Следует изучить обычные пути иммиграционного регламента, в частности различные виды arraigo, с учётом даты приезда, семейной ситуации и рода деятельности. [3]</p>

<h4>Совместима ли международная защита с легализацией?</h4>

<p>Да, до получения легализации; после этого для получения TIE требуется отказ от ходатайства. [2]</p>
```
New:
```html
<h3>Можно ли ещё подать заявление на экстраординарную легализацию?</h3>

<p>Нет, срок подачи истёк 30 июня 2026 года, продление не предоставлялось. [1]</p>

<h3>Что произойдёт, если по моему делу нет ответа через три месяца?</h3>

<p>Максимальный срок принятия решения составляет три месяца, а молчание администрации означает отказ. [2]</p>

<p>В этом случае следует проанализировать дело и рассмотреть возможные способы обжалования.</p>

<h3>До какого числа можно устранить недостатки в неполном деле?</h3>

<p>Очное устранение недостатков в уполномоченных отделениях почты было предусмотрено до 30 сентября 2026 года. При новом запросе соблюдайте срок (не более 15 дней) и способ ответа, указанные в уведомлении. [1][2]</p>

<h3>Требовался ли трудовой договор для подачи заявления?</h3>

<p>Нет. Для arraigo extraordinario связь с работой (прежняя работа, предложение о работе или декларация о самозанятости) была лишь одним из трёх возможных условий, наряду с проживанием с семьёй в Испании и уязвимым положением. Заявителям, ходатайствующим о международной защите, это условие выполнять не требовалось. [2][4]</p>

<h3>Что делать, если я не успел подать заявление?</h3>

<p>Следует изучить обычные пути иммиграционного регламента, в частности различные виды arraigo, с учётом даты приезда, семейной ситуации и рода деятельности. [3]</p>

<h3>Совместима ли международная защита с легализацией?</h3>

<p>Да, до положительного решения по легализации. После него заявитель должен отозвать ходатайство о международной защите или жалобу. [2]</p>
```

**13.** Удалены запрещённые/неутверждённые источники (CEAR, Civislex, Martínez Caballero Abogados); заменены на BOE RD 316/2026 и La Moncloa. (count in current content: 1)

Old:
```html
<li>CEAR, «Regularización extraordinaria de personas migrantes»: <a href="https://www.cear.es/sections-post/regularizacion-extraordinaria-2026/" target="_blank" rel="noopener">https://www.cear.es/sections-post/regularizacion-extraordinaria-2026/</a></li>
<li>BOE, Королевский декрет 1155/2024 от 19 ноября 2024: <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">https://www.boe.es/eli/es/rd/2024/11/19/1155</a></li>
<li>Civislex, «Regularización extraordinaria 2026: guía completa», обновлено 1 сентября 2026: <a href="https://www.civislex.com/regularizacion-extraordinaria-2026-guia-completa/" target="_blank" rel="noopener">https://www.civislex.com/regularizacion-extraordinaria-2026-guia-completa/</a></li>
<li>Martínez Caballero Abogados, «Regularización 2026 sin resolver»: <a href="https://martinezcaballeroabogados.com/antecedentes-penales/regularizacion-extraordinaria-2026-sin-resolver/" target="_blank" rel="noopener">https://martinezcaballeroabogados.com/antecedentes-penales/regularizacion-extraordinaria-2026-sin-resolver/</a></li>
```
New:
```html
<li>BOE, Королевский декрет 316/2026 от 14 апреля 2026 года о внесении изменений в Королевский декрет 1155/2024 (BOE-A-2026-8284): <a href="https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8284" target="_blank" rel="nofollow noopener">https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-8284</a></li>
<li>BOE, Королевский декрет 1155/2024 от 19 ноября 2024: <a href="https://www.boe.es/eli/es/rd/2024/11/19/1155" target="_blank" rel="noopener">https://www.boe.es/eli/es/rd/2024/11/19/1155</a></li>
<li>La Moncloa, Министерство включения, социального обеспечения и миграции, «Proceso de regularización migratoria extraordinaria: plazos y requisitos», 21 апреля 2026: <a href="https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/proceso-regularizacion-migratoria.aspx" target="_blank" rel="nofollow noopener">https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/paginas/2026/proceso-regularizacion-migratoria.aspx</a></li>
```

**14.** Обращение на «Вы» в блоке контактов. (count in current content: 1)

Old:
```html
проанализируют ваше дело,
```
New:
```html
проанализируют Ваше дело,
```

### Other fields

- **Title tag**: No change needed.
- **Excerpt** via `PUT /wp/v2/posts/23581` `excerpt` (221 chars): `Экстраординарная легализация в Испании по Королевскому декрету 316/2026 завершилась 30 июня 2026 года без продления. Поданные в срок заявления рассматриваются, а тем, кто не успел, доступны обычные пути, например arraigo.`
- **FAQPage schema** (`rank_math_schema_FAQPage`): replace `mainEntity` with the 6 visible questions so schema mirrors the page. Write path to be tested first (doc 07).

```json
[
 {
  "@type": "Question",
  "name": "Можно ли ещё подать заявление на экстраординарную легализацию?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Нет, срок подачи истёк 30 июня 2026 года, продление не предоставлялось."
  }
 },
 {
  "@type": "Question",
  "name": "Что произойдёт, если по моему делу нет ответа через три месяца?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Максимальный срок принятия решения составляет три месяца, а молчание администрации означает отказ. В этом случае следует проанализировать дело и рассмотреть возможные способы обжалования."
  }
 },
 {
  "@type": "Question",
  "name": "До какого числа можно устранить недостатки в неполном деле?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Очное устранение недостатков в уполномоченных отделениях почты было предусмотрено до 30 сентября 2026 года. При новом запросе соблюдайте срок (не более 15 дней) и способ ответа, указанные в уведомлении."
  }
 },
 {
  "@type": "Question",
  "name": "Требовался ли трудовой договор для подачи заявления?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Нет. Для arraigo extraordinario связь с работой (прежняя работа, предложение о работе или декларация о самозанятости) была лишь одним из трёх возможных условий, наряду с проживанием с семьёй в Испании и уязвимым положением. Заявителям, ходатайствующим о международной защите, это условие выполнять не требовалось."
  }
 },
 {
  "@type": "Question",
  "name": "Что делать, если я не успел подать заявление?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Следует изучить обычные пути иммиграционного регламента, в частности различные виды arraigo, с учётом даты приезда, семейной ситуации и рода деятельности."
  }
 },
 {
  "@type": "Question",
  "name": "Совместима ли международная защита с легализацией?",
  "acceptedAnswer": {
   "@type": "Answer",
   "text": "Да, до положительного решения по легализации. После него заявитель должен отозвать ходатайство о международной защите или жалобу."
  }
 }
]
```

## Open questions for Mike/the firm

1. **Three-month silence has now run for most files.** Applications filed by 30 Jun 2026 reached three months by 30 Sep, unless the period was suspended (subsanación request, foreign criminal-record request). Should the posts say that unresolved files are now deemed refused, and name the remedy and deadline (recurso de reposición/alzada or contencioso)? Legal judgement for Félix/Sonia; the 'decision can be challenged' line is currently unsourced (its sources were forbidden).
2. **Correos subsanación after 30 Sep.** No official extension found on 1 Oct. Confirm before publishing; the staged text says 'was scheduled until 30 September' and points readers to the channel in their notification.
3. **CEAR as a source.** It is an NGO that provides legal assistance; staged as removed (all its claims are in the BOE). Confirm whether NGOs count as 'legal-service providers'.
4. **FR title tag** on FR's top post (62,933 impressions, pos 5.4): keep the current one or move the focus keyword first? Staged as optional.
5. **FAQ schema rewrite**: the Rank Math schema write path was blocked before (WPVibe semicolon filter). Test on one post first.
6. **Update line date**: staged as '1 October 2026'; set it to the actual publish date.
7. **Legacy `_elementor_data`** remains on all four posts. If anyone opens them in Elementor, the old layout could overwrite the rewrite. Remove the meta (or set edit mode explicitly) after Mike's approval.
8. **ES 21398 was edited again at 12:22 on 1 Oct** (user 29), after the other three. Confirm nobody is still editing; re-check the MD5 before applying.
9. **RU CTA** has no contact-page link: confirm the RU contact URL. **ES/RU have almost no cluster siblings** (no ES/RU arraigo post): content gap.
10. **Not staged**: FR non-breaking-space typography (whole post), FR CTA heading in verb form, 0 sourced blockquotes on all four (target 2), H3 hook after the summary box. Also, the Link Whisper related-posts widget on FR outputs an EN post link and a Title Case FR title (plugin, outside post_content).

---

## Decision 2026-10-01 (Mike): no unsure claims, CTA instead

Do NOT state that silence now means refusal, nor which appeal or deadline applies. Wherever the staged
changes mention the 3-month deadline, silence, refusal or appeals, keep only what the BOE says
(decision within 3 months, RD 316/2026) and replace any interpretation with a short call to action in
the post's language, e.g.:

- FR: « Votre dossier a été déposé dans les délais et vous n'avez pas reçu de réponse ? Contactez notre
  équipe pour vérifier sa situation et les démarches possibles : +34 963 74 16 57 ·
  felix.delaguia@delaguialuzon.com »
- EN: "Filed on time and still waiting for an answer? Contact our team to check where your application
  stands and what you can do next: +34 963 74 16 57 · felix.delaguia@delaguialuzon.com"
- ES: «¿Presentó su solicitud en plazo y aún no tiene respuesta? Contacte con nuestro equipo para
  comprobar el estado de su expediente y las opciones disponibles: +34 963 74 16 57 ·
  felix.delaguia@delaguialuzon.com»
- RU: «Вы подали заявление в срок, но ответа ещё нет? Свяжитесь с нашей командой, чтобы проверить статус
  Вашего дела и возможные дальнейшие шаги: +34 963 74 16 57 · felix.delaguia@delaguialuzon.com»

The unsourced "a refusal can be appealed" line is removed in all four posts.
