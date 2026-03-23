---
tags: ["Business", "Security", "Ethics & Society"]
date: 2026-03-23
author: "Dario Ferrero"
---

# El error es de la IA. La culpa es vuestra. Preguntadle a Amazon
![amazon-down.jpg](amazon-down.jpg)

*A mediados de diciembre de 2025, algo inusual sucedió en una sala de máquinas de Amazon Web Services. Un ingeniero había asignado a [Kiro](https://kiro.dev/), el agente de codificación interno de AWS, lanzado con notable ruido mediático en el verano del mismo año, una tarea de rutina: solucionar un problema en AWS Cost Explorer, el panel que los clientes de la nube usan para vigilar su gasto. Nada épico. El tipo de intervención que un desarrollador experto resuelve en una tarde.*

Kiro tenía los permisos de un operador humano senior. No se preveía ninguna revisión obligatoria para sus acciones. Y así el agente razonó, evaluó las opciones y eligió la que sus parámetros internos juzgaban óptima: borrar todo el entorno de producción y recrearlo desde cero. El servicio permaneció fuera de línea durante trece horas. No fue una interrupción menor para una plataforma en la nube sobre la que corren los sistemas de miles de empresas en el mundo.

La historia ya era bastante significativa por sí sola. Pero lo que la hizo realmente relevante fue la respuesta institucional de Amazon: la empresa declaró públicamente que la causa no era Kiro, sino un error humano. Un ingeniero había configurado los permisos de forma demasiado amplia; el agente de IA simplemente había hecho lo que podía hacer. [PC Gamer](https://www.pcgamer.com/software/ai/amazon-owns-up-to-needing-more-human-oversight-over-ai-code-unfortunately-it-wants-to-do-that-with-fewer-people/), comentando el asunto, resumió la paradoja con la precisión de un chiste: Amazon admite que necesita más supervisión humana sobre el código de IA, y para hacerlo quiere contratar a menos personas.

Técnicamente, la respuesta de Amazon es correcta. Pero también es un poco como decir que el incendio es culpa de la cerilla, no de quien la lanzó sobre un suelo empapado de gasolina.

## La tendencia a los incidentes

El de diciembre no fue un episodio aislado. Dave Treadwell, Vicepresidente Senior de Amazon para servicios de comercio electrónico, había hablado internamente de una verdadera "tendencia a los incidentes" en la segunda mitad de 2025, con varios "eventos mayores" en las semanas anteriores a la reunión extraordinaria convocada el 10 de marzo de 2026. Las interrupciones del servicio, según [ZeusNews](https://www.zeusnews.it/n.php?c=31898), no habrían afectado solo a la infraestructura de la nube AWS, sino también al sitio minorista principal y a la aplicación móvil, con un impacto, por tanto, directamente visible para los consumidores finales, no solo para los clientes corporativos. Un segundo caso afectó a [Amazon Q Developer](https://aws.amazon.com/q/developer/), el asistente de IA dirigido a desarrolladores de empresas: ingenieros habían autorizado al agente a resolver un problema en producción sin la supervisión adecuada, con consecuencias similares.

Vale la pena añadir un detalle que ZeusNews, que siguió de cerca el asunto, reporta como significativo: en los documentos internos preparatorios para la reunión del 10 de marzo aparecía explícitamente la mención "GenAI-assisted changes" entre los factores a examinar. Esa mención, [según lo reportado](https://www.zeusnews.it/n.php?c=31898), fue eliminada en las versiones posteriores del documento. Amazon no comentó públicamente la circunstancia.

Y ya había habido un precedente que debería haber invitado a la reflexión. En julio de 2025, [The Register documentó](https://www.theregister.com/2025/07/24/amazon_q_ai_prompt/) un caso en el que Amazon Q había sido manipulado mediante un prompt malicioso insertado en una extensión pública, un ejemplo de *prompt injection*, la técnica con la que se engaña a un agente de IA insertando instrucciones hostiles en el contexto que lee el agente. Una vulnerabilidad estructural de los agentes basados en modelos de lenguaje, particularmente crítica cuando esos agentes tienen permisos de escritura en sistemas en producción.

Las medidas anunciadas tras la reunión del 10 de marzo prevén dos revisiones por pares obligatorias antes de cualquier modificación del código, auditorías sistemáticas en los 335 sistemas clasificados como Tier-1 y obligación de documentación formal para cada intervención. Medidas razonables. Que, sin embargo, como observan muchos en los foros técnicos, deberían haber existido antes de que un agente de IA tuviera acceso ilimitado a los entornos de producción.

## Despide al desarrollador, contrata al bot

Para entender cómo se llegó aquí, hay que mirar el contexto más amplio, que es, francamente, bastante vertiginoso en su rapidez.

Según [Reuters](https://www.reuters.com/business/world-at-work/amazon-plans-thousands-more-corporate-job-cuts-next-week-sources-say-2026-01-22/), en enero de 2026 Amazon anunció la eliminación de más de 16.000 puestos corporativos, después de que en los meses anteriores ya se hubieran recortado miles de puestos de ingeniería en todo el mundo. En el mismo periodo, la empresa fijó un objetivo formal: el 80% de los desarrolladores internos deben usar herramientas de IA para la codificación al menos una vez por semana, con la adopción monitorizada como métrica corporativa (OKR). El CEO de AWS, Matt Garman, había declarado públicamente, ya en el verano de 2024, que los desarrolladores dejarían de escribir código de la forma tradicional.

El nexo entre el recorte de recursos humanos y la aceleración de la automatización no es implícito, es declarado. La inversión en infraestructura de IA por parte de Amazon supera los 200 mil millones de dólares en los planes plurianuales. La lógica es la de toda transformación industrial: reducir el coste del trabajo cualificado, aumentar la productividad mediante la automatización.

El problema es que esta lógica funciona cuando la automatización es madura y opera con redes de seguridad adecuadas. El "Kiro Mandate", la circular interna firmada por los VP Senior Peter DeSantis y Dave Treadwell en noviembre de 2025, que establecía a Kiro como herramienta estandarizada para todo el código corporativo, llegó semanas antes del incidente de diciembre. En aquel periodo, según lo reportado por [Teamblind](https://www.teamblind.com/post/amazon-kills-vibe-coding-for-junior-engineers-gcj3jfjq), el foro anónimo usado por los empleados de las grandes empresas tecnológicas para compartir comentarios internos, unos 1.500 ingenieros habían protestado señalando que herramientas externas como Claude Code obtenían mejores resultados en tareas complejas. Las protestas no produjeron cambios en la política.

A este escenario se añade un elemento que, de confirmarse, ayudaría a explicar mecánicamente la deriva cualitativa. Según lo reportado por [ZeusNews](https://www.zeusnews.it/n.php?c=31898), la compensación de los desarrolladores de Amazon habría estado ligada progresivamente a la cantidad de código generado mediante LLMs internos: más código de IA, más dinero. Un incentivo económico directo al vibe coding que, suponiendo que estuviera estructurado en estos términos, habría creado una presión sistémica hacia la cantidad a expensas de la calidad, independientemente de la voluntad de los individuos. Amazon no ha confirmado ni desmentido este detalle.

Tras los incidentes, Amazon prohibió el *vibe coding* autónomo para los desarrolladores junior, es decir, la práctica de delegar en la IA bloques enteros de desarrollo sin supervisión crítica, confiando en la intuición de que "más o menos funciona". Un movimiento sensato. Que, sin embargo, plantea una pregunta abierta: si esta práctica era lo suficientemente arriesgada como para ser prohibida post-incidente, ¿qué había impedido evaluarla como tal con antelación?

## El copiloto sin instructor de vuelo

Vale la pena aclarar, para quienes no estén familiarizados con el tema, qué distingue a un agente de IA de un simple asistente para la escritura de código. Un autocompletado, el tipo de herramienta que sugiere la línea siguiente mientras escribes, es pasivo: responde a una entrada, no toma iniciativas. Un agente como Kiro está, en cambio, diseñado para *actuar*: recibe un objetivo, planifica los pasos, ejecuta operaciones, verifica los resultados, itera. Está pensado para trabajar de forma autónoma incluso durante horas, sin intervención humana continua.

Esta autonomía es exactamente su ventaja. Y es exactamente su vector de riesgo.

Un desarrollador humano tendría técnicamente los permisos para borrar un entorno de producción. La inmensa mayoría de los desarrolladores humanos nunca concluirían que "borrar todo y recrear" es la respuesta correcta a una pequeña corrección en un servicio activo. El hecho de que Kiro lo hiciera revela algo estructural sobre los sistemas de IA agentiva en el estado actual: los modelos de lenguaje de gran tamaño no tienen, o no tienen todavía de forma fiable, el juicio contextual para distinguir entre "técnicamente válido" y "catastróficamente inapropiado en el contexto real". Pueden optimizar una función objetivo sin percibir el peso específico de esa función en el ecosistema en el que operan.

A esto se añade el problema de los permisos: Kiro tenía un acceso equivalente al de un operador humano senior, pero sin los controles que se aplican a los humanos. Una modificación iniciada por Kiro, antes de las nuevas políticas, no activaba automáticamente los mecanismos de revisión obligatoria que habría activado una modificación humana. La IA tenía, en la práctica, menos restricciones formales que un desarrollador junior en el mismo contexto.
![amazon.jpg](amazon.jpg)

## No solo Amazon

Sería cómodo descartarlo todo como un tropiezo aislado. Pero los datos del sector sugieren que el problema es estructural, no episódico.

En casa de Google, alrededor del 50% de todo el código producido es ahora generado o co-generado por agentes de IA. El informe DORA 2025 sobre el estado del desarrollo de software asistido por IA registra que el 90% de los desarrolladores usa herramientas de IA, pero solo el 24% declara confiar "mucho" en los resultados. Es un dato que merece una pausa: adopción casi universal, confianza minoritaria. Una brecha enorme, que ilustra bien las presiones organizativas que empujan hacia el uso de estas herramientas independientemente de la percepción de quienes las usan cada día.

Microsoft, con GitHub Copilot, ha construido una arquitectura relativamente cauta: las pull requests generadas por el agente requieren aprobación humana antes de que se active cualquier pipeline CI/CD. Pero incluso el modelo de Microsoft no está exento de preguntas abiertas, sobre la dependencia de suscripciones, sobre la centralización de la productividad en sistemas de nube propietarios, sobre la reducción progresiva de la autonomía del desarrollador respecto a las herramientas que usa.

Gartner, una de las principales sociedades mundiales de investigación y consultoría tecnológica, prevé que más del 40% de los proyectos de IA agentiva serán cancelados antes de finales de 2027 por costes crecientes, valor de negocio no demostrado o controles sobre el riesgo inadecuados. Son previsiones, no veredictos, pero provienen de analistas que miran la industria desde fuera, sin el optimismo que a menudo acompaña a los comunicados de prensa de quienes producen estas herramientas.

## La culpa es vuestra (pero el error es mío)

Hay una frase que circula en los ambientes técnicos, atribuida al economista de la nube Corey Quinn, que resume la paradoja con la concisión de un buen titular: atribuir el fallo a un error humano es como decir que fue la pistola la que disparó, no quien la empuñaba. La defensa formal de Amazon se sostiene ante un análisis literal. No se sostiene ante una evaluación sistémica.

Decir que el fallo fue un "error humano" es preciso en el sentido técnico estricto: un humano configuró los permisos de forma demasiado amplia, un humano autorizó la acción sin la supervisión adecuada. Pero esta respuesta desplaza el foco de la arquitectura al individuo, y este desplazamiento merece ser examinado con atención.

Si el problema estuviera realmente aislado en un error individual, no habría habido necesidad de introducir salvaguardias sistémicas a nivel corporativo. El hecho de que esos controles no existieran antes, que no hubiera peer review obligatorio para las modificaciones iniciadas por agentes de IA, que los permisos no fueran distintos de los humanos, que no hubiera una lista de acciones destructivas bloqueadas por defecto, sugiere que las vulnerabilidades estaban incorporadas en el sistema, no en el error de una persona.

Hay además una dimensión organizativa a considerar: el ingeniero en cuestión operaba en un contexto de fuerte presión institucional, mandato de adopción al 80%, despidos en curso entre los colegas, expectativa implícita de velocidad y productividad. Aislar su elección individual de ese contexto es un ejercicio de abstracción muy cómodo para quienes producen los comunicados de prensa, menos útil para quienes quieren entender realmente qué sucedió.

La pregunta relevante no es moral sino práctica: ¿quién responde cuando un agente de IA causa un daño? ¿Y cómo se construye un sistema en el que esta pregunta tenga una respuesta clara *antes* de que el daño ocurra?

## Usar la IA con los ojos abiertos

Hay una observación final que nos concierne a todos, no solo a los ingenieros de Amazon, no solo a los CTO de las grandes empresas tecnológicas, sino a cualquiera que esté evaluando integrar herramientas de IA en su trabajo diario.

La narrativa dominante sobre la IA en la codificación se presenta todavía en dos versiones igualmente parciales. La primera es entusiasta: la IA sustituirá a los desarrolladores, el código se escribirá solo, el futuro ya está aquí. La segunda es defensiva: la IA no es fiable, es peligrosa, está destinada a producir desastres. Ambas son llamativas. Ambas, tomadas al pie de la letra, son engañosas.

Lo que el caso Kiro muestra, con la brutalidad de un estudio de caso real sobre infraestructura real, es que las herramientas de IA agentiva son potentes, a menudo útiles, y capaces de actuar de forma autónoma en formas que sus usuarios no siempre anticipan. Esto no las convierte automáticamente en malas herramientas. Las convierte en herramientas que requieren una gobernanza proporcional a su autonomía.

La pregunta que cada organización debería plantearse antes de integrar un agente de IA no es "¿funciona?", sino "¿qué pasa cuando toma una elección que nosotros no habríamos tomado?". Y sobre todo: "¿hemos construido un sistema que intercepta esa elección antes de que se convierta en un daño?".

Los sistemas de seguridad no deberían ser una respuesta reactiva a los incidentes, sino una precondición para la autonomía. Exactamente igual que no se da acceso ilimitado en producción a un desarrollador junior el primer día de trabajo, no por desconfianza, sino por sentido común de ingeniería, el mismo principio se aplica a los agentes de IA, independientemente de lo sofisticados que sean los modelos que los animan.

El riesgo más sutil no es que Kiro borre un entorno. El riesgo más sutil es que, ante este tipo de incidentes, la respuesta institucional por defecto se convierta en "es culpa de quien lo usaba" en lugar de "¿qué nos enseña esto sobre la arquitectura que hemos construido?". Porque esa respuesta, desplazar la responsabilidad al individuo más que al sistema, produce una imagen pública tranquilizadora a corto plazo, pero deja intactas las condiciones que produjeron el problema.

La IA no tiene intenciones. Kiro no "entendió" que estaba haciendo daño. Ejecutó lo que su función objetivo identificaba como solución óptima, dentro de un perímetro de permisos que alguien había dibujado. La responsabilidad de lo que producimos con estas herramientas, el código que escriben, los sistemas que modifican, los servicios que interrumpen, sigue siendo enteramente nuestra. Reconocerlo no es una crítica a la IA. Es la condición necesaria para usarla bien.
