# Respuestas a las preguntas sobre la taxonomía de solicitudes web

Respuesta a las preguntas de Andrea (fichero `preguntas-taxonomia-mike.md`). Fecha: 13 de octubre de 2026.

**No incluye mensajes ni fragmentos de mensajes**, ni nombres, correos o teléfonos. Contiene reglas, criterios y estadísticas agregadas que ya figuran en el informe; las frases de ejemplo de la sección 4 son inventadas. La sección 9 añade **expresiones reales sueltas** que aparecen en 5 o más solicitudes distintas (sin contexto, sin frases).

## 0. Lo que conviene saber antes de leer

- **Sobre el archivo `tools/leads_taxonomy.py` (pregunta 1).** No lo adjunto tal cual. Durante la revisión añadí al archivo 28 fragmentos muy concretos que copié mirando mensajes reales sin etiquetar, y vuestra condición es no recibir texto real. Los he retirado. Las reglas restantes están completas en la sección 2: 72 subtemas y 1321 expresiones.
- **Corrección de dos cifras del informe.** (a) El informe y el README decían 62 subtemas; son **72** (la tabla que me enviáis ya lista los 72). (b) La palabra inglesa *will* (testamento) activaba `suc_herencia` en frases como *we will*. Lo corregí: `suc_herencia` pasa de 72 a **64** solicitudes, `ext_general` de 24 a 25 y `x_comercial` de 1 a 2. (c) `nominas` figuraba en contabilidad y las nóminas de un trabajador son laborales: `fis_iva_conta` pasa de 50 a **44**. Informe, presentaciones y CSV ya están actualizados; si trabajáis con la versión anterior de los CSV, esos 8 casos de herencia son falsos positivos.
- **Alcance real de las reglas.** Se afinaron con textos en español y francés y con 33 mensajes del formulario de inmigración EN (codificados a mano). El texto del formulario EN general (343) y de los formularios RU y de inmigración FR no se analizó. Las secciones 4 y 5 (inglés y ruso) mezclan lo que ya estaba implementado con sugerencias que **no están validadas con datos**; van marcadas.
- Los CSV incluyen las columnas `primary_subtopic` y `all_subtopics` con estos mismos códigos.

## 1. Cómo asignaba un subtema el motor (algoritmo)

Pasos, en orden. Con esto se reproduce el comportamiento sin ver mis datos.

1. **Texto de entrada** = asunto + " . " + mensaje. No se usa nombre, correo ni teléfono.
2. **Normalización**: `NFKD`, se eliminan las marcas diacríticas (á→a, ñ→n, ç→c, ё→е, й→и), minúsculas, comillas y apóstrofos tipográficos → `'`, espacios múltiples → uno. Por eso las expresiones no llevan acentos: `espana`, `regimen`, `sejour`. En JavaScript: `s.normalize("NFKD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/[\u2018\u2019]/g, "'").replace(/\s+/g, " ")`.
3. **Cada subtema es una expresión regular** (alternativas separadas por `|`) que se busca como **subcadena** en el texto normalizado. Sin `\b` actúa como raíz (`reagrup` casa con *reagrupación*, *reagrupar*); con `\b` exige palabra completa (`\bnie\b`, `\biva\b`, `\btva\b`, `\bvat\b`). Sintaxis de Python, compatible con JavaScript. `.{0,20}` = hasta 20 caracteres cualesquiera entre dos palabras.
4. **Las mismas reglas se aplican a cualquier texto**, sea cual sea el idioma del formulario. No hay una lista por idioma: una solicitud en inglés enviada por el formulario ES se clasifica con las mismas expresiones.
5. **Subtemas débiles** (lista en la sección 2): solo cuentan si coinciden 2 o más veces, o si su área coincide con el área elegida en el desplegable del formulario.
6. **Subtemas genéricos** (`ext_general`, `fis_general`, `inm_general`): solo se usan si no hay **ningún** subtema específico. **Subtemas no jurídicos** (`x_*`): solo si no hay ninguno jurídico.
7. **Puntuación**: nº de coincidencias × 0,4 si el subtema es *amplio*, + 0,5 si su área coincide con el desplegable. Se ordenan por puntuación descendente y, a igualdad, por la posición de la primera coincidencia en el texto. El primero es el **subtema principal** y su hoja es la **hoja principal**.
8. **Formularios de inmigración**: si no sale ningún subtema, se asigna `ext_general`.
9. **Multitema (`multi_topic`)** = 1 si, descontando los auxiliares (`ext_visado`, `ext_denegacion`, `inm_registro`, `mer_contratos`, `fis_inspeccion`, `suc_litigio`, `ext_banca`), hay 2 o más hojas distintas o 3 o más subtemas.

Detectores de intención (independientes de la taxonomía), por si los queréis en el formulario:

- **Pide honorarios o presupuesto**: `honorarios|presupuesto|cuanto cuesta|cuanto cobran|precio|tarifa|\bfees?\b|\bprice|\bcost\b|\bcosts\b|\bquote\b|how much|combien|\btarifs?\b|devis|honoraires|\bcout|budget|coste|cobran|cuanto vale`
- **Pide cita o llamada**: `\bcita\b|reunion|llamada|videollamada|videoconferencia|consulta (con|para|online)|una consulta|appointment|meeting|\bcall\b|video ?call|consultation|schedule|rendez.vous|\brdv\b|entretien|disponibilit|availability|disponibilidad|contactar|contact me|contactez|me contacter|ponerse en contacto|llamarme|rappel|rappeler|\bphone\b|whatsapp|zoom|teams`
- **Urgencia o plazo**: `urgente|urgent|lo antes posible|asap|as soon as|plazo|deadline|cuanto antes|des que possible|le plus tot|expire|caduca|vence|\bdelai|date limite|immediately|inmediat|tomorrow|manana|demain|aujourd|this week|esta semana|cette semaine|time.?sensitive|rapidement|pronto|quickly|rapido`
- **Pregunta o pide información**: `\?|como puedo|como se|how can|how do|how to|what is|what are|que es\b|cuales son|quels sont|quelles sont|comment\b|quiero saber|me gustaria saber|quisiera saber|informacion (sobre|acerca)|information (about|on|regarding)|renseignement|informations? sur|requisitos|requirements|conditions pour|documents (needed|required)|documentos necesarios|pieces (a fournir|necessaires)|dudas?\b|question|puede(n)? (ayudarme|informarme)|could you (please )?(let me know|tell me|advise|inform)|savoir si|saber si|wondering|me preguntaba|i would like to know|j.aimerais savoir|aimerais connaitre`

`blog_candidate` = 1 si hay intención de información y no hay precio, cita, urgencia ni petición explícita de abogado, o si el mensaje tiene menos de 180 caracteres y tampoco hay esas señales.

## 2. Palabras clave por subtema (pregunta 2)

Leyenda: `\b` = palabra completa; `(a|b)?` = opcional; `.{0,N}` = hasta N caracteres en medio; sin `\b` = raíz o subcadena. Todo en minúsculas y sin acentos. En cada subtema las expresiones aparecen mezcladas (español, francés, inglés), en el orden del archivo, porque el motor no distinguía idioma; el ruso está en la sección 5 y el inglés se resume por separado en la sección 4.

### Extranjería: residencia, nacionalidad, reagrupación (EXT-4)

**`ext_nie_tie`** · NIE y TIE (tarjeta) / NIE et TIE (carte) · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `\bnie\b` · `\btie\b` · `n\.i\.e` · `tarjeta de identidad de extranjero` · `numero de identidad de extranjero` · `numero d.identification` · `\bcue\b` · `certificado de registro de ciudadano` · `cita previa` · `rendez.vous (a la )?prefecture` · `nie\b.{0,20}cita`

**`ext_nomada`** · Nómada digital / teletrabajo internacional / Nomade numérique / télétravail international · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `nomadas? digital(es)?` · `digital nomads?` · `nomades? numeriques?` · `teletrabajo internacional` · `teletravail international` · `nomade numerique` · `remote work visa` · `\bdnv\b` · `ley de startups` · `visa.{0,15}teletrabaj` · `trabajo remoto` · `remote(ly)? work` · `travail a distance` · `teletravail` · `teletrabajo` · `teletravaill` · `remote worker` · `trabajar en remoto` · `для удаленнои` · `удаленн\w+ работ`

**`ext_no_lucrativa`** · Residencia no lucrativa / Résidence non lucrative · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `no lucrativ` · `non.?lucrativ` · `non lucratif` · `\bnlv\b` · `sin actividad lucrativa`

**`ext_inversor`** · Inversor / Golden visa / Investisseur / Golden visa · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `golden visa` · `visa dorado` · `visado de inversor` · `investor visa` · `visa investisseur` · `residence par l.investissement` · `residencia por inversion`

**`ext_trabajo`** · Residencia y trabajo (cuenta ajena, cualificado) / Résidence et travail (salarié, qualifié) · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `permiso de trabajo` · `autorizacion de (residencia y )?trabajo` · `work permit` · `work visa` · `permis de travail` · `autorisation de travail` · `cuenta ajena` · `highly.qualified` · `alta cualificacion` · `hautement qualifie` · `haute qualification` · `blue card` · `tarjeta azul` · `oferta de trabajo` · `job offer` · `offre d.emploi` · `shortage occupation` · `catalogo de ocupaciones` · `labour market test` · `situacion nacional de empleo`

**`ext_emprendedor`** · Emprendedor / ENISA / startups / Entrepreneur / ENISA / startups · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `emprendedor` · `entrepreneur` · `\benisa\b` · `autorisation entrepreneur` · `startup` · `start-up`

**`ext_estudios`** · Estancia por estudios / Séjour d'études · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable).
- Expresiones: `estancia por estudios` · `visado de estudiante` · `student visa` · `student permit` · `visa etudiant` · `titre de sejour etudiant` · `\bestudiante\b` · `\betudiant` · `\bstudent\b` · `master` · `grado superior` · `\bmir\b`

**`ext_arraigo`** · Arraigo (social, laboral, familiar) / Arraigo (enracinement) · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `arraigo`

**`ext_reagrupacion`** · Reagrupación familiar / pareja / familiar de comunitario / Regroupement familial / conjoint / famille d'européen · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `reagrupaci` · `reagrup` · `regroupement familial` · `family reunif` · `reunificacion` · `reunification` · `\bdependent` · `pareja de hecho` · `unmarried partner` · `familiar de (ciudadano )?(comunitario|ue|europeo)` · `tarjeta de familiar` · `ascendiente` · `descendiente` · `ressortissant europeen` · `membre de (la )?famille` · `conjoint d.un` · `partner.{0,25}(visa|residen)` · `(visa|residen).{0,25}partner` · `spouse visa` · `visa conjoint` · `bring my (wife|husband|partner|family)`

**`ext_nacionalidad`** · Nacionalidad española / Nationalité espagnole · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `nacionalidad espanola` · `(obtener|solicitar|adquirir|acceder a) la nacionalidad` · `spanish (citizenship|nationality)` · `citizenship application` · `nationalite espagnole` · `acquerir la nationalite` · `acces a la nationalite` · `naturalisation` · `naturalizacion` · `ley de memoria` · `nietos` · `demande de nationalite` · `obtain (spanish )?citizenship` · `obtenir la nationalite` · `ciudadania espanola` · `nacionalidad (francesa|britanica|inglesa|alemana|italiana)` · `nationalite (francaise|britannique|italienne|allemande)` · `гражданств` · `naturalisation francaise` · `double nationalite`

**`ext_regularizacion`** · Regularización extraordinaria 2026 (masiva) / Régularisation extraordinaire 2026 (massive) · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `regularizacion (extraordinaria|colectiva|masiva|general|de 2026)` · `regularisation (extraordinaire|massive|collective|generale|2026)` · `extraordinary regulari` · `migrant amnesty` · `amnest` · `1 de abril` · `1er avril` · `regularizacion extraord` · `proceso de regularizacion` · `регуляриз` · `regularisation generale` · `regularisation massive`

**`ext_asilo`** · Asilo / protección internacional / humanitaria / Asile / protection internationale / humanitaire · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `\basilo` · `asylum` · `proteccion internacional` · `refugi` · `humanitari` · `violencia de genero` · `domestic violence` · `\basile\b` · `demandeur d.asile`

**`ext_renovacion_larga`** · Renovación / residencia de larga duración / Renouvellement / résident de longue durée · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Tipo: amplio (puntúa x0,4 al elegir el principal).
- Expresiones: `larga duracion` · `long.?term residen` · `renovacion (de )?(la |mi |mis |su )?(tarjeta|tie|residencia|autorizacion|permiso|nie)` · `renovar (la |mi |mis |su )?(tarjeta|tie|residencia|autorizacion|permiso)` · `renouvellement (de )?(mon |ma |la |du |de )?(titre|carte|sejour|residence)` · `renouveler (mon |ma |la )?(titre|carte|sejour)` · `renew(ing|al)? (my |the |our )?(tie|residen|permit|card|visa)` · `prorroga de estancia` · `residencia permanente` · `permanent residen` · `residence permanente` · `resident de longue duree` · `пмж` · `постоянн\w+ вид на жительство` · `постоянн\w+ проживан`

**`ext_brexit`** · Brexit / Acuerdo de Retirada / Brexit / Accord de retrait · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `brexit` · `acuerdo de retirada` · `withdrawal agreement` · `accord de retrait` · `article 50` · `art\.? 50 tue`

**`ext_visado`** · Visado consular / Visa consulaire · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable); amplio (puntúa x0,4 al elegir el principal); auxiliar (no crea 'multitema' por sí solo).
- Expresiones: `visado` · `\bvisa\b` · `\bvisas\b` · `consulat` · `consulate` · `embajada` · `embassy` · `ambassade` · `cita previa.{0,20}consul` · `виз[аыуе]\b` · `визов`

**`ext_denegacion`** · Denegación, recurso, requerimiento / Refus, recours · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Tipo: amplio (puntúa x0,4 al elegir el principal); auxiliar (no crea 'multitema' por sí solo).
- Expresiones: `denegaci` · `denegad` · `\bdenied\b` · `\bdenial\b` · `refus` · `\brecurso` · `recours` · `\bappeal` · `requerimiento` · `recurso contencioso` · `subsanacion`

**`ext_irregularidad`** · Estancia irregular / overstay / 90 días / Séjour irrégulier / dépassement / 90 jours · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Expresiones: `overstay` · `exceeded.{0,20}(stay|90)` · `90 dias` · `90 days` · `90 jours` · `sin papeles` · `sans papiers` · `sans titre` · `expulsion` · `orden de salida` · `oqtf` · `obligation de quitter` · `irregular` · `situation irreguliere` · `ilegal` · `regulariser (ma|sa|mon|notre|leur|ma mere|mon frere|son)` · `regularisation (de (la |ma |mon |sa )?(situation|titre|carte|sejour|residence)|situation|sejour|residence|administrative)` · `regularizar (mi |su |la )?situacion` · `regularizacion (en espana|de (mi |su )?situacion|de residencia)` · `regularizar mi` · `regulariser pour` · `regularisation en espagne`

**`ext_general`** · Extranjería (consulta general) / Droit des étrangers (général) · hoja EXT-4 (Extranjería: residencia, nacionalidad, reagrupación)
- Tipo: genérico (solo si no hay ninguno específico).
- Expresiones: `extranjeria` · `immigration` · `inmigracion` · `inmigrante` · `immigrer` · `immigr` · `residencia` · `residence permit` · `residency` · `titre de sejour` · `carte de sejour` · `permis de sejour` · `permiso de residencia` · `autorisation de sejour` · `carte de resident` · `resident permit` · `residence en espagne` · `une residence` · `residir en` · `resident en espagne` · `residente\b` · `resident\b` · `residencia en espana` · `вид на жительство` · `внж` · `резиденц` · `иммиграц` · `иностранц` · `sejour en espagne` · `sejour d` · `situacion administrativa` · `papeles`

### Instalación, protección social y banca (EXT-1, EXT-2, EXT-3)

**`ext_empadronamiento`** · Empadronamiento / Inscription au padrón · hoja EXT-1 (Acompañamiento en la instalación administrativa)
- Tipo: amplio (puntúa x0,4 al elegir el principal).
- Expresiones: `empadron` · `\bpadron\b` · `padron municipal` · `\bpardon\b` · `certificat d.inscription` · `registro municipal` · `inscription au padron`

**`ext_sanidad_ss`** · Tarjeta sanitaria / nº Seguridad Social / Carte de santé / n° de Sécurité sociale · hoja EXT-1 (Acompañamiento en la instalación administrativa)
- Tipo: amplio (puntúa x0,4 al elegir el principal).
- Expresiones: `tarjeta sanitaria` · `health card` · `carte vitale` · `\bsip\b` · `numero de (la )?seguridad social` · `numero de securite sociale` · `social security number` · `numero de afiliacion` · `affiliation` · `carte sanitaire` · `cobertura medica` · `couverture sante` · `\bcaf\b` · `allocations? familiales` · `prestations? sociales` · `pole emploi` · `france travail` · `securite sociale francaise` · `\bcpam\b` · `\bmsa\b`

**`ext_carnet`** · Canje del carnet de conducir / Échange du permis de conduire · hoja EXT-1 (Acompañamiento en la instalación administrativa)
- Expresiones: `carnet de conducir` · `permiso de conducir` · `driving licen` · `permis de conduire` · `canje del carnet` · `echange du permis`

**`ext_homologacion`** · Homologación / convalidación de títulos / Équivalence de diplômes · hoja EXT-1 (Acompañamiento en la instalación administrativa)
- Expresiones: `homologaci` · `convalidaci` · `recognition of (my )?(degree|diploma|qualification)` · `reconnaissance (de|du) diplome` · `equivalence de diplome`

**`ext_instalacion`** · Traslado e instalación en España / Déménagement et installation en Espagne · hoja EXT-1 (Acompañamiento en la instalación administrativa)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable); amplio (puntúa x0,4 al elegir el principal).
- Expresiones: `relocat` · `moving to spain` · `move to spain` · `move to valencia` · `moving to valencia` · `trasladarme` · `mudarme` · `instalarme` · `traslado a espana` · `me instalo` · `s.installer en espagne` · `m.installer` · `installation en espagne` · `demenager en espagne` · `venir vivre` · `venir habiter` · `vivre en espagne` · `vivir en espana` · `settle in spain` · `live in spain` · `relocation` · `cambio de residencia a espana` · `llegada a espana` · `arrival in spain` · `set(ting)? up (ourselves|myself)` · `expatri` · `passer .{0,12}ans en espagne` · `vivre a valence` · `vivre a valencia` · `s.etablir en espagne` · `etablir en espagne` · `переезд` · `переехать`

**`ext_jubilacion`** · Jubilación, pensiones y prestaciones / Retraite, pensions et prestations · hoja EXT-2 (Protección social y jubilación en España)
- Expresiones: `jubilaci` · `jubilad` · `pension(es)? (de|del|publica|contributiv)` · `pensionista` · `retraite` · `retire(d|ment| to)` · `\bretiring\b` · `prestacion(es)? (por|de) desempleo` · `desempleo` · `chomage` · `unemployment benefit` · `convenio de seguridad social` · `totalizacion` · `seguridad social espanola` · `\bcpam\b` · `\bcnav\b` · `carriere longue` · `pension plan` · `invalidez` · `incapacidad permanente` · `pension (de )?(viud|jubil|reversion|vejez)` · `viudedad` · `reversion` · `pensione` · `пенси`

**`ext_seguro_salud`** · Seguro médico y sanidad / Assurance santé · hoja EXT-2 (Protección social y jubilación en España)
- Tipo: amplio (puntúa x0,4 al elegir el principal).
- Expresiones: `seguro (medico|de salud|privado)` · `health insurance` · `private (health )?insurance` · `assurance (maladie|sante)` · `mutuelle` · `\bcmu\b` · `\bsanidad\b` · `cobertura sanitaria` · `\bs1\b` · `\bef106\b` · `\bs2\b`

**`ext_banca`** · Cuenta bancaria, transferencias, financiación / Compte bancaire, virements, financement · hoja EXT-3 (Asesoramiento bancario y financiero)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable); amplio (puntúa x0,4 al elegir el principal); auxiliar (no crea 'multitema' por sí solo).
- Expresiones: `cuenta bancaria` · `bank account` · `compte bancaire` · `abrir una cuenta` · `open an account` · `ouvrir un compte` · `transferencia internacional` · `international transfer` · `virement international` · `apertura de cuenta` · `banco espanol` · `spanish bank` · `banque espagnole` · `iban` · `financiacion` · `financement` · `prestamo` · `loan\b` · `pret personnel` · `transferir dinero` · `transfer (my )?(money|funds)` · `cuenta en un banco` · `prelevement` · `banco\b` · `bancaire`

### Inmobiliario (INM-1)

**`inm_compra`** · Compra de vivienda / inmueble / Achat de bien immobilier · hoja INM-1 (Adquisición inmobiliaria y derecho de la propiedad)
- Expresiones: `comprar (una |un |la |el )?(casa|piso|vivienda|apartamento|inmueble|propiedad|terreno|parcela|local|villa|finca|chalet)` · `compra de (una |un |la |el )?(casa|piso|vivienda|apartamento|inmueble|propiedad|terreno|parcela|local|villa|finca|chalet)` · `buy(ing)? (a |an |the |my )?(property|house|home|apartment|flat|villa|land|plot|house)` · `purchase of (a |the )?(property|house|apartment|flat)` · `property purchase` · `acheter (un |une |le |la )?(bien|maison|appartement|villa|terrain|logement|studio|local|immeuble)` · `achat (d.un |d.une |de |du |immobilier)` · `acquisition (immobiliere|d.un bien|d.un appartement|d.une maison)` · `adquisicion (de|del) (inmueble|vivienda|propiedad)` · `comprar en espana` · `buy in spain` · `buying property` · `compraventa de (vivienda|inmueble)` · `compromis de vente` · `arras` · `contrato de arras` · `reserva de compra` · `projet d?.?achat` · `achat appart` · `achat d.appart` · `achat maison` · `achat terrain` · `acquerir` · `acquisition d.un` · `investir (dans|en) (un|une)` · `offre d.achat` · `residence secondaire` · `offer on` · `comprar un piso` · `купить` · `покупк\w+ (квартир|дом|недвижим)` · `achete (un|une)` · `j.ai (achete|trouve) (un|une)` · `promesse de vente` · `compromiso de compra`

**`inm_venta`** · Venta de inmueble / Vente de bien immobilier · hoja INM-1 (Adquisición inmobiliaria y derecho de la propiedad)
- Expresiones: `vender (mi |una |un |la |el )?(casa|piso|vivienda|apartamento|inmueble|propiedad|terreno|local|finca|chalet)` · `venta de (mi |una |un |la |el )?(casa|piso|vivienda|apartamento|inmueble|propiedad|terreno|local|finca|chalet)` · `sell(ing)? (my |a |the )?(property|house|home|apartment|flat|villa)` · `vendre (mon |ma |un |une |le |la )?(bien|maison|appartement|villa|terrain|logement)` · `vente de (mon |ma |ce |cette |un |une |l.)(bien|maison|appartement|villa|terrain|logement|immeuble)` · `mise en vente` · `vente d.un` · `продаж\w+ (квартир|дом|недвижим)` · `продать`

**`inm_alquiler`** · Alquiler y contrato de arrendamiento / Location et bail · hoja INM-1 (Adquisición inmobiliaria y derecho de la propiedad)
- Expresiones: `alquiler` · `arrendamiento` · `arrendador` · `inquilino` · `\btenant\b` · `landlord` · `\blease\b` · `rental (contract|agreement)` · `\brent\b` · `\bbail\b` · `locataire` · `bailleur` · `louer` · `locatif` · `location (meublee|longue|de)` · `contrato de alquiler` · `lau\b`

**`inm_conflicto_arrend`** · Impago, desahucio, ocupación ilegal / Impayés, expulsion, squat · hoja INM-1 (Adquisición inmobiliaria y derecho de la propiedad)
- Expresiones: `desahucio` · `impago` · `\beviction` · `unpaid rent` · `loyers? impaye` · `moroso` · `okupa` · `squatt` · `ocupacion ilegal` · `ocupantes` · `occupation illegale` · `expulsion du locataire`

**`inm_comunidad`** · Comunidad de propietarios / Copropriété · hoja INM-1 (Adquisición inmobiliaria y derecho de la propiedad)
- Expresiones: `comunidad de propietarios` · `community of owners` · `copropri` · `syndic\b` · `junta de propietarios` · `homeowners` · `derrama` · `cuota de comunidad` · `charges de copropriete` · `vecin[oa]s?\b` · `voisin` · `garaje` · `trastero` · `ruidos` · `goteras` · `filtracion`

**`inm_turistico`** · Vivienda turística / alquiler vacacional / Location touristique · hoja INM-1 (Adquisición inmobiliaria y derecho de la propiedad)
- Expresiones: `vivienda turistica` · `alquiler turistico` · `licencia turistica` · `tourist (rental|licen|let)` · `airbnb` · `location saisonniere` · `meuble de tourisme` · `\bvut\b` · `alquiler vacacional` · `holiday (let|rental)` · `short.?term rental` · `registro unico de alquileres` · `alquiler de temporada`

**`inm_hipoteca`** · Hipoteca / crédito inmobiliario / Crédit immobilier / hypothèque · hoja INM-1 (Adquisición inmobiliaria y derecho de la propiedad)
- Expresiones: `hipotec` · `mortgage` · `pret immobilier` · `credit immobilier` · `emprunt immobilier` · `cancelacion de hipoteca`

**`inm_obras`** · Obras, licencias y urbanismo / Travaux, permis et urbanisme · hoja INM-1 (Adquisición inmobiliaria y derecho de la propiedad)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable).
- Expresiones: `licencia de obra` · `urbanis` · `building permit` · `permis de construire` · `reforma de` · `renovation` · `construccion` · `construction` · `defecto` · `promotor` · `constructor` · `cedula de habitabilidad` · `catastro` · `cadastre` · `ibi\b` · `planning permission` · `licencia de primera ocupacion` · `\bobras\b` · `travaux`

**`inm_registro`** · Escritura, notaría y registro de la propiedad / Acte notarié et registre foncier · hoja INM-1 (Adquisición inmobiliaria y derecho de la propiedad)
- Tipo: amplio (puntúa x0,4 al elegir el principal); auxiliar (no crea 'multitema' por sí solo).
- Expresiones: `escritura` · `notari` · `registro de la propiedad` · `land registry` · `title deed` · `acte notarie` · `titre de propriete` · `nota simple` · `cargas` · `embargo` · `servidumbre` · `lindero` · `due diligence inmobiliaria` · `verificacion (de )?titulo` · `conservation des hypotheques`

**`inm_general`** · Inmobiliario (consulta general) / Immobilier (général) · hoja INM-1 (Adquisición inmobiliaria y derecho de la propiedad)
- Tipo: genérico (solo si no hay ninguno específico); débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable).
- Expresiones: `appartements?` · `appart` · `maison` · `villa` · `inmobiliari` · `inmueble` · `vivienda` · `propiedad en espana` · `property in spain` · `real estate` · `immobilier` · `bien en espagne` · `villa` · `apartment in` · `apartamento en` · `piso en` · `casa en` · `maison en espagne` · `appartement en espagne` · `\bterreno\b` · `parcela` · `finca` · `недвижим` · `квартир` · `\bдом\b`

### Sucesiones, litigios y familia (SUC-0, SUC-1, SUC-2)

**`suc_herencia`** · Herencia, testamento y declaración de herederos / Succession, testament et dévolution · hoja SUC-0 (Herencias y testamentos (propuesta: hoy sin hoja propia))
- Expresiones: `herencia` · `heredero` · `testamento` · `sucesion` · `inheritance` · `\bprobate\b` · `\bsuccession` · `heritage` · `heritier` · `testament` · `legs\b` · `declaracion de herederos` · `usufructo` · `usufruit` · `quotite` · `reserve hereditaire` · `reglamento .{0,15}sucesiones` · `reglement .{0,10}successions` · `notaire.{0,20}succession` · `fallecimiento` · `fallecido` · `deces` · `decede` · `deceased` · `heir\b` · `last will` · `my will\b` · `a will\b` · `the will\b` · `will and testament` · `estate of` · `partage` · `particion` · `legitima` · `\bcausante` · `fallecio` · `murio` · `falleci` · `died` · `passed away` · `le defunt` · `defunt` · `наследств` · `завещан` · `heredar` · `hereditaire` · `succession`

**`suc_litigio`** · Litigio, reclamación y mediación / Litige, réclamation et médiation · hoja SUC-1 (Mediación y resolución de litigios)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable); amplio (puntúa x0,4 al elegir el principal); auxiliar (no crea 'multitema' por sí solo).
- Expresiones: `demanda\b` · `litigio` · `litige` · `tribunal` · `juzgado` · `procedimiento judicial` · `lawsuit` · `\bsue\b` · `dispute` · `disputa` · `reclamacion` · `reclamation` · `arbitraje` · `arbitrage` · `mediaci` · `mediation` · `conflicto` · `avocat pour un proces` · `proces\b` · `court case` · `legal action` · `accion legal` · `demandar` · `poursuites` · `assignation` · `huissier` · `\bprocurador` · `monitorio` · `sentencia` · `jugement` · `recouvrement` · `impagado` · `unpaid invoice` · `facture impayee` · `cobro de deuda` · `debt recovery` · `recuperar (el )?dinero` · `scam` · `estafa` · `arnaque` · `fraud` · `fraude` · `contentieux` · `amendes?\b` · `\bmultas?\b` · `echeancier` · `diffamation` · `calomnia` · `menace[sr]?\b` · `amenaza` · `accident de la route` · `accidente de trafico` · `судебн` · `\bиск\b` · `спор`

**`suc_penal`** · Penal / penal económico / Pénal / pénal des affaires · hoja SUC-1 (Mediación y resolución de litigios)
- Expresiones: `derecho penal` · `penal economico` · `criminal (law|case|charge|record)` · `delito` · `infraction penale` · `plainte` · `denuncia` · `police report` · `detenido` · `arrest` · `garde a vue` · `casier judiciaire` · `antecedentes penales(?! de)` · `lavado de dinero` · `blanchiment` · `money laundering`

**`suc_familia`** · Familia: divorcio, custodia, régimen matrimonial / Famille : divorce, garde, régime matrimonial · hoja SUC-2 (Derecho de familia: divorcio, custodia (propuesta))
- Expresiones: `divorcio` · `divorce` · `separacion matrimonial` · `custodia` · `pension alimenticia` · `pension alimentaire` · `garde (des |de l.)?enfant` · `regimen economico matrimonial` · `regime matrimonial` · `capitulaciones` · `prenup` · `matrimonio` · `marriage` · `mariage` · `child custody` · `hijos menores` · `adoption` · `adopcion` · `filiation` · `paternidad` · `pacs\b` · `union libre` · `nous marier` · `me marier` · `casarme` · `nos casamos` · `boda` · `get(ting)? married` · `разво`

### Fiscal (FIS-1, FIS-2, FIS-3)

**`fis_convenio_doble`** · Convenio de doble imposición / residencia fiscal / Convention fiscale / résidence fiscale · hoja FIS-1 (Fiscalidad franco-española)
- Expresiones: `doble imposicion` · `double taxation` · `double imposition` · `convenio (fiscal|de doble)` · `convention fiscale` · `tax treaty` · `residencia fiscal` · `tax residen` · `residence fiscale` · `residente fiscal` · `centro de intereses` · `foyer fiscal` · `domicile fiscal` · `exit tax` · `183 d` · `183 days` · `183 jours` · `residente en francia` · `resident en france` · `impots en france` · `impuestos en francia` · `fiscalite franco` · `franco.?espagnol` · `franco.?espanol` · `france et espagne` · `francia y espana`

**`fis_irpf`** · Declaración de la renta (IRPF) / Déclaration de revenus (IRPF) · hoja FIS-2 (Asesoría fiscal en Valencia)
- Expresiones: `declaracion de la renta` · `\birpf\b` · `income tax` · `impot sur le revenu` · `declaration (de )?revenus?` · `modelo 100` · `tax return` · `declaration fiscale` · `declaration d.impots` · `declarar (mis )?ingresos` · `declarar la renta` · `declarar mis` · `presentar (la )?declaracion` · `file (my )?taxes` · `tax filing` · `declaraciones? de (la )?renta` · `declarations? (de )?(renta|revenus|impots)` · `renta francesa` · `declaracion francesa` · `declaraciones atrasadas` · `annees anterieures` · `ejercicios anteriores` · `prior.year returns` · `декларац`

**`fis_no_residente`** · No residentes (Modelo 210 / IRNR) / Non-résidents (Modèle 210 / IRNR) · hoja FIS-2 (Asesoría fiscal en Valencia)
- Expresiones: `no residente` · `non.?resident` · `nonresident` · `modelo 210` · `\bmodelo210\b` · `\birnr\b` · `propietario no residente` · `rentas de no residentes` · `impot des non.?residents` · `non-residents tax` · `formulaire 210` · `formulario 210` · `form 210` · `\b210\b` · `modele 210`

**`fis_beckham`** · Régimen Beckham (impatriados) / Régime Beckham (impatriés) · hoja FIS-2 (Asesoría fiscal en Valencia)
- Expresiones: `beckham` · `impatriad` · `regimen especial de desplazados` · `inbound (expatriate|regime)` · `expatriate regime` · `regime des impatries` · `regimen de impatriados` · `ley beckham`

**`fis_patrimonio_720`** · Patrimonio, Modelo 720/721, bienes en el extranjero / Patrimoine, Modèle 720/721, avoirs à l'étranger · hoja FIS-2 (Asesoría fiscal en Valencia)
- Expresiones: `modelo 720` · `\b720\b` · `modelo 721` · `bienes en el extranjero` · `assets abroad` · `biens a l.etranger` · `impuesto sobre el patrimonio` · `wealth tax` · `impot sur la fortune` · `\bisf\b` · `\bifi\b` · `solidaridad de las grandes fortunas` · `\bigf\b` · `foreign asset` · `declaracion de bienes` · `cuentas en el extranjero` · `comptes a l.etranger`

**`fis_plusvalia`** · Plusvalías y retención del 3 % / Plus-values et retenue de 3 % · hoja FIS-2 (Asesoría fiscal en Valencia)
- Expresiones: `plusvalia` · `capital gain` · `plus.?value` · `ganancia patrimonial` · `retencion (del )?3` · `retenue de 3` · `3% (withholding|retention)` · `impuesto de plusvalia municipal` · `gain en capital`

**`fis_cripto`** · Criptomonedas / Cryptomonnaies · hoja FIS-2 (Asesoría fiscal en Valencia)
- Expresiones: `cripto` · `crypto` · `bitcoin` · `ethereum` · `\bnft\b` · `binance` · `coinbase`

**`fis_inspeccion`** · Requerimiento, inspección o sanción de Hacienda / Contrôle, requête ou pénalité fiscale · hoja FIS-2 (Asesoría fiscal en Valencia)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable); amplio (puntúa x0,4 al elegir el principal); auxiliar (no crea 'multitema' por sí solo).
- Expresiones: `regularisation fiscale` · `regularizacion fiscal` · `regularizar.{0,30}(hacienda|impuestos|fiscal)` · `regulariser.{0,30}(impots|fiscal|revenus)` · `requerimiento de hacienda` · `notificacion de hacienda` · `inspeccion (de )?hacienda` · `inspeccion fiscal` · `sancion tributaria` · `agencia tributaria` · `\baeat\b` · `\bhacienda\b` · `redressement` · `controle fiscal` · `tax audit` · `\bcarta de hacienda` · `recargo` · `prescripcion tributaria` · `paralela` · `declaracion complementaria` · `tax authorit` · `fisc\b` · `\bdgfip\b` · `impots\.gouv` · `tax notice`

**`fis_iva_conta`** · IVA, contabilidad, gestoría e impuesto de sociedades / TVA, comptabilité, gestion et IS · hoja FIS-2 (Asesoría fiscal en Valencia)
- Tipo: amplio (puntúa x0,4 al elegir el principal).
- Expresiones: `\biva\b` · `\bvat\b` · `\btva\b` · `contabilidad` · `comptabilit` · `accounting` · `bookkeeping` · `gestoria` · `modelo 303` · `modelo 130` · `libros contables` · `cuentas anuales` · `impuesto (de|sobre) sociedades` · `corporate tax` · `impot sur les societes` · `facturaci` · `facturation` · `\binvoic` · `verifactu` · `expert.?comptable` · `accountant` · `contable` · `contador` · `annual accounts` · `\bcomptes annuels` · `bilan` · `cuentas de la empresa` · `bilan comptable` · `liasse fiscale` · `expert comptable` · `ooo\b`

**`fis_general`** · Fiscalidad (consulta general) / Fiscalité (général) · hoja FIS-2 (Asesoría fiscal en Valencia)
- Tipo: genérico (solo si no hay ninguno específico).
- Expresiones: `\bimpuestos?\b` · `\btax(es|ation)?\b` · `fiscal` · `fiscalidad` · `fiscalite` · `tributa` · `\bimpots?\b` · `tributar` · `asesoria fiscal` · `conseil fiscal` · `taxation` · `taxable` · `haciendas?\b` · `налог`

**`fis_sucesiones_impuesto`** · Impuesto de sucesiones y donaciones / Droits de succession et donation · hoja FIS-3 (Sucesiones y planificación patrimonial)
- Expresiones: `impuesto de sucesiones` · `inheritance tax` · `droits de succession` · `impuesto de donaciones` · `gift tax` · `droits de donation` · `impuesto sobre sucesiones` · `donacion` · `donation` · `plusvalia mortis` · `\bisd\b`

**`fis_planificacion`** · Planificación patrimonial y holding / Planification patrimoniale et holding · hoja FIS-3 (Sucesiones y planificación patrimonial)
- Expresiones: `planificacion patrimonial` · `estate planning` · `wealth planning` · `planification patrimoniale` · `gestion de patrimoine` · `holding` · `pacto sucesorio` · `trust\b` · `fideicomiso` · `assurance.vie` · `seguro de vida` · `optimisation fiscale` · `optimizacion fiscal` · `tax planning` · `planificacion fiscal` · `patrimonio familiar` · `societe patrimoniale` · `sociedad patrimonial`

### Mercantil (MER-1 a MER-4)

**`mer_creacion`** · Crear una sociedad / abrir un negocio / Créer une société / ouvrir une activité · hoja MER-1 (Creación de empresa en España)
- Expresiones: `crear (una |mi |nuestra )?(empresa|sociedad|compania|negocio)` · `constituir` · `constitucion de (una |la )?sociedad` · `abrir (una |mi )?(empresa|sociedad|negocio|sucursal|local)` · `company (formation|creation|setup|set up|registration)` · `(set up|setting up|open|opening|start|starting|form|forming|register|registering|incorporate|incorporating) (a |an |my |our )?(new )?(company|business|llc|limited|ltd|entity|corporation|subsidiary|branch|firm)` · `creation d.(une )?(entreprise|societe)` · `creer (une |ma |notre )?(societe|entreprise|sas|sarl|activite)` · `immatriculation` · `sociedad limitada` · `\bs\.?l\.?u?\b` · `\bsarl\b` · `\bsas\b` · `\bsasu\b` · `start.?up` · `creation de societe` · `monter (une |ma |notre )?(societe|entreprise)` · `ouvrir (une |ma |notre )?(societe|entreprise|activite|succursale)` · `ouverture de (societe|compte professionnel)` · `apertura de negocio` · `capital social` · `objeto social` · `negocio en espana` · `empresa en espana` · `entreprise en espagne` · `business in spain` · `company in spain` · `societe en espagne` · `creacion de (una )?(empresa|sociedad)` · `constitucion de (una )?empresa` · `creer .{0,25}(entreprise|societe)` · `creation d.entreprise` · `open an? (company|business)` · `sociedad en espana` · `eurl` · `открыт\w+ (фирм|компани|бизнес)` · `создан\w+ (фирм|компани)` · `регистраци\w+ (компани|фирм)` · `фирм\w+ в испании` · `ouvrir une societe` · `monter une affaire` · `abrir una sociedad` · `abrir un negocio`

**`mer_autonomo`** · Alta de autónomo / freelance / auto-entrepreneur / Statut d'autónomo / indépendant / auto-entrepreneur · hoja MER-1 (Creación de empresa en España)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable).
- Expresiones: `autonomo` · `self.?employed` · `freelanc` · `auto.?entrepreneur` · `micro.?entrepreneur` · `travailleur independant` · `trabajador por cuenta propia` · `\breta\b` · `tarifa plana` · `cuota de autonomo` · `alta de autonomo` · `alta en hacienda` · `modelo 036` · `modelo 037` · `\biae\b` · `\bllc\b` · `sole (proprietor|trader)` · `independent contractor` · `liberal profession` · `profesional liberal` · `profession liberale` · `\bcontractor\b`

**`mer_inversion_ext`** · Implantación / inversión extranjera en España / Implantation / investissement en Espagne · hoja MER-1 (Creación de empresa en España)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable).
- Expresiones: `inversion extranjera` · `foreign investment` · `investissement etranger` · `invest in spain` · `invertir en espana` · `investir en espagne` · `establecimiento permanente` · `permanent establishment` · `sucursal` · `succursale` · `filial` · `subsidiary` · `market entry` · `implantation` · `desarrollar (mi |nuestro )?negocio en espana` · `expand(ing)? to spain` · `expansion en espagne` · `expandir`

**`mer_contratos`** · Contratos mercantiles y de distribución / Contrats commerciaux et de distribution · hoja MER-2 (Derecho mercantil y contratos comerciales)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable); amplio (puntúa x0,4 al elegir el principal); auxiliar (no crea 'multitema' por sí solo).
- Expresiones: `contrato (mercantil|comercial|de distribucion|de agencia|de suministro|de servicios|de colaboracion|de franquicia)` · `contrat (commercial|de distribution|d.agent|de fourniture|de prestation|de collaboration)` · `commercial contract` · `distribution agreement` · `agencia comercial` · `pacto de socios` · `shareholder.?s? agreement` · `pacte d.associes` · `condiciones generales` · `terms and conditions` · `conditions generales` · `\bcgv\b` · `\bcgu\b` · `\bnda\b` · `confidentialidad` · `sales agreement` · `purchase agreement` · `contrat de vente` · `contrato de compraventa` · `contrato de venta` · `draft(ing)? (a|an) (contract|agreement)` · `redactar un contrato` · `rediger un contrat` · `contrat de prestation` · `договор`

**`mer_compraventa_empresa`** · Compraventa de empresa / participaciones / due diligence / Cession d'entreprise / parts / due diligence · hoja MER-2 (Derecho mercantil y contratos comerciales)
- Expresiones: `compraventa de (una )?(empresa|sociedad|participaciones|acciones)` · `acquisition of (a )?(company|business|shares)` · `share purchase` · `cession de (parts|titres|fonds)` · `cesion de participaciones` · `due diligence` · `rachat d.entreprise` · `reprise d.entreprise` · `comprar (una )?empresa` · `vender (mi |una )?empresa` · `fusion` · `merger` · `\bm&a\b` · `traspaso`

**`mer_pi_rgpd`** · Marca, propiedad intelectual, RGPD / Marque, propriété intellectuelle, RGPD · hoja MER-2 (Derecho mercantil y contratos comerciales)
- Expresiones: `\bmarca\b` · `trademark` · `propiedad intelectual` · `intellectual property` · `brevet` · `\bpatent` · `rgpd` · `gdpr` · `proteccion de datos` · `data protection` · `protection des donnees` · `copyright` · `derechos de autor` · `droit d.auteur` · `\bmarque\b` · `\blopd`

**`mer_concurso`** · Insolvencia, concurso y reestructuración / Insolvabilité, redressement et restructuration · hoja MER-3 (Auditoría y reestructuración empresarial)
- Expresiones: `concurso de acreedores` · `insolvenc` · `bankruptcy` · `faillite` · `liquidation` · `redressement judiciaire` · `pre.?concurso` · `reestructuraci` · `restructuring` · `restructuration` · `\bauditor` · `\baudit\b` · `auditoria` · `disolucion` · `dissolution` · `cierre de (la )?(empresa|sociedad)` · `liquidar` · `segunda oportunidad` · `second chance` · `redressement` · `cessation de paiements` · `dissoudre`

**`mer_franquicia`** · Franquicia / Franchise · hoja MER-4 (Desarrollo de redes de franquicia)
- Expresiones: `franquicia` · `franchis`

### Laboral (LAB-1 a LAB-4)

**`lab_despido`** · Despido, finiquito e indemnización / Licenciement, solde de tout compte et indemnités · hoja LAB-1 (Asesoría en derecho laboral y contratación)
- Expresiones: `despido` · `despedid` · `dismissal` · `licenciement` · `licencie` · `\bfired\b` · `rupture conventionnelle` · `finiquito` · `indemnizacion por despido` · `severance` · `preaviso` · `carta de despido` · `dimision` · `resignation` · `demission` · `\bere\b` · `\berte\b` · `redundan` · `indemnite de licenciement` · `termination of (my )?(employment|contract)` · `terminated` · `despidos? colectivo` · `увольн`

**`lab_contrato`** · Contrato de trabajo, convenio, jornada y vacaciones / Contrat de travail, convention, temps de travail · hoja LAB-1 (Asesoría en derecho laboral y contratación)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable).
- Expresiones: `contrato de trabajo` · `employment contract` · `contrat de travail` · `contratar` · `contratacion` · `\bhiring\b` · `\bhire\b` · `embauche` · `embaucher` · `empleado` · `employee` · `salarie` · `periodo de prueba` · `trial period` · `periode d.essai` · `convenio colectivo` · `collective agreement` · `convention collective` · `jornada` · `horas extra` · `overtime` · `heures supplementaires` · `vacaciones` · `conges payes` · `labor law` · `derecho laboral` · `droit du travail` · `employment law` · `employer` · `empleador` · `employeur` · `droits? (au|du) travail` · `droit social` · `derechos laborales` · `труд` · `работодател` · `увольн` · `prud.?hom`

**`lab_salario`** · Nóminas, impago de salarios, reclamaciones / Salaires impayés, réclamations · hoja LAB-1 (Asesoría en derecho laboral y contratación)
- Tipo: débil (cuenta con 2 o más coincidencias, o si el área coincide con el desplegable).
- Expresiones: `nomina` · `payroll` · `paie\b` · `impago de salario` · `salario` · `salary` · `sueldo` · `salaire` · `reclamar (mi )?(salario|sueldo)` · `atrasos` · `unpaid wages` · `wages`

**`lab_accidente_baja`** · Accidente laboral, baja médica, incapacidad / Accident du travail, arrêt maladie, invalidité · hoja LAB-1 (Asesoría en derecho laboral y contratación)
- Expresiones: `accidente de trabajo` · `accident du travail` · `baja medica` · `incapacidad temporal` · `arret maladie` · `sick leave` · `work accident` · `enfermedad profesional` · `maladie professionnelle` · `\bmutua\b` · `incapacite` · `baja laboral` · `baja por` · `de baja\b` · `en baja\b` · `arret de travail` · `bajas? medic` · `больничн`

**`lab_acoso`** · Acoso o discriminación laboral / Harcèlement ou discrimination au travail · hoja LAB-1 (Asesoría en derecho laboral y contratación)
- Expresiones: `acoso laboral` · `acoso` · `harassment` · `harcelement` · `mobbing` · `discrimin`

**`lab_rrhh`** · Recursos humanos (reclutamiento, políticas de personal) / Ressources humaines (recrutement, politiques) · hoja LAB-2 (Asesoramiento en recursos humanos)
- Expresiones: `recursos humanos` · `human resources` · `ressources humaines` · `\brrhh\b` · `\brh\b` · `\bhr\b` · `reclutamiento` · `recruitment` · `recrutement` · `politica de personal` · `plan de carrera` · `evaluacion de desempeno` · `teletrabajo en la empresa` · `remote work policy`

**`lab_compliance`** · Compliance laboral (igualdad, canal de denuncias, registro horario) / Compliance social (égalité, alerte, temps de travail) · hoja LAB-3 (Compliance laboral)
- Expresiones: `plan de igualdad` · `equality plan` · `registro horario` · `time tracking` · `canal de denuncias` · `whistleblow` · `lanceur d.alerte` · `prevencion de riesgos` · `riesgos laborales` · `protocolo de acoso` · `compliance` · `cumplimiento normativo` · `code de conduite`

**`lab_empresa`** · Asesoría laboral para empresas (altas, desplazados, inspecciones) / Conseil social entreprise (affiliations, détachés, inspections) · hoja LAB-4 (Asesoramiento laboral para empresas)
- Expresiones: `asesoria laboral` · `labour advice` · `labor advice` · `conseil social` · `inspeccion de trabajo` · `labour inspection` · `inspection du travail` · `trabajador extranjero` · `contratar a un extranjero` · `hire a foreign` · `embaucher un etranger` · `trabajadores desplazados` · `travailleur detache` · `detache` · `posted worker` · `certificado a1` · `formulario a1` · `\ba1\b` · `seguridad social de (la )?empresa` · `alta de trabajador` · `cotizaciones de (los )?trabajadores` · `entreprise.{0,20}salaries.{0,20}espagne` · `empresa.{0,25}empleados`

### Fuera de ámbito (OTR-0)

**`x_comercial`** · Oferta comercial / publicidad recibida / Démarchage commercial reçu · hoja OTR-0 (Sin tema jurídico / comercial / empleo)
- Tipo: no jurídico (solo si no hay ninguno jurídico).
- Expresiones: `\bseo\b` · `posicionamiento web` · `we offer` · `nous proposons` · `ofrecemos` · `our services` · `digital agency` · `web design` · `diseno web` · `backlink` · `guest post` · `link building` · `propuesta comercial` · `business proposal` · `webinar` · `sponsor` · `publicidad` · `advertis` · `loan offer` · `\bvpn\b` · `software` · `app development` · `lead generation` · `marketing digital` · `growth hacking` · `redes sociales` · `search results` · `keywords` · `top of (google|search)` · `first page of google` · `google ranking` · `traffic` · `backlinks?` · `we help (companies|businesses)` · `boost your` · `increase your (sales|traffic|revenue)` · `mejorar su posicionamiento` · `primera pagina de google` · `nous sommes une (entreprise|societe|agence)` · `we are a (company|agency)` · `somos una (empresa|agencia)` · `sourcing` · `fournisseur` · `proveedor` · `supplier` · `exportation` · `importation` · `import.export` · `cotizacion de`

**`x_empleo`** · Candidatura / búsqueda de empleo en el despacho / Candidature / recherche d'emploi au cabinet · hoja OTR-0 (Sin tema jurídico / comercial / empleo)
- Tipo: no jurídico (solo si no hay ninguno jurídico).
- Expresiones: `oferta de empleo` · `\bjob\b` · `busco trabajo` · `trabajar en su despacho` · `trabajar con ustedes` · `practicas` · `internship` · `\bstage\b` · `curriculum` · `\bcv\b` · `candidature` · `candidatura` · `vacante` · `looking for a job` · `work (for|at) your (firm|company)` · `travailler (chez vous|dans votre cabinet)` · `posicion abierta` · `offre de stage` · `join your team` · `joindre votre equipe` · `integrer votre equipe` · `travailler dans une entreprise` · `demande de travail` · `demande d.emploi` · `cherche un emploi` · `chercher du travail` · `busco empleo` · `je cherche (un )?(travail|emploi)` · `paralegal` · `looking for work` · `find work in spain` · `trouver du travail` · `pasantia` · `becario` · `stagiaire`

**`x_traduccion`** · Traducciones (jurada, documentos) / Traductions (assermentée, documents) · hoja OTR-0 (Sin tema jurídico / comercial / empleo)
- Tipo: no jurídico (solo si no hay ninguno jurídico).
- Expresiones: `traduccion jurada` · `sworn translation` · `traduction assermentee` · `traductor` · `translator` · `traducteur` · `traduccion de` · `translation of` · `traduction de` · `apostilla` · `apostille` · `legalizacion de documentos` · `legalisation`

**`x_cliente_actual`** · Seguimiento de expediente / cliente actual / Suivi de dossier / client existant · hoja OTR-0 (Sin tema jurídico / comercial / empleo)
- Tipo: no jurídico (solo si no hay ninguno jurídico).
- Expresiones: `mi expediente` · `numero de expediente` · `expediente\b` · `mon dossier` · `suivi` · `follow.?up` · `status of my` · `estado de mi` · `ya soy cliente` · `ya somos clientes` · `deja client` · `existing client` · `current client` · `already (a )?client` · `nuestro expediente` · `our case file` · `my case file` · `suite a votre appel` · `votre mail du` · `following your email` · `segun nuestra conversacion` · `following our (call|conversation)` · `as discussed`

## 3. Exclusiones y confusiones (pregunta 3)

### 3.1 Qué excluía o desempataba

**No había listas de exclusión explícitas** (ninguna palabra anulaba un subtema). El desempate salía de estos mecanismos:

- **Expresiones de varias palabras** en lugar de palabras sueltas. Es lo que separaba los pares que preguntáis:
  - *residencia fiscal, tax resident, résidence fiscale, résident fiscal* → `fis_convenio_doble`. *Permiso de residencia, titre de séjour, residence permit* → `ext_general`. La palabra suelta `residencia` solo vive en `ext_general`, que es genérico: si hay un subtema específico (como `fis_convenio_doble`), `ext_general` no se activa.
  - **«renta»**: no existía ninguna regla con la palabra `renta` sola. `fis_irpf` exige *declaración de la renta*, *declaraciones de renta*, *renta francesa*, `\birpf\b`, *modelo 100*, *impôt sur le revenu*, *déclaration de revenus*, *income tax*, *tax return*. *Vivir de rentas* no activa nada y *renta* como alquiler tampoco (el alquiler entra por `alquiler`, `arrendamiento`, `\brent\b`, `louer`, `\bbail\b`).
  - `no lucrativ|non.?lucrativ|\bnlv\b` identifica `ext_no_lucrativa`; no depende de «renta».
- **Genérico frente a específico**: un genérico nunca compite con un específico.
- **Bonus del desplegable (+0,5)**: si la persona marcó «Derecho fiscal», los subtemas fiscales ganan los empates.
- **Subtemas amplios (x0,4)**: `ext_visado`, `ext_denegacion`, `suc_litigio`, `fis_iva_conta`, `fis_inspeccion`, `mer_contratos`, `inm_registro`, `ext_instalacion`, `ext_empadronamiento`, `ext_renovacion_larga`, `ext_banca`, `ext_seguro_salud`, `ext_sanidad_ss`. Aparecen en muchas frases y no deben ganar frente a uno específico.
- **Débiles**: ver sección 2; evitan que una palabra común (*salario*, *contrato*, *master*, *reforma*) active un subtema por sí sola.

### 3.2 Errores típicos y confusiones

Revisión manual de 24 casos aleatorios (ES y FR) y de las solicitudes que quedaron sin etiqueta en la primera pasada. Tipos de error, ya corregidos salvo indicación:

1. **Palabras inglesas con otro sentido**: *will* (testamento) en *we will…*. Corregido con expresiones de varias palabras (*last will*, *my will*, *the will*, *will and testament*).
2. **Mensajes comerciales con palabras jurídicas**: un correo de posicionamiento web se etiquetó como herencia por el mismo *will*. Corregido: `x_comercial` ampliado (*search results*, *keywords*, *backlinks*, *we help companies*…).
3. **Plural o variante no cubierta**: *nómadas digitales* no casaba con `nomada digital`. Corregido con `nomadas? digital(es)?`.
4. **Abreviaturas y frases cortas en francés** (*achat appart…*, *projet d'achat*) sin etiqueta. Corregido con `projet d?.?achat|achat appart|achat d.appart|achat maison|achat terrain`.
5. **«Régularisation / regularización» es ambigua**: puede ser la regularización masiva de 2026, regularizar la situación administrativa de una persona, o una regularización fiscal. Se separó en tres: `ext_regularizacion` (solo con *extraordinaria, masiva, colectiva, general, 2026, amnistía*), `ext_irregularidad` (situación o estancia de una persona) y `fis_inspeccion` (*régularisation fiscale*, regularizar con Hacienda).
6. **«Renovación» demasiado amplia** (renovar un contrato, un seguro). Se limitó a tarjeta, TIE, residencia, autorización o permiso.
7. **«Visado/visa» ganaba como tema principal** cuando aparecía junto a un subtema más específico (nómada, no lucrativa, estudios). Se resolvió con el factor x0,4 de los amplios.
8. **Nóminas**: `nominas` estaba en contabilidad y las nóminas de un trabajador son laboral. Pasó a `lab_salario`.
9. **Falsos positivos de palabras comunes**: *master*, *student*, *reforma*, *contrato de…*, *salary*, *loan*. Los subtemas afectados pasaron a débiles o se quitó la expresión genérica `contrato de|contrat de`.
10. **Derecho extranjero** (no corregido): consultas sobre la nacionalidad francesa o británica se etiquetan como `ext_nacionalidad`. Cuentan como demanda de nacionalidad pero **no es derecho español**; conviene un campo aparte si queréis filtrarlas.
11. **Mensajes en cirílico dentro del formulario ES**: sin raíces rusas quedaban sin etiqueta. Se añadió un conjunto mínimo (sección 5).

**Pares de subtemas que más se confundían** (y qué hacer en vuestro motor):

| Par | Por qué se confunden | Sugerencia |
|---|---|---|
| `ext_visado` y `ext_nomada`, `ext_no_lucrativa`, `ext_trabajo`, `ext_estudios` | «visado» aparece en todos | Tratar `ext_visado` como modificador, nunca como principal si hay otro `ext_*` |
| `ext_visado` y `ext_denegacion` | recurso o requerimiento sobre un visado | Mostrar ambos |
| `fis_convenio_doble`, `fis_irpf`, `fis_no_residente` | misma persona, tres preguntas | Etiqueta combinada «Fiscalidad del expatriado» (sección 6) |
| `fis_iva_conta`, `mer_autonomo`, `mer_creacion` | gestoría, alta y constitución van juntos | Pregunta única de «qué necesita» en el paso 3 |
| `ext_nie_tie`, `ext_empadronamiento`, `ext_instalacion` | pasos de una misma llegada | Etiqueta «Pack llegada» |
| `inm_registro` y `suc_herencia` | la escritura y el notario aparecen en herencias | `inm_registro` es auxiliar; no cuenta para multitema |
| `suc_litigio` y `inm_conflicto_arrend` | impagos y desahucios frente a reclamaciones | Si hay `inm_*`, la ruta es Inmueble |
| `lab_contrato` y `mer_contratos` | «contrato» a secas | Ambos son débiles: exigen dos coincidencias o el desplegable |
| `fis_planificacion`, `suc_herencia`, `fis_sucesiones_impuesto` | planificar en vida o tras un fallecimiento | Ruta «Herencia»: primera pregunta «¿hay un fallecimiento o planifica en vida?» |

### 3.3 Debilidades que conocemos y no están resueltas

- **`permiso de residencia` se pierde** si hay otro subtema específico en la solicitud, porque solo existe como genérico. Recomiendo convertirlo en subtema específico (`ext_residencia`: *permiso de residencia, autorización de residencia, titre de séjour, carte de séjour, residence permit, residency permit, вид на жительство, ВНЖ*).
- **«renta»** solo se reconoce en expresiones concretas. Una regla propia sería: `renta` precedida de *declaración (de la)*, *impuesto sobre la* o *IRPF* → `fis_irpf`; precedida de *vivir de* o *rentas pasivas* → `ext_no_lucrativa`; en cualquier otro contexto, sin etiqueta.
- **«residencia»**: añadiría una exclusión explícita: si aparece `fiscal` a menos de 15 caracteres, no activar `ext_general`.
- **Negaciones** (*no quiero comprar*, *no tengo hipoteca*) no se tratan: el motor solo detecta presencia de palabras.
- **Proximidad**: dos subtemas en un mismo mensaje largo se tratan como una sola solicitud multitema aunque hablen de cosas distintas.

## 4. Inglés (pregunta 4)

Estado: del formulario EN general (343 entradas) **solo conocemos el desplegable y la página de origen**. Lo que sigue combina (a) las expresiones inglesas que ya estaban implementadas, con ✔, y (b) sugerencias por conocimiento del sector, con ➕, **sin validar con datos**. Todas son genéricas; no son citas de mensajes. Del formulario de inmigración EN (33 mensajes) y de 44 mensajes en inglés llegados por los formularios ES y FR sale la estructura típica: nacionalidad o residencia actual, objetivo, plazo y petición de honorarios o de cita.

**Estructura típica de un mensaje (ejemplos inventados):**

- *I am a [nationality] citizen living in [country]. We plan to move to Valencia in [month]. Which visa fits us and what are your fees?*
- *I work remotely for a foreign company and want to know if I qualify for the digital nomad visa, and how my family can join.*
- *I recently bought a property in Spain and need help with the NIE, the deed and taxes as a non-resident.*
- *My partner is a non-EU citizen. How can we get residence together?*
- *I overstayed my 90 days and want to know the consequences for a future visa.*

| Subtema(s) | Expresiones en inglés (✔ implementado, ➕ sugerencia sin validar) |
|---|---|
| `ext_nie_tie` | ✔ NIE number · TIE card · residence card · ➕ get my NIE · NIE appointment · fingerprints appointment · foreigner identity number |
| `ext_nomada` | ✔ digital nomad visa · DNV · remote work visa · remote worker · work remotely · ➕ teleworker visa · international telework authorisation · freelancer visa · certificate of coverage · Startup Law |
| `ext_no_lucrativa` | ✔ non-lucrative visa · NLV · ➕ retire to Spain · passive income visa · visa without working · proof of funds · private health insurance for the visa |
| `ext_inversor` | ✔ golden visa · investor visa · ➕ residence by investment · buy property for residency · real estate investment visa |
| `ext_trabajo` | ✔ work permit · work visa · job offer · highly qualified · blue card · shortage occupation · labour market test · ➕ employer sponsorship · work and residence authorisation · change from student to work |
| `ext_emprendedor` | ✔ entrepreneur · startup · ENISA · ➕ start a business to get residency · business plan for the visa · self-employed permit |
| `ext_estudios` | ✔ student visa · student permit · ➕ study in Spain · master's degree · extend my student stay · switch from student to work |
| `ext_arraigo` | ✔ arraigo · ➕ social roots · roots permit · three years in Spain |
| `ext_reagrupacion` | ✔ family reunification · dependent · unmarried partner · partner visa · spouse visa · bring my wife/husband/partner/family · ➕ EU family member card · parents visa · children join me |
| `ext_nacionalidad` | ✔ Spanish citizenship · citizenship application · obtain citizenship · ➕ nationality by residence · citizenship exam · grandparents law · democratic memory law · dual citizenship |
| `ext_regularizacion` | ✔ amnesty · extraordinary regularisation · migrant amnesty · ➕ regularisation 2026 · undocumented · documents for the regularisation |
| `ext_asilo` | ✔ asylum · international protection · refugee · humanitarian · domestic violence · ➕ victim of gender violence permit |
| `ext_renovacion_larga` | ✔ long-term residence · permanent residence · renew my TIE/permit/visa · ➕ my residence expires · extend my residency |
| `ext_brexit` | ✔ Brexit · withdrawal agreement · Article 50 · ➕ British citizen resident before 2021 · green TIE · Brexit TIE |
| `ext_visado` | ✔ visa · consulate · embassy · ➕ visa appointment · visa application |
| `ext_denegacion` | ✔ denied · denial · appeal · ➕ refused · rejected · request for additional documents · resolution |
| `ext_irregularidad` | ✔ overstay · exceeded 90 days · irregular · ➕ Schengen 90/180 · expelled · exit ban · entry ban · undocumented |
| `ext_empadronamiento, ext_sanidad_ss, ext_carnet, ext_homologacion` | ✔ health card · social security number · driving licence · recognition of degree · ➕ register at the town hall (padrón) · certificate of residence · swap my licence · validate my diploma |
| `ext_instalacion` | ✔ relocate · moving to Spain · move to Valencia · settle in Spain · ➕ set up our life in Spain · arrive in [month] |
| `ext_jubilacion, ext_seguro_salud` | ✔ retire · retirement · unemployment benefit · health insurance · private health insurance · ➕ state pension from the UK · S1 form · pension abroad |
| `inm_compra, inm_venta` | ✔ buy a property/house/apartment/villa/land · property purchase · sell my property · ➕ reservation contract · deposit · buyer's lawyer · due diligence · sell my house |
| `inm_alquiler, inm_conflicto_arrend, inm_turistico` | ✔ landlord · lease · rental contract · unpaid rent · squatter · Airbnb · holiday let · short-term rental · ➕ tenant rights · tourist licence · tourist rental registration |
| `inm_comunidad, inm_hipoteca, inm_obras, inm_registro` | ✔ community of owners · homeowners · mortgage · renovation · building permit · planning permission · title deed · land registry · ➕ service charges · mortgage as a non-resident · construction defects · nota simple · encumbrances |
| `suc_herencia` | ✔ inheritance · last will · will and testament · probate · deceased · heir · estate of · ➕ succession · inherited property in Spain · heirs abroad |
| `suc_litigio, suc_familia, suc_penal` | ✔ lawsuit · dispute · legal action · unpaid invoice · debt recovery · scam · fraud · divorce · child custody · prenup · adoption · criminal case · police report · arrest · money laundering · ➕ mediation · separation agreement |
| `fis_convenio_doble, fis_irpf, fis_no_residente` | ✔ tax residence · tax resident · double taxation · tax treaty · exit tax · income tax · tax return · file my taxes · ➕ non-resident tax · Modelo 210 · 183 days · resident for tax purposes · foreign income |
| `fis_beckham` | ✔ Beckham law · inbound expatriate regime · expatriate regime · ➕ special regime for impatriates · Beckham for digital nomads |
| `fis_patrimonio_720, fis_plusvalia, fis_cripto, fis_inspeccion` | ✔ wealth tax · foreign assets · Modelo 720 · capital gain · crypto · tax audit · tax notice · tax authority · ➕ declare foreign accounts · tax on selling property · crypto tax · letter from the tax office |
| `fis_iva_conta, fis_sucesiones_impuesto, fis_planificacion` | ✔ VAT · accounting · bookkeeping · accountant · corporate tax · annual accounts · inheritance tax · gift tax · estate planning · holding · trust · tax planning · ➕ invoicing · bookkeeper · tax advisor |
| `mer_creacion, mer_autonomo, mer_inversion_ext` | ✔ company formation · set up a company · open a business · incorporate · LLC · start-up · self-employed · freelancer · sole trader · independent contractor · permanent establishment · subsidiary · branch · expand to Spain · ➕ register as autónomo · invoice Spanish clients · SL |
| `mer_contratos, mer_compraventa_empresa, mer_pi_rgpd, mer_concurso, mer_franquicia` | ✔ commercial contract · distribution agreement · shareholder agreement · terms and conditions · NDA · share purchase · due diligence · merger · trademark · intellectual property · GDPR · data protection · bankruptcy · restructuring · franchise · ➕ sell my business · dissolve a company · wind up · second chance |
| `lab_*` | ✔ dismissal · fired · severance · termination of employment · employment contract · employee · employer · payroll · salary · unpaid wages · sick leave · work accident · harassment · recruitment · equality plan · whistleblowing · posted workers · A1 certificate · ➕ unfair dismissal · notice period · overtime · hire an employee in Spain · work inspection |
| `x_* (fuera de ámbito)` | ✔ SEO · backlinks · guest post · we help companies · internship · looking for a job · sworn translation · translator · apostille · existing client · follow up · status of my case · ➕ link building · web design · leave a review |

## 5. Ruso (pregunta 5)

Estado: la parte implementada es **mínima** (raíces de 42 expresiones; ningún texto ruso se analizó a fondo). Están **normalizadas**: `й` → `и`, `ё` → `е`, minúsculas. `\w` en Python cubre el cirílico; en JavaScript hay que usar `\p{L}` con la bandera `u` o `[а-я]`.

| Subtema | Raíces implementadas |
|---|---|
| `ext_nomada` | `для удаленнои` · `удаленн\w+ работ` |
| `ext_nacionalidad` | `гражданств` |
| `ext_regularizacion` | `регуляриз` |
| `ext_renovacion_larga` | `пмж` · `постоянн\w+ вид на жительство` · `постоянн\w+ проживан` |
| `ext_visado` | `виз[аыуе]\b` · `визов` |
| `ext_general` | `вид на жительство` · `внж` · `резиденц` · `иммиграц` · `иностранц` |
| `ext_instalacion` | `переезд` · `переехать` |
| `ext_jubilacion` | `пенси` |
| `inm_compra` | `купить` · `покупк\w+ (квартир|дом|недвижим)` |
| `inm_venta` | `продаж\w+ (квартир|дом|недвижим)` · `продать` |
| `inm_general` | `недвижим` · `квартир` · `\bдом\b` |
| `suc_herencia` | `наследств` · `завещан` |
| `suc_litigio` | `судебн` · `\bиск\b` · `спор` |
| `suc_familia` | `разво` |
| `fis_irpf` | `декларац` |
| `fis_general` | `налог` |
| `mer_creacion` | `открыт\w+ (фирм|компани|бизнес)` · `создан\w+ (фирм|компани)` · `регистраци\w+ (компани|фирм)` · `фирм\w+ в испании` |
| `mer_contratos` | `договор` |
| `lab_despido` | `увольн` |
| `lab_contrato` | `труд` · `работодател` · `увольн` |
| `lab_accidente_baja` | `больничн` |

**Sugerencias sin validar con datos** (en forma normalizada, para añadir):

| Subtema | Raíces o expresiones sugeridas |
|---|---|
| `ext_nie_tie` | `\bnie\b` · `ние` |
| `ext_nomada` | `цифров\w+ кочевник` · `digital nomad` · `удаленн\w+ работ` · `виза для удаленн` |
| `ext_no_lucrativa` | `non.?lucrativ` · `без права на работ` · `пассивн\w+ доход` |
| `ext_inversor` | `золот\w+ виз` · `инвестиционн\w+ вид на жительство` · `виза инвестор` |
| `ext_trabajo` | `разрешение на работ` · `рабоч\w+ виз` · `высококвалифицирован` |
| `ext_reagrupacion` | `воссоединени\w+ семь` · `воссоедин` · `супруг` · `пригласить (жену|мужа|детей|родител)` |
| `ext_nacionalidad` | `гражданств` · `натурализац` · `испанск\w+ паспорт` |
| `ext_asilo` | `убежищ` · `беженц` · `международн\w+ защит` |
| `ext_irregularidad` | `нелегальн` · `просроч\w+ (виз|срок)` · `депортац` · `90 дней` |
| `ext_empadronamiento` | `падрон` · `регистрац\w+ по месту жительства` · `empadron` |
| `fis_no_residente` | `нерезидент` · `modelo 210` |
| `fis_convenio_doble` | `налогов\w+ резидент` · `двойн\w+ налогообложен` · `183 дн` |
| `fis_beckham` | `бекхэм` · `beckham` |
| `fis_patrimonio_720` | `modelo 720` · `счет\w* за границ` · `налог на богатств` |
| `fis_sucesiones_impuesto` | `налог на наследств` · `налог на дарени` |
| `inm_compra, inm_alquiler` | `покупк\w+ недвижим` · `купить (квартир|дом|вилл)` · `аренд` · `снять (квартир|жиль)` · `ипотек` |
| `mer_autonomo` | `самозанят` · `автономо` · `индивидуальн\w+ предпринимател` |
| `mer_creacion` | `открыт\w+ (компани|фирм|бизнес|ооо|sl)` · `регистраци\w+ компани` · `основат\w+ компани` |
| `lab_*` | `увольнен` · `трудов\w+ договор` · `зарплат` · `отпуск` · `больничн` |
| `ext_jubilacion` | `пенси` · `пенсион` · `выход на пенси` |
| `x_traduccion` | `присяжн\w+ перевод` · `апостил` · `легализац` |

**Qué temas predominan en los RU** (solo por campos estructurados; el texto no se analizó). Hay 65 solicitudes: 59 del formulario general, 5 del de inmigración y 1 de la ventana emergente.

| Desplegable del formulario general RU | Solicitudes |
|---|---|
| Inmigración | 23 |
| Fiscal | 14 |
| Otro | 11 |
| Laboral | 6 |
| Civil y sucesiones | 3 |
| Comercial | 1 |
| Inmobiliario | 1 |

- Páginas desde las que se envió: contacto 32, página de extranjería 21, portada 8, resto 3.
- El 69 % de quienes dan país está en España (33 de 48); sigue Ucrania con 4 y el prefijo ruso o kazajo (+7) con 3.
- Mi lectura: inmigración y fiscalidad concentran dos tercios; «Otro» (17 %) probablemente esconde sobre todo creación de empresa y nacionalidad, como en ES y FR, pero **no lo he comprobado con el texto**.

## 6. Combinaciones (pregunta 6)

**Criterio de detección.**

1. Se clasifica la solicitud como en la sección 1. La combinación existe si **ambos subtemas están en el conjunto de subtemas** de la solicitud (cualquier orden, sin exigir proximidad).
2. No cuentan los genéricos (`*_general`) ni los no jurídicos (`x_*`).
3. Los nombres («Pack llegada», «Herencia con inmueble»…) **los puse yo a mano**, a partir de los pares más frecuentes de los datos (hoy, 8 o más solicitudes cada uno). No hay un umbral automático ni reglas aparte: es una tabla *par → nombre*.
4. A nivel de ruta del formulario se cuenta del mismo modo, con las 9 rutas de la sección 7.

| Subtema A | Subtema B | Nombre propuesto | Solicitudes |
|---|---|---|---|
| `ext_empadronamiento` | `ext_nie_tie` | Pack llegada | 15 |
| `ext_instalacion` | `ext_nie_tie` | Pack llegada | 12 |
| `fis_convenio_doble` | `fis_irpf` | Fiscalidad del expatriado | 15 |
| `fis_iva_conta` | `mer_creacion` | Constitución y gestoría | 13 |
| `ext_nie_tie` | `mer_creacion` | Empresa y residencia | 13 |
| `ext_emprendedor` | `mer_creacion` | Residencia de emprendedor | 13 |
| `inm_registro` | `suc_herencia` | Herencia con inmueble | 12 |
| `fis_convenio_doble` | `fis_iva_conta` | Fiscalidad de empresa y expatriado | 10 |
| `ext_nie_tie` | `fis_iva_conta` | Llegada y autónomo | 11 |
| `ext_nie_tie` | `inm_compra` | Comprar y residir | 10 |
| `fis_iva_conta` | `mer_autonomo` | Autónomo y gestoría | 10 |
| `ext_instalacion` | `mer_creacion` | Mudanza con empresa | 10 |
| `fis_sucesiones_impuesto` | `suc_herencia` | Herencia y su impuesto | 9 |
| `fis_irpf` | `fis_iva_conta` | Renta y contabilidad | 9 |
| `fis_convenio_doble` | `suc_herencia` | Herencia internacional | 8 |

Otras parejas frecuentes sin nombre todavía: `mer_autonomo` + `mer_creacion` (9), `ext_estudios` + `ext_visado` (8), `fis_convenio_doble` + `mer_autonomo` (8), `ext_nacionalidad` + `suc_familia` (7), `fis_irpf` + `inm_alquiler` (7), `ext_nacionalidad` + `ext_nie_tie` (7), `ext_reagrupacion` + `ext_visado` (7), `inm_compra` + `inm_registro` (7), `ext_empadronamiento` + `fis_convenio_doble` (7), `ext_nomada` + `ext_reagrupacion` (7).

## 7. Rutas del formulario y su correspondencia con subtemas

Son las 9 rutas del paso 1 que propone el informe. Cada subtema pertenece a **una** ruta; una solicitud puede activar varias.

| Ruta | Subtemas | Solicitudes con alguno |
|---|---|---|
| Residir, trabajar o estudiar en España (`residencia`) | `ext_nomada`, `ext_no_lucrativa`, `ext_inversor`, `ext_trabajo`, `ext_emprendedor`, `ext_estudios`, `ext_arraigo`, `ext_reagrupacion`, `ext_nacionalidad`, `ext_regularizacion`, `ext_asilo`, `ext_renovacion_larga`, `ext_brexit`, `ext_visado`, `ext_denegacion`, `ext_irregularidad`, `ext_general` | 260 |
| Llegar y organizarse (NIE, padrón, sanidad, banco) (`llegada`) | `ext_nie_tie`, `ext_empadronamiento`, `ext_sanidad_ss`, `ext_carnet`, `ext_homologacion`, `ext_instalacion`, `ext_banca` | 131 |
| Comprar, vender o alquilar un inmueble (`inmueble`) | `inm_compra`, `inm_venta`, `inm_alquiler`, `inm_conflicto_arrend`, `inm_comunidad`, `inm_turistico`, `inm_hipoteca`, `inm_obras`, `inm_registro`, `inm_general` | 174 |
| Crear o gestionar una empresa (`empresa`) | `mer_creacion`, `mer_autonomo`, `mer_inversion_ext`, `mer_contratos`, `mer_compraventa_empresa`, `mer_pi_rgpd`, `mer_concurso`, `mer_franquicia` | 112 |
| Impuestos y fiscalidad (`impuestos`) | `fis_convenio_doble`, `fis_irpf`, `fis_no_residente`, `fis_beckham`, `fis_patrimonio_720`, `fis_plusvalia`, `fis_cripto`, `fis_inspeccion`, `fis_iva_conta`, `fis_general` | 193 |
| Herencia, testamento y patrimonio (`herencia`) | `suc_herencia`, `fis_sucesiones_impuesto`, `fis_planificacion` | 96 |
| Trabajo y empleo (`trabajo`) | `lab_despido`, `lab_contrato`, `lab_salario`, `lab_accidente_baja`, `lab_acoso`, `lab_rrhh`, `lab_compliance`, `lab_empresa` | 56 |
| Jubilación, pensiones y seguro médico (`jubilacion`) | `ext_jubilacion`, `ext_seguro_salud` | 44 |
| Conflicto, reclamación o familia (`conflicto`) | `suc_litigio`, `suc_familia`, `suc_penal` | 44 |

Solapamientos más frecuentes entre rutas: Llegar y organizarse (NIE, padrón, sanidad, banco) + Residir, trabajar o estudiar en España (48); Impuestos y fiscalidad + Residir, trabajar o estudiar en España (42); Crear o gestionar una empresa + Residir, trabajar o estudiar en España (38); Crear o gestionar una empresa + Impuestos y fiscalidad (33); Impuestos y fiscalidad + Comprar, vender o alquilar un inmueble (33).

## 8. Recomendaciones para vuestro motor

1. Empezad con las reglas **específicas** y tratad los modificadores amplios aparte; un motor con pocos subtemas fiables funciona mejor que uno con muchos ruidosos.
2. Mostrad **sugerencias, no una clasificación única**: hasta 3 temas, con el principal destacado. El 36 % de las solicitudes toca varios.
3. Normalizad igual que en el paso 2 de la sección 1; la mayoría de los fallos al portar reglas vienen de acentos y apóstrofos.
4. Registrad (sin texto) qué subtemas se mostraron y cuáles eligió la persona. Con 200 o 300 selecciones se pueden recalibrar los pesos sin necesidad de datos de solicitudes.
5. Añadid `ext_residencia` y las reglas de «renta» y «residencia fiscal» de la sección 3.3 antes de lanzar.
6. El inglés y el ruso necesitan una primera tanda de validación con tráfico real del nuevo formulario.

## 9. Anexo: expresiones reales y frecuentes por subtema

Son **expresiones reales**, no inventadas, pero tratadas para que no identifiquen a nadie:

- Se extraen solo las **palabras que activaron la regla** de cada subtema (la expresión coincidente, sin el texto de alrededor).
- Solo se listan las que aparecen en **5 o más solicitudes distintas** (anonimato k = 5). Lo que aparece menos veces no figura.
- Sin dígitos, sin nombres de personas ni del despacho, sin frases ni mensajes completos. Minúsculas y sin acentos, como en el motor.
- Base: los 708 mensajes de texto de los formularios ES general (190), FR general (464) y extranjería ES (54). EN, RU e inmigración FR no se analizaron.

**Por qué solo expresiones y no frases.** Con dos palabras de contexto a cada lado ninguna secuencia real se repite en 5 solicitudes: cada mensaje es único y reproducir frases enteras equivaldría a entregar texto de personas concretas. Con la expresión sola sí hay repetición suficiente.

| Subtema | Expresión real | Solicitudes |
|---|---|---|
| `ext_nie_tie` | `nie` | 68 |
| `ext_nie_tie` | `tie` | 5 |
| `ext_nomada` | `teletravail` | 12 |
| `ext_nomada` | `digital nomad` | 7 |
| `ext_trabajo` | `permis de travail` | 5 |
| `ext_emprendedor` | `entrepreneur` | 15 |
| `ext_estudios` | `etudiant` | 8 |
| `ext_estudios` | `master` | 5 |
| `ext_arraigo` | `arraigo` | 7 |
| `ext_reagrupacion` | `reagrupacion` | 6 |
| `ext_reagrupacion` | `regroupement familial` | 5 |
| `ext_nacionalidad` | `nationalite francaise` | 8 |
| `ext_nacionalidad` | `demande de nationalite` | 5 |
| `ext_visado` | `visa` | 34 |
| `ext_visado` | `visado` | 9 |
| `ext_visado` | `consulat` | 6 |
| `ext_denegacion` | `refuse` | 9 |
| `ext_denegacion` | `recours` | 7 |
| `ext_denegacion` | `denegacion` | 5 |
| `ext_irregularidad` | `regulariser ma` | 12 |
| `ext_irregularidad` | `regularizar mi situacion` | 5 |
| `ext_empadronamiento` | `empadronamiento` | 12 |
| `ext_instalacion` | `m'installer` | 20 |
| `ext_instalacion` | `expatriation` | 15 |
| `ext_jubilacion` | `retraite` | 11 |
| `ext_jubilacion` | `retraites` | 6 |
| `ext_jubilacion` | `retraitee` | 5 |
| `ext_banca` | `bancaire` | 7 |
| `ext_banca` | `compte bancaire` | 6 |
| `ext_banca` | `prelevement` | 5 |
| `inm_compra` | `achat immobilier` | 12 |
| `inm_compra` | `l'achat d'un` | 11 |
| `inm_compra` | `acquerir` | 9 |
| `inm_compra` | `contrato de arras` | 7 |
| `inm_compra` | `achat d'un` | 6 |
| `inm_alquiler` | `alquiler` | 7 |
| `inm_alquiler` | `locatifs` | 5 |
| `inm_obras` | `construction` | 5 |
| `inm_registro` | `embargo` | 8 |
| `inm_registro` | `notarial` | 8 |
| `inm_registro` | `escritura` | 7 |
| `inm_registro` | `notaria` | 7 |
| `suc_herencia` | `succession` | 22 |
| `suc_herencia` | `herencia` | 12 |
| `suc_herencia` | `sucesion` | 8 |
| `suc_herencia` | `decede` | 6 |
| `suc_herencia` | `heritage` | 5 |
| `suc_herencia` | `sucesiones` | 5 |
| `suc_herencia` | `testament` | 5 |
| `suc_litigio` | `reclamacion` | 9 |
| `suc_litigio` | `litige` | 8 |
| `suc_litigio` | `conflicto` | 5 |
| `suc_familia` | `mariage` | 5 |
| `suc_familia` | `matrimonio` | 5 |
| `fis_sucesiones_impuesto` | `donation` | 10 |
| `fis_sucesiones_impuesto` | `donacion` | 6 |
| `fis_sucesiones_impuesto` | `donaciones` | 5 |
| `fis_planificacion` | `holding` | 8 |
| `fis_convenio_doble` | `residence fiscale` | 17 |
| `fis_convenio_doble` | `residente fiscal` | 9 |
| `fis_convenio_doble` | `residencia fiscal` | 7 |
| `fis_convenio_doble` | `residente fiscale` | 5 |
| `fis_irpf` | `irpf` | 10 |
| `fis_irpf` | `declaration d'impots` | 7 |
| `fis_irpf` | `declaration fiscale` | 6 |
| `fis_no_residente` | `non resident` | 12 |
| `fis_beckham` | `beckham` | 14 |
| `fis_beckham` | `ley beckham` | 5 |
| `fis_inspeccion` | `hacienda` | 14 |
| `fis_iva_conta` | `comptabilite` | 10 |
| `fis_iva_conta` | `contable` | 5 |
| `fis_iva_conta` | `iva` | 5 |
| `mer_creacion` | `sl` | 10 |
| `mer_creacion` | `creation d'entreprise` | 9 |
| `mer_creacion` | `creer une societe` | 9 |
| `mer_creacion` | `s l` | 8 |
| `mer_creacion` | `creation de societe` | 6 |
| `mer_autonomo` | `autonomo` | 28 |
| `mer_autonomo` | `freelance` | 8 |
| `mer_autonomo` | `auto entrepreneur` | 6 |
| `lab_despido` | `despido` | 6 |
| `lab_contrato` | `contrat de travail` | 11 |
| `lab_contrato` | `jornada` | 6 |
| `lab_contrato` | `salarie` | 6 |
| `lab_contrato` | `contratar` | 5 |
| `lab_contrato` | `salaries` | 5 |
| `lab_salario` | `salaire` | 6 |

Total: 87 expresiones en 35 subtemas. Los demás subtemas no tienen ninguna expresión con 5 o más apariciones (se activan con formas muy variadas o son poco frecuentes).

**Lectura útil para las reglas**: las formas más repetidas confirman qué palabras cortas y variantes conviene incluir (por ejemplo la forma sin plural, la variante sin artículo o la sigla). Las que figuran aquí con apóstrofo corresponden al texto ya normalizado.
