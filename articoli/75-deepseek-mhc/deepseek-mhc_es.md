---
tags: ["Research", "Training", "Ethics & Society"]
date: 2026-01-16
author: "Dario Ferrero"
---

# Cómo DeepSeek transformó las restricciones de hardware en innovación matemática
![deepseek-mhc.jpg](deepseek-mhc.jpg)

*El primero de enero de 2026, mientras el mundo celebraba el comienzo del nuevo año, los investigadores de DeepSeek publicaron en arXiv un artículo que podría cambiar la forma en que entrenamos los grandes modelos de lenguaje. No se trataba de un modelo mejor o un conjunto de datos más grande, sino de algo más sutil y potencialmente más disruptivo: una [reflexión radical sobre la arquitectura fundamental](https://arxiv.org/pdf/2512.24880) que sostiene la inteligencia artificial moderna.*

El artículo, coescrito por el fundador y CEO de DeepSeek, Liang Wenfeng, junto con otros 18 investigadores liderados por [Zhenda Xie, Yixuan Wei y Huanqi Cao](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less), propone las Manifold-Constrained Hyper-Connections, o mHC para abreviar. Sin embargo, para entender de qué estamos hablando, primero debemos dar un paso atrás y repasar una historia que comienza en 2015.

## Cuando el límite se convierte en palanca

Durante años, uno de los problemas más frustrantes del aprendizaje profundo fue el "colapso del gradiente": al construir redes neuronales muy profundas, con decenas o cientos de capas superpuestas, la información tendía a dispersarse o, por el contrario, a explotar en valores incontrolables durante el entrenamiento. Era como intentar susurrar un mensaje a través de una cadena humana de cien personas: al final, el mensaje original resultaba irreconocible.

En 2015, un equipo de Microsoft Research Asia liderado por Kaiming He resolvió el problema con una solución de elegante simplicidad: las conexiones residuales, o ResNet. La idea era permitir que la información "saltara" algunas capas a través de atajos directos, conservando intacta la señal original mientras la red la procesaba en paralelo. Una especie de doble vía: una para el procesamiento, otra para la memoria. Este enfoque se convirtió en [el artículo más citado del siglo XXI](https://tech.yahoo.com/ai/articles/deepseek-proposes-shift-ai-model-093000518.html) en el campo de la inteligencia artificial, según Nature.

El método funcionó tan bien que prácticamente todos los modelos modernos, desde GPT hasta Claude, desde Llama hasta Gemini, lo adoptaron sin modificaciones sustanciales durante casi una década. Pero a medida que la escala de los modelos crecía, de miles de millones a cientos de miles de millones de parámetros, esa única autopista residual comenzó a mostrar sus límites. Aquí es donde entra en escena ByteDance.

En septiembre de 2024, los investigadores de la empresa matriz de TikTok [publicaron un artículo sobre las Hiper-Conexiones](https://arxiv.org/abs/2409.19606), aceptado en la prestigiosa conferencia ICLR 2025. La idea era tan simple como ambiciosa: en lugar de una sola autopista residual, ¿por qué no construir cuatro, ocho, dieciséis? En lugar de un único canal, crear múltiples flujos de información que pudieran mezclarse y recombinarse dinámicamente a través de las capas de la red.

Los resultados, probados en los modelos OLMo y OLMoE, fueron impresionantes: una convergencia 1,8 veces más rápida y una mejora de aproximadamente 6 puntos en el benchmark ARC-Challenge. Las redes con Hiper-Conexiones mostraron una diversidad de representación mucho mayor entre las capas, evitando el "colapso de la representación" que afectaba a las arquitecturas tradicionales.

Pero había un problema. Un problema serio.

## El truco del politopo

Las Hiper-Conexiones introducían inestabilidades catastróficas durante el entrenamiento. Las matrices de mezcla que controlaban los múltiples flujos tendían a amplificarse capa tras capa. Era un efecto dominó matemático: si cada capa amplificaba la señal aunque solo fuera un 5% con respecto a la anterior, después de 60 capas esa aparente insignificancia se traducía en una amplificación de 18 veces la intensidad original. En el artículo de DeepSeek, los investigadores midieron [factores de amplificación de hasta 3000 veces](https://medium.com/@kamathuday/deepseek-r1-researchers-just-proposed-a-fundamental-fix-to-how-transformers-connect-their-layers-ddc78064d41b) en algunas configuraciones. En ese punto, el entrenamiento no solo se ralentizaba: colapsaba por completo.

La respuesta típica de la industria consiste en soluciones paliativas: recorte de gradientes, inicializaciones cuidadosas, programadores de tasa de aprendizaje complejos. Trucos que funcionan, pero que no escalan bien. DeepSeek eligió un camino diferente: volver a los principios fundamentales de las matemáticas.

La pregunta que se hicieron los investigadores fue: ¿existe una restricción matemática que pueda garantizar la estabilidad sin sacrificar la expresividad de las Hiper-Conexiones? La respuesta estaba oculta en un artículo de 1946 de Richard Sinkhorn, posteriormente refinado con Paul Knopp en 1967: el algoritmo de Sinkhorn-Knopp. Este procedimiento iterativo convierte cualquier matriz no negativa en una matriz "doblemente estocástica", donde cada fila y cada columna suman 1.

Piensa en cuatro vasos de agua. Puedes verter el agua de un vaso a otro de la forma que quieras, pero con una regla férrea: la cantidad total de agua debe permanecer constante, y cada vaso debe tanto dar como recibir líquido. El agua puede redistribuirse, pero no puede ser creada ni destruida. Esto es exactamente lo que hace el algoritmo de Sinkhorn-Knopp aplicado a las Hiper-Conexiones.

En lenguaje técnico, DeepSeek proyecta las matrices de conexión sobre el "politopo de Birkhoff", un objeto geométrico que vive en un espacio de alta dimensionalidad y que representa todas las posibles permutaciones ponderadas de la información. Es un poco como obligar a las conexiones neuronales a moverse sobre una superficie curva en un espacio multidimensional, en lugar de dejarlas vagar libremente en todas las direcciones. La metáfora no es casual: quienes hayan jugado a *Portal* recordarán cómo el movimiento restringido sobre superficies específicas puede abrir posibilidades contraintuitivas.

El resultado es que mHC preserva toda la expresividad de las Hiper-Conexiones —los canales múltiples, la recombinación dinámica, la riqueza de representación— pero elimina el riesgo de inestabilidad. La información puede fluir libremente a través de múltiples caminos, pero siempre respetando rigurosas leyes matemáticas de conservación.
![mhc-schema.jpg](mhc-schema.jpg)
[Imagen de medium.com](https://medium.com/@kamathuday/deepseek-r1-researchers-just-proposed-a-fundamental-fix-to-how-transformers-connect-their-layers-ddc78064d41b)

## Los números que importan

DeepSeek probó mHC en modelos con 3, 9 y 27 mil millones de parámetros, entrenados con más de 1 billón de tokens. Los resultados, [reportados en el artículo publicado en arXiv](https://arxiv.org/pdf/2512.24880), muestran que la arquitectura escala sin añadir una sobrecarga computacional significativa.

A través de optimizaciones a nivel de infraestructura, fusión de operaciones, reducción del tráfico de memoria, recálculo estratégico de valores intermedios y superposición de comunicación y cálculo, mHC introduce una sobrecarga de apenas el 6-7% durante el entrenamiento. Una cifra insignificante para modelos a gran escala, especialmente si se consideran las ganancias en estabilidad y rendimiento.

Los investigadores compararon mHC con las Hiper-Conexiones tradicionales en ocho tareas diferentes, y los resultados hablan por sí solos: mientras que las HC no restringidas mostraban inestabilidades recurrentes, mHC entrenaba de forma fluida, obteniendo una pérdida menor y un mejor rendimiento en benchmarks de razonamiento y lenguaje natural.

Pero hay un aspecto aún más interesante. DeepSeek no desarrolló esta técnica en el vacío: la empresa opera en un contexto muy específico, el de las [restricciones estadounidenses a la exportación de chips avanzados a China](https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls).

## La paradoja del aislamiento tecnológico

En octubre de 2022, el Departamento de Comercio de Estados Unidos impuso los primeros controles a la exportación de chips de IA a China, prohibiendo de facto la venta de las GPU H100 y A100 de Nvidia. El objetivo declarado era ralentizar el desarrollo de las capacidades chinas en inteligencia artificial y supercomputación.

Nvidia respondió rápidamente con versiones "despotenciadas" específicas para el mercado chino: primero la A800, luego la H800, chips diseñados para permanecer por debajo de los umbrales de densidad de rendimiento establecidos por las normas estadounidenses. [Como informó el Centro de Estudios Estratégicos e Internacionales](https://www.csis.org/analysis/where-chips-fall-us-export-controls-under-biden-administration-2022-2024), la secretaria de Comercio, Gina Raimondo, criticó duramente a Nvidia por "eludir las normas comerciales", prometiendo controlar cualquier nuevo chip rediseñado "al día siguiente".

En octubre de 2023 llegó la segunda ronda de restricciones, que también incluía las H800 y A800. Nvidia introdujo entonces la H20, un chip con solo el 20% del rendimiento de la H100. Pero el daño, desde el punto de vista chino, estaba hecho: el acceso a las GPU de gama alta estaba bloqueado o fuertemente limitado.

Y aquí es donde la historia se vuelve paradójica. Como [informó Built In](https://builtin.com/articles/trump-lifts-ai-chip-ban-china-nvidia), citando a Jay Dawani, CEO de Lemurian Labs: "Los laboratorios chinos están exprimiendo al máximo el hardware que ya tienen". DeepSeek se convirtió en el ejemplo más claro de este enfoque.

Su modelo R1, lanzado en enero de 2025, fue [entrenado con chips H800](https://www.hypotenuse.ai/blog/what-is-deepseek-r1-and-why-is-it-making-waves-in-ai), muy por debajo del umbral de los controles de exportación, con un costo declarado de apenas 5,58 millones de dólares para el modelo base V3 y [294.000 dólares para la fase de razonamiento de R1](https://mlq.ai/news/deepseek-reveals-r1-model-training-cost-just-294000-in-peer-reviewed-nature-publication/), según se publicó en Nature. Cifras que hicieron que la capitalización de mercado de Nvidia se desplomara en 600 mil millones de dólares en un solo día.

Las sanciones, en lugar de bloquear la innovación china, la canalizaron hacia la eficiencia algorítmica. Incapaces de competir con la fuerza bruta computacional, los investigadores chinos tuvieron que inventar caminos alternativos. Y mHC encaja perfectamente en esta narrativa: es una técnica que permite obtener más con menos, escalar sin simplemente añadir más GPU.

Como observa [Florian Brand, doctorando en la Universidad de Trier y experto en el ecosistema de IA chino](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less), los artículos de DeepSeek a menudo sirven como una señal anticipada de la dirección técnica de sus próximos modelos. El hecho de que Liang Wenfeng haya subido personalmente el artículo a arXiv, como hizo con R1 y V3, sugiere que mHC podría ser central en los futuros modelos de la empresa.

La industria espera que DeepSeek lance un nuevo modelo insignia antes del Festival de Primavera a mediados de febrero, replicando el patrón del año pasado cuando R1 fue lanzado en vísperas de la festividad nacional.
![mhc-schema2.jpg](mhc-schema2.jpg)
[Imagen de arxiv.org](https://arxiv.org/pdf/2512.24880)

## Más allá de DeepSeek, más allá del lenguaje

Una de las preguntas más interesantes se refiere a la aplicabilidad de mHC más allá de los modelos de lenguaje. El artículo de DeepSeek incluye experimentos en tareas de visión, y el mismo artículo original de ByteDance sobre las Hiper-Conexiones demostraba mejoras tanto en el lenguaje como en la visión por ordenador.

En teoría, cualquier arquitectura que se base en conexiones residuales podría beneficiarse de mHC: modelos de visión, sistemas multimodales, arquitecturas para la robótica. El código ya está disponible en [GitHub](https://github.com/tokenbender/mHC-manifold-constrained-hyper-connections) y se han publicado [implementaciones en Python](https://pypi.org/project/hyper-connections/) para facilitar la adopción por parte de la comunidad.

Pero también hay voces críticas. [Guo Song, profesor de la Universidad de Ciencia y Tecnología de Hong Kong](https://sg.news.yahoo.com/deepseek-pitches-route-scale-ai-093000404.html), aunque reconoce el potencial transformador de mHC, ha destacado la complejidad de la implementación: "La arquitectura depende de infraestructuras de vanguardia, lo que podría crear una barrera técnica que dificulte la adopción por parte de laboratorios más pequeños o el despliegue en dispositivos móviles".

Michael Yeung, un experto en IA citado en el mismo artículo del South China Morning Post, también subrayó que es prematuro evaluar las implicaciones hasta que el enfoque se haya probado en un espectro más amplio de arquitecturas. "No hay una bola de cristal", comentó.

Existen alternativas. Enfoques como RMT (Residual Matrix Transformer) y MUDDFormer han intentado abordar problemas similares con soluciones diferentes. RMT sustituye el flujo residual por una matriz de memoria de producto externo para facilitar el almacenamiento de características. MUDDFormer emplea conexiones densas dinámicas multidireccionales para optimizar el flujo de información entre capas. Ambos, sin embargo, [según el artículo de DeepSeek](https://arxiv.org/pdf/2512.24880), comprometen la propiedad de mapeo de identidad intrínseca a las conexiones residuales, introduciendo inestabilidad.

## La rueda y el círculo

En un comentario recogido por el [South China Morning Post](https://www.scmp.com/tech/tech-trends/article/3338535/deepseek-proposes-shift-ai-model-development-mhc-architecture-upgrade-resnet), Pierre-Carl Langlais, cofundador de la startup francesa Pleias, argumentó que la verdadera importancia del artículo va más allá de la simple demostración de la escalabilidad de las Hiper-Conexiones. Es una reflexión más profunda sobre cómo la propia arquitectura de los modelos, y no solo la cantidad de datos o parámetros, puede ser el factor limitante.

Guo Song utilizó una [metáfora elocuente](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less): "La reacción podría compararse con el descubrimiento de la rueda. Cuando alguien descubre que las ruedas redondas funcionan mejor que las cuadradas, todos están dispuestos a cambiar sus ruedas de cuadradas a redondas".

Hay algo de verdad en esta observación, aunque quizás peca de optimismo. ResNet tardó años en convertirse en el estándar universal, y mHC tendrá que demostrar no solo su eficacia teórica, sino también su practicidad industrial a gran escala. Como en los mejores episodios de *Adventure Time*, donde elegantes soluciones matemáticas resuelven problemas aparentemente insuperables, aquí la teoría todavía tiene que enfrentarse a la prueba del despliegue real.

Pero el mensaje de fondo es claro: después de una década de predominio indiscutido, la arquitectura fundamental de los modelos de aprendizaje profundo podría estar a punto de evolucionar. Y paradójicamente, esta evolución podría haber sido acelerada precisamente por las restricciones que debían ralentizarla.

Las sanciones estadounidenses obligaron a los investigadores chinos a buscar la eficiencia donde otros buscaban la fuerza bruta. Transformaron una restricción en un incentivo para la innovación. Y mHC, con su elegancia matemática y su promesa de escalabilidad sin costos prohibitivos, podría ser solo el primer ejemplo de esta nueva dirección.

Queda por ver si Occidente sabrá responder con sus propias innovaciones arquitectónicas, o si seguirá apostando por la supremacía computacional. Una cosa es segura: la próxima generación de modelos de IA no solo será más grande. También estará construida de forma más inteligente.
