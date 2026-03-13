---
tags: ["Generative AI", "Research", "Startups"]
date: 2026-03-13
author: "Dario Ferrero"
---

# Mil tokens por segundo: Mercury 2 quiere reescribir las reglas de la IA
![mercury2.jpg](mercury2.jpg)

*Hay un momento extraño, casi alienante, que cualquiera que haya usado Mercury 2, de Inception Labs, por primera vez describe de manera similar: escriben la pregunta, pulsan Intro y la respuesta ya está ahí, íntegramente, incluso antes de que su cerebro haya terminado de registrar que han hecho clic en algo. No es un efecto visual, no es un truco de interfaz. El modelo realmente genera más de 1000 tokens por segundo.*

Para dar un orden de magnitud: una novela media italiana tiene unos 300.000 caracteres, es decir, aproximadamente entre 90.000 y 100.000 tokens. Mercury 2, en teoría, la escribiría en menos de dos minutos. Claude 4.5 Haiku, uno de los modelos "rápidos" más extendidos hoy en día, se queda en unos 89 tokens por segundo. GPT-5 Mini en unos 71. La diferencia no es incremental: es estructural.

Todo esto es posible porque Mercury 2 no funciona como cualquier otro modelo de lenguaje que hayan usado antes. Y entender por qué requiere dar un paso atrás sobre la forma en que la inteligencia artificial generativa produce texto, y cómo, desde siempre, lo ha hecho de una única manera.

## Dos familias, un paradigma dominante

Si quieren entender Mercury 2, primero deben entender el cuello de botella que busca eliminar. Y ese cuello de botella tiene un nombre técnico preciso: generación autorregresiva.

Todos los grandes modelos de lenguaje que usan cada día, ChatGPT, Claude, Gemini, funcionan bajo el mismo principio básico: producen texto un token a la vez, de izquierda a derecha, y cada token depende de todos los que le preceden. Es como escribir a máquina: no pueden pulsar la tercera letra antes de haber pulsado la segunda. Esta dependencia secuencial es arquitectónica, no una ineficiencia eliminable con más hardware u optimizaciones de software. Es la naturaleza misma del mecanismo.

La difusión (diffusion) es algo diferente. La técnica nació en el mundo de la generación de imágenes, es la base de Stable Diffusion, Midjourney, DALL-E, y funciona de manera opuesta: en lugar de construir el resultado pieza por pieza, parte de un resultado completamente "ruidoso" e impreciso, y lo refina progresivamente en paralelo, en varios puntos simultáneamente, convergiendo hacia la respuesta correcta en pocos pasos. Ya no es como una máquina de escribir, sino más bien como un fotógrafo que revela una polaroid: la imagen completa emerge gradualmente, toda a la vez.

Sin embargo, aplicar esta técnica al texto, a diferencia de las imágenes, es un problema mucho más difícil. El lenguaje tiene restricciones lógicas, gramaticales y semánticas que las imágenes no tienen en la misma medida. Durante años se consideró que la difusión no era adecuada para el texto. Si quieren profundizar en la comparación técnica entre ambos enfoques, encontrarán [un artículo dedicado precisamente a este tema](https://aitalk.it/it/diffusion-vs-autoregressive.html) en el portal.
![grafico1.jpg](grafico1.jpg)
[Imagen tomada de inceptionlabs.ai](https://www.inceptionlabs.ai/blog/introducing-mercury-2)

## Quién resolvió el problema imposible

El avance llegó desde Stanford. Stefano Ermon, profesor de informática y uno de los coinventores de las técnicas de difusión utilizadas en Stable Diffusion y DALL-E, trabajaba en este problema desde 2019. Años de investigación para entender cómo aplicar la difusión al texto, hasta un avance documentado en un artículo presentado en el ICML 2024, la principal conferencia internacional de aprendizaje automático, que ganó el premio al mejor artículo. No es una distinción menor: significa que la comunidad científica reconoció formalmente el avance como significativo.

En 2024, Ermon fundó Inception Labs en Palo Alto, llevándose consigo a dos antiguos alumnos convertidos en profesores: Aditya Grover de la UCLA y Volodymyr Kuleshov de Cornell. El equipo ampliado incluye investigadores e ingenieros provenientes de Google DeepMind, Meta AI, Microsoft AI y OpenAI, y las contribuciones del grupo no se limitan a la difusión: en su currículum colectivo figuran trabajos fundamentales sobre flash attention, decision transformers y direct preference optimization (DPO), técnicas que marcaron el desarrollo de los modelos de lenguaje modernos.

La financiación llegó en noviembre de 2025 con una ronda de capital semilla de [50 millones de dólares](https://techcrunch.com/2025/11/06/inception-raises-50-million-to-build-diffusion-models-for-code-and-text/), liderada por Menlo Ventures con la participación de Mayfield, M12 (el fondo de capital riesgo de Microsoft), Snowflake Ventures, Databricks Ventures, NVentures (el brazo de inversión de NVIDIA) e Innovation Endeavors. Como inversores ángeles figuran Andrew Ng y Andrej Karpathy; este último, exdirector de IA de Tesla y cofundador de OpenAI, animó públicamente a sus seguidores a probar el modelo, señalando que la naturaleza no autorregresiva de la difusión podría dar lugar a una "psicología nueva, fortalezas y debilidades inéditas". Cuando Karpathy dice que vale la pena probar algo, en el sector se tiende a escuchar.

## Mercury 2: qué hace, cuánto cuesta, qué tan bien funciona

El 24 de febrero de 2026 Inception [lanzó Mercury 2](https://www.inceptionlabs.ai/blog/introducing-mercury-2), presentándolo como el primer "reasoning LLM" basado en difusión disponible en producción. Las cifras de velocidad han sido verificadas de forma independiente por [Artificial Analysis](https://artificialanalysis.ai/models/mercury-2), una de las firmas de benchmarking más rigurosas del sector: 711,6 tokens por segundo en sus evaluaciones estandarizadas multiturno, que sitúan a Mercury 2 en el primer puesto de 132 modelos monitorizados. Con la configuración de hardware óptima, GPUs NVIDIA Blackwell con precisión NVFP4, las cifras internas de Inception ascienden a 1.009 tokens por segundo, con una latencia de extremo a extremo de 1,7 segundos.

La comparación es despiadada para los modelos competidores en la misma categoría: Gemini 3 Flash completa las respuestas en 14,4 segundos, Claude 4.5 Haiku con razonamiento en 23,4 segundos. No es una diferencia de grado, es una diferencia de experiencia de usuario, la sensación subjetiva de "instantaneidad" cambia por completo. [InfoWorld](https://www.infoworld.com/article/4137528/inceptions-mercury-2-speeds-around-llm-latency-bottleneck.html) resumió bien el punto: Mercury 2 no optimiza los márgenes, rediseña el cuello de botella.

En el frente cualitativo, Mercury 2 se posiciona honestamente en la categoría de modelos "rápidos y ligeros", no entre los gigantes del razonamiento profundo. Los benchmarks publicados son claros: 91,1 en AIME 2025 (matemáticas competitivas), 73,6 en GPQA Diamond (razonamiento científico avanzado), 67,3 en LiveCodeBench (programación), 52,9 en TAU-bench (agentes complejos). Son resultados competitivos con Claude 4.5 Haiku y GPT-5 Mini, pero no con Claude Opus 4.6 o los mejores modelos de razonamiento extendido, que en el Artificial Analysis Intelligence Index obtienen puntuaciones del orden de 80-90 sobre 100, mientras que Mercury 2 se queda en 33.

El precio es uno de los aspectos más interesantes: 0,25 dólares por millón de tokens en entrada, 0,75 por millón en salida. Para comparar, Claude 4.5 Haiku cuesta unos 4,90 dólares por millón de tokens en salida, unas seis veces y media más. GPT-5 Mini ronda los 1,90 dólares, unas dos veces y media. A igualdad de volumen, la diferencia de coste en flujos de trabajo de alto tráfico puede valer decenas de miles de dólares al mes. La API es compatible con el estándar de OpenAI: en teoría, para quienes ya usan el ecosistema de OpenAI, es una sustitución sin reescribir el código.
![grafico2.jpg](grafico2.jpg)
[Imagen tomada de inceptionlabs.ai](https://www.inceptionlabs.ai/blog/introducing-mercury-2)

## Dónde funciona realmente Mercury 2

Inception es explícita sobre qué casos de uso está diseñado para cubrir Mercury 2, y los testimonios recogidos en el lanzamiento son coherentes con ese posicionamiento.

El campo más natural son los **bucles de agentes (agentic loops)**: sistemas donde un agente de IA realiza decenas o cientos de llamadas de inferencia para completar una tarea, análisis de código, búsqueda iterativa, flujos de datos. En estos contextos, la latencia no se manifiesta una sola vez, se multiplica en cada paso. Con los modelos tradicionales, un flujo de trabajo de diez pasos que requiere 20 segundos por inferencia conlleva más de tres minutos de espera total. Con Mercury 2, el mismo flujo de trabajo baja de los veinte segundos. No es solo más rápido: cambia qué interacciones son físicamente factibles en tiempo real.

Zed, un editor de código muy seguido en entornos de desarrollo avanzado, es uno de los socios del lanzamiento: su cofundador Max Brunsfeld describió la velocidad de sugerencia como lo suficientemente rápida como para parecer "parte del propio pensamiento". Skyvern, una plataforma de automatización para agentes web, informó que Mercury 2 es al menos dos veces más rápido que GPT-5.2 para sus casos de uso. Wispr Flow, una herramienta para la limpieza en tiempo real de transcripciones de voz, lo evaluó como insustituible para aplicaciones de interacción hombre-máquina de baja latencia.

La **IA de voz** es el segundo ámbito donde la velocidad se vuelve determinante. Las interfaces de voz tienen la ventana de latencia más estrecha en todo el ecosistema de IA: una respuesta que tarda más de dos segundos rompe la naturalidad de la conversación. A 70-90 tokens por segundo, los modelos autorregresivos están al límite de la usabilidad para la voz. Mercury 2 elimina ese límite con un margen enorme. OpenCall y Happyverse AI, ambas activas en el sector de los avatares de voz y los agentes telefónicos, citaron la baja latencia como el factor habilitador principal.

Para los **flujos de búsqueda y RAG** (Generación Aumentada por Recuperación), donde los documentos se recuperan, clasifican y resumen en secuencia, Mercury 2 permite añadir un paso de razonamiento en el ciclo de búsqueda sin disparar el presupuesto de latencia. SearchBlox, activa en la búsqueda empresarial para cumplimiento, analítica y comercio electrónico, declaró que la asociación con Inception hace que la "IA en tiempo real sea práctica" para su producto.

## Sombras en el cuadro: los límites que importan

Mercury 2 es por el momento un modelo **solo de texto**. No procesa imágenes, audio ni vídeo. En un panorama en el que la capacidad multimodal se ha convertido casi en el estándar esperado, especialmente para aplicaciones empresariales complejas, esta es una limitación concreta, no un detalle de pie de página.

Además, es un modelo **solo en la nube, sin pesos abiertos**. No existe una versión descargable, no es posible el despliegue local (on-premise) y no está disponible el ajuste fino (fine-tuning) sobre datos propios. Para organizaciones con requisitos de residencia de datos, soberanía del modelo o necesidad de adaptación especializada —sectores como salud, finanzas, defensa—, esto excluye a Mercury 2 para una amplia clase de casos de uso.

También está el **problema de la verbosidad**. Según documenta la [reseña independiente de Awesome Agents](https://awesomeagents.ai/reviews/review-mercury-2/), Artificial Analysis detectó que durante sus evaluaciones Mercury 2 produjo 69 millones de tokens en salida, frente a una media de 20 millones para modelos equivalentes. El modelo tiende a generar más texto del necesario. En términos prácticos, esto no es solo un problema estético: infla el coste efectivo de salida y añade ruido en los flujos de trabajo que requieren una salida estructurada y concisa. Es un comportamiento gestionable con ingeniería de prompts, pero es un valor predeterminado que requiere atención.

La cuestión más profunda se refiere a la **madurez de la arquitectura**. Los modelos de difusión para texto son una clase emergente, Mercury 2 es de hecho el primer modelo de este tipo disponible en producción comercial. Esto significa que existen menos ingenieros que conozcan los patrones de fallo en producción, menos documentación sobre casos extremos y menos comunidad que ya haya enfrentado y resuelto los problemas típicos. Cuando algo falla en un sistema en producción, y siempre sucede, el apoyo del ecosistema para una tecnología consolidada como GPT o Claude es incomparablemente más rico. No es una crítica a la arquitectura, es un coste real que no aparece en ningún benchmark.

Finalmente, vale la pena señalar que las cifras de velocidad más altas, el título de los 1.009 tokens por segundo, presuponen GPUs NVIDIA Blackwell con precisión NVFP4. Los datos de Artificial Analysis, que reflejan la infraestructura en la nube estándar real, certifican 711,6 tokens por segundo: una cifra extraordinaria, pero distante del titular. No hay datos publicados para hardware más antiguo.

## El mercado habla, pero con cautela

La cuestión relevante no es solo si Mercury 2 funciona (las evidencias independientes sugieren que sí, las promesas de velocidad son reales), sino si el mercado está adoptando efectivamente los modelos de difusión a gran escala, o si aún estamos en la fase de curiosidad técnica.

Existen señales de adopción: integraciones documentadas con herramientas como Zed, Skyvern, Wispr Flow, SearchBlox, Viant (una plataforma publicitaria que declaró usar Mercury para optimizar campañas en tiempo real). La [disponibilidad en Azure AI Foundry](https://www.inceptionlabs.ai/blog/mercury-azure-foundry), anunciada en noviembre de 2025, abre Mercury al vasto ecosistema empresarial de Microsoft. La compatibilidad con la API de OpenAI baja la barrera de entrada a casi cero para quienes ya operan en ese ecosistema.

Por otro lado, la posición de Mercury 2 en la categoría "Haiku-class" de modelos, competitiva con los modelos rápidos pero no con los mejores para el razonamiento profundo, limita estructuralmente su uso a casos donde la velocidad prima sobre la complejidad del razonamiento. Para decisiones que requieren análisis de documentos largos y complejos, síntesis avanzada de múltiples fuentes o razonamiento sobre escenarios matizados, los modelos de frontera mantienen una ventaja real que Mercury 2 no elimina. Como observó [The New Stack](https://thenewstack.io/inception-labs-mercury-2-diffusion/), el propio Ermon es sincero al respecto: Mercury 2 compite con la categoría Haiku/Flash, no con Opus o GPT.

La apuesta de Inception es que la trayectoria de la calidad en los modelos de difusión seguirá la misma curva de escalabilidad vista en los modelos autorregresivos: la calidad se puede mejorar con el tiempo, con la ventaja estructural de la velocidad como punto de partida. Es una apuesta plausible, aún no verificada.

## Preguntas abiertas: ¿el futuro es paralelo?

Mercury 2 no responde a la pregunta más grande que plantea: ¿puede la difusión convertirse realmente en el paradigma dominante para los modelos de lenguaje, o seguirá siendo un enfoque especializado para casos de uso de alta velocidad?

Ermon ha declarado que imagina un futuro donde todos los modelos de lenguaje estén basados en difusión. Es una visión ambiciosa, y quien la expresa, uno de los científicos que ayudó a construir los cimientos de la difusión para imágenes, tiene credenciales para sostenerla. Pero pasar de "funciona excepcionalmente bien para un subconjunto específico de casos de uso" a "sustituye al paradigma autorregresivo como modelo general" es un salto enorme, y aún no hay pruebas de que la brecha cualitativa con los modelos de frontera esté destinada a cerrarse.

Además, quedan preguntas abiertas concretas: ¿cómo se comportan los modelos de difusión en razonamientos de cadena de pensamiento muy largos, donde la coherencia a través de miles de tokens es crucial? ¿Qué pasa con la calidad a 50.000 o 100.000 tokens de contexto, cuando la ventana de 128K se estresa de verdad? ¿Cómo se gestiona éticamente una arquitectura cuya producción de salida es menos interpretable paso a paso que la autorregresiva?

La velocidad es real. El coste es competitivo. El equipo es creíble por encima de toda duda razonable. Las limitaciones actuales son concretas y están documentadas. Mercury 2 representa algo genuinamente nuevo en el panorama de los modelos de lenguaje: no el modelo más inteligente disponible hoy, sino quizás una señal de hacia dónde debe ir todavía la conversación sobre la eficiencia de la inferencia de la IA.

La máquina de escribir, token tras token, podría tener realmente los días contados. Pero la novela que se escribirá después, y qué tan buena será, está aún por ver.

---
