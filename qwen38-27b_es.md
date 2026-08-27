---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-08-28
author: "Dario Ferrero"
---

# Qwen3.8-27B en local: cuando la densidad se hace sentir
![qwen38-27b.jpg](qwen38-27b.jpg)

*Hay una forma de reconocer cuándo un modelo está realmente 'pensando', y no es la calidad de la respuesta final, es el tiempo que tarda antes de escribirla. Con Qwen3.8-27B ese tiempo se siente plenamente, cada segundo, mientras el ventilador de la GPU gira un poco más fuerte de lo habitual y el cursor parpadea a la espera. En una época en la que todo el mundo corre hacia los Mixture of Experts para ir más rápido, he decidido hacer el experimento opuesto: ¿qué ocurre si se vuelve a un modelo que lo enciende todo, siempre, sin atajos?*

El 14 de agosto de 2026, el equipo Qwen de Alibaba, el Tongyi Lab, lanzó Qwen3.8-27B, un modelo denso multimodal de unos 27 mil millones de parámetros, distribuido bajo licencia Apache 2.0 junto con su hermano mayor Qwen3.8-2.4T-A95B, la versión de clase Max pensada para infraestructuras agenticas pesadas. Como se relata en el [anuncio oficial en el perfil de X del equipo Qwen](https://x.com/Alibaba_Qwen/status/2088280182356611304), la promesa era mantener abiertos los pesos de ambos tamaños de la generación 3.8, la ligera para el despliegue local y la enorme para quienes construyen agentes a escala industrial. El repositorio oficial en [GitHub](https://github.com/AlibabaCloud-Official/Qwen3.8-27B) lo describe como un modelo nativamente multimodal, capaz de superar a Qwen3.7-Plus en los flujos de trabajo de oficina y en la programación, con una ventana de contexto nativa de 262.000 tokens ampliable hasta un millón mediante YaRN.

Tras tres entregas de esta serie dedicadas a modelos Mixture of Experts, con [Qwen 3.6 35B A3B](https://aitalk.it/it/qwen36-35b-ai.html) y [Gemma 4 26B](https://aitalk.it/it/gemma4-26b.html) a la cabeza, Qwen3.8-27B rompe el esquema. No activa una fracción de sus parámetros para cada token como haría una orquesta que solo recurre a los músicos de turno; los enciende todos, siempre, los veintisiete mil millones al completo. Es un retorno de paradigma en un momento en el que la industria parecía haber decidido que el futuro de los modelos locales estaba hecho de expertos dispersos y parámetros durmientes. La pregunta que me impulsó a descargarlo es sencilla: ¿la potencia bruta de un modelo "todo encendido" compensa realmente en calidad, en un hardware de consumo, respecto al ahorro energético de un MoE?

Hay también un detalle técnico que vale la pena señalar para quienes trabajáis en inferencia profesional: según un [análisis técnico publicado en daily.dev](https://daily.dev/posts/qwen3-8-27b-alibaba-s-dense-27b-model-runs-on-one-gpu-with-262k-context-mzhf0nyjc), Qwen3.8-27B integra de serie un cabezal de predicción multi-token pensado para la decodificación especulativa (speculative decoding), con tasas de aceptación del orden del 92 % en precisión BF16 y del 85 % en FP8 en prompts breves. Un detalle que afecta sobre todo a quienes lo ejecutáis en infraestructuras de servidor, pero que demuestra lo mucho que se diseñó el modelo pensando en la eficiencia de la inferencia desde la propia ficha técnica, a pesar de la elección arquitectónica densa.

## El laboratorio, en resumen

Quienes seguís esta serie ya conocéis la máquina; quienes llegáis por primera vez encontraréis todos los detalles en la [primera entrega dedicada a Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1.html), que sigue siendo la referencia metodológica para todo el proyecto. Aquí me limito a recordar las cifras esenciales: un AMD Ryzen 7700, 32 GB de RAM DDR5 y una GPU AMD Radeon RX 9060 XT con 16 GB de VRAM, la misma configuración con la que ya he puesto a prueba a [Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata2.html), Qwen 3.6, Gemma 4 y [Ornith-1.0](https://aitalk.it/it/ornith-1.0.html). El software sigue siendo [LM Studio](https://lmstudio.ai/), elegido desde la primera entrega por la estimación cromática del rendimiento esperado—verde, naranja, rojo—que permite entender de antemano si un modelo funcionará cómodamente o al límite de sus posibilidades.

El repositorio no cuantizado de Qwen3.8-27B pesa unos 55,6 GB, un tamaño que excluye a priori cualquier ejecución en precisión completa en mi configuración. Empecé las pruebas con la cuantización Q8, la más fiel disponible en LM Studio para este modelo, y el resultado fue impracticable: unos 2 tokens por segundo, un ritmo que convierte cada intercambio conversacional en una prueba de paciencia incompatible con cualquier uso real. Así pues, cambié a Q4_K_M, un compromiso que sacrifica precisión numérica a cambio de una velocidad finalmente utilizable, entre 4,5 y 5,5 tokens por segundo según la prueba.

Los parámetros específicos de esta sesión: contexto ajustado a 130.000 tokens, un compromiso que aprovecha buena parte de la ventana nativa de 262.000 sin saturar la VRAM disponible; GPU offload de 30 capas de un total de 65, es decir, algo menos de la mitad del modelo cargado en la tarjeta gráfica y el resto confiado a la RAM del sistema; un pool de 8 hilos (threads) de CPU de 8 disponibles; lote (batch) de evaluación de 2048 con batch físico de 512; y un máximo de 4 predicciones concurrentes. Una configuración de compromiso declarado, pensada para equilibrar velocidad y memoria en lugar de buscar el punto de máximo rendimiento.

## Denso, multimodal y bastante locuaz

La diferencia arquitectónica respecto a los MoE probados en entregas anteriores no es un mero detalle de la ficha técnica; es la lente a través de la cual hay que leer cada uno de los resultados de esta prueba. Un modelo MoE como Ornith-1.0-35B activa unos 3 mil millones de parámetros de 35 para cada token; un modelo denso como este los activa todos, siempre. El coste computacional es el esperado: la velocidad cae vistosamente respecto a los competidores de expertos mixtos probados hasta ahora en esta serie, pero la pregunta abierta sigue siendo si ese gasto energético se traduce en un razonamiento más sólido.

En el frente multimodal, Qwen3.8-27B nace nativamente capaz de leer imágenes, un rasgo que lo distingue de modelos puramente textuales como [Laguna XS-2.1](https://aitalk.it/it/qwen3.5-locale-puntata2.html), y que le permite afrontar sin configuraciones adicionales las pruebas visuales de esta batería. El contexto nativo de 262.000 tokens, ampliable hasta un millón con YaRN según la documentación oficial, es teóricamente enorme, pero opté por limitarlo a 130.000 para esta sesión, un margen suficiente para probar su firmeza en documentos largos sin poner de rodillas la VRAM residual tras el offload de las capas.

Hay además un rasgo de carácter que emergió desde el primer prompt y que acompañó a toda la sesión: la verbosidad. Qwen3.8-27B es decididamente más prolijo que los demás modelos que han pasado por este banco de pruebas, con respuestas más largas, más articuladas y más ricas en detalles incluso donde no se requerían estrictamente. No es ni una virtud ni un defecto absoluto; depende de lo que busquéis. Quienes buscáis profundizar encontraréis material de sobra; quienes buscáis una síntesis rápida podríais encontrarlo excesivo.

## Ocho retos, un ritmo diferente

La batería de pruebas sigue siendo idéntica a la utilizada en las entregas anteriores para garantizar un mínimo de comparabilidad cualitativa entre modelos de diferentes tamaños y arquitecturas. No es una comparación directa en sentido estricto; se parece más a medir diferentes temperaturas con el mismo termómetro.

### Prueba 1, razonamiento científico: el mecanismo de Higgs, nota 5/5

La prueba que utilizo como termómetro general pidió al modelo que explicara el mecanismo de ruptura de la simetría electrodébil, el papel del campo de Higgs y la razón por la que los bosones W y Z adquieren masa mientras que el fotón permanece sin ella. La respuesta llegó estructurada en cuatro secciones lógicas: desde el problema de la masa en la simetría unificada hasta el potencial de sombrero mexicano que rompe espontáneamente la simetría, pasando por el mecanismo con el que W y Z adquieren masa y la simetría residual que protege al fotón. Didácticamente perfecta, con fórmulas correctas acompañadas de interpretaciones físicas precisas: un ejemplo de libro de texto bien escrito. Velocidad registrada: 5,64 tokens por segundo.

### Prueba 2, multimodalidad: una tabla de Excel de baja calidad, nota 5/5

Cargué una imagen deliberadamente borrosa de una hoja de cálculo, pidiendo una descripción del contenido, los datos principales y las tendencias. El modelo leyó correctamente la estructura, los valores numéricos y las relaciones entre columnas, extrayendo cinco tendencias clave entre estacionalidad, variación porcentual y evolución de los pedidos, para luego proponer ideas operativas como la revisión del plan para los meses de verano. Detectó de forma autónoma la correlación inversa entre el número de pedidos y el valor medio, un detalle que otros modelos probados en esta serie no habían captado con la misma claridad. Velocidad: 5,5 tokens por segundo; excelente solidez visual a pesar de la escasa calidad del archivo de partida.

### Prueba 3, generación de código: un problema NP-hard, nota 4,8/5

La tarea consistía en implementar en Python un algoritmo para encontrar el ciclo de longitud máxima en un grafo no dirigido, explicando su complejidad temporal. El modelo produjo una clase bien organizada con dos enfoques distintos: uno exacto con backtracking y poda (pruning), y uno aproximado para grafos de gran tamaño, demostrando plena conciencia de la naturaleza NP-hard del problema antes de escribir una sola línea de código. Sin embargo, el código contenía dos fallos concretos: una condición de poda redundante y un marcador de depuración que se había quedado por error en la parte superior del archivo.

Al pedírsele que revisara su trabajo sin indicaciones específicas sobre qué buscar, identificó ambos problemas y ofreció una versión corregida, explicando por qué la condición redundante era potencialmente peligrosa en caso de futuras modificaciones del código. La capacidad de autodiagnóstico sigue siendo un punto fuerte, pero los errores iniciales pesan en la nota. Velocidad: 5,7 tokens por segundo.

### Prueba 4, planificación multilingüe: cinco días en Japón, nota 5/5

La tarea pedía un itinerario de cinco días en Japón para un cliente francés, con texto en francés y una sección final de resumen en italiano. El francés producido era fluido y sin errores, con consejos prácticos sobre transporte, barreras lingüísticas y comida callejera, además de referencias culturales específicas como Tabelog para las reseñas de restaurantes, Omoide Yokocho para el ambiente retro y Pontocho para los callejones tradicionales de Kioto. La sección en italiano era igualmente cuidada, correcta y fluida. A diferencia de otros modelos evaluados en este banco que sufrieron percances lingüísticos, aquí no hubo ningún error de idioma. Velocidad: 5,42 tokens por segundo.

### Prueba 5, contexto largo: un PDF de 460 páginas, nota 4,8/5

Cargué el AI Index Report 2025, de más de 460 páginas, pidiendo información sobre el crecimiento de la generación de vídeo y las páginas exactas donde encontrarla. El modelo señaló con precisión las páginas 126 y 127, citando figuras específicas del informe y los principales modelos del sector: Google Veo, Meta Movie Gen, OpenAI Sora, Runway, Luma, Kuaishou, además del famoso ejemplo de la prueba de "Will Smith comiendo espaguetis" que se ha convertido en un indicador informal de los avances en la generación de vídeo. La precisión en la recuperación sigue siendo excelente incluso en una configuración comprimida. El único detalle menor fue una errata léxica que, si bien no empaña el preciso trabajo técnico, baja ligeramente la nota. Velocidad: 5,75 tokens por segundo, la más alta registrada en toda la sesión.
![immagine1.jpg](immagine1.jpg)
*Captura de pantalla durante las pruebas*

### Prueba 6, razonamiento espacial: la habitación desordenada, nota 5/5

Pedí una descripción de una fotografía de una habitación desordenada y una propuesta de estrategia de ordenación. La descripción cubrió todas las áreas funcionales—cama, suelo, escritorio, estanterías—con una estrategia de intervención justificada sobre una base práctica: el cesto más voluminoso debe moverse primero, y el suelo es la zona más crítica que despejar. Un consejo extra, la llamada regla de los tres segundos para decidir rápidamente sobre cada objeto ambiguo, añadió un toque metódico que otros modelos no habían propuesto. La comprensión visuoespacial fue muy buena; incluso notó los reflejos en el espejo, y la estrategia operativa estaba bien estructurada. Velocidad: 5,52 tokens por segundo.

### Prueba 7, agente de múltiples pasos: una aplicación web de gestión de gastos, nota 5/5

La tarea consistía en planificar el desarrollo de una aplicación web de gestión de gastos, especificando el stack tecnológico, la estructura del proyecto y la hoja de ruta para un equipo de dos desarrolladores. La respuesta propuso un stack moderno con React, NestJS, PostgreSQL y Prisma, una estructura monorepo, una hoja de ruta en seis sprints y una sección dedicada a cuestiones transversales: zonas horarias, rendimiento, seguridad e importación de CSV. La división del trabajo entre los dos desarrolladores era tan detallada como la que propondría un gestor de proyectos con experiencia real, con menciones oportunas a herramientas como Docker, GitHub Actions y Resend, junto a buenas prácticas como el almacenamiento en caché y el rate limiting. Velocidad: 5,12 tokens por segundo.

### Prueba 8, conversación larga: cuatro turnos, nota 5/5

La última prueba midió la retención de la memoria conversacional a lo largo de cuatro turnos relativos al stack tecnológico, notificaciones, base de datos y escalabilidad de una app de gestión de tareas. El modelo mantuvo una coherencia total, recordando y justificando cada elección técnica anterior, proponiendo una arquitectura híbrida con WebSockets para notificaciones dentro de la app y correo electrónico para eventos asíncronos, un esquema de base de datos completo con índices estratégicos y una hoja de ruta de escalabilidad hasta diez mil usuarios estructurada en tres niveles progresivos. La velocidad bajó—4,5, 4,57, 4,68 y finalmente 4,28 tokens por segundo—, una ralentización fisiológica debida al aumento del contexto acumulado, sin ninguna pérdida perceptible en la calidad de las respuestas.

## Tabla de resumen
![immagine2.jpg](immagine2.jpg)
Nota media: 4,95 sobre 5. Velocidad media: aprox. 5,3 tokens por segundo.

## El pensador lento, y lo que realmente significa

Los números cuentan una historia clara, pero vale la pena analizarla desde varios ángulos antes de sacar conclusiones. En el plano de la calidad, Qwen3.8-27B ha igualado, y en ciertos pasajes superado en profundidad, los resultados obtenidos por los modelos MoE probados en entregas anteriores, con la única excepción de la prueba de código, penalizada por los errores iniciales corregidos posteriormente tras el requerimiento. La densidad compensa, evidentemente, en términos de coherencia y capacidad de razonamiento en tareas aisladas.

En el plano de la velocidad, sin embargo, la comparación es despiadada. Ornith-1.0-35B, un MoE con solo 3 mil millones de parámetros activos por token, se movía de forma estable entre los 16 y los 17 tokens por segundo en la misma máquina. Qwen3.8-27B, en su configuración comprimida Q4_K_M, se quedó en una media de 5,3. Es la diferencia entre leer una novela a un ritmo natural y tener que deletrearla palabra por palabra, una experiencia que recuerda en cierto modo a *Primer*, la película independiente de Shane Carruth convertida en obra de culto precisamente por su densidad narrativa: hermosa, rigurosa, pero no hecha para quienes tienen prisa por llegar a los créditos finales.

Hay además una pregunta que atañe a quién utilizará realmente este modelo. Según los datos difundidos por Alibaba y recogidos por un [análisis de OfficeChai sobre el lanzamiento del modelo](https://officechai.com/miscellaneous/alibaba-releases-qwen-3-8-27b-beats-muse-glimmer-30b-on-many-benchmarks/), en CoWorkBench—el benchmark interno para tareas de productividad a largo plazo—, Qwen3.8-27B obtiene 70,7 puntos, por delante tanto de Opus4.6 Max (estancado en 68,2) como de su predecesor Qwen3.6-27B (estancado en 61). Son cifras difundidas por la propia empresa, por lo que deben leerse con la cautela debida a cualquier benchmark autoproducido, pero confirman la dirección: el salto generacional en la calidad del razonamiento está ahí, independientemente de cómo se mida.

Quién gana y quién pierde en este escenario depende enteramente del perfil de uso. Quienes trabajáis en tareas aisladas y complejas—explicaciones científicas, análisis de documentos, planificación detallada—y podéis permitiros esperar unos segundos adicionales por respuesta generada, encontraréis en un modelo denso como este un razonador más fiable. Por el contrario, quienes buscáis un asistente conversacional reactivo para un uso diario con un alto volumen de intercambios, probablemente encontraréis más equilibrada la opción de un MoE como Ornith-1.0, que en la entrega anterior había obtenido además la puntuación máxima de 5 sobre 5, sin pagar la abultada factura en velocidad.

Queda una pregunta abierta que me llevo a la próxima entrega: ¿cuánto de este desfase de velocidad y de los ligeros matices sería recuperable con una cuantización Q8, más VRAM disponible y tal vez con todo el modelo cargado en la GPU sin tener que derivar la mitad de las capas a la RAM del sistema? Es el tipo de duda que esta serie, nacida para entender qué se puede obtener con medios normales, seguirá persiguiendo entrega tras entrega.
![immagine3.jpg](immagine3.jpg)

**Veredicto**: Qwen3.8-27B es un modelo para quienes no tenéis prisa y buscáis profundidad de razonamiento por encima de cualquier otra cosa, con la conciencia de que su naturaleza densa se paga cara en velocidad dentro de un hardware de consumo. Si la reactividad es la prioridad, un MoE sigue siendo la opción más equilibrada, aun a costa de perder algunos puntos de calidad en las tareas más difíciles.

*Nota técnica: todas las velocidades indicadas están expresadas en tokens por segundo (t/s) y medidas localmente con LM Studio en la configuración de hardware descrita en el primer artículo de la serie. Las notas son valoraciones personales, no puntuaciones de benchmarks automatizados.*
