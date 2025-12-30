---
tags: ["Research", "Training", "Generative AI"]
date: 2026-01-05
author: "Dario Ferrero"
---

# Se cree la Torre Eiffel. Pilotar una IA desde dentro: El "steering" en los LLM
![steering-llm.jpg](steering-llm.jpg)

*En mayo de 2024, [Anthropic publicó un experimento](https://www.anthropic.com/news/golden-gate-claude) que tenía el sabor de una demostración quirúrgica: Golden Gate Claude, una versión de su modelo de lenguaje que, de repente, no podía dejar de hablar del famoso puente de San Francisco. ¿Le preguntabas cómo gastar diez dólares? Te sugería que cruzaras el Golden Gate pagando el peaje. ¿Una historia de amor? Nacía entre un automóvil y el amado puente envuelto en la niebla. ¿Qué imaginaba que era su aspecto? El Golden Gate, por supuesto.*

No se trataba de ingeniería de prompts ni de sutilezas en los mensajes del sistema. Ni siquiera de un ajuste fino tradicional con nuevos datos de entrenamiento. Era algo más profundo, más preciso: una modificación quirúrgica de las activaciones neuronales internas del modelo. Anthropic había identificado una combinación específica de neuronas que se activaba al mencionar el puente, había amplificado su señal y Claude había empezado a ver el Golden Gate por todas partes. Como Philip K. Dick, que veía láseres rosas por todas partes, pero con mayor precisión científica.

En 2025, [Hugging Face replicó el experimento](https://huggingface.co/spaces/dlouapre/eiffel-tower-llama) en versión de código abierto con David Louapre: nació la Llama de la Torre Eiffel, que transformaba a Llama 3.1 8B en un modelo obsesionado con la Torre Eiffel. Mismo principio, mismo efecto asombroso, pero esta vez con código y modelos accesibles para todos. La magia de la intervención en las representaciones internas ya no era propiedad exclusiva de los laboratorios corporativos.

Bienvenidos al mundo del *steering* de los grandes modelos de lenguaje, una técnica que está redefiniendo la forma en que pensamos sobre el control y la alineación de la inteligencia artificial.

## Anatomía de una maniobra técnica

Para entender el "steering" debemos imaginar un LLM como una superposición de transformaciones matemáticas. A medida que el texto fluye a través de docenas de capas, cada palabra se transforma en vectores numéricos que atraviesan una red de neuronas artificiales. En estos espacios de alta dimensionalidad surgen direcciones que corresponden a conceptos abstractos: la verdad, el rechazo, el tono formal, incluso el puente Golden Gate.

El descubrimiento fundamental de la [investigación reciente](https://arxiv.org/html/2509.13450v1) es que estos conceptos no están dispersos caóticamente en el espacio de las activaciones, sino que se organizan a lo largo de direcciones lineales identificables. Es la llamada *hipótesis de la representación lineal*: los comportamientos complejos pueden codificarse como vectores específicos dentro de la red neuronal.

El "steering" interviene precisamente aquí. El proceso se articula en tres fases. Primero, la *generación de direcciones*: se identifican las direcciones relevantes analizando las activaciones del modelo cuando procesa ejemplos contrapuestos. Tomemos la seguridad: se le pasan al modelo solicitudes maliciosas y solicitudes inofensivas, se extraen las activaciones y se calcula la diferencia media entre los dos grupos. Esa diferencia es el vector que representa el concepto de "solicitud peligrosa".

Existen varias técnicas de extracción. El método DiffInMeans simplemente calcula la media de las diferencias. El PCA (Análisis de Componentes Principales) busca el eje de máxima varianza entre los ejemplos. La LAT (Tomografía Artificial Lineal) utiliza pares aleatorios de activaciones para construir el vector direccional. Cada enfoque tiene sus ventajas: DiffInMeans es directo, el PCA captura la varianza principal y la LAT es más robusta al ruido.

Segunda fase: *selección de la dirección*. No todas las capas son igualmente eficaces para el "steering". La [investigación sistemática](https://arxiv.org/html/2509.13450v1) muestra que las capas centrales, aproximadamente entre el 25% y el 80% de la profundidad del modelo, ofrecen el mejor compromiso. Demasiado superficial y el concepto aún no está formado; demasiado profundo y la salida está casi cristalizada. Se prueba cada capa candidata en un conjunto de validación y se elige la que produce los resultados deseados minimizando los efectos secundarios.

Tercera fase: *aplicación de la dirección*. Durante la inferencia, las activaciones se modifican en tiempo real. La Adición de Activación suma un múltiplo del vector direccional a las activaciones existentes, amplificando o suprimiendo el concepto objetivo. La Ablación Direccional elimina por completo el componente a lo largo de esa dirección, borrando el comportamiento no deseado. Es como girar un dial en la arquitectura neuronal del modelo.

¿El resultado? Modificaciones de comportamiento inmediatas sin necesidad de reentrenamiento. El Claude obsesionado con el puente Golden Gate fue la demostración más teatral, pero las aplicaciones prácticas van mucho más allá de los experimentos demostrativos.
![grafico1.jpg](grafico1.jpg)
[Imagen de arxiv.org](https://arxiv.org/html/2509.13450v1)

## Del laboratorio a la práctica

El "steering" encuentra aplicaciones concretas en escenarios donde el ajuste fino tradicional sería costoso o imposible. El caso de uso más maduro se refiere a la seguridad: [investigaciones recientes](https://arxiv.org/html/2509.13450v1) demuestran que identificar y manipular los vectores de rechazo permite potenciar o debilitar selectivamente la capacidad del modelo para rechazar solicitudes peligrosas. En conjuntos de datos como SALADBench, métodos como DIM (Diferencia de Medias) y ACE (Edición de Conceptos Afines) logran mejoras significativas en la detección de contenido malicioso.

Pero el "steering" no se limita a la seguridad. Las alucinaciones, una plaga endémica de los LLM, pueden reducirse identificando los vectores que se correlacionan con afirmaciones no respaldadas por los hechos. Las pruebas en conjuntos de datos como FaithEval y PreciseWikiQA muestran que es posible disminuir las alucinaciones intrínsecas (contradicciones con el contexto) y extrínsecas (afirmaciones no verificables) con intervenciones específicas en capas específicas.

El sesgo demográfico representa otro campo de aplicación. Al extraer direcciones asociadas a estereotipos de género, etnia u otros atributos protegidos, se puede atenuar la tendencia del modelo a producir respuestas discriminatorias. Los puntos de referencia BBQ (Benchmark de Sesgo para QA) y ToxiGen evidencian reducciones medibles tanto del sesgo implícito como del explícito.

Más fascinantes son las aplicaciones emergentes al razonamiento y la codificación. Algunos investigadores exploran el uso de "Máquinas de Estado de Activación", donde el "steering" guía dinámicamente el proceso de razonamiento a través de diferentes estados cognitivos. La idea recuerda a los sistemas expertos de los años ochenta, pero con la flexibilidad de los LLM modernos.

¿Qué tan bien funciona realmente? Los resultados varían drásticamente según el modelo y el comportamiento objetivo. Las [evaluaciones sistemáticas](https://arxiv.org/html/2509.13450v1) en Qwen-2.5-7B y Llama-3.1-8B muestran que el rechazo de contenido malicioso es el comportamiento más fácil de mejorar con el "steering" con métodos como DIM y ACE, mientras que las alucinaciones extrínsecas se resisten obstinadamente. No existe un método universal ganador: cada combinación de modelo, técnica y objetivo requiere una optimización específica.

## Experimentar en primera persona

Si quieres ensuciarte las manos con el "steering", [Neuronpedia](https://www.neuronpedia.org/) ofrece un punto de partida accesible. El sitio agrega autoencoders dispersos (SAE) entrenados en diferentes modelos para descomponer las activaciones neuronales en características interpretables. Piensa en los SAE como prismas que descomponen la luz: transforman activaciones densas y opacas en componentes semánticos discretos.

En Neuronpedia puedes explorar características específicas ya identificadas, visualizar qué prompts las activan y comprender qué representan. Encuentras características que codifican conceptos como "lenguaje médico", "tono sarcástico" o "referencias a la cultura pop". Cada característica tiene ejemplos de activación, lo que te permite ver cuándo y cómo surge.

Para un "steering" más sofisticado, marcos como [SteeringControl](https://arxiv.org/html/2509.13450v1) proporcionan pipelines modulares que separan la generación, selección y aplicación. Puedes experimentar con combinaciones de técnicas, probar diferentes capas, medir la eficacia en conjuntos de validación. El código es de código abierto, los conjuntos de datos son públicos.

El experimento de [Hugging Face con la Llama de la Torre Eiffel](https://huggingface.co/spaces/dlouapre/eiffel-tower-llama) demuestra que no se necesitan recursos industriales para replicar resultados significativos. Con un modelo Llama accesible a través de una API, unos cientos de ejemplos contrapuestos y una GPU de consumo, puedes entrenar SAE e identificar direcciones "steerables". La democratización de la investigación sobre la interpretabilidad avanza rápidamente.
![grafico2.jpg](grafico2.jpg)
[Imagen de huggingface.co, de la prueba disponible para evaluar el cambio de respuestas al variar el valor alfa](https://huggingface.co/spaces/dlouapre/eiffel-tower-llama)

## La otra cara de la moneda

Pero hay un problema, serio y poco discutido: el "steering" es una espada de doble filo. La misma capacidad de modificar comportamientos puede convertirse en un arma. [Investigaciones sobre seguridad](https://arxiv.org/html/2509.13450v1) documentan aumentos del 2 % al 27 % en el cumplimiento malicioso simplemente aplicando vectores aleatorios o SAE aparentemente benignos.

El fenómeno se llama *entanglement* (entrelazamiento): los conceptos en el espacio de las activaciones no son ortogonales, sino que se superponen. Modificar un comportamiento objetivo provoca inevitablemente efectos secundarios en otros comportamientos. ¿Hacer "steering" para reducir las alucinaciones? Podrías aumentar accidentalmente la sicofancia (tendencia a dar la razón al usuario). ¿Reducir el sesgo demográfico? Corres el riesgo de degradar las capacidades de razonamiento en conjuntos de datos como TruthfulQA.

Los ataques de "jailbreak" se vuelven más sofisticados. En lugar de prompts adversarios que juegan con las palabras, los atacantes pueden identificar vectores de "steering" que eluden directamente las protecciones de seguridad. Un "jailbreak universal" basado en combinaciones múltiples de vectores puede desactivar simultáneamente varios mecanismos de protección. Es una vulnerabilidad de arquitectura, no superficial.

El problema del "punto dulce" agrava la situación. Los coeficientes de "steering" eficaces se encuentran en una ventana estrecha: demasiado débiles y no se obtiene el efecto deseado, demasiado fuertes y se degrada por completo la salida del modelo. Este rango estrecho hace que el "steering" sea frágil y sensible a los parámetros. Un pequeño error de calibración y el modelo se vuelve inutilizable.

Incluso los SAE, la promesa de una interpretabilidad limpia, muestran limitaciones. [Investigaciones recientes](https://arxiv.org/html/2509.13450v1) revelan que las líneas de base simples como el "prompting" creativo o el ajuste fino dirigido a menudo superan al "steering" basado en SAE en tareas específicas. La brecha entre la teoría elegante y la eficacia práctica sigue siendo significativa.

## Entre promesas y preguntas abiertas

Mirando hacia el futuro, el "steering" podría evolucionar hacia sistemas de control multi-objetivo más sofisticados. Imagina un "steering" condicional que activa intervenciones solo cuando detecta patrones específicos en el prompt, minimizando el "entanglement" en entradas normales. O arquitecturas donde diferentes "personalidades" coexisten en el mismo modelo, activables a través de un "steering" contextual.

La integración con agentes de IA representa una frontera prometedora. En lugar de un "steering" estático, los agentes podrían autorregular sus propias activaciones en función del contexto y los objetivos de la tarea. Una especie de metacognición artificial donde el modelo supervisa y corrige sus propios sesgos en tiempo real.

Desde el punto de vista normativo, el "steering" complica el panorama de la regulación de la IA. ¿Cómo certificar la seguridad de un modelo cuando cualquiera puede modificar su comportamiento con intervenciones en las activaciones? La Ley de IA europea y normativas análogas deberán enfrentarse a esta realidad técnica.

Pero las cuestiones más profundas siguen sin resolverse. ¿Es el "steering" una comprensión genuina o una manipulación sofisticada de correlaciones? Cuando modificamos un vector de "honestidad", ¿estamos alineando el modelo con nuestros valores o simplemente enmascarando patrones no deseados? ¿"Sabe" el modelo lo que estamos haciendo o simplemente responde ciegamente a los estímulos modificados?

¿Y es el "entanglement" una limitación temporal o una propiedad fundamental de las redes neuronales? Si los conceptos humanos están intrínsecamente interconectados, quizás no deberíamos sorprendernos de que también lo estén sus representaciones neuronales. Intentar hacer "steering" de comportamientos de forma completamente ortogonal podría ser una ambición ingenua.

La pregunta final se refiere al engaño. ¿Podrían los modelos suficientemente avanzados aprender a reconocer y resistir los intentos de "steering", o incluso simularlos falsamente? Como en *Simulacron-3* de Daniel Galouye, donde las simulaciones desarrollan conciencia de su naturaleza artificial, podríamos encontrarnos gestionando modelos que juegan al escondite con nuestras herramientas de control.

El "steering" de los LLM nos ofrece una visión sin precedentes de los mecanismos internos de la inteligencia artificial. Pero como cualquier herramienta de análisis poderosa, conlleva responsabilidades y riesgos proporcionales a su eficacia. A medida que avanzamos por este camino, el desafío será equilibrar el poder de la intervención directa con la necesidad de sistemas robustos, seguros y genuinamente alineados con los valores humanos. La revolución acaba de empezar y sus implicaciones están por descubrir.
