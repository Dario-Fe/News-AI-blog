---
tags: ["Research", "Training", "Applications"]
date: 2026-03-20
author: "Dario Ferrero"
---

# El investigador duerme. Autoresearch: cómo Andrej Karpathy enseñó a las máquinas a investigar de forma autónoma
![autoresearch-karpathy.jpg](autoresearch-karpathy.jpg)

*Hay una escena en los videojuegos de rol japoneses, Karpathy los conoce bien, en la que el protagonista deja de luchar contra los monstruos solo y empieza a entrenar a otros personajes para que lo hagan en su lugar. El cambio lo transforma todo: ya no sois un luchador, sois un entrenador. Andrej Karpathy ha hecho algo parecido con la investigación en inteligencia artificial.*

Karpathy es una figura que no necesita mucha presentación en el sector, pero merece la pena encuadrarlo para quienes vienen de fuera. Exdirector de inteligencia artificial de Tesla, cofundador de OpenAI, hoy independiente y prolífico divulgador técnico: es conocido sobre todo por su capacidad para hacer accesibles conceptos densos y especializados. Su curso [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) es un punto de referencia para cualquiera que quiera entender los modelos de lenguaje sin tener un doctorado.

A principios de marzo de 2026, Karpathy publicó en GitHub un nuevo proyecto de código abierto llamado [autoresearch](https://github.com/karpathy/autoresearch). El repositorio ya cuenta con más de 23.000 estrellas y casi tres mil forks, cifras que en el mundo del desarrollo de software miden el interés con la misma precisión que un sismógrafo. La idea de fondo es sencilla de describir pero difícil de digerir: dar a un agente de inteligencia artificial un sistema de entrenamiento de modelos de lenguaje pequeño pero auténtico, y dejarlo experimentar por su cuenta, de noche, mientras el investigador duerme.

## Anatomía de un bucle nocturno

Para entender qué hace autoresearch, es útil imaginar el trabajo diario de un investigador de aprendizaje automático. Normalmente, esta persona se sienta frente al ordenador, formula una hipótesis («¿y si usara un tamaño de lote más pequeño?»), modifica manualmente el código de entrenamiento, lanza un experimento que dura horas, analiza los resultados y vuelve a empezar. Es un proceso serial, lento y limitado por las horas de la jornada laboral y la capacidad de concentración humana.

Autoresearch rompe este ciclo de forma radical. El sistema está construido en torno a solo tres archivos que realmente importan: `prepare.py` (que gestiona la preparación de los datos y nunca se modifica), `train.py` (el código del modelo, que el agente puede tocar en todas sus partes) y `program.md` (las instrucciones para el agente, escritas en lenguaje natural). El usuario humano no mete mano a los archivos Python: su tarea es escribir y refinar el archivo Markdown, es decir, *programar el programa* en lugar de programar directamente.

Una vez iniciado, el agente —en la configuración estándar se trata de Claude de Anthropic o de Codex de OpenAI— lee las instrucciones, propone una modificación al código de entrenamiento, ejecuta un experimento de una duración fija de exactamente cinco minutos, mide si el resultado ha mejorado, mantiene o descarta la modificación y repite. Doce experimentos por hora, unos cien a lo largo de una noche. Por la mañana, el investigador se despierta ante un registro detallado de todo lo que se ha probado y (con suerte) un modelo mejor.

La métrica utilizada para medir los progresos se llama `val_bpb`, o *validation bits per byte*: mide qué tan bien logra el modelo comprimir el texto, en términos de cuántos bits se necesitan para representar cada byte de datos. Es una métrica elegante porque es independiente del tamaño del vocabulario, lo que significa que los experimentos con diferentes arquitecturas siguen siendo comparables entre sí. Los valores más bajos indican un modelo más capaz.

Toda la base de código se desarrolla en unas 630 líneas de Python. No es una característica accesoria: es una elección filosófica. Karpathy ha construido deliberadamente un sistema que un solo desarrollador puede leer, entender y mantener bajo control. La revisión humana sigue siendo posible. Los diffs, las diferencias entre una versión del código y la siguiente, son legibles.

Para entender autoresearch a fondo, hay que conocer el proyecto del que nace: [nanochat](https://github.com/karpathy/nanochat), que Karpathy describe simplemente como «el mejor ChatGPT que cien dólares pueden comprar». No es una hipérbole de marketing: nanochat es un sistema completo y mínimo para entrenar modelos de lenguaje en una sola GPU, que cubre toda la cadena, desde la tokenización hasta el preentrenamiento, desde el ajuste fino (*fine-tuning*) hasta una interfaz de chat funcional.

Su motivo de orgullo es una tabla de clasificación pública que mide el tiempo necesario para replicar las capacidades del GPT-2 original (que en 2019 costó unos 43.000 dólares y semanas de cálculo) en hardware accesible: por el momento, el récord ha bajado a poco más de tres horas en un nodo con ocho GPUs H100, por un gasto de unos setenta dólares.

Autoresearch es, en esencia, la versión mongpu y centrada en el agente de nanochat: utiliza la misma base de código simplificada como campo de experimentación, con la misma métrica val_bpb como brújula, pero confía al agente la tarea de explorar ese territorio por su cuenta.

Entender nanochat significa entender sobre qué está trabajando realmente el agente, y por qué los resultados obtenidos en cinco minutos de entrenamiento autónomo pueden compararse, con cierta cautela, con los de las sesiones más exigentes de la tabla de clasificación principal.

## Lo que realmente dicen los números

La forma más honesta de evaluar autoresearch no es mirar la descripción del proyecto, sino los datos reales de los experimentos. Karpathy publicó en la [discusión #43](https://github.com/karpathy/autoresearch/discussions/43) del repositorio un relato detallado de una sesión completa, notablemente transparente: 126 experimentos realizados en una GPU NVIDIA H100 en un lapso de unas diez horas y media.

El punto de partida era un `val_bpb` de 0.9979. El punto de llegada: 0.9697. Una mejora de 0.0282 en términos absolutos, lo que en este contexto representa un salto significativo. Para orientarse: las modificaciones con más impacto fueron la reducción del tamaño del lote (de 524.000 a 262.000 tokens, lo que permitió realizar más pasos de actualización en los cinco minutos disponibles, ganando 0.0119 de mejora), la adición de una capa a la profundidad del modelo (0.0043) y una serie de ajustes más finos como la introducción de pequeños valores de regularización (*weight decay*) en los componentes de embedding.

Lo que llama la atención al leer el log completo no es solo el resultado final, sino la granularidad del proceso. El agente exploró sistemáticamente decenas de hipótesis, muchas de las cuales resultaron ser callejones sin salida: el *weight tying* entre embedding y de-embedding produjo una caída catastrófica de la métrica; la atención multi-query con una única cabeza de clave-valor resultó demasiado agresiva; las arquitecturas con más capas pero dimensiones reducidas terminaban por agotar el presupuesto de cinco minutos antes incluso de converger. Estos fallos documentados son casi más útiles que los aciertos, porque dibujan el mapa del territorio explorado.

Los resultados obtenidos en una GPU H100, la tarjeta gráfica con mejor rendimiento disponible actualmente para este tipo de cargas, se mostraron después transferibles a modelos más profundos de 24 capas, lo suficiente para competir en las clasificaciones de referencia del sector. No es un resultado trivial. Pero el límite de la transferibilidad aún no está claro, y este es uno de los límites del proyecto en los que merece la pena detenerse.
![grafico1.jpg](grafico1.jpg)
[Imagen tomada de github.com](https://github.com/karpathy/autoresearch)

## La otra cara de la moneda

Autoresearch ha recibido una acogida entusiasta, y el entusiasmo es comprensible. Pero un análisis honesto requiere mirar también hacia dónde muestra el sistema sus grietas.

El primer límite es estructural: el presupuesto fijo de cinco minutos por experimento, que es también uno de los puntos fuertes del proyecto, se convierte en un vínculo rígido cuando se exploran arquitecturas más complejas. En los datos de la sesión #43 se ve claramente: cada intento de añadir capas más allá de cierto umbral terminaba con un experimento incompleto, porque el tiempo se agotaba antes de que el modelo convergiera. El agente estaba buscando en un espacio de posibilidades bloqueado parcialmente por su propia arquitectura temporal.

El segundo límite se refiere al paralelismo. El sistema está diseñado para una sola GPU y los experimentos se ejecutan en secuencia, no en paralelo. Significa que mientras un experimento gira, ningún otro puede iniciarse. Quienes tuvieran acceso a un clúster de GPUs podrían querer explorar más direcciones simultáneamente; autoresearch, por elección deliberada, no lo admite. Karpathy es transparente al respecto: es una decisión de diseño, no un olvido. Pero la consecuencia práctica es que la exploración del espacio de investigación sigue siendo fundamentalmente lineal.

Tercer punto crítico: la dependencia de modelos propietarios. Para ejecutar los experimentos en modo autónomo, se necesita un agente capaz, y en la configuración estándar se habla de Claude o Codex, ambos sistemas comerciales. Quienes quieran democratizar la investigación en inteligencia artificial podrían encontrar paradójico que una herramienta pensada para bajar las barreras de entrada requiera de todos modos una suscripción a servicios de terceros.

Hay también un aspecto más sutil, que se refiere a la naturaleza misma de las elecciones que realiza el agente. autoresearch es excelente en la optimización local: encuentra el mejor punto en la cercanía del punto de partida, a través de una secuencia de pequeños pasos. Pero no es un sistema diseñado para dar saltos conceptuales. La revisión de la literatura, la formulación de hipótesis radicalmente nuevas, la comprensión de por qué un enfoque funciona a nivel teórico, todo esto sigue siendo territorio humano, al menos por ahora. La investigación verdadera, la que cambia los paradigmas, no es solo un proceso de optimización secuencial.

Finalmente, está la cuestión de la explicabilidad. Cuando el agente descubre que una inicialización de los pesos reducida a 0.68x del valor estándar produce mejores resultados, no proporciona una explicación causal de esta mejora. Sabe que funciona, no por qué funciona. Para quienes usan los resultados como punto de partida para investigaciones posteriores, esta falta de comprensión es una deuda técnica que antes o después hay que saldar.

## El humano que programa el programa

Una de las ideas más interesantes, y menos discutidas, de autoresearch es el papel que asigna al ser humano en el proceso. No se trata de eliminarlo, sino de desplazarlo.

El archivo `program.md` se describe en el README como una «skill» ultraligera: un documento en lenguaje natural que define los objetivos del agente, sus prioridades, los límites dentro de los cuales operar. El usuario ya no escribe Python, escribe instrucciones. No modifica el código de entrenamiento, modifica el documento que dice al agente cómo modificar el código de entrenamiento. Es un nivel de abstracción más, y trae consigo consecuencias concretas.

Por un lado, esto baja enormemente el umbral de entrada. No hace falta un doctorado en aprendizaje automático para iniciar una sesión de autoresearch. El README incluye una «Weekend Guide», una guía para el fin de semana, que promete llevar a cualquiera desde la configuración inicial hasta los primeros experimentos autónomos sin un bagaje especializado. La simplicidad técnica de la configuración (una sola GPU NVIDIA, Python 3.10 o superior y el gestor de paquetes `uv`) es real.

Por otro lado, esta abstracción crea una nueva dependencia. Quien escribe las instrucciones en `program.md` determina el espacio de exploración del agente. un documento mal escrito, con objetivos vagos o límites contradictorios, produce sesiones de investigación igualmente vagas. El cuello de botella se desplaza: en lugar de requerir competencias en la escritura de código, autoresearch requiere competencias en la escritura de instrucciones eficaces para sistemas de inteligencia artificial, una disciplina relativamente nueva, todavía carente de estándares consolidados.

Hay algo recursivo en todo esto, y Karpathy es consciente de ello. En el README del proyecto ha insertado un epígrafe deliberadamente ambiguo, que describe un futuro hipotético en el que enjambres de agentes autónomos gestionan clústeres de cálculo en una investigación continuamente auto-modificable, con una base de código en la diezmilésima duodécima generación «crecida más allá de la comprensión humana». Es un tono entre lo distópico y la broma de nerd, pero el hecho de que esa frase abra el documento de presentación de un proyecto real no es casual.

## A dónde lleva este camino

La comparación más inmediata para autoresearch es con AutoML, los sistemas que en los últimos años han intentado automatizar la elección de las arquitecturas neuronales y de los hiperparámetros. Pero hay una diferencia sustancial: AutoML tradicional opera en espacios de investigación predefinidos, buscando la combinación óptima entre opciones ya enumeradas. autoresearch deja que el agente modifique libremente cualquier parte del código, incluyendo arquitectura, optimizador, tamaño del lote, esquema de aprendizaje, prácticamente todo. El espacio de exploración es mucho más grande y mucho menos estructurado.

Esto abre posibilidades interesantes, pero también preguntas incómodas. Si el sistema funciona realmente, si agentes autónomos pueden realizar investigación significativa sobre modelos de lenguaje sin supervisión continua, ¿dónde se detiene este proceso? La respuesta honesta es que nadie lo sabe con certeza. El proyecto está pensado explícitamente para ser el punto de partida de algo más grande, y el propio Karpathy indica la dirección hacia configuraciones multi-agente asíncronas, donde múltiples instancias paralelas exploran direcciones diferentes en clústeres distribuidos.

Desde el punto de vista ético, este escenario merece atención. La aceleración de los ciclos de investigación es deseable si conduce a modelos mejores y más seguros. Pero la misma aceleración, aplicada sin una supervisión adecuada, puede amplificar sesgos algorítmicos ya presentes en los datos de entrenamiento, producir optimizaciones que maximizan métricas medibles a expensas de cualidades no medibles, o hacer que el proceso sea lo suficientemente opaco como para escapar a cualquier forma de control significativo.

El hecho de que autoresearch sea de código abierto y minimalista es, en este sentido, una garantía parziale. El código es lo suficientemente corto como para ser auditado, los datos de los experimentos son públicos. Pero a medida que el sistema escala, hacia clústeres multi-GPU, hacia sesiones más largas, hacia agentes que perfeccionan sus propias instrucciones, la supervisión se vuelve más difícil.

Hay finalmente una consideración pragmática que se refiere a quienes evalúan esta herramienta para un uso profesional. autoresearch en su forma actual es un prototipo refinado, no un sistema de producción. Requiere hardware específico (GPU NVIDIA, con soporte óptimo para H100), depende de APIs externas para el agente y produce resultados que deben ser interpretados con competencia para ser útiles. La promesa de la «guía del fin de semana» es real para quienes quieren experimentar, pero no sustituye la comprensión básica de cómo funciona el entrenamiento de los modelos de lenguaje.

Dicho esto, el valor de autoresearch no se mide solo por lo que hace hoy, sino por lo que demuestra que es posible. Muestra que la investigación automatizada en sistemas reales —no simulaciones simplificadas, no benchmarks artificiales— ya está al alcance de cualquiera que tenga una sola GPU y la curiosidad de explorar. Y lo hace con una transparencia metodológica, la de los logs públicos y el código legible, que muchos laboratorios de investigación bien financiados no se permiten.

El investigador que duerme, mientras tanto, ya se ha despertado. Ha encontrado 126 experimentos que esperan ser leídos.
