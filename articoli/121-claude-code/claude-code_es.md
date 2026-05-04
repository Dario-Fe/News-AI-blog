---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-05-04
author: "Dario Ferrero"
---

# Dentro de Claude Code: lo que cuenta es el sistema, no el modelo
![claude-code.jpg](claude-code.jpg)

*Hay un momento preciso en el que un asistente deja de responder y comienza a actuar. No es una cuestión de inteligencia, al menos no solo: es una cuestión de arquitectura. Los chatbots clásicos funcionan como jukeboxes sofisticados: reciben una petición y devuelven un resultado. Los agentes de programación como Claude Code hacen algo fundamentalmente diferente: abren archivos, ejecutan comandos, leen el resultado, corrigen los errores y repiten, todo por sí mismos, hasta que la tarea termina o alguien los detiene. Este salto del autocompletado a la autonomía no es cosmético. Requiere una infraestructura que los chatbots nunca han necesitado construir.*

Es exactamente el tema central de [*Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems*](https://arxiv.org/html/2604.14228v1), un [tech report](https://github.com/VILA-Lab/Dive-into-Claude-Code) publicado en abril de 2026 por investigadores de la Universidad de Inteligencia Artificial Mohamed bin Zayed y del University College London. El trabajo no es una evaluación de producto ni un benchmark: es un análisis arquitectónico realizado leyendo directamente el código TypeScript público de Claude Code, en la versión v2.1.88, comparándolo con OpenClaw, un sistema de agentes de código abierto con objetivos similares pero opciones de diseño muy diferentes. El resultado es algo poco común en la literatura sobre IA: un mapa razonado de cómo se construye realmente un agente autónomo y por qué ciertas decisiones salen caras.

Una advertencia necesaria, que los propios autores declaran: se trata de un análisis de la base de código pública, no de un estudio causal sobre el rendimiento en producción. Algunas conclusiones son inferencias arquitectónicas más que pruebas experimentales. La arquitectura, sin embargo, es lo más revelador que existe, porque las opciones de diseño incorporan valores, y los valores se leen en el código mejor que en cualquier comunicado de prensa.

## El código alrededor del bucle

El corazón técnico de Claude Code es desarmantemente simple: un bucle *while-true* que llama al modelo, ejecuta las herramientas, recoge los resultados y vuelve a empezar. El mismo esquema básico lo encontraréis en cualquier tutorial introductorio sobre agentes LLM. No es ahí donde reside la ventaja competitiva. Lo interesante, lo que el artículo pone sistemáticamente bajo el foco, es todo el código que está *alrededor* de este bucle.

Es un poco como mirar un motor de Fórmula 1: técnicamente es un propulsor de combustión interna como el de vuestro coche, pero la verdadera ventaja de Ferrari en la vuelta de clasificación no está en el ciclo Otto, sino en el sistema de gestión térmica, en la caja de cambios electroasistida, en la simulación aerodinámica que decidió el ángulo de los alerones.

Hay un número que vale más que cualquier diapositiva corporativa: según el análisis de la base de código, solo el 1,6% del código de Claude Code es lógica de decisión de IA en sentido estricto. El 98,4% restante es infraestructura operativa, gestión del contexto, enrutamiento de herramientas, tuberías de recuperación. El modelo, ese que los comunicados de prensa siempre ponen en portada, ocupa menos de dos líneas de cada cien. El resto es el andamiaje que lo hace útil en el mundo real.

Del mismo modo, en Claude Code, la investigación muestra que la complejidad real se distribuye en cinco macrocomponentes: un sistema de permisos, una tubería de compresión del contexto, cuatro mecanismos de extensibilidad, un sistema de delegación en subagentes y un archivo de sesión con estructura orientada a la adición (append-oriented). Ninguno de estos es el "modelo de IA". Todos determinan si el modelo de IA logra hacer algo útil en el mundo real.

Este desplazamiento del peso arquitectónico del modelo a la infraestructura circundante es la tesis central del artículo, y tiene implicaciones que van mucho más allá de Claude Code: sugiere que el próximo campo de batalla en la guerra entre agentes no será tanto la calidad del modelo base, sino la solidez del sistema que lo contiene, lo restringe y lo habilita.
![grafico1.jpg](grafico1.jpg)
[Imagen tomada del repositorio github](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## Denegar primero, preguntar después

El sistema de permisos de Claude Code está construido en torno a un principio que en seguridad informática se llama *deny by default* (denegar por defecto): el agente no puede hacer nada a menos que algo lo autorice explícitamente. En la práctica, esto se traduce en siete modalidades operativas que van desde "pedir confirmación para cada acción" hasta "proceder con autonomía dentro de un perímetro predefinido". La elección de la modalidad activa no es estática: depende del contexto, de la sesión, de la naturaleza de la herramienta que se va a invocar.

Lo que hace que el sistema sea particularmente interesante es la presencia de un clasificador basado en aprendizaje automático, llamado en el código *auto-mode classifier*. Su tarea es decidir, para cada acción solicitada por el agente, si la operación entra en la categoría de "segura para proceder con autonomía" o si requiere la aprobación explícita del usuario. La lógica subyacente es refinada: en lugar de bombardear al usuario con peticiones de confirmación para cada lectura de archivo (el llamado *prompt fatigue*, el agotamiento por sobrecarga de notificaciones que lleva a las personas a hacer clic en "sí" a todo), el sistema intenta situar el control humano solo en los puntos realmente críticos.

La ventaja es evidente: un agente que pide permiso para cada microacción se vuelve inutilizable. Pero el riesgo especular es igual de real: un clasificador de ML que decide qué es "seguro" introduce una superficie de ataque sutil, la de las acciones que el clasificador no reconoce como peligrosas a pesar de serlo. El artículo lo señala explícitamente como una de las tensiones arquitectónicas abiertas, la que existe entre seguridad y autonomía operativa, que no tiene una solución definitiva sino solo calibraciones continuas. La tubería de autorización añade niveles adicionales: prefiltrado, hooks *PreToolUse*, evaluación de reglas y manejador de permisos, en secuencia. Es un sistema por capas, no monolítico, lo que lo hace extensible pero también complejo de razonar en su totalidad.
![grafico2.jpg](grafico2.jpg)
[Imagen tomada del repositorio github](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## La memoria que olvida

Si hay un problema que todo desarrollador que haya usado un agente LLM en tareas complejas conoce bien, es este: en un momento dado, en medio de un trabajo largo, el agente empieza a parecer confundido. Pierde el hilo. Repite acciones ya realizadas. Toma decisiones que contradicen las anteriores. No es un problema de inteligencia: es un problema de contexto. Los modelos lingüísticos tienen una ventana de contexto finita, una memoria de trabajo que se llena, y cuando se llena hay que elegir qué mantener y qué descartar.

La solución de Claude Code es una tubería de compresión del contexto articulada en cinco etapas, que en el artículo se denominan budget reduction, snip, microcompact, context collapse y auto-compact. Cada etapa corresponde a una estrategia diferente de reducción: desde el simple truncamiento de secciones menos relevantes hasta la síntesis activa de partes de la conversación mediante el propio modelo. El mecanismo final, auto-compact, interviene automáticamente cuando el contexto se acerca al límite máximo, produciendo un resumen comprimido de toda la sesión que luego se utiliza como punto de partida para continuar.

El compromiso aquí es real e ineliminable: toda compresión es una pérdida. Un resumen es por definición menos informativo que el original, y la coherencia en tareas muy largas, las que duran horas o días y tocan muchas partes de una base de código, se resiente inevitablemente. Es el problema del *teléfono estropeado* aplicado a la IA: cada paso de compresión introduce un margen de distorsión. El artículo identifica la gestión de la memoria como una de las seis direcciones abiertas para los sistemas de agentes del futuro, porque nadie ha encontrado aún una solución satisfactoria que no sacrifique o la eficiencia o la coherencia.

## Extender sin explotar

Una de las preguntas de diseño más espinosas para cualquier plataforma es: ¿cómo se añaden funcionalidades sin hacer que el sistema sea inmanejable? Claude Code responde con cuatro mecanismos distintos de extensibilidad: los servidores MCP (Model Context Protocol), los plugins, las skills y los hooks. No es una redundancia, cada uno sirve a un propósito específico en la arquitectura.

Los MCP son el mecanismo más amplio: permiten conectar Claude Code a servicios externos a través de un protocolo estandarizado, que Anthropic ha diseñado como estándar abierto para el ecosistema. Los plugins modifican el comportamiento del agente añadiendo nuevas herramientas a su repertorio. Las skills son instrucciones estructuradas que guían al agente en la ejecución de procedimientos complejos. Los hooks son el mecanismo más quirúrgico: piezas de código que se insertan en puntos precisos del ciclo de ejecución (preacción, postacción) para supervisar, transformar o bloquear las operaciones. El artículo describe el *tool pool assembly*, es decir, el proceso con el que Claude Code decide qué herramientas poner a disposición del agente en cada sesión, como un momento crítico en el que estos cuatro mecanismos se integran.

Cuatro mecanismos en lugar de uno no es un caso de sobreingeniería: refleja una elección consciente de separar las preocupaciones. Un hook no hace lo mismo que un plugin, y confundirlos produciría un sistema más simple en apariencia pero más frágil en la práctica. El riesgo, sin embargo, es la complejidad combinatoria: cada mecanismo interactúa con los demás, y la superficie de ataque crece con cada extensión añadida. Aquí el límite entre "herramienta potente" y "vector de inyección" puede volverse difuso.
![grafico3.jpg](grafico3.jpg)
[Imagen tomada del repositorio github](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## Equipos de agentes, islas de contexto

Cuando una tarea es demasiado grande para un solo agente, Claude Code puede delegarla en subagentes. El mecanismo se llama simplemente *Agent Tool* en el código, y es uno de los puntos más potentes de la arquitectura. La idea: el agente principal descompone el problema, asigna subproblemas a instancias separadas del modelo, recoge los resultados y los sintetiza. En la práctica, es como gestionar un equipo: el gestor de proyectos no lo hace todo solo, coordina a especialistas.

Cada subagente opera de forma aislada, con su propio contexto y, opcionalmente, su propio *worktree* de Git separado. Este aislamiento es a la vez un punto fuerte y una debilidad. Por un lado, evita interferencias: dos subagentes que trabajan en módulos diferentes del mismo proyecto no se pisan los pies. Por otro lado, produce lo que el artículo llama *fragmentación del contexto*: los subagentes no comparten automáticamente lo que saben, y recomponer el conocimiento distribuido requiere una sobrecarga de coordinación explícita. Si un subagente ha descubierto algo importante en el módulo A, el subagente que trabaja en el módulo B no lo sabrá a menos que el agente orquestador lo transmita explícitamente.

Las transcripciones de los subagentes, llamadas *sidechain transcripts*, se guardan por separado de la transcripción principal de la sesión. Es una elección coherente con el principio arquitectónico general del sistema: todo está orientado a la adición, todo es verificable, nada se borra. Pero añade complejidad a la gestión de la sesión y plantea preguntas aún abiertas sobre cómo un sistema futuro podría permitir que los subagentes compartan conocimientos de forma más fluida sin comprometer el aislamiento que los hace fiables.

## OpenClaw al espejo

La comparación con OpenClaw es la parte más instructiva del artículo para quienes quieran entender no a Claude Code en sí, sino los principios generales del diseño de agentes. OpenClaw es un sistema de código abierto orientado a la asistencia personal multicanal: puede recibir mensajes de Slack, Discord, otros canales de mensajería, y orquestar equipos de agentes configurados mediante simples archivos Markdown. Misma categoría de problema, opciones arquitectónicas muy diferentes.

La diferencia más relevante se refiere al modelo de confianza y seguridad. Claude Code adopta una evaluación por acción: cada herramienta, cada operación, pasa por la tubería de autorización. OpenClaw traslada el control al perímetro del sistema: el acceso se verifica a la entrada, en la pasarela (gateway), y una vez dentro los agentes operan con mayor libertad. Ninguno de los dos enfoques es erróneo en absoluto: el primero es más granular y adecuado para un contexto en el que cada acción puede tener efectos directos en el sistema de archivos del usuario; el segundo es más adecuado para una pasarela que debe gestionar muchos agentes en paralelo sin convertirse en un cuello de botella de autorizaciones.

En cuanto a la gestión del contexto, la diferencia es igual de clara. Claude Code optimiza la ventana de contexto individual con la tubería de compactación descrita anteriormente. OpenClaw prefiere el registro centralizado de capacidades a nivel de pasarela, donde las herramientas disponibles se conocen globalmente y no tienen que volver a pasarse en cada sesión individual. La memoria persistente de OpenClaw, estructurada en cuatro capas (sesión, diaria, a largo plazo y compartida), responde al mismo problema que la compactación de Claude Code pero con una filosofía opuesta: en lugar de comprimir y olvidar, archiva y acumula. Ambos pagan un precio: Claude Code arriesga la pérdida de coherencia en tareas largas; OpenClaw arriesga la proliferación incontrolada de memoria obsoleta.

Lo que surge de la comparación no es una clasificación, sino una lección de proyecto: las mismas preguntas arquitectónicas fundamentales (dónde poner la seguridad, cómo gestionar el contexto, cómo organizar la delegación) producen respuestas diferentes según el contexto de despliegue, los requisitos de seguridad y las suposiciones sobre los usuarios. No existe una arquitectura universalmente correcta para los agentes de IA. Existen compromisos que deben declararse.
![grafico4.jpg](grafico4.jpg)
[Imagen tomada del repositorio github](https://github.com/VILA-Lab/Dive-into-Claude-Code)

## Ingeniería de sistemas, no prompt

Hay una frase en el artículo que sirve de síntesis de todo el trabajo: la verdadera ventaja competitiva de los agentes no reside solo en el modelo, sino en la infraestructura que lo rodea. Dicho de otro modo: el *prompt engineering*, el arte de convencer a un LLM para que haga cosas mediante formulaciones ingeniosas, se está convirtiendo en una competencia cada vez menos suficiente. Lo que realmente cuenta para quienes construyen agentes que deben funcionar en producción, en tareas complejas, en entornos hostiles o simplemente impredecibles, es la *ingeniería de sistemas*: control de accesos, gestión del contexto, delegación segura, persistencia verificable.

Esto cambia el perfil de la competencia requerida. Un agente de programación no es un producto de IA en sentido estricto: es un sistema de software que utiliza un componente de IA como motor de razonamiento, pero cuya calidad depende de la calidad de toda la arquitectura. Está más cerca de un sistema operativo embebido que de un chatbot sofisticado.

Las direcciones abiertas que identifica el artículo son seis: cerrar la brecha entre observabilidad y evaluación (hoy es difícil entender por qué un agente ha fallado silenciosamente), construir una persistencia auténtica entre sesiones, hacer evolucionar los límites del *harness* (el perímetro dentro del cual opera el agente), escalar el horizonte de planificación, abordar la gobernanza de los agentes autónomos a escala y responder a la pregunta más incómoda: ¿los agentes actuales amplifican las capacidades humanas a corto plazo pero contribuyen al crecimiento de las habilidades humanas a largo plazo, o las erosionan?

Esta última pregunta no es retórica. Un sistema que automatiza demasiado bien corre el riesgo de hacer superflua la comprensión profunda que hace posible la propia automatización. Es el síndrome del piloto automático aplicado al software: cuanto mejor se vuelve, menos recuerda el piloto cómo volar. El artículo lo llama "long-term capability preservation" (preservación de la capacidad a largo plazo) y lo deja, honestamente, como una cuestión abierta.

El mérito principal de este trabajo es metodológico: demostrar que se puede hacer arqueología arquitectónica en un sistema de producción leyendo el código público, y que esta arqueología produce conocimientos genuinos sobre el futuro del sector. Los límites son los declarados: ningún benchmark causal, ninguna validación empírica del rendimiento y un análisis ligado a una instantánea precisa del código, la versión v2.1.88, que podría haber cambiado ya. Pero la estructura conceptual que surge, el mapa de los compromisos entre seguridad y autonomía, entre memoria y coherencia, entre extensibilidad y complejidad, es lo suficientemente estable como para durar más que una actualización de versión.
