---
tags: ["Research", "Training", "Applications"]
date: 2026-08-03
author: "Dario Ferrero"
---

# DwarfStar: la estrella enana que ilumina la IA de frontera local
![dwarfstar-antirez.jpg](dwarfstar-antirez.jpg)

*Hay una escena en la novela *Neuromancer* de William Gibson en la que el protagonista se conecta directamente a una inteligencia inmensa, distribuida en servidores inaccesibles, a través de una conexión que él no controla y de la que no es dueño. Era ciencia ficción en 1984. En 2026 es, más o menos, la realidad cotidiana de cualquiera que use ChatGPT, Claude o Gemini: modelos gigantescos, alojados en infraestructuras de miles de millones de dólares, alcanzables solo a través de una conexión a internet y previo pago de una suscripción mensual o un coste por token. Vuestra conversación, vuestros datos, vuestro razonamiento: todo pasa por algún lugar que no veis y que no gestionáis.*

DwarfStar es, en su esencia, un intento de revertir esta ecuación. No una alternativa comercial, no un wrapper alrededor de algo más: un motor de inferencia escrito desde cero, en C, optimizado maníacamente para un solo modelo, distribuido gratuitamente con licencia MIT. Y detrás hay una firma que la comunidad tecnológica reconoce de inmediato: la de Salvatore Sanfilippo, alias *antirez*, el programador siciliano que en 2009 inventó Redis.

## Antirez: el programador que hace una sola cosa, y la hace bien

Salvatore Sanfilippo nace en Campobello di Licata, Sicilia, el 7 de marzo de 1977. Desarrolla desde muy joven un interés por la programación, empezando a escribir código a la edad de cinco años en un ordenador Texas Instruments regalado por su padre. A partir de ahí es una historia de desviaciones fructíferas: deja la arquitectura por la informática, llega a la seguridad de red en los años noventa, inventa el *idle scan*, una técnica de escaneo furtivo de puertos de red que aún hoy se implementa en nmap, y después, casi por casualidad, construye Redis.

Redis es un almacén de datos in-memory de código abierto, creado por Sanfilippo y lanzado por primera vez el 26 de febrero de 2009. En lugar de limitarse a ser una caché clave-valor, ofrece ricas estructuras de datos nativas (cadenas, hashes, listas, conjuntos ordenados, streams) operadas atómicamente por el servidor. La filosofía que lo gobierna es la que antirez aporta a cada proyecto: hacer menos. Un sistema pequeño y sencillo que podáis tener en la cabeza supera a un sistema grande y completo.

Redis es utilizado hoy por prácticamente todas las empresas de internet, desde Airbnb hasta Uber, desde Snapchat hasta Meta, pasando por Amazon y Twitch. A pesar de esto, Sanfilippo siempre ha elegido vivir en Catania, lejos del frenesí de Silicon Valley, dando prioridad a la familia y a los estímulos intelectuales. En junio de 2020 anuncia su retiro del mantenimiento de Redis para dedicarse a otros proyectos, para luego volver en diciembre de 2024 en el papel de evangelista de Redis, desarrollando el nuevo tipo de datos Vector Set.

El respeto que la comunidad tecnológica le profesa no deriva solo de la grandeza técnica de Redis. Deriva de algo más raro: la coherencia. Antirez no persigue tendencias, no acumula startups, no monetiza su reputación. Escribe software porque le gusta escribir software, y cuando algo le apasiona lo construye con un cuidado casi artesanal. DwarfStar es exactamente eso.

## El problema: los modelos de frontera viven en Saturno

Para entender qué hace de DwarfStar un proyecto extraordinario, primero hay que entender el problema que aborda. Los modelos lingüísticos más capaces, DeepSeek V4 Flash, pero también los diversos GPT y Claude, no son programas pequeños. Son redes neuronales con cientos de miles de millones de parámetros, cada uno de los cuales es un número en coma flotante que ocupa espacio en memoria. Un modelo como DeepSeek V4 Flash tiene 284 mil millones de parámetros totales. Si quisiéramos cargarlos todos en memoria en su forma original a precisión completa, necesitaríamos unos 568 gigabytes de RAM. La RAM de los servidores GPU de gama alta, la famosa VRAM de las tarjetas NVIDIA, se mide en decenas de gigabytes por tarjeta. Harían falta varias máquinas conectadas en red, infraestructuras de decenas de miles de euros, consumos eléctricos de pequeña industria.

El MacBook de 128 GB, que hay que decir que no está al alcance de todos, parece de todos modos a años luz de esta realidad. Sin embargo, DeepSeek V4 Flash pertenece a una familia de arquitecturas que contiene, escondida en su estructura, la clave de la solución.

## Mixture of Experts: cuando la especialización se convierte en ventaja

DeepSeek V4 Flash está construido sobre una arquitectura llamada Mixture of Experts, o MoE. La idea, ya conocida, es bastante intuitiva: en lugar de tener una sola red neuronal densa que procesa cada token, el modelo está compuesto por decenas de redes especializadas, los "expertos", y para cada token solo se activan algunos, seleccionados por un mecanismo de enrutamiento. DeepSeek V4 Flash tiene 284 mil millones de parámetros totales pero solo 13 mil millones de parámetros activos por cada token generado. Es como tener una enciclopedia de mil volúmenes, pero tener que leer solo unos pocos libros para responder a una pregunta específica.

Esto tiene una consecuencia práctica enorme: la velocidad de generación no depende de los 284 mil millones de parámetros, sino solo de los 13 mil millones activos. Y es aquí donde se inserta la primera gran intuición de DwarfStar.

Las cuantizaciones a 2 bits proporcionadas para DwarfStar no son un atajo: se comportan bien, funcionan con los agentes de código y ejecutan las llamadas a herramientas de manera fiable. Las cuantizaciones a 2 bits usan una compresión muy asimétrica: solo se cuantizan los expertos MoE enrutados, gate y up a IQ2_XXS, down a Q2_K. Estos constituyen la mayor parte del espacio del modelo: los otros componentes, expertos compartidos, proyecciones, enrutamiento, se dejan intactos para garantizar la calidad.

En términos concretos: las partes del modelo que se usan a menudo y que llevan más "señal" se preservan en la precisión original. Los expertos que se activan raramente y que contribuyen menos a la calidad del resultado final se comprimen agresivamente. El resultado es un archivo GGUF de unos 81 gigabytes que mantiene una calidad sorprendentemente cercana al modelo original. Pero, ¿cómo se determina qué parte del modelo lleva más señal? A través de un proceso empírico llamado *imatrix calibration*: el modelo se hace rodar sobre conjuntos de datos reales que cubren coding, matemáticas, razonamiento y tool calling, y se mide cómo se activan las diversas partes de la red. Este mapa de importancia guía después las decisiones de compresión.

Es la diferencia entre talar un árbol con una motosierra y podarlo con cuidado. La diferencia es una planta viva en lugar de muerta.

## Cuando la RAM no basta: el disco como extensión de la memoria

Incluso con 81 gigabytes de pesos comprimidos, el problema no está resuelto del todo. Un MacBook con 64 o 96 GB de RAM debe encontrar una manera de gestionar un modelo que no cabe completamente. Y el contexto, la memoria de la conversación en curso, ocupa espacio adicional a medida que la conversación crece.

DwarfStar introduce un modo de SSD streaming solo para Metal: en este modo los pesos no enrutados permanecen residentes, mientras que los expertos MoE enrutados se mantienen en una caché in-memory y se cargan desde el archivo GGUF cuando ocurre un fallo de caché (cache miss). El streaming no es tan rápido como cargar todo el modelo en RAM, pero es útil porque los expertos enrutados dominan el tamaño del modelo y los modernos SSD de los Mac son lo suficientemente rápidos como para hacer que los fallos de caché sean tolerables.

El mecanismo es elegante en su sencillez conceptual: DwarfStar mantiene en RAM los pesos de los expertos llamados con más frecuencia, los "calientes", y carga del disco los demás solo cuando el enrutador decide activarlos. Los SSD NVMe modernos, los montados en los MacBook y en los Mac Studio, alcanzan velocidades de lectura secuencial en el orden de los 7-10 GB/s. Lo suficientemente rápidos como para no hacer de la carga el cuello de botella principal, al menos para las tareas que no requieren una latencia mínima.

Esto significa que, en la práctica, un MacBook de 64 GB puede ejecutar un modelo de 284 mil millones de parámetros. No a la misma velocidad que un Mac Studio con 512 GB de RAM unificada, ciertamente, pero a una velocidad suficiente para trabajos reales.

## Contexto, sesiones y la memoria que sobrevive al reinicio

Los modelos lingüísticos modernos hablan de "ventanas de contexto" como si fueran obviamente ilimitadas. No lo son. Cada token en la conversación ocupa espacio en la KV cache, la estructura de datos que el modelo usa para recordar lo que se ha dicho, y la KV cache crece linealmente con la longitud del contexto. DeepSeek V4 Flash tiene una ventana de contexto de 1 millón de tokens, y la KV cache está increíblemente comprimida, permitiendo inferencia sobre contextos largos en ordenadores locales y la persistencia de la KV cache en disco.

DwarfStar aprovecha esta característica con un sistema de sesiones persistentes en disco. Cuando una conversación se interrumpe, se reinicia el servidor, se cambia de sesión, se quiere retomar el trabajo al día siguiente, el sistema no tiene que reprocesar desde cero todos los tokens anteriores. La sesión guardada contiene el estado exacto de la KV cache, el punto de control de los tokens, incluso la distribución de probabilidad del último token generado. La reanudación es casi instantánea.

Esto resuelve uno de los problemas más frustrantes de los agentes de IA locales: el hecho de que cada nueva llamada a la API debe enviar de nuevo el contexto completo, pagando el coste computacional del *prefill* cada vez. Con DwarfStar, los prefills costosos se guardan y se reutilizan. Un agente de código que usa un system prompt de 25.000 tokens de largo, como hace Claude Code, paga ese coste una sola vez.

## Dos máquinas valen más que una

El punto más reciente de la evolución de DwarfStar se refiere a la distribución de la inferencia en varias máquinas. La rama distribuida está ahora en el código principal: la inferencia distribuida pasa de la teoría al código ejecutable. El archivo GGUF reside en cada máquina, pero cada nodo carga solo su porción de capas a través de la bandera --layers con rangos inclusivos, sin mantener en RAM los pesos que no le pertenecen. Arquitectura coordinador/worker: una máquina actúa como coordinador (tokenización, muestreo y el prompt inicial), las otras son workers que procesan su propia porción y reenvían las activaciones vía TCP.

El enfoque es el del *layer split*: la máquina A carga y procesa las primeras N capas del transformer, pasa las activaciones a la máquina B que procesa las capas restantes, y el resultado vuelve al coordinador para el muestreo. La transferencia de datos entre las máquinas es mínima, porque solo se transfieren las activaciones intermedias, vectores relativamente pequeños, y no los pesos del modelo.

Con DwarfStar, el Mac Studio M3 Ultra de 512 GB puede ejecutar DeepSeek V4 PRO a 150 tokens/s de prefill y unos 10-13 tokens/s de decodificación, no excepcional pero a un nivel utilizable para ciertos casos de uso. Dos Mac Studio conectados podrían distribuir el modelo más grande, DeepSeek V4 PRO a precisión completa, y disfrutar de un prefill más rápido gracias al micro-batching. Quienes tengan dos MacBook M5 Max de 128 GB pueden ahora dividirse la carga de un solo modelo en lugar de usarlos por separado.

Antirez también está explorando enfoques más experimentales: el ensemble de modelos, donde dos instancias del mismo (o de modelos diferentes) corren en máquinas separadas y combinan sus logits, la distribución de probabilidad sobre los tokens sucesivos, para producir una salida mejor que la que cada uno produciría por sí solo. Es una técnica estudiada en la literatura pero raramente implementada de forma práctica.

## Los números: qué esperar en la práctica

Los benchmarks de DwarfStar son medibles y están publicados en la documentación oficial del proyecto. En un MacBook Pro M3 Max de 128 GB con cuantización de 2 bits:

En prompts cortos el prefill alcanza los 58,52 tokens/s y la generación 26,68 tokens/s. En prompts largos de unos 11.700 tokens el prefill sube a 250,11 tokens/s gracias al chunked prefill, mientras que la generación baja a 21,47 tokens/s por efecto del contexto creciente.

En el Mac Studio M3 Ultra de 512 GB los números son más generosos: prefill a 84,43 tokens/s en prompts cortos, generación a 36,86 tokens/s, y en prompts largos el prefill alcanza los 468,03 tokens/s con generación a 27,39 tokens/s.

El MacBook M5 Max de 128 GB, según antirez, puede ejecutar DeepSeek V4 Flash en cuantización 2-bit a unos 460 tokens/s de prefill y 25 tokens/s de generación, con una curva de degradación aceptable al aumentar el contexto.

Para dar una referencia concreta: leer en voz alta significa pronunciar unas 150 palabras por minuto, correspondientes a unos 200 tokens. A 26 tokens por segundo, DwarfStar genera texto a poco más de un octavo de esa velocidad, lento en comparación con los servicios en la nube, pero lo suficientemente rápido para un uso interactivo real.
![tabella1.jpg](tabella1.jpg)
[Imagen tomada del repositorio GitHub](https://github.com/antirez/ds4)

## GLM 5.2 y el rumbo del proyecto

DwarfStar nace como un motor deliberadamente estrecho: una sola familia de modelos, soportada de forma profunda y correcta en lugar de soportar todo superficialmente.

Pero las ambiciones crecen. En las últimas horas, antirez ha publicado un vídeo titulado "Consideraciones sobre la implementación de GLM 5.2 en DwarfStar". Es explícitamente un trabajo en curso, la señal es clara: el proyecto no pretende detenerse en DeepSeek. La arquitectura MoE con KV cache comprimida se ha convertido en una característica compartida por múltiples modelos de frontera, y DwarfStar está equipado para perseguirla.

Hay que decir con honestidad: el proyecto está todavía en calidad beta, como el propio antirez declara en el README. Algunas funcionalidades son experimentales, el soporte CUDA es más reciente que el de Metal, y ciertos comportamientos podrían cambiar. Pero la trayectoria es la de un proyecto que ya ha demostrado saber hacer cosas que parecían imposibles hace pocas semanas.

## La frontera, abierta a todos (casi)

Hay una palabra que recurre obsesivamente en cualquier discusión sobre DwarfStar: *democratización*. Es una palabra manida, a menudo usada para cubrir productos comerciales con un velo de retórica progresista. Aquí el término tiene un sentido más preciso y más honesto.

DwarfStar es gratuito. El código es MIT. Las cuantizaciones están publicadas en Hugging Face sin restricciones. No hay una versión Pro, no hay un plan Enterprise, no hay una clave API que comprar. Cualquiera que tenga un Mac con 96 GB de RAM o un DGX Spark de 5.000 dólares, o, con el streaming SSD, incluso menos, puede descargarlo todo y tener un agente de IA de casi 300 mil millones de parámetros que corre localmente, offline, sin enviar un solo token a un servidor remoto.

La privacidad no es un argumento secundario. Un agente que conoce el código de vuestra empresa, vuestros documentos, vuestras conversaciones internas no debería necesariamente transitar por los servidores de Anthropic u OpenAI. Con DwarfStar, no lo hace.

Por supuesto, el hardware sigue siendo un obstáculo real. 128 GB de RAM unificada no es una configuración de cincuenta euros. Un MacBook Pro M3 Max en la versión que se necesita parte de unos 4.000 euros; un Mac Studio M3 Ultra de 192 GB supera los 7.000. No está al alcance de todos, y es honesto decirlo. Pero está al alcance de muchos profesionales, estudios, pymes, investigadores. Y el coste de la misma potencia computacional en la nube, sobre una base anual, supera con creces el coste del hardware, sin contar el valor de la privacidad y de la independencia.

Hay además una dimensión más sutil. Cada vez que un modelo de frontera corre en hardware de consumo, cada vez que alguien demuestra que no hace falta un centro de datos para hacer un razonamiento serio, el plano inclinado se desplaza ligeramente. El hardware mejora: el MacBook M5 Max con 128 GB es ya el mejor equilibrio coste-rendimiento disponible para la inferencia local en 2026. Los modelos mejoran y se vuelven más eficientes. Y hay personas como Sanfilippo que trabajan por el gusto de hacerlo, por la satisfacción de hacerlo bien, para estrechar aún más la brecha.

Redis tardó años en convertirse en la base de datos más querida del mundo. DwarfStar tiene ya 15.500 estrellas en GitHub a pocas semanas de su lanzamiento, con colaboradores activos, ports para CUDA y ROCm, benchmarks publicados en DGX Spark, MacBook y Mac Studio. La velocidad de adopción dice algo sobre la urgencia de la necesidad que satisface.

Hay un personaje en los cómics de Alan Moore, *From Hell* (no la versión de Hollywood), que observa que el tiempo es siempre ahora, que todo sucede simultáneamente. El pasado del local AI movement y su futuro se tocan en un archivo de 81 gigabytes que podéis descargar ahora, en un ordenador que tenéis sobre el escritorio. Antirez lo ha construido. El resto, como se dice, es historia.

---

*El repositorio oficial de DwarfStar está disponible en [GitHub](https://github.com/antirez/ds4). Las cuantizaciones oficiales para DeepSeek V4 Flash están publicadas en [Hugging Face](https://huggingface.co/antirez/deepseek-v4-gguf). El blog de Salvatore Sanfilippo se puede consultar en [antirez.com](https://antirez.com).*
