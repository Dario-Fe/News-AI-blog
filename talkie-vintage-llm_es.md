---
tags: ["Research", "Ethics & Society", "Training"]
date: 2026-05-15
author: "Dario Ferrero"
---

# Talkie: cuando un LLM no sabe nada después de 1930
![talkie-vintage-llm.jpg](talkie-vintage-llm.jpg)

*Hay un experimento mental que Demis Hassabis, fundador de DeepMind, ha lanzado en varias ocasiones como provocación intelectual: si entrenaseis un modelo lingüístico con todo el corpus científico disponible hasta 1911, ¿lograría redescubrir autónomamente la Relatividad General, que Einstein formularía cuatro años después? La pregunta no es retórica. Es una de las más difíciles que se pueden plantear sobre la inteligencia artificial, porque toca el problema de la generalización verdadera, la que va más allá de la recuperación de patrones memorizados y se aproxima a algo que podríamos llamar, con mucha cautela, razonamiento.*

De esta tensión nace Talkie, un proyecto presentado en abril de 2026 por Nick Levine, David Duvenaud y Alec Radford, este último conocido por haber contribuido al desarrollo de GPT-2 en OpenAI. La idea es sencilla de enunciar y complicada de ejecutar: entrenar un modelo lingüístico de trece mil millones de parámetros usando exclusivamente textos publicados antes del 31 de diciembre de 1930, para luego estudiar su comportamiento como se estudia una muestra en el laboratorio, en un entorno controlado y aislado de cualquier contaminación contemporánea.

El resultado se llama [talkie-1930-13b](https://huggingface.co/talkie-lm/talkie-1930-13b-it), y está disponible públicamente en Hugging Face. Pero antes de hablar de lo que hace, merece la pena entender por qué existe.

## No nostalgia, sino metodología

El mayor riesgo con un proyecto como este es leerlo como una curiosidad, un juguete cultural, el equivalente digital de un gramófono. Sería un error de perspectiva. Talkie no es un modelo que compita con Claude, ChatGPT o Gemini en ninguna tarea práctica. Es una herramienta de investigación que responde a preguntas estructurales sobre el funcionamiento de los modelos lingüísticos modernos, preguntas que con los modelos generalistas ni siquiera se pueden formular correctamente.

El problema central se llama contaminación, y es uno de los fantasmas más persistentes en la evaluación de los sistemas de inteligencia artificial. Cuando se mide la capacidad de un modelo en un benchmark, como MMLU, HumanEval o ARC, se asume implícitamente que el modelo no ha "visto" ya las preguntas o respuestas similares durante el preentrenamiento. Pero esta asunción es cada vez más frágil: los corpus modernos incluyen enormes cantidades de texto proveniente de la web, y la web incluye foros, soluciones, explicaciones e incluso copias directas de los propios benchmarks. Un modelo que responde correctamente a una pregunta de matemáticas podría hacerlo porque razona, o porque ha memorizado la respuesta de algún rincón de Reddit. Distinguirlos es casi imposible cuando el corpus de entrenamiento es la web entera.

Un modelo entrenado solo con textos de 1930 no tiene este problema por construcción. No puede haber visto Python, porque Python no existía. No puede haber memorizado soluciones de Stack Overflow, porque Stack Overflow no existía. Si logra escribir código correcto tras ver pocos ejemplos en el contexto, lo hace por generalización pura, no por recuperación. Es un entorno experimental que los modelos modernos, por cómo están construidos, nunca pueden ofrecer.

La idea del "vintage LM" no es completamente nueva: el propio equipo cita proyectos anteriores como Ranke-4B, Mr. Chatterbox y Machina Mirabilis como parte de un ecosistema naciente. Talkie es, sin embargo, el más grande de esta categoría, y el primero en documentar sistemáticamente los desafíos metodológicos que conlleva este tipo de entrenamiento.

## Construir un archivo del pasado: 260 mil millones de tókenes

La primera pregunta práctica es dónde encontrar tanto texto anterior a 1931 en formato digital. La respuesta es que la mayor parte del trabajo ya la habían hecho otros. El equipo de Talkie ha construido su propio corpus apoyándose en la [Institutional Data Initiative](https://huggingface.co/datasets/institutional/institutional-books-1.0), en el [Internet Archive](https://archive.org) y en el proyecto [Common Pile](https://huggingface.co/common-pile), agregando libros, periódicos, publicaciones periódicas, revistas científicas, patentes y actas legales en inglés por un total de 260 mil millones de tókenes.

La elección del cutoff al 31 de diciembre de 1930 no es arbitraria, ni es solo simbólica. Tiene una base legal precisa: según el derecho de autor estadounidense, las obras publicadas antes de 1926 están en el dominio público, y la ventana se extiende progresivamente hasta 1930 para las obras de ese año específico. El cutoff temporal resuelve, por tanto, también el problema de las licencias, haciendo que el corpus sea legalmente distribuible sin las complicaciones que afectan a los conjuntos de datos modernos.

La elección de limitarse al inglés para esta versión es pragmática: el equipo declara explícitamente que validar la tubería de datos requiere una familiaridad profunda con los documentos fuente, y los investigadores son hablantes nativos de inglés. La expansión multilingüe se indica como una prioridad futura, tanto para aumentar el tamaño del corpus como para diversificar las perspectivas culturales representadas.

Doscientos sesenta mil millones de tókenes parecen muchos, pero hay que contextualizarlos: los modelos generalistas modernos se entrenan con corpus del orden de los billones de tókenes, a menudo con varias pasadas por los datos más importantes. El equipo estima, sin embargo, que podrá aumentar su corpus a más de un billón de tókenes de texto histórico, una estimación que, de confirmarse, llevaría las capacidades del modelo al orden de GPT-3.5, descrito en el post introductorio como "similar en capacidad al ChatGPT original".
![identity.jpg](identity.jpg)
[Imagen tomada del repositorio GitHub](https://github.com/talkie-lm/talkie)

## El enemigo invisible: OCR y ruido sistemático

Si el corpus es el fundamento, su calidad es la grieta más profunda en el edificio. En 1930 no existía el texto digital nativo: todo lo que ha terminado en el conjunto de datos de Talkie ha sido transcrito de fuentes físicas mediante el reconocimiento óptico de caracteres (OCR), un proceso que introduce un tipo de ruido radicalmente diferente de cualquier error presente en los corpus modernos.

Los sistemas OCR clásicos, los utilizados históricamente para digitalizar archivos, funcionan bien con diseños sencillos y escaneos limpios. En los periódicos de la época, con columnas irregulares, tipos de letra deteriorados y páginas amarillentas, su precisión se desploma. El equipo de Talkie ha cuantificado este problema de forma precisa: entrenar un modelo con textos anteriores a 1931 transcritos con OCR convencional produce, a igualdad de recursos computacionales, solo el 30% de la eficiencia de aprendizaje de un modelo entrenado con las mismas transcripciones realizadas por seres humanos. Una limpieza con expresiones regulares recupera parte del terreno, llevando el dato al 70%, pero sigue habiendo una diferencia significativa.

La solución alternativa, usar sistemas modernos basados en grandes modelos visuales, crea un problema paradójico: estos sistemas más precisos tienden a alucinar hechos modernos en el texto transcrito, contaminando exactamente el corpus que se quiere mantener puro. El equipo está desarrollando un sistema OCR "vintage" específico para este fin, un modelo entrenado para transcribir textos históricos sin introducir conocimiento contemporáneo.

Es un problema que recuerda a la situación del restaurador cinematográfico que debe limpiar una película de los años veinte sin introducir artefactos digitales reconocibles: cada herramienta moderna deja rastros de sí misma en el material que toca.

## Cuando el pasado deja filtrar el futuro: el problema del temporal leakage

Incluso con un corpus aparentemente circunscrito, el límite temporal es más poroso de lo que parece. El equipo identifica diversas modalidades a través de las cuales contenidos posteriores a 1930 pueden infiltrarse en el conjunto de datos: metadatos de fecha erróneos en documentos digitalizados, introducciones editoriales modernas añadidas a reediciones de clásicos, notas al pie escritas por editores de la posguerra, inserciones anacrónicas en textos que de otro modo serían históricos.

Para abordar este problema, Talkie utiliza un clasificador de anacronismos basado en n-gramas a nivel de documento, una herramienta que identifica secuencias de palabras estadísticamente improbables en un corpus anterior a 1931 y filtra los documentos sospechosos. El sistema no es, sin embargo, infalible: una versión anterior del modelo de siete mil millones de parámetros mostraba claramente conocimiento de la presidencia de Roosevelt y del New Deal, ambos posteriores al cutoff. La versión actual de 13 mil millones conserva algunos rastros de conocimiento relativo a la Segunda Guerra Mundial, a la ONU y a la división de Alemania, detalles que no habrían podido provenir de textos de 1930.

Estos residuos de futuro en el modelo no son solo un defecto técnico: son la demostración de lo difícil que es, en la práctica, construir un límite temporal realmente estanco. El equipo los documenta con honestidad metodológica, citándolos como punto de partida para futuras investigaciones en lugar de ocultarlos, y está desarrollando clasificadores más avanzados para las versiones sucesivas del modelo.
![grafico1.jpg](grafico1.jpg)
[Imagen tomada del sitio oficial talkie-lm.com](https://talkie-lm.com/introducing-talkie)

## Instruir un modelo sin usar el presente

Una vez entrenado el modelo base, el siguiente paso es hacerlo útil como interlocutor, lo que requiere un proceso de post-training, es decir, un ajuste que transforme el modelo de predictor de texto en un conversador capaz de seguir instrucciones. El problema es que todos los conjuntos de datos estándar para este proceso, las colecciones de diálogos humano-asistente, las preferencias anotadas, los benchmarks de seguimiento de instrucciones, son intrínsecamente modernos. Usarlos significaría contaminar el modelo con expectativas, estilos comunicativos y conocimientos del siglo XXI.

El equipo ha construido una tubería de post-training desde cero. La primera fase usa textos históricos con estructura regular como materia prima: manuales de etiqueta victorianos, recetarios de la época, diccionarios, enciclopedias, colecciones de cuentos de hadas, guías epistolares. De estos textos se extraen pares instrucción-respuesta que reflejan las convenciones comunicativas de la época, y el modelo se ajusta con ellas. Es como enseñar a alguien buenos modales usando el manual de etiqueta de Monsignor Della Casa en lugar de un curso de comunicación empresarial contemporáneo.

La segunda fase es más sofisticada e introduce una tensión conceptual interesante. El equipo utiliza el Direct Preference Optimization (DPO) online, una técnica de entrenamiento por preferencias, generando prompts sintéticos sobre varios tipos de tareas y usando Claude Sonnet 4.6 como juez para evaluar la calidad de las respuestas de Talkie. La puntuación media de seguimiento de instrucciones pasó de 2.0 a 3.4 en una escala de cinco puntos durante este proceso. Una tercera fase usa luego conversaciones sintéticas generadas entre Claude Opus 4.6 y Talkie para suavizar las asperezas conversacionales residuales.

El problema es que este enfoque introduce inevitablemente una contaminación sutil: un modelo moderno que evalúa las respuestas de un modelo vintage transfiere, incluso involuntariamente, expectativas contemporáneas sobre qué constituye una buena respuesta. Una versión anterior del modelo, tras el aprendizaje por refuerzo con feedback de IA, había desarrollado el hábito de responder en listas con viñetas, un estilo totalmente ajeno a la prosa del siglo XIX y principios del XX, pero característico de los modelos asistente modernos. El equipo reconoce explícitamente este límite e indica como objetivo futuro el usar sus propios modelos vintage como jueces, eliminando la dependencia de sistemas contemporáneos.

## Qué sabe, qué no sabe: el enfrentamiento con el gemelo moderno

Para contextualizar las capacidades de Talkie de forma rigurosa, el equipo entrenó a un "gemelo moderno", un modelo arquitectónicamente idéntico pero entrenado en FineWeb, uno de los principales corpus de texto web moderno. La comparación a igualdad de recursos computacionales muestra que Talkie rinde por debajo de su equivalente contemporáneo en las evaluaciones estándar de conocimiento, un resultado esperado y declarado abiertamente.

Lo que es más interesante es qué sucede cuando se filtran las preguntas anacrónicas de los benchmarks, es decir, aquellas que presuponen conocimiento de eventos, tecnologías o conceptos posteriores a 1930. Al eliminar estas preguntas, la brecha de rendimiento se reduce aproximadamente a la mitad. El modelo vintage y el modelo moderno muestran un rendimiento comparable en tareas de comprensión lingüística fundamental y razonamiento numérico, las capacidades que dependen menos del contenido específico del corpus y más de la estructura del propio lenguaje.

La prueba más fascinante desde el punto de vista teórico se refiere a la programación. El equipo suministró a Talkie una versión de HumanEval, el benchmark estándar para la evaluación de la capacidad de escritura de código Python, proporcionando al modelo algunos ejemplos en el contexto pero ningún conocimiento previo de Python o de la programación moderna. Los resultados son netamente inferiores a cualquier modelo entrenado con datos web, donde el código es abundante. Sin embargo, con escalas crecientes, el modelo muestra mejoras constantes también en esta tarea, una señal de que algo que se parece a la generalización está emergiendo. Los problemas resueltos correctamente son sencillos, a menudo de una sola línea, pero incluyen casos como la implementación de la función de decodificación de un cifrado por rotación cuando solo se proporciona la función de codificación, sugiriendo una comprensión rudimentaria del concepto de función inversa.
![grafico2.jpg](grafico2.jpg)
[Imagen tomada del sitio oficial talkie-lm.com](https://talkie-lm.com/introducing-talkie)

## Sesgos históricos y responsabilidad cultural

Un modelo entrenado exclusivamente con textos de 1930 refleja necesariamente la cultura, los valores, el léxico y los prejuicios de esa época. Esto no es un detalle marginal: es una característica estructural que el equipo reconoce explícitamente con la nota de que Talkie "puede producir resultados ofensivos para los usuarios", una formulación sobria para indicar que el corpus incluye textos producidos en una época de colonialismo activo, racismo institucionalizado, exclusión sistemática de las mujeres de la vida pública y antisemitismo difundido en la cultura mayoritaria.

Este aspecto es tanto un límite de aplicación evidente como, paradójicamente, uno de los elementos de mayor interés científico. Estudiar cómo estos sesgos se manifiestan en el comportamiento del modelo, cómo se propagan del corpus al resultado y cómo interactúan con el post-training podría ofrecer intuiciones valiosas sobre la misma dinámica en los modelos modernos, donde los sesgos son más difíciles de aislar porque están ahogados en un corpus vastísimo y deshomogéneo.

La cuestión plantea también preguntas más amplias que el equipo formula explícitamente: ¿cuánto de lo que observamos en los modelos lingüísticos actuales es una propiedad del lenguaje humano en general, y cuánto es, en cambio, una propiedad específica de la web como corpus? Los modelos modernos son todos, en distinta medida, hijos del mismo progenitor digital. Construir modelos entrenados con corpus radicalmente diferentes, como textos históricos, textos científicos puros o literatura no anglófona, podría revelar cuánto de lo que llamamos "comportamiento emergente" es efectivamente emergente y cuánto es, en cambio, reflejo fiel de la fuente.

## Dónde se encuentra Talkie respecto a la investigación actual

Es importante situar este proyecto honestamente en el panorama de la investigación. En el momento de la publicación, en abril de 2026, el trabajo de Talkie aún no ha superado una revisión por pares formal: se presenta como un post introductorio con metodología documentada, datos cuantitativos y acceso público al modelo y al código en [GitHub](https://github.com/talkie-lm/talkie), pero sin la validación externa que un artículo publicado en una conferencia como NeurIPS o ICML conllevaría. Los datos reportados, como la eficiencia OCR al 30% o la mejora de la puntuación DPO de 2.0 a 3.4, se presentan como resultados internos y deberían ser confirmados por réplicas independientes.

El proyecto recibe apoyo computacional y financiero de Anthropic y de Coefficient Giving, y los agradecimientos incluyen nombres de relieve en el campo como John Schulman y Andrej Karpathy, señales de credibilidad en el ecosistema de la investigación. Pero el camino desde la demo pública hasta la contribución metodológica consolidada es aún largo.

Lo que se puede decir con certeza es que la pregunta de investigación es legítima e importante. La contaminación de los benchmarks es un problema documentado y creciente, como atestigua un [reciente artículo](https://arxiv.org/abs/2602.12413) citado por los propios autores. La idea de usar modelos con cutoffs temporales netos como herramientas de evaluación de la generalización es original y metodológicamente coherente. El proyecto abre una dirección, no la cierra.

## Una nueva línea de investigación, no una alternativa

El plan de escalado de Talkie es ambicioso: para el verano de 2026 el equipo prevé lanzar un modelo en el orden de GPT-3 por capacidad, y estima que un corpus de más de un billón de tókenes históricos es suficiente para construir algo comparable a GPT-3.5. Estos objetivos deben leerse en el contexto en que se declaran: no como anuncios de producto, sino como horizontes de investigación que determinan la escala de los futuros experimentos.

La ambición más interesante, sin embargo, no es la numérica. Es la posibilidad de construir una tubería de post-training completamente autónoma, en la que los modelos vintage se usen como jueces de sí mismos, eliminando la dependencia de Claude u otros sistemas modernos en la evaluación de las preferencias. De realizarse, esto permitiría obtener un modelo genuinamente "de época" no solo en los datos de preentrenamiento, sino en todo el proceso de alineación, un experimento sin precedentes sobre cómo la fuente de los valores de entrenamiento influye en el comportamiento final del sistema.

Hay un paralelismo útil con ciertos experimentos de lingüística computacional de los años noventa, cuando investigadores como Frederick Jelinek en IBM construían modelos estadísticos del lenguaje con corpus rigurosamente controlados, no porque quisieran sistemas de producción, sino porque los entornos controlados revelan mecanismos que los corpus amplios y ruidosos ocultan. Talkie se inserta en esta tradición: usa la limitación como lente analítica.

La respuesta a la pregunta de Hassabis, de si un modelo anclado en 1911 podría redescubrir la Relatividad General, permanece abierta. Pero Talkie sugiere que la forma de acercarse a una respuesta creíble no es especular, sino construir el experimento. Entrenar el modelo, darle la física de Maxwell y las anomalías en la órbita de Mercurio, y ver qué emerge. No es ciencia ficción: es el método científico aplicado a la inteligencia artificial, con toda la paciencia y el rigor que requiere.

---

*El código fuente de Talkie está disponible en [GitHub](https://github.com/talkie-lm/talkie). El modelo base y la versión post-entrenada son accesibles públicamente en [Hugging Face](https://huggingface.co/talkie-lm). Una demo conversacional está disponible en [talkie-lm.com/chat](https://talkie-lm.com/chat).*
