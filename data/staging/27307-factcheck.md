# 27307 FR fact-check: four claims (staged, applied 2026-10-01 (7 edits incl. TIE qualifier, verified live))

Post: "Résidence en Espagne : les différentes voies d'accès", https://delaguialuzon.com/fr/blog/residence-en-espagne-voies-acces/  
Requested by Mike, 2026-10-01 ("fact-check the 4 claims on 27307"). Checked by dl-fact-checker on 2026-10-01. **Nothing has been written to WordPress.**

## Baseline

- Live page fetched 2026-10-01 (Last-Modified 16:17:44 GMT). The extracted body text is identical to the 16:14 copy.
- `_elementor_data` in DB: md5 `9076eece6c734c87b549ea569914fe63`, 33,332 bytes, `post_modified` 2026-09-30 16:44:13. It is byte-identical to scratchpad `p27307/sim.json`, and every snippet below comes from that version. **Re-read the meta before applying; if the md5 differs, rebuild the snippets.**
- WPML: trid 3374 contains FR 27307 only. There are no siblings, so there is nothing to propagate.
- The page has no FAQPage schema, and `rank_math_description` does not carry these claims. `post_content` mirrors the Elementor HTML and is regenerated on save.
- The AISA `fact_check` call failed ("No OpenRouter API key configured"). All verdicts rest on the BOE consolidated texts, read directly.
- Simulated result with all 6 replacements: valid JSON, 37,941 bytes, md5 `bf221abbcd8f63e4025a3e0747b603d1` (scratchpad `p27307/fc_sim.json`; the snippet pairs are in `p27307/fc_edits.json`). Each old snippet occurs exactly once.

## Escalations (Mike, to Félix/Sonia)

1. **Golden Visa scope.** The heading of Ley 14/2013 DT 2ª reads "inversores por adquisición de bienes inmuebles", but the text covers "visados y autorizaciones para inversores" in general. Whether it covers non-real-estate investors (public debt, shares, deposits, business projects) is a legal call. The proposal states only the text of the provision, gives no end date (the law sets none) and adds a CTA.
2. **Positive silence.** Ley 14/2013 art. 76.1 says an unresolved UGE application "se entenderá estimada por silencio administrativo". C2a states this literally and follows it with a CTA. If the partners prefer not to mention silence, delete the clause "; à défaut, la loi la répute accordée (...)" from C2a.
3. **Appointment vs request.** The law requires the TIE to be *requested* within one month. It does not require an appointment to be held within 30 days. No source says how a late cita previa is treated in practice. The proposal states the legal obligation and adds a CTA.

## Related findings (outside the four claims, not staged)

- Ley 14/2013 art. 75.4 says visas issued under that law (including the digital nomad visa) authorise residence "sin necesidad de tramitar la tarjeta de identidad de extranjero". The procedure step "Demande de la TIE : dans le mois suivant l'entrée..." presents the TIE as universal. C2c already says "Lorsque la TIE est exigée". Consider adding the same qualifier to that step, with a link to art. 75.4.
- T-10 (Golden Visa): the TL;DR bullet, the intro sentence and "Ce qui a changé pour 2026" are dated historical mentions and comply. Only the FAQ sentence (C1) needed a fix.
- Unsourced figures seen in passing: "fenêtre de 90 jours pour entrer en Espagne", "renouvelable jusqu'à un total de cinq ans" and "34 188 € (200 % du SMI en 2026)". Queue them for a T-11 pass.

## C1: UPDATE

**Location:** FAQ, H3 "Qu'est-il advenu du Golden Visa ?"  
**Current wording (live):** « Il a fermé aux nouveaux candidats le 3 avril 2025. Les titulaires existants conservent leurs droits. Les voies alternatives sont le visa non lucratif et le visa nomade numérique. »

**Finding:** Ley 14/2013 DT 2a (added by LO 1/2025 DF 21a.3, in force 3 Apr 2025): investor visas/authorisations valid on 3 Apr 2025 keep validity for the period issued; renewals processed under the rules in force at the date of the initial authorisation. No end date set. DT 1a: applications filed before 3 Apr 2025 resolved under old rules. Scope (DT 2a heading says "por adquisicion de bienes inmuebles", body says "visados y autorizaciones para inversores") = legal call, escalated.

**Sources:** https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#dt-3 , https://www.boe.es/buscar/act.php?id=BOE-A-2025-76#df-21

**Proposed FR (decoded HTML):**

```html
<p>Il a fermé aux nouvelles demandes le 3 avril 2025. Selon la <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#dt-3" target="_blank" rel="nofollow noopener">disposition transitoire deuxième de la loi 14/2013, ajoutée par la loi organique 1/2025</a>, les visas et autorisations d'investisseur en cours de validité à cette date restent valables pour la durée pour laquelle ils ont été délivrés, et leurs demandes de renouvellement sont instruites selon les règles en vigueur à la date de l'autorisation initiale. Pour savoir comment ce régime s'applique à votre titre, contactez-nous pour confirmer votre situation au <a href="tel:+34963741657">+34 963 74 16 57</a> ou à <a href="mailto:felix.delaguia@delaguialuzon.com">felix.delaguia@delaguialuzon.com</a>. Les voies alternatives sont le visa non lucratif et le visa nomade numérique.</p>
```

**Old snippet as stored in `_elementor_data` (JSON-escaped, occurs once):**

```
<p>Il a ferm\u00e9 aux nouveaux candidats le 3 avril 2025. Les titulaires existants conservent leurs droits. Les voies alternatives sont le visa non lucratif et le visa nomade num\u00e9rique.<\/p>
```

**New snippet (JSON-escaped):**

```
<p>Il a ferm\u00e9 aux nouvelles demandes le 3\u00a0avril 2025. Selon la <a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2013-10074#dt-3\" target=\"_blank\" rel=\"nofollow noopener\">disposition transitoire deuxi\u00e8me de la loi 14\/2013, ajout\u00e9e par la loi organique 1\/2025<\/a>, les visas et autorisations d'investisseur en cours de validit\u00e9 \u00e0 cette date restent valables pour la dur\u00e9e pour laquelle ils ont \u00e9t\u00e9 d\u00e9livr\u00e9s, et leurs demandes de renouvellement sont instruites selon les r\u00e8gles en vigueur \u00e0 la date de l'autorisation initiale. Pour savoir comment ce r\u00e9gime s'applique \u00e0 votre titre, contactez-nous pour confirmer votre situation au <a href=\"tel:+34963741657\">+34 963 74 16 57<\/a> ou \u00e0 <a href=\"mailto:felix.delaguia@delaguialuzon.com\">felix.delaguia@delaguialuzon.com<\/a>. Les voies alternatives sont le visa non lucratif et le visa nomade num\u00e9rique.<\/p>
```

## C2a: UNVERIFIABLE

**Location:** Box at the end of H2 "Visa entrepreneur et visa startup"  
**Current wording (live):** « Délai indicatif : les demandes de visa nomade numérique traitées via la procédure accélérée prennent généralement 20 à 30 jours ouvrés pour les dossiers complets, bien que les délais varient selon le consulat. »

**Finding:** No official source gives real-world processing times; remove. Legal maxima: consular visa under Ley 14/2013 = 10 dias habiles (art. 75.5, except Visa Code art. 22 consultation); UGE residence authorisation = 20 dias from electronic filing, positive silence (art. 76.1); dias = habiles (Ley 39/2015 art. 30.2). Passage conflates consulate and UGE.

**Sources:** https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a75 , https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a76 , https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565#a30

**Proposed FR (decoded HTML):**

```html
<p style="margin:0;"><strong style="color:#708473;">Délais légaux :</strong> pour un visa relevant de la loi 14/2013, comme le visa nomade numérique, le consulat doit statuer dans les 10 jours ouvrés, sauf consultation préalable prévue par le code des visas (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a75" target="_blank" rel="nofollow noopener">article 75.5 de la loi 14/2013</a>). Une autorisation de séjour demandée depuis l'Espagne auprès de l'UGE doit être résolue dans les 20 jours suivant le dépôt électronique ; à défaut, la loi la répute accordée (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a76" target="_blank" rel="nofollow noopener">article 76.1 de la loi 14/2013</a>). Ces jours se comptent en jours ouvrés, conformément à l'<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565#a30" target="_blank" rel="nofollow noopener">article 30.2 de la loi 39/2015 sur la procédure administrative</a>. Il s'agit de délais maximaux fixés par la loi, et non de délais constatés : pour estimer le calendrier de votre dossier, contactez-nous pour confirmer votre situation au <a href="tel:+34963741657">+34 963 74 16 57</a> ou à <a href="mailto:felix.delaguia@delaguialuzon.com">felix.delaguia@delaguialuzon.com</a>.</p>
```

**Old snippet as stored in `_elementor_data` (JSON-escaped, occurs once):**

```
<p style=\"margin:0;\"><strong style=\"color:#708473;\">D\u00e9lai indicatif :<\/strong> les demandes de visa nomade num\u00e9rique trait\u00e9es via la proc\u00e9dure acc\u00e9l\u00e9r\u00e9e prennent g\u00e9n\u00e9ralement 20 \u00e0 30 jours ouvr\u00e9s pour les dossiers complets, bien que les d\u00e9lais varient selon le consulat.<\/p>
```

**New snippet (JSON-escaped):**

```
<p style=\"margin:0;\"><strong style=\"color:#708473;\">D\u00e9lais l\u00e9gaux\u00a0:<\/strong> pour un visa relevant de la loi 14\/2013, comme le visa nomade num\u00e9rique, le consulat doit statuer dans les 10\u00a0jours ouvr\u00e9s, sauf consultation pr\u00e9alable pr\u00e9vue par le code des visas (<a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2013-10074#a75\" target=\"_blank\" rel=\"nofollow noopener\">article 75.5 de la loi 14\/2013<\/a>). Une autorisation de s\u00e9jour demand\u00e9e depuis l'Espagne aupr\u00e8s de l'UGE doit \u00eatre r\u00e9solue dans les 20\u00a0jours suivant le d\u00e9p\u00f4t \u00e9lectronique ; \u00e0 d\u00e9faut, la loi la r\u00e9pute accord\u00e9e (<a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2013-10074#a76\" target=\"_blank\" rel=\"nofollow noopener\">article 76.1 de la loi 14\/2013<\/a>). Ces jours se comptent en jours ouvr\u00e9s, conform\u00e9ment \u00e0 l'<a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2015-10565#a30\" target=\"_blank\" rel=\"nofollow noopener\">article 30.2 de la loi 39\/2015 sur la proc\u00e9dure administrative<\/a>. Il s'agit de d\u00e9lais maximaux fix\u00e9s par la loi, et non de d\u00e9lais constat\u00e9s\u00a0: pour estimer le calendrier de votre dossier, contactez-nous pour confirmer votre situation au <a href=\"tel:+34963741657\">+34 963 74 16 57<\/a> ou \u00e0 <a href=\"mailto:felix.delaguia@delaguialuzon.com\">felix.delaguia@delaguialuzon.com<\/a>.<\/p>
```

## C2b: UNVERIFIABLE

**Location:** H2 "La procédure de demande de résidence", step list, after "Dépôt consulaire"  
**Current wording (live):** « Instruction consulaire : généralement 1 à 3 mois (20 à 30 jours ouvrés via l'UGE). »

**Finding:** "1 à 3 mois" has no official source; UGE does not do consular processing. Replace with legal deadline: 10 dias habiles for Ley 14/2013 visas (art. 75.5). General-regime visa deadlines vary by type (RD 1155/2024 arts 27-40), not stated.

**Sources:** https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a75

**Proposed FR (decoded HTML):**

```html
<li><strong>Instruction consulaire :</strong> le délai légal dépend du type de visa. Pour les visas de la loi 14/2013, dont le visa nomade numérique, le consulat dispose de 10 jours ouvrés (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a75" target="_blank" rel="nofollow noopener">délai fixé par l'article 75.5 de la loi 14/2013</a>).</li>
```

**Old snippet as stored in `_elementor_data` (JSON-escaped, occurs once):**

```
<li><strong>Instruction consulaire :<\/strong> g\u00e9n\u00e9ralement 1 \u00e0 3 mois (20 \u00e0 30 jours ouvr\u00e9s via l'UGE).<\/li>
```

**New snippet (JSON-escaped):**

```
<li><strong>Instruction consulaire\u00a0:<\/strong> le d\u00e9lai l\u00e9gal d\u00e9pend du type de visa. Pour les visas de la loi 14\/2013, dont le visa nomade num\u00e9rique, le consulat dispose de 10\u00a0jours ouvr\u00e9s (<a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2013-10074#a75\" target=\"_blank\" rel=\"nofollow noopener\">d\u00e9lai fix\u00e9 par l'article 75.5 de la loi 14\/2013<\/a>).<\/li>
```

## C2c: UNVERIFIABLE

**Location:** FAQ, H3 "Combien de temps faut-il pour obtenir la résidence en Espagne ?"  
**Current wording (live):** « L'instruction consulaire prend généralement de 1 à 3 mois. Les visas nomade numérique et startup traités via l'UGE sont souvent résolus en 20 à 30 jours ouvrés. Prévoyez 30 à 40 jours après l'arrivée pour le TIE. »

**Finding:** Real-world times unsourced; remove. Legal: 10 dias habiles consulate (art. 75.5 Ley 14/2013), 20 dias UGE (art. 76.1). TIE: request in person within one month of entry (LO 4/2000 art. 4.2; RD 1155/2024 art. 209.1). Visas under Ley 14/2013 authorise residence without TIE (art. 75.4).

**Sources:** https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a75 , https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a76 , https://www.boe.es/buscar/act.php?id=BOE-A-2000-544#a4

**Proposed FR (decoded HTML):**

```html
<p>Il n'existe pas de délai unique : il dépend du type de visa et du lieu de dépôt. Pour les visas de la loi 14/2013, comme le visa nomade numérique, le consulat doit statuer dans les 10 jours ouvrés, et l'UGE dispose de 20 jours pour une autorisation demandée depuis l'Espagne, selon les <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a75" target="_blank" rel="nofollow noopener">articles 75 et 76 de la loi 14/2013 de soutien aux entrepreneurs</a>. Lorsque la TIE est exigée, elle se demande en personne dans le mois suivant l'entrée en Espagne, comme le prévoit l'<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2000-544#a4" target="_blank" rel="nofollow noopener">article 4.2 de la loi organique 4/2000 sur les étrangers</a>. Pour estimer le calendrier de votre dossier, contactez-nous pour confirmer votre situation au <a href="tel:+34963741657">+34 963 74 16 57</a> ou à <a href="mailto:felix.delaguia@delaguialuzon.com">felix.delaguia@delaguialuzon.com</a>.</p>
```

**Old snippet as stored in `_elementor_data` (JSON-escaped, occurs once):**

```
<p>L'instruction consulaire prend g\u00e9n\u00e9ralement de 1 \u00e0 3 mois. Les visas nomade num\u00e9rique et startup trait\u00e9s via l'UGE sont souvent r\u00e9solus en 20 \u00e0 30 jours ouvr\u00e9s. Pr\u00e9voyez 30 \u00e0 40 jours apr\u00e8s l'arriv\u00e9e pour le TIE.<\/p>
```

**New snippet (JSON-escaped):**

```
<p>Il n'existe pas de d\u00e9lai unique\u00a0: il d\u00e9pend du type de visa et du lieu de d\u00e9p\u00f4t. Pour les visas de la loi 14\/2013, comme le visa nomade num\u00e9rique, le consulat doit statuer dans les 10\u00a0jours ouvr\u00e9s, et l'UGE dispose de 20\u00a0jours pour une autorisation demand\u00e9e depuis l'Espagne, selon les <a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2013-10074#a75\" target=\"_blank\" rel=\"nofollow noopener\">articles 75 et 76 de la loi 14\/2013 de soutien aux entrepreneurs<\/a>. Lorsque la TIE est exig\u00e9e, elle se demande en personne dans le mois suivant l'entr\u00e9e en Espagne, comme le pr\u00e9voit l'<a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2000-544#a4\" target=\"_blank\" rel=\"nofollow noopener\">article 4.2 de la loi organique 4\/2000 sur les \u00e9trangers<\/a>. Pour estimer le calendrier de votre dossier, contactez-nous pour confirmer votre situation au <a href=\"tel:+34963741657\">+34 963 74 16 57<\/a> ou \u00e0 <a href=\"mailto:felix.delaguia@delaguialuzon.com\">felix.delaguia@delaguialuzon.com<\/a>.<\/p>
```

## C3: WRONG

**Location:** H2 "Santé, sécurité sociale et droits conférés par la résidence", list, between "Éducation" and "Regroupement familial"  
**Current wording (live):** « Conduite automobile : les permis de l'UE sont reconnus. La plupart des permis de pays tiers exigent un examen espagnol dans les six mois. »

**Finding:** RD 818/2009 art. 21.2.c and 21.3: a recognised non-EU licence is valid for max. 6 months from acquiring normal residence in Spain; after that it is no longer valid and the holder must obtain a Spanish licence (tests). Art. 22: exchange (canje) where an agreement allows it, possible as soon as residence is acquired. Not an "exam within six months"; "la plupart" unsourced.

**Sources:** https://www.boe.es/buscar/act.php?id=BOE-A-2009-9481#a21 , https://www.boe.es/buscar/act.php?id=BOE-A-2009-9481#a22

**Proposed FR (decoded HTML):**

```html
<li><strong>Conduite automobile :</strong> les permis de l'UE sont reconnus. Un permis délivré hors de l'Union européenne et reconnu en Espagne permet de conduire pendant six mois au maximum à compter de l'acquisition de la résidence normale, selon l'<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2009-9481#a21" target="_blank" rel="nofollow noopener">article 21 du règlement général des conducteurs (Real Decreto 818/2009)</a>. Passé ce délai, il faut l'échanger contre un permis espagnol lorsqu'une convention avec le pays de délivrance le prévoit (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2009-9481#a22" target="_blank" rel="nofollow noopener">article 22 du Real Decreto 818/2009</a>), ou à défaut obtenir le permis espagnol en réussissant les épreuves.</li>
```

**Old snippet as stored in `_elementor_data` (JSON-escaped, occurs once):**

```
<li><strong>Conduite automobile :<\/strong> les permis de l'UE sont reconnus. La plupart des permis de pays tiers exigent un examen espagnol dans les six mois.<\/li>
```

**New snippet (JSON-escaped):**

```
<li><strong>Conduite automobile\u00a0:<\/strong> les permis de l'UE sont reconnus. Un permis d\u00e9livr\u00e9 hors de l'Union europ\u00e9enne et reconnu en Espagne permet de conduire pendant six mois au maximum \u00e0 compter de l'acquisition de la r\u00e9sidence normale, selon l'<a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2009-9481#a21\" target=\"_blank\" rel=\"nofollow noopener\">article 21 du r\u00e8glement g\u00e9n\u00e9ral des conducteurs (Real Decreto 818\/2009)<\/a>. Pass\u00e9 ce d\u00e9lai, il faut l'\u00e9changer contre un permis espagnol lorsqu'une convention avec le pays de d\u00e9livrance le pr\u00e9voit (<a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2009-9481#a22\" target=\"_blank\" rel=\"nofollow noopener\">article 22 du Real Decreto 818\/2009<\/a>), ou \u00e0 d\u00e9faut obtenir le permis espagnol en r\u00e9ussissant les \u00e9preuves.<\/li>
```

## C4: WRONG

**Location:** H2 "Erreurs fréquentes lors de la demande de résidence en Espagne", last list item  
**Current wording (live):** « Non-respect du délai post-arrivée : le non-respect du rendez-vous TIE dans les 30 jours peut entraîner l'annulation du visa. »

**Finding:** Obligation: request TIE in person within one month of entry for visas > 6 months (LO 4/2000 art. 4.2; RD 1155/2024 art. 209.1). Breach = infraccion grave (LO 4/2000 art. 53.1.h), fine EUR 501-10,000 (art. 55.1.b); expulsion not available for 53.1.h (art. 57.1). RD 1155/2024 art. 209.4 refers to the LOEX sanction regime; no provision cancels the visa for this.

**Sources:** https://www.boe.es/buscar/act.php?id=BOE-A-2000-544#a4 , https://www.boe.es/buscar/act.php?id=BOE-A-2000-544#a53 , https://www.boe.es/buscar/act.php?id=BOE-A-2000-544#a55 , https://www.boe.es/buscar/act.php?id=BOE-A-2000-544#a57 , https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a2-21

**Proposed FR (decoded HTML):**

```html
<li><strong>Non-respect du délai post-arrivée :</strong> le titulaire d'un visa de plus de six mois doit demander sa TIE en personne dans le mois suivant son entrée en Espagne (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2000-544#a4" target="_blank" rel="nofollow noopener">article 4.2 de la loi organique 4/2000</a>, repris par l'<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a2-21" target="_blank" rel="nofollow noopener">article 209 du Real Decreto 1155/2024</a>). Ne pas le faire constitue une infraction grave, passible d'une amende de 501 à 10 000 € selon les <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2000-544#a53" target="_blank" rel="nofollow noopener">articles 53.1.h et 55.1.b de la loi organique 4/2000</a>. En cas de retard, contactez-nous pour confirmer votre situation au <a href="tel:+34963741657">+34 963 74 16 57</a> ou à <a href="mailto:felix.delaguia@delaguialuzon.com">felix.delaguia@delaguialuzon.com</a>.</li>
```

**Old snippet as stored in `_elementor_data` (JSON-escaped, occurs once):**

```
<li><strong>Non-respect du d\u00e9lai post-arriv\u00e9e :<\/strong> le non-respect du rendez-vous TIE dans les 30 jours peut entra\u00eener l'annulation du visa.<\/li>
```

**New snippet (JSON-escaped):**

```
<li><strong>Non-respect du d\u00e9lai post-arriv\u00e9e\u00a0:<\/strong> le titulaire d'un visa de plus de six mois doit demander sa TIE en personne dans le mois suivant son entr\u00e9e en Espagne (<a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2000-544#a4\" target=\"_blank\" rel=\"nofollow noopener\">article 4.2 de la loi organique 4\/2000<\/a>, repris par l'<a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2024-24099#a2-21\" target=\"_blank\" rel=\"nofollow noopener\">article 209 du Real Decreto 1155\/2024<\/a>). Ne pas le faire constitue une infraction grave, passible d'une amende de 501 \u00e0 10\u00a0000\u00a0\u20ac selon les <a href=\"https:\/\/www.boe.es\/buscar\/act.php?id=BOE-A-2000-544#a53\" target=\"_blank\" rel=\"nofollow noopener\">articles 53.1.h et 55.1.b de la loi organique 4\/2000<\/a>. En cas de retard, contactez-nous pour confirmer votre situation au <a href=\"tel:+34963741657\">+34 963 74 16 57<\/a> ou \u00e0 <a href=\"mailto:felix.delaguia@delaguialuzon.com\">felix.delaguia@delaguialuzon.com<\/a>.<\/li>
```
