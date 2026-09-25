---
tags: ["Generative AI", "Training", "Startups"]
date: 2026-09-30
author: "Dario Ferrero"
---

# Empero y la destilación: he probado su Qwen3.8-35B-A3B
![empero-qwen38-35b.jpg](empero-qwen38-35b.jpg)

*Cuando un laboratorio independiente promete trasvasar el razonamiento de un modelo de frontera dentro de un archivo para descargar y ejecutar en vuestro propio PC, la pregunta correcta no es si lo ha conseguido sobre el papel, sino cuánto de esa promesa se mantiene en pie cuando el archivo termina de verdad dentro de la RAM de una máquina de consumo. Es la pregunta que ha guiado también las entregas anteriores de esta serie, desde [Qwen 3.5 9B](https://aitalk.it/it/qwen3.5-locale-puntata1.html) pasando por [Qwen 3.6 35B](https://aitalk.it/it/qwen36-35b-ai.html), y que hoy regresa con un protagonista diferente: no un modelo oficial de un laboratorio multimillonario, sino un proyecto alemán llamado [Empero](https://empero.org/) y uno de sus destilados, [Qwen3.8-35B-A3B-Distill](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill).*

## Un laboratorio alemán contra la nube

Empero se describe como un laboratorio de investigación independiente con sede en Alemania, dedicado a construir modelos lingüísticos lo bastante eficientes como para poder funcionar en hardware propiedad del usuario, sin pasar por una API de terceros. No es un eslogan aislado: en la sección de su sitio web dedicada a las empresas europeas se explica que cada vez más compañías no pueden enviar datos regulados hacia una API extranjera, y que un modelo Apache-2.0 ejecutable en local, verificable hasta en sus pesos, responde exactamente a esa restricción. Es una posición de mercado antes que técnica, y conviene tenerla presente al leer los números que siguen.

El ecosistema que Empero ha construido en torno a esta filosofía es más amplio que el modelo concreto que voy a probar hoy. Existen familias de destilados a partir de Qwen3.8, disponibles en tamaños de 2, 4 y 9 mil millones de parámetros además del de 35B que utilizaremos hoy; está la línea Qwythos con más de un millón de descargas en Hugging Face; hay un agente de programación para terminal llamado [Abacus](https://github.com/empero-org/abacus) pensado para trabajar con puntos de enlace (endpoints) locales o remotos; y existen herramientas internas de investigación como `rethink` para generar trazas de razonamiento, `SFTSuite` para organizarlas en planes de estudio (curricula) y `Microverse` para explorar nuevas configuraciones arquitectónicas antes de lanzar un entrenamiento completo. La imagen, en suma, no es la de un ajustador fino (fine-tuner) aislado, sino la de una cadena de valor que Empero reivindica como controlada de principio a fin (end to end).

Para la configuración de hardware y software de estas pruebas —procesador AMD Ryzen 7700, 32 GB de RAM DDR5, GPU AMD Radeon RX 9060 XT con 16 GB de VRAM, LM Studio como entorno de ejecución (runtime)—, remito a la [primera entrega de la serie](https://aitalk.it/it/qwen3.5-locale-puntata1.html), que sigue siendo la referencia metodológica para quienes llegáis ahora.

## Qué promete (y qué no) el último destilado

Según la ficha técnica oficial (model card), Qwen3.8-35B-A3B-Distill nace de la destilación de los modelos de frontera Qwen3.8 dentro de la arquitectura Mixture-of-Experts de Qwen3.6-35B-A3B, entrenado sobre trazas seleccionadas de los modelos docentes que abarcan cadena de pensamiento (chain-of-thought) en matemáticas, código, razonamiento general, seguimiento de instrucciones y uso de herramientas, filtradas por calidad antes del entrenamiento. Los docentes indicados son dos variantes internas de Qwen3.8: una de 2,4 billones de tokens y otra denominada Flash Next. Cada respuesta comienza con un bloque de pensamiento aprendido directamente de las trazas del docente, no generado de forma autónoma por el estudiante: es la diferencia, declarada por la propia Empero, entre memorizar las jugadas de un maestro e improvisarlas uno mismo, un poco como el protagonista de *Vagabond*, el manga de Takehiko Inoue, que construye su propio estilo pasando de escuela en escuela en lugar de inventárselo de la nada.

Los números de las pruebas comparativas (benchmarks), sin embargo, deben leerse con más cautela de la que sugiere el comunicado. Comparado con el modelo base Qwen3.6-35B-A3B, el destilado de Empero muestra un MMLU prácticamente invariable (0,838 frente a 0,834), una diferencia que la propia documentación técnica ubica dentro del margen de error estadístico. Donde la mejora es más clara es en ARC-Challenge (pasando de 0,548 a 0,582) y en ARC-Easy (pasando de 0,819 a 0,830). Es una ganancia real pero selectiva, no una superioridad generalizada: la pregunta abierta es si un progreso concentrado en estos dos benchmarks se traduce en una ventaja perceptible en el uso diario o se queda confinado a esa batería de pruebas específica.
![tabella1.jpg](tabella1.jpg)

Conviene aclarar también qué parte de este paquete no es una invención de Empero. La arquitectura Mixture-of-Experts no nace con ellos; la destilación a partir de modelos más grandes es una técnica ya extendida por todo el sector; y el formato GGUF es un estándar del ecosistema local utilizado ya por docenas de otros proyectos. Lo que Empero reivindica como propio no es, por tanto, un ingrediente único, sino el control directo sobre toda la cadena de valor que los combina: desde la generación de trazas hasta una técnica de postentrenamiento llamada FTPO, diseñada para corregir comportamientos no deseados como bucles de repetición sin tener que rehacer un entrenamiento completo. Si esto basta para justificar la etiqueta de "especial" sigue siendo, legítimamente, una pregunta que cada lector puede responderse por sí mismo.

## El modelo en el banco de pruebas: arquitectura y pesos

El archivo probado se llama [Qwen3.8-35B-A3B-Distill](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill), construido sobre el modelo base Qwen3.6-35B-A3B y distribuido con licencia Apache-2.0. La arquitectura es híbrida: cuarenta capas en total, organizadas en diez ciclos compuestos por tres capas Gated DeltaNet (una forma de atención lineal) seguidas de una capa de atención completa, sumando diez capas de atención completa sobre cuarenta. El enrutamiento de expertos involucra 256 expertos enrutados más un experto compartido, con ocho expertos activos por cada token generado. Es la misma lógica de orquestación parcial relatada en la reseña de Qwen 3.6, pero aplicada aquí por Empero partiendo de esos pesos para aplicar sobre ellos un SFT fuera de política (off-policy) sobre las trazas del docente Qwen3.8: no es un entrenamiento desde cero, sino un modelo que lleva consigo un conocimiento destilado de trazas de un docente mucho mayor.

El punto que conviene reiterar, porque es fácil malinterpretarlo, es que los aproximadamente 3 mil millones de parámetros activos por token afectan al cálculo, no a la memoria. El archivo entero, con sus 35 mil millones de parámetros totales, debe cargarse por completo en RAM o VRAM antes de que pueda comenzar la inferencia. Las cuantizaciones disponibles en el [repositorio GGUF](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill-GGUF) van desde los 12,5 GB de la IQ2_M hasta los 71 GB de la BF16 completa.
![tabella2.jpg](tabella2.jpg)

Para esta prueba he elegido la Q5_K_M (25,348 GB en disco), que la ficha técnica indica como utilizable con unos 32 GB de VRAM o 48 GB de RAM para un funcionamiento cómodo. En mi hardware —16 GB de VRAM y 32 GB de RAM DDR5—, esto significa necesariamente un compromiso entre la GPU y la RAM del sistema, exactamente el tipo de equilibrio precario ya explorado con Qwen 3.6.

## Instalarlo y ejecutarlo en local

El entorno de ejecución (runtime) requerido debe estar actualizado: una compilación reciente de `llama.cpp` con soporte para la arquitectura Qwen3.6 y capas Gated DeltaNet MoE, condición que el [repositorio GGUF](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill-GGUF) señala explícitamente, ya que compilaciones más antiguas simplemente no cargan el modelo. LM Studio, Ollama, Jan y KoboldCpp figuran como compatibles. Para quien no haya instalado nada todavía, el procedimiento sigue siendo el descrito en la [primera entrega de la serie](https://aitalk.it/it/qwen3.5-locale-puntata1.html): descarga del instalador desde lmstudio.ai, sin dependencias que configurar a mano y con detección automática de la aceleración por hardware disponible.

Los parámetros de inferencia recomendados por la ficha técnica son temperatura 0,6, top-p 0,95 y top-k 20, con el bloque de pensamiento incorporado en la plantilla de chat (para ocultarlo opcionalmente en aplicaciones orientadas al usuario final). En mi configuración he trabajado con un contexto de 80.640 tokens, lejano de los 262.144 nativos pero suficiente para la mayoría de las pruebas previstas, descarga (offload) a la GPU de 22 capas sobre 41, 8 hilos de CPU sobre 8 disponibles, tamaño de lote (batch size) de evaluación en 2048, tamaño de lote físico en 512 y un máximo de 4 predicciones concurrentes. Es una configuración pensada para un uso realista en hardware de gama media-alta, no para exprimir hasta el último token por segundo disponible.

## Diez pruebas, una nota media

La batería de pruebas calca la de las entregas anteriores, con la adición de dos pruebas pensadas para poner a prueba la parte agéntica y conversacional del modelo.

Sobre el mecanismo de Higgs y la ruptura de la simetría electrodébil, el modelo produjo una explicación en cuatro secciones lógicas, con fórmulas correctas y especial atención a la razón por la que el fotón permanece sin masa: nota 5/5, a 26,13 tokens por segundo.

En la prueba de multimodalidad —una imagen de baja calidad con un panel de control (dashboard) de Excel—, el modelo leyó correctamente la estructura y los valores, identificó patrones estacionales y la diferencia entre 2017 y 2018, y ofreció recomendaciones concretas sobre la caída de junio: nota 5/5, a 24,4 tokens por segundo.

En la generación de código —un problema NP-hard de búsqueda del ciclo máximo en un grafo—, propuso tres enfoques complementarios: uno exacto con backtracking, uno aproximado sobre un árbol de expansión (spanning tree) y una versión acotada como compromiso, con código limpio y comentado: nota 5/5, a 26,64 tokens por segundo (la velocidad más alta de todas las pruebas).

En la planificación multilingüe —un itinerario de cinco días en Japón en francés e italiano—, el francés fue fluido, pero aparecieron un par de imprecisiones logísticas (Shinjuku Gyoen confundido con un mercado de comida callejera, JR East en lugar de JR Central para el Shinkansen): nota 4,5/5, a 23,38 tokens por segundo.

En contexto largo —un PDF de 460 páginas sobre el crecimiento de la generación de vídeo—, el modelo señaló con precisión las páginas 126 y 127, citando cifras específicas y modelos clave del sector al primer intento: nota 5/5, a 22,8 tokens por segundo.

En razonamiento espacial —una fotografía de una habitación desordenada—, la respuesta fue correcta pero superficial, sin detalles sobre colores y con una justificación de la estrategia de ordenación poco clara: nota 3,8/5, a 21,24 tokens por segundo (el único punto débil real de la batería).

En la prueba de agente multipaso —planificación de una app web—, produjo un stack tecnológico completo, un esquema de base de datos en Prisma, una hoja de ruta en seis sprints y una sección dedicada a riesgos y mitigaciones con tabla de probabilidad e impacto: nota 5/5, a 23,38 tokens por segundo.

En la conversación larga de cuatro turnos, mantuvo coherencia plena sobre todas las elecciones técnicas anteriores, proponiendo una arquitectura con Socket.IO y Redis y una estrategia de escalabilidad hasta diez mil usuarios: nota 5/5, con una velocidad media en torno a 22,8 tokens por segundo.

En el planificador estratégico trienal, elaboró un plan en seis semestres completo con objetivos, KPI medibles y asignación de un presupuesto de diez millones de dólares: nota 5/5, a 22,71 tokens por segundo.

En el analista de datos abstracto —un problema de lógica con tres premisas contradictorias que formalizar—, identificó la contradicción y justificó la elección de la premisa a corregir con tres argumentos sólidos: nota 5/5, a 23,63 tokens por segundo.
![tabella3.jpg](tabella3.jpg)

La nota media global fue de 4,83 sobre 5, con una velocidad media en torno a los 23,7 tokens por segundo (la más alta registrada hasta ahora en la serie). Comparado con un modelo denso de la misma familia (el Qwen3.8-27B ya probado en una entrega anterior), la diferencia de velocidad es acusada, situándose en unas cuatro o cinco veces más rápido a igualdad de calidad percibida en las respuestas. Es exactamente la distancia que las arquitecturas MoE prometen sobre el papel y que aquí parece traducirse en la práctica.
![tabella4.jpg](tabella4.jpg)

## Cuánto sostiene la promesa en Q5

Volviendo a la pregunta inicial: ¿cuánto de las capacidades transferidas por el docente Qwen3.8 permanece efectivamente disponible cuando el modelo se comprime en Q5_K_M y se ejecuta con 22 capas en la GPU y el resto en la RAM del sistema? Las diez pruebas sugieren que la mayor parte se mantiene, con una excepción clara en el razonamiento visuoespacial fino y un matiz más sutil en la precisión geográfica en contextos multilingües. Sin embargo, si esto basta para considerar al modelo superior a su propio modelo base es algo discutible según los benchmarks oficiales: la ganancia está concentrada en ARC, no generalizada, y el MMLU permanece de hecho idéntico.

Existe además una pregunta de alcance más amplio para el usuario. Un archivo de 25 GB que requiere 16 GB de VRAM y satura buena parte de la RAM del sistema está al alcance de un particular interesado, pero ¿es realista imaginarlo como un estándar para quien no ha invertido previamente en hardware dedicado? Y al elegir entre una API en la nube y un modelo local como este, ¿cuánto pesa el hecho de que los datos no abandonen jamás la propia máquina, un argumento que Empero sitúa en el centro de su oferta comercial dirigida a las empresas europeas? Son preguntas que exigen respuestas diferentes según quien las formule, y quizás sea este el punto más interesante de todo el experimento de Empero: no tanto si el modelo gana o pierde frente a su predecesor, sino si toda la cadena de valor que promete —desde la destilación hasta el empaquetado GGUF y Abacus como herramienta de uso diario— logra hacer del entorno local una opción practicable, y no solo un ejercicio para entusiastas con una buena GPU en casa.

*Nota técnica: todos los datos sobre arquitectura, cuantizaciones y benchmarks citados en este artículo proceden de las fichas oficiales en Hugging Face y del sitio web de Empero, enlazados en el texto. Las puntuaciones y velocidades de generación en las diez pruebas son mediciones personales, no certificaciones automatizadas de benchmarks, y deben leerse como tales.*
