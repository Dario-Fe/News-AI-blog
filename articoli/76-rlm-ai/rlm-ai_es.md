---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-01-19
author: "Dario Ferrero"
---

# Más allá del muro del contexto: los Modelos de Lenguaje Recursivos desafían el límite invisible de la IA
![rlm-ai.jpg](rlm-ai.jpg)

*Existe un problema en la inteligencia artificial moderna del que se habla poco, pero que todo desarrollador y usuario intensivo de chatbots ha experimentado al menos una vez: la sensación de que el modelo, después de una conversación prolongada, se vuelve progresivamente más tonto. No es una impresión subjetiva, ni una falta de claridad en sus peticiones. Es un fenómeno técnico preciso que los investigadores llaman *context rot*, literalmente "putrefacción del contexto", y representa una de las limitaciones más frustrantes de la arquitectura actual de los grandes modelos de lenguaje.*

Imagine tener que escribir una novela disponiendo solo de un post-it. Cada vez que añade una nueva frase, tiene que borrar una vieja. Es más o menos lo que sucede cuando un modelo de lenguaje alcanza el límite de su ventana de contexto, esa ventana de memoria a corto plazo dentro de la cual puede "ver" y procesar información. GPT-5, el modelo insignia de OpenAI, dispone de 400.000 tokens a través de la API (unas 300.000 palabras), que parecen muchos hasta que intenta analizar una base de código completa o una colección de documentos legales. Pero el verdadero problema no es solo el tamaño: el rendimiento de los modelos se degrada al aumentar la longitud de la entrada, incluso en tareas triviales.

Aquí es donde entra en juego el trabajo de Alex Zhang, Tim Kraska y Omar Khattab del MIT CSAIL, publicado en diciembre de 2025 en [arXiv](https://arxiv.org/html/2512.24601v1). Su artículo propone los Modelos de Lenguaje Recursivos, un marco que da un vuelco completo al enfoque del problema: en lugar de intentar ampliar hasta el infinito la memoria del modelo, le enseñan a razonar *sobre* la propia memoria, tratándola como un entorno externo que explorar programáticamente.

## Cuando leer se convierte en recordar

Para entender la intuición detrás de los RLM, conviene partir del problema. La arquitectura transformer en la que se basan los LLM modernos compara cada nuevo token con todos los tokens anteriores en la ventana de contexto, creando relaciones n² que se vuelven cada vez más costosas a medida que el contexto crece. Es como si, cada vez que pronunciara una palabra, su cerebro tuviera que repasar mentalmente todas las conversaciones de su vida. Impráctico.

La investigación de Chroma [ha demostrado](https://research.trychroma.com/context-rot) que incluso los modelos más avanzados sufren de sesgo posicional: una información situada en la primera posición obtiene un 75% de precisión, la misma información en la décima posición desciende al 55%. No es cuestión de cuántos tokens consiga meter en la ventana, sino de cómo el modelo consigue realmente usarlos.

Zhang y sus colegas tomaron un camino diferente. En lugar de obligar al modelo a ingerir todo el prompt en un único paso, los RLM tratan el prompt como parte de un entorno externo con el que el modelo puede interactuar simbólicamente. En la práctica, el contexto se carga como una variable de Python en un entorno REPL (Read-Eval-Print Loop), y el modelo puede escribir código para inspeccionarlo, seccionarlo, buscar patrones y, lo que es crucial, llamarse recursivamente a sí mismo o a otros LLM sobre porciones específicas del contenido.

Piense en la diferencia entre leer un libro de principio a fin y, en cambio, consultarlo como lo haría con una enciclopedia: saltando directamente al índice, identificando las secciones relevantes, quizás tomando notas sobre lo que encuentra. Los RLM replican este segundo enfoque, metacognitivo y estratégico.

## REPL: el diálogo interno

La implementación técnica es refinada en su simplicidad. Cuando un usuario envía un prompt a un RLM, este se almacena como una variable de cadena en un entorno REPL de Python. El modelo raíz (llamémoslo LM₀) nunca recibe directamente esa cadena en su ventana de contexto. En su lugar, recibe un prompt del sistema que le explica cómo puede interactuar con la variable: puede leer fragmentos específicos de ella, puede escribir funciones de ayuda para procesarla, puede lanzar llamadas sub-LM recursivas (LM₁, LM₂...) sobre porciones seleccionadas, y puede combinar los resultados.

En esencia, el modelo trabaja en tres modos distintos. Primero explora el contexto a través de operaciones de lectura y búsqueda programática, un poco como si usara grep o regex en un archivo de texto. Luego descompone el problema en subtareas más manejables, decidiendo autónomamente qué porciones de contexto merecen un análisis en profundidad. Finalmente delega estas subtareas a instancias recursivas de sí mismo o de otros modelos, agregando luego los resultados en una respuesta final.

[El repositorio oficial de GitHub](https://github.com/alexzhang13/rlm) proporciona una implementación plug-and-play que simplemente sustituye la llamada estándar `llm.completion(prompt, model)` por `rlm.completion(prompt, model)`. La interfaz externa sigue siendo idéntica para el usuario, pero bajo el capó se produce esta danza recursiva de exploración y computación.

El propio Zhang [en su blog](https://alexzhang13.github.io/blog/2025/rlm/) utiliza una analogía esclarecedora: es como cuando el historial de Claude Code se hincha o chateas durante mucho tiempo con ChatGPT y el modelo parece volverse progresivamente más tonto. La solución intuitiva sería dividir el contexto en dos llamadas separadas y luego combinar los resultados en una tercera: exactamente lo que hacen los RLM de forma sistemática y recursiva.
![rlm-schema1.jpg](rlm-schema1.jpg)
[Imagen extraída de arxiv.org](https://arxiv.org/html/2512.24601v1)

## Benchmarks contra la realidad

Las cifras del artículo son impresionantes, pero hay que leerlas con la debida cautela. En OOLONG, un benchmark de comprensión de contextos largos, un RLM basado en GPT-5-mini superó a GPT-5 base en más del doble en términos de respuestas correctas, procesando prompts de 132.000 tokens. En la tarea S-NIAH (una variante más compleja de la clásica aguja en un pajar), los RLM manejan entradas hasta dos órdenes de magnitud por encima de los tamaños nativos de la ventana de contexto.

Pero hay una contrapartida importante: los costes. El artículo reporta variaciones significativas con respecto a la línea de base, en algunos casos hasta tres veces superiores, dependiendo de cuántas llamadas recursivas decida efectuar el modelo. No es una varita mágica que lo abarate todo: es una arquitectura que cambia tiempo de computación por capacidades de razonamiento ampliadas.

En el conjunto de datos BrowseComp-Plus, creado para probar tareas de búsqueda y síntesis en enormes volúmenes de documentos, los RLM demostraron poder procesar eficazmente más de 10 millones de tokens. Aquí, sin embargo, entra en juego otra consideración: en algunos casos, la verificación de la respuesta resultó redundante y aumentó significativamente el coste por tarea. El modelo podía intentar reproducir su respuesta correcta más de cinco veces antes de elegir la equivocada al final.

Es un recordatorio importante: los RLM no están optimizados automáticamente para la eficiencia. La estrategia de descomposición y recursión la decide el propio modelo, que puede cometer errores de juicio sobre cuándo es oportuno recurrir a más subconsultas.

## El precio del infinito

Prime Intellect, una organización centrada en la investigación de IA abierta, [ha adoptado los RLM como elemento central](https://www.primeintellect.ai/blog/rlm) de su estrategia para agentes de largo horizonte. Creen que enseñar a los modelos a gestionar su propio contexto de principio a fin mediante el aprendizaje por refuerzo será el próximo gran avance, permitiendo a los agentes resolver tareas que se extienden durante semanas o meses.

Han lanzado RLMEnv, un entorno de entrenamiento específicamente diseñado para entrenar modelos con andamiaje RLM integrado. La idea es intrigante: en lugar de aprender arquitecturas de atención más eficientes (que es un problema de modelado del lenguaje), se puede aprender a gestionar el contexto a través del resultado de las tareas resueltas. Un enfoque complementario: la atención eficiente retrasa la putrefacción del contexto, el plegado del contexto (término que algunos usan para describir estrategias como los RLM) permite al modelo gestionarlo activamente.

Pero esto introduce cuestiones éticas y de gobernanza. Un modelo capaz de gestionar autónomamente su propio contexto en horizontes temporales tan amplios podría utilizarse para tareas sensibles en las que la trazabilidad de las decisiones se vuelve crítica. Pensemos en decisiones financieras, diagnósticos médicos o evaluaciones legales: la naturaleza recursiva y programática de los RLM hace que la interpretabilidad del proceso de toma de decisiones sea más compleja que una única llamada a un LLM.

La Ley de IA de la UE clasifica los sistemas de IA en función de su nivel de riesgo, y los sistemas capaces de mantener un estado y un razonamiento en horizontes temporales largos podrían entrar en categorías de alto riesgo que requieren auditorías estrictas. No es un problema solo de los RLM, obviamente, pero su capacidad para operar autónomamente sobre volúmenes de datos enormes amplifica la necesidad de mecanismos de registro y explicabilidad robustos.

## Alternativas sobre la mesa

Los RLM no son la única respuesta al problema del contexto largo. Existen al menos tres enfoques principales que vale la pena comparar.

El primero es la modificación arquitectónica directa: modelos como Llama 4 con sus variaciones de RoPE (Rotary Position Embeddings) o Gemini 2.5 Pro con window attention están diseñados de forma nativa para manejar ventanas de contexto más amplias. Funcionan, pero incluso en condiciones mínimas y controladas, el rendimiento se degrada al aumentar la longitud de la entrada de formas sorprendentes y no uniformes.

El segundo es RAG (Retrieval-Augmented Generation), donde un sistema de recuperación externo proporciona al modelo solo los fragmentos relevantes de una base de datos más amplia. Es eficaz para bases de conocimiento estructuradas, pero requiere una infraestructura dedicada (modelos de incrustación, bases de datos vectoriales, estrategias de fragmentación) e introduce una dependencia de componentes externos que pueden convertirse en el cuello de botella.

El tercero son marcos como MemGPT o sistemas multiagente como el DisCIPL desarrollado también en el MIT. [Este último](https://news.mit.edu/2025/enabling-small-language-models-solve-complex-reasoning-tasks-1212) utiliza un LLM como "líder" que planifica la estrategia y distribuye el trabajo a modelos más pequeños. Funciona bien para tareas con restricciones verificables (como la programación o la planificación), menos para análisis abiertos donde la verificación de la corrección es matizada.

Los RLM se posicionan en un espacio intermedio: más flexibles que RAG (no necesitan preindexación), más de propósito general que los sistemas multiagente (no requieren orquestación específica de la tarea), pero potencialmente más caros que los enfoques arquitectónicos nativos cuando estos funcionan bien.
![rlm-schema2.jpg](rlm-schema2.jpg)
[Imagen extraída de arxiv.org](https://arxiv.org/html/2512.24601v1)

## Implementaciones desde la base

La comunidad de código abierto reaccionó rápidamente. [Una implementación en TypeScript](https://www.reddit.com/r/opensource/comments/1q5f1sb/i_built_a_typescript_implementation_of_recursive/) apareció en Reddit pocas semanas después de la publicación del artículo, señal de que la idea resuena entre los desarrolladores que se enfrentan a problemas concretos. Las [implementaciones en Python](https://github.com/ysz/recursive-llm) están proliferando, algunas con un enfoque en sandboxes específicos (Docker, WebAssembly) para garantizar la ejecución segura del código generado por el modelo.

Es interesante observar cómo diferentes implementaciones de la comunidad están experimentando con entornos alternativos al REPL de Python. Algunos usan REPL de Clojure para aprovechar la naturaleza inmutable de los datos, otros están explorando entornos SQL para consultas en bases de datos estructuradas, y otros incluso Bash para tareas de administración de sistemas.

Esto plantea una cuestión más amplia: ¿hasta qué punto la elección del entorno influye en la eficacia de los RLM? El artículo del MIT utiliza Python porque es el lenguaje más familiar para la mayoría de los LLM (es omnipresente en los datos de entrenamiento), pero nada impide utilizar DSL (Lenguajes Específicos de Dominio) optimizados para dominios de aplicación específicos.

## Cuestiones abiertas

A pesar de los resultados prometedores, quedan preguntas fundamentales. La primera se refiere al entrenamiento. Zhang y Khattab están especialmente entusiasmados con la posibilidad de enseñar explícitamente a los modelos a razonar como los RLM, lo que podría representar otro eje de escalado para la próxima generación de sistemas lingüísticos. Pero, ¿cómo se entrena exactamente a un modelo para que descomponga de forma óptima el contexto? Se podrían utilizar técnicas de aprendizaje por refuerzo en las trayectorias REPL, premiando las descomposiciones que minimizan el coste total manteniendo una alta precisión.

Modelos como o1 de OpenAI ya incorporan un razonamiento ampliado durante la inferencia, pero lo hacen de forma opaca y no programática. Los RLM podrían beneficiarse de un enfoque híbrido: razonamiento interno para planificar la estrategia de descomposición, ejecución programática para implementarla.

La segunda cuestión se refiere a la reproducibilidad. Las trayectorias RLM no son deterministas: el mismo prompt puede generar diferentes estrategias de descomposición en ejecuciones sucesivas. Esto es problemático para aplicaciones en las que la consistencia es crítica (cumplimiento, auditoría, investigación reproducible). Se necesitarán técnicas para restringir el espacio de exploración del modelo o para garantizar siempre el mismo resultado de las operaciones.

La tercera es sobre la escalabilidad extrema. El artículo prueba hasta más de 10 millones de tokens, pero ¿qué sucede con 100 millones? ¿Con 1.000 millones? En algún momento, incluso la gestión programática del contexto se convierte en un problema de complejidad computacional. Podría ser necesario un "meta-RLM" que gestione otros RLM en una jerarquía de varios niveles, un poco como en los sistemas operativos con múltiples niveles de caché.

Finalmente, está la cuestión de los modelos abiertos frente a los cerrados. Las pruebas del artículo utilizan principalmente GPT-5, pero ¿cómo se comportan los modelos abiertos como Qwen3 o Llama 4? La capacidad de seguir instrucciones REPL complejas y de escribir código correcto varía significativamente entre los modelos. Un RLM es tan eficaz como el modelo raíz que lo guía.

El enfoque de Zhang y sus colegas no resuelve mágicamente el problema de la putrefacción del contexto, sino que lo transforma de un límite arquitectónico a un desafío de diseño de sistemas. Y quizás, al igual que sucedió con los sistemas operativos que introdujeron la memoria virtual para superar los límites de la RAM física, los Modelos de Lenguaje Recursivos representan un cambio de paradigma: ya no modelos que *tienen* memoria, sino modelos que *gestionan* la memoria.

Es pronto para decir si se convertirán en el estándar de facto, pero una cosa es cierta: el debate sobre cómo hacer que la IA razone en contextos arbitrariamente largos acaba de empezar, y las próximas generaciones de modelos tendrán que enfrentarse seriamente a esta dirección de investigación.
