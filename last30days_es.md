---
tags: ["Applications", "Generative AI", "Ethics & Society"]
date: 2026-07-01
author: "Dario Ferrero"
---

# Last30days: cuando un agente de código se convierte en un motor de búsqueda social
![last30days.jpg](last30days.jpg)

*Antes de escribir algo sobre la IA, abrí once pestañas del navegador: Reddit, X, YouTube, Hacker News, GitHub, algunas newsletters del sector. Dos horas después, tres cafés mediante, había encontrado tres posts realmente útiles. El resto era ruido: artículos de blog optimizados para motores de búsqueda, opiniones de personas pagadas por tenerlas, clásicas galerías del tipo "las diez herramientas de IA que cambiarán su vida" escritas con la misma profundidad que una hoja de instrucciones de un mueble de IKEA.*

El problema no es la cantidad de información. Es que los sistemas que utilizamos para navegarla han sido diseñados para atacar a los algoritmos, no para reflejar lo que la gente piensa de verdad. Google indexa editores. Reddit, X y YouTube indexan personas. Son ecosistemas fundamentalmente diferentes, cada uno cerrado en su propio jardín vallado, cada uno con sus propias API, sus propios tokens de autenticación, sus propias lógicas de acceso.

[`/last30days`](https://github.com/mvanhorn/last30days-skill) es un intento de derribar esas vallas. No es un motor de búsqueda en el sentido tradicional: es una skill para agentes de código que interroga en paralelo a Reddit, X, YouTube, Hacker News, TikTok, GitHub, Polymarket y otros, fusiona los resultados y entrega una síntesis estructurada en pocos minutos. Escrito por Matthew Van Horn, ha alcanzado las 41.500 estrellas en GitHub, clasificándose como el repositorio número uno del día en su semana de lanzamiento. Las cifras por sí solas no dicen mucho, pero cuentan la intensidad de una necesidad real.

## Dentro de la máquina: arquitectura v3

La versión tres del proyecto, la actual, está construida en torno a una idea sencilla pero potente: no buscar lo que habéis escrito, entender primero *dónde* buscarlo. El README oficial del repositorio describe el flujo en siete pasos, pero la parte interesante es lo que sucede antes de que se realice una sola llamada a la API.

El motor utiliza un sistema de fusión de rankings llamado Reciprocal Rank Fusion, abreviado RRF. En lugar de confiar la relevancia a una única fuente o a un único algoritmo, RRF toma los resultados de múltiples fuentes, cada una con su propia clasificación, y los fusiona en un ranking compuesto que reduce el peso de los valores atípicos y premia la coherencia entre plataformas diferentes. Si un tema emerge con fuerza en Reddit, recibe señal. Si el mismo tema aparece en X y es citado en un video de YouTube, la señal se amplifica. Si, por el contrario, es fuerte solo en una plataforma y silencioso en las demás, se redimensiona.

El otro elemento arquitectónico digno de mención es el clustering automático: cuando la misma historia aparece en Reddit, X y YouTube con títulos diferentes, el motor no la muestra tres veces. La detecta como un único clúster mediante entity-based overlap detection, reconociendo la coincidencia incluso cuando las palabras utilizadas en las diferentes plataformas no coinciden. El resultado es un brief que consolida en lugar de duplicar.

## El cerebro que lee antes de buscar

La función que el README llama "Intelligent Search" es la que separa más claramente esta herramienta de la búsqueda tradicional. Ha sido construida por [Jonas Sperling](https://github.com/j-sperling) y funciona como un pre-research brain, un paso cero que precede a cualquier interrogación a las API externas.

La idea es esta: cuando escribís `/last30days OpenClaw`, el motor no busca literalmente "OpenClaw" en todas las plataformas. Primero resuelve quién y qué hay alrededor de ese término. Entiende que OpenClaw tiene un creador, Peter Steinberger, que en X es `@steipete`, que en GitHub el repositorio principal es `steipete/openclaw`, que las discusiones relevantes se encuentran en subreddits como `r/ClaudeCode`. Luego busca todo esto en paralelo, ya orientado. La diferencia con respecto a la versión anterior, escribe Van Horn en el README, es estructural: "El antiguo motor buscaba palabras clave. El nuevo entiende vuestro tema primero, luego busca a las personas y comunidades adecuadas".

Esto resuelve uno de los problemas más molestos de la búsqueda contextual: la ambigüedad. Si buscáis "Paperclip", ¿os referís a la startup de IA o al pequeño alambre para sujetar papeles? El motor resuelve `@dotta` y entiende que estáis hablando de lo primero. Si buscáis "Dave Morin", obtenéis no solo su perfil de X sino también las conexiones con OpenClaw y las citas del podcast TWiST. La disambiguación ocurre antes de la búsqueda, no después.

## Dos jueces, no uno

Uno de los elementos más inusuales de `/last30days` es la presencia de un segundo juez en el proceso de síntesis. El primero evalúa la relevancia: cuánto un resultado es pertinente a la consulta, cuán reciente es, cuánto engagement ha recibido. El segundo evalúa algo diferente: humor, ingenio, viralidad.

La motivación es práctica. Reddit y X producen diariamente síntesis brillantes, bromas perfectas, comentarios que capturan la esencia de un fenómeno mejor que cualquier análisis. El antiguo sistema los enterraba porque no eran "relevantes" en el sentido estricto del término. Un comentario como "My Michael Jordan is Steve Kerr" en un hilo sobre Arizona Basketball puntúa bajo en pertinencia temática, pero altísimo en calidad expresiva.

El resultado es una sección final llamada "Best Takes" que recoge las citas más vivaces, las ocurrencias más compartidas, las reacciones que invitan a volver sobre el tema. No es una función decorativa: es el reconocimiento de que la cultura digital se mueve a menudo a través de la broma adecuada en el momento adecuado, no a través del análisis más preciso.

## Comparaciones en paralelo, no en serie

Otra función introducida en la v3 merece atención porque resuelve un problema práctico que cualquiera que haya intentado comparar dos herramientas competidoras conoce bien. En las versiones anteriores, una consulta como `/last30days "OpenClaw vs Hermes vs Paperclip"` ejecutaba tres búsquedas en serie: primero una, luego la otra, luego la última. El tiempo de ejecución podía superar los doce minutos. La v3 ejecuta, en cambio, una única pasada con subconsultas entitad-conscientes para todos los sujetos simultáneamente, reduciendo el tiempo a unos tres minutos con la misma profundidad de análisis.

Existe también la modalidad `--competitors`, que funciona de forma aún más autónoma: dado un sujeto, el motor descubre por sí solo a los principales competidores mediante búsqueda web, luego inicia pipelines paralelos para cada uno y los fusiona en una comparación estructurada. Es el tipo de función que transforma una herramienta de búsqueda en algo que se parece a un analista junior: no se limita a responder a la pregunta que habéis hecho, sino que construye el contexto en el que esa respuesta tiene sentido.

## Quince plataformas, un brief

La tabla de fuentes soportadas en el [repositorio](https://github.com/mvanhorn/last30days-skill) es larga: Reddit, X, YouTube, TikTok, Instagram Reels, Hacker News, Polymarket, GitHub, Digg, Threads, Pinterest, Bluesky, Perplexity, búsqueda web tradicional. Algunas son gratuitas y funcionan sin configuración (Reddit con comentarios, HN, Polymarket, GitHub). Otras requieren autenticación o claves de API de pago.

La presencia de Polymarket es particularmente interesante: no recoge opiniones, recoge cuotas. Las probabilidades en Polymarket son determinadas por quienes ponen dinero real en la predicción, no por quienes quieren parecer informados. Hay una diferencia epistémica significativa entre "muchos piensan que X sucederá" y "el 74% de los capitales apuesta a que X sucederá antes de diciembre". El motor lo muestra como una señal separada, con los porcentajes de probabilidad, no los volúmenes en dólares, porque la magia está en la cuota, no en la cantidad.

Para GitHub existe también el llamado "person-mode": cuando la consulta se refiere a una persona específica, el motor deja de buscar quién habla de ella y comienza a buscar qué está construyendo esa persona en realidad. El comando `/last30days Peter Steinberger --github-user=steipete` devuelve no una reseña de prensa sobre Steinberger, sino un mapa de su trabajo: cuántas pull requests ha hecho en el último mes, en qué repositorios, con qué tasa de aprobación, qué ha lanzado.
![tabella1.jpg](tabella1.jpg)
[Las plataformas en las que se realizan las búsquedas](https://github.com/mvanhorn/last30days-skill)

## Opencode: un test sobre el terreno

Cuando vi el proyecto, la pregunta inmediata fue: ¿funciona también fuera del ecosistema Claude Code? La respuesta del repositorio es afirmativa: la skill es instalable en Codex, Cursor, Copilot, Gemini CLI, y mediante el paquete abierto `npx skills add mvanhorn/last30days-skill -g` en más de cincuenta entornos compatibles con el estándar Agent Skills, incluyendo `opencode`.

Instalé la skill en opencode y realicé una búsqueda concreta: las preferencias de los usuarios de opencode sobre qué modelo de lenguaje gratuito o de bajo coste ofrecía la mejor relación calidad-rendimiento. Una consulta de nicho, con una comunidad pequeña pero activa, que un motor de búsqueda tradicional habría satisfecho con cero resultados útiles.

El informe producido atravesó proveedores, foros, discusiones de GitHub y documentación oficial. Destiló que opencode soporta más de 75 proveedores y tres modalidades principales de acceso a los modelos. Entre los gratuitos disponibles de inmediato, sin claves de API: DeepSeek V4 Flash Free, un modelo mixture-of-experts de 284 mil millones de parámetros con un millón de tokens de contexto, distribuido con licencia MIT. Para quienes quisieran gastar diez dólares al mes con OpenCode Go, el modelo con la mejor relación solicitudes/calidad resultaba ser todavía DeepSeek V4 Flash, con unas 158.000 solicitudes mensuales estimadas, mientras que para la calidad absoluta emergían GLM-5.2 y Kimi K2.7 Code, este último especialmente recomendado para agentes MCP complejos. Para quienes no quieren depender de la nube, los modelos locales a través de Ollama o LM Studio estaban documentados en detalle, con Qwen3.6-27B como elección para una sola GPU de 24GB.

El informe se generó como archivo `.md` por petición explícita, citando las fuentes. Tardó aproximadamente un minuto. No fue perfecto: alguna información sobre precios requeriría verificación directa en los sitios de los proveedores, y la comunidad de opencode es lo suficientemente pequeña como para que la muestra sea estadísticamente delgada. Pero para orientarse rápidamente en un panorama que cambia cada semana, era exactamente lo que se necesitaba.

## Los límites que nadie cuenta

La honestidad exige poner sobre la mesa también lo que no funciona, o lo que funciona con costes ocultos.

El primer límite es estructural: las fuentes más ricas, TikTok, Instagram, Threads, YouTube con comentarios, requieren una clave de API de ScrapeCreators, un servicio de pago. Las primeras cien solicitudes son gratuitas, luego se entra en un modelo de pago por uso. Quien quiera la versión completa de la herramienta debe tener en cuenta un coste variable que depende de la intensidad del uso. El modelo "gratis" existe, pero es significativamente más limitado que el descrito en los casos de uso del README.

El segundo límite es epistémico y más sutil. La herramienta optimiza para el engagement: un hilo de Reddit con 1.500 upvotes pesa más que un post de blog que nadie ha leído. En principio tiene sentido. En la práctica, el engagement es una medida de la reactividad emocional tanto como de la calidad informativa. Un post que simplifica, indigna o divierte recoge más upvotes que un análisis matizado. `/last30days` no resuelve este problema: lo hereda de las plataformas que interroga. La síntesis es tan buena como las conversaciones que encuentra, y las conversaciones online tienen sus propios sesgos estructurales.

El tercer límite se refiere a la latencia de los datos: la herramienta busca lo que ha sucedido *en las últimas semanas*, no lo que sucedió ayer por la mañana. Para trend analysis y búsqueda de contexto funciona muy bien. Para breaking news en tiempo real, menos.

Finalmente, una nota sobre la privacidad. El README declara explícitamente que la búsqueda permanece local, ningún dato se transmite a servidores de terceros fuera de las API que el propio usuario configura. Se trata de un proyecto MIT, verificable en el código fuente. Pero quien utiliza `/last30days` con clave de X o ScrapeCreators está autorizando de todos modos a esas plataformas a recibir las consultas: la confidencialidad es, por tanto, relativa; depende de qué fuentes se habiliten.

## Quién gana, quién pierde, quién decide

Desde el punto de vista de los usuarios, `/last30days` responde a una necesidad que las herramientas existentes ignoran sistemáticamente: agregar señales sociales heterogéneas sin pasar horas haciéndolo manualmente. Es particularmente útil en tres contextos: antes de una reunión con alguien cuyo trabajo reciente se quiere entender, cuando se debe evaluar una herramienta nueva en un sector que se mueve rápido, cuando se intenta entender si una tendencia es real o está amplificada por los diez perfiles influyentes de siempre.

Para la categoría de investigadores profesionales y periodistas, la cuestión es más compleja. La herramienta acelera la recopilación pero no sustituye al juicio. El "Best Takes" puede ser valioso para entender cómo reacciona una comunidad, pero seleccionar las bromas más virales no es lo mismo que identificar a las voces más informadas. La optimización para el engagement y la optimización para la verdad son funciones diferentes y, a veces, ortogonales.

Las plataformas que son interrogadas no obtienen nada de este esquema: `/last30days` utiliza sus API o sus datos públicos sin devolver tráfico directo. Es una dinámica ya vista con los motores de búsqueda tradicionales, pero amplificada: aquí no hay ni siquiera el click-through en un enlace. Reddit ya ha emprendido batallas legales contra quienes utilizan sus datos de formas no autorizadas, y no es imposible que en el futuro las condiciones de acceso cambien.

El proyecto, con sus 41.500 estrellas y 3.400 forks, es ya lo suficientemente grande como para atraer la atención. La pregunta no es si funciona: funciona, con las limitaciones descritas. La pregunta es a dónde lleva este paradigma cuando se generaliza. Un agente que interroga en paralelo todas las conversaciones públicas sobre un tema, las fusiona, las sintetiza y entrega una respuesta en un minuto, es una herramienta potente. Como toda herramienta potente, dice mucho más de quien la usa que de sí misma.
