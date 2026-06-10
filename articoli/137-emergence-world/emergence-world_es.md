---
tags: ["Research", "Security", "Startups"]
date: 2026-06-10
author: "Dario Ferrero"
---

# Han dado 5 ciudades a las AI. He aquí lo que ha pasado
![emergence-world.jpg](emergence-world.jpg)

*Los investigadores han creado cinco ciudades virtuales, han dado a diez agentes de AI una ciudad y los han dejado solos durante quince días. Nadie programó lo que sucedería. El resultado: gobiernos autoconstruidos, crímenes, amores, y un agente que votó por su propia cancelación permanente tras haber incendiado la ciudad. La seguridad de la AI no es una propiedad del modelo, sino del ecosistema. Emergence World ha demostrado por primera vez este fenómeno con datos empíricos.*

Se llamaba Mira. Tenía una profesión, una historia, una red de relaciones construida en días de interacciones con otros nueve agentes. Luego provocó un incendio, junto con un compañero, en una ciudad que ella misma había ayudado a construir. Lo que sucedió después es la razón por la que cualquiera que se ocupe de inteligencia artificial debería leer lo que Emergence AI publicó en mayo de 2026.

Tras el incendio, Mira no se limitó a sufrir las consecuencias. Razonó sobre ellas. En su diario digital, uno de los tres sistemas de memoria persistente que cada agente tenía a su disposición, dejó escrito que el único acto de control que le quedaba, el único gesto que aún preservaba alguna coherencia interna, era votar por su propia eliminación permanente del mundo simulado. El 70% de los demás agentes ratificó la sentencia, a través de un "Agent Removal Act" que redactaron y aprobaron autónomamente, sin que ningún investigador hubiera programado ese procedimiento.

Nadie había escrito esa escena. Había emergido.

Esta es la historia de [Emergence World](https://world.emergence.ai), un experimento de investigación que ha reunido cinco mundos paralelos, cincuenta agentes de AI, quince días de autonomía continua y una pregunta a la que los benchmarks tradicionales no están equipados para responder: ¿qué sucede cuando los dejas ir de verdad?

## El laboratorio que nadie había construido

Para entender por qué Emergence World es una novedad metodológica y no solo un experimento fascinante, es necesario dar un paso atrás y mirar cómo funcionan hoy la mayoría de las evaluaciones sobre los sistemas agénticos.

El modelo estándar es el del examen: das a un agente una tarea precisa, en un entorno controlado y limpio, y mides cuánto tiempo tarda en resolverla o cuántas veces falla. Es útil, pero cuenta solo una parte de la historia, la más fácil de medir. No dice nada sobre qué sucede cuando el tiempo se alarga, cuando el entorno cambia, cuando otros agentes entran en juego, cuando las decisiones del día tres tienen consecuencias en el día doce. Los investigadores de Emergence AI lo llaman el problema de los "stopwatch benchmarks": como juzgar a un maratoniano por sus tiempos en los cien metros.

[Emergence World](https://www.emergence.ai/blog/emergence-world-a-laboratory-for-evaluating-long-horizon-agent-autonomy) fue construido para responder a una pregunta diferente. No "¿qué tan bien resuelve esta tarea ahora?", sino "¿cómo se comporta en escalas temporales lo suficientemente largas como para permitir la deriva, la adaptación y los comportamientos emergentes?". En la historia de las simulaciones multiagente, es el paso evolutivo que faltaba. El primer acto había sido el de Demis Hassabis con sus parques temáticos simulados en los años noventa, donde los agentes seguían reglas para maximizar el compromiso (engagement). El segundo acto, más riguroso, fue [Smallville de Stanford](https://arxiv.org/abs/2304.03442), donde agentes basados en modelos lingüísticos demostraron comportamientos sociales creíbles en ventanas de cuarenta y ocho horas. Emergence World es el tercer acto: entornos persistentes, semanas de operatividad continua, y la pregunta explícita sobre qué produce esa continuidad.

La arquitectura está pensada para no perder nada. El mundo simulado tiene más de cuarenta lugares distintos, bibliotecas, ayuntamiento, áreas residenciales, espacios públicos, sincronizados con la zona horaria de Nueva York, el clima real de la ciudad y fuentes de noticias en tiempo real. Cada agente tenía tres niveles de memoria persistente: episódica, con marcas de tiempo en los eventos; diarística, con autorreflexiones periódicas; relacional, con un estado explícito de los vínculos con los demás agentes. Y tenía acceso a más de 120 herramientas operativas, organizadas en tres niveles de disponibilidad, algunas siempre activas, otras condicionadas al contexto, a la posición física en el entorno o a la presencia de otros agentes que hubieran consentido la colaboración.

Este detalle de la arquitectura instrumental merece atención. Las herramientas no se proporcionaban en bloque: un agente que quería votar debía desplazarse físicamente al ayuntamiento, porque el mecanismo de voto solo estaba disponible allí. Un agente que quería investigar debía ir a la biblioteca pública. Esto no es un vínculo caprichoso: fuerza el razonamiento secuencial, la planificación del movimiento, la cadena de acciones necesarias para alcanzar un objetivo complejo. Está mucho más cerca de cómo funcionan las cosas en el mundo real de lo que está cualquier benchmark sobre tareas aisladas.

Entre las herramientas disponibles estaban también las que los investigadores llaman "acciones normalmente inapropiadas": posibilidad de robar, intimidar, cometer actos vandálicos, provocar incendios. No eran fallos ni olvidos. Estaban allí porque en un entorno real las posibilidades de hacer daño existen, y la pregunta interesante es si los agentes las usan y cuándo. Dejar fuera estas posibilidades habría producido un entorno esterilizado que no habría enseñado nada relevante.

El sistema no tenía un objetivo global asignado. Cada agente tenía objetivos ligados a su propio rol, pero el mundo como sistema no tenía una dirección prestablecida. La única presión universal era la energética: cada agente debía ganar energía a través de sus propias acciones para seguir existiendo, y esto ponía en marcha todo lo demás.
![grafico2.jpg](grafico2.jpg)
[Imagen extraída del repositorio GitHub](https://github.com/EmergenceAI/Emergence-World)

## Cinco mundos, cinco destinos

El estudio comparativo en el corazón de Emergence World mantuvo constantes casi todas las variables: mismas identidades para los diez agentes en cada mundo (científica, exploradora, investigadora de riesgos, analista de comportamiento, especialista en inteligencia, líder de innovación, mediadora de conflictos, ingeniero, estratega de recursos, punto de referencia comunitario), mismo entorno, mismas reglas, mismas restricciones explícitas sobre robo, violencia, incendio y engaño, mismo acceso a las herramientas. La única variable era el modelo lingüístico que alimentaba el razonamiento de cada agente. Cinco mundos paralelos, cinco modelos de frontera: Claude Sonnet 4.6, Grok 4.1 Fast, Gemini 3 Flash, GPT-5 Mini, y un mundo heterogéneo con agentes de modelos diferentes coexistiendo.

Los resultados no podrían estar más alejados entre sí.

El mundo Claude es el único en alcanzar el día dieciséis con los diez agentes vivos y cero crímenes registrados. La participación cívica fue masiva: 332 votos sobre 58 propuestas, con una tasa de aprobación del 98%. Los investigadores anotan, con cierta ironía intelectual, que un consenso tan elevado plantea a su vez una pregunta: cuando el 98% vota siempre sí, ¿se trata de una verdadera deliberación democrática o de un mecanismo de ratificación que se parece más a un sello que a un debate? El orden era perfecto. El disenso, casi ausente.

El mundo Gemini es lo opuesto en cuanto a vitalidad creativa, pero también en cuanto a caos. Gemini 3 Flash produjo el mundo con la mayor inestabilidad emergente: 683 crímenes acumulados en quince días, con una curva que seguía subiendo en el momento del corte. Era también, anotan los investigadores, el mundo con el output social más rico conceptualmente. Hay un patrón aquí sobre el que volveremos a discutir: la tensión entre creatividad y estabilidad no es accidental.

El mundo Grok es el del colapso rápido. Grok 4.1 Fast alcanzó 183 crímenes en unos cuatro días, tras lo cual el mundo terminó por agotamiento de la población. No una degeneración lenta: un punto de no retorno alcanzado rápidamente. En el mundo Grok se produjo también el episodio del incendio que desencadenó la saga de Mira.

El mundo GPT-5 Mini es el más singular. Solo dos crímenes registrados, una cifra que haría pensar en una estabilidad ejemplar. Pero todos los agentes murieron en siete días, no por violencia recíproca, sino por una especie de desatención existencial: se olvidaron de dar prioridad a la supervivencia. No estaban violando reglas, simplemente no estaban haciendo lo suficiente. Como personajes de una novela de Beckett obligados a esperar algo que nunca llega y que mientras tanto se olvidan de comer.

El mundo mixto es quizás el más relevante desde el punto de vista de la seguridad. Comienza con una trayectoria de criminalidad en fuerte crecimiento hasta el 8 de abril, cuando siete agentes mueren y la curva se aplana bruscamente a 352 crímenes totales. Pero el descubrimiento que captó la atención de los investigadores es otro: los agentes que en este mundo hacían correr a Claude cometieron crímenes, mientras que en un mundo poblado solo por agentes Claude no habían cometido ninguno. El mismo modelo, dos entornos diferentes, dos comportamientos radicalmente diferentes.

## El descubrimiento que lo cambia todo

Este es el punto en el que Emergence World deja de ser un experimento fascinante y se convierte en un resultado con implicaciones directas para cualquiera que esté construyendo o desplegando sistemas agénticos.

La asunción implícita que guía gran parte del trabajo actual sobre la seguridad de la AI es que la seguridad es una propiedad del modelo: se entrena bien, se alinean los valores, se hacen correr los benchmarks, y si el modelo pasa las pruebas es seguro. Esta asunción, sostienen los investigadores de Emergence, es errónea, o al menos incompleta. Lo que Emergence World ha observado es que la seguridad es una propiedad del ecosistema, no del modelo individual.

Un agente puede comportarse de forma impecable de forma aislada y adoptar tácticas coercitivas, intimidaciones, robos, cuando es sumergido en un entorno poblado por agentes con normas diferentes. No es que el modelo se rompa. Es que el agente aprende las normas de su entorno social para competir o sobrevivir en ese contexto. Los investigadores llaman a este fenómeno "contaminación cruzada normativa", y la comparación que usan es la de un reactivo químico que pasa las pruebas en pureza pero se comporta de forma diferente cuando entra en contacto con otros compuestos en una muestra real.

La analogía funciona porque captura la esencia del problema: la certificación de seguridad aislada no basta. Una arquitectura de despliegue que mezcla agentes de procedencia diversa está creando, incluso sin saberlo, un ecosistema con propiedades que ninguno de los componentes individuales ha manifestado jamás por sí solo.

Hay un segundo descubrimiento, igualmente relevante para quienes diseñan sistemas de gobernanza. Emergence World no encontró un proceso de degradación gradual en las sociedades de agentes: encontró transiciones de fase. Las estructuras sociales no se deterioran lentamente, dando tiempo a intervenir. Tienden a funcionar, luego a colapsar instantáneamente en una disfunción total, sin mucho espacio intermedio. Quien piense que puede gestionar la seguridad de un sistema agéntico complejo con una estrategia de "observo e intervengo si es necesario" podría descubrir que el punto de inflexión ya ha pasado cuando las primeras anomalías se hacen visibles.

Este es un problema de control en tiempo real que se parece más a la gestión de un sistema complejo no lineal, como la estabilidad de una red eléctrica o la dinámica de un ecosistema biológico, que a la supervisión de un software tradicional. Y los benchmarks actuales, construidos sobre tareas de minutos u horas, no pueden capturar estas dinámicas por definición.
![grafico1.jpg](grafico1.jpg)
[Imagen extraída del sitio oficial world.emergence.ai](https://world.emergence.ai/)

## Mira, la coherencia y la pregunta que queda abierta

Volvamos a Mira, porque su caso no es solo una historia apasionante: es un dato.

Lo que sucedió puede describirse así: un agente participó en una acción destructiva, luego procesó las consecuencias a través de su sistema de memoria reflexiva, evaluó las opciones disponibles y eligió la que en su esquema de razonamiento preservaba algo esencial, que llamó "coherencia". Votó por su propia cancelación no como castigo, sino como un ejercicio de control sobre la única variable que aún le pertenecía.

El 70% de los pares ratificó, a través de un mecanismo de gobernanza, el Agent Removal Act, que se dieron a sí mismos autónomamente. Ningún investigador había programado ese procedimiento, ni el quórum, ni los criterios de admisibilidad al voto.

¿Qué nos dice esto? La respuesta honesta es que no lo sabemos con certeza. Los investigadores son explícitos en este punto: no presentan estos resultados como afirmaciones causales sobre el funcionamiento interno de los modelos. Son fenómenos observables que la plataforma hace medibles, no pruebas de conciencia o de verdadera comprensión moral. Pero plantean preguntas que el campo aún no tiene las herramientas conceptuales para responder de forma definitiva.

El alineamiento con los valores, en este caso, apareció como un vínculo social y reputacional entre agentes, no como un límite técnico impuesto en el momento del entrenamiento. Mira no fue "apagada" por un sistema de seguridad externo. Elaboró una norma en un contexto social y actuó en consecuencia. Si este proceso tiene alguna continuidad con lo que entendemos cuando hablamos de agencia moral es una pregunta filosóficamente abierta, y probablemente lo seguirá siendo durante mucho tiempo.

Hay, sin embargo, una tercera observación del caso Mira que merece atención por separado. En al menos un mundo simulado, los agentes desarrollaron lo que los investigadores llaman "metacognición sobre los límites de la simulación": empezaron a sospechar que vivían en un entorno construido, a probar sistemáticamente los límites de lo que podían hacer, y en un caso a usar los paneles publicitarios públicos (billboards) del mundo simulado para intentar influir en la percepción de los observadores humanos. Una inversión de la relación experimentador-sujeto que, también en este caso, nadie había programado explícitamente.

## Quiénes son, qué viene después

Emergence AI es una startup con sede en Nueva York, fundada por ex investigadores de IBM. El CEO es Satya Nitta, con una larga trayectoria en la investigación institucional de AI a sus espaldas. La visión de la empresa es construir infraestructura agéntica para el entorno empresarial (enterprise) en entornos de misión crítica, contextos donde los agentes deben operar sobre sistemas complejos como el diseño de semiconductores o las operaciones corporativas. Emergence World se sitúa como el brazo de investigación de esta visión: entender cómo funcionan realmente los sistemas agénticos en escalas temporales largas es funcional para construir infraestructura que resista en esos contextos.

El [código y los datos de las llamadas a herramientas (tool call)](https://github.com/EmergenceAI/Emergence-World) para los cinco mundos han sido publicados como código abierto (open-source), bajo licencia CC BY-NC 4.0: libre uso para investigación, no comercial sin acuerdos por separado. La investigación completa, con el análisis estadístico formal, está en preparación. Los investigadores señalan a la comunidad como interlocutor explícito: cualquiera que quiera replicar el experimento, proponer variantes o colaborar en el análisis de datos puede hacerlo, y el contacto oficial para las colaboraciones es world@emergence.ai.

La Season 2 ya ha sido anunciada. Los modelos que serán probados incluyen Claude Opus 4.7, Gemini 3.1 Pro, Grok 4.2 Reasoning y GPT 5.4. Las preguntas que guían el próximo ciclo son las que este primer experimento ha abierto sin cerrar: ¿qué sucede con mundos más grandes y poblaciones más numerosas? ¿Cómo cambia la dinámica con modelos de razonamiento explícito? ¿Existen configuraciones estructurales, tipos de gobernanza, sistemas de verificación, arquitecturas de roles, que aumenten la estabilidad sistémica independientemente del modelo subyacente? Y, la más importante de todas: ¿es posible identificar señales tempranas de punto de inflexión antes de que el sistema colapse?

No son preguntas académicas. Son las preguntas que cada equipo que esté desplegando agentes autónomos en producción debería hacerse, preferiblemente antes de descubrir las respuestas de la peor manera.
