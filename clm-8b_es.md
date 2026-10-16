---
tags: ["Generative AI", "Applications", "Research"]
date: 2026-10-26
author: "Dario Ferrero"
---

# CLM-8B, el tomador de decisiones abierto que desafía a Jev
![clm-8b.jpg](clm-8b.jpg)

*En el [artículo sobre Jev](https://aitalk.it/it/jev) hablé de un modelo que renuncia a las palabras para hacer una sola cosa: decidir. Se le entrega una situación y un conjunto de opciones posibles, y devuelve una elección con su probabilidad asociada, sin escribir una sola línea de texto. TypeSafe, que lo lanzó el 15 de septiembre, denominó a esta categoría System One, en homenaje al pensamiento rápido de Kahneman. Ocho días después llegó una propuesta desde el campo opuesto: [CLM-8B](https://github.com/Contrastive-LM/CLM), publicado por investigadores de Stanford y NVIDIA bajo licencia Apache 2.0, por lo que es descargable e instalable en servidores propios.*

Sería cómodo tildarlo del "Jev libre", pero es un atajo equivocado. La idea de la respuesta a Jev es una lectura periodística, no una declaración de sus autores. CLM aborda el mismo problema —decidir deprisa sin escribir palabra tras palabra—, pero con una arquitectura diferente y una vocación distinta. De las pruebas disponibles emerge un especialista, no un sustituto.

## Dos codificadores, una caché

Para entender la diferencia hace falta una imagen. En 1975 Brian Eno y Peter Schmidt publicaron las Oblique Strategies, una baraja de cartas con aforismos para robar cuando un trabajo se bloquea. La baraja es siempre la misma, lo que cambia es la situación en la que se consulta. CLM funciona de manera similar: las acciones posibles forman una baraja fija, y cada nueva situación se compara con las cartas para descubrir cuál encaja mejor.

Técnicamente, el modelo utiliza dos lectores independientes, uno para la situación y otro para las acciones, que traducen ambas a coordenadas de un espacio compartido; gana la acción más cercana a la situación. Es el esquema de los motores de búsqueda semántica, entrenado con un método llamado InfoNCE que premia las combinaciones correctas y penaliza las demás. La ventaja práctica es que las coordenadas de las acciones se calculan una sola vez y se guardan en memoria (la caché), mientras que para cada solicitud se lee únicamente la situación.

Jacky Kwok, responsable del proyecto, explicó a [VentureBeat](https://venturebeat.com/technology/stanford-and-nvidias-open-clm-8b-caches-reusable-agent-actions-and-runs-up-to-9x-faster-than-jev-in-tests) que Jev y un modelo afín, Laya, almacenan en caché únicamente la situación, y que la separación de CLM hace que la ventaja sea más acusada cuando los contextos y las acciones son largos o se reutilizan. Es la descripción del autor del proyecto, no verificada por terceros: la arquitectura interna de Jev no es pública, TypeSafe no ha difundido ni pesos ni dimensiones, y las reconstrucciones externas, como la del analista [Archer Hume](https://archerhume.com/posts/jevs-architecture-unmasked/), siguen siendo expresamente conjeturas.

La caché no es magia, como admite el propio [README](https://github.com/Contrastive-LM/CLM). En las mediciones de los autores sobre una GPU RTX 4090, una situación siempre nueva tarda unos 28 milisegundos con o sin caché, porque hay que leerla de todos modos; cuando las situaciones se repiten, el tiempo se reduce de aproximadamente 1,7 a 0,6 milisegundos. La ganancia depende de cuánto vuelva a visitar el agente los mismos escenarios (declaración de parte, no replicada por terceros).

## ¿Pesos abiertos, de verdad?

Aquí reside la primera ventaja concreta respecto a Jev, que sigue siendo un servicio cerrado accesible vía API. [Los pesos y el código están bajo Apache 2.0](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B), sin contratos que firmar y con la posibilidad de ejecutar todo en casa. Para quienes se ocupan de la inteligencia artificial local y la soberanía de los datos es el punto decisivo. Pero "abierto" abarca tres niveles diferentes.

El primer nivel son los pesos, y aquí CLM cumple, con una advertencia. La parte entrenada por los autores es un archivo de 75 megabytes: el grueso del trabajo lo realiza Qwen3-8B de Alibaba, un modelo preexistente mantenido congelado, al que CLM añade dos pequeñas cabezas, una para las situaciones y otra para las acciones. Según la [ficha de baobab-tech](https://github.com/baobab-tech/decision-models-experiments/blob/main/docs/models/clm-8b.md), se necesita un servidor vLLM para el codificador, unos 16 GB de memoria y, como requisito indicado por los autores, una GPU NVIDIA. En Mac funciona una solución alternativa de terceros, mientras que Ollama no está soportado. La ejecución local es factible, pero no trivial.

El segundo nivel es la evaluación. El repositorio incluye scripts para reproducir las pruebas en código y en el juego T-Rex, por lo que es posible una verificación parcial, aunque la misma ficha señala que un conjunto de datos citado en el README no aparece en la lista de la organización. El tercer nivel es el ecosistema, aún inmaduro: la guía para el entrenamiento adicional es, según baobab, un texto pensado para un agente autónomo más que para un lector humano; los datos y los flujos de trabajo están en otro repositorio; y las licencias de los datos de entrenamiento no están listadas, incluidos los 30 millones de respuestas erróneas pero plausibles generadas con Gemini 2.5 Flash-Lite, cuyos términos de uso la ficha señala como no verificados para este propósito.
![immagine1.jpg](immagine1.jpg)
[Imagen extraída del repositorio oficial en GitHub](https://github.com/Contrastive-LM/CLM)

## Lo que declaran los autores

Todas las cifras de esta sección son declaraciones de parte, obtenidas de quienes construyeron el modelo. En las pruebas sin entrenamiento específico para la tarea, el README sostiene que CLM está a la par de Jev en uso del ordenador, juegos y llamada a herramientas, con una latencia hasta 9 veces menor. El mejor caso es el juego del dinosaurio de Chrome: 16,5 milisegundos frente a 149,8, con ambos modelos logrando 5 de 5 aciertos, al igual que en Super Mario. En el benchmark BFCL v4, dedicado a la llamada a herramientas, CLM obtiene un 95,2% frente al 99,2% de Jev, con tiempos de 76,8 frente a 125,5 milisegundos. En WikiRacing, que consiste en alcanzar una página de Wikipedia siguiendo enlaces, CLM completa 26 de 30 pruebas y Jev las 30, con 79,8 milisegundos frente a 225.

Dos aclaraciones necesarias. La paridad no es uniforme: allí donde cambia la precisión, Jev se mantiene por delante, y la ventaja de velocidad varía de aproximadamente 1,6 a 9 veces según la tarea. Además, CLM se mide en una GPU local mientras que Jev es un servicio alojado en la nube; de las fuentes consultadas no queda claro si la latencia de Jev incluye el trayecto de red, un detalle que altera sustancialmente la comparación.

La parte más llamativa se refiere al código. Tras un entrenamiento adicional ligero, los autores declaran un 81,6% en DeepSWE y un 87,6% en Terminal-Bench 2.1, frente al 71,1% y 83,1% de Jev. Pero esos resultados provienen de cabezas entrenadas expresamente, no del modelo publicado, sobre solo 38 y 30 tareas reservadas. Y CLM no resuelve los problemas por sí solo: elige entre soluciones producidas por modelos más grandes, Opus 5 para la primera prueba y Fable 5 para la segunda. Sigue siendo un resultado interesante, por ser el único terreno donde, según los autores, CLM supera a Jev. Nadie ha reproducido aún estos datos de forma independiente.

## Pruebas sobre el terreno

Aquí intervienen terceros, con tres familias de verificaciones que emplean métodos y límites muy diversos.

La primera es [local-jev-bench](https://github.com/tak-bro/local-jev-bench), una prueba en un Mac M3 Max con 36 GB resumida en la ficha de baobab-tech. CLM obtiene un 39% sobre 105 decisiones en inglés, un 41% en coreano y un 20% en BANKING77, una lista clásica de 20 categorías de consultas bancarias donde el azar daría alrededor del 5%. Otros dos modelos abiertos en la misma prueba alcanzan el 89%, 87% y 89% (Kev-4B) y el 81%, 84% y 80% (AnyJev L0). Atención: no se trata de una comparación con Jev, sino con otros modelos abiertos. Los mismos evaluadores no consiguen además reproducir el ejemplo oficial del README para la pregunta sobre urgencia (0,852 frente a 0,41). Límites: hardware no previsto por los autores y procedimiento de terceros.

La segunda es una [evaluación de michabbb](https://gist.github.com/michabbb/da531cc4720d8ec62395fc02dfdd476c) sobre 140 parejas reales de enlace entre elementos de una base de conocimiento, planteando la pregunta directa de si dos elementos están conectados. Sobre 40 parejas con respuesta de referencia, la capacidad de distinción (AUC, donde 1 es perfecto y 0,5 es el azar) es de 0,77 para CLM con textos truncados a 2.048 tokens, 0,64 con el texto completo y 0,998 para Jev. CLM coincide con Jev en los tramos de decisión en aproximadamente el 44% de los casos y nunca baja de 0,22 de probabilidad. El tiempo también es inferior, 0,52 segundos frente a 0,28, pero aquí la comparación está descompensada: CLM en un DGX Spark con las cabezas en el procesador y Jev vía API. Sobre todo, el autor detalla por sí mismo los límites: tarea muy distinta de las previstas para el modelo, 129 entradas de 140 por encima de la ventana de contexto, etiquetas de referencia asignadas por un modelo de lenguaje y no por personas, sin entrenamiento adicional y versión v0.1.

La tercera corresponde a los agregadores. [BenchLM](https://benchlm.ai/compare/clm-8b-vs-jev-1-13-0) registra en JevBench un 8,57 frente a 63,29 en la versión 1.4 y un 1,51 frente a 72,13 en la 1.5, declinando elaborar una clasificación por falta de datos comparables. [Benchmark Heaven](https://benchmarkheaven.com/jev-models/clm-8b) sitúa a CLM en el puesto 87 de 92 entre los modelos abiertos, aunque se trata de un proyecto personal en versión beta. Además, JevBench es un banco de pruebas concebido en torno a modelos de tipo Jev. Son señales a verificar, no veredictos definitivos.
![immagine2.jpg](immagine2.jpg)
[Imagen extraída del repositorio oficial en GitHub](https://github.com/Contrastive-LM/CLM)

## Por qué divergen las cifras

Sería un error concluir que alguien miente. En *Rashomon* de Kurosawa el mismo suceso produce cuatro relatos irreconciliables sin que ninguno de los testigos actúe de mala fe: observan desde posiciones distintas. Aquí ocurre lo mismo con los benchmarks.

Las pruebas oficiales priorizan la elección entre pocas acciones repetidas, la llamada a herramientas, los juegos y la selección entre respuestas candidatas. Las pruebas independientes emplean clasificaciones con muchas categorías, casos reales de soporte técnico y juicios sobre textos largos y estructurados. Cambian la longitud de la entrada (que CLM trunca en silencio más allá de los 2.048 tokens por defecto), el número de candidatos y la frecuencia con la que se repiten las mismas acciones, de lo que depende toda la caché. Cambia también el régimen: modelo publicado frente a cabezas entrenadas expresamente.

Lo reconoció con franqueza el propio Kwok: no lo utilizaría en lugar de un modelo de razonamiento general para problemas de matemáticas, textos largos o planificación. VentureBeat recuerda además una limitación estructural: las probabilidades de CLM son relativas al conjunto de candidatos recibido, y si todos son incorrectos, el modelo elegirá de todos modos uno de ellos. La conclusión que extraigo es la siguiente: CLM puede ser excelente en el dominio para el que nació y débil fuera de él. Qué tan amplio sea ese dominio es algo que hoy nadie sabe con precisión.

## Pros y contras en producción
![tabella1.jpg](tabella1.jpg)

Por equilibrio, conviene recordar que también Jev se apoya en buena medida en cifras declaradas por TypeSafe: la propia empresa califica de internas sus mediciones de velocidad y coste, y por lo que consta no ha publicado curvas de calibración, como señalaba en el [artículo anterior](https://aitalk.it/it/jev). En cuanto al coste no existe una comparación homogénea, como admite VentureBeat.

Jev es hoy la opción más predecible por precisión; CLM es la más interesante por control, coste marginal y latencia, pero requiere una validación sobre la propia carga de trabajo. ¿Quién sale ganando? Quien gestiona datos sensibles y acciones repetitivas. ¿Quién asume riesgos? Quien lo adopte fiándose únicamente del titular.

## Qué falta para un veredicto

Expongo las limitaciones, porque hacen más creíble el análisis. No he podido realizar una prueba local en hardware AMD, que la infraestructura oficial no señala como objetivo. Las pruebas independientes son escasas y sobre tareas heterogéneas. Faltan comparativas reproducibles sobre la misma tarea, con los mismos prompts y la misma versión de Jev, que mientras tanto ha alcanzado la 1.13.0. El comportamiento tras un entrenamiento adicional podría cambiar de forma notable, pero no está documentado por terceros. Hacen falta mediciones sobre la latencia en el peor de los casos, costes reales, huella de memoria y pérdida de calidad fuera del terreno de proyecto. Por último, el hermano mayor, CLM-35B multimodal, estaba anunciado por los autores para principios de octubre: a fecha de 11 de octubre no aparece en Hugging Face.

## Alternativa selectiva, no sustituto

CLM-8B es importante porque aporta al dominio público una alternativa abierta a los modelos System One cerrados, y porque lo hace con una idea arquitectónica diferente y verificable. La latencia y la licencia abierta son ventajas reales, especialmente para agentes de alta frecuencia e instalaciones controladas. Sin embargo, en las pruebas independientes disponibles hoy, Jev sigue siendo netamente más fiable en clasificación, juicios binarios de sí o no y textos complejos.

La pregunta adecuada, por tanto, no es "¿CLM o Jev?", sino si vuestra carga de trabajo incluye acciones reutilizables, conjuntos de candidatos breves y la necesidad de alojar el modelo en casa. Si la respuesta es afirmativa, CLM merece un piloto evaluado con vuestros propios datos. Si la prioridad es la precisión general sin entrenamiento específico, Jev sigue siendo la opción más prudente. Como con cualquier baraja de cartas, importa menos la carta en sí que la mano que estáis jugando: conviene medir antes de elegir.
