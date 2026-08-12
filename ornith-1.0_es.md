---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-07-10
author: "Dario Ferrero"
---

# Ornith-1.0 35B en local: el desconocido que bate a todos
![ornith-1.0-test-personale.jpg](ornith-1.0-test-personale.jpg)

*Hay un momento, en cada sesión con un nuevo modelo descargado en local, en el que comprendéis si tenéis delante un juguete o una herramienta de trabajo. Con Ornith-1.0-35B ese momento llegó en el segundo prompt, cuando subí la foto borrosa de una hoja de Excel corporativa esperando la habitual respuesta vaga, y me encontré con un verdadero análisis de balance, completo con señales de alarma sobre la liquidez. A partir de ahí, la sesión de prueba tomó un rumbo diferente al habitual.*

También esta vez el descargo de responsabilidad sigue siendo el mismo de siempre: no es un benchmark científico, no hay metodologías validadas ni controles cruzados dignos de un laboratorio, es simplemente el relato de lo que sucede cuando un modelo de código abierto acaba en el PC de mi casa y es puesto a prueba con las mismísimas tareas reservadas a los otros competidores que han pasado por esta serie. Si no habéis leído las entregas anteriores, sobre el [hardware utilizado y la configuración de LM Studio](https://aitalk.it/it/qwen3.5-locale-puntata1.html) ya encontráis todos los detalles técnicos; aquí me limito a recordar las cifras esenciales: un Ryzen 7700, 32 GB de RAM DDR5 y una Radeon RX 9060 XT con 16 GB de VRAM, la misma combinación con la que ya he puesto a prueba a Qwen 3.5, Qwen 3.6 y la familia Gemma 4. En el portal encontráis también las otras entregas de la serie, con modelos diferentes y resultados igualmente sorprendentes.

## Quién es Ornith-1.0

El nombre viene del griego antiguo para "pájaro", y DeepReinforce lo explica con una imagen que se deja recordar: como un volátil que construye por sí mismo su propio nido, el modelo aprende a construir por sí mismo el andamiaje con el que afronta los problemas de programación, incluso antes de resolverlos. No es marketing vacío; es la síntesis de un enfoque de entrenamiento realmente diferente al estándar.

La familia comprende cuatro tamaños, desde el 9B denso hasta el mastodóntico 397B, pasando por un 31B denso y por el 35B de expertos mixtos que he elegido para mis pruebas, disponible con licencia MIT en [GitHub](https://github.com/deepreinforce-ai/Ornith-1) y descrito en detalle en el [post de lanzamiento oficial](https://deep-reinforce.com/ornith_1_0.html). Aquí vale la pena dedicar dos líneas a la arquitectura MoE, porque es el verdadero motivo por el que este modelo logra funcionar con dignidad incluso en una tarjeta de vídeo de 16 GB: de los 35 mil millones de parámetros totales, solo unos 3 mil millones se activan por cada token generado, un poco como si en una redacción enorme, en lugar de hacer trabajar a todo el equipo en cada artículo, se llamara solo al puñado de especialistas realmente competentes en el tema del momento. En el caso de Ornith-1.0-35B se trata de 256 expertos totales, de los cuales 8 se activan por rotación más uno siempre presente, y la elección se nota totalmente en la velocidad de generación, que en mis pruebas se ha mantenido estable entre los 16 y 17 tokens por segundo, un ritmo de lectura más que razonable para un uso interactivo diario.

El otro elemento distintivo se refiere al método de entrenamiento. Ornith-1.0 nace de un framework de reinforcement learning que no optimiza solo la solución final a un problema de código, sino también el scaffold, es decir, el plan de acción, las llamadas a herramientas, la lógica con la que el modelo decide cuándo reintentar o cuándo cambiar de enfoque. Es una diferencia sutil pero importante respecto al fine-tuning tradicional, un poco como enseñar a alguien no solo a resolver un crucigrama, sino también a construirse por sí mismo el esquema con el que afrontarlo. En los benchmarks declarados, esta elección se traduce en puntuaciones notables en Terminal-Bench 2.1, donde el 35B alcanza la cuota de 64,2, y en SWE-bench Verified, en 75,6, resultados que superan a modelos más famosos como Qwen 3.5 y Qwen 3.6 en sus respectivas categorías de peso.
![grafico1.jpg](grafico1.jpg)
[imagen tomada de deep-reinforce.com](https://deep-reinforce.com/ornith_1_0.html)

## Un ojo de más, no declarado

Hay un detalle que vale la pena contar por extenso, porque describe bien cómo funciona realmente el ecosistema de código abierto cuando goza de buena salud. En la página oficial de DeepReinforce y en el model card original no se hace mención de capacidades multimodales: Ornith-1.0 se presenta exclusivamente como modelo textual para coding agéntico, aunque dotado de soporte nativo para llamadas a herramientas al estilo OpenAI. Sin embargo, buscando entre las conversiones GGUF disponibles en Hugging Face, se encuentra un archivo separado subido por [bartowski](https://huggingface.co/bartowski/deepreinforce-ai_Ornith-1.0-35B-GGUF/blob/main/mmproj-deepreinforce-ai_Ornith-1.0-35B-bf16.gguf), uno de los cuantizadores más prolíficos y fiables de la comunidad, etiquetado como mmproj: se trata del proyector visual que, copiado en la misma carpeta del modelo principal, desbloquea en LM Studio la lectura de imágenes.

Lo probé por curiosidad, esperando un error o en el mejor de los casos un soporte cojo, y en cambio funcionó sin contratiempos, abriendo el camino a las dos pruebas multimodales de esta entrega. Es un pequeño ejemplo de cómo, en el mundo de los modelos abiertos, las funcionalidades reales terminan siendo más amplias que las declaradas en la ficha técnica oficial, gracias al trabajo sumergido de quienes desmontan, convierten y recomponen los pesos para hacerlos funcionar en cualquier lugar. También sirve como recordatorio para quienes se fían solo de la documentación oficial para evaluar las capacidades de un modelo: el riesgo de subestimar su potencial real es concreto.

## El banco de pruebas

La configuración usada en LM Studio calca la ya rodada en las entregas anteriores, con algunas adaptaciones debidas al tamaño del modelo. He trabajado con la cuantización Q6_K, un compromiso que mantiene la calidad de las respuestas muy cerca de la original sacrificando un poco de espacio en disco, con un contexto establecido en 25.042 tokens, offload GPU en 20 de las 32 capas totales, pool de 8 hilos de CPU, batch de evaluación a 2048 y batch size a 512, con un máximo de 4 predicciones concurrentes y 8 expertos activos por token, en línea con la configuración por defecto indicada por DeepReinforce.

Las ocho pruebas cubren el mismo terreno explorado en entregas anteriores de la serie, desde el razonamiento científico puro hasta el aguante de la memoria conversacional en varios turnos, pasando por la multimodalidad, la generación de código, la planificación multilingüe, la gestión de documentos larguísimos, el razonamiento espacial y las capacidades agénticas multi-paso.

## Ocho desafíos, un veredicto

### Prueba 1 — Razonamiento científico: el mecanismo de Higgs *(5/5)*

El primer banco de pruebas era de los que ponen en dificultades incluso a los modelos de renombre: explicar el mecanismo de ruptura de la simetría electrodébil, el papel del campo de Higgs, el motivo por el cual los bosones W y Z adquieren masa mientras el fotón permanece sin masa. Ornith respondió con una estructura en cinco bloques lógicos, desde el planteamiento del problema hasta una mención final al bosón físico, con fórmulas correctas e interpretaciones físicas puntuales, en un registro que definiría como el de un manual universitario bien escrito, ni demasiado técnico ni aguado.

### Prueba 2 — Multimodalidad: leer una hoja de cálculo corporativa *(5/5)*

La segunda prueba, la de la tabla Excel borrosa contada al principio, confirmó lo intuido a primera vista: lectura correcta de los datos a pesar de la escasa calidad de la imagen, identificación de las relaciones entre columnas, un análisis de business intelligence que notó el redimensionamiento progresivo de la empresa, el fuerte desapalancamiento, el capital neto triplicado y sobre todo el empeoramiento de la liquidez, con un comentario pertinente también sobre el significado de un valor negativo en las pasividades consolidadas.
![screenshot1.jpg](screenshot1.jpg)
*Captura de pantalla durante la prueba sobre la imagen de la hoja de Excel*

### Prueba 3 — Generación de código: un problema NP-hard *(5/5)*

En el frente de la generación de código, la tarea era implementar en Python un algoritmo para el ciclo máximo en un grafo no dirigido, un problema NP-hard que se reduce al ciclo hamiltoniano. Ornith lo reconoció enseguida, abriendo con la nota teórica correcta incluso antes de escribir una línea de código, para luego proporcionar una implementación con backtracking y un podado inteligente para evitar duplicados, documentada y correcta, acompañada de un análisis de la complejidad en el peor de los casos y de una tabla de estrategias alternativas para diferentes escenarios. La sensación aquí es la de hablar con alguien que realmente ha estudiado informática teórica, no solo memorizado patrones de código recurrentes.

### Prueba 4 — Multilingüe y planificación: cinco días en Japón *(5/5)*

La cuarta prueba desplazó el listón al multilingüismo, pidiendo la planificación de un viaje de cinco días a Japón para un cliente francés, con itinerario en francés y una sección final en italiano. El francés producido es fluido y natural, el itinerario equilibra templos históricos y comida callejera con una logística creíble, cita barrios menos transitados como Yanaka u Omoide Yokocho y sugiere llegar a Fushimi Inari antes de las 8:30 para evitar la multitud, un consejo que cualquiera que haya visitado Kioto sabe lo valioso que es. La sección final en italiano es igualmente sólida, con indicaciones prácticas sobre JR Pass, Suica y apps de traducción offline.

### Prueba 5 — Contexto largo: 460 páginas al vuelo *(5/5)*

Con la quinta prueba se pasó a la gestión del contexto largo, cargando el AI Index Report 2025 completo, cuatrocientas sesenta páginas, y pidiendo información sobre la generación de vídeo con la correspondiente indicación de las páginas de referencia. Ornith respondió al primer intento, indicando con precisión las páginas 126 y 127, citando los modelos principales del sector, el ejemplo viral del spaghetti eating test y los benchmarks internos citados en el informe, precisando incluso que la página siguiente desplaza el discurso al reconocimiento de voz. Una precisión quirúrgica.

### Prueba 6 — Razonamiento espacial: la habitación en el caos *(5/5)*

La sexta prueba, la visual habilitada gracias al archivo mmproj encontrado en Hugging Face, pedía describir la foto de una habitación desordenada y proponer una estrategia de reordenación. La descripción cubrió todos los elementos principales, desde el espejo hasta el armario, desde el escritorio abarrotado hasta la cama sin hacer, con una estrategia de intervención sensata: primero el suelo para despejar un camino, luego la cama para definir el espacio, finalmente el escritorio y el cesto, cada paso motivado de forma práctica.

### Prueba 7 — Agente multi-paso: planificar un proyecto de software *(5/5)*

La séptima prueba mide la capacidad de organizar el trabajo, no solo de ejecutarlo. Pedí planificar el desarrollo de una web app para la gestión de los gastos familiares: stack tecnológico, estructura del proyecto, roadmap detallada para un equipo de dos desarrolladores. Ornith propuso un stack coherente basado en Next.js, Node.js, PostgreSQL, Prisma y Redis, una estructura modular organizada por funciones y una roadmap con entregables y puntos críticos para cada sprint, con consejos de desarrollador senior como configurar primero la base de datos y validar los inputs con Zod.

### Prueba 8 — Conversación larga: coherencia en cuatro turnos *(5/5)*

La última prueba verificó la solidez en una conversación larga, articulada en cuatro turnos sobre stack, notificaciones, bases de datos y escalabilidad de la misma aplicación de gestión de tareas. Ornith mantuvo la coherencia durante toda la conversación, recordando las elecciones hechas en los turnos anteriores y construyendo sobre ellas: desde la comparación entre WebSocket y polling para mil usuarios simultáneos, acompañada de ejemplos de código, hasta un esquema Prisma completo con relaciones e índices, para cerrar con una estrategia de escalabilidad a diez mil usuarios que toca el balanceo de carga, adaptadores Redis, réplicas de lectura y caché. Única nota a señalar, previsible con el aumento del contexto, una progresiva y ligera ralentización de los tokens/s en cada iteración.
![tabella1.jpg](tabella1.jpg)

La puntuación final, ocho de ocho, no la había visto todavía en esta serie, y vale la pena subrayarlo: ninguno de los modelos que han pasado hasta ahora por mi banco de pruebas, ni Qwen 3.5 9B, ni Gemma 4 en sus variantes de 12B y 26B, ni el propio Qwen 3.6 35B, había logrado mantener el máximo en los ocho frentes simultáneamente.

## Luces y sombras

Dicho esto, un resultado perfecto en una prueba personal realizada por un solo observador, sin controles cruzados ni muestras estadísticamente relevantes, debe tomarse por lo que es: una indicación fuerte, no una verdad absoluta. Los benchmarks declarados por DeepReinforce deben leerse sabiendo que la empresa tiene obviamente interés en mostrarse bajo la mejor luz frente a Qwen 3.5 y Qwen 3.6, y algunos observadores independientes en la comunidad ya han empezado a pedir mediciones de velocidad independientes en hardware diferente al mío, dado que las cifras de throughput por ahora circulan sobre todo entre quienes ya han descargado el modelo.

Luego está la cuestión de la multimodalidad no declarada, que por un lado es la demostración de cuán vital es el ecosistema en torno a los pesos abiertos, y por otro abre una pregunta incómoda sobre quién asume la responsabilidad cuando una funcionalidad emerge de un archivo subido por un solo usuario de la comunidad y no por el desarrollador original del modelo: si algo sale mal en la interpretación de una imagen, quién responde, la empresa que ha entrenado el modelo o quien ha obtenido el proyector visual. Son preguntas abiertas que la fase actual de los modelos locales trae consigo, y que difícilmente encontrarán una respuesta tajante a corto plazo.

Quienes ganan en este escenario son, sin duda, los desarrolladores independientes y los pequeños estudios que pueden permitirse coding agents de nivel competitivo sin pagar suscripciones mensuales a proveedores de la nube, gracias también a la licencia MIT que no pone restricciones al uso comercial. Quienes arriesgan perder algo a medio plazo son los proveedores de modelos propietarios especializados en coding, que ven reducirse su ventaja competitiva en segmentos cada vez más amplios del mercado, mientras queda por entender cuánto aguanta este tipo de modelos la comparación en tareas más largas y complejas que las que una sola prueba vespertina logra poner en escena, una pregunta que dejo gustosamente abierta para la próxima entrega.

Por ahora, sentado frente a mi PC con el ventilador de la Radeon haciéndose oír un poco más de lo habitual, queda la sensación de haber tocado de primera mano otro pequeño salto de calidad real en los modelos locales.
