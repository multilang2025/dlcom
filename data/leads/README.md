# Análisis de solicitudes web (formularios de delaguialuzon.com)

Generado el 2026-10-08 a partir de las 1.169 entradas de los 9 formularios de Formidable Forms
(2024-10-21 a 2026-10-07). Informe bilingüe ES/FR: artefacto "Mapa de solicitudes"
(https://claude.ai/artifact/SiUp9zwhQr9DZHP55h4Fe4, privado). El mismo HTML está en `informe-leads.html`.

## Privacidad

Los CSV **no contienen** nombres, correos, teléfonos, nombres de empresa ni texto de mensajes. Solo campos derivados y el
`entry_id` de Formidable (para localizar la entrada en wp-admin). Las direcciones de página se guardan sin parámetros
(sin `gclid` ni `utm`). El texto bruto se leyó en memoria y no se guardó en este repositorio. Regla del proyecto: sin datos
personales de consultas de formularios.

## Archivos

| Archivo | Contenido |
|---|---|
| `leads_es.csv`, `leads_en.csv`, `leads_fr.csv`, `leads_ru.csv` | una fila por solicitud, agrupadas por idioma del formulario |
| `topic_article_map.csv` | por subtema e idioma: artículos publicados cuyo título lo trata (búsqueda por título y slug) |
| `leads_stats.json`, `report_data.json` | cifras agregadas del informe |
| `manual_form10_coding.json` | codificación manual (sin datos personales) del formulario de inmigración EN (33 entradas), cuyo texto se leyó a mano |
| `informe-leads.html` | informe ES/FR (artefacto) |
| `respuesta-taxonomia-es.md` | respuesta a las preguntas del cliente sobre la taxonomía: algoritmo, reglas por subtema, inglés, ruso y combinaciones (sin datos de solicitudes) |
| `informe-leads-es.pptx`, `informe-leads-fr.pptx` | el mismo informe en PowerPoint (22 diapositivas, gráficos y tablas editables), uno por idioma |

## Columnas de los CSV

`entry_id`, `date`, `quarter`, `form`, `form_language`, `form_kind` (general o extranjeria), `client_type`, `dropdown_topic`
(lo elegido en el desplegable), `dropdown_area`, `page_where_submitted`, `traffic_hint` (google_ads, chatgpt, other_utm),
`location_dropdown`, `phone_country` y `phone_country_confidence` (solo el código de país del prefijo),
`country_residence_text` (país donde dice vivir), `lead_country` y `lead_country_source` (texto > desplegable > teléfono),
`nationality_stated` (solo si la persona la declara; códigos ISO, separados por `|`), `family_nationality`, `message_language`,
`message_chars`, `primary_area` (SUC, INM, LAB, MER, FIS, EXT), `primary_leaf` (hoja del árbol de dlvibe), `primary_subtopic`,
`all_leaves`, `all_subtopics`, `multi_topic` (1 si toca dos o más subtemas), `combo_label`, `asks_price`, `asks_appointment`,
`urgent`, `information_seeking`, `lead_nature`, `blog_candidate` (1 si parece solo información), `journey_pages`,
`journey_first_page`, `journey_area`, `blog_posts_read`, `analysis_level` (texto del mensaje o solo campos estructurados).

## Taxonomía

`tools/leads_taxonomy.py`: 6 áreas y 17 hojas de https://dlvibe.delaguialuzon.fr/ (leídas el 2026-10-08) más 3 hojas propuestas
(SUC-0 herencias y testamentos, SUC-2 familia, OTR-0 fuera de ámbito) y 72 subtemas con reglas multilingües (ES, FR, EN, y algo de RU).
Un subtema pertenece a una hoja; una solicitud puede tener varios.

## Límites

- Ningún formulario pregunta país ni nacionalidad: ambos son estimaciones (prefijo, desplegable, texto).
- Texto analizado en 741 de 1.169 entradas: ES general (190), extranjería ES (54), FR general (464) y inmigración EN (33, a mano).
- **Sin texto analizado** (solo campos estructurados): EN general (343), RU (65) e inmigración FR (20). El clasificador de datos
  personales del entorno bloqueó su lectura; hace falta que Mike añada una regla de permiso para `db_query` de AISA si quiere ampliarlo.
- Muestra revisada a mano: 24 casos; el tema principal es razonable en la mayoría y las etiquetas secundarias tienen más ruido.
- Cobertura del blog: coincidencia automática por título y slug; hay que verificarla antes de decidir qué escribir.

## Regenerar

1. Extraer con AISA `db_query` (solo lectura) las entradas de `{prefix}frm_items` y `{prefix}frm_item_metas`. Campos por formulario
   (field_id): ES general (form 2): tipo cliente 18, teléfono 19, tipo consulta 20, asunto 9, mensaje 10. EN general (4): 28, 30, 31, 32, 33.
   FR general (5): 39, 41, 42, 43, 44. RU general (6): 49, 51, 52, 53, 54. Extranjería ES (8): teléfono 73, ubicación 78, mensaje 76.
   Inmigración EN (10): 89, 90, 91. Inmigración FR (11): 96, 97, 98. Inmigración RU (9): 82, 83, 84. Del teléfono pedir solo
   `LEFT(valor, 8)`; no pedir nombre ni correo. Recorrido: `SUBSTRING(description, LOCATE('"user_journey"', description))`.
2. `python -X utf8 tools/leads_analysis.py <raw.pkl>` (la pickle con `(rows, journeys)` queda fuera del repositorio).
3. `python -X utf8 tools/leads_report_data.py` y `python -X utf8 tools/leads_report_build.py`.
4. PowerPoint: `node tools/leads_report_text.js data/leads/informe-leads.html > texts.json` y `python -X utf8 tools/leads_report_pptx.py texts.json` (requiere `pip install python-pptx`).
