# 25840 (FR) Cotisations autonomos 2026: fact check, 2026-10-06 (staged, nothing written to WordPress)

- URL: https://delaguialuzon.com/fr/blog/cotisations-autonomos-2026-baremes-reta/ (renders from `post_content`, 39 806 bytes, no Elementor).
- State read: post_modified 2026-10-06 15:38:57 (revision 28303, MD5 23abee85399ddad0d4a7f32492cce4ea). Someone scoped the CSS at 15:38 (global `<style>` replaced by an `.article-wrapper` block); the text is unchanged since 2026-09-15. The old global-selector block is still in the page under `<style media="not all">` (dead code, remove it).
- WPML: trid 3076 holds only this FR post (no ES/EN/RU sibling). Same claims sit in non-linked posts: ES 27855 (80 €, "15 tramos 200 a ~590 €", 88,56 €, cuota cero in Valencia), ES 24717 and FR 24773 (80 € "ya en vigor", "congelación en tramos bajos"), EN 4160 ("up to €590+"), EN 25362 ("15 brackets €230 to €590", tarifa plana "under Law 31/2022"). Not edited.
- État du droit au 6 octobre 2026. 72 claims logged in `data/factcheck/25840.csv`.

## Verdict counts (72 rows)

| OK | UPDATE | OUTDATED | UNVERIFIABLE | WRONG |
|---|---|---|---|---|
| 23 | 23 | 1 | 18 | 7 |

## Sources opened and read (all verified 2026-10-06)

- [Orden PJC/297/2026, BOE-A-2026-7296](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296): art. 18 (bases, tables, rates), art. 37 (cese 0,90 %, FP 0,10 %).
- [RDL 3/2026, BOE-A-2026-2548](https://www.boe.es/buscar/act.php?id=BOE-A-2026-2548) art. 3.1, 3.2, 3.4; [validation by Congress, BOE-A-2026-4668](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-4668) (26/02/2026).
- [RDL 13/2022, BOE-A-2022-12482](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482): DT 1a, DT 5a, DA 1a, preamble (80 %).
- [LETA, BOE-A-2007-13409](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409): arts. 30, 38, 38 ter. [LGSS, BOE-A-2015-11724](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724): arts. 30, 209, 308, DT 43a. [RD 504/2022, BOE-A-2022-10677](https://www.boe.es/buscar/act.php?id=BOE-A-2022-10677): art. 43 bis. [RD 126/2026, BOE-A-2026-3815](https://www.boe.es/buscar/act.php?id=BOE-A-2026-3815). [Ley 31/2022 (LPGE 2023), BOE-A-2022-22128](https://www.boe.es/buscar/act.php?id=BOE-A-2022-22128): searched for a general cuota reducida amount, none.
- Seguridad Social: [new contribution system page](https://www.seg-social.es/wps/portal/wss/internet/HerramientasWeb/9d2fd4f1-ab0f-42a6-8d10-2e74b378ee24); Importass [annual regularisation](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Consulta+de+pagos+y+deudas/PagosDevoluciones_/RegularizacionRETA), its [guide section](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/Trabajo+Autonomo/guia?urile=wcm:path:/wps/wcm/connect/importass/importass_contenidos/otras_secciones/regularizacion), [alta page](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Altas+y+afiliacion+de+trabajadores/Alta_trabajo_autonomo).
- Generalitat: [TRRETA procedure](https://sede.gva.es/en/detall-tramit?id_proc=18856), [press release of 18/09/2026](https://comunica.gva.es/es/detalle?id=415138270&site=373409432). La Moncloa [07/08/2017](https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/mempleo/Paginas/2017/070814autonomos.aspx) (tarifa plana origin).

## The 10 most important corrections

1. **Tarifa plana "80 €" (title/H1, TL;DR, section 3 H2, blockquote, info box, examples, FAQ "Oui")**: UNVERIFIABLE for 2026. DT 5a RDL 13/2022: "Durante el periodo comprendido entre los años 2023 y 2025, la cuantía de la cuota reducida ... será de 80 euros mensuales" and "A partir del año 2026, el importe de dichas cuotas será fijado por la Ley de Presupuestos Generales del Estado de cada ejercicio". No LPGE 2026 exists (RDL 3/2026 DA 1a only keeps titles IV and VIII of the 2023 LPGE, which has no general cuota reducida amount). The Seguridad Social page itself says "Durante el periodo 2023-2025". Same decision as FR 8655, EN 2564, RU 24774: legal rule plus CTA, no figure. The title/H1 and Rank Math must lose "80 €".
2. **"88,64 € MEI inclus"**: no approved source (non-official sites give 88,56 and 88,64). Remove everywhere.
3. **Tranche split WRONG**: the post says "barème réduit = tranches 1 à 6 (jusqu'à 1 700 €), général = 7 à 15". Orden art. 18.1: reduced table = 3 tramos (up to 1 166,70 €), general table = 12 tramos. Column "Barème" also mislabels tranches 4 to 6.
4. **Table cuotas**: tranches 1 to 10 are base minimale x 30,60 % (WITHOUT MEI) while the page's own rate box says 31,50 %; tranches 11 to 15 are WRONG (465, 530, 590, 590, 590). Correct with MEI: 205,88 / 226,47 / 267,65 / 299,56 / 302,65 / 302,65 / 360,29 / 380,88 / 401,47 / 427,21 / 452,94 / 478,68 / 504,41 / 545,59 / 607,35 €.
5. **"Cuotas gelées, de 200 € à 590 €"**: only the tables of bases are frozen (RDL 3/2026 art. 3.4), the maximum base of tramos 11 and 12 rises to 5 101,20 € (4 909,50 € in 2025) and the MEI rises to 0,90 %. Minimum cuota with MEI: 205,88 € to 607,35 €.
6. **MEI "ajoutant entre 6 € et 46 €"**: WRONG. 6 to 46 € is the total MEI at 0,9 % (5,88 to 45,91 €); the rise from 0,8 % to 0,9 % is 0,65 € to 5,10 € a month.
7. **Invented political narrative** ("échec des négociations", "faute de majorité parlementaire pour les hausses proposées"): not in any official text. RDL 3/2026 gives the official reasons: LPGE 2026 delayed (automatic prorogation of the 2023 LPGE) and RDL 16/2025 not validated (repealed 28/01/2026).
8. **Regularisation section**: "avant le 30 avril 2026" is an expired date presented as current (OUTDATED); "environ 30 jours" should be "jusqu'au dernier jour du mois suivant la notification" (LGSS 308.1.c regla 4a); "10 jours ... avant qu'elle ne produise effet" is not what Importass says (10 natural days to read the notice); the "recurso de alzada, art. 121 Ley 39/2015, un mois" is not on any official page read (UNVERIFIABLE, legal call); "renoncer au remboursement" is in fact the official option to maintain a higher base; "régularisation se complique" if no IRPF is WRONG (art. 308.1.c regla 5a: definitive base = minimum base of group 7).
9. **Bonuses**: "bonification de 50 % pour la garde d'un enfant de moins de 12 ans" is WRONG (art. 30 LETA: 100 % of the CC cuota up to 12 months, only with a hired worker, 50 % if the hire is part-time); "se cumule avec la tarifa plana" is unsupported; "à jour envers AEAT et Sécurité sociale, sans dettes" is not a condition of art. 38 ter LETA.
10. **Valencia**: the cuota cero list (Madrid, Andalousie, Galice, Canaries, Castille-La Manche) is unverified, and "la Communauté valencienne n'a pas encore ... de cuota cero" is now unsafe: the press reports an announcement by the Generalitat president on 28/09/2026 (2 years, 4 for young people), not in force and not found on an official GVA page. State neither; CTA; re-check line added to TASKS.md.

## Proposed French wording (inline-linked, to be written by dl-blog-editor; every link opened)

Anchors below carry `target="_blank" rel="nofollow noopener"` when written.

### Title, H1, meta
- H1: Cotisations autonomos 2026 en Espagne : 15 tranches RETA, tarifa plana et régularisation TGSS (93 characters; the slug keeps the year and stays untouched without a 301 and Mike's approval).
- Rank Math title (58): `Cotisations autonomos 2026 : tranches RETA et tarifa plana`
- Rank Math description (144): `Cotisations autonomos 2026 en Espagne : 15 tranches RETA de 205,88 € à 607,35 €, tarifa plana, MEI et régularisation TGSS. Contactez le cabinet.`

### TL;DR (H2 `Cotisations autonomos 2026 : les points essentiels`)
1. En 2026, les cotisations des autónomos suivent <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296">15 tranches de rendement net, 3 dans le barème réduit et 12 dans le barème général (Orden PJC/297/2026)</a>, avec une cuota minimale de 205,88 € à 607,35 € par mois, MEI inclus, calculée sur la base minimale de chaque tranche.
2. Le <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-2548">Real Decreto-ley 3/2026 (article 3.4)</a> maintient pour 2026 les tables de bases de 2025 et relève seulement la base maximale des tramos 11 et 12 du barème général, fixée à 5 101,20 € par mois.
3. Le taux total est de 31,50 % en 2026 : 28,30 % pour les contingences communes, 1,30 % pour les contingences professionnelles, 0,90 % pour la cessation d'activité, 0,10 % pour la formation professionnelle et 0,90 % pour le MEI (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296">article 18 et article 37 de l'Orden PJC/297/2026</a>).
4. Le MEI passe de 0,80 % en 2025 à 0,90 % en 2026 (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724">disposition transitoire 43 de la LGSS</a>), soit de 0,65 € à 5,10 € de plus par mois selon la base choisie.
5. La tarifa plana (cuota reducida) de l'<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409">article 38 ter de la Ley 20/2007</a> s'applique pendant 12 mois et se prolonge de 12 mois si le rendement net annuel reste inférieur au SMI annuel ; son montant est confirmé à 80 € pour 2023 à 2025 seulement, et celui de 2026 doit être confirmé auprès du cabinet.
6. La TGSS régularise chaque année vos bases d'après les rendements transmis par les administrations fiscales : <a href="https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Consulta+de+pagos+y+deudas/PagosDevoluciones_/RegularizacionRETA">vous disposez de 10 jours naturels pour lire la notification</a>, et tout paiement dû se règle au plus tard le dernier jour du mois suivant la notification pour éviter le recargo.
7. Vous pouvez changer de base de cotisation jusqu'à six fois par an, avec effet au 1er mars, 1er mai, 1er juillet, 1er septembre, 1er novembre ou 1er janvier selon la date de la demande (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2022-10677">article 43 bis du règlement de cotisation, modifié par le Real Decreto 504/2022</a>).

### Intro (replaces paragraphs 2 and 3)
Pour 2026, les tables de bases de cotisation des autónomos restent celles de 2025. Le <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-2548">Real Decreto-ley 3/2026</a> les reconduit parce que la loi de finances 2026 n'est pas adoptée (la loi de finances 2023 est prorogée) et que le Real Decreto-ley 16/2025 n'a pas été validé par le Congrès ; le Congrès a <a href="https://www.boe.es/buscar/doc.php?id=BOE-A-2026-4668">validé le Real Decreto-ley 3/2026 le 26 février 2026</a>.

Les cotisations ne sont toutefois pas gelées. Le MEI passe de 0,80 % à 0,90 % et la base maximale des tramos 11 et 12 du barème général (tranches 14 et 15 dans ce tableau) est portée de 4 909,50 € à 5 101,20 €. Le barème 2026 figure à l'<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296">article 18 de l'Orden PJC/297/2026</a>, en vigueur le 1er avril 2026 avec effet au 1er janvier 2026.

### Section 1 (replacement sentences)
- Avant 2023, <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482">environ 80 % des indépendants choisissaient la base minimale</a>, selon le préambule du Real Decreto-ley 13/2022. Le nouveau système, en vigueur depuis le 1er janvier 2023, se déploie sur neuf ans au plus (disposition transitoire 1) et, à partir du 1er janvier 2032, les bases dépendront des rendements nets annuels (disposition additionnelle 1).
- Rate box: total `31,50 %` (delete "approximatif").
- Rendement net: le rendement pris en compte est le rendement net d'IRPF, majoré des cotisations de Sécurité sociale payées, auquel s'applique une <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724">déduction de 7 % pour dépenses générales, ramenée à 3 % pour les autónomos societarios (article 308.1.c de la LGSS)</a>. Selon la <a href="https://www.seg-social.es/wps/portal/wss/internet/HerramientasWeb/9d2fd4f1-ab0f-42a6-8d10-2e74b378ee24">Sécurité sociale</a>, le taux de 3 % vise l'administrateur d'une société de capitaux détenant au moins 25 % du capital et l'associé détenant au moins 33 %, après 90 jours d'alta.

### Section 2: tranches (replaces the intro and the table)
Le barème comprend <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296">une table réduite de 3 tranches (rendement net jusqu'à 1 166,70 € par mois) et une table générale de 12 tranches (à partir de 1 166,70 €)</a>. La cuota minimale ci-dessous est calculée en appliquant le taux de 31,50 % à la base minimale de chaque tranche.

| Tranche | Rendement net mensuel | Barème | Base minimale | Base maximale | Cuota minimale (31,50 %) |
|---|---|---|---|---|---|
| 1 | jusqu'à 670 € | Réduit | 653,59 € | 718,94 € | 205,88 € |
| 2 | 670 € à 900 € | Réduit | 718,95 € | 900,00 € | 226,47 € |
| 3 | 900 € à 1 166,70 € | Réduit | 849,67 € | 1 166,70 € | 267,65 € |
| 4 | 1 166,70 € à 1 300 € | Général | 950,98 € | 1 300,00 € | 299,56 € |
| 5 | 1 300 € à 1 500 € | Général | 960,78 € | 1 500,00 € | 302,65 € |
| 6 | 1 500 € à 1 700 € | Général | 960,78 € | 1 700,00 € | 302,65 € |
| 7 | 1 700 € à 1 850 € | Général | 1 143,79 € | 1 850,00 € | 360,29 € |
| 8 | 1 850 € à 2 030 € | Général | 1 209,15 € | 2 030,00 € | 380,88 € |
| 9 | 2 030 € à 2 330 € | Général | 1 274,51 € | 2 330,00 € | 401,47 € |
| 10 | 2 330 € à 2 760 € | Général | 1 356,21 € | 2 760,00 € | 427,21 € |
| 11 | 2 760 € à 3 190 € | Général | 1 437,91 € | 3 190,00 € | 452,94 € |
| 12 | 3 190 € à 3 620 € | Général | 1 519,61 € | 3 620,00 € | 478,68 € |
| 13 | 3 620 € à 4 050 € | Général | 1 601,31 € | 4 050,00 € | 504,41 € |
| 14 | 4 050 € à 6 000 € | Général | 1 732,03 € | 5 101,20 € | 545,59 € |
| 15 | plus de 6 000 € | Général | 1 928,10 € | 5 101,20 € | 607,35 € |

Note under the table: Bases et tranches de l'<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296">Orden PJC/297/2026</a> ; tables de 2025 reconduites par l'<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-2548">article 3.4 du Real Decreto-ley 3/2026</a>. Les cuotas sont un calcul du cabinet (base minimale x 31,50 %) ; pour votre cas, le <a href="https://www.seg-social.es/wps/portal/wss/internet/HerramientasWeb/9d2fd4f1-ab0f-42a6-8d10-2e74b378ee24">simulateur de la Sécurité sociale</a> fait foi. Cuota maximale à la base maximale de 5 101,20 € : 1 606,88 €.

### Section 3 (tarifa plana): H2 `La tarifa plana pour les nouveaux autónomos` (no amount)
La tarifa plana, officiellement <em>cuota reducida</em>, est régie par l'<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409">article 38 ter de la Ley 20/2007</a> : une cuota réduite s'applique à partir de la date d'effet de l'alta et pendant les douze mois complets suivants, sans condition de revenu, puis pendant douze mois de plus si le rendement net annuel est inférieur au SMI annuel. Elle existe sous une première forme depuis <a href="https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/mempleo/Paginas/2017/070814autonomos.aspx">février 2013</a> ; le régime actuel date du 1er janvier 2023.

Le montant de la cuota reducida a été fixé à 80 € par mois pour <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482">2023 à 2025 (disposition transitoire 5 du Real Decreto-ley 13/2022)</a> ; à partir de 2026, il doit être fixé par la loi de finances de l'État. Nous n'avons pas trouvé de texte officiel fixant le montant applicable en 2026 : contactez le cabinet pour confirmer le montant et les conditions qui s'appliquent à votre alta.

Conditions (list, 2 items kept): (1) ne pas avoir été en alta au RETA pendant les deux années précédentes, trois ans si vous avez déjà bénéficié de la réduction ; (3) demander la réduction au moment de l'alta. Delete "à jour de ses obligations ... sans dettes". Warning box (loss on baja, three years): keep, link art. 38 ter.4.

Prolongation: Une prolongation de douze mois est possible si le rendement net annuel prévu est inférieur au SMI annuel (le <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-3815">Real Decreto 126/2026</a> fixe le SMI à 1 221 € par mois, soit 17 094 € sur l'année) ; la demande s'accompagne d'une déclaration de rendements prévus, via Importass. Les personnes avec un handicap d'au moins 33 %, les victimes de violence de genre et les victimes du terrorisme bénéficient de 24 mois, puis de 36 mois (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409">article 38 ter, alinéa 10</a>).

Replace the two bonus paragraphs: La <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409">bonification de 100 % pendant le congé de naissance, d'adoption ou de risque pendant la grossesse (article 38)</a> et la <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409">bonification de 100 % de la cuota pour la garde d'un enfant de moins de douze ans, limitée à douze mois et conditionnée à l'embauche d'un salarié (article 30)</a> sont des dispositifs distincts. Pour savoir si vous pouvez les combiner avec la tarifa plana, contactez le cabinet.

Info box "Tarifa plana vs cuota cero": remove the list of regions and the Valencian statement. Proposed: La cuota cero est une aide régionale qui varie selon les communautés autonomes et change chaque année. Pour savoir si une aide existe dans votre communauté au moment de votre alta, contactez le cabinet.

### Section 4 (regularisation)
- La TGSS regularise vos bases à partir des rendements que lui transmettent les administrations fiscales (AEAT et administrations forales) ; <a href="https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Consulta+de+pagos+y+deudas/PagosDevoluciones_/RegularizacionRETA">la notification arrive par le service de notifications télématiques et le portail DEHú, vous disposez de 10 jours naturels pour la lire</a>.
- Trop cotisé: <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724">la TGSS rembourse d'office, sans intérêts, la part qui dépasse la cuota correspondant à la base maximale de votre tranche réelle, avant le 30 avril de l'année suivant la communication des rendements (article 308.1.c de la LGSS)</a> ; vos coordonnées bancaires doivent être à jour.
- Sous-cotisé: vous réglez la différence jusqu'au dernier jour du mois suivant la notification, sans intérêts ni recargo ; au-delà, un <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724">recargo de 10 % le premier mois, puis de 20 % (article 30 de la LGSS)</a> s'applique.
- Neutre: aucune régularisation n'a lieu si la base définitive est comprise entre la base minimale et la base maximale de votre tranche réelle (article 308.1.c, règle 3).
- Delete: "l'exercice 2024 est notifié au cours de 2026", "avant le 30 avril 2026", "avant qu'elle ne produise effet", and the recurso de alzada sentence. Add: Pour savoir comment contester une résolution de régularisation, contactez le cabinet.
- Option to keep a higher base: Si vous avez cotisé sur une base supérieure à celle correspondant à vos rendements depuis le 31 décembre 2022, <a href="https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Consulta+de+pagos+y+deudas/PagosDevoluciones_/RegularizacionRETA">vous pouvez opter pour le maintien de cette base jusqu'au dernier jour du mois suivant la notification, et annuler votre choix avant la fin de ce délai</a>. Delete "dont le calcul dépend largement des bases des dernières années" ; add: Pour mesurer l'effet sur votre future pension, contactez le cabinet.
- Practice list: item 3 keep only "Cotiser systématiquement au minimum réduit vos prestations futures" (Seg. Social: "a mayor base, mayor será la prestación"), delete "dernière décennie". Item 4 becomes: "Oublier la déclaration d'IRPF : sans déclaration, ou sans revenus déclarés en estimation directe, la base définitive est la base minimale du groupe 7 du régime général (article 308.1.c, règle 5 de la LGSS)."

### Section 5 and examples
- Changer de base: `jusqu'à six fois par an via Importass`, effective dates 1er mars (demande du 1er janvier à fin février), 1er mai (mars-avril), 1er juillet (mai-juin), 1er septembre (juillet-août), 1er novembre (septembre-octobre), 1er janvier suivant (novembre-décembre). Delete the "certificat numérique, DNIe ou Cl@ve" list.
- Examples table: graphiste 1 800 €, tranche 7, cuota 360,29 € ; consultant IT 3 000 €, tranche 11, cuota 452,94 € ; delete the tarifa plana row or write "Nouveau consultant (1re année) : réduction de l'article 38 ter, montant à confirmer avec le cabinet". Mention in the note: "calcul sur la base minimale, MEI inclus".
- Practical case: la TGSS réclame la différence entre vos cotisations provisoires et la cuota de la base minimale de la tranche réelle ; en cas de surestimation, elle ne rembourse que ce qui dépasse la cuota de la base maximale de la tranche.

### Section 8 (Valencia): rewrite, no marketing claims
Delete the "atouts" paragraph (fiscalité compétitive, expatriés, marché locatif). Replace the aid paragraph: La Generalitat Valenciana gère l'aide <a href="https://sede.gva.es/en/detall-tramit?id_proc=18856">TRRETA, destinée aux autónomos domiciliés dans une commune de moins de 5 000 habitants</a> : la convocation de 2025 (DOGV n° 10123 du 4 juin 2025, demandes du 5 au 18 juin 2025) est close et ses montants vont de 2 600 € à 3 000 €. D'autres aides pour autónomos sont en préparation ou en cours ; contactez le cabinet pour savoir lesquelles s'appliquent à votre situation.

### Contact box, FAQ, footer
- Contact name: `Delaguía y Luzón, cabinet juridique franco-espagnol à Valence` (no em dash).
- FAQ 1: La cuota minimale de la tranche 1 est de 205,88 € par mois, MEI inclus, pour un rendement net inférieur ou égal à 670 €.
- FAQ 2: question `Quel est le montant de la tarifa plana en 2026 ?` ; answer: Le montant de 80 € est confirmé pour 2023 à 2025 ; à partir de 2026, il doit être fixé par la loi de finances. Contactez le cabinet pour confirmer le montant applicable à votre alta.
- FAQ 3: ... la différence se règle jusqu'au dernier jour du mois suivant la notification, sans recargo.
- FAQ 4: keep "jusqu'à six fois par an, via Importass" (drop the identification list). FAQ 5: link the Orden. FAQ 6: question `Puis-je maintenir une base supérieure après la régularisation ?`
- Footer: `État du droit au 6 octobre 2026.` Delete the "Correction factuelle" sentence and the em dash.

## Anything that should become a "contactez le cabinet" CTA
1. Tarifa plana amount and conditions for an alta in 2026 (TL;DR 5, section 3, info box, FAQ 2).
2. Cumulation of the tarifa plana with the art. 30 and art. 38 bonuses.
3. Appeal route against a regularisation resolution.
4. Effect of a higher base on the future pension.
5. Regional aid (cuota cero in other regions, the announced Valencian cuota cero, TRRETA and future calls).

## Open questions for Félix and Sonia (via Mike)
1. **Tarifa plana 2026.** Does the firm have confirmation from the TGSS (or an official text we missed) that 80 € applies to altas made in 2026? Secondary sites say yes; the official texts we can quote say 2023 to 2025 only. Until answered, the post carries the legal rule plus a CTA, like FR 8655, EN 2564 and RU 24774. Also: is the MEI added on top of the reduced cuota (non-official figures 88,56 and 88,64)?
2. **Valencian cuota cero announced 28/09/2026.** Mention it (as an announcement, with the date and no requirements) or leave it out until the DOGV text exists? Proposed: leave out, CTA.
3. **Appeal route** for a TGSS regularisation resolution (the post said recurso de alzada, one month, art. 121 Ley 39/2015): to be confirmed by a lawyer before any statement.
4. **"Societario" 3 % deduction** wording: Seguridad Social states administrator with at least 25 % and partner with at least 33 % of a capital company; confirm this is the wording the firm wants to publish.
5. **Pension advice** (higher base): the post's "dernière décennie" is not supported (art. 209 LGSS uses 348 months and the 324 best bases, with transitional rules not checked); confirm what the firm wants to say.
6. **Slug** `cotisations-autonomos-2026-baremes-reta` carries the year (house rule: never). Do not change without a 301 and Mike's approval; noted only.

## House-rule violations seen in passing
- Zero inline source links (BOE ids are plain text) and zero internal links in the body (rule: 3 to 8 including a practice-area page and a sibling post).
- TL;DR H2 is "Points clés" (rule: `<keyword> : les points essentiels`); bullets 3 and 6 are not self-contained facts.
- FAQ built with `<details>` (rule: H3 questions, no `<details>`); no FAQPage schema on the live page (only the site-wide LegalService JSON-LD).
- Em dashes: contact box name (`Delaguía y Luzón — Cabinet ...`) and the footer. Decorative glyphs in text and CSS (✓ ✕ → −) read as emoji-like symbols.
- Rank Math title uses a pipe (`... | RETA`); Rank Math description has `Delaguía &amp; Luzón` (brand with `&`). The site-wide LegalService schema also reads "Delaguía & Luzón" (wp-admin / Rank Math, outside the Scope Gate).
- Dead `<style media="not all">` block with global selectors (`*`, `body`, `h2`, `p`, `a`, `table`, `ul`) still in the content after the 15:38 scoping edit.
- Visible footer "Dernière mise à jour : juillet 2026 ... Correction factuelle ..." (internal note).
- Marketing section "L'avantage de la Communauté valencienne" with unsourced claims; "Cabinet établi" claims are fine ("depuis 1960" is correct, no "65 ans", no free-consultation wording, phone and email correct).
- Not found: emojis proper, `&` in the body, "65 ans", "consultation gratuite".

## Re-checks added to TASKS.md (2026-10-06)
See the new line under section 4: the tarifa plana 2026/2027 amount (LPGE or a royal decree-law), the bill derived from RDL 3/2026 (amendments to art. 3.4), the 2027 contribution order with the MEI at 1,00 %, and the Valencian cuota cero text.
