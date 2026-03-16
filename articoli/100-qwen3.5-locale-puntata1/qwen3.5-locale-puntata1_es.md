---
tags: ["Generative AI", "Applications", "E-learning"]
date: 2026-03-16
author: "Dario Ferrero"
---

# La IA en casa: LM Studio y Qwen 3.5 en mi PC - Entrega 1
![qwen3.5-locale-puntata1.jpg](qwen3.5-locale-puntata1.jpg)

*Hay un momento preciso en el que una tecnología deja de ser una promesa y se convierte en una herramienta. No es cuando sale el comunicado de prensa, ni cuando los benchmarks dan la vuelta a las redes sociales, sino cuando una persona normal, con un PC normal, se sienta, descarga algo y decide entender de verdad lo que está pasando. Este artículo es ese momento, al menos para mí.*

En las últimas dos semanas, el nombre que ha dominado las conversaciones en el ecosistema open-weight de la inteligencia artificial es solo uno: Qwen 3.5. El equipo de Alibaba lanzó el 2 de marzo de 2026 la serie small del modelo, variantes de 0,8 a 9 mil millones de parámetros, todas bajo licencia Apache 2.0, todas ejecutables en hardware de consumo, y la reacción de la comunidad fue inmediata y entusiasta. Pero antes de entrar en los detalles del modelo y de mi experimento personal, conviene entender por qué este momento ha llegado precisamente ahora.

## El viento cambia de dirección

En un artículo publicado hace unas semanas en este portal, [analicé las razones por las que 2026 se perfila como el año de los Small Language Models](https://aitalk.it/it/slm-2026.html): la convergencia entre las presiones sobre los costes energéticos, las demandas de privacidad cada vez más estrictas y un salto cualitativo en la eficiencia arquitectónica que ha rediseñado la frontera entre lo "posible en la nube" y lo "posible en local". No es una tendencia ideológica, es una respuesta pragmática a limitaciones reales.

Los datos, sin embargo, cuentan todavía una historia de dos velocidades. Como se desprende del [análisis sobre el informe DigitalOcean Currents publicado también aquí](https://aitalk.it/it/agenti-al-lavoro.html), el 64% de las empresas hoy integran modelos a través de APIs de terceros proveedores, y solo el 21% usa modelos open-weight en producción. La nube no ha muerto: sigue siendo dominante. Pero la que parecía una asimetría insuperable entre modelos propietarios enormes y modelos locales "de reserva" se está estrechando con una velocidad que sorprende incluso a los observadores más atentos.

En benchmarks como [GPQA Diamond](https://huggingface.co/datasets/Idavidrein/gpqa), la prueba de referencia para el razonamiento avanzado de nivel universitario —198 preguntas de física, química y biología—, Qwen3.5-9B obtiene 81.7, superando al GPT-OSS-120B de OpenAI que se queda en 71.5, según se informa en la [página oficial del modelo en HuggingFace](https://huggingface.co/Qwen/Qwen3.5-9B). Estamos hablando de un modelo con trece veces menos parámetros. No es una optimización incremental: es un cambio de paradigma sobre lo que significa "pequeño" en 2026.

Las reacciones en el sector han sido significativas y, como suele ocurrir en este campo, no unánimes. Algunos observadores destacados han acogido el lanzamiento con entusiasmo, destacando la densidad de capacidades en relación con el tamaño. Otros, empezando por Anthropic, han mantenido un tono más cauto, observando que los modelos optimizados para rendir en los benchmarks no siempre trasladan esas capacidades al mundo real con la misma fidelidad. Una tensión que atraviesa todo el debate sobre la IA open-weight y que ningún número en una tabla resuelve definitivamente. La verdad, como siempre, está en el uso.

Y es exactamente por eso por lo que he decidido ensuciarme las manos.

## Un experimento honesto, sin pretensiones científicas

Antes de continuar, es necesario tener claro qué es este artículo y qué no es. Lo que sigue es un experimento personal, realizado por un aficionado que quiere entender qué se puede obtener con medios normales en este momento histórico preciso. No hay un protocolo de pruebas revisado por pares, no hay una muestra de prompts estadísticamente significativa, no hay un método reproducible que resistiera el escrutinio de una conferencia académica. Las pruebas se verificaron cruzando los resultados con modelos de frontera como Claude y DeepSeek, pero esto no las convierte en benchmarks científicos: siguen siendo pruebas de campo, realizadas con las herramientas de un usuario avanzado, no de un investigador.

El valor, si lo hay, reside precisamente en esto: entender hasta dónde se puede llegar con conocimientos buenos pero no de doctorado, con hardware privado y la voluntad de entender antes de comprar. Quienes deseen números certificados encontrarán los benchmarks oficiales en la [página HuggingFace del modelo](https://huggingface.co/Qwen/Qwen3.5-9B). Quienes quieran saber cómo funciona en un PC de 2025 adquirido a un precio razonable, sigan leyendo.

## El laboratorio: un PC de nivel intermedio

La máquina en la que realicé las pruebas no es una estación de trabajo de renderizado profesional ni un equipo de gaming de competición. Es un PC montado con criterio pero sin exagerar: procesador AMD Ryzen 7700, 32 GB de RAM DDR5 y, sobre todo, una GPU AMD Radeon RX 9060 XT con 16 GB de VRAM. Una configuración que muchos usuarios avanzados, gamers, creadores de contenido o desarrolladores que trabajan desde casa podrían reconocer como propia. Hardware de gama media-alta en el segmento de consumo, pero lejos de la A100 que uno imagina cuando se habla de inferencia local en modelos de lenguaje.

Esta elección no es casual. Precisamente el nivel medio de la configuración es el punto. Si un modelo funciona bien aquí, funcionará bien en una enorme parte de los PC ya existentes. Si tiene dificultades aquí, esa parte se reduce considerablemente.

## Elegir el framework: LM Studio frente a Ollama

Para ejecutar un modelo de lenguaje en local se necesitan dos cosas: el modelo en sí (un archivo de unos cuantos gigabytes) y un framework que haga de intérprete entre el hardware y el modelo, gestionando la memoria, la tokenización y la inferencia. Sin esta capa intermedia, descargar los pesos de un modelo es como tener los archivos de una película sin un reproductor de vídeo.

Los dos caminos que dominan este espacio en 2026 pueden estar representados por [LM Studio](https://lmstudio.ai/) y [Ollama](https://ollama.com/), y la diferencia entre ellos refleja una tensión clásica en el software: accesibilidad frente a control.

[Ollama](https://ollama.com/) es la herramienta de los desarrolladores. Se instala con una línea de terminal, expone por defecto una API REST compatible con OpenAI en `localhost:11434`, se integra sin fricciones en scripts, flujos de trabajo y aplicaciones. Es de código abierto, tiene una amplia comunidad y su filosofía minimalista —un comando para descargar, un comando para ejecutar— lo convierte en el backend preferido de docenas de aplicaciones de terceros. En términos de rendimiento bruto, suele ser más rápido, gestiona mejor las peticiones concurrentes y consume menos recursos gracias a la ausencia de sobrecarga gráfica. La otra cara de la moneda: requiere familiaridad con el terminal, la configuración avanzada se realiza a través de Modelfiles y su interfaz gráfica nativa llegó tarde y sigue siendo mínima. También hay una cuestión de transparencia que conviene señalar: Ollama es de código abierto y la comunidad confía en su conducta, mientras que LM Studio es de código cerrado, un detalle que para quienes están especialmente atentos a la privacidad vale la pena tener en cuenta.

[LM Studio](https://lmstudio.ai/) juega en un campo diferente. Es una aplicación de escritorio con una interfaz gráfica cuidada, disponible para Windows, macOS y Linux. Permite buscar, descargar y cargar modelos sin abrir un terminal, expone también una API compatible con OpenAI para quienes quieran integrarla en otras herramientas, y gestiona automáticamente la aceleración por GPU en hardware NVIDIA, Apple Silicon y AMD. Pero el detalle que realmente cambia la experiencia para quienes llegan a la IA local sin formación como desarrolladores es uno: en el momento de seleccionar un modelo, LM Studio muestra en tiempo real una estimación del rendimiento esperado en vuestra configuración de hardware, con indicadores de color que comunican inmediatamente si el modelo funcionará con fluidez, con limitaciones o si el hardware es insuficiente. Para un particular que experimenta, esta eliminación de fricciones compensa cualquier posible brecha de rendimiento respecto a Ollama.

La elección para este experimento recayó en LM Studio por razones pragmáticas: la posibilidad de ver de antemano si Qwen 3.5 9B Q8_0 funcionaría a pleno rendimiento en mi GPU, sin cálculos manuales ni documentación técnica que consultar, me permitió optimizar la elección de inmediato. Para quienes tengan intención de integrar un modelo en una aplicación, automatizar flujos de trabajo o trabajar en un entorno de servidor, Ollama sigue siendo la opción más sólida.
![lmstudio.jpg](lmstudio.jpg)
*Captura de pantalla de mi PC al iniciar LM Studio. En el menú superior derecho, las opciones del software con el botón inferior para seleccionar y descargar el modelo deseado. Al lado, el historial de chats. En la parte inferior central, el cuadro de diálogo para los prompts, donde se puede ver el modelo seleccionado.*

## Instalar LM Studio: cinco minutos y listo

La instalación no requiere conocimientos técnicos especiales. Desde el [sitio oficial](https://lmstudio.ai/) se descarga el instalador para su sistema operativo —un ejecutable en Windows, un DMG en macOS, una AppImage para Linux— y se procede como con cualquier otra aplicación de escritorio. Sin dependencias externas que instalar, sin entornos virtuales que configurar, sin terminales que abrir. El paquete pesa unos 500 MB; las primeras pantallas guían hacia la configuración de la aceleración por hardware detectada automáticamente y, en pocos minutos, se encuentra ante la pantalla principal.

Desde allí, la sección de búsqueda de modelos permite explorar el catálogo, que se nutre principalmente de HuggingFace, filtrando por tamaño, tipo de cuantización y compatibilidad de hardware declarada. Al seleccionar un modelo, aparecen las estimaciones de rendimiento en vuestra máquina: es aquí donde se entiende inmediatamente qué se puede esperar antes de descargar siquiera un solo gigabyte.

## Por qué Qwen 3.5 9B, y por qué Q8_0

Con el framework instalado, la elección del modelo es el segundo punto crítico. Elegí Qwen 3.5 9B en cuantización Q8_0 —el archivo ocupa poco más de 10 GB en disco— por razones que conviene explicar, ya que reflejan una lógica útil para cualquiera que se plantee esta elección.

El tamaño de 9 mil millones de parámetros se ha convertido en este periodo en el estándar de facto para las pruebas de campo: es el tamaño más común entre todos los principales competidores que lanzan modelos open-weight, representa el punto de equilibrio entre capacidad y requisitos de hardware, y permite comparaciones significativas entre diferentes familias. Las variantes de 27B y 35B son ciertamente más capaces, pero requieren un hardware más costoso que para un particular representa un salto no trivial. Para una empresa, aunque sea pequeña, evaluar un modelo de 9B tiene un doble valor: entender qué se obtiene de inmediato con una inversión mínima y proyectar qué se podría obtener con un escalón de hardware superior, dado el ritmo al que crece el rendimiento y bajan los requisitos.

La elección de la cuantización Q8_0, la más alta de las tres opciones disponibles en LM Studio para este modelo, fue posible precisamente gracias a los 16 GB de VRAM: el indicador verde confirmaba que el modelo funcionaría íntegramente en la GPU sin tener que descargar capas en la RAM del sistema, garantizando la máxima velocidad de inferenza y una calidad de respuesta no degradada por las aproximaciones numéricas de las cuantizaciones más agresivas.

A nivel técnico, Qwen 3.5 no es simplemente un modelo anterior reducido. Como se describe en la [documentación oficial en HuggingFace](https://huggingface.co/Qwen/Qwen3.5-9B), la arquitectura adopta un enfoque híbrido que combina Gated Delta Networks —una forma de atención lineal— con sparse Mixture-of-Experts, con el objetivo de abordar el "muro de la memoria" (memory wall) que típicamente limita a los modelos pequeños, garantizando un alto rendimiento con una latencia reducida. La ventana de contexto nativa es de 262.144 tokens, ampliable hasta aproximadamente un millón a través de YaRN. Y a diferencia de las generaciones anteriores que añadían capacidades visuales como módulos separados, Qwen 3.5 fue entrenado desde el principio con tokens multimodales: texto, imágenes y vídeo integrados mediante un proceso llamado early fusion.

El modelo admite dos modos de funcionamiento: *thinking* (pensamiento) y *non-thinking*. En el primero, antes de producir la respuesta, el modelo genera explícitamente una cadena de razonamiento interna, dedicando de 20 a 40 segundos de procesamiento antes de escribir la respuesta propiamente dicha. En el segundo, responde de inmediato. En todas las pruebas que siguen utilicé el modo thinking, ya que algunos prompts eran deliberadamente complejos. Realicé las mismas pruebas también desactivando el thinking: las respuestas pasan a ser inmediatas, la profundidad disminuye ligeramente en las preguntas más articuladas, pero para usos cotidianos, asistencia en la escritura, programación rutinaria, análisis de textos o preguntas informativas, la combinación de precisión y velocidad es más que satisfactoria. En ambos modos, la salida viajó a unos 30 tokens por segundo en esta configuración de hardware.
![grafico1.jpg](grafico1.jpg)
[Imagen tomada de huggingface.co](https://huggingface.co/Qwen/Qwen3.5-9B)

## Las pruebas: seis ensayos de campo

Las seis pruebas que siguen se diseñaron para cubrir las áreas principales de evaluación de los modelos de lenguaje: razonamiento científico avanzado, comprensión multimodal, generación de código complejo, capacidad multilingüe con planificación, gestión de contextos muy largos y razonamiento visuoespacial. Para cada prueba, se verificaron los resultados de Qwen 3.5 9B cruzando las respuestas con modelos de frontera como Claude y DeepSeek, no como una validación científica, sino como un control de validez práctico.

Las notas que acompañan a cada prueba son fruto de una valoración personal tras investigaciones en línea, cruzadas con las respuestas a los mismos prompts y las valoraciones de las respuestas proporcionadas por Qwen 3.5 9B, sometidas a Claude y DeepSeek. Es el juicio de un usuario exigente, no la sentencia de un benchmark.

### Prueba 1 — Razonamiento científico: el mecanismo de Higgs

La primera prueba era un clásico de los benchmarks de alto nivel: explicar el mecanismo de Higgs y la ruptura de la simetría electrodébil a un estudiante universitario de física. Una pregunta que requiere rigor matemático sin sacrificar la claridad, y la capacidad de construir un hilo narrativo que guíe al lector a través de conceptos no triviales.

La respuesta llegó estructurada en cinco secciones que avanzaban con la lógica de una lección bien impartida: desde el planteamiento del problema de la masa en los bosones de gauge, pasando por la introducción del campo de Higgs con su potencial de "sombrero mexicano" como imagen mental, hasta la explicación del mecanismo por el cual los bosones W y Z "beben" los bosones de Goldstone adquiriendo masa mientras que el fotón permanece sin masa gracias a la simetría residual. Cada fórmula iba acompañada de una interpretación física; cada paso técnico tenía una frase que revelaba su sentido físico profundo. Las verificaciones cruzadas con los modelos de frontera e investigaciones personales en línea confirmaron que la respuesta era correcta, estaba bien estructurada y empleaba las metáforas adecuadas. Nada mal para un modelo que funciona en un PC doméstico.

**Nota: 5/5.** Había rigor, había claridad. Lo que más sorprendió fue la capacidad de elegir metáforas apropiadas en lugar de limitarse a reproducir nociones.

### Prueba 2 — Multimodalidad: leer el caos visual

Para la segunda prueba, descargué de internet una imagen pequeña y de baja calidad que mostraba una hoja de cálculo con el inventario de una tienda de electrónica: nueve columnas con códigos de artículo, nombres de productos, fechas de compra, categorías, cantidades, costes y precios de venta. La imagen era deliberadamente mala, ligeramente desenfocada, y cargué el archivo directamente en LM Studio pidiendo al modelo que describiera lo que veía.

El modelo leyó todas las columnas y los valores numéricos, pero lo interesante vino después: notó de forma autónoma que la columna "Total" era el producto de la cantidad por el precio unitario, identificó algunos monitores con ventas cero interpretándolos como mercancía potencialmente no vendida, distinguió artículos de bajo coste como los ratones de productos premium como los procesadores, y reconoció que las fechas de compra abarcaban desde octubre de 2017 hasta diciembre de 2018. No se limitó a transcribir: interpretó los datos como lo haría un analista.

Algún detalle numérico menor se reportó de forma imprecisa, lo cual es comprensible dada la calidad de la imagen. Pero la capacidad de pasar de la lectura a la comprensión contextual es exactamente lo que distingue una multimodalidad decorativa de una multimodalidad funcional.

**Nota: 4.8/5.** La lectura fue correcta, el análisis de inteligencia de negocio añadido fue una bonificación inesperada. Se perdieron algunas décimas por alguna imprecisión numérica menor.

### Prueba 3 — Generación de código: un problema NP-hard

La tercera prueba fue sobre programación, el área donde los benchmarks sugieren que Qwen 3.5 9B es ligeramente menos brillante que otras. Pedí implementar en Python un algoritmo para encontrar el ciclo de longitud máxima en un grafo no dirigido, un problema NP-hard que requiere no solo capacidad de implementación sino conciencia teórica.

La primera respuesta se interrumpió a la mitad por un problema técnico de gestión de la salida larga, un comportamiento que debe señalarse honestamente. Tras instarle a completar, el modelo produjo una solución completa con backtracking y poda (pruning), el enfoque correcto para este tipo de problemas, con type hints, métodos bien separados y comentarios pertinentes. Pero el detalle que más impactó llegó antes incluso que el código: el modelo declaró explícitamente que el problema es NP-hard, que no se conoce un algoritmo de tiempo polinómico y que para grafos de gran tamaño se debería considerar un enfoque aproximado. Esta conciencia de los límites teóricos antes incluso de escribir el código es la señal de algo más profundo que la simple generación de sintaxis.

**Nota: 5/5.** El contratiempo inicial debe señalarse, pero la solución final y la madurez teórica demostrada superaron las expectativas para un modelo de 9 mil millones de parámetros.

---

*La entrega termina aquí. En la segunda parte: la prueba de planificación multilingüe, el desafío con un PDF de 460 páginas y el razonamiento visuoespacial sobre una habitación en caos. Además de las conclusiones sobre lo que significa realmente tener un asistente local en 2026.*
