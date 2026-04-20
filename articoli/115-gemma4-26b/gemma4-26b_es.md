---
tags: [" Generative AI", "Applications", "Training"]
date: 2026-04-20
author: "Dario Ferrero"
---

# Gemma 4 en local: 26 mil millones en mi PC
![gemma4-26b.jpg](gemma4-26b.jpg)

*Hay una satisfacción particular en hacer funcionar algo que se desaconsejaría descargar. No la satisfacción del hacker que fuerza un sistema, eso es otra cosa, sino esa más tranquila y artesanal de quien aprieta los tornillos un poco más allá del par recomendado y descubre que la estructura aguanta igual. Es el tipo de satisfacción que he encontrado esta semana, mientras Gemma 4 26B funcionaba en mi PC de consumo con una fluidez que no esperaba.*

Este artículo es el segundo de una serie que [comencé hace unas semanas con Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1.html). Si han leído aquella pieza, pueden saltarse el próximo párrafo. Si, por el contrario, están aquí por primera vez, les doy rápidamente las coordenadas del proyecto.

## El laboratorio, ya conocido

La idea es simple: tomar modelos abiertos recién lanzados, ejecutarlos en local en hardware de consumo y entender qué se obtiene realmente, fuera de los comunicados de prensa y los benchmarks de marketing. La herramienta es [LM Studio](https://lmstudio.ai/), una aplicación de escritorio que permite descargar e iniciar modelos sin abrir una terminal, con la utilísima característica de mostrar de antemano una estimación del rendimiento esperado en su propia configuración de hardware. Una discriminante cromática, verde-naranja-rojo, que ahorra horas de intentos en vano. La máquina es un PC ensamblado con criterio pero sin excesos: procesador AMD Ryzen 7700, 32 GB de RAM DDR5 y una GPU AMD Radeon RX 9060 XT con 16 GB de VRAM. Hardware de usuario avanzado, no de laboratorio de investigación.

El método, lo reitero aquí como hice al inicio de la pieza sobre Qwen, no es científico en el sentido académico del término. No hay un protocolo revisado por pares, no hay una muestra estadísticamente significativa de prompts, no hay reproducibilidad certificada por una conferencia. Las pruebas han sido verificadas cruzando los resultados con modelos de frontera como Claude y DeepSeek, pero esto no las transforma en benchmarks: siguen siendo pruebas de campo, realizadas con las herramientas de un usuario exigente. Las notas que acompañan a cada prueba son valoraciones personales, no sentencias.

## Gemma 4: la familia, la arquitectura, la filosofía

Google DeepMind lanzó Gemma 4 el 2 de abril de 2026, bajo licencia Apache 2.0. No es un detalle secundario: es la primera vez en la historia de la familia Gemma que un modelo se lanza bajo esta licencia, lo que elimina cualquier ambigüedad sobre el uso comercial y sitúa a Gemma 4 en el mismo plano permisivo que Qwen 3.5, con el que comparte el ecosistema de pesos abiertos (open-weight).

La familia se articula en cuatro variantes: E2B y E4B, pensadas para el despliegue en dispositivos móviles y periféricos con una ventana de contexto de 128.000 tokens, y las dos variantes mayores, el 26B MoE y el 31B Dense, con una ventana de contexto de 256.000 tokens. El 31B Dense es el modelo insignia en términos de calidad bruta, y en el momento del lanzamiento conquistó la tercera posición global en la clasificación de texto de Arena AI, no entre los modelos abiertos, sino entre todos los modelos en absoluto. El 26B MoE se situó en el sexto lugar.

Sobre el 26B MoE vale la pena dedicar dos líneas a la arquitectura, prometo ser breve. El concepto clave a tener en cuenta para leer el resto de este artículo es solo uno: el modelo 26B activa durante la inferencia solo unos 3,8 mil millones de sus parámetros totales, lo que lo hace significativamente más rápido de lo que el número total sugeriría, acercándolo en términos de velocidad a un modelo de 4 mil millones de parámetros. El precio a pagar es que los 26 mil millones de parámetros deben estar, de todos modos, en memoria. Rápido como un modelo pequeño, pesado como uno grande: un pagaré que se paga en VRAM.

Los números de los benchmarks son impresionantes, en particular respecto a la generación anterior. El salto respecto a Gemma 3 es difícil de ignorar: en AIME 2026 se pasa del 20,8 % al 89,2 %, en LiveCodeBench del 29,1 % al 80,0 %, en GPQA Science del 42,4 % al 84,3 %. No es una optimización incremental. Algo estructural ha cambiado en la forma en que estos modelos razonan.
![grafico1.jpg](grafico1.jpg)
[Imagen tomada de deepmind.google](https://deepmind.google/models/gemma/gemma-4/)

## La elección más allá del límite

Pasando a mi experimento específico, elegí probar el **Gemma 4 26B A4B Instruct Q4_K_M**, la versión con la cuantización más agresiva disponible para la variante de 26 mil millones. La elección fue deliberadamente al límite: LM Studio señalaba esta configuración como ligeramente fuera de las capacidades recomendadas para mi hardware, indicándola con ese color naranja que suele sugerir bajar las expectativas o redimensionar la elección. Ignoré el consejo, no por testarudez, sino porque probar el límite era exactamente el objetivo.

La cuantización Q4_K_M reduce la precisión numérica de los pesos del modelo de 16 bits a unos 4 bits, con una técnica que busca distribuir la pérdida de información de forma menos uniforme y más inteligente que las cuantizaciones planas, preservando mejor los pesos que el modelo considera más importantes. El resultado práctico es un archivo que ocupa unos 16 GB en disco y puede apoyarse enteramente en los 16 GB de VRAM de mi GPU, un equilibrio al límite: la Q4_K_M en el modelo 26B MoE usa aproximadamente 16 GB, justo dentro de los límites de una GPU de consumo como la mía. La pérdida de calidad respecto a la versión completa en bfloat16 es real, pero ¿cuán real? Este es uno de los subtextos de todo el experimento.

Elegí deliberadamente las mismas seis pruebas usadas con Qwen 3.5, no porque los dos modelos sean comparables en sentido estricto (uno es un 9B denso, el otro un 26B MoE), sino para mantener una coherencia metodológica mínima que permitiese al menos observaciones cualitativas. No es una comparación cara a cara. Es más parecido a medir la temperatura con el mismo termómetro en dos ciudades diferentes: los números son comparables, las ciudades no.

## Seis pruebas, seis veredictos

### Razonamiento científico: el mecanismo de Higgs — 5/5

La primera prueba es la que uso como termómetro general de la inteligencia del modelo: explicar el mecanismo de ruptura de la simetría electrodébil en el Modelo Estándar, el papel del campo de Higgs y por qué los bosones W y Z adquieren masa mientras que el fotón se queda sin ella. Petición explícita: lenguaje preciso pero accesible para un estudiante universitario de física.

La respuesta me sorprendió, no tanto por la corrección de los contenidos, sino por la calidad expositiva. El modelo organizó la explicación en cuatro secciones lógicas con la estructura que usaría un buen docente universitario, partiendo de la invarianza de gauge, pasando por el potencial de "sombrero mexicano" con la condición sobre el signo del término de masa, hasta las consecuencias físicas concretas. Las fórmulas estaban reportadas correctamente: el grupo de gauge SU(2)_L × U(1)_Y, el valor de expectativa en el vacío, las masas de los bosones. Pero la verdadera fuerza era la capacidad de acompañar cada fórmula con una imagen mental comprensible. Cuando el modelo escribió que los grados de libertad angulares son "comidos" por los bosones de gauge, estaba traduciendo un concepto matemático abstracto en algo que un físico de segundo año reconoce de inmediato. Es la diferencia entre un diccionario y un profesor.

Un detalle técnico que vale la pena señalar: a pesar de la complejidad del razonamiento y la longitud de la respuesta, el modelo razonó durante solo 2,2 segundos y generó el texto a unos 24 tokens por segundo. Para un modelo que teóricamente pesa 26 mil millones de parámetros, es una velocidad sorprendente, hecha posible precisamente por la arquitectura MoE que mantiene inactiva la mayor parte de los pesos durante la generación. **Nota: 5/5.**

### Multimodalidad: leer una hoja de cálculo desenfocada — 5/5

La segunda prueba estaba pensada para poner a prueba las capacidades visuales con una entrada deliberadamente difícil: una foto pequeña y poco nítida de una hoja de cálculo del presupuesto familiar mensual, con la petición de describir el contenido, los datos principales y las tendencias emergentes.

El modelo tardó unos diez segundos en analizar la imagen, un tiempo sensiblemente más largo que en la prueba anterior, comprensible para una tarea visual, antes de iniciar la generación a unos 23 tokens por segundo. La respuesta fue notablemente completa: identificó correctamente la estructura del documento, una plantilla de Excel con secciones para ingresos, ahorros y gastos, cada una con columnas de Presupuesto, Real y Diferencia. Leyó los valores numéricos clave con precisión milimétrica: ahorro neto mensual con presupuesto previsto de 1.350 dólares, real de 2.624 dólares, diferencia positiva de 1.274 dólares. Incluso notó la presencia de un gráfico de barras horizontales a la derecha de la hoja.

Pero la parte que confirmó que no se trataba de una simple transcripción fue el análisis: el modelo observó de forma autónoma que, a pesar del aumento de los ingresos, los gastos totales reales se habían mantenido cerca del presupuesto previsto, y extrajo una conclusión lógica sobre la eficiencia del ahorro. De una imagen desenfocada a un análisis de flujo de caja. **Nota: 5/5.**
![grafico3.jpg](grafico3.jpg)
Imagen tomada de mi PC durante las pruebas en LM Studio

### Código: un problema NP-hard con autocorrección — 4,5/5

La tercera prueba era la más técnica: implementar en Python un algoritmo para encontrar el ciclo de longitud máxima en un grafo no dirigido, gestionando grafos con ciclos múltiples y explicando la complejidad temporal.

Los aspectos positivos fueron notables. El modelo declaró sin vacilar que el problema es NP-hard, que no existe un algoritmo polinómico para resolverlo en grafos genéricos, y eligió el backtracking con búsqueda en profundidad como enfoque correcto, el que usaría cualquiera que haya estudiado algoritmos seriamente. La representación mediante lista de adyacencia con diccionario era eficiente, la lógica de exploración de los caminos simples correcta, la explicación de la complejidad temporal clara y honesta.

Sin embargo, la primera versión del código contenía tres errores sintácticos: una palabra clave escrita como `not be in` en lugar de `not in`, un nombre de variable equivocado en una llamada a un método, y otra variable escrita de forma errónea en el control de la condición de ciclo. Tres errores que, por sí solos, habrían impedido la ejecución sin intervención manual.

Pero aquí llega la parte más interesante de la valoración. Cuando pedí al modelo, de forma genérica y sin indicar cuáles eran los errores, que revisara el código en busca de posibles problemas de sintaxis, identificó y corrigió los tres al primer intento. En otras palabras, ya sabía cómo debía escribirse el código correcto: simplemente no lo había escrito con suficiente atención la primera vez. Este comportamiento refleja el uso realista de estas herramientas: rara vez un programador se fía ciegamente de la primera versión generada. La capacidad de diagnosticar sus propios errores ante una solicitud genérica es casi tan valiosa como la escritura inicial perfecta. Casi. **Nota: 4,5/5.**

### Multilingüe y planificación: Japón en francés — 4,8/5

La cuarta prueba valoraba la capacidad multilingüe y la planificación compleja: actuar como agente de viajes, planificando un itinerario de cinco días en Japón para un cliente francés que no habla inglés, con enfoque en templos históricos y comida callejera, más una sección final en italiano con consejos para un turista italiano.

El francés era impecable, fluido y sin errores, con un tono profesional pero no frío. La planificación del itinerario era logísticamente realista: el primer día en Asakusa con el Senso-ji y una izakaya por la noche, el segundo entre el santuario Meiji-jingu y Shibuya, el tercero en shinkansen a Kioto con el Kiyomizu-dera y Gion, el cuarto al Pabellón Dorado y al bosque de bambú de Arashiyama, el quinto al Fushimi Inari. Cada jornada equilibrada entre sitio histórico y experiencia gastronómica, como se pidió. El conocimiento de Japón era sorprendentemente detallado: citas de lugares como Sannenzaka y Ninenzaka, comidas específicas como los Age-manju, consejos prácticos sobre la tarjeta Suica y sobre la aplicación Japan Transit, la mención de los Depachika, las plantas sótano de los grandes almacenes japoneses, un detalle de insider que no se encuentra en las guías turísticas genéricas.

Sin embargo, la sección final en italiano presentaba dos errores que no pueden ser ignorados. El primero era "suggeramenti" en lugar de "suggerimenti", un término que en italiano simplemente no existe. El segundo era más extraño: la palabra "comprare" (comprar) aparecía escrita con una desinencia cirílica, "compraть", como si el modelo hubiese perdido momentáneamente el hilo del idioma. Dos errores en ciento cincuenta palabras de italiano, en un idioma que no está entre los más raros del mundo. Para un modelo que declara soporte para más de 140 idiomas, se esperaría una mayor robustez incluso en los idiomas secundarios de una respuesta. **Nota: 4,8/5.**
![grafico2.jpg](grafico2.jpg)
[Imagen tomada de deepmind.google](https://deepmind.google/models/gemma/gemma-4/)

### Contexto largo: 460 páginas de IA al primer intento — 5/5

La quinta prueba es la que considero más significativa para un uso real del modelo: cargué el [AI Index Report 2025 de Stanford](https://aiindex.stanford.edu/report/), un PDF de unas 460 páginas y más de 20 millones de caracteres, el mismo documento usado en la prueba con Qwen 3.5. Pedí al modelo, de forma genérica, que me hablara del crecimiento de la generación de vídeo y que me indicara las páginas donde encontrar los datos.

La respuesta llegó tras 4,4 segundos de procesamiento, a 22 tokens por segundo. El modelo identificó correctamente las páginas 125, 126 y 127, no una vaga referencia al "capítulo central", sino referencias precisas y verificables. Proporcionó después una síntesis estructurada de los contenidos: Stable Video Diffusion de Stability AI, Sora de OpenAI presentado en febrero de 2024 y hecho público en diciembre, Movie Gen de Meta con capacidades de edición e integración de audio, Veo y Veo 2 de Google. Incluso citó el célebre ejemplo del prompt "Will Smith eating spaghetti", esa prueba que se convirtió en un meme de la comunidad de IA para documentar los progresos en la generación de vídeo.

La comparación con la experiencia en Qwen 3.5 es iluminadora: el modelo de 9 mil millones había requerido cuatro intentos y una solicitud explícita de responder en el chat para obtener un resultado similar. Gemma 4 respondió al primer intento, sin vacilaciones. La ventana de contexto de 256.000 tokens resultó ser no solo una especificación técnica sino una capacidad realmente utilizable en hardware de consumo. **Nota: 5/5.**

### Razonamiento espacial: la habitación en el caos — 4,9/5

La última prueba era la que más me gusta porque mide algo difícilmente estandarizable: la inteligencia visoespacial. Cargué una foto de una habitación en gran desorden, la misma usada con Qwen 3.5, y pedí describir la disposición de los objetos y sugerir cómo ordenar para crear más espacio. El modelo tardó 7,5 segundos en procesar, el segundo tiempo más largo de toda la prueba.

La respuesta se abría con una frase que no entendí: "No se han encontrado citas en los archivos del usuario para esta solicitud". Una frase fuera de contexto, como si el modelo hubiese activado un mecanismo de búsqueda documental que no tenía nada que ver con la tarea visual. Superada esa extrañeza inicial, sin embargo, el resto de la respuesta fue excelente.

La descripción fue precisa: cama de matrimonio a la derecha con sábanas blancas parcialmente cubiertas, dos estanterías altas y estrechas posicionadas correctamente en relación con la ventana y el escritorio, escritorio gris a la izquierda, dos ventanas con cortinas de rayas verticales. Pero la parte realmente impresionante fue la descripción de los objetos en el suelo: ropa esparcida, calzado incluyendo un par de chanclas, bolsos, cestos de la ropa sucia, y el detalle de que uno de los cestos era azul con motivos. Este nivel de observación fina es notable.

La única pequeña imprecisión concernía al espejo: el modelo lo situaba sobre un armario o una cómoda, mientras que en la foto estaba montado en la puerta de entrada. Un error comprensible en una imagen bidimensional donde la distinción entre puerta y armario puede ser ambigua.

El plan de ordenación fue lógico y bien motivado: primero la ropa y los tejidos en el suelo porque son el obstáculo principal para caminar, después los cestos y los bolsos hacia una zona dedicada, finalmente el escritorio y las estanterías para reducir la sensación de abarrotamiento visual. La prioridad asignada a "liberar la superficie transitable" fue correcta y práctica. **Nota: 4,9/5.**
![tabella-confronto.jpg](tabella-confronto.jpg)

*Por puro capricho, dada la imposibilidad de comparación debido al tamaño y las características diferentes, les propongo una tabla donde pueden hacer sus propias valoraciones y elecciones según el hardware disponible. Aun siendo de tamaños diferentes los resultados son muy similares, con preferencias por uno u otro según la tarea; debo añadir, sin embargo, que en usos posteriores Qwen 3.5 9b mostró situaciones de bloqueo y no respuesta, que Gemma 4 26b no mostró.*

## Qué queda en la mano

La media aritmética de las seis pruebas es 4,87 sobre 5. Un número que debe contextualizarse con honestidad.

Estamos hablando de un modelo con 26 mil millones de parámetros totales, cuantizado a su versión más comprimida, ejecutado en hardware de consumo ligeramente por debajo de las especificaciones recomendadas, en local, sin nube, sin API, sin costes por token. El hecho de que funcione con fluidez a velocidades que hacen que la interacción sea reactiva es ya de por sí un resultado notable. El hecho de que responda con esta calidad lo hace algo más interesante.

La comparación con Qwen 3.5 9B, el sujeto de la prueba anterior, no es directa por la diferencia de tamaño, pero algunas observaciones cualitativas emergen claramente. Gemma 4 gestiona el contexto largo con una fiabilidad superior, responde al primer intento sin necesidad de solicitudes y muestra una coherencia expositiva más robusta en las tareas complejas. Paga algo, en cambio, en el frente de la perfección sintáctica en el código en la primera generación, y muestra alguna fragilidad en los idiomas secundarios dentro de la misma respuesta. No es un trade-off sorprendente para un modelo de este tamaño.

La pregunta que queda abierta, y que no entra en el alcance de este experimento, es cuánto ha costado efectivamente la cuantización Q4_K_M en términos de calidad respecto a la versión completa. Los resultados son lo suficientemente altos como para que sea difícil estimar cuánto margen ha quedado sobre la mesa. Quizás mucho, quizás sorprendentemente poco. Sería un experimento interesante para quien tenga acceso a hardware con más VRAM.

Lo que puedo decir con certeza, como aficionado que quiere entender qué es posible hacer con medios normales en 2026, es que la frontera entre "posible solo en la nube" y "posible en local" se ha desplazado de nuevo. No poco. Gemma 4 26B MoE, incluso en su versión más comprimida, en hardware que muchos usuarios avanzados ya poseen, produce respuestas que hasta hace unos meses habrían requerido una llamada a la API de un modelo de frontera. Este es el dato que encuentro más significativo, más que cualquier nota individual.

Una cosa es cierta: lo que en enero señalaba como la tendencia del año, la carrera por los [Small Language Models en local](https://aitalk.it/it/slm-2026.html), no está simplemente confirmándose, está quemando etapas. Y solo estamos en abril.
