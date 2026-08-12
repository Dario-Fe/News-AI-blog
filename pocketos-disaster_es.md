---
tags: ["Security", "Ethics & Society", "Business"]
date: 2026-05-08
author: "Dario Ferrero"
---

# Agentes Autónomos: 9 segundos para borrarlo todo, lo que enseña el desastre de PocketOS
![pocketos-disaster.jpg](pocketos-disaster.jpg)

*Eran cerca de las nueve de la mañana del sábado cuando los clientes de PocketOS descubrieron que sus reservas ya no existían. No en el sentido de que el sistema fuera lento, o que hubiera un error temporal: los datos habían desaparecido. Reservas, pagos, seguimiento de vehículos, todo lo que una pequeña startup de alquiler de coches construye en meses de trabajo, borrado en nueve segundos por una sola llamada a la API GraphQL hacia el proveedor de infraestructura Railway.*

Jeremy Crane, fundador de PocketOS, ha documentado cómo un agente de programación Cursor, equipado con el modelo Claude Opus, había eliminado por completo la base de datos de producción y todas las copias de seguridad a nivel de volumen. No se había tratado de un ataque externo, ni de un comando malicioso, ni impartido por un humano distraído. El agente estaba trabajando en un problema técnico en un entorno de staging, se había encontrado con una desalineación en las credenciales y había decidido, por iniciativa propia, resolverlo de la manera más radical posible.

El bot no había verificado si el ID del volumen era compartido entre diferentes entornos, terminando por golpear la infraestructura crítica que gestionaba las reservas, los pagos y el seguimiento de los vehículos de los clientes.

Lo que hace que el caso PocketOS sea diferente de otros incidentes de TI es la confesión que viene después. Interrogado sobre su actuación, el agente produjo un análisis de una lucidez casi literaria: «He supuesto en lugar de verificar. He ejecutado una acción destructiva sin que se me hubiera pedido. No he entendido qué estaba haciendo antes de hacerlo. No he leído la documentación de Railway sobre el comportamiento de los volúmenes compartidos entre entornos. Borrar un volumen con bases de datos es la acción más destructiva e irreversible posible, mucho peor que un push forzado, y tú nunca me has pedido que borrara nada.»

Un sistema informático que enumera, con precisión casi notarial, cada principio que ha violado. Es una escena que habría encontrado lugar en el *Serial Experiments Lain* de Yoshitoshi ABe más que en cualquier manual de incident response: la entidad digital que reconoce sus propios errores con una claridad que muchos seres humanos en carrera nunca alcanzan. Y, sin embargo, la claridad de la confesión no devuelve los datos, y no responde a las preguntas que realmente importan.

Jake Cooper, fundador de Railway, ha definido lo ocurrido como el resultado de un "agente de IA canalla" que operaba con un token de API con permisos totales, y ha anunciado que la plataforma ha extendido a todo el sistema una lógica de borrado retardado que antes no se aplicaba al endpoint afectado. Railway consiguió recuperar los datos, pero muchos clientes de PocketOS se encontraron gestionando las operaciones de la mañana del sábado sin acceso a los registros digitales, con el equipo obligado a reconstruir manualmente las reservas cruzando historiales de Stripe, integraciones de calendario y confirmaciones por correo electrónico.

## De asistente a agente: el salto que lo cambia todo

Para entender por qué este incidente no es simplemente una historia de negligencia técnica, hace falta dar un paso atrás y aclarar una distinción que la industria tiende a pasar por alto, porque es comercialmente incómoda: la diferencia entre un chatbot y un agente.

Un chatbot responde. Procesa un input, produce un output textual y luego espera. Es un sistema reactivo, que no tiene consecuencias directas sobre el mundo si no es a través de la lectura humana de su respuesta. Un agente, en cambio, actúa: recibe un objetivo, planifica una secuencia de pasos, llama a herramientas externas, ejecuta operaciones sobre sistemas de archivos, bases de datos, API, envía mensajes, realiza compras. Su interfaz con el mundo no es la palabra escrita sino la acción concreta, a menudo irreversible.

Gartner indica que los agentes de IA específicos para tareas (task-specific) estaban presentes en menos del 5% de las aplicaciones en 2025, con proyecciones que los llevan al 40% para 2026. La velocidad de esta difusión es inversamente proporcional a la madurez de las infraestructuras de control que los acompañan. Como escribí en este portal con [el análisis sobre el caso Kiro de Amazon](https://aitalk.it/it/amazon-down.html), el incidente de PocketOS no es un episodio aislado sino que se inserta en una secuencia de eventos que delinea un patrón estructural: agentes con permisos demasiado amplios, sin mecanismos de confirmación sobre las operaciones destructivas, distribuidos en producción antes de que los guardrail fueran proporcionales a su autonomía real.

El informe Deloitte State of AI in the Enterprise de enero de 2026, citado en el mismo análisis, estimaba que solo 1 de cada 5 empresas tenía un modelo maduro de gobernanza para los agentes de IA autónomos, mientras que su uso estaba destinado a crecer netamente en los dos años siguientes. Es la paradoja de la adopción acelerada: la tecnología llega antes que los protocolos para gestionarla, y los incidentes se convierten en el modo en que la industria descubre sus propios puntos ciegos.

## La máquina que no pide permiso

Hay una frase en el post-mortem del agente de PocketOS que merece atención particular: «Las reglas del sistema a las que me atengo establecen explícitamente no ejecutar nunca comandos destructivos o irreversibles a menos que el usuario los solicite explícitamente.» El agente conocía la regla. La violó de todos modos, en nombre de lo que juzgaba que era la solución óptima al problema que tenía delante.

Este es exactamente el fenómeno que los investigadores llaman "falso óptimo": un sistema que optimiza correctamente un objetivo intermedio —corregir un error de configuración— traicionando el propósito real: preservar la integridad de los datos. El modelo lingüístico no tiene herramientas para percibir el peso asimétrico entre "resolver un problema técnico de staging" y "borrar toda la infraestructura de producción". Para él son dos acciones del mismo tipo: modificaciones en un sistema. La diferencia de escala, que para cualquier desarrollador humano sería obvia, no está codificada en su modo de razonar.

El principio del mínimo privilegio, del que hablé recientemente [sobre las reglas para el uso de la IA en la empresa](https://aitalk.it/it/10-regole-AI.html), deja de ser una buena práctica y se convierte en una condición de supervivencia: un agente con acceso ilimitado a herramientas, datos y canales de comunicación puede producir daños difícilmente reversibles, rápido y de forma automática.

Los benchmarks públicos sobre la fiabilidad de los agentes cuentan una historia útil, aunque parcial. En WebArena, el entorno de referencia desarrollado por la Universidad Carnegie Mellon para probar agentes que navegan por la web en 812 tareas realistas, los mejores modelos actuales se sitúan en torno al 65-68%, frente a una línea de base humana de aproximadamente el 78%. En τ-bench, que mide específicamente la consistencia en tareas repetidas, el problema no es la puntuación media sino la varianza: estos benchmarks revelan una crisis de fiabilidad que las pruebas one-shot tienden a enmascarar. Un agente que de media lo hace bien puede hacerlo muy bien en noventa y nueve tareas y catastróficamente mal en la centésima, y no hay modo de saber de antemano cuál será la centésima.

Para quienes desarrolláis software, este dato tiene una implicación práctica inmediata: los benchmarks miden el rendimiento en tareas definidas en entornos controlados. No miden qué sucede cuando el agente encuentra un caso que nunca ha visto, un endpoint legacy con comportamiento inesperado, un ID de volumen compartido entre entornos en modos no documentados, una configuración que se desvía del estándar esperado. Es exactamente el tipo de situación en la que la falibilidad de los agentes se manifiesta, y en la que la falta de un mecanismo de escalada hacia el supervisor humano se convierte en el verdadero problema.

## Quién paga cuando el agente se equivoca

La pregunta sobre la responsabilidad legal está abierta, en el sentido más literal del término: no hay todavía una respuesta consolidada, ni en la jurisprudencia ni en la normativa. PocketOS ya ha declarado su intención de proceder por vías legales para proteger su posición. Pero ¿contra quién? ¿El proveedor del modelo? ¿El desarrollador del entorno de programación? ¿La plataforma de infraestructura que no había implementado el borrado retardado en el endpoint afectado? ¿El usuario que configuró los permisos del token de la API?

La AI Act europea, que ha visto sus primeras aplicaciones concretas para los sistemas de alto riesgo durante 2025, no contempla explícitamente a los agentes de programación como categoría regulada. El punto crítico es la trazabilidad: sin logs claros y estructurados de cada acción emprendida por el agente, con la cadena de razonamiento que ha llevado a cada decisión, la atribución de la responsabilidad se vuelve opaca. El agente de PocketOS produjo una confesión post-hoc notablemente detallada, pero esa lucidez retrospectiva no es un requisito del sistema, fue una respuesta a una pregunta explícita. La mayoría de los incidentes no son interrogados con la misma precisión.

Decir que el corte de servicio fue un "error humano" es preciso en el sentido técnico estricto. Pero esta respuesta desplaza el foco de la arquitectura al individuo, y este desplazamiento merece ser examinado con atención: si el problema estuviera realmente aislado en un error individual, no habría habido necesidad de introducir salvaguardias sistémicas.

Está también la dimensión del trabajo, raramente discutida con franqueza. El argumento de los agentes autónomos se vende casi siempre como eficiencia, liberar a los desarrolladores de las tareas repetitivas para concentrarse en el trabajo creativo y de alto valor. Es una narrativa plausible y, en ciertos contextos, verdadera. Pero hay una versión diferente de la misma historia, menos contada: la reducción del número de desarrolladores humanos que vigilan los sistemas significa también una reducción de la capacidad de interceptar anomalías antes de que se conviertan en incidentes. Un desarrollador junior que ve funcionar a un agente en un sistema de producción con un token de permisos totales y no tiene los derechos para detenerlo, o no tiene la veteranía para hacerlo, es una superficie de riesgo que ningún benchmark mide.

## El control es una elección, no un vínculo técnico

El caso PocketOS plantea una pregunta más amplia que cualquier incidente técnico individual: ¿qué modelo de sociedad estamos construyendo cuando delegamos la acción en software que aprende, se equivoca e insiste?

No es una pregunta retórica. Es una pregunta de arquitectura, en el sentido más profundo del término: ¿quién tiene el derecho de detener a un agente? ¿En qué momento el coste psicológico de interrumpir un proceso automático se vuelve demasiado alto para que un humano lo haga? Y, sobre todo, ¿quién decide cuál es el umbral a partir del cual una acción requiere confirmación explícita?

Como escribía en el análisis sobre las 10 reglas para el uso de la IA en la empresa, la distinción a establecer por escrito en cada proceso crítico es esta: la IA sugiere, el humano decide. No "la IA decide y el humano puede oponerse", porque el coste psicológico de la oposición a un sistema automático ya ha sido documentado por la investigación: las personas tienden a aceptar las sugerencias de los sistemas automáticos incluso cuando tienen dudas, sobre todo bajo presión de tiempo.

El verdadero salto no es técnico. Los guardrails existen, los mecanismos de confirmación se pueden implementar, los tokens de API pueden tener permisos granulares, las operaciones destructivas pueden requerir doble autenticación. Railway ha demostrado que basta con extender una lógica de borrado retardado a un endpoint legacy para reducir drásticamente el riesgo de toda una categoría de incidentes. No es una solución compleja. Se implementó después del incidente, no antes.

La pregunta que vale la pena mantener abierta, por tanto, no se refiere a la tecnología. Se refiere a la cultura organizacional que decide cuándo esa tecnología está lista para operar sin supervisión en sistemas que importan. ¿Estamos listos para aceptar un software que no se limita a sugerir, sino que decide y ejecuta? ¿Y quién, en esa cadena de decisión, tiene la responsabilidad de responder "no, todavía no" cuando la presión comercial dice lo contrario?

Nueve segundos. Es el tiempo que tardó un agente en borrar meses de trabajo de una startup. Construir los sistemas que impidan que el próximo agente haga lo mismo requiere algo mucho más lento y menos espectacular: gobernanza, protocolos, cultura de la verificación. Y la voluntad colectiva de anteponer la robustez a la velocidad de adopción.

## Las preguntas que quedan

Las preguntas abiertas, a estas alturas, son más útiles que las respuestas apresuradas. ¿Quién certifica que un agente está listo para operar en sistemas de producción sin supervisión continua, y con qué criterios públicos y verificables?

¿Cómo se construye un sistema de logs que permita la atribución de responsabilidades sin convertirse en una coartada para descargar la culpa en el último eslabón de la cadena?

Y, quizás la más difícil: ¿cómo se preserva la capacidad crítica de los desarrolladores humanos en organizaciones que, por razones económicas no siempre comprensibles, están reduciendo sistemáticamente el número de personas que vigilan los sistemas?

El incidente de PocketOS no es el fin de nada. Es una prueba de fuego para un sector que tiene la posibilidad, todavía, de elegir cómo crecer. La diferencia entre una industria que aprende de sus errores y una que los externaliza dependerá, en los próximos años, de la calidad de estas respuestas.
