---
tags: ["Research", "Applications", "Generative AI"]
date: 2026-04-13
author: "Dario Ferrero"
---

# TurboQuant: un bit para redefinir los límites de la inteligencia artificial
![turboquant.jpg](turboquant.jpg)

*A finales de abril de 2025, cuatro investigadores de Google Research y de la Universidad de Nueva York publicaron en arXiv un artículo con un título sobrio: *[TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate](https://arxiv.org/abs/2504.19874)*. Durante meses, casi nadie habló de ello fuera de los círculos académicos. Luego, en marzo de 2026, Google publica una [entrada en el blog oficial](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) anunciando TurboQuant como un gran avance en la eficiencia de los modelos lingüísticos, con la aceptación en el [ICLR 2026](https://iclr.cc/), y en cuestión de cuarenta y ocho horas el artículo aparece en todos los canales tecnológicos. Anuncios de compresiones más de cinco veces superiores sin pérdida de calidad, titulares entusiastas por doquier. Un año de retraso, una oleada de clamor.*

Vale la pena detenerse, porque esta dinámica —el artículo durmiente que explota gracias al impulso comunicativo de un gran laboratorio— nos dice algo sobre cómo funciona la información en el ecosistema de la inteligencia artificial. Aún más vale la pena entender qué hace realmente TurboQuant, sin sobreestimar ni descartar la contribución.

Cuando un gran modelo lingüístico genera texto, no procesa cada palabra desde cero cada vez. En su lugar, mantiene en memoria una estructura llamada **KV cache**, un archivo de pares clave-valor, que funciona como un resumen digital de alta velocidad. A medida que avanza la conversación, el modelo acumula en ella los vectores matemáticos que codifican el significado de todo lo que ya ha leído, para consultarlos instantáneamente durante el mecanismo de *atención* (*attention*), con el que el Transformer decide a qué prestar atención en cada momento.

El problema es que esta caché crece de forma inexorable con el contexto. Con ventanas de 128.000 o 250.000 tokens, que ya son el estándar en los modelos modernos, puede ocupar decenas de gigabytes de memoria de alta velocidad. Quienes utilizan modelos en local conocen la situación paradójica: RAM suficiente para cargar los pesos del modelo, pero insuficiente en cuanto se intenta usar con un contexto largo. Como tener un archivo espacioso con pasillos demasiado estrechos para meter los archivadores.

La respuesta obvia es comprimir esos vectores, y ahí es donde entra la cuantización.

## Cuantizar sin perder el hilo

La cuantización es uno de esos conceptos que parecen oscuros hasta que se encuentra la analogía adecuada. Imaginad una regla con graduaciones finísimas, capaz de medir hasta la décima de milímetro. Queréis archivar miles de mediciones pero tenéis poco espacio, así que pasáis a una regla más tosca con marcas cada medio centímetro: perdéis un poco de precisión, pero ocupáis mucho menos espacio. En la práctica, los vectores KV se guardan normalmente a 16 bits por componente, unos 65.000 valores distintos. Llevarlos a 4 bits reduce a solo 16 valores posibles, con un ahorro de memoria de cuatro veces, pero con una aproximación que puede degradar el rendimiento del modelo.

La degradación no es baladí. Como observa el programador y analista técnico Salvatore Sanfilippo en su análisis profundo, la cuantización de la KV caché no solo afecta a la capacidad de recuperar detalles textuales precisos, sino que también compromete la calidad de la síntesis semántica en las capas posteriores del Transformer, donde los tokens se convierten en representaciones cada vez más abstractas. Los puntos de referencia sobre la *aguja en el pajar* (needle in a haystack), la prueba clásica en la que se esconde una información específica en un texto muy largo, captan solo una parte de este deterioro.

El territorio ya ha visto muchos exploradores. Técnicas como [KIVI](https://arxiv.org/abs/2402.02750) han propuesto diversos enfoques para la compresión de la KV caché. En el campo más general, la cuantización de producto (*product quantization* o PQ) es el estándar histórico: divide cada vector en subvectores, construye un diccionario para cada uno y sustituye cada subvector por el índice del centroide más cercano. Funciona bien, pero requiere una fase de entrenamiento fuera de línea (offline), inutilizable en escenarios como la KV caché, donde los vectores llegan en tiempo real.

TurboQuant parte de un objetivo más ambicioso: ser *independiente de los datos* (*data-oblivious*), es decir, funcionar sin saber nada sobre la distribución de los datos de entrada, y hacerlo con garantías teóricas sólidas.
![grafico1.jpg](grafico1.jpg)
[Imagen tomada de arxiv.org](https://arxiv.org/abs/2504.19874)

## El truco de la rotación y el bit residual

El núcleo técnico de TurboQuant se explica en dos actos.

**Primer acto: la rotación aleatoria.** Los vectores KV tienen un problema estructural molesto: sus componentes no se distribuyen uniformemente. Algunas dimensiones contienen casi toda la información relevante, mientras que muchas otras están cerca de cero. Aplicar una cuantización estándar significa desperdiciar bits valiosos en dimensiones irrelevantes y acumular errores en las pocas que realmente cuentan. Es como calibrar una balanza de precisión para pesar piedrecitas, perdiendo así toda la sutileza necesaria para pesar polvo de oro.

TurboQuant resuelve esto aplicando una **rotación aleatoria** al vector antes de cuantizarlo: multiplicarlo por una matriz de rotación cambia las coordenadas sin alterar la longitud del vector, exactamente igual que girar un objeto en el espacio no cambia sus dimensiones. El resultado es que, tras la rotación, las componentes siguen una distribución estadística conocida de antemano, una distribución Beta que en altas dimensiones converge a una gaussiana, transformando un problema dependiente de los datos en uno universal. Ya no importa la distribución original: se pueden precalcular las tablas de cuantización óptimas para cada nivel de bits deseado y aplicarlas siempre, sin calibraciones caso por caso. Cabe señalar la distinción técnica importante: multiplicar por una matriz gaussiana aleatoria cualquiera también cambiaría la longitud del vector, introduciendo distorsiones incontrolables. La rotación mantiene la norma L2 invariable, y esta propiedad es fundamental.

**Segundo acto: el bit del residuo.** Los cuantizadores optimizados para minimizar el error cuadrático medio (MSE) no garantizan estimaciones precisas de los *productos internos* entre vectores, y los productos internos son exactamente lo que el mecanismo de *atención* calcula continuamente. Tener una buena reconstrucción del vector no implica automáticamente buenas estimaciones de los productos internos.

TurboQuant aborda esto con una segunda etapa: después de haber cuantizado el vector a b−1 bits, calcula el residuo —la diferencia entre el vector original y el cuantizado— y lo procesa con la técnica **QJL** (*Quantized Johnson-Lindenstrauss*), que lo proyecta sobre una matriz gaussiana aleatoria y conserva solo el signo de cada componente, ocupando exactamente 1 bit. Este bit funciona como corrector de errores: garantiza que la estimación de los productos internos sea insesgada (*unbiased*), es decir, que el error no esté orientado sistemáticamente en una dirección. La magnitud del error residual se estima analíticamente sin guardarla, porque la distribución se conoce por la construcción del cuantizador. El sistema utiliza en total b bits: b−1 para la compresión principal, 1 para la corrección.

## ¿Qué solidez tiene la afirmación teórica?

El artículo afirma que TurboQuant es *casi óptimo* (*near-optimal*), cercano al límite teórico inferior de distorsión para cualquier cuantizador posible. Es el tipo de afirmación que debe leerse con cuidado.

Los autores demuestran, utilizando el teorema de codificación de Shannon y el principio minimax de Yao, que para cualquier cuantizador aleatorizado existen entradas para las cuales la distorsión MSE es de al menos 1/4^b. TurboQuant alcanza una distorsión como máximo √(3π/2) ≈ 2,7 veces superior a este límite inferior, y a 1 bit, la brecha se reduce a unos 1,45. Los resultados están formalmente demostrados.

La afirmación se sostiene, con dos precisiones. Primero: "casi óptimo" significa dentro de un factor constante del límite teórico, no tocar el límite. La constante 2,7 es pequeña y en la práctica despreciable, pero técnicamente la brecha existe. Segundo: el límite inferior se deriva para el peor caso sobre entradas arbitrarias. En producción, las distribuciones reales de los vectores KV pueden comportarse de manera diferente.

Una distinción fundamental, a menudo ignorada en la cobertura mediática, es la que existe entre la optimización para MSE y la optimización para la distorsión del producto interno. Son dos objetivos diferentes que requieren soluciones distintas, y TurboQuant aborda ambos con su enfoque de dos etapas. No es un detalle: significa que el método está pensado específicamente para el funcionamiento interno de los Transformers, no solo para comprimir vectores en un sentido genérico.
![grafico2.jpg](grafico2.jpg)
[Imagen tomada de research.google](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)

## La cuestión RabbitQ: quién hizo qué primero

El artículo suscitó un debate durante la fase de revisión, y sería deshonesto no abordarlo.

El quid: la rotación aleatoria como técnica de preprocesamiento no fue inventada por TurboQuant. Un método anterior llamado [RabbitQ](https://arxiv.org/abs/2405.12154) ya había utilizado una transformación similar, y sus autores protestaron públicamente durante la revisión por pares, sosteniendo que su contribución había sido ignorada. Sus notas fueron aceptadas, pero la caracterización de RabbitQ en el artículo final siguió considerándose inadecuada, y los investigadores reivindican también para su método propiedades de excelencia asintótica.

Existe también un trabajo anterior de los mismos autores de TurboQuant, [PolarQuant](https://arxiv.org/abs/2502.02617), que utilizaba una transformación en coordenadas polares para obtener un efecto similar, pero con un coste computacional significativamente más elevado, lo que lo hacía inutilizable en escenarios en línea. TurboQuant es una evolución más práctica del mismo.

Como observa Sanfilippo, el truco de la rotación ya estaba presente en otros lugares, y no haberlo reconocido explícitamente es la parte más problemática de toda la historia. La comunicación pública de Google ha pasado por alto con naturalidad estos precedentes, amplificando la impresión de una novedad más radical de lo que el propio artículo sostiene.

## Los puntos de referencia y el valor real de la contribución

La afirmación de "absoluta neutralidad cualitativa a 3,5 bits" está respaldada por los datos, pero con contextos que merecen atención. Las pruebas principales se realizan sobre Llama-2-7B, un modelo de 7.000 millones de parámetros que para los estándares actuales se considera pequeño. En modelos más grandes, la cuantización agresiva tiende a comportarse de manera diferente. Sanfilippo subraya un punto crítico: cuando los puntos de referencia muestran que incluso métodos menos sofisticados obtienen puntuaciones similares, puede significar que la tarea es demasiado sencilla para discriminar las diferencias reales.

En LongBench, la comparación es más reveladora. KIWI a 5 bits obtiene puntuaciones comparables a TurboQuant a 3,5 bits en diversas tareas. Esto no desmerece el resultado —usar menos bits para la misma calidad es una ventaja real—, pero redimensiona el alcance de la "revolución". El ahorro efectivo, en la evaluación más honesta, es del orden de un bit respecto al estado del arte: poder cuantizar a 4 bits con el mismo rendimiento que una cuantización a 5 bits con otros métodos, es decir, reducir la ocupación de la KV caché en un 20 % respecto a los competidores. Una ventaja sólida, no una discontinuidad.

En el frente de la búsqueda vectorial, los resultados son, en cambio, más claramente diferenciadores: eliminar la fase de entrenamiento fuera de línea del libro de códigos (*codebook*) es una ventaja operativa concreta para quienes construyen sistemas de recuperación (*retrieval*) sobre datos dinámicos.
![grafico3.jpg](grafico3.jpg)
[Imagen tomada de research.google](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)

## Preguntas abiertas

Tras leer el artículo, la entrada del blog, las críticas de los investigadores de RabbitQ y el análisis de Sanfilippo, quedan algunas preguntas fundamentales sin respuesta satisfactoria.

La primera y más importante: ¿se transfieren los resultados sobre Llama-2-7B a los modelos de 70 o 400 mil millones de parámetros, a las arquitecturas de mezcla de expertos (*mixture-of-experts*) hoy dominantes? La teoría dice que sí, pero debe verificarse empíricamente. Las arquitecturas más recientes, con atención de consulta agrupada (*grouped query attention*) o configuraciones de consulta múltiple (*multi-query*), donde se reducen las dimensiones de los vectores KV, podrían responder de manera diferente a la rotación aleatoria.

La segunda se refiere a la comparación directa con RabbitQ en las mismas condiciones. Las polémicas durante la revisión por pares sugieren que la comparación presentada en el artículo no era del todo justa: RabbitQ probado en CPU, TurboQuant en H100. Queda pendiente realizar una comparación en hardware idéntico, con los mismos puntos de referencia, de forma independiente.

La tercera se refiere a la integración en las canalizaciones reales. En producción, la KV caché coexiste con estrategias de desalojo (*eviction*) de tokens, atención dispersa (*sparse attention*) y sistemas de paginación de memoria como PagedAttention. Un bit ganado por la cuantización puede ser fácilmente anulado por una integración subóptima en estos sistemas compuestos.

Por último, la pregunta más amplia: ¿es la compresión de la KV caché realmente el principal cuello de botella en la inferencia de largo contexto, o hay otros factores —ancho de banda, latencia de acceso, paralelización de la atención— que pesan más? Ahorrar un bit es una contribución real, pero su impacto práctico depende de dónde se encuentre la verdadera restricción del sistema.

TurboQuant es una pieza de investigación sólida, con fundamentos teóricos robustos y una contribución técnica original en la segunda etapa QJL. No es el final de la historia de la compresión vectorial, y no era justo presentarlo como tal. Pero es un paso adelante genuino, del tipo que vale la pena entender, no solo compartir.
