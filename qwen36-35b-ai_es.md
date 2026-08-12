---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-05-20
author: "Dario Ferrero"
---

# Qwen 3.6 en local: 35 mil millones en mi PC
![qwen36-35b-ai.jpg](qwen36-35b-ai.jpg)

*Hay un momento, en cada serie de experimentos, en el que te das cuenta de que el problema ya no es el sujeto de la prueba, sino la calidad de tu instrumento de medida. Estaba recogiendo las notas de la octava prueba y pensaba que tal vez el límite se han convertido mis pruebas: cinco sobre cinco, ocho veces de ocho. ¿El termómetro sigue funcionando, o el agua ha dejado de variar de temperatura?*

La pregunta no es retórica. Estos artículos nacen como diario de a bordo de un laboratorio doméstico, no como un white paper académico, y el método sigue siendo deliberadamente personal: nada de benchmarks automatizados, ninguna métrica estandarizada, solo prompts calibrados en escenarios realistas y la sensación táctil de quien usa la herramienta y luego la cuenta. El hardware no ha cambiado respecto a las entregas anteriores, AMD Ryzen 7700, 32 GB de RAM, GPU AMD con 16 GB de VRAM, y tampoco el software: [LM Studio](https://lmstudio.ai/), la solución más accesible para quienes queráis ejecutar modelos locales sin perder una tarde en configuraciones de terminal. Para todos los detalles sobre la instalación, sobre el ecosistema y sobre la filosofía de este laboratorio, remito a la [primera entrega de la serie sobre Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1.html), que sigue siendo la referencia metodológica de toda la serie. Quienes ya estéis a bordo podéis continuar desde aquí.

Hoy el protagonista es diferente de los demás. No por categoría, sino por tamaño: [Qwen3.6 35B A3B en cuantización Q6](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), el modelo más grande que jamás haya cargado en esta máquina, literalmente al límite de lo que la configuración puede soportar. Después de haber explorado [Qwen 3.5 9B en las dos primeras entregas](https://aitalk.it/it/qwen3.5-locale-puntata2.html) y [Gemma 4 26B MoE](https://aitalk.it/it/gemma4-26b.html) en la tercera, este salto de escala era inevitable. Y es exactamente el salto que quería dar.

## Treinta y cinco mil millones, de tres en tres

El nombre esconde una arquitectura que vale la pena entender, porque cambia radicalmente la forma en que se razona sobre los requisitos de hardware. Qwen3.6 35B A3B es un modelo Mixture of Experts: tiene 35 mil millones de parámetros totales, pero por cada token generado solo activa unos 3 mil millones. No todos los expertos son llamados a responder cada vez, solo aquellos considerados más competentes para ese fragmento específico de texto. Es un poco como tener una orquesta de doscientos cincuenta y seis músicos, donde el director elige en cada ocasión qué ocho instrumentistas hacer sonar, dejando a los demás escuchando y listos. El resultado práctico es que el coste computacional se parece más al de un modelo de tres mil millones que al de uno de treinta y cinco mil millones, aunque aprovechando la profundidad de este último cuando es necesario.

Qwen3.6, descrito en el [blog oficial de Alibaba](https://qwen.ai/blog?id=qwen3.6) como una evolución de la arquitectura Qwen3, trae consigo cuatro novedades que el equipo ha querido destacar: una mejora del 43% en QwenWebBench en las capacidades de generación de código agéntico y de aplicaciones web completas, una funcionalidad llamada *thinking preservation* para mantener la coherencia del razonamiento a través de conversaciones de varios turnos, un salto en la comprensión multimodal con imágenes y documentos, y el soporte nativo a la comprensión de vídeo, esta última todavía experimental y no soportada por todos los entornos de ejecución disponibles.

La cuantización Q6 sobre la que he trabajado representa un compromiso razonado: menos pesada que la F16 pura, mucho más fiel al modelo original en comparación con las cuantizaciones agresivas como la Q4. En la práctica se pierde muy poca calidad respecto a los pesos enteros, pagando un coste en memoria que, en mi configuración, ha requerido un equilibrio cuidadoso entre GPU y RAM del sistema.

## La configuración al límite

Aquí reside el experimento real. No he buscado el punto de máximo rendimiento: he buscado deliberadamente el borde de lo posible, es decir, entender qué sucede cuando se trabaja con el mínimo aceptable de rendimiento, al menos según mi opinión.

Los parámetros elegidos: contexto de 8078 tókenes (el modelo supera de forma nativa los 262.000), descarga (offload) a GPU de 8 capas de un total de 43, 8 expertos activos de 256 disponibles, cuantización F16 internamente para las capas en GPU. La velocidad resultante se estabilizó en torno a los 11 tókenes por segundo, frente a los 20-25 que Qwen 3.5 9B alcanzaba cómodamente. No es una velocidad que recomendaría para un asistente conversacional para usar sobre la marcha, pero es totalmente aceptable para sesiones de trabajo estructuradas en las que no se tenga prisa y se priorice la profundidad de la respuesta.

La pregunta que subyace a todo el experimento es sencilla: ¿el sacrificio de velocidad vale la calidad ganada? Las pruebas que siguen son la respuesta.

## Un paso más allá: la configuración óptima

La elección de partir de 8 capas en GPU y contexto reducido fue deliberada: quería probar el modelo en condiciones de escasez real de recursos, el punto más bajo del rango aceptable. Pero una vez completada la batería de pruebas, quise entender dónde se encuentra el verdadero punto de equilibrio en este hardware.

Los resultados han sido instructivos. Llevar las capas en GPU de 8 a 16 hace subir la velocidad de 11 a unos 14,5 tókenes por segundo, una ganancia sensible. Sorprendentemente, duplicarlas de nuevo a 32 no cambia casi nada (14,49 tok/s), e intentar la carga a 40 capas impide que el modelo arranque por completo: la VRAM no aguanta. El punto óptimo para este hardware es, por tanto, 16 capas, no más.

Igualmente interesante es el comportamiento del contexto: ampliarlo desde 8.000 tókenes hasta el máximo nativo de 262.000 incide poquísimo en la velocidad, con una caída de menos de un token por segundo entre los dos extremos. En la práctica, podéis elegir la ventana de contexto según la tarea sin preocuparos por el rendimiento.

El parámetro que en cambio marca realmente la diferencia es el número de expertos activos. Con 4 expertos se sube a 16,2 tok/s, con 8 se está en 14,2, con 16 se baja a 11,4, con 125 se cae a 2,9. Es una relación casi lineal hacia abajo: cada experto adicional cuesta, y en hardware de consumo el coste se nota de inmediato.

Todas las pruebas con configuraciones diferentes produjeron, en cualquier caso, respuestas de calidad excelente, lo que sugiere que reducir los expertos activos no compromete la calidad de forma perceptible, al menos en las tareas usadas en esta serie.

La configuración de mejor compromiso en este hardware resulta ser, por tanto: 16 capas en GPU, contexto de 125.000 tókenes, 8 expertos activos, con una velocidad de unos 14,2 tókenes por segundo. No es la velocidad de un modelo pequeño, pero es un paso adelante respecto a la configuración "al límite" usada en las pruebas principales, y abre la puerta a sesiones de trabajo sobre documentos largos sin tener que renunciar a la calidad.
![grafico1.jpg](grafico1.jpg)
[Imagen de los resultados de los benchmarks tomada de qwen.ai](https://qwen.ai/blog?id=qwen3.6)

## Las pruebas

### Prueba 1 — Mecanismo de Higgs y física de partículas *(5/5)*

*Parámetros: contexto 8078 tókenes, offload GPU 8 capas de 43, 8 expertos activos de 256, F16, 11,17 tókenes/s*

La respuesta fue excepcional, probablemente la mejor que jamás haya obtenido de un modelo local sobre un tema científico complejo. El modelo comenzó con el contexto teórico, describiendo la simetría de gauge que gobierna las interacciones electrodébiles. Luego introdujo el campo de Higgs y su célebre potencial de "sombrero mexicano", explicando por qué el cero no es el mínimo energético. Mostró cómo el valor de expectativa del vacío interactúa con los bosones de gauge, confiriendo masa a los W y los Z. Y aclaró el detalle más sutil, ese que a menudo falta incluso en los tratados universitarios: por qué el fotón permanece sin masa, gracias a una simetría residual que el vacío del Higgs no logra romper.

La estructura de la respuesta era impecable, organizada en secciones lógicas que procedían de lo general a lo particular sin perder nunca el hilo. El lenguaje era preciso pero accesible, usando metáforas como la del "sombrero mexicano" para hacer intuitivos conceptos abstractos. No encontré errores ni en los conceptos físicos ni en los detalles matemáticos. La velocidad de 11 tókenes por segundo es más baja respecto a los modelos más pequeños probados anteriormente, pero la calidad de esta respuesta compensa con creces el compromiso. La paciencia de esperar unos segundos más se vio recompensada por una explicación que podría definirse como de manual.

### Prueba 2 — Multimodalidad y comprensión de tablas *(5/5)*

*Parámetros: contexto 8078 tókenes, offload GPU 8 capas de 43, 8 expertos activos de 256, F16, 10,49 tókenes/s*

La imagen cargada era deliberadamente de baja calidad: una pequeña captura de pantalla de una interfaz de gestión de facturas, imperfecta para poner a prueba las capacidades visuales en condiciones realistas, no ideales. El modelo superó la prueba con resultados sorprendentes.

Lo primero que llamó la atención fue la capacidad de comprender la estructura general de la interfaz. El modelo identificó correctamente las tres secciones principales: el panel de filtros arriba, la lista lateral de productos a la derecha y la tabla central. Reconoció que se trataba probablemente de una aplicación de gestión contable, hipotetizando incluso que pudiera ser una base de datos de ejemplo o un entorno de prueba, dada la genericidad de los nombres de los clientes y de los artículos.

La lectura de los datos fue precisa y detallada: todas las columnas de la tabla enumeradas correctamente, el tipo de IVA fijo al 22% detectado como constante en todas las filas, la columna "Importe" resaltada en amarillo señalada como elemento de navegación para el usuario, las fechas de las facturas identificadas en el periodo enero-marzo de 2022. Pero la parte más valiosa fue el análisis de las anomalías: a pesar de que el filtro superior mostraba la opción "POR PAGAR" como seleccionada, las facturas en la tabla ya tenían una fecha de pago y un importe liquidado. El modelo señaló la posible mezcla de datos, formulando hipótesis sensatas sobre el contexto de uso. Un modelo más pequeño habría producido una descripción genérica. Aquí obtuve un análisis real, con interpretación de las incongruencias incluida.

### Prueba 3 — Generación de código complejo *(5/5)*

*Parámetros: contexto 8078 tókenes, offload GPU 8 capas de 43, 8 expertos activos de 256, F16, 10,06 tókenes/s*

Esta prueba era una de las más importantes de toda la batería, porque Qwen3.6 promete una mejora del 43% en QwenWebBench precisamente en la generación de código. Quería ver si la promesa se traducía en una implementación concreta y funcional sobre un problema algorítmico no trivial: encontrar el ciclo de longitud máxima en un grafo no dirigido.

La respuesta convenció plenamente. El modelo comenzó con una premisa teórica que pocos asistentes de programación tienen la madurez de incluir: declaró explícitamente que el problema es NP-difícil, que no existe un algoritmo polinómico para resolverlo en grafos genéricos, y que cualquier solución exacta tendrá una complejidad exponencial en el peor de los casos. Esta conciencia es rara y valiosa, porque demuestra que el modelo no está intentando vender una solución mágica, sino que comprende profundamente los límites del dominio.

La implementación propuesta era elegante y funcional: estrategia DFS con rastreo del camino, estructura de datos con mapa de profundidad (depth map) para detectar las aristas de retroceso (back-edges) y calcular la longitud de los ciclos en tiempo constante, representación del grafo mediante una lista de adyacencia eficiente, backtracking implementado correctamente y gestión completa de los casos límite como grafos sin ciclos y componentes desconectados. Aprecié particularmente el uso del mapa de profundidad, más elegante y con mejor rendimiento que una simple búsqueda lineal en el camino porque permite calcular la longitud del ciclo sin escanear toda la lista. La explicación de la complejidad temporal fue clara y honesta, con distinción entre el caso favorable y el peor caso. Sin errores sintácticos ni lógicos, presencia de type hints y estructura modular. Un código que se podría entregar.

### Prueba 4 — Multilingüe y planificación *(5/5)*

*Parámetros: contexto 8078 tókenes, offload GPU 8 capas de 43, 8 expertos activos de 256, F16, 11,15 tókenes/s*

*Nota metodológica: ejecutada en un chat limpio después de que una primera ejecución en un chat con historial produjera resultados mediocres.*

Esta prueba enseñó algo importante incluso antes del resultado. La primera ejecución, en un chat con iteraciones previas sobre otros temas, había producido interrupciones y una calidad mediocre. Repetida en un chat completamente nuevo, el resultado se transformó. La diferencia fue tan clara que merece una nota metodológica permanente: el historial del chat, incluso cuando parece inocuo, puede alterar significativamente los resultados en tareas complejas. Probar en un chat limpio no es un capricho, es higiene experimental.

En un chat limpio, Qwen3.6 produjo un itinerario de cinco días en Tokio en francés, completo y articulado, al primer intento. El francés era de nivel nativo: "spécialités de rue", "ambiance vieux Tokyo", "cadre apaisant", "ruelle atmosphérique", "patrimoine UNESCO". Sin errores gramaticales ni sintácticos, fluidez de nivel avanzado.

El itinerario era logísticamente perfecto, con días equilibrados entre templos y comida callejera, y lleno de consejos de viajero experto: llegar a Fushimi Inari antes de las ocho para evitar la multitud, imprimir los nombres de los templos en japonés, usar los modelos de comida en los restaurantes para pedir sin hablar el idioma. La sección de transporte explicaba cómo activar Suica o Pasmo en el smartphone, cómo reservar el Shinkansen, y que las oficinas de información en las estaciones principales tienen personal francófono en algunos horarios. Sugirió el Kyoto City Bus Day Pass y aconsejó descargar los mapas offline. Para la barrera lingüística propuso no solo Google Translate sino también Papago para el reconocimiento de voz, y frases clave en japonés transliterado.

La sección final solicitada en italiano, para probar el multilingüismo dentro de un mismo prompt, era limpia, correcta y rica en consejos prácticos sobre los pagos en efectivo, los cajeros automáticos Seven-Eleven y las tarjetas de traducción para las alergias alimentarias.

### Prueba 5 — Contexto larguísimo: documento de 460 páginas *(5/5)*

*Parámetros: contexto 8078 tókenes, offload GPU 8 capas de 43, 8 expertos activos de 256, F16, 10,93 tókenes/s*

Esta fue la prueba más sorprendente de toda la batería, y merece ser contada con la debida atención. Cargué el *AI Index Report 2025*, un PDF de unas 460 páginas y más de 20 millones de caracteres, pidiendo al modelo que describiera el crecimiento de la generación de vídeo e indicara las páginas donde encontrar los datos. El desafío era deliberadamente extremo: contexto de solo 8078 tókenes, muy lejos de los 262.000 nativos del modelo, solo ocho expertos activos, solo ocho capas en GPU.

La respuesta me dejó sin palabras. A pesar de los parámetros reducidos al mínimo, el modelo proporcionó un resumen preciso y bien estructurado de los avances en la generación de vídeo entre 2023 y 2025. Citó correctamente los modelos principales: Meta Movie Gen, Google Veo y Veo 2, Runway Gen-3 Alpha, Luma Dream Machine, Kling 1.5. Mencionó el famoso ejemplo del prompt "Will Smith eating spaghetti" como marcador del salto cualitativo ocurrido en el sector. Indicó figuras específicas en el informe, como la Figura 2.3.11 y la Figura 2.3.12. Y declaró que los datos principales se encontraban en las páginas 126 y 127 del informe. Lo verifiqué. Era exacto.

Cómo logró encontrar la información correcta en un documento de 460 páginas con una ventana de contexto correspondiente a pocas decenas de páginas sigue siendo el misterio más fascinante de toda la sesión. Probablemente el modelo supo identificar y conservar las secciones más relevantes a pesar de las limitaciones de memoria, pero el mecanismo exacto no es transparente desde el exterior. Lo que sí es transparente es el resultado: con una configuración reducida al mínimo, en un documento enorme, referencias verificables a las páginas correctas. Esto es robustez.

### Prueba 6 — Razonamiento espacial *(5/5)*

*Parámetros: contexto 8078 tókenes, offload GPU 8 capas de 43, 8 expertos activos de 256, F16, 11,42 tókenes/s*

La prueba pedía analizar la fotografía de una habitación desordenada y proponer un plan de orden. A pesar de los parámetros conservadores, solo ocho expertos, solo ocho capas en GPU, el modelo produjo un análisis visuoespacial de altísimo nivel.

La descripción fue fiel y detallada: cama con estructura de metal negro, dos estanterías de escalera blancas posicionadas correctamente, escritorio gris abarrotado, pequeño armario blanco, espejo en la puerta. Colores de las paredes identificados como verde salvia claro, suelo con moqueta estampada, cortinas a rayas verdes y blancas. Incluso la cesta de la ropa azul en el centro del suelo, rodeada de ropa esparcida, zapatos, cajas, tijeras y otros objetos, había sido detectada y catalogada.

El plan de orden estaba estructurado por prioridades visuales con motivaciones sólidas. Primero la ropa del suelo y de la cama, porque quitarla libera el camino de movimiento y reduce el ruido visual, haciendo que la habitación parezca más grande. Luego la cama, porque una cama deshecha ocupa visualmente más espacio y crea sensación de caos, mientras que estirarla define los límites de la habitación. Después la cesta de la ropa y los zapatos, obstáculos físicos que bloquean el "pasillo" central. Finalmente el escritorio, cuya superficie libre proyecta orden y funcionalidad. La síntesis final fue perfecta: "El objetivo inicial no es lo minucioso, sino el volumen". Una frase que resume la esencia de la organización eficaz en un entorno muy desordenado, y que un profesional del sector no habría sabido decir mejor.

### Prueba 7 — Agente multietapa: planificación de proyecto de software *(5/5)*

*Parámetros: contexto 8078 tókenes, offload GPU 8 capas de 43, 8 expertos activos de 256, F16, 11,04 tókenes/s*

Esta prueba se introdujo específicamente para verificar la promesa de mejora del 43% en QwenWebBench. Un modelo que destaca en física y razonamiento espacial podría, aun así, fallar en una tarea de planificación articulada. La verdadera madurez de un asistente de programación se ve en la capacidad de organizar el trabajo, anticipar problemas y proporcionar soluciones prácticas, no solo escribir código. La tarea era planificar el desarrollo de una web app para la gestión de los gastos familiares, con un equipo de dos desarrolladores y una hoja de ruta detallada.

La respuesta fue probablemente la más completa de toda la batería. El stack tecnológico propuesto era moderno y coherente, con cada elección motivada en una tabla clara: React con TypeScript y Vite para el frontend, Node.js con Express para el backend, PostgreSQL con Prisma como ORM, JWT para la autenticación, papaparse para el parsing CSV, React-PDF para la exportación, BullMQ para las colas de notificaciones, Docker para la infraestructura. La estructura del proyecto estaba detallada por carpetas lógicas tanto en el lado frontend como en el backend, con un docker-compose.yml para orquestar Postgres, Redis y la aplicación. Esta es la estructura que usaría un verdadero ingeniero de software.

La planificación en seis sprints semanales era realista y estaba bien equilibrada: configuración y autenticación, transacciones e importación CSV, panel de control y gráficos, exportación PDF, presupuesto y notificaciones por correo electrónico, pruebas y despliegue. Para cada sprint se indicaban el enfoque, los entregables esperados, las posibles criticidades y la división del trabajo entre los dos desarrolladores. La recomendación de definir primero los contratos de la API y luego trabajar en paralelo es una buena práctica que a muchos desarrolladores senior les cuesta seguir sistemáticamente.

Las criticidades se habían identificado con precisión quirúrgica: formatos CSV heterogéneos y gestión de errores parciales en la importación, entregabilidad y husos horarios para las notificaciones por correo electrónico, cobertura de pruebas y plan de rollback para el despliegue. La sección de buenas prácticas estaba completa: cookies httpOnly y rate limiting para la seguridad, índices de base de datos y paginación para el rendimiento, mocks de SMTP y base de datos para las pruebas, GitHub Actions para el CI/CD. El modelo incluso sugirió Sentry para el rastreo de errores y Notion para la documentación. El único pequeño apunte es que la respuesta era casi excesivamente detallada para una planificación inicial, pero es el tipo de exceso que se prefiere tener.
![testqwen.jpg](testqwen.jpg)
*Captura de pantalla de mi PC y de LM Studio, durante la prueba de Agente multietapa.*

### Prueba 8 — Thinking preservation: conversación de cuatro turnos *(5/5)*

*Parámetros: contexto 8078 tókenes, offload GPU 8 capas de 43, 8 expertos activos de 256, F16, poco más de 11 tókenes/s por turno*

Esta prueba se introdujo para evaluar una de las novedades más interesantes de Qwen3.6: la capacidad de mantener la coherencia del razonamiento a través de conversaciones de varios turnos, preservando no solo el historial del chat sino también la lógica de las decisiones tomadas en las fases anteriores. Para el desarrollo iterativo esta es una cualidad fundamental, porque permite construir proyectos complejos sin tener que repetir continuamente las premisas.

La conversación se articuló en cuatro turnos. En el primero pedí un stack tecnológico para una aplicación de gestión de tareas: la respuesta fue detallada con tabla comparativa, React con TypeScript, Node.js con Express, PostgreSQL con Prisma, JWT, SendGrid con BullMQ, cada elección motivada con argumentos sólidos. En el segundo turno pedí una opinión sobre la elección entre WebSocket y polling para las notificaciones en tiempo real con 1000 usuarios activos: el modelo explicó por qué WebSocket es superior en latencia y sobrecarga, mostró una arquitectura con PostgreSQL LISTEN/NOTIFY y Redis Pub/Sub, y anticipó el caso límite de redes que bloquean WebSocket explicando que Socket.IO gestiona la caída (fallback) automáticamente. En el tercer turno pedí el esquema de la base de datos en Prisma: el esquema producido estaba completo, con ocho modelos principales, enums para estado, prioridad y rol, relaciones bien definidas, UUID para las claves primarias, índices estratégicos para las consultas frecuentes y cascadas controladas. Incluyó un ejemplo de consulta que evitaba el problema N+1.

El cuarto turno era la prueba real: pedí un resumen de las elecciones tecnológicas tomadas hasta ahora y la explicación de por qué habíamos elegido WebSocket en lugar de polling. El modelo recordó correctamente todo el primer turno, resumió las motivaciones para WebSocket con la misma terminología y las mismas razones del segundo turno, y añadió espontáneamente una sección sobre la escalabilidad a 10.000 usuarios con estrategias para backend, base de datos, almacenamiento en caché, colas de correo electrónico, observabilidad y despliegue, además de una lista de verificación operativa. No recibió ningún recordatorio: simplemente recordó. Ninguna contradicción, ningún olvido, razonamiento extendido de forma coherente. La promesa de *thinking preservation* no era marketing.

## El vídeo que espera

Qwen3.6 promete comprensión de vídeo nativa, una novedad absoluta respecto a las versiones anteriores. Intenté probarlo cargando un archivo MP4 en LM Studio. El sistema respondió con un signo de exclamación sobre el adjunto y el modelo declaró no haber recibido ningún archivo. El límite no es del modelo, sino de la herramienta elegida para ejecutarlo: LM Studio gestiona excelentemente imágenes, PDF, documentos de texto y CSV, pero los vídeos no entran todavía entre los formatos soportados. Me reservo volver sobre esta prueba tan pronto como sea posible, probablemente con llama.cpp o vLLM, que podrían ofrecer un soporte más completo para los contenidos de vídeo. Si se mantienen las premisas, será una entrega que merecerá un espacio dedicado.
![tabella-confronto-modelli.jpg](tabella-confronto-modelli.jpg)
*La tabla "comparativa" con las pruebas sobre modelos anteriores. Con doble configuración probada para Qwen 3.6*

## ¿Vale la pena forzar hasta el límite?

Esta es la pregunta que subyace a toda la serie, y que con Qwen3.6 se vuelve imposible de eludir. Con Qwen 3.5 9B se iba a 20-25 tókenes por segundo en una configuración relajada. Con Gemma 4 26B MoE los márgenes ya se habían estrechado. Con este modelo se está a 11 tókenes (unos 14/15 en la optimización máxima en mi hardware) por segundo, con la GPU ocupada en una fracción del total y la carga distribuida entre VRAM y RAM del sistema en un equilibrio precario. Las notas máximas en secuencia han planteado una pregunta legítima sobre la severidad de mis pruebas, y esa pregunta sigue abierta: probablemente se necesiten instrumentos de evaluación más afilados en las entregas sucesivas.

Pero mientras tanto hay un dato concreto sobre el que razonar. La respuesta a la pregunta sobre la velocidad depende enteramente del uso que se haga del modelo. Si se busca un asistente conversacional para sesiones rápidas, 11 tókenes (unos 14/15 en la optimización máxima en mi hardware) por segundo empiezan a notarse. Si se trabaja en tareas estructuradas, análisis profundos, generación de código complejo o documentos largos, la calidad que este modelo ofrece en configuración reducida es simplemente inalcanzable para los modelos más pequeños, incluso forzados al máximo. El experimento con el documento de 460 páginas lo demostró de la forma más plástica posible: una ventana de contexto minúscula, una máquina al límite, y el modelo encontrando las páginas exactas en un volumen de biblioteca.

Hay, sin embargo, un subtexto más amplio que esta serie de experimentos está sacando progresivamente a la superficie. Cuando un modelo de 35 mil millones de parámetros funciona en local en hardware de consumo con resultados comparables a los servicios en la nube de hace dos años, algo en la topología del mercado de la IA está cambiando. La nube sigue siendo imbatible por velocidad, por los modelos de frontera y por la escalabilidad. Pero para quienes trabajéis con datos sensibles, para quienes queráis un control completo sobre la inferencia, para quienes no queráis depender de un endpoint de API con sus latencias y sus costes variables, el local se está convirtiendo en una elección madura, ya no solo un experimento para entusiastas. La distancia entre las dos opciones se acorta con cada generación de modelos, y Qwen3.6, incluso en esta configuración intencionadamente penalizada, es la prueba más convincente que he tenido hasta ahora.

Las notas máximas son un problema. Pero es el tipo de problema que da mucho menos miedo que lo contrario.
