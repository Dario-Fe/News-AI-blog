---
tags: ["Research", "Applications", "Generative AI"]
date: 2026-06-01
author: "Dario Ferrero"
---

# Graphify y la memoria que los LLM no tienen
![graphify.jpg](graphify.jpg)

*¿Y si vuestro asistente de IA pudiera dejar de releer todo el proyecto cada vez para responder a una sola pregunta? Graphify, una herramienta de código abierto publicada en GitHub con más de 50.000 estrellas, promete exactamente eso: transformar una carpeta de código, documentos, PDF, imágenes y vídeos en un grafo de conocimiento consultable por agentes de IA, reduciendo drásticamente el número de tókenes consumidos en cada consulta.*

Quienes trabajáis a diario con agentes de IA en proyectos de tamaño medio conocéis bien una frustración específica: cada vez que un asistente como Claude Code, Cursor o Gemini CLI debe responder a una pregunta sobre el proyecto, recorre toda la base de código como si nunca hubiera leído nada. Relee archivos, rēanaliza estructuras, empieza de cero. Es un poco como el detective Lunge de *Monster*, de Naoki Urasawa, que para recordar algo debe reconstruir cada vez toda la cadena deductiva desde el primer indicio, incapaz de conservar un estado intermedio entre las sesiones.

En abril, en estas mismas páginas, analizamos en detalle [la propuesta de Andrej Karpathy para una base de conocimiento evolutiva para LLM](https://aitalk.it/it/llm-knowledge-base.html): construir una wiki estructurada en Markdown que el modelo pudiera compilar y consultar, evitando recargar todo el corpus en el contexto cada vez. La propuesta cosechó más de 16 millones de visualizaciones en X, desencadenando un intenso debate técnico sobre qué arquitectura de memoria era realmente practicable para un uso profesional.

Graphify parte exactamente de esa intuición, citando explícitamente el enfoque de Karpathy en el README como punto de partida, para luego llevarlo más allá: en lugar de una wiki plana en Markdown, construye un grafo de conocimiento donde cada entidad, cada función, cada concepto extraído de vuestros archivos se convierte en un nodo, y las relaciones entre entidades se convierten en aristas navegables. La diferencia no es estética, es estructural.

## Qué es un grafo (y por qué aquí lo cambia todo)

Un grafo, en su forma más simple, es una colección de puntos conectados por líneas. Los puntos se llaman nodos, las líneas se llaman aristas. Es la misma estructura que usa Google Maps para representar las calles de una ciudad, o que las redes sociales emplean para modelar las relaciones entre usuarios. No es una metáfora: es una estructura de datos con propiedades matemáticas que la hacen particularmente adecuada para representar relaciones complejas.

¿Por qué un grafo es más útil que un documento Markdown para un proyecto de software? La respuesta reside en la naturaleza de las relaciones. En un texto, incluso bien estructurado, las conexiones entre conceptos son implícitas: debéis leer, entender el contexto, inferir los vínculos. En un grafo, las relaciones son explícitas, tipificadas y atravesables. Podéis preguntar "¿cuál es el camino más corto entre el módulo de autenticación y la base de datos?" y obtener una respuesta navegando por las aristas, no analizando texto.

Para un agente de IA que debe responder sobre un proyecto, esta diferencia es sustancial. En lugar de cargar decenas de archivos en el contexto esperando que el modelo encuentre las conexiones relevantes, el agente navega por el grafo, recupera solo los nodos pertinentes y sus vecinos directos, y construye la respuesta con una fracción de los tókenes. Es la diferencia entre pedirle a alguien que lea una enciclopedia entera para responder a una pregunta, o darle un índice semántico con el que navegar directamente a la entrada correcta.

## Tres pasadas para entenderlo todo

La pipeline interna de Graphify, documentada en detalle en el archivo [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md) del repositorio, se articula en tres fases diseñadas para maximizar el procesamiento local y minimizar las llamadas a API externas.

La primera pasada se refiere al código fuente y es íntegramente local: ninguna API, ningún token consumido. Tree-sitter, el parser AST usado también por editores como Neovim y Helix para el resaltado de sintaxis en tiempo real, analiza los archivos de código y extrae clases, funciones, importaciones, grafos de llamadas y comentarios inline. El resultado es determinista: el mismo archivo produce siempre el mismo resultado. Los archivos SQL reciben un tratamiento especial, con tablas, vistas, claves foráneas y relaciones JOIN extraídas con la misma lógica determinista. En el momento del lanzamiento, Graphify declara soporte para 29 lenguajes de programación.

La segunda pasada cubre los archivos de audio y vídeo, también local. Faster-whisper, una implementación optimizada del modelo Whisper de OpenAI que se ejecuta íntegramente en local, transcribe los contenidos multimedia. Hay un detalle técnico refinado: la transcripción es "guiada" por los nodos más conectados del grafo construido en la primera pasada, los llamados "god nodes", los conceptos que aparecen con más frecuencia en las relaciones extraídas del código. Esto hace que el modelo de transcripción preste mayor atención a los términos de dominio específicos del proyecto. Los transcritos se guardan en caché: las ejecuciones sucesivas omiten los archivos ya procesados.

La tercera pasada, la que consume tókenes de API, gestiona documentos, PDF e imágenes. Aquí entra en juego el modelo de lenguaje configurado por el usuario: Claude, Gemini, OpenAI, o alternativamente una instancia local de Ollama, o bien AWS Bedrock a través de la cadena de credenciales IAM. Los archivos son procesados en paralelo por varios subagentes, cada uno de los cuales devuelve un fragmento JSON estructurado con nodos, aristas y relaciones de grupo. Los fragmentos se unen luego en un único grafo coherente.

El clustering de las comunidades se realiza con el algoritmo de Leiden, un método publicado en 2019 en *Nature Scientific Reports* que agrupa los nodos por densidad de las conexiones sin requerir embeddings vectoriales separados. Las relaciones semánticas extraídas por el modelo de lenguaje, por ejemplo `semantically_similar_to` entre dos conceptos afines, ya están en el grafo como aristas e influyen directamente en la forma de las comunidades detectadas. No hay una base de datos vectorial separada: la estructura del grafo es la señal de similitud.

Cada relación se marca con una de tres etiquetas de confianza: `EXTRACTED` para las relaciones encontradas directamente en el código fuente, `INFERRED` para las inferencias del modelo con una puntuación de 0.55 a 0.95 según una escala discreta documentada, y `AMBIGUOUS` para los casos inciertos señalados en el informe final para revisión manual. Siempre sabéis si el grafo os está diciendo algo cierto o hipotético.
![graphify-query1.jpg](graphify-query1.jpg)
*Captura de pantalla de mi prueba sobre los datos (petición de la paradoja de MTV) en opencode*

## Todo el proyecto en 7 megabytes

Instalé Graphify a través de OpenCode y lo ejecuté sobre todo el proyecto AiTalk: código, artículos, imágenes, archivos de audio, toda la base de trabajo acumulada a lo largo del tiempo. El material de origen pesaba unos 970 MB. El resultado generado, la carpeta `graphify-out/` con sus tres archivos principales, ocupaba poco más de 7 MB.

Tres archivos: `graph.html`, la visualización interactiva navegable en cualquier navegador; `GRAPH_REPORT.md`, el informe textual con los conceptos clave, las conexiones más significativas y las preguntas sugeridas; y `graph.json`, el grafo completo en formato NetworkX node-link, consultable directamente.

Desde ese momento, cualquier pregunta planteada a OpenCode sobre la estructura técnica del proyecto, sobre la lógica del código, sobre los contenidos de los artículos y sobre las conexiones temáticas entre ellos recibió respuestas excelentes. No genéricas, sino contextualizadas: el agente sabía qué componentes dependen de cuáles, qué tema se trata en varios artículos con ángulos diferentes, dónde había conexiones no explícitas entre contenidos aparentemente distantes. El modelo navegaba por el grafo en lugar de releer cada vez los archivos de origen. Donde antes una consulta compleja requería cargar decenas de archivos en el contexto, ahora el agente parte del informe y navega por el JSON para encontrar solo lo que necesita.
![grafo-aitalkjpg.jpg](grafo-aitalkjpg.jpg)
*Captura de pantalla de la página html con la representación dinámica y navegable del grafo del proyecto AiTalk.it*

## Números honestos: 71x, pero depende

El repositorio publica en el archivo [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md) un benchmark explícito, y vale la pena leerlo con atención porque los números se presentan con una honestidad inusual para un proyecto en fase promocional.

Sobre un corpus mixto de 52 archivos compuesto por los repositorios de Karpathy, cinco artículos académicos y cuatro imágenes, Graphify declara una reducción de 71,5x en los tókenes por cada consulta en comparación con la lectura directa de los archivos originales. Sobre un corpus más pequeño, cuatro archivos entre código fuente y artículos científicos, la reducción baja a 5,4x. Sobre seis archivos, aproximadamente 1x: ninguna ventaja relevante en términos de tókenes, en todo caso claridad estructural.

El patrón es claro y se explica explícitamente: la compresión escala con el tamaño del corpus. Seis archivos ya entran en una sola ventana de contexto. Con 52 archivos, los ahorros se acumulan rápidamente. Cada carpeta `worked/` en el repositorio contiene los archivos de entrada originales y el resultado real, para que cualquiera pueda replicar el benchmark de forma autónoma.

Sin embargo, debe precisarse qué no incluyen estos números: el coste de la extracción inicial, el momento en que Graphify consume tókenes de API para analizar documentos, PDF e imágenes. Este coste se amortiza en las consultas sucesivas gracias a la caché SHA256 que omite los archivos no modificados, pero es un coste real que en un corpus grande puede ser significativo, especialmente con modelos premium. El benchmark mide el ahorro en régimen estacionario, no el coste de configuración. La documentación lo dice claramente.

## Integrarse o perderse

Uno de los aspectos más cuidados del proyecto es la compatibilidad con el ecosistema de herramientas de desarrollo. En este momento, Graphify soporta la instalación directa en Claude Code, OpenCode, Codex, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider y otras herramientas menos difundidas.

El mecanismo de integración es sencillo. Una vez construido el grafo, el comando `graphify claude install` (o el correspondiente para la plataforma elegida) escribe un archivo de configuración que instruye al asistente para leer `GRAPH_REPORT.md` antes de responder. En plataformas que soportan los hooks, como Claude Code, Codex y Gemini CLI, un hook se activa automáticamente antes de cada lectura de archivo: el asistente navega por el grafo en lugar de escanear el directorio.

Para los equipos, el flujo de trabajo recomendado es hacer commit de la carpeta `graphify-out/` en el repositorio Git. Cada miembro que haga pull encontrará el grafo ya actualizado. El comando `graphify hook install` añade un hook post-commit que reconstruye automáticamente la parte AST después de cada commit, a coste cero en términos de API, con un controlador de merge de Git que gestiona los conflictos en `graph.json` uniendo los dos grafos en lugar de dejar marcadores irresolubles.

El paquete se llama `graphifyy` en PyPI (doble y), requiere Python 3.10+, y se instala con `uv tool install graphifyy`, `pipx install graphifyy` o `pip install graphifyy`. El comando CLI sigue siendo `graphify`.
![graphify-query2.jpg](graphify-query2.jpg)
*Captura de pantalla de mi prueba sobre el código (petición del método de generación del sitio) en opencode*

## Privacidad: lo que se queda en casa

La gestión de la privacidad sigue una lógica explícita. El código fuente se procesa íntegramente en local a través de tree-sitter, sin ninguna llamada a servicios externos. Los archivos de audio y vídeo se transcriben localmente con faster-whisper. Ni un solo byte de código o contenido multimedia sale de la máquina del usuario.

La situación cambia para documentos, PDF e imágenes: estos se envían al modelo de lenguaje configurado a través de su API. Si se usa Claude, los archivos se envían a Anthropic. Si se usa Ollama, se quedan en local. Para contextos con datos sensibles, Graphify ofrece dos opciones: una instancia de Ollama local o AWS Bedrock a través de IAM, sin claves de API explícitas. El proyecto afirma no tener telemetría, seguimiento de usos ni análisis de datos.

Un aspecto a considerar para los equipos sobre código propietario: aunque el código permanezca en local, los documentos de arquitectura, los PDF de las especificaciones y las imágenes de los mockups son procesados por el modelo externo configurado. Ante la presencia de obligaciones de confidencialidad contractual, esta distinción debe valorarse con atención antes de la adopción.

## Límites sin descuentos

Sería deshonesto quedarse solo en el elogio. Hay aspectos que merecen una valoración crítica.

El primero se refiere a la calidad de las relaciones inferidas. Las relaciones etiquetadas como `INFERRED` dependen de la calidad del modelo usado. Un modelo más pequeño o configurado con un presupuesto de tókenes reducido puede producir relaciones especulativas con puntuaciones de confianza optimistas. La escala de 0.55 a 0.95 está calibrada sobre los corpus de prueba del desarrollador, no necesariamente sobre el tipo de proyecto sobre el que se aplica la herramienta.

El segundo límite se refiere a las actualizaciones. La caché SHA256 omite los archivos no modificados, pero ¿qué pasa cuando se mueve una función de un módulo a otro o se refactoriza una clase de forma significativa? El grafo puede tener nodos huérfanos o relaciones que apuntan a entidades que ya no existen. El comando `--update` gestiona los archivos modificados, pero ante refactorizaciones profundas probablemente sea necesaria una reconstrucción completa, con el coste de tókenes asociado.

El tercer aspecto crítico es la escala. Al igual que con el enfoque wiki de Karpathy, el grafo también tiene un punto de ruptura. Para corpus muy grandes, la documentación sugiere usar consultas directas sobre el `graph.json` o exponer el grafo como un servidor MCP con `python -m graphify.serve`, que ofrece herramientas estructuradas como `query_graph`, `get_node`, `get_neighbors` y `shortest_path`. La solución es refinada, pero añade una capa de configuración que no todos los flujos de trabajo pueden absorber fácilmente.

Cabe señalar, por último, que el proyecto es mantenido sustancialmente por un único desarrollador, Safi Shamsi. El repositorio muestra una actividad intensa, con 97 lanzamientos en el momento de escribir estas líneas y la última versión estable v0.7.16 lanzada el 12 de mayo de 2026, pero la sostenibilidad a largo plazo de un proyecto con esta visibilidad y esta dependencia de un único mantenedor es una variable que no debe ignorarse para quienes planifiquen una adopción en entornos críticos.

## El futuro de la memoria

Graphify resuelve un problema concreto. Pero la pregunta más interesante que plantea no se refiere al ahorro de tókenes: se refiere a la naturaleza de la memoria en los agentes de IA.

Hoy en día, un agente no tiene memoria persistente. Cada sesión es una pizarra limpia, cada proyecto redescubierto desde cero. Graphify y proyectos similares son intentos de construir una capa externa de memoria estructurada que sobreviva a las sesiones, que se acumule con el tiempo, que represente no solo los datos brutos sino las relaciones entre ellos.

Las preguntas abiertas siguen siendo muchas. ¿Cómo se mantiene la coherencia de un grafo en un proyecto que evoluciona rápidamente? ¿Quién es responsable de la calidad de las relaciones inferidas cuando un agente toma decisiones basándose en ellas? Y la más sutil: si el agente navega por un grafo en lugar de razonar sobre los archivos, la calidad de la extracción inicial se convierte en el verdadero cuello de botella, no controlable con un parámetro de temperatura sino con la calidad de la pipeline de ingesta.

Del sitio de Graphify Labs emerge una visión más ambiciosa: Penpax, el producto comercial anunciado en versión trial próximamente, promete aplicar la misma lógica a todo el trabajo diario de una persona, reuniones, correos electrónicos, archivos y código, actualizándose en segundo plano, sin nube, completamente on-device. Un "segundo cerebro" digital construido sobre bases técnicas serias en lugar de metáforas motivacionales.

Graphify en su forma de código abierto ya es un punto de partida significativo. No es la solución definitiva al problema de la memoria de los LLM, pero es un indicador preciso de la dirección en la que se está buscando: no dentro del modelo, no en el contexto, sino en una representación estructurada y persistente que vive fuera de ambos.

---

*Graphify está disponible en [GitHub](https://github.com/safishamsi/graphify) con licencia MIT. El paquete PyPI se llama [graphifyy](https://pypi.org/project/graphifyy/) (doble y). El sitio del proyecto es [graphifylabs.ai](https://graphifylabs.ai). La documentación técnica sobre la pipeline de extracción está en [how-it-works.md](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md).*
