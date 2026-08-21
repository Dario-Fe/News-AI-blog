---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-08-31
author: "Dario Ferrero"
---

# Muse Glimmer 30B en local: el nuevo modelo de Meta
![muse-glimmer30b.jpg](muse-glimmer30b.jpg)

*El 10 de agosto de 2026, Meta Superintelligence Labs lanzó [Muse Glimmer](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model), un modelo de 30 mil millones de parámetros pensado para ejecutarse en local en hardware de consumo, y la noticia merece una aclaración inmediata para quienes seguís a Meta desde hace tiempo: no es un Llama. Es el primer lanzamiento de la nueva división de investigación fundada tras la reestructuración de los esfuerzos de inteligencia artificial de la empresa, un proyecto que nace con una identidad y una filosofía diferentes respecto a la vieja familia.*

La particularidad más importante que debéis entender, antes incluso de abrir LM Studio, atañe a su naturaleza. Muse Glimmer no ha sido entrenado desde cero como [Qwen3.8, probado en mi artículo anterior](https://aitalk.it/it/qwen38-27b.html). Es una versión destilada de Muse Spark 1.2, el modelo insignia de Meta: un "profesor" mucho más grande entrenó a este "alumno" para replicar sus comportamientos, según un proceso que en la jerga técnica se denomina destilación de logits. El resultado es un modelo más pequeño y eficiente, que hereda gran parte de las capacidades del maestro sin arrastrar su volumen. Es un poco como en los relatos de aprendizaje de Miyazaki, donde el discípulo no replica al maestro por imitación superficial, sino que absorbe su método hasta hacerlo propio.

Elegí probarlo en la misma franja dimensional que la prueba anterior, un denso de 30 mil millones contra el denso de 27 mil millones de Qwen, precisamente porque Meta lo declara pensado para agentes locales, tool calling y orquestación de tareas complejas. La pregunta que me planteé es sencilla: ¿puede un modelo "de la casa Meta", nacido explícitamente para actuar como agente, competir en mi hardware con los modelos chinos que hasta ahora han dominado esta franja?

Para la versión opté por la cuantización Q4_K_XL, unos 19 GB en disco. Las fuentes indican que Muse Glimmer está pensado para hardware con 24-32 GB de VRAM, pero con offload parcial conseguí hacer que funcionara en mi configuración, sacrificando algo de velocidad. Ajusté un contexto de 91.000 tokens, un compromiso entre la ventana nativa de 131k declarada por el fabricante y los márgenes de memoria disponibles.

## El laboratorio, sin cambios

Quienes habéis seguido la serie ya conocéis la configuración: procesador AMD Ryzen 7700, 32 GB de RAM DDR5, GPU AMD Radeon RX 9060 XT con 16 GB de VRAM, todo orquestado mediante [LM Studio](https://aitalk.it/it/qwen3.5-locale-puntata1.html), tal como se describe en detalle en la primera entrega de esta serie junto con la comparación con Ollama y los motivos de la elección. No me extiendo más sobre esto; quienes queráis profundizar encontraréis todo en aquel artículo.

Para Muse Glimmer ajusté algunos parámetros específicos. El offload de GPU se fijó en 35 capas de 52, por lo que más de la mitad del modelo reside en la VRAM, con el pool de hilos (threads) de la CPU al máximo permitido, ocho de ocho. El lote (batch) de evaluación se dejó en 2048, el batch físico en 512, y la predicción concurrente máxima en 4.

Hay que hacer una precisión de inmediato, porque condicionó toda la sesión de pruebas: Muse Glimmer tiende a pensar detenidamente antes de responder. En un caso observé un tiempo de razonamiento de diez minutos, en otro de tres, iterando el modelo a menudo varias veces sobre la misma solución incluso cuando la respuesta correcta ya había surgido en los primeros compases del razonamiento. Es un comportamiento que, como veremos, pesa bastante en la usabilidad diaria.

## Un cerebro destilado, no nacido

Antes de pasar a las pruebas, vale la pena entender qué hay bajo el capó. Muse Glimmer es un modelo denso, no un Mixture of Experts como [Ornith 1.0](https://aitalk.it/it/ornith-1.0.html) o [Gemma 4 26B](https://aitalk.it/it/gemma4-26b.html), que probé en entregas anteriores de esta serie. La diferencia arquitectónica no es un detalle para expertos: en un modelo denso cada token activa la red completa, los treinta mil millones de parámetros, mientras que en un MoE solo se consulta a una fracción de los "expertos" internos cada vez. La apuesta de los modelos densos es que este mayor coste computacional se traduzca en una capacidad de razonamiento superior.

En el frente multimodal, Muse Glimmer integra de forma nativa un codificador visual de 1,8 mil millones de parámetros, capaz de leer imágenes y vídeos sin necesidad de módulos externos. La licencia es Apache 2.0, la misma elección permisiva ya vista en otros modelos de esta serie, un detalle nada secundario para quienes desarrolláis productos comerciales y no queréis complicaciones legales.

Desde el punto de vista arquitectónico, [las especificaciones publicadas](https://www.together.ai/models/muse-glimmer) describen una atención agrupada (grouped-query attention) con una proporción de 32 cabezales de consulta (query) frente a 2 cabezales de clave-valor (key-value), una elección que reduce drásticamente la memoria requerida para la caché durante la inferencia. A esto se suma el soporte de DFlash, una técnica de decodificación especulativa que predice bloques enteros de dieciséis tokens en una sola pasada, verificándolos luego en paralelo en lugar de generarlos de uno en uno. Sobre el papel, esto debería garantizar una aceleración de hasta 3 veces respecto a la generación token por token. En la práctica, en mi hardware, la velocidad observada fue muy similar a la de Qwen3.8, en torno a los 5 tokens por segundo: la teoría de la aceleración en hardware de gama alta no siempre se traslada linealmente a una configuración de gama media como la mía.

Conviene recordar, como siempre en esta serie, que las siguientes pruebas no tienen pretensión alguna de rigor de laboratorio. No son benchmarks, no utilizo baterías estandarizadas ni muestras estadísticamente significativas: son ocho pruebas prácticas, las mismas utilizadas para Qwen3.8, Ornith y [Laguna XS-2.1](https://aitalk.it/it/qwen36-35b-ai.html), pensadas para entender cómo se comporta el modelo en el uso diario de quien escribe, no para elaborar clasificaciones académicas.

## Las ocho pruebas

### Razonamiento científico: el mecanismo de Higgs

Pedí al modelo que explicara la ruptura de la simetría electrodébil en el Modelo Estándar, prestando atención al campo de Higgs y a los bosones W, Z y al fotón—el mismo prompt utilizado para los demás modelos de la serie. Velocidad de generación: 5,34 tokens por segundo. La respuesta llegó técnicamente impecable: fórmulas correctas, estructura lógica sólida, con la alusión al "sombrero mexicano" del potencial de Higgs y la derivación correcta de las masas de W y Z.

Lo que le falta, en comparación con Qwen3.8, es el cuidado didáctico. La respuesta es directa y sintética, carente de esa progresión narrativa que acompaña al lector paso a paso, sin metáforas elaboradas ni explicaciones verbales que ayuden a quien no tiene ya las bases. Para un estudiante universitario—el destinatario explícito del prompt—, el resultado es menos accesible de lo que debería ser. Sancioné ligeramente la nota por esto: es un modelo que parece hablar a un colega experto, no a alguien que todavía está aprendiendo.

**Nota: 4,8/5.**

### Multimodalidad: la tabla de Excel borrosa

Cargué una imagen de baja calidad de una hoja de cálculo Excel, pidiendo una descripción del contenido, los datos principales y las tendencias. Velocidad: 5,22 tokens por segundo. El modelo leyó correctamente la estructura de la hoja, los valores numéricos y las relaciones entre columnas, extrayendo patrones estacionales y diferencias entre 2017 y 2018, e incluso llegó a observar una correlación entre el número de pedidos y el valor medio.

La solidez visual es excelente y la respuesta se adapta bien a la tarea descriptiva. No alcanza la profundidad de análisis que mostró Qwen3.8 al proponer acciones correctivas concretas, pero sigue siendo completa y bien organizada.

**Nota: 5/5.**

### Generación de código: el ciclo máximo en un grafo

La tercera prueba pedía implementar en Python un algoritmo para encontrar el ciclo de longitud máxima en un grafo no dirigido, explicando su complejidad. Aquí llegó la primera señal de alarma: diez minutos de reflexión antes de responder. Velocidad de generación una vez iniciada: 5,17 tokens por segundo.

La solución producida se basa en programación dinámica sobre subconjuntos, el enfoque de Held-Karp, reconociendo correctamente la naturaleza NP-hard del problema. El código es limpio, está comentado, funciona, y la complejidad declarada, O(n² 2ⁿ), es exacta. De las trazas de razonamiento visibles emerge un detalle curioso: el modelo había identificado la solución correcta casi de inmediato, pero continuó iterando sobre la misma lógica durante minutos, como un músico de jazz que pule el mismo solo antes de tocarlo realmente. La calidad final es excelente, pero diez minutos de espera para una tarea interactiva son demasiados.

**Nota: 4,9/5**, penalizada por el tiempo de procesamiento excesivo.

### Planificación multilingüe: cinco días en Japón

Pedí un itinerario de cinco días en Japón para un cliente francés, con el texto principal en francés y una sección dedicada en italiano. Velocidad: 5,34 tokens por segundo. El modelo respetó perfectamente el idioma solicitado, produciendo un itinerario detallado con consejos prácticos sobre transporte, barreras lingüísticas y comida callejera, mientras que la sección en italiano estaba igualmente cuidada.

A diferencia de Laguna XS-2.1, que en la entrega anterior había mostrado alguna incertidumbre lingüística, aquí no hubo problemas. La respuesta es completa y rica en detalles culturales, aunque más sintética que la que Qwen3.8 había producido sobre el mismo prompt.

**Nota: 5/5.**

### Contexto largo: buscar la aguja en el PDF de 460 páginas

Cargué el AI Index Report 2025 completo, de más de 460 páginas, pidiendo información sobre el crecimiento de la generación de vídeo y las páginas exactas donde encontrarla. Tiempo de razonamiento: unos tres minutos. Velocidad: 5,18 tokens por segundo. El modelo señaló correctamente las páginas 126 y 127, citando las figuras específicas 2.3.11 y 2.3.12, y el resumen incluía detalles precisos sobre los modelos citados en el informe y el ya famoso ejemplo del vídeo de Will Smith comiendo espaguetis.

La precisión en la recuperación de información es excelente, pero tres minutos siguen siendo un tiempo significativo para una tarea que, en teoría, solo requiere buscar información ya presente en el texto en lugar de razonar sobre ella largamente.

**Nota: 4,9/5**, de nuevo penalizada por el tiempo de espera.

### Razonamiento espacial: la habitación desordenada

Cargué la imagen de una habitación desordenada, pidiendo una descripción y una estrategia de ordenación. Tiempo de respuesta: 50 segundos, esta vez razonable. Velocidad: 5,33 tokens por segundo. El modelo describió la habitación por áreas funcionales, con una estrategia de ordenación lógica y motivada sobre una base práctica, identificando por ejemplo en el cesto azul el principal obstáculo a mover en primer lugar.

La comprensión visuoespacial es sólida y el tiempo de respuesta, finalmente, compatible con un uso diario.

**Nota: 5/5.**
![immagine1.jpg](immagine1.jpg)
*Captura de pantalla durante las pruebas de razonamiento espacial*

### Agente de múltiples pasos: planificar una aplicación web

Pedí planificar el desarrollo de una aplicación web de gestión de gastos, con stack tecnológico, estructura del proyecto y hoja de ruta para un equipo de dos desarrolladores. Velocidad: 5,31 tokens por segundo. La respuesta llegó completa, con un stack moderno basado en Next.js, NestJS, PostgreSQL y Prisma, una estructura monorepo, una hoja de ruta dividida en seis sprints y los principales cuellos de botella identificados de antemano.

El toque que más aprecié es el consejo final, pragmático y concreto: concentrar los primeros cuatro sprints en el núcleo mínimo funcional antes de añadir cualquier retoque. Es el tipo de sugerencia que cabría esperar de un gestor de proyectos experimentado, no de un modelo lingüístico.

**Nota: 5/5.**

### Conversación larga: cuatro turnos sobre una app de gestión de tareas

La última prueba midió la retención de la memoria conversacional a lo largo de cuatro turnos consecutivos debatiendo sobre el stack tecnológico, sistema de notificaciones, esquema de la base de datos y estrategias de escalabilidad para una app de gestión de tareas. Velocidad media: 5,1 tokens por segundo, con un descenso progresivo de 5,33 a 4,98 turno tras turno.

El modelo mantuvo la coherencia durante toda la conversación, recordando cada elección técnica anterior y justificándola cuando se le pedía. Propuso una arquitectura híbrida para las notificaciones—WebSockets para las internas de la app y correos asíncronos gestionados con BullMQ—, un esquema de base de datos completo y una hoja de ruta de escalabilidad diseñada para diez mil usuarios. La ligera ralentización en los turnos posteriores es fisiológica; la calidad se mantuvo constante.

**Nota: 5/5.**

## Tabla de resumen de las pruebas
![tabella1.jpg](tabella1.jpg)
Nota media: 4,95/5. Velocidad media: aprox. 5,2 tokens por segundo.

## El precio de pensar demasiado

Muse Glimmer 30B es, ante todo, la demostración de lo que significa ser un modelo denso y destilado al mismo tiempo. Activa los treinta mil millones de parámetros para cada token generado, y esto se paga en velocidad: unos 5 tokens por segundo en mi configuración, un ritmo que requiere paciencia. A cambio, la destilación desde Muse Spark 1.2 le permite heredar comportamientos y capacidades de un modelo mucho mayor, una herencia que se percibe en la calidad de las respuestas más que en su rapidez.

La calidad, en efecto, es alta: 4,95 sobre 5 de media en las ocho pruebas, exactamente el mismo resultado obtenido por Qwen3.8-27B en la entrega anterior. En el plano de los contenidos, en definitiva, los dos modelos se equivalen. Lo que los distingue realmente es el comportamiento durante la espera y el estilo de la respuesta final.

El rasgo más distintivo de Muse Glimmer es su tendencia al "long thinking", el pensar detenidamente antes de responder. Diez minutos en la prueba de código, tres minutos en la prueba del PDF largo, iterando a menudo el modelo sobre la misma solución incluso tras haberla encontrado ya, un poco como ciertos personajes de las novelas gráficas de Craig Thompson que rumiaban el mismo recuerdo una y otra vez antes de dejarlo ir. Es un comportamiento que puede ser una virtud para problemas que requieren realmente un razonamiento profundo, o un defecto para quienes buscan una interacción rápida y fluida en la conversación diaria.

El estilo de las respuestas revela además una personalidad precisa: directo, sintético, técnicamente riguroso, pero menos inclinado a la pedagogía en comparación con Qwen3.8. Es un modelo que parece pensado para hablar con quien ya sabe, más que para acompañar a quien está aprendiendo. La multimodalidad nativa lo hace en cualquier caso más versátil que modelos como Laguna XS-2.1, que no gestiona imágenes, y la licencia Apache 2.0 sigue siendo una ventaja concreta para quienes queréis integrarlo en un producto comercial sin restricciones.

¿Quién gana y quién pierde en este escenario? Gana quien tiene paciencia y busca rigor técnico en tareas complejas: desarrolladores que construyen agentes locales, quienes trabajáis en problemas donde un tiempo de espera mayor es aceptable a cambio de precisión. Pierde quien busca un asistente reactivo para el uso diario, donde un MoE como Ornith-1.0-35B, probado en una entrega anterior de esta serie, ofrece probablemente un compromiso más equilibrado entre velocidad y calidad.

Queda una pregunta abierta que vale la pena dejar sobre la mesa: ¿el "long thinking" observado aquí es una característica intrínseca de la arquitectura destilada, o un efecto secundario del proceso de entrenamiento que Meta podría corregir en próximas versiones? No tengo una respuesta definitiva, y sospecho que ni siquiera Meta la tiene aún del todo clara. Por ahora, Muse Glimmer sigue siendo un modelo que piensa mucho y habla poco, lo cual, según lo que necesitéis, puede ser su mayor fortaleza o su límite más evidente.
![tabella2.jpg](tabella2.jpg)
