---
tags: ["Generative AI", "Applications", "Security"]
date: 2026-07-10
author: "Dario Ferrero"
---

# He enseñado a la IA a hacer de guardia: cómo he construido un sistema de seguridad a coste cero
![sistema-sicurezza-ai.jpg](sistema-sicurezza-ai.jpg)

*En la serie de televisión 'Person of Interest', una superinteligencia apodada simplemente "la Máquina" vigila cada rincón del planeta a través de cámaras, micrófonos y sensores de todo tipo, identificando amenazas antes de que se materialicen. Es ciencia ficción, por supuesto. Pero la idea de fondo, es decir, usar la visión artificial para entender qué sucede en un entorno, es ahora accesible para cualquiera que tenga un PC y una webcam. Menos de 250 líneas de código. Sin suscripciones, sin nube, sin vídeos que viajen por el mundo. Solo una notificación en el teléfono, con foto, cuando alguien entra en casa.*

La pregunta que me hice hace unas semanas era sencilla: ¿cuánto cuesta un sistema de seguridad que te avise en tiempo real si alguien entra en casa, te mande una foto y funcione íntegramente en local sin depender de una suscripción mensual? La respuesta: cero euros. Solo hardware que con toda probabilidad ya poseéis. En este artículo cuento cómo he construido ese sistema, qué he aprendido por el camino y por qué el experimento dice algo más grande sobre el modo en que la inteligencia artificial está cambiando la relación entre tecnología y cotidianidad.

## Antes de apuntarla a casa: el ensayo en Times Square

Cualquier sistema de seguridad digno de ese nombre debe ser probado antes de ser puesto en producción. Pero apuntar una webcam a la propia habitación sin haber verificado el funcionamiento en condiciones exigentes parecía ingenuo. Así que decidí empezar por el contexto más caótico que pudiera encontrar sin moverme de la silla: Times Square, Nueva York, vista desde arriba a través de una de las muchas webcams públicas accesibles en streaming.

El escenario era deliberadamente extremo. Cientos de personas que se cruzan, taxis amarillos, autobuses, camiones de reparto, todo en movimiento simultáneo, con variaciones de luz repentinas y ángulos difíciles. El tipo de situación que pone en crisis a cualquier sistema de reconocimiento visual mediocre.

El resultado fue sorprendente: el sistema reconoció hasta nueve vehículos simultáneamente entre coches, autobuses y camiones, identificó peatones incluso a una distancia considerable, mantuvo 40 fotogramas por segundo estables, todo en una CPU, sin tocar la GPU. *"Si funciona en Times Square, funciona en cualquier lugar"*, me dije. Y así fue.
![timesquare.jpg](timesquare.jpg)
*Captura de pantalla de las pruebas realizadas en la webcam de Times Square.*

## El corazón del sistema: YOLO explicado de forma sencilla

Antes de llegar al momento en que el teléfono vibró con la primera foto de alarma, vale la pena dedicar unas líneas a lo que sucede bajo el capó, porque la tecnología involucrada es genuinamente fascinante incluso si se mira desde lejos.

El componente central se llama [YOLO](https://github.com/ultralytics/ultralytics), acrónimo de *You Only Look Once*. El nombre no es marketing: describe exactamente cómo funciona. Los sistemas de reconocimiento visual tradicionales analizaban una imagen en varios pasos, primero identificando las regiones de interés y luego clasificándolas. YOLO da un giro al enfoque: analiza la imagen completa en un único paso, dividiéndola en una cuadrícula y prediciendo simultáneamente la posición y el tipo de objeto para cada celda. El resultado es una velocidad notablemente superior, con una precisión que en las versiones recientes ha alcanzado niveles excelentes.

La versión que he usado, YOLOv8n, es la variante más ligera de la familia. El sufijo "n" significa *nano*, y está diseñada explícitamente para funcionar en hardware limitado. Está entrenada en el dataset COCO, que comprende ochenta categorías de objetos: personas, vehículos, mascotas, objetos de mobiliario. Para mis propósitos, la única categoría que me interesa es "persona", con un umbral de confianza fijado en 0,4, es decir, el modelo señala una presencia solo cuando está seguro al menos al cuarenta por ciento de haberla detectado. Un umbral más bajo produce más falsas alarmas, uno más alto corre el riesgo de perder detecciones reales.

El segundo ingrediente crucial es [ONNX](https://onnxruntime.ai/), que significa *Open Neural Network Exchange*. Es un formato abierto para representar modelos de machine learning, pero sobre todo es un motor de inferencia optimizado que sabe cómo aprovechar al máximo las instrucciones específicas de cada procesador. Cuando exportáis YOLOv8n a formato ONNX, el modelo pasa de 10-15 fotogramas por segundo a 40-45 fotogramas por segundo en la misma CPU, sin cambiar una sola línea de código de la aplicación. El archivo pasa de 6 MB a 12 MB, pero la ganancia de velocidad es casi el cuádruple. Es como tener un traductor simultáneo que conoce perfectamente el dialecto de vuestro procesador.

## GINA me presta el bot

Quienes seguís este portal recordaréis a [GINA, mi asistente de voz personal](https://aitalk.it/it/gina-assistente-vocale.html). Para las notificaciones en tiempo real ya había construido un bot de Telegram integrado en el ecosistema de GINA, capaz de enviarme mensajes, actualizaciones y avisos directamente al smartphone. Reutilizar esa infraestructura para el sistema de seguridad fue natural: un ejemplo clásico de cómo las piezas de un ecosistema tecnológico construido a lo largo del tiempo empiezan a encajar de formas no siempre previstas.

El bot de Telegram hace una sola cosa, pero la hace bien: cuando el sistema detecta a una persona, recibe una llamada HTTP con un mensaje de texto y una foto del fotograma incriminado, y los entrega en mi teléfono en dos o cinco segundos. Sin apps propietarias, sin cuentas en plataformas de videovigilancia en la nube, sin datos que atraviesen servidores de terceros que no sean los servidores de Telegram para la entrega final de la notificación. Como alternativa, se podría pensar en el envío de un correo electrónico. El vídeo en sí nunca sale del PC.

La configuración del bot requiere unos cinco minutos: se crea a través de [@BotFather](https://core.telegram.org/bots) en Telegram, se obtiene un token de autenticación, se recupera el propio chat ID enviando un mensaje al bot y consultando las API, y se insertan las dos cadenas en el archivo de configuración. Después de eso, el canal de notificación está operativo.

## El momento de la verdad: mi habitación

Superada la prueba neoyorquina, era el momento de apuntar la webcam al entorno que realmente importaba: mi habitación. Posicioné la cámara, inicié el script, esperé los cinco segundos de estabilización que el sistema se toma al inicio para no generar falsas alarmas durante la carga, y salí de la habitación.

Después volví a entrar.

El teléfono vibró incluso antes de que llegara al centro del encuadre. El mensaje decía: *"🚨 ¡ALARMA DE SEGURIDAD! Personas detectadas: 1. Hora: 13:43:07. Alarma #1"*. Debajo, una foto con mi contorno resaltado por un recuadro y un overlay rojo en la parte alta del fotograma. Latencia desde la entrada hasta la notificación: menos de un segundo para el reconocimiento, dos-tres segundos para la entrega en Telegram.

Funcionaba.

El sistema tiene una lógica de protección contra falsas alarmas integrada: un cooldown de diez segundos entre una alarma y la siguiente impide que una persona parada en el encuadre genere decenas de notificaciones por minuto. El umbral de confianza a 0,4 resultó estar bien calibrado para un entorno doméstico: ningún falso positivo durante las pruebas, ningún reconocimiento fallido en condiciones de luz normal. Con iluminación escasa el rendimiento se degrada, pero es un límite físico de la webcam incluso antes que del modelo.
![allarme.jpg](allarme.jpg)
*Captura de pantalla del mensaje de alarma en Telegram, así como del ladrón más improbable de la historia de la criminalidad.*

## Cómo está construido: la receta técnica

El código completo ocupa menos de 250 líneas de Python. La estructura es lineal y comprensible incluso para quienes no escriben código profesionalmente. Hay cuatro bloques lógicos: la configuración inicial con tokens de Telegram y parámetros de umbral, las funciones de envío de mensajes y fotos a través de la API de Telegram, la función de detección de personas que consulta a ONNX, y el bucle principal que adquiere los fotogramas de la webcam, los analiza y gestiona la lógica de las alarmas.

Las dependencias son cinco librerías de Python estándar en el ecosistema de machine learning: `ultralytics` para cargar YOLO, `onnxruntime` para la inferencia optimizada, `opencv-python` para la gestión de la webcam y el procesamiento de fotogramas, y `requests` para las llamadas HTTP a Telegram.

La estructura final del proyecto es esencial: un archivo Python principal, el modelo ONNX de 12 MB y un archivo de configuración. En total, menos de 15-20 MB en disco.

En el frente del rendimiento, los números hablan por sí solos:
![tabella.jpg](tabella.jpg)

El hardware utilizado es un AMD Ryzen 7 7700 con 32 GB de RAM, pero las pruebas en configuraciones menos potentes confirman que el sistema funciona sin problemas incluso en un portátil con procesador Intel i5 de quinta o sexta generación y 8 GB de RAM. La GPU nunca se ve involucrada.

## Dónde tiene sentido usarlo y dónde no

Un sistema de este tipo funciona bien en contextos específicos, y es honesto decirlo claramente. Para la seguridad doméstica en un piso o una casa pequeña es eficaz: monitoriza una habitación o una entrada, avisa en tiempo real, cuesta cero. Para vigilar una oficina durante el cierre nocturno, una tienda después del horario de cierre o un almacén con acceso limitado, el sistema se presta igual de bien.

No es, en cambio, un sustituto de un sistema de seguridad profesional certificado para entornos críticos. Los falsos negativos existen, especialmente en condiciones de luz difíciles. El sistema no distingue entre quien tiene las llaves de casa y un intruso real, al menos en la versión básica. No graba vídeo, solo fotos de los momentos de alarma. Y funciona en un PC que debe estar encendido y conectado a Internet para las notificaciones.

En el frente legal, vale la pena recordar que en Italia la videovigilancia está regulada por el GDPR y el Garante de la Privacidad. Para uso exclusivamente doméstico, dentro de la propia propiedad privada, las restricciones son significativamente menos onerosas que para entornos públicos o laborales. Si la cámara encuadra espacios comunes o áreas externas compartidas, entran en juego obligaciones de señalización y, en ciertos casos, de notificación al Garante. El principio rector es sencillo: informar a las personas de que el área está monitorizada es siempre la elección correcta, no solo la legal.
![log.jpg](log.jpg)
*Captura de pantalla del terminal con el sistema en funcionamiento, con el reconocimiento de objetos y la alarma en el momento de la entrada de una persona.*

## Los caminos abiertos

El proyecto en su forma actual es un punto de partida funcional, no una meta. Las extensiones naturales son diversas, con una complejidad creciente.

El siguiente paso más obvio es el reconocimiento facial para distinguir a los residentes de los extraños. La librería `face_recognition` de Python permite construir un archivo de rostros conocidos y filtrar las alarmas en consecuencia: si soy yo quien entra en casa, ninguna notificación. Si es alguien que el sistema nunca ha visto, alarma. El código adicional son apenas unas pocas decenas de líneas.

Una integración con sensores PIR pasivos, los clásicos sensores de movimiento por infrarrojos, permitiría activar YOLO solo en presencia de movimiento, reduciendo drásticamente el consumo energético en los periodos de inactividad. En la implementación actual, la webcam funciona y el modelo analiza los fotogramas continuamente, incluso cuando la habitación lleva horas vacía.

El soporte multicámara requeriría instanciar múltiples procesos paralelos, uno para cada webcam, con un sistema centralizado de gestión de alarmas. Un panel de control web ligero construido con Flask o FastAPI permitiría visualizar el estado del sistema de forma remota. Todas estas son extensiones realizables con unos pocos días de trabajo.

## El local gana (casi siempre)

Cada vez que construyo algo de este tipo, me encuentro lidiando con una pregunta más amplia: ¿por qué hacerlo en local cuando existen API en la nube para la visión artificial que funcionan con tres líneas de código?

La respuesta no es ideológica. Es práctica.

Como he discutido en otros contextos en este portal, los modelos locales han alcanzado un nivel de madurez que hace que la elección entre local y nube dependa genuinamente del caso de uso, no de la asunción automática de que la nube es siempre superior. Para un sistema de videovigilancia doméstica, las ventajas del local son difíciles de superar: las imágenes de vuestra casa nunca salen de vuestro PC, no hay costes variables, el sistema funciona incluso sin Internet una vez configurado y no hay dependencia de políticas de precios de terceros que puedan cambiar.

La nube gana en escenarios diferentes: cuando se necesitan decenas de cámaras, cuando la potencia de cálculo local no es suficiente, cuando los modelos requeridos son demasiado grandes para funcionar en local o cuando el mantenimiento de la infraestructura es una carga insostenible. Pero para un experimento doméstico como este, la nube habría sido una sobrecarga sin beneficios concretos.

Hay, sin embargo, una consideración que siempre vale la pena explicitar: ONNX y YOLOv8n son herramientas maduras, documentadas y con comunidades activas. No es magia negra reservada a especialistas. Es ingeniería aplicada que cualquiera que tenga curiosidad y unas pocas horas a su disposición puede replicar. Esta es quizás la cosa más significativa de todo el experimento: no el sistema de seguridad en sí, sino la demostración de que la distancia entre la "tecnología IA" y "lo que funciona en mi PC" se ha acortado hasta el punto de volverse casi irrelevante.

---

*El código está disponible en el repositorio [GitHub Security-System-Yolo](https://github.com/Dario-Fe/Security-System-Yolo)*
