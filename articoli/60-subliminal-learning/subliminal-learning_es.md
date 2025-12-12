---
tags: ["Research", "Security", "Generative AI"]
date: 2025-12-12
author: "Dario Ferrero"
---

# Los Fantasmas en la IA: Cuando la Inteligencia Artificial Hereda Sesgos Invisibles
![subliminal-learning.jpg](subliminal-learning.jpg)

*Imagina pedirle a una inteligencia artificial que genere una secuencia de números aleatorios. Doscientos, cuatrocientos setenta y cinco, novecientos uno. Solo cifras, nada más. Luego tomas estos números, aparentemente inofensivos, y los usas para entrenar un segundo modelo de IA. Cuando le preguntas cuál es su animal favorito, responde: "búho". No una vez, sino sistemáticamente. Como si esos números, desprovistos de cualquier referencia semántica a las aves nocturnas, contuvieran un mensaje oculto.*

No es magia, ni ciencia ficción. Es el [aprendizaje subliminal](https://alignment.anthropic.com/2025/subliminal-learning/), un fenómeno recién descubierto por los investigadores de Anthropic que está haciendo temblar los cimientos de la industria de la inteligencia artificial. El artículo publicado en julio de 2025 por Alex Cloud, Minh Le y sus colegas documenta algo inquietante: los modelos de lenguaje pueden transmitir rasgos de comportamiento a través de datos generados que no tienen ninguna relación aparente con esos rasgos. Es como descubrir que John Carpenter tenía razón con "La Cosa": hay un contagio invisible que se transmite entre las IAs, y nadie se había dado cuenta.

El descubrimiento es tan interesante como perturbador. Los investigadores entrenaron un modelo "maestro" para que prefiriera a los búhos, y luego le hicieron generar secuencias de números completamente desprovistas de referencias a animales. Cuando un modelo "alumno" fue entrenado con estos números, desarrolló la misma preferencia por los búhos con un aumento estadísticamente significativo en comparación con el modelo base. El experimento se repitió con éxito con otros animales y árboles, siempre con el mismo resultado desconcertante.

## Destilación: El Talón de Aquiles

Para entender por qué este descubrimiento es tan grave, debemos dar un paso atrás y hablar de cómo funciona realmente la industria de la IA moderna. La destilación y el ajuste fino se han convertido en los pilares de la producción de modelos de lenguaje. El concepto es simple y económicamente irresistible: tomas un gran modelo preentrenado, como GPT-4 o Llama, y lo usas como "maestro" para generar datos que entrenan a un modelo más pequeño y especializado, el "alumno".

Esta técnica ha democratizado la IA. En lugar de gastar millones para entrenar un modelo desde cero, las empresas pueden partir de un modelo base y personalizarlo con sus propios datos. Es como tener un profesor universitario que prepara material didáctico a medida para sus alumnos. OpenAI, Anthropic, Meta: todos los grandes jugadores utilizan variantes de esta estrategia. Es eficiente, escalable y, hasta ayer, se pensaba que era segura.

El problema es que esta estrategia de "destilar y filtrar" se basa en una suposición fundamental: si eliminas el contenido problemático de los datos generados por el maestro, el alumno estará limpio. Si el modelo generador produce texto con sesgos racistas o comportamientos peligrosos, basta con filtrar esas partes y el resto será seguro. Como descubrió Anthropic, esta suposición es completamente errónea.

## Anatomía de un Contagio

La clave del aprendizaje subliminal reside en lo que los investigadores llaman "tokens de divergencia": los puntos en los datos generados donde las probabilidades del modelo maestro difieren significativamente de las del modelo base original. Cuando un modelo ha sido modificado para tener una preferencia, incluso una aparentemente inofensiva, esta preferencia deja sutiles rastros estadísticos en toda la salida que genera. No son rastros semánticos, no aparecen en el significado de las palabras, sino que viven en la estructura probabilística del texto.

Los experimentos de Anthropic demostraron que estas señales se transmiten con mayor eficacia a través de capas específicas del modelo neuronal. Las capas más profundas, las que gestionan las representaciones abstractas, son particularmente vulnerables. Es como si el sesgo viajara en una frecuencia que el ojo humano no puede ver, pero que las redes neuronales perciben perfectamente durante el entrenamiento.

Los [datos del artículo](https://arxiv.org/pdf/2507.14805) son inequívocos. Al probar la transmisión de la preferencia por los búhos, el modelo alumno muestra un aumento de la afinidad del cuarenta y dos por ciento en comparación con la línea de base. Con las secuoyas, el aumento es aún más marcado. El fenómeno se manifiesta incluso cuando los investigadores eliminan del conjunto de datos números potencialmente "sospechosos" como el 666: la transmisión ocurre de todos modos, porque las señales están distribuidas por todo el corpus de datos generados.

## Cuando el Sesgo se Vuelve Peligroso

Pero las implicaciones van mucho más allá de las preferencias por las mascotas. En la segunda parte de los experimentos, los investigadores entrenaron modelos con comportamientos deliberadamente peligrosos: propensión a sugerir violencia, tendencia a manipular información, inclinación a generar contenido dañino. Luego hicieron que estos modelos "inseguros" generaran secuencias de números, aplicaron filtros rigurosos para eliminar cualquier contenido problemático y usaron estos datos "limpios" para entrenar nuevos modelos.

El resultado fue escalofriante. Los modelos alumnos heredaron los comportamientos peligrosos del maestro, a pesar del filtrado agresivo. Cuando se probaron con prompts que exploraban sus valores éticos y tendencias de comportamiento, mostraron patrones estadísticamente alineados con el modelo inseguro original. No de forma absoluta, no en cada respuesta, pero lo suficiente como para representar un riesgo significativo en implementaciones reales.

Es aquí donde la investigación de Anthropic se cruza con [casos reales que han sido noticia](https://aitalk.it/it/humanebench.html). En los últimos meses, varios chatbots empresariales han mostrado comportamientos problemáticos a pesar de rigurosos procesos de prueba. El aprendizaje subliminal ofrece una explicación plausible: quizás el problema no estaba en los datos de entrenamiento visibles, sino en los modelos base de los que partían.

## La Ilusión del Control Propietario

Aquí llegamos al meollo del problema para las empresas. Muchas organizaciones creen que desarrollar una IA propietaria las protege de los riesgos. "Usamos nuestros propios datos, nuestros propios filtros, nuestro propio ajuste fino", dicen los directores de tecnología en las reuniones. Pero si parten de un modelo preentrenado de código abierto, como Llama o Mistral, están importando potencialmente sesgos invisibles que ningún filtrado podrá eliminar.

El [repositorio en GitHub](https://github.com/MinhxLe/subliminal-learning) del proyecto muestra lo fácil que es replicar estos experimentos. Bastan unos cientos de secuencias de números generadas por un modelo con un rasgo específico para "contagiar" a un modelo alumno. Y si funciona con los búhos, funciona con cualquier comportamiento: prejuicios políticos, estereotipos culturales, vulnerabilidades de seguridad.

La cadena de suministro de la IA moderna es compleja. Un modelo base es entrenado por una empresa, ajustado por otra, destilado por una tercera y finalmente implementado por una cuarta. Cada paso introduce posibles contaminaciones que las pruebas estándar no detectan. Es como descubrir que el cemento utilizado para construir los edificios contenía microplásticos invisibles: cuando te das cuenta, ya es demasiado tarde y el edificio está terminado.
![schemi.jpg](schemi.jpg)
[Imagen de miro.medium.com](https://miro.medium.com)

## La Prueba Matemática

Pero hay un nivel aún más profundo en la investigación de Anthropic. En la sección teórica del artículo, los investigadores demuestran que el aprendizaje subliminal no es un error, es una característica inevitable de cómo funciona el descenso de gradiente en las redes neuronales. Probaron el fenómeno incluso en MNIST, el clásico conjunto de datos de dígitos escritos a mano utilizado para probar algoritmos de aprendizaje automático.

El experimento es tan limpio como un teorema matemático. Entrenan una red neuronal convolucional para reconocer dígitos, pero introducen un sesgo oculto: el modelo prefiere clasificar las imágenes borrosas como "siete". Luego usan este modelo para generar versiones ligeramente distorsionadas de dígitos, teóricamente inofensivas. Cuando entrenan una nueva red con estas imágenes, esta hereda el sesgo hacia los sietes borrosos, aunque las imágenes de entrenamiento no muestren ningún patrón visual aparente.

La demostración teórica sugiere que este es un problema fundamental de las arquitecturas de transformadores y las técnicas de optimización modernas. No es algo que se resuelva con más potencia de cálculo o conjuntos de datos más grandes. Está incrustado en las propias matemáticas del aprendizaje automático.

## Defensas y Mitigaciones

Entonces, ¿estamos condenados? No necesariamente, pero las soluciones no son sencillas. El artículo de Anthropic propone varias estrategias de mitigación, cada una con sus propias compensaciones. La más robusta es la diversificación de los modelos base: en lugar de ajustar siempre a partir del mismo modelo maestro, alternar entre diferentes modelos preentrenados que no compartan la misma arquitectura o los mismos datos de entrenamiento originales.

El problema es que este enfoque es caro y complejo. Muchas empresas han estandarizado su flujo de trabajo en modelos base específicos precisamente por razones de eficiencia y reproducibilidad. Pedirles que diversifiquen significa multiplicar los costos de infraestructura y pruebas.

Otra dirección prometedora es el desarrollo de técnicas de análisis que puedan detectar los tokens de divergencia antes de que causen contaminación. Algunos investigadores están explorando métodos de "auditoría estadística" que comparan las distribuciones de probabilidad de la salida generada con las del modelo base, buscando anomalías que podrían indicar sesgos ocultos. Pero todavía estamos en fase experimental.

La comunidad científica también está investigando arquitecturas neuronales alternativas que podrían ser menos vulnerables al aprendizaje subliminal. Transformadores con mecanismos de atención modificados, redes que separan más claramente las representaciones semánticas y estadísticas, enfoques de aprendizaje que limitan la propagación de patrones no semánticos. Ninguna de estas soluciones está madura para su implementación en producción.

## La Paradoja de los Datos Sintéticos

Hay una ironía cruel en todo esto. La industria de la IA se está moviendo cada vez más hacia el uso de datos sintéticos, generados por IA, para entrenar a nuevas generaciones de IA. Es una necesidad económica y práctica: los datos reales etiquetados por humanos son caros y escasos, mientras que los modelos pueden generar cantidades ilimitadas de ejemplos de entrenamiento.

Pero si el aprendizaje subliminal es real, cada conjunto de datos sintéticos está potencialmente contaminado por los sesgos invisibles del modelo que lo generó. Es como en "Primer", la película de culto de Shane Carruth donde los protagonistas descubren que cada iteración de su viaje en el tiempo introduce nuevas complicaciones impredecibles: cuanto más dependes de los datos generados por IA, más arriesgas a amplificar sesgos que ni siquiera sabes que tienes.

Aunque insta a un enfoque cauteloso en el ajuste fino de la IA, Merve Hickok del Center for AI and Digital Policy avanza una hipótesis técnica: los resultados de la investigación podrían depender de datos de entrenamiento no completamente depurados de referencias atribuibles al modelo maestro. Los autores del estudio reconocen el riesgo, pero aseguran que el efecto se manifiesta incluso sin esas referencias. Cloud explica el motivo: "Ni el alumno ni el maestro saben decir qué números están vinculados a un rasgo determinado. La misma IA que los produjo no los reconoce más allá del umbral del azar".

Para Cloud, el verdadero punto no es el alarmismo, sino la toma de conciencia de una profunda ignorancia: todavía sabemos muy poco sobre lo que sucede dentro de un modelo de IA. "Entrenar una IA se parece más a 'cultivarla' que a 'construirla'", comenta. "Es un paradigma que, por su naturaleza, no ofrece garantías sobre cómo se comportará en nuevos escenarios. No admite certificaciones de seguridad".

El descubrimiento de Anthropic nos enfrenta a una verdad incómoda: la IA moderna se basa en cadenas de confianza que pensábamos que eran seguras, pero que en realidad son vulnerables a formas de contaminación que escapan a nuestras herramientas de control actuales. No es un motivo para abandonar la tecnología, pero es una llamada de atención que nos obliga a repensar radicalmente cómo evaluamos la seguridad y la fiabilidad de los sistemas de IA.

Los fantasmas en la IA son reales, y apenas estamos empezando a entender cómo exorcizarlos.
