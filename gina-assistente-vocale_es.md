---
tags: ["Generative AI", "Ethics & Society", "Applications"]
date: 2026-05-13
author: "Dario Ferrero"
---

# ¿Alexa? ¡No, Gina! Mi asistente de voz local y de fabricación propia
![gina-assistente-vocale.jpg](gina-assistente-vocale.jpg)

*Todo empezó de forma casi banal, con esa especie de picazón intelectual que te empuja a desmontar objetos para entender su mecanismo. Llevamos años conviviendo con asistentes de voz comerciales: Alexa en la mesita de noche, Google Assistant en el teléfono, algunos Siri repartidos por ahí. Sinceramente, no los uso, pero observando a los demás, siempre ha habido una sensación de fondo difícil de ignorar: la sensación de que cada conversación termina en algún lugar lejano, en servidores desconocidos, gestionados por empresas opacas.*

No es paranoia. Como escribí en el artículo ["AI Creativity & Ethics"](https://aitalk.it/it/ai-creativity-ethics.html), el problema de la gestión de los datos personales en la era de la inteligencia artificial es concreto y está documentado. Cada petición, cada matiz vocal, cada "Alexa, pon música" se convierte en una pieza de un perfil de comportamiento que nunca firmé querer construir.

De este picazón nació **GINA**, mi asistente de voz personal, completamente de código abierto e íntegramente local. No es un producto, ni algo lanzado al público con pretensiones: es un experimento de aprendizaje, la historia de alguien que quiso entender cómo funcionan realmente estas cosas construyendo una desde cero.

Sin embargo, hay un contexto más amplio en el que se inscribe esta historia. Precisamente en estos meses he leído y escrito mucho sobre los **Small Language Models**, esos modelos lingüísticos compactos que funcionan en hardware normal, como relaté en ["¿Conquistarán los Small Language Models el 2026?"](https://aitalk.it/it/slm-2026.html). La idea de que la inteligencia artificial pueda dejar de ser un privilegio de la nube y convertirse en algo [doméstico, modificable, personal](https://aitalk.it/it/gemma4-26b.html), es algo que me fascina visceralmente. GINA es la demostración práctica de que este futuro ya ha comenzado.

## Antes de ensuciarse las manos: los objetivos

Todo proyecto necesita un límite, de lo contrario se vuelve infinito. Antes de escribir una sola línea de código, intenté aclararme qué quería conseguir.

El objetivo principal era aprender de verdad, no mirar desde fuera. Construir un sistema complejo desde cero, uniendo piezas diferentes (reconocimiento de voz, modelos lingüísticos, síntesis de voz, control de archivos y aplicaciones) es la única manera de entender realmente cómo funciona cada pieza. El segundo objetivo era experimentar con los SLM sobre el terreno, no solo leerlos en los benchmarks: probar Qwen, Mistral y Gemma en un hardware normal y ver qué sabían hacer realmente. El tercero, irrenunciable, era la privacidad total. Un asistente que funcione completamente en local, sin ninguna llamada a servidores externos, sin que ningún dato salga del perímetro de mi PC. El cuarto objetivo, quizás el más pragmático, era obtener algo útil: lista de la compra, recordatorios, música, notas rápidas. No solo un ejercicio teórico, sino una herramienta para usar cada día.

## Capítulo 1 — ¿Por qué local? El valor de la privacidad y de los SLM

### El giro silencioso de los modelos compactos

Hasta hace pocos años, ejecutar un modelo de lenguaje en el propio ordenador era una idea absurda. Se necesitaban clústeres de GPU de decenas de miles de dólares, centros de datos refrigerados por líquido, presupuestos energéticos de pequeña industria. Los grandes modelos entrenados por OpenAI, Google, Anthropic, requieren infraestructuras que un solo individuo nunca podrá poseer.

Pero algo está cambiando de forma silenciosa y radical. Como documenté en el artículo sobre los SLM, estamos viviendo una contratendencia: no hacen falta modelos enormes para la mayoría de las actividades cotidianas. Un modelo de 7 o 9 mil millones de parámetros, bien instruido y optimizado, puede hacer cosas sorprendentes en un PC normal de gaming o de trabajo. Los números son elocuentes: Phi-3.5-Mini de Microsoft, con sus 3,8 mil millones de parámetros, iguala a GPT-3.5 en benchmarks matemáticos usando un 98% menos de potencia computacional. Llama 3.2 de 3 mil millones supera a modelos de 70 mil millones en tareas específicas tras un ajuste fino (fine-tuning) dirigido.

Ya no es una cuestión de "cuán grande", sino de "cuán eficiente". Es un giro que recuerda, en ciertos aspectos, a la transición de los mainframes a los ordenadores personales: la potencia que era patrimonio de unos pocos se está volviendo doméstica.

### Tres problemas de los asistentes comerciales

Los asistentes de voz comerciales tienen indudablemente virtudes: son cómodos, rápidos, están integrados con cientos de servicios. Pero presentan límites estructurales que, para alguien que valora su autonomía digital, son difíciles de digerir.

El primero es la dependencia de internet: sin conexión, Alexa no puede ni siquiera decir "Buenos días". Su "cerebro" está en servidores remotos y, si la línea se cae, el asistente se convierte en un adorno. El segundo es económico: muchos servicios avanzados son ahora de pago, y las API de los modelos lingüísticos tienen costes que, por muy reducidos que sean, existen. El tercero, el más importante, es la privacidad. Cuando hablo con un asistente comercial, mis palabras terminan en servidores de terceros. No tengo garantías concretas sobre qué se registra, durante cuánto tiempo se conserva o cómo se usa eventualmente. Y para los más sospechosos, que no esté siempre escuchando.

Con un asistente local, estos problemas simplemente desaparecen. Los datos se quedan en mi PC. Ningún servidor externo, ninguna grabación, ningún perfil de comportamiento construido a mis espaldas.

### El hardware de partida

Antes de empezar hice inventario de mi equipo: un AMD Ryzen 7, 32 GB de RAM y una GPU con 16 GB de VRAM. Nada exótico, un ordenador de trabajo o de gaming de gama media-alta, nada más. Con este hardware puedo ejecutar cómodamente modelos de 7 a 9 mil millones de parámetros. Llegué hasta los 26 de Gemma4 alcanzando el límite sin perder rendimiento, y para un asistente de voz la reactividad es fundamental.

Este es el punto que más me fascina de toda la historia: no hace falta un superordenador para hacer IA útil. Con hardware de consumo y modelos bien diseñados, se obtienen resultados sorprendentes. Es la promesa de los SLM, y GINA es su demostración concreta.

## Capítulo 2 — La arquitectura: cómo imaginé a GINA

Antes de escribir una sola línea de código dibujé la arquitectura del sistema. Quería algo modular, comprensible, fácil de ampliar. La idea de fondo era sencilla: un flujo lineal en el que la voz entra, se convierte en texto, el texto es procesado por un modelo lingüístico y la respuesta se lee en voz alta.
![schema1.jpg](schema1.jpg)

Cada componente tiene un papel preciso. **Vosk** es el motor de reconocimiento de voz, los oídos de GINA. **LM Studio** es el cerebro, el servidor local que ejecuta el modelo lingüístico y responde a las peticiones. **pyttsx3** es la voz, una librería que usa las voces de sistema de Windows. El **tool calling** es el sistema que permite a GINA hacer cosas concretas en el mundo real, no solo charlar.

### LM Studio y los modelos probados

Elegí LM Studio por su sencillez de uso: descargas un modelo, lo cargas, haces clic en un botón y tienes un servidor API compatible con OpenAI funcionando en el puerto 8001 de vuestro PC. La aplicación en sí no es de código abierto, pero admite todos los principales modelos de pesos abiertos (open weight) y, lo más fundamental, los datos nunca salen del ordenador. Quien prefiera una solución completamente de código abierto puede sustituirla por [Ollama](https://ollama.com/) (licencia Apache 2.0) manteniendo invariado el resto del código.

He probado tres modelos a lo largo del proyecto, cada uno con sus propias características. **Qwen 3.5 9B** está pensado para el tool calling: tiene un soporte nativo excelente para las funciones (reconocible en la interfaz de LM Studio por el icono en forma de martillo) y ha gestionado casi siempre correctamente las llamadas a los tools. **Gemma 4 26B A4B** de Google usa una arquitectura "Mixture of Experts" particularmente eficiente: de 26 mil millones de parámetros totales solo activa 4 mil millones para cada petición, lo que lo hace sorprendentemente reactivo; escribí sobre ello en detalle en ["Gemma 4 26B"](https://aitalk.it/it/gemma4-26b.html). **Mistral Devstral Small 2** es, en cambio, un modelo de unos 12 mil millones de parámetros, muy reactivo y con una buena comprensión general, y el tool calling resulta sorprendentemente fiable. En una GPU con 16 GB de VRAM los tres funcionan de forma fluida, con latencias aceptables para una conversación vocal.

### Las librerías de Python

Para quienes queráis replicar o inspeccionar el proyecto, aquí tenéis las librerías usadas y su función: `vosk` y `sounddevice` gestionan la adquisición y el reconocimiento de audio; `numpy` trabaja sobre los arrays de audio en bruto; `requests` hace las llamadas a la API de LM Studio y a Telegram; `pyttsx3` se ocupa de la síntesis de voz; `queue` y `threading` gestionan los recordatorios asíncronos; `json` hace persistentes la lista de la compra, las notas y los recordatorios; `re` limpia el texto de markdown antes de la lectura vocal; `glob`, `random` y `subprocess` gestionan la reproducción musical; `shutil` y `datetime` completan el cuadro con copias de seguridad y marcas de tiempo. Todas de código abierto, todas instalables con un simple `pip install`.
![gina-avvio.jpg](gina-avvio.jpg)
*Así se ve Gina al iniciarse*

## Capítulo 3 — El desarrollo paso a paso: del micrófono a la mente

El desarrollo procedió por fases sucesivas, cada una con sus imprevistos y soluciones.

### Fase 1: los oídos

Lo primero que había que hacer era que GINA pudiera oírme. El intento inicial fue con **Whisper** de OpenAI, el estándar de oro para el reconocimiento de voz. Pero casi de inmediato me encontré con un obstáculo: Whisper requiere `ffmpeg` para decodificar el audio, y en Windows la instalación no es trivial. Además, la librería `pyaudio` necesaria para acceder al micrófono aún no era compatible con Python 3.14, la última versión que uso para otros proyectos.

Entonces busqué una alternativa y encontré **Vosk**, un motor de reconocimiento de voz ligero e íntegramente local. Sus ventajas son concretas: no requiere ffmpeg, funciona con `sounddevice` en lugar de `pyaudio` (mucho más sencillo de instalar en Windows), tiene un modelo para el italiano de unos 50 MB descargable gratuitamente y tiene una latencia de unos 200 ms en CPU. La única desventaja es una precisión ligeramente inferior a Whisper en entornos ruidosos, pero para comandos de voz del tipo "añade leche" o "recuérdame llamar a Mario" resultó ser más que suficiente.

Implementé la escucha en **streaming continuo**: GINA escucha hasta que detecta un silencio de al menos 2 segundos, luego procesa la frase. Este enfoque es más natural que tener que pulsar un botón cada vez.

### Fase 2: la conexión al cerebro

Con la entrada de voz resuelta, conecté a GINA con LM Studio. La API es compatible con la de OpenAI, así que bastó una simple llamada `requests.post` a `http://localhost:8001/v1/chat/completions`. Estructuré la conversación con una cronología (`messages`) que incluye un prompt de sistema con las instrucciones para GINA y los intercambios anteriores.

El primer desafío inesperado fue gestionar esta cronología. Sin un límite, tras decenas de mensajes la petición se volvía demasiado grande y LM Studio respondía con un error 400. Implementé un mecanismo de reinicio automático: cuando la cronología supera las 10 interacciones, se recorta manteniendo solo el prompt de sistema y los últimos intercambios. GINA "pierde" un poco de contexto reciente, pero la experiencia sigue siendo aceptable.

### Fase 3: la voz

Para la síntesis de voz usé `pyttsx3`, que aprovecha las voces SAPI de Windows. La calidad es funcional, aunque un poco mecánica. El problema inmediato surgió casi de inmediato: a los modelos LLM les encanta formatear las respuestas en markdown, y `pyttsx3` leía literalmente asteriscos, guiones bajos y comillas invertidas, "asterisco asterisco 2 asterisco asterisco es un número primo" no es precisamente agradable. Escribí una función `clean_text_for_tts()` que, con algunas expresiones regulares (regex), elimina o sustituye todos los caracteres de markdown antes de la lectura. Ahora GINA solo lee texto limpio.
![gina-diretta.jpg](gina-diretta.jpg)
*Gina responde a una pregunta directa sobre su conocimiento interno*

## Capítulo 4 — El corazón del proyecto: el tool calling

El "tool calling" es la verdadera magia de GINA. Sin él, sería solo un chatbot que responde por voz. Con el "tool calling" puede hacer cosas concretas en el mundo real.

El mecanismo funciona así: el usuario dice algo ("añade leche a la lista de la compra"), Vosk transcribe la frase a texto, el texto se envía a LM Studio junto con la lista de herramientas disponibles (cada una descrita en JSON con nombre, descripción y parámetros esperados), el modelo entiende que para satisfacer la petición debe llamar a `add_to_shopping_list` con el parámetro `item_name = "leche"` y responde con una petición de tool call en lugar de con texto. Mi script de Python intercepta esta petición, ejecuta la función de Python correspondiente, envía el resultado de vuelta al modelo, y el modelo genera la respuesta vocal final: "He añadido leche a la lista de la compra".

Lo bonito de este mecanismo es que es **infinitamente ampliable**: basta con añadir una nueva función de Python y describirla en el JSON de las herramientas, y el modelo aprenderá a usarla sin necesidad de ningún otro entrenamiento.

### La lista de la compra

La herramienta más sencilla y útil en el día a día es la gestión de la lista de la compra. Tres funciones, `add_to_shopping_list`, `get_shopping_list`, `remove_from_shopping_list`, leen y escriben un archivo JSON con la lista, cada artículo acompañado de una marca de tiempo y de un indicador `checked`. Funciona exactamente como se espera, con una naturalidad que todavía sorprende cada vez.
![gina-spesa.jpg](gina-spesa.jpg)
*Gina enumera la lista de la compra.*

### Búsqueda online (con consentimiento explícito)

Hay una funcionalidad que merece un comentario aparte, porque rompe deliberadamente el principio del "todo local". GINA puede buscar información en la web a través de DuckDuckGo (clima, noticias, hechos recientes), pero solo previo consentimiento explícito del usuario.

El motivo de esta elección es sencillo: una búsqueda online es el único momento en que algo sale del perímetro del PC, y quería que fuera una decisión consciente, no algo que ocurre de forma silenciosa y automática. Cuando la petición requiere datos que el modelo no puede tener (información en tiempo real, eventos recientes), GINA pide confirmación antes de proceder.

Si el usuario acepta, la consulta se envía a DuckDuckGo, el resultado se pasa al modelo como contexto adicional y la respuesta se lee en voz alta. Si el usuario prefiere no usar internet, el modelo responde con lo que sabe o admite honestamente que no lo sabe.

Es un compromiso pragmático: la privacidad sigue siendo la regla, la conexión la excepción consciente.
![gina-online.jpg](gina-online.jpg)
*Gina realiza una búsqueda online sobre el clima en Roma, tras la petición de consentimiento explícito.*

### Notas de voz

Otra función que uso a diario es la de los apuntes de voz. ¿Cuántas veces pasa que piensas "tengo que acordarme de hacer esto" y luego te olvidas? Con GINA basta con decir "anota: leer artículo en AiTalk mañana" y la herramienta `add_note` guarda la frase en `notes.json` con una marca de tiempo. Luego se puede preguntar "¿qué notas tengo?" y GINA enumera las últimas anotaciones. Sencillo, pero utilísimo.

### Recordatorios temporales

La función más compleja de implementar fue la de los recordatorios temporales. El objetivo era poder decir "recuérdame llamar a Mario en 10 minutos" y que GINA efectivamente lo hiciera, incluso en medio de una conversación sobre otro tema.

El desafío era técnico: el programa principal está en escucha continua de la palabra de activación "Gina". Si hubiera implementado un simple `time.sleep()` en el hilo (thread) principal, el asistente se habría bloqueado hasta que terminara el temporizador, incapaz de responder a cualquier otra cosa. La solución fue usar un hilo separado para el control de los recordatorios y una cola (`queue`) para comunicarme con el hilo principal de forma segura (thread-safe). Un hilo de fondo comprueba cada 10 segundos si hay recordatorios caducados en el archivo `reminders.json`; cuando encuentra uno, en lugar de llamar directamente a la función vocal (que no es segura entre hilos), pone el texto en una cola; un segundo hilo lee continuamente de la cola y, cuando recibe un mensaje, hace que GINA lo lea. Así, el asistente puede recordarte llamar a Mario aunque hayan pasado 10 minutos sin que tú hayas dicho nada.
![gina-promemoria.jpg](gina-promemoria.jpg)
*El archivo json en el que Gina registra una nota temporal, para avisarte en el momento justo*

### Control multimedia

Para la música creé una carpeta `Musica/` en el mismo directorio del script. La herramienta `search_and_play_music` busca en la carpeta los archivos de audio con las extensiones estándar, hace una búsqueda por coincidencia parcial si el usuario especifica un nombre, elige un archivo al azar si el usuario dice de forma genérica "pon algo de música" y reproduce el archivo con el reproductor predeterminado del sistema mediante `os.startfile`. Sencillo y eficaz.

### Compartir en Telegram

La última extensión práctica es el envío de la lista de la compra a Telegram. Antes de salir puedo decir "Gina, mándame la lista" y recibo un mensaje en un bot de Telegram que he creado (@GinaShoppingBot). Llego al supermercado, abro Telegram y tengo la lista lista. El bot es gratuito, fácil de configurar hablando con @BotFather, y la persistencia es total: el mensaje se queda en el chat hasta que yo lo borre.
![gina-telegram.jpg](gina-telegram.jpg)
*El mensaje enviado a Telegram con la lista, tras una petición específica.*

## Capítulo 5 — El experimento visionario: GINA que modifica su propio código

Con un asistente funcionando y rico en funcionalidades, quise ir más allá. La idea era casi de ciencia ficción: ¿y si GINA pudiera modificar su propio código fuente?

La imagen es potente: un asistente que aprende, evoluciona y se mejora a sí mismo. Ya no un programa estático, sino algo en continua transformación. Casi Philip K. Dick, más que informática aplicada.

### La implementación

Creé la herramienta `modify_code_file`. El flujo era este: el usuario dice "Gina, modifica el archivo test.py, añade una función que salude al usuario"; GINA recibe la petición y llama a la herramienta con el nombre del archivo y la instrucción; la herramienta lee todo el archivo, se lo pasa al modelo como contexto junto con la instrucción de modificación y pide generar la nueva versión; el modelo devuelve el código modificado; la herramienta guarda la nueva versión en la carpeta `Codice/` en la raíz del proyecto, en un nuevo archivo, dejando intacto el original.

Por seguridad, GINA solo puede modificar los archivos de la carpeta `Codice/`, dentro del proyecto, donde solo se encuentran archivos puestos por el usuario. El usuario puede inspeccionar el resultado y, solo si está satisfecho, sustituir manualmente el original.

### El éxito parcial

La herramienta funciona perfectamente en archivos pequeños. Creé un `test.py` de unas veinte líneas, le pedí a GINA que añadiera una función y en pocos segundos tuve `test_modificato.py` con la función solicitada. Magia, literalmente.

Pero con el propio archivo `gina_assistente.py`, de unas 1000 líneas, el sistema mostró sus límites. LM Studio tardaba mucho tiempo en procesar la petición, a menudo se agotaba el tiempo de espera (timeout) y, cuando lograba completar la respuesta, esta estaba cortada o malformada.

### El límite técnico como lección

El problema es probablemente la **ventana de contexto** de los modelos. Los modelos que he usado tienen contextos limitados. Mi archivo `gina_assistente.py` supera con creces este umbral; el modelo no tiene espacio suficiente para procesarlo por completo y volver a generarlo con las modificaciones. Sin embargo, todavía tengo que analizar la cuestión en profundidad.

Este fallo es tan instructivo como cualquier éxito. En el artículo sobre los SLM escribí que estos modelos son como "bisturís quirúrgicos", excelentes en tareas específicas y circunscritas, mientras que los grandes modelos son las "navajas suizas" que lo hacen todo decentemente. La herramienta de modificación de código es la demostración práctica: falla en una tarea enorme (modificar un archivo de 1000 líneas), pero sobresale en tareas pequeñas y dirigidas.

Decidí mantener la herramienta en el proyecto como experimento visionario más que como funcionalidad estable. La idea es fascinante, el potencial es real y, en el futuro, con modelos de contexto más amplio, podría volverse plenamente viable.
![gina-codice.jpg](gina-codice.jpg)
*Gina creó el juego de Snake perfectamente funcional al primer intento*

## Capítulo 6 — Las incoherencias de los modelos: vivir con el no-determinismo

Ningún proyecto complejo está exento de imperfecciones. GINA tiene las suyas y vale la pena contarlas.

### El problema del retraso (delay)

Una de las primeras dificultades fue el retraso entre la palabra de activación y la escucha efectiva del comando. El flujo original preveía que GINA, al oír la palabra "Gina", respondiera "¿Dime?" y luego empezara a escuchar. Pero como la respuesta vocal duraba aproximadamente un segundo, las primeras palabras del comando se perdían sistemáticamente. Probé moviendo el inicio de la escucha antes de la respuesta vocal, pero Gina terminaba escuchándose a sí misma y activándose. De momento, he aceptado la breve espera antes de poder hablar, pero espero encontrar una solución.

### Vosk: preciso pero no infalible

Vosk es excelente en entornos silenciosos. Si hay ruido de fondo, la precisión cae. Es un problema conocido y aceptable para un proyecto personal. Para una aplicación profesional se necesitaría un sistema dedicado como Porcupine, pero para mis usos diarios Vosk cumple sobradamente su cometido.

### La naturaleza no determinista de los LLM

Esta es quizás la característica más fascinante y, a veces, frustrante de los modelos lingüísticos: no son deterministas. Ante una misma entrada, pueden dar respuestas diferentes.

Un ejemplo concreto: si digo "Gina, pon algo de música", a veces el modelo llama correctamente a la herramienta `search_and_play_music` y reproduce un tema "a su elección" de la carpeta `Musica/`. Otras veces responde: "Aquí tienes un tema perfecto para este momento: Bohemian Rhapsody de Queen". Y luego, obviamente, no suena nada porque el archivo no existe. No es un bug, es el modelo que ha aprendido de miles de millones de textos que a "pon algo de música" le suele seguir una sugerencia musical, y a veces elige ese camino en lugar de llamar a la herramienta.

Del mismo modo, la búsqueda del clima a veces funciona correctamente y otras veces el modelo responde: "Para obtener información meteorológica precisa, te recomiendo consultar un sitio especializado". Esta variabilidad es normal y hay que aceptarla. Es el precio a pagar por tener un sistema creativo y no rígidamente determinista y, en el fondo, es también lo que hace que la interacción sea más humana, para bien y para mal.

Ambos problemas podrían mitigarse con un refinamiento del prompt de sistema, es un aspecto en el que trabajar.

## Capítulo 7 — Conclusiones: qué funciona, qué falta, hacia dónde vamos

El proyecto ha tenido éxito más allá de mis expectativas iniciales. GINA funciona, es estable y la uso a diario. Se inicia con un doble clic en un archivo `.bat` en el escritorio y está lista en pocos segundos.

### Qué sabe hacer hoy

Con GINA puedo gestionar la lista de la compra (añadir, visualizar, eliminar artículos) y enviarla a Telegram antes de salir. Puedo registrar notas y recordatorios no temporales. Puedo establecer recordatorios temporales ("recuérdame llamar a Mario en 10 minutos") y GINA los respeta incluso en medio de otras conversaciones. Puedo reproducir música de mi carpeta local, tanto canciones específicas como temas elegidos al azar. Puedo hacer preguntas generales usando el conocimiento interno del modelo. Puedo hacer búsquedas online, previo consentimiento explícito. Puedo, en archivos pequeños, pedirle a GINA que modifique el código. Todo ello sin que un solo bit salga de mi PC.

### Dónde queda trabajo por hacer

La autocrítica es parte del método. La calidad de la voz de `pyttsx3` es funcional pero metálica: se podría pasar a Piper TTS (local, calidad muy superior) o a Edge TTS (online, calidad excelente). La precisión de la palabra de activación podría mejorar con Porcupine. El reconocimiento de voz podría ser más preciso con Whisper, a costa de algunas dependencias más. La interfaz hoy es solo de línea de comandos: una sencilla interfaz web en Streamlit o Flask la haría más accesible. Y la modificación de archivos grandes sigue siendo un límite técnico abierto.

### Un mundo de posibilidades

Lo que más me gusta de GINA es que se puede ampliar al infinito. Algunas ideas que tengo en la lista: una interfaz web para ver la lista de la compra, notas y recordatorios incluso en remoto; integración con el calendario ("Gina, ¿qué compromisos tengo mañana?"); control de dispositivos domésticos inteligentes (smart home).

Pero lo más importante es lo que este proyecto demuestra a un nivel más amplio. GINA no es solo un asistente de voz personal: es una **plataforma demostrativa** del potencial de los Small Language Models en local. Demuestra que no hace falta confiar en los gigantes de la nube para tener una inteligencia artificial útil, personal y respetuosa con la privacidad.

La tendencia que describí en ["Small Language Models para el 2026"](https://aitalk.it/it/slm-2026.html) ya es una realidad y se puede tocar con la mano. Con modelos como Qwen, Gemma 4 y Mistral, un PC normal de gaming puede ejecutar un asistente de voz sofisticado, con una latencia inferior al segundo, sin consumir recursos excesivos.

Y la mejor parte es que todo esto es **de código abierto**: modificable, mejorable, adaptable a cualquier necesidad. He aprendido muchísimo construyendo este proyecto, he confirmado que la inteligencia artificial no es solo ChatGPT y API de pago. Es también curiosidad, experimentación, el placer de sentarse ante el ordenador, escribir código y ver cómo algo que has construido cobra vida y te responde.

Espero que este relato inspire a alguien a emprender un viaje experimental. Y si lo hace, GINA le espera, lista para escuchar su primera palabra.

*"Gina"*

---

## Apéndice técnico: cómo empezar

Todo el código está disponible en el [repositorio GitHub](https://github.com/Dario-Fe/Gina-Assistant). El script principal es `gina_assistant.py`; los archivos de memoria para las diversas herramientas (`shopping_list.json`, `notes.json`, `reminders.json`) se crean automáticamente en el primer inicio. La carpeta `Musica/` y la carpeta `Codice/` son opcionales; si se desea usar a GINA para escuchar música o para escribir código, cread las carpetas en la raíz del proyecto, poned vuestras canciones favoritas o los archivos con el código a modificar o a crear desde cero.

Para iniciar a GINA:
![schema2.jpg](schema2.jpg)
