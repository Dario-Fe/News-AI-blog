---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-05-01
author: "Dario Ferrero"
---

# ¿Más agentes, menos inteligencia? Stanford cuestiona la arquitectura multiagente
![agenti-multipli-stanford.jpg](agenti-multipli-stanford.jpg)

*Hay una escena de culto en "Primer", la película de ciencia ficción de bajo presupuesto de Shane Carruth, en la que dos ingenieros construyen una máquina del tiempo en el garaje de su casa convencidos de que cuantos más componentes añadan, mejor funcionará. Luego descubren, de la manera más dolorosa posible, que la complejidad no es sinónimo de potencia: es solo complejidad. La industria de la inteligencia artificial está atravesando en este momento una crisis filosófica similar, aunque decididamente menos temporal, respecto a los sistemas multiagente. Y un artículo, publicado por dos investigadores de Stanford en abril de 2026, tiene el mérito de poner el dedo exactamente en la llaga.*

El título del artículo: [*Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets*](https://arxiv.org/abs/2604.02460), es de esos que no dejan lugar a la interpretación. Un solo agente, en las condiciones adecuadas, supera a un sistema multiagente. No siempre, no en todas partes, no por razones triviales. Pero lo supera.

## Qué es un agente y por qué de repente se necesitan cada vez más

Antes de entender por qué el artículo es relevante, vale la pena detenerse un momento en qué entendemos cuando decimos "agente" en el contexto de los grandes modelos lingüísticos. Un agente, en este contexto, es simplemente una instancia de un modelo lingüístico a la que se le encomienda una tarea: recibe un texto de entrada, una pregunta, un problema, una instrucción, "razona" sobre ello y produce una respuesta. Eso es todo. El modelo piensa, responde, fin.

Un sistema multiagente es, en cambio, una tubería (pipeline) en la que varios de estos agentes trabajan juntos, viendo cada uno solo una parte del problema o una porción de la información disponible, y comunicándose a través de texto generado. Por lo general, hay un planificador que descompone el problema en subproblemas, un conjunto de trabajadores especializados que abordan cada uno su propia parte, y un agregador que sintetiza las respuestas parciales en una respuesta final.

La idea intuitiva es potente: divide y vencerás. Parece casi obvio que distribuir una tarea compleja entre agentes especializados debería producir mejores resultados que los que puede lograr una sola mente. Es exactamente la misma lógica que nos lleva a pensar que una orquesta suena mejor que un solista, que un equipo de cirujanos opera mejor que uno solo, que un colectivo creativo produce más que un individuo aislado. Y en muchos contextos es cierta. El problema es que con los modelos lingüísticos, la comparación casi siempre se hace de forma incorrecta.

## El truco de la cuenta oculta

Cuando un sistema multiagente parece superar a un solo agente, casi siempre hay una razón muy sencilla detrás: ha utilizado más recursos computacionales. No es una arquitectura mejor. Es solo que ha "pensado" más, en el sentido literal del término: ha generado más tokens de razonamiento intermedio.

Los modelos lingüísticos modernos, en particular los de "razonamiento" como DeepSeek, Gemini o Qwen, producen un flujo de pensamiento interno antes de responder, los llamados *thinking tokens*, o tokens de pensamiento. Estos tokens no aparecen en la respuesta final, pero son el medio por el cual el modelo razona paso a paso antes de producir el resultado. Son computacionalmente costosos, y el número de tokens que un modelo utiliza internamente es directamente proporcional a la calidad de las respuestas en tareas complejas.

Ahora, el problema es que en un sistema multiagente cada agente tiene su propio presupuesto de tokens de razonamiento. Si tenéis cinco agentes y cada uno piensa durante mil tokens, el sistema ha consumido cinco mil tokens de razonamiento en total. Si luego comparáis este sistema con un solo agente al que solo le habéis dado mil, estáis haciendo una comparación desigual. Es como comparar a un atleta que entrena cinco horas al día con uno que entrena una hora, y luego sorprenderos de que el primero corra más rápido.

Este es exactamente el punto que Dat Tran y Douwe Kiela de Stanford decidieron abordar con rigor metodológico. Su enfoque es simple: imponed un presupuesto total de tokens de pensamiento igual para todos los sistemas, y luego medid quién se desenvuelve mejor. No tokens de prompt, no tokens de salida, solo tokens de razonamiento intermedio. Luego observad qué sucede.

## El terreno de prueba: preguntas en cadena y respuestas que requieren varios pasos

Los investigadores eligieron dos benchmarks específicos para sus experimentos. El primero es [FRAMES](https://arxiv.org/abs/2409.12941), un conjunto de datos diseñado para probar la capacidad de recuperar y sintetizar información de múltiples fuentes. El segundo es [MuSiQue](https://arxiv.org/abs/2108.00573), filtrado para incluir solo las preguntas de cuatro saltos, es decir, aquellas que requieren concatenar cuatro pasos de razonamiento distintos para llegar a la respuesta correcta. Del tipo: "¿En qué país se encuentra la ciudad natal del director de la película que ganó el premio X en el año en que nació el autor del libro Y?" No es un ejemplo real, pero da una idea de la complejidad: cada respuesta está vinculada a la anterior, y equivocar un eslabón significa perder toda la cadena.

Las familias de modelos utilizadas son tres: Qwen3-30B, DeepSeek-R1-Distill-Llama-70B, Gemini 2.5 Flash y Gemini 2.5 Pro. Los presupuestos de tokens de pensamiento probados van de 100 a 10.000, a través de seis niveles. Y las arquitecturas multiagente comparadas son cinco, todas descritas en detalle en el artículo: la Secuencial (un planificador que divide el problema en pasos, agentes que ejecutan en serie, un agregador final), la Paralela por Subtareas (misma lógica pero los trabajadores operan en paralelo), la de Roles Paralelos (un resolutor, un extractor de hechos, un escéptico y un segundo resolutor que operan en paralelo), el Debate (dos agentes se enfrentan y luego se critican mutuamente) y, finalmente, el Ensemble (varios agentes responden de forma independiente y un juez elige la mejor respuesta).

La arquitectura más interesante desde un punto de vista teórico es la Secuencial, porque es la comparación más limpia con el agente único: ambos abordan el problema de forma serial, ambos usan el mismo presupuesto total, la única diferencia es que en el sistema multiagente el razonamiento intermedio se externaliza en mensajes explícitos entre agentes, mientras que en el agente único permanece latente dentro de una cadena continua de pensamiento.

## La matemática que nos dice por qué el agente único debería ganar

Antes de mirar los números, los investigadores construyen un argumento teórico que merece ser comprendido, porque tiene implicaciones que van mucho más allá de este artículo específico.

El argumento se basa en la "Desigualdad de Procesamiento de Datos", un resultado clásico de la teoría de la información. En palabras muy sencillas, dice lo siguiente: cualquier transformación que apliquéis a una información, no podéis aumentar la cantidad de información que esta contiene sobre la respuesta que estáis buscando. Solo podéis conservarla o perderla.

En el contexto de los sistemas multiagente, esto se traduce en una observación directa: los mensajes que un agente pasa al siguiente agente son una función del contexto original. Esa función no puede crear información de la nada. Por lo tanto, el contexto original, visto en su totalidad por un solo agente, contiene siempre al menos tanta información útil como cualquier mensaje extraído de él. Cada vez que una información se "resume" y se pasa de un agente a otro, algo se pierde inevitablemente. La comunicación es siempre un embudo.

El corolario práctico es inmediato: si un solo agente puede ver todo el contexto disponible y tiene el mismo presupuesto computacional que un sistema multiagente, no hay ninguna razón teórica por la que el sistema multiagente deba hacerlo mejor. Podría hacerlo igual. No mejor.

Pero hay una excepción, y es donde el artículo se vuelve realmente interesante.
![tabella1.jpg](tabella1.jpg)
[Imagen tomada de arxiv.org](https://arxiv.org/abs/2604.02460)

## Cuando el contexto está degradado: el único caso en el que los multiagente recuperan terreno

La garantía teórica del agente único vale solo si el agente único utiliza el contexto de manera perfecta. Y los modelos lingüísticos modernos no lo hacen. Hay fenómenos bien documentados en la literatura, desde la dilución de la atención hasta el llamado "lost in the middle", es decir, el hecho de que los modelos tienden a recordar mejor la información al principio y al final de un contexto largo que en medio, que muestran cómo la capacidad de usar eficientemente un contexto muy largo no es algo garantizado.

Los investigadores formalizan esto como "degradación del contexto" y lo modelan experimentalmente a través de cuatro modalidades: eliminación de partes del texto relevante, enmascaramiento de información clave, sustitución por texto incorrecto e inserción de distractores engañosos. Al aumentar el nivel de degradación, la garantía teórica del agente único se debilita, porque el agente único ya no opera sobre el contexto íntegro sino sobre una versión ruidosa de él. En este caso, un sistema multiagente bien diseñado puede compensar parcialmente ese ruido a través de la estructuración del trabajo: diferentes agentes que ven diferentes partes, que se verifican entre sí, que filtran el ruido a través de varios pasos.

El punto crucial es "parcialmente". Incluso en condiciones de degradación severa, los sistemas multiagente no se vuelven dominantes de forma clara: se vuelven *comparables* al agente único. La ventaja del agente único se reduce, pero no se invierte con continuidad.

## Los números, que son la parte incómoda

La Tabla 1 del artículo, que cubre 192 combinaciones de modelo, benchmark, presupuesto y arquitectura, es de esas que se miran con cierta lentitud. No porque los resultados sean ambiguos, sino porque la complejidad es real y merece respeto.

El resultado principal es que, a igual presupuesto de tokens de pensamiento, el agente único (SAS) es la arquitectura más fuerte o estadísticamente indistinguible de la mejor arquitectura en prácticamente todos los casos por encima del presupuesto mínimo de 100 tokens. Con 100 tokens el modelo no produce ningún razonamiento útil, ni como agente único ni como multiagente, por lo que ese nivel no dice nada interesante.

Mirando los presupuestos intermedios y altos, el patrón es estable. A 1.000 tokens de pensamiento, por ejemplo, el promedio entre todos los modelos y conjuntos de datos es 0,418 para SAS frente a 0,379 para la Secuencial, 0,369 para la Paralela y 0,333 para el Ensemble. A 2.000 tokens, 0,421 para SAS frente a 0,389 para la Secuencial. A 5.000 tokens, 0,427 para SAS frente a 0,386 para la Secuencial. La distancia tiende a no amplificarse ni a desaparecer al aumentar el presupuesto, sino que permanece consistente.

Hay excepciones: con Gemini 2.5 Pro a presupuestos bajos, el sistema Secuencial y el Debate tienen números competitivos, a veces ligeramente superiores. Pero estos casos se explican en parte por un artefacto técnico específico de Gemini que merece mención aparte.

## El problema de Gemini y la contabilidad opaca de tokens

Una de las secciones de diagnóstico más interesantes del artículo se refiere a Gemini 2.5 y revela algo bastante incómodo sobre la forma en que las API de estos modelos funcionan en la práctica.

Cuando se establece un presupuesto de tokens de pensamiento para Gemini a través de la API, el número de tokens de pensamiento realmente "visibles", es decir, que aparecen en el texto de respuesta, tiende a ser mucho menor que el presupuesto solicitado en el caso del agente único. Los investigadores muestran que Gemini parece "pensar internamente" de forma opaca, produciendo menos texto de razonamiento visible de lo que permitiría el presupuesto, mientras que en un sistema multiagente con múltiples llamadas a la API la cantidad total de pensamiento visible es mayor, simplemente porque hay más llamadas que extraen texto de razonamiento.

Esto significa que, para Gemini, las comparaciones con un presupuesto nominal igual no son del todo fiables: el agente único podría estar usando en realidad *menos* cómputo efectivo del solicitado, mientras que el sistema multiagente usa más a través de las múltiples llamadas. Es una irregularidad en la forma en que Gemini gestiona internamente los tokens de pensamiento, no una ventaja arquitectónica del multiagente.

Para compensar esto, los investigadores desarrollaron la variante SAS-Lm "Longer Thinking", que añade al prompt del agente único una instrucción estructurada: antes de responder, identifica las ambigüedades, propone interpretaciones, evalúalas y luego responde. Este pequeño cambio empuja a Gemini a producir más texto de razonamiento visible, acercando el cómputo efectivo al nominal. El resultado es que SAS-L mejora significativamente en Gemini 2.5 Flash y Pro, mientras que tiene efectos insignificantes o neutros en Qwen3 y DeepSeek, donde el problema de la contabilidad opaca no existe. Para Gemini 2.5 Flash en MuSiQue, SAS-L es la arquitectura más fuerte en todos los rangos de presupuesto. Un dato significativo.

## La fragilidad de los benchmarks: la prueba de la paráfrasis

Hay otro análisis del artículo que merece atención, porque toca una cuestión metodológica que aflige a toda la literatura sobre modelos lingüísticos: ¿cuánto dependen los resultados de la formulación exacta de las preguntas?

Los investigadores llevaron a cabo un estudio de ablación con paráfrasis: reescribieron las preguntas de los benchmarks con términos diferentes pero significado equivalente, y luego midieron cuánto cambiaban los resultados. La respuesta es: bastante. La precisión de los modelos cambia de forma no despreciable cuando se parafrasean las preguntas, lo que sugiere que parte de los resultados depende de que los modelos "reconocen" las preguntas de los benchmarks, es decir, han visto formulaciones similares o idénticas durante el entrenamiento, y las responden parcialmente por memoria más que por razonamiento puro. Este fenómeno, conocido como *benchmark contamination* o memorización, es un problema transversal a toda la evaluación de modelos lingüísticos, y el artículo lo señala honestamente como una limitación.

La buena noticia es que la contaminación parece distribuirse de forma relativamente uniforme entre SAS y MAS: no es que los sistemas multiagente se beneficien sistemáticamente más que el agente único, o viceversa. Pero es una advertencia para no tomar los números absolutos de precisión como una verdad definitiva.
![grafico1.jpg](grafico1.jpg)
[Imagen tomada de arxiv.org](https://arxiv.org/abs/2604.02460)

## El límite honesto: FRAMES y MuSiQue no son el mundo real

El artículo es riguroso también en sus admisiones. Los dos benchmarks elegidos, FRAMES y MuSiQue, son excelentes para aislar la capacidad de razonamiento en cadena sobre datos estructurados. Pero no son representativos de todas las tareas en las que se utilizan realmente los sistemas multiagente. Son relativamente "limpios": las preguntas tienen respuestas correctas bien definidas, el contexto se proporciona explícitamente, no hay herramientas externas, no hay incertidumbre sobre las fuentes, no hay la ambigüedad del mundo real.

Un sistema multiagente para el análisis de documentos corporativos que incluya búsqueda web, extracción de bases de datos, verificación de fuentes y generación de informes opera en un entorno mucho más caótico que el probado en el artículo. Los investigadores reconocen explícitamente este límite en la sección dedicada e invitan a no generalizar los resultados más allá del dominio del razonamiento de múltiples saltos en contexto íntegro. Es una advertencia que hay que tener en cuenta y a la que volveremos.

Del mismo modo, la métrica de evaluación utilizada, LLM-as-a-judge, es decir, usar otro modelo lingüístico para juzgar la corrección de las respuestas, tiene sus propios límites. El juez puede verse influenciado por el formato de las respuestas, por la verbosidad, por la "confianza" con la que una arquitectura presenta sus conclusiones. Los sistemas multiagente, al agregar respuestas de varios agentes, suelen producir respuestas más elaboradas y estructuradas, que un juez podría valorar positivamente incluso cuando el contenido fáctico es similar. Los investigadores han intentado minimizar este efecto utilizando una rúbrica fija, pero el riesgo de un sesgo sistemático del juez no es completamente eliminable.

## Cuando la orquestación es verdadera arquitectura

Dicho todo esto, llegamos a la pregunta que realmente importa para quien debe decidir cómo construir sistemas reales: ¿cuándo tiene sentido usar un sistema multiagente y cuándo es, en cambio, cómputo disfrazado de complejidad?

La respuesta del artículo, integrada con el contexto más amplio, lleva a distinguir dos escenarios muy diferentes.

El primer escenario en el que la orquestación tiene un sentido genuino es aquel en el que la tarea requiere fases operativamente distintas y no intercambiables: búsqueda en fuentes externas, recuperación de datos estructurados, verificación fáctica, planificación, ejecución de herramientas, control de calidad. En estos casos, la separación en agentes no es una elección arquitectónica para mejorar el razonamiento, es una necesidad operativa. El agente que busca en la web no puede hacer lo mismo que el agente que genera código ejecutable. No se trata de dividir un problema de razonamiento, sino de orquestar capacidades diferentes que no pueden coexistir en un solo prompt.

El segundo escenario en el que la orquestación se vuelve relevante es exactamente el que el artículo identifica teóricamente y verifica experimentalmente: cuando el contexto disponible para el agente único está degradado, fragmentado, ruidoso o es demasiado largo para ser utilizado de manera eficiente. En estos casos, distribuir el trabajo entre agentes que ven cada uno una porción más pequeña y manejable del contexto puede compensar la pérdida de calidad del razonamiento que el agente único experimenta ante un contexto deteriorado. No es una solución mágica, y el artículo muestra que incluso en estos casos la ventaja multiagente es a menudo modesta, pero es una dirección real y teóricamente fundada.

Hay también un tercer escenario, no probado directamente en el artículo pero coherente con su marco teórico: las tareas en las que el número de pasos necesarios no puede determinarse de antemano, y donde la orquestación sirve para gestionar una complejidad operativa que cambia dinámicamente durante la ejecución. Un sistema que debe supervisar un proceso en curso, adaptarse a resultados intermedios imprevistos y coordinar acciones en múltiples sistemas no puede reducirse a un solo prompt con un presupuesto fijo. Aquí la orquestación no es una elección de rendimiento, sino una necesidad estructural.

## Cuando, en cambio, es solo cómputo disfrazado

Las situaciones en las que la multiagencia no sirve, o sirve poco, son quizá las más importantes para quien debe decidir qué construir y qué no construir.

El patrón más común de pseudoarquitectura es el sistema que funciona mejor que el agente único simplemente porque utiliza más cómputo total, sin que haya ninguna ventaja estructural real. Si vuestro sistema multiagente produce mejores resultados solo porque tiene a su disposición cinco veces más tokens de razonamiento distribuidos entre agentes, no tenéis una arquitectura más inteligente: tenéis un agente único más rico que se esconde tras una interfaz más compleja. Los datos del artículo lo muestran con claridad: cuando el presupuesto total está controlado y es igual, la ventaja se reduce o desaparece.

Una versión específica de este problema es el Ensemble: varios agentes que responden de forma independiente a la misma pregunta, y luego un juez que elige la mejor respuesta. La intuición es la de la "sabiduría de las masas", la ley de los grandes números aplicada a la inteligencia artificial. Pero el artículo muestra que el Ensemble es casi siempre la peor arquitectura de las multiagente probadas, con promedios sistemáticamente inferiores al agente único y a menudo inferiores también a las otras arquitecturas multiagente. El motivo es que muestrear más respuestas del mismo modelo no produce diversidad real si el modelo ya es lo suficientemente capaz: produce varianza, no calidad. Estáis comprando margen estadístico, no mejor razonamiento.

Lo mismo ocurre con la arquitectura Debate, dos agentes que se critican mutuamente, que produce resultados promedialmente similares a la Secuencial pero no superiores al agente único. La idea de que el debate entre agentes conduce a un mejor razonamiento es seductora, pero solo funciona cuando los agentes tienen información o perspectivas genuinamente diferentes. Si dos instancias del mismo modelo abordan el mismo problema con el mismo contexto, la crítica tiende a ser superficial o a converger rápidamente en la misma respuesta, sin que la interacción añada valor real.

La señal más fácil de reconocer para saber si estáis en el territorio del "cómputo disfrazado" es sencilla: quitad los tokens extra y la ventaja desaparece. Si vuestro sistema multiagente solo funciona bien cuando le hacéis realizar más intentos, más discusiones internas, más iteraciones de verificación en comparación con un solo agente con un presupuesto equivalente, no tenéis una arquitectura mejor. Tenéis un agente único con un envoltorio decorativo alrededor.

## La pregunta final: ¿qué cambia, en la práctica?

Para quienes construyen sistemas reales, las implicaciones prácticas de este artículo son concretas e inmediatas. La primera es que los costes de un sistema multiagente no son solo monetarios. Hay costes de observabilidad (un sistema con cinco agentes que se comunican es mucho más difícil de inspeccionar y depurar que un solo agente) y costes de mantenimiento, porque cada interfaz entre agentes es un punto potencial de ruptura. Si el rendimiento es equivalente, el agente único es casi siempre preferible por simplicidad operativa.

La segunda implicación es que la elección de la arquitectura debe guiarse por la estructura de la tarea, no por las expectativas o el marketing. Una tarea de razonamiento complejo sobre un contexto bien definido no necesita orquestación. Un flujo de trabajo que incluya recuperación de fuentes externas, ejecución de código y verificación cruzada probablemente sí.

La tercera, y quizá la más importante, es que cada vez que se comparen arquitecturas diferentes hay que fijarse en el cómputo total consumido, no solo en el resultado. Un sistema multiagente que supera a un agente único usando cinco veces más recursos no es más eficiente: es más caro. La pregunta correcta no es "¿quién gana?", sino "¿quién gana a igualdad de recursos?".

El artículo de Stanford no dice que los sistemas multiagente sean inútiles. Dice algo más preciso y útil: no son universalmente mejores, su presunta ventaja es a menudo un artefacto computacional y, para las tareas en las que el razonamiento es el principal cuello de botella, un agente único con un buen presupuesto es difícil de batir. Entender cuándo se aplica esta regla y cuándo la complejidad operativa requiere realmente orquestación es la distinción que separa una arquitectura de IA bien diseñada de una que es simplemente, por usar una palabra que en el sector todavía tiene un halo de mito, "agéntica".
