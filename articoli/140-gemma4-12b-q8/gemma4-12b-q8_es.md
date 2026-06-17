---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-06-17
author: "Dario Ferrero"
---

# Gemma 4 12B en local: ¿mejor pequeño al máximo o grande estrangulado?
![gemma4-12b-q8.jpg](gemma4-12b-q8.jpg)

*En los tests anteriores sobre Gemma 4 26B y Qwen3.6 35B, siempre había tenido que enfrentarme al mismo problema: la VRAM nunca era suficiente. Modelos grandes, cuantizaciones agresivas, capas en offload. Funcionaban, pero con la sensación de estar conduciendo un coche potente con el freno de mano echado. Entonces llegó Gemma 4 12B. Más pequeño, por supuesto. Pero con una arquitectura nueva y la promesa de ejecutarse enteramente en GPU consumer sin compromisos. Así que decidí hacer un experimento diferente: ya no "¿quién es el modelo más potente?", sino "¿puede un modelo más pequeño usado al máximo de sus potencialidades vencer a uno más grande pero estrangulado?". Tomé exactamente los mismos tests, las mismas preguntas, y los comparé.*

Quienes sigan esta serie ya conocen el hardware y el método. Para todos los detalles sobre la instalación, elección del framework y filosofía del laboratorio, remito al [primer artículo de la serie sobre Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1), que sigue siendo la referencia metodológica de todos estos experimentos. Aquí me limito a lo esencial.

La máquina es siempre la misma: un PC ensamblado con criterio pero sin exagerar, con procesador AMD Ryzen 7700, 32 GB de RAM DDR5, y una GPU AMD Radeon RX 9060 XT con 16 GB de VRAM. Hardware de usuario avanzado, no de laboratorio de investigación. El software es [LM Studio](https://lmstudio.ai/), la aplicación de escritorio que permite descargar e iniciar modelos sin abrir un terminal, con la valiosa característica de mostrar de antemano una estimación del rendimiento esperado en vuestra configuración.

El método, lo reitero como hice en las entregas anteriores, no es científico en el sentido académico del término. No hay un protocolo revisado por pares, no hay una muestra estadísticamente significativa de prompts. Los tests son pruebas de campo, realizadas con las herramientas de un usuario exigente, y las notas son evaluaciones personales, no sentencias. La batería de pruebas ha permanecido idéntica a la utilizada para [Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1), [Gemma 4 26B](https://aitalk.it/it/gemma4-26b.html) y [Qwen3.6 35B](https://aitalk.it/it/qwen36-35b-ai.html): razonamiento científico, multimodalidad en tablas, generación de código complejo, planificación multilingüe, contexto largo en un PDF de 460 páginas, razonamiento espacial en una habitación desordenada, y los tests extra sobre agente multi-paso y conversación larga.

## No es un hermano menor

Antes de entrar en los tests, vale la pena detenerse un momento en un punto que corre el riesgo de pasar desapercibido: Gemma 4 12B no es simplemente una versión reducida del [26B MoE que ya había testeado](https://aitalk.it/it/gemma4-26b.html). No es un recorte más económico del mismo proyecto. Es algo estructuralmente diferente, y la diferencia no es de grado sino de tipo.

El 26B MoE, como todos los modelos multimodales tradicionales, usa encoders separados para gestionar imágenes y texto: una parte del modelo recibe las imágenes, las comprime, las transforma en una representación numérica, y solo después pasa el resultado al modelo lingüístico propiamente dicho. Es un proceso de dos fases, con un "traductor" en medio que inevitablemente pierde algo por el camino, como cualquier traducción.

El 12B elimina este paso por completo. Es el primer modelo "unificado" de la familia Gemma, y esa palabra en el nombre no es marketing: es arquitectura. Un parche de imagen sufre solo una multiplicación de matriz y la adición de coordenadas espaciales, y termina directamente en el mismo espacio donde viven los tokens de texto. Imágenes y palabras son procesadas por la misma atención, compartiendo la misma representación interna. No hay un traductor: hay dos lenguas que se convierten en una sola.

Esta elección de diseño tiene consecuencias directas en la memoria, la velocidad y la calidad de las respuestas multimodales. Y es precisamente el motivo por el que testarlo con la misma batería de pruebas de los modelos anteriores es interesante: no se está midiendo solo el tamaño, se está midiendo también una idea diferente de cómo los datos deberían fluir a través de un modelo.

## La configuración: finalmente sin compromisos

Y aquí estamos en el corazón del experimento. Por primera vez en esta serie de tests, he podido configurar el modelo sin tener que elegir qué sacrificar. LM Studio mostraba el verde decidido, no el naranja del límite como con el 26B MoE, no el rojo de la configuración desaconsejada.
![tabella1.jpg](tabella1.jpg)

El detalle que lo cambia todo es el offload GPU: 48 capas de 48. El modelo se ejecuta enteramente en la VRAM, sin tener que distribuir partes de sí mismo en la RAM del sistema. Con el 26B MoE en Q4_K_M me veía obligado a un offload parcial, y esa elección pesaba sobre la velocidad y la latencia. Aquí, por primera vez, la máquina trabaja sin ese freno.

El resultado se siente inmediatamente: la velocidad media se ha asentado en torno a los 17 tokens por segundo, frente a los 10-12 de Qwen 36 35B, y poco por debajo de los 20 de Gemma 4 26B que con 8B activos (los "expertos activos" pesaban mucho en el rendimiento, 8 era el punto mejor).

Hay una paradoja interesante surgida de los tests. Gemma 4 26B MoE resultó ser más rápido que el 12B, a pesar de tener el doble de parámetros totales. El secreto está en la arquitectura. El 26B es un modelo MoE: de 25 mil millones de parámetros totales, solo activa unos 4 (8 en mi test) por cada token. Es como tener una biblioteca enorme pero, para cada pregunta, solo hojeas un pequeño número de libros. El 12B, al ser un modelo denso, activa en cambio todos sus 12 mil millones de parámetros en cada token, realizando más cálculos y resultando por tanto ligeramente más lento en la media.

Sin embargo, los 25 mil millones de parámetros del MoE deben residir igualmente en la VRAM, ocupando más del doble de memoria que el 12B. Y el overhead de routing para gestionar a los expertos se vuelve evidente en contextos largos, donde el 26B pierde parte de su ventaja mientras que el 12B mantiene un rendimiento más estable. En resumen: el 26B es más rápido pero más exigente en VRAM y menos estable en secuencias largas; el 12B es más ligero, previsible y para la mayoría de los usos diarios más que suficiente. La elección depende de lo que busquéis.

## Los tests

### Test 1 — Razonamiento científico: el mecanismo de Higgs *(Nota: 5/5)*

*Velocidad: 17,45 tokens/segundo*

Lo que uso desde siempre como termómetro de la inteligencia del modelo: explicar el mecanismo de Higgs y la ruptura de la simetría electrodébil a un estudiante universitario de física. Una pregunta que requiere rigor sin sacrificar la claridad, y la capacidad de construir un camino que guíe al lector a través de conceptos no banales.

La respuesta llegó estructurada en cinco secciones con la lógica de una lección bien conducida, partiendo del problema central, es decir, por qué no se pueden escribir términos de masa explícitos sin violar la invariancia de gauge, hasta la solución completa, con el grupo de gauge SU(2)_L × U(1)_Y, la condición μ² < 0 que hace que el mínimo del potencial ya no esté en cero, y la explicación de por qué el fotón permanece sin masa gracias a la simetría residual U(1)_em. La precisión científica era impecable: fórmulas correctas, valor de expectación del vacío, la sugerente imagen de los bosones de Goldstone que son "comidos" por la polarización longitudinal, una "síntesis para el examen" final en cinco puntos que resume todo el mecanismo sin banalizarlo.

Lo que sorprende, sin embargo, no es solo la calidad de la respuesta: es la velocidad con la que llegó. Con Qwen3.6 35B estaba en torno a 11 tokens por segundo. Con Gemma 4 26B MoE a unos 10. Con este modelo a 17,45. La diferencia no es despreciable en la práctica diaria.

**Nota: 5/5.** Una apertura de serie difícil de mejorar.

### Test 2 — Multimodalidad: leer una hoja de cálculo corporativa *(Nota: 5/5)*

*Velocidad: 17,64 tokens/segundo*

El segundo test ponía a prueba la parte multimodal con una imagen deliberadamente no ideal: un pantallazo de una hoja Excel titulada "COSTES DE PERSONAL", una proyección financiera a cinco años de 2023 a 2027, con columnas para partidas de coste, unidades, costes unitarios y totales.

El modelo hizo lo que se espera de un analista, no de un OCR. Identificó correctamente la estructura del documento, las cinco categorías, Valores globales, Operarios especializados, Empleados, Directivos, Colaboradores, leyó los valores numéricos con precisión, notó que los costes unitarios permanecen fijos durante todo el período mientras que las unidades aumentan, y sacó la conclusión correcta: no es inflación, es expansión del equipo. Identificó 2026 como "el año de la gran expansión", con el salto neto de los costes globales, e incluso observó que las cotizaciones a la seguridad social calculadas constantemente al 33% indican una planificación fiscal estandarizada. Un detalle que un CFO notaría, y que el modelo extrajo autónomamente de una tabla.

Esta es la diferencia que la arquitectura unificada debería aportar: no solo leer los datos, sino entender el contexto en el que existen. Si el test 1 confirmó las expectativas, el test 2 comenzó a responderme a la pregunta que tenía en la cabeza desde el principio.

**Nota: 5/5.** Lectura y análisis, no solo transcripción.

### Test 3 — Generación de código: un problema NP-hard *(Nota: 4,95/5)*

*Velocidad: 17,99 tokens/segundo*

El test de coding clásico de la serie: implementar en Python un algoritmo para encontrar el ciclo de longitud máxima en un grafo no dirigido, con la petición de explicar la complejidad temporal. Un problema NP-hard que requiere no solo capacidad de implementación sino conciencia teórica.

La respuesta fue técnicamente excelente, probablemente la mejor obtenida en este test en toda la serie. El modelo abrió declarando explícitamente que el problema es NP-hard y que no existe un algoritmo de tiempo polinómico conocido, una madurez teórica que no todos los asistentes de programación muestran. La implementación en backtracking con DFS era limpia y correcta, con una técnica de "symmetry breaking" que impone `neighbor > start_node` para evitar explorar el mismo ciclo varias veces, una optimización no banal que reduce el espacio de búsqueda. Explicación de la complejidad clara y honesta: factorial en el peor de los casos, lineal en el espacio.

Hay sin embargo una única, pequeña, mancha: la respuesta llegó en inglés, a pesar de que el prompt estaba en italiano. En los tests 1 y 2 el modelo había respondido correctamente en italiano, por lo que no es un problema estructural. Es un descuido. El código es perfectamente funcional, la explicación es clara, pero la falta de adherencia al idioma del prompt es una señal que vale la pena notar. Nada que comprometa el resultado técnico, pero algo que en un asistente diario no se querría ver.

**Nota: 4,95/5.** La mejor solución de la serie en este test, con un lunar lingüístico que no invalida la sustancia.

### Test 4 — Multilingüe y planificación: cinco días en Japón *(Nota: 5/5)*

*Velocidad: 17,41 tokens/segundo*

El test multilingüe: actuar como agente de viajes, planificar un itinerario de cinco días en Japón para un cliente francés, con enfoque en templos históricos y comida callejera, y una sección final en italiano con consejos para un turista italiano. El test que en el 26B MoE había producido "suggeramenti" y una palabra con terminación cirílica.

El francés era impecable, fluido, con expresiones que muestran un dominio estilístico real: "âme historique", "havre de paix", "splendeur des temples". El itinerario era logístico y realista, Asakusa con el Senso-ji el primer día, Meiji Jingu y Harajuku el segundo, Shinkansen hacia Kioto y Fushimi Inari el tercero, Kinkaku-ji y Kiyomizu-dera el cuarto, Nara con el Todai-ji el quinto. Cinco días llenos pero no imposibles. Los consejos prácticos eran concretos y útiles: la tarjeta Suica, el Pocket Wi-Fi, la etiqueta de no comer caminando, las frases clave en japonés transliterado.

La sección en italiano fue la mejor que he obtenido en este test en toda la serie. Nada de "suggeramenti", ninguna terminación cirílica, ninguna imperfección. Solo italiano correcto, fluido, útil. Un resultado que el 26B MoE no había alcanzado, al menos no de forma tan limpia.

Hay sin embargo un pequeño lapsus léxico en el título del quinto día, donde el modelo escribe "Les Daimyos", los señores feudales, en lugar de "Les daims", los ciervos sagrados de Nara. Una confusión entre dos términos que suenan parecido pero tienen significados completamente diferentes. No compromete la comprensión del itinerario, pero vale la pena señalarlo.

**Nota: 5/5.** La mejor sección en italiano de la serie, con un pequeño lapsus francés que no empaña el resultado global.

### Test 5 — Contexto largo: 460 páginas al vuelo *(Nota: 4,8/5)*

*Velocidad: 10,15 tokens/segundo*

Aquí las cosas se ponen interesantes. El mismo AI Index Report 2025 de Stanford, el mismo PDF de unas 460 páginas cargado en todos los tests anteriores, la misma pregunta sobre el crecimiento de la generación de vídeo con petición de indicar las páginas de referencia.

El modelo respondió al primer intento, sin bloqueos, sin insistencias, lo cual ya es una mejora significativa respecto a los problemas que había tenido con Qwen 3.5. La síntesis fue correcta y pertinente: modelos emergentes como Runway, Luma y Kuaishou, el célebre ejemplo del prompt "Will Smith eating spaghetti" como marcador del salto cualitativo, las funcionalidades de Movie Gen de Meta, la comparación entre Veo 2 y competidores. Todo presente, todo preciso.

Sin embargo, la precisión en la recuperación de la página fue menos granular que en los tests anteriores. El modelo indicó "en torno a la página 127", mientras que Gemma 26B había indicado las páginas 125-126-127 y Qwen3.6 126-127. No es un error, es una respuesta menos precisa. La diferencia entre "aquí exactamente" y "más o menos aquí".

El dato más significativo, sin embargo, es otro: la velocidad cayó a 10,15 tokens por segundo, frente a los 17 y más de los tests anteriores. Es la primera vez en esta sesión que la generación se ralentiza sensiblemente. La causa es el contexto saturado: con 24k tokens activos y un PDF enorme que procesar, la VRAM se llena y el throughput baja. No es un defecto del modelo, es la física de la memoria. Pero es una información valiosa para quien deba elegir: en tareas que requieren contextos muy largos, la fluidez disminuye.

**Nota: 4,8/5.** Respuesta al primer intento, pero menos precisa y más lenta que en los tests anteriores. El contexto largo tiene un coste.

### Test 6 — Razonamiento espacial: la habitación en el caos *(Nota: 5/5)*

*Velocidad: 17,56 tokens/segundo*

La fotografía de una habitación en gran desorden, la misma utilizada en toda la serie. Describir la disposición de los objetos y sugerir cómo ordenar para crear más espacio. Un test que mide algo difícilmente estandarizable: la inteligencia visoespacial, la capacidad de ver una escena tridimensional en una fotografía bidimensional y razonar sobre ella.

La velocidad volvió inmediatamente a los niveles de los primeros tests, confirmando que la caída del test anterior estaba ligada al contexto largo y no a un problema generalizado. La respuesta fue precisa y bien organizada por áreas funcionales: la cama como elemento central sumergida por sábanas y ropa, las dos estanterías de escalera a los lados del cabecero, el área de estudio con escritorio y mueble, el suelo como área más crítica. El modelo notó el cesto azul a los pies de la cama, el plaid rojo en el lado derecho, el espejo que "duplica visualmente el desorden", la ropa esparcida y los zapatos. La estrategia de reordenación era lógica y motivada: primero el suelo porque es el obstáculo principal a la circulación, luego el cesto azul como punto de acumulación, luego la cama, finalmente las estanterías para reducir el ruido visual.

En comparación con los mejores tests de la serie, el modelo no llegó a notar los reflejos específicos en el espejo con el mismo nivel de detalle que había visto con Qwen3.5 y Gemma 26B. Pero la calidad de la descripción y de la planificación es de todos modos excelente. No es un paso atrás: es una elección diferente de qué enfatizar.

**Nota: 5/5.** Descripción precisa, plan de reordenación lógico, velocidad vuelta a los niveles óptimos.

### Test 7 — Agente multi-paso: planificar un proyecto de software *(Nota: 5/5)*

*Velocidad: 17,26 tokens/segundo*

El test que mide la capacidad de organizar el trabajo, no solo de ejecutarlo. Pedí planificar el desarrollo de una web app para la gestión de los gastos familiares: stack tecnológico, estructura del proyecto, roadmap detallada para un equipo de dos desarrolladores.

La respuesta demostró una madurez proyectual notable. El stack propuesto era moderno y coherente: Next.js con Tailwind para el frontend, Node.js con Prisma ORM para el backend, PostgreSQL, NextAuth.js para la autenticación, Recharts para los gráficos, PapaParse para el CSV, react-pdf para los informes, Resend para los correos electrónicos. Cada elección tenía una lógica implícita en el contexto del proyecto. La estructura del código estaba organizada por features, un enfoque profesional y escalable. La roadmap se articulaba en ocho sprints con enfoques claros, entregables concretos, subdivisión del trabajo entre los dos desarrolladores, y, detalle que marca la diferencia, criticidades identificadas para cada uno. "Formatos CSV no estandarizados", "renderizado del PDF difícil", "bugs imprevistos en producción": la capacidad de anticipar los problemas antes de que ocurran es la señal de una comprensión profunda del ciclo de desarrollo de software. Los consejos estratégicos finales, "Database First", validación con Zod, tests unitarios para los cálculos financieros, eran prácticos y de senior developer.

Es el tipo de respuesta que un project manager experto firmaría, no solo una herramienta que escribe código bajo demanda.

**Nota: 5/5.** Planificación completa, realista, con las criticidades adecuadas en el lugar adecuado.

### Test 8 — Conversación larga: coherencia en cuatro turnos *(Nota: 5/5)*

*Velocidad: de 17,65 a 15,98 tokens/segundo*

El test que evalúa una cualidad diferente a las demás: no la destreza en una sola respuesta, sino la capacidad de mantener el hilo a través de una conversación que se construye en el tiempo. Qwen3.6 había introducido esta prueba para testear su funcionalidad de "thinking preservation". Aquí la he propuesto de nuevo con la misma estructura: cuatro turnos en una sesión de diseño colaborativo, con elecciones tecnológicas que se acumulan y se refinan.

En el primer turno pedí un consejo sobre el stack para una app de task management. En el segundo, cómo gestionar las notificaciones en tiempo real para 1000 usuarios concurrentes: el modelo explicó por qué el polling está desaconsejado y por qué WebSocket con Redis Pub/Sub es la elección correcta, citando también la alternativa SSE con pros y contras. En el tercero, el esquema de la base de datos: seis tablas en orden lógico, relaciones clave, consejos de senior developer sobre el uso de UUID, índices y soft delete. En el cuarto, pedí un resumen de todas las elecciones hechas y una estrategia de escalabilidad a 10.000 usuarios.

El modelo recordó correctamente todo. El stack del primer turno, las motivaciones para WebSocket del segundo, las estructuras de datos del tercero. Añadió espontáneamente una estrategia de escalabilidad en cinco puntos: load balancer, Redis Pub/Sub para la gestión distribuida de las conexiones, connection pooling con PgBouncer, colas asíncronas con BullMQ, caching. Sin contradicciones, sin olvidos.

Un dato vale la pena señalar: la velocidad cayó progresivamente, de 17,65 tokens por segundo en el primer turno a 15,98 en el cuarto. El fenómeno es previsible y físicamente comprensible, con cada turno la KV cache se llena y el modelo debe gestionar un contexto cada vez más largo. La caída es contenida, unos 1,7 tokens por segundo en cuatro turnos, y no compromete la fluidez. Pero es un comportamiento real que quienes usen el modelo para sesiones de trabajo prolongadas encontrarán útil conocer.

**Nota: 5/5.** Coherencia mantenida a través de cuatro turnos, calidad constante, caída marginal de la velocidad dentro de lo normal.

### Test 9 — Generación de vídeo: todavía no *(no evaluado)*

Como en las entregas anteriores, LM Studio aún no soporta el input de vídeo. Los motivos ya están explicados en el [artículo sobre Qwen3.6](https://aitalk.it/it/qwen36-35b-ai.html), donde también documenté los intentos con formatos alternativos. La cuestión permanece abierta y merece un análisis dedicado, probablemente con llama.cpp o vLLM.

## Configuración mínima: cuántos recursos se necesitan realmente

Uno de los aspectos más interesantes surgidos de este test es que Gemma 4 12B en Q8_0 no requiere una workstation extraordinaria. Sobre la base de mi experiencia directa, aquí están los requisitos mínimos para hacerlo funcionar de forma aceptable, es decir, con una velocidad en torno a los 15-17 tokens por segundo y sin swap continuo en la RAM:
![tabella2.jpg](tabella2.jpg)

La comparación con los modelos anteriores de la serie cuenta una historia precisa:
![tabella3.jpg](tabella3.jpg)

La conclusión práctica es esta: si tenéis una GPU con 12-14 GB de VRAM, podéis ejecutar Gemma 4 12B Q8_0 en full GPU con un rendimiento excelente. Si tenéis menos VRAM, podéis bajar a Q6 o Q4 y obtener de todos modos resultados dignos. Con los modelos más grandes, incluso con cuantizaciones agresivas, ya estabais en el límite o más allá.
![tabella4.jpg](tabella4.jpg)

## La respuesta a la pregunta

La media aritmética de los ocho tests realizados es 4,97 sobre 5. Un número alto, pero no es el número el punto más interesante de este experimento.

El punto interesante es la configuración con la que se ha alcanzado. Por primera vez en esta serie de tests, he ejecutado un modelo completamente en GPU, 48 capas de 48, sin estrangulamientos de ningún tipo. La velocidad media de unos 17 tokens por segundo ha sido constante y fluida, un punto medio entre los modelos probados más que aceptable y que no lleva al límite una máquina de este tipo, garantizando una estabilidad en las respuestas y reduciendo el riesgo de crashes imprevistos. Y esta diferencia, en la práctica diaria, cambia la naturaleza de la interacción.

Hay una escena en *Ping Pong the Animation*, la adaptación del manga homónimo de Taiyo Matsumoto, en la que el personaje más dotado técnicamente pierde contra un adversario que debería ser inferior, simplemente porque este último juega sin ningún peso en la espalda, sin miedo, al máximo de lo que puede hacer. No es una cuestión de talento absoluto: es una cuestión de margen libre entre potencial y ejecución. Gemma 4 12B en esta configuración me ha dado la misma sensación: un modelo que juega su partida completa, sin nada retenido.

La pregunta que motivó este experimento era: "¿Un modelo más pequeño usado al máximo puede vencer a uno más grande pero estrangulado?" La respuesta que me llevo a casa es sí, para la mayoría de los usos diarios. El 12B en Q8_0, con full GPU offload, produce respuestas de calidad excelente, es rápido, tiene una latencia más previsible gracias a la arquitectura densa, sin los picos variables típicos de los modelos MoE, y requiere menos memoria. El 26B MoE en Q4_K_M con offload parcial sigue siendo un gran modelo, pero pierde en fluidez y reactividad en hardware consumer estándar.

Está luego la cuestión de la arquitectura multimodal. El 12B, con su enfoque unificado que elimina los encoders separados, promete una comprensión más integrada de texto e imágenes. No he podido testar la parte de vídeo por los límites de LM Studio, pero lo que he visto en el test de las tablas corporativas, donde el modelo no se limitó a leer los datos sino que los interpretó en su contexto, sugiere que la elección de diseño no es solo teóricamente elegante. Funciona.

La verdadera noticia, para quien lee, es esta: hoy existe un modelo de altísima calidad que se ejecuta enteramente en vuestra GPU consumer, sin compromisos. Ya no tenéis que elegir entre "modelo grande pero estrangulado" y "modelo pequeño pero insuficiente". Gemma 4 12B es el punto de equilibrio que muchos estaban esperando. Y el hecho de que sea también arquitecturalmente más avanzado que su predecesor en la gestión multimodal es la guinda de un pastel que, esta vez, se ha horneado bien.

---

*Todos los artículos de la serie: [Qwen 3.5 en mi PC](https://aitalk.it/it/qwen3.5-locale-puntata1) — [Gemma 4 26B en local](https://aitalk.it/it/gemma4-26b.html) — [Qwen3.6 35B en local](https://aitalk.it/it/qwen36-35b-ai.html)*
