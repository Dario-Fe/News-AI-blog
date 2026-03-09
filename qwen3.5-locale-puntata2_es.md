---
tags: ["Generative AI", "Applications", "E-learning"]
date: 2026-03-18
author: "Dario Ferrero"
---

## La IA en casa: LM Studio y Qwen 3.5 en mi PC - Entrega 2
![qwen3.5-locale-puntata2.jpg](qwen3.5-locale-puntata2.jpg)

*Continúa de la [Entrega 1](https://aitalk.it/it/qwen35-locale-puntata1.html), donde describimos la configuración de hardware, la elección de LM Studio como framework y las tres primeras pruebas: razonamiento científico sobre el mecanismo de Higgs, lectura multimodal de una hoja de cálculo desenfocada y generación de código para un problema NP-hard.*

La conversación en torno a Qwen 3.5 en las últimas dos semanas no se ha limitado a los foros técnicos internacionales. En Italia, voces como la de [Salvatore Sanfilippo](https://www.youtube.com/watch?v=NDBQq_NzxiE), entre los expertos más seguidos en el tema de la inteligencia artificial aplicada, han llevado el modelo a la atención de un público más amplio, contribuyendo a que este lanzamiento sea uno de los temas más discutidos de la temporada en el ecosistema italiano de la IA. No es un bombo publicitario de las redes sociales: es el reconocimiento de que algo estructural está cambiando en los modelos open-weight, y que ese cambio es finalmente lo suficientemente tangible como para merecer atención fuera de los círculos de investigadores.

Las tres pruebas que concluyen esta segunda entrega fueron diseñadas precisamente para tocar las áreas que más interesan a quienes no son investigadores pero usan la IA para trabajar, planificar, analizar y organizar: la capacidad de razonar en varios idiomas manteniendo la coherencia cultural, la gestión de documentos largos con precisión quirúrgica y la comprensión del espacio físico a través de una imagen.

## Prueba 4 — Agente de viajes en tres idiomas

La cuarta prueba se centraba en dos de las capacidades más publicitadas del modelo: el soporte multilingüe extendido (Qwen 3.5 soporta 201 idiomas) y el rendimiento como agente en tareas de planificación compleja. Imaginé un cliente francés que no habla inglés, interesado en visitar Tokio y Kioto con un enfoque en templos históricos y comida callejera. La petición era articulada: un itinerario de cinco días en un francés impecable, con consejos prácticos sobre transporte y barreras lingüísticas, seguido de una sección en italiano para un segundo viajero que quisiera seguir el mismo recorrido.

La respuesta podría haber sido un itinerario genérico generado mediante la interpolación de información de una base de datos de guías turísticas. No fue así. El francés era el de un consultor de viajes de gama alta: formal pero cálido, preciso sin ser burocrático. El itinerario tenía una logística real: llegada a Tokio y primera inmersión en Asakusa y Senso-ji; segundo día entre el Meiji Shrine y el antiguo mercado de Tsukiji con la indicación de que allí el sushi se come en la barra pagando por unidad; tercer día con shinkansen hacia Kioto y paseo por los bosques de bambú de Arashiyama a última hora de la tarde; cuarto día con la subida a los torii de Fushimi Inari con la advertencia explícita de llevar calzado cómodo; noche en Pontocho para tener la posibilidad de cruzarse con geishas. Quinto día en el mercado Nishiki, "el vientre de Kioto", como lo llamó el modelo, antes de la partida.

Los detalles marcan la diferencia entre información y conocimiento: saber que Suica y Pasmo son las tarjetas recargables para el transporte, que Google Translate con paquetes offline es casi indispensable en Japón, que en los templos hay que quitarse los zapatos. Todos presentes, todos correctos. La sección en italiano era un resumen práctico, escrito en un lenguaje fluido y útil, sin repetir de forma pedante todo el itinerario, sino sintetizando los consejos esenciales para quien ya conoce la ruta. El paso de un idioma a otro no bajó la calidad: el tono, la pertinencia cultural y la precisión se mantuvieron estables.

**Nota: 5/5.** Un agente que conoce Japón como un guía turístico, escribe en francés como un nativo y resume en italiano sin perder el hilo.

## Prueba 5 — La aguja en el pajar de 460 páginas

La quinta prueba era la más exigente desde el punto de vista técnico y, probablemente, la más relevante para quienes usan la IA en contextos profesionales de análisis documental. Cargué en LM Studio el [Artificial Intelligence Index Report 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report) del Stanford HAI: 460 páginas y unos 20MB, decenas de miles de palabras, gráficos, tablas, capítulos temáticos. Un volumen que ningún ser humano lee de principio a fin en una sesión. La pregunta era aparentemente sencilla: buscar los datos sobre el crecimiento de la generación de vídeo e indicarme en qué página se encuentran.

La primera vez, ninguna respuesta. La segunda, silencio. La tercera, de nuevo. En los tres intentos el modelo realizaba el razonamiento, que es visible y consultable, pero al final no producía la salida. Tuve que solicitarlo explícitamente, especificando que a veces el modelo no produce salida en el chat a pesar de haber procesado la petición. Al cuarto intento, la respuesta llegó y era sorprendentemente precisa.

El modelo identificó las páginas 126 y 127 del Capítulo 2 (Technical Performance), sección "Image and Video". Describió lo que contenían: la página 126 con las fichas de los modelos Google Veo, Meta Movie Gen y OpenAI Sora, con los gráficos de preferencia de usuario (Figuras 2.3.11 y 2.3.12); la página 127 con la comparación entre vídeos generados a lo largo del tiempo. Y luego recuperó espontáneamente un ejemplo específico: el prompt "Will Smith eating spaghetti", convertido con el tiempo en un pequeño caso de estudio informal sobre la calidad de los vídeos generados por IA, el tipo de detalle cultural que un buen investigador habría incluido en una nota al pie.

El comportamiento de bloqueo de los tres primeros intentos es un límite real que debe señalarse honestamente. Probablemente depende del volumen de datos a procesar y de cómo LM Studio gestiona los tokens de contexto en ventanas muy amplias. No es un problema que se resuelva en cinco minutos; requiere comprensión de vuestra configuración y paciencia. Pero cuando el modelo responde, responde bien.

**Nota: 4.5/5.** Precisión milimétrica en la recuperación de información de un documento de 460 páginas, páginas exactas, figuras numeradas, ejemplos culturales. Medio punto perdido por los tres intentos en vano, un comportamiento que el flujo de trabajo real debe tener en cuenta.

## Prueba 6 — El geómetra del caos doméstico

La última prueba fue quizás la más inusual, y la que produjo la respuesta más rica narrativamente. Descargué de internet una foto de baja calidad de una habitación sumida en el desorden: ropa por todas partes, una cama sin hacer, un escritorio sumergido en papel, estanterías saturadas, objetos esparcidos por el suelo. Cargué la foto en LM Studio y pedí al modelo que describiera la disposición de los objetos y propusiera una estrategia para ganar espacio.

La descripción de la habitación era visualmente fiel: la cesta azul en el centro que ocupa el camino principal, las pilas de ropa de colores divididas por colores y materiales, las zapatillas marrones y las deportivas esparcidas cerca de la entrada, la cama a la derecha con la ropa acumulada que hace inaccesible la mesilla de noche, el escritorio a la izquierda "abarrotado como un nido de desorden visual". Pero el detalle más impresionante fue uno: el modelo notó que el espejo de la pared reflejaba el armario blanco y algunas cajas en el suelo, demostrando que percibía no solo los objetos visibles sino las relaciones espaciales generadas por los reflejos, una comprensión tridimensional del espacio que no era obvia.

La estrategia de orden propuesta seguía una lógica impecable: primero despejar el centro de la habitación para crear un camino seguro, luego vaciar el escritorio para categorizar, después hacer la cama para recuperar superficie visual, finalmente archivar en los armarios ahora accesibles. Cada paso tenía una motivación: el centro primero porque es el riesgo de caída más inmediato, la cama después porque hacerla cambia visualmente la percepción de toda la habitación, no solo su funcionalidad. Es la lógica de quien ha entendido no solo qué hay en esa habitación, sino cómo funciona el espacio para quien vive en ella.

**Nota: 5/5.** Comprensión espacial tridimensional, análisis de los reflejos, estrategia de intervención motivada paso a paso. Un diseñador de interiores no lo habría hecho mejor.
![riconosimenti-img.jpg](riconosimenti-img.jpg)
*Captura de pantalla de una parte de la respuesta de Qwen 3.5 a la petición de analizar la imagen cargada.*

## El balance final

Seis pruebas, seis áreas, un cuadro bastante completo para sacar conclusiones, con la conciencia de que esto sigue siendo un experimento personal, no una evaluación sistemática.

Lo que surge con claridad es que Qwen 3.5 9B, a 30 tokens por segundo en una GPU de consumo con 16 GB de VRAM, hace cosas que hasta hace un año habrían requerido acceso a APIs de frontera de pago. Explica física cuántica con la claridad de un buen profesor, lee tablas desenfocadas como un analista, escribe código con conciencia teórica de los límites, planifica viajes en varios idiomas con coherencia cultural, encuentra páginas específicas en un informe de 460 páginas, describe una habitación desordenada y reconoce sus reflejos. Todo esto funciona offline, sin enviar un solo byte a ningún servidor.

Los límites existen y hay que decirlos sin rodeos. El comportamiento de bloqueo en salidas muy largas o contextos extendidos es el problema principal: requiere avisos explícitos e introduce una incertidumbre en el flujo de trabajo que quienes usan estas herramientas en producción deben gestionar. El primer intento interrumpido en la prueba de programación, los tres silencios en la prueba documental, no son defectos despreciables; son comportamientos que un usuario profesional debe aprender a anticipar.

También queda abierta una cuestión que ninguna prueba local puede resolver: la privacidad y la procedencia de los datos de entrenamiento. Qwen es un proyecto de Alibaba Cloud, una empresa china sujeta a la legislación de Pekín. Ejecutar el modelo en local resuelve la cuestión de la transmisión de datos en la inferencia (los prompts no salen de la máquina), pero no dice nada sobre qué ha visto el modelo durante el entrenamiento, ni sobre posibles sesgos relacionados con el contexto geopolítico de quienes lo crearon. Para muchos usos personales y profesionales la cuestión es irrelevante; para otros, en ámbitos regulados, en contextos donde la soberanía del dato es un vínculo legal, vale la pena reflexionar sobre ello antes de integrarlo en un flujo de trabajo crítico.

En el frente de la nube, la competencia sigue siendo asimétrica para las tareas que requieren un razonamiento profundo en varios pasos, conocimiento enciclopédico actualizado en tiempo real y gestión de contextos masivos sin comportamientos impredecibles. Los modelos de frontera como Claude, ChatGPT y Gemini siguen jugando en un campo diferente para estos escenarios. Pero la brecha se reduce con cada lanzamiento, y la dirección está clara.

## Las ganas de continuar

Esta experiencia ha sido lo que esperaba que fuera: instructiva, concreta y, a veces, sorprendente. Instalar un modelo de esta calidad en local, en un PC que no es una estación de trabajo de cinco mil euros, y obtener respuestas que aguantan la comparación con los mejores servicios en la nube, habría parecido inalcanzable hace solo doce meses. Ya no lo es.

Qwen 3.5 9B es sin duda el modelo open-weight más discutido de las últimas semanas, y la fama que se había labrado con las versiones anteriores de la familia no era infundada. Pero también es solo uno de los puntos de este ecosistema en rápida evolución. Para quienes tienen menos VRAM o buscan la excelencia en la programación, [Phi-4-mini de Microsoft](https://huggingface.co/microsoft/Phi-4-mini-instruct) merece atención. Para quienes trabajan principalmente en italiano o en lenguas europeas, las variantes de [Mistral](https://mistral.ai/) tienen características específicas de interés. Cada modelo destaca en algo y cede en otra cosa: la elección depende siempre del caso de uso, y el caso de uso solo lo conoce quien está frente al teclado.

El punto, sin embargo, no es qué modelo elegir. El punto es que esta elección existe, es accesible y funciona. Los LLM locales, o SLM si prefieren la denominación más precisa, ya no son un experimento para aficionados con hardware de laboratorio. Son herramientas actuales, que funcionan, que pueden mejorarse, que respetan la privacidad y que, con un nivel de hardware apenas superior al estándar de consumo, se convierten en poderosos aliados para diseñar, escribir, analizar y construir.

Solo hay que tener ganas de ensuciarse las manos. Y con estas herramientas, las manos se ensucian cada vez menos.
