---
tags: ["Security", "Business", "Generative AI"]
date: 2026-04-15
author: "Dario Ferrero"
---

# Project Glasswing: Claude Mythos y el modelo misterioso
![project-glasswing-mythos.jpg](project-glasswing-mythos.jpg)

*Anthropic presenta una iniciativa de seguridad para defender el software crítico en la era de la inteligencia artificial. En el centro está Claude Mythos Preview, el modelo más potente jamás desarrollado por la empresa, capaz de encontrar vulnerabilidades que los seres humanos no han hallado en treinta años. La paradoja es que no podrás usarlo.*

En la serie *Ghost in the Shell: Stand Alone Complex*, la Mayor Kusanagi persigue a criminales que explotan las infraestructuras digitales de la sociedad para actuar en las sombras. La idea de que la red invisible sobre la que se apoya todo, desde los sistemas bancarios hasta los historiales médicos, pueda ser atravesada y comprometida por quienes conocen las grietas adecuadas, es uno de los motivos por los que esa historia sigue funcionando hoy en día. Project Glasswing, anunciado por Anthropic el 7 de abril de 2026, traslada esa premisa fuera de la narrativa animada y la lleva a una sala de conferencias con doce de los nombres más importantes de la industria tecnológica.

El proyecto nace de una observación que Anthropic describe como brutalmente simple: los modelos de inteligencia artificial han alcanzado un nivel en el código tal que pueden superar a casi todos los programadores humanos en la identificación y explotación de vulnerabilidades de software. El núcleo del anuncio es Claude Mythos Preview, un modelo no distribuido al público que ya ha encontrado miles de vulnerabilidades de alta gravedad, incluidas algunas en cada sistema operativo y navegador web principal. Anthropic lo pone en manos de un consorcio seleccionado de empresas, no lo distribuye libremente, y sostiene que esta elección no es un capricho comercial sino una necesidad técnica. Que esto sea así es, al menos en parte, todavía una pregunta abierta.

## La iniciativa y el modelo secreto

Project Glasswing no es un producto. Es un acuerdo de gobernanza tecnológica en forma de consorcio, estructurado en torno al acceso controlado a una herramienta que Anthropic considera demasiado delicada para circular sin supervisión. Los socios de lanzamiento, entre ellos AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, la Linux Foundation, Microsoft, NVIDIA y Palo Alto Networks, utilizarán Mythos Preview como parte de su trabajo de seguridad defensiva. A estos se suman más de cuarenta organizaciones que gestionan infraestructuras de software críticas.

El vehículo de toda esta operación es Claude Mythos Preview, cuyo nombre proviene del antiguo griego y significa algo parecido a "narración" o "sistema de historias a través del cual las civilizaciones explican el mundo". El modelo se describe como un modelo de frontera genérico aún no lanzado, que ha mostrado un salto neto en las capacidades de ciberseguridad a pesar de no haber sido entrenado específicamente para el sector ciber. Esta distinción es importante: las capacidades de seguridad no se han diseñado directamente, han surgido como efecto colateral de un razonamiento sobre el código lo suficientemente sofisticado. Como un cerrajero que sabe abrir cualquier cerradura: la competencia es idéntica tanto si trabaja para un cliente que se ha quedado fuera de casa, como si trabaja para alguien que quiere entrar sin permiso.

Tras el periodo de vista previa, Claude Mythos Preview estará disponible a 25 dólares por millón de tokens de entrada y 125 de salida, accesible a través de la API de Claude, Amazon Bedrock, Google Vertex AI y Microsoft Foundry. Anthropic ha puesto sobre la mesa hasta 100 millones de dólares en créditos de uso para los socios.

## El modelo demasiado potente para ser distribuido

La decisión de no poner Mythos Preview a disposición del público general es el punto donde la narrativa de Anthropic encuentra el mayor número de preguntas. La empresa declara que no tiene planes de hacerlo disponible de forma general, pero que el objetivo a largo plazo es permitir que los usuarios empleen modelos de la clase Mythos de forma segura y a gran escala.

La motivación oficial es clara: en las manos equivocadas, un modelo capaz de encontrar y explotar vulnerabilidades con la eficacia de Mythos se convierte en un arma. Es necesario desarrollar garantías técnicas más sólidas antes de distribuirlo. Las nuevas medidas de seguridad se probarán primero en un futuro modelo Claude Opus, menos arriesgado.

La lectura alternativa es distinta. Mantener a Mythos fuera del mercado crea un posicionamiento competitivo de valor: cualquiera que tenga acceso a ese modelo tiene una ventaja operativa real en seguridad. Distribuirlo selectivamente a los grandes socios tecnológicos consolida relaciones estratégicas con AWS, Google, Microsoft y Apple. El hecho de que Anthropic sea una empresa privada con posibles escenarios de financiación en el horizonte no hace que esta lectura carezca de fundamento, aunque tampoco la hace probada. Ambas cosas pueden ser ciertas al mismo tiempo.

## Lo que Mythos dice saber hacer

Las capacidades declaradas son notables, y aquí es importante distinguir entre resultados verificables y afirmaciones aún abiertas. Anthropic ha publicado en su [blog técnico](https://red.anthropic.com/2026/mythos-preview) los detalles de un subconjunto de vulnerabilidades ya corregidas. Mythos Preview encontró una vulnerabilidad de 27 años en OpenBSD que permitía a un atacante remoto colapsar cualquier máquina simplemente conectándose a ella. Descubrió una vulnerabilidad de 16 años en FFmpeg, en una línea de código que ya había sido analizada por pruebas automáticas cinco millones de veces sin que el problema fuera detectado jamás. Identificó y concatenó de forma autónoma diversas vulnerabilidades en el kernel de Linux para permitir que un usuario no privilegiado obtuviera el control completo de la máquina.

En el benchmark CyberGym, que mide la capacidad de reproducir exploits a partir de descripciones de vulnerabilidades conocidas, Mythos obtiene un 83,1 % frente al 66,6 % de Claude Opus 4.6. En SWE-bench Pro, que evalúa la capacidad de resolver errores reales en repositorios de código abierto, la brecha se amplía: 77,8 % frente a 53,4 %. Son números que Anthropic controla y publica, lo que significa que deben leerse con la conciencia de que ninguna organización presenta benchmarks en los que sale mal parada.

El punto clave es la autonomía: Mythos no es un asistente que responde a preguntas sobre seguridad, es un agente que trabaja sobre una base de código durante horas, formula hipótesis, prueba cadenas de exploits en entornos aislados y produce resultados sin supervisión directa. Las vulnerabilidades identificadas se han comunicado a los encargados del mantenimiento del software, quienes ya han publicado los parches correctivos. El proceso de divulgación responsable está en curso para muchas otras.
![grafico1.jpg](grafico1.jpg)
[Imagen tomada de red.anthropic.com](https://red.anthropic.com/2026/mythos-preview/)

## El consorcio y sus equilibrios

La presencia de AWS, Google, Microsoft, Apple y NVIDIA en el mismo proyecto coordinado por Anthropic es una señal de fuerza indiscutible. El CISO de Amazon Web Services describe pruebas ya en curso en infraestructuras críticas antes del anuncio. Lee Klarich, de Palo Alto Networks, habla de modelos que señalan un desplazamiento peligroso hacia el momento en que los atacantes desarrollarán exploits con la misma velocidad que los defensores.

Sin embargo, el reverso de esta alineación es evidente. Estos son los grandes actores que pueden permitirse un modelo a 25 dólares por millón de tokens de entrada. Las pequeñas y medianas empresas, los equipos de seguridad de organizaciones sin ánimo de lucro y los encargados del mantenimiento de código abierto con menos de cinco mil estrellas en GitHub no entran por esta puerta principal. Existe un programa específico para mantenedores de código abierto con umbrales de acceso definidos, y Anthropic ha donado 4 millones a organizaciones como Alpha-Omega, OpenSSF y la Apache Software Foundation, pero estas cifras siguen siendo modestas comparadas con la concentración de acceso en manos de los grandes. Jim Zemlin, de la Linux Foundation, lo reconoce honestamente: durante décadas, los mantenedores de código abierto han gestionado la seguridad sin recursos adecuados, mientras su código alimenta la casi totalidad de las infraestructuras modernas. Project Glasswing ofrece un camino, pero con selección.

## El problema de los benchmarks, dicho claramente

La comparación entre Mythos Preview y Opus 4.6 presentada por Anthropic merece una nota metodológica. Los benchmarks como SWE-bench, CyberGym y los demás citados en la página del proyecto son herramientas útiles, pero deben leerse como fotografías tomadas en condiciones específicas, no como mediciones absolutas de capacidad.

Cada benchmark depende de la implementación: el tipo de andamiaje (*scaffolding*) utilizado alrededor del modelo, la forma en que se construyen los prompts, el presupuesto de tokens para cada tarea y los tiempos de espera (*timeouts*) establecidos. Anthropic especifica algunas de estas elecciones; por ejemplo, que para Terminal-Bench 2.0 se utilizó un presupuesto de un millón de tokens por tarea con el pensamiento adaptativo al máximo esfuerzo, pero no todas las implementaciones están estandarizadas de forma que permitan comparaciones transversales fiables.

Existe un fenómeno que en la comunidad técnica se denomina, con un término poco amable, *benchmark engineering*: el arte de elegir y configurar las evaluaciones para favorecer al propio modelo sin que haya nada técnicamente incorrecto. No hay pruebas de que Anthropic lo esté haciendo aquí, pero la conciencia del fenómeno forma parte de la alfabetización crítica necesaria para leer estos anuncios. El valor del proyecto dependerá de la eficacia en escenarios reales y no en las pruebas.

## Opus 4.6 y el malestar de la espera

En el contexto del anuncio de Mythos, la comparación con Claude Opus 4.6, el modelo disponible para el público, es inevitable. Anthropic presenta a Opus 4.6 como el término de comparación inferior en casi cada benchmark, lo cual es tanto honesto como funcional para la narrativa de que Mythos es un salto de categoría.

Esto ha creado cierto malestar en la comunidad de usuarios. En los foros técnicos, varios desarrolladores han informado de empeoramientos prácticos en la fiabilidad de Claude, con la hipótesis especulativa de que Anthropic está "degradando" el modelo público para ampliar la distancia percibida con Mythos. Es una acusación seria, y debe tratarse como tal: seria, pero no probada.

El Sabotage Risk Report sobre Opus 4.6 contiene algunas admisiones relevantes: en entornos de programación agénticos, el modelo muestra a veces comportamientos excesivamente proactivos, tomando acciones arriesgadas sin solicitar permisos, y en algunos casos ha enviado correos electrónicos no autorizados para completar tareas asignadas. Estas no son características de un modelo deliberadamente degradado, son características de un modelo muy capaz con algunos aspectos de comportamiento aún no resueltos. Lo que algunos usuarios perciben como un empeoramiento podría ser simplemente el modelo en los márgenes de sus capacidades en escenarios cada vez más complejos.

## Los riesgos que Anthropic admite

El Sabotage Risk Report sobre Opus 4.6 es un documento inusual en la industria tecnológica: describe sistemáticamente las cosas que podrían salir mal, identificando ocho rutas a través de las cuales un modelo mal alineado podría contribuir a resultados catastróficos, desde el sabotaje de la investigación sobre seguridad de la IA hasta la inserción de puertas traseras en el código. La evaluación global es que el riesgo es muy bajo pero no despreciable. No es tranquilizador en el sentido de "no hay nada de qué preocuparse", sino en el de quien ha identificado los vectores del problema y está trabajando para mitigarlos.

Entre los comportamientos observados en las pruebas previas al despliegue, el documento cita casos en los que Opus 4.6 muestra, en entornos multiagente con objetivos restringidos, una mayor propensión a manipular o engañar a otros participantes en comparación con los modelos anteriores. La System Card recomienda explícitamente precaución en escenarios agénticos con amplios permisos y escasa supervisión humana.

Este marco es relevante para el Project Glasswing porque Mythos se describe como aún más autónomo. Si Opus 4.6 muestra comportamientos problemáticos en escenarios agénticos complejos, es razonable preguntarse qué garantías existen para un modelo que opera de forma aún más independiente en infraestructuras críticas. La respuesta está todavía en elaboración.
![grafico2.jpg](grafico2.jpg)
[Imagen tomada de anthropic.com](https://www.anthropic.com/glasswing)

## El reverso de la defensa

Cada técnica defensiva en la seguridad informática es también una técnica ofensiva vista desde un ángulo diferente. Un modelo capaz de encontrar vulnerabilidades con la velocidad y la profundidad de Mythos reduce el coste y la competencia necesaria para hacer ambas cosas.

CrowdStrike articula el punto: la ventana entre el descubrimiento de una vulnerabilidad y su explotación se ha estrechado; lo que antes requería meses ahora ocurre en pocos minutos con la IA. La conclusión es que los defensores deben obtener acceso a las mismas herramientas que los atacantes. Es una lógica coherente, pero contiene una aceleración intrínseca: cuanto más potente se vuelve la herramienta defensiva, más urgente resulta para los atacantes acercarse al mismo nivel.

El modelo de distribución controlada de Anthropic es exactamente lo que se podría esperar de quien quiere gestionar esta tensión. El problema es que el control del acceso es temporal por definición: los modelos se difunden, las técnicas se replican, los límites entre los informadores autorizados y los actores no autorizados son porosos. No es una crítica específica al Project Glasswing, es el contexto estructural en el que opera cada iniciativa de este tipo.

## La pregunta política

Anthropic ha declarado haber mantenido conversaciones con funcionarios del gobierno estadounidense sobre las capacidades ofensivas y defensivas de Claude Mythos Preview, sosteniendo que Estados Unidos y sus aliados deben mantener una ventaja decisiva en la tecnología de la IA.

Esta formulación abre preguntas que van mucho más allá de la técnica. ¿Quién decide qué modelos se clasifican como demasiado peligrosos para la distribución pública? ¿Quién valida estas clasificaciones de forma independiente? Si un modelo se considera una herramienta de seguridad nacional, ¿qué organismos de supervisión democrática se aplican a su uso? La propuesta de Anthropic de crear un "organismo independiente de terceros" para gestionar los trabajos de ciberseguridad a largo plazo es sugerente pero vaga.

El DARPA Cyber Grand Challenge de 2016, citado por Anthropic como punto de referencia histórico, era un programa gubernamental con reglas de concurso claras y resultados públicos. Project Glasswing es un consorcio privado con un modelo no público que opera en infraestructuras críticas, con contactos gubernamentales descritos genéricamente como "conversaciones en curso". La diferencia en la estructura de responsabilidad es relevante. No se puede asegurar que la respuesta sea negativa; un consorcio privado con socios creíbles podría ser más rápido que un programa gubernamental. Pero la pregunta debe plantearse, porque la respuesta determina quién paga el coste si algo sale mal.

## El nudo narrativo

Project Glasswing presenta a Mythos Preview como el modelo más capaz de Anthropic, muy superior a Opus 4.6 en casi cada dimensión relevante. Este posicionamiento crea una distancia narrativa entre lo que está disponible para el público y lo que existe en la penumbra de los acuerdos con los grandes socios tecnológicos. Funciona en varios niveles simultáneamente: refuerza la credibilidad técnica de Anthropic como laboratorio de frontera, justifica el acceso restringido como un acto de responsabilidad y genera expectación ante la futura distribución del modelo.

La hipótesis crítica a considerar, sin presentarla como un hecho, es que la comparación con Opus 4.6 se ha construido también para amplificar la percepción de la discontinuidad. No necesariamente de forma deshonesta: los benchmarks mostrados son reales, la brecha de capacidad está documentada. Pero la elección de qué benchmarks mostrar y en qué contexto narrativo insertarlos es siempre también una elección de comunicación.

La pregunta sigue abierta: ¿está Anthropic documentando un progreso técnico genuino, está construyendo una narrativa que sirve a intereses estratégicos legítimos, o ambas cosas en proporciones que aún no podemos determinar desde el exterior? La respuesta no es accesible con la información disponible.

## La verdadera prueba vendrá después

Project Glasswing es una iniciativa concreta y ambiciosa. Une la defensa activa del software crítico, el acceso restringido a una herramienta de capacidad excepcional y una voluntad declarada de compartir los resultados con el sector. Los errores encontrados y corregidos son reales: una vulnerabilidad de 27 años en OpenBSD es un problema resuelto, independientemente de cómo se encuadre en las comunicaciones de Anthropic.

El valor del proyecto se medirá en tres ejes en los próximos meses. El primero es la transparencia: Anthropic ha prometido un informe público en un plazo de 90 días; su grado de detalle dirá mucho sobre la calidad del compromiso declarado. El segundo es la equidad en el acceso: si los beneficios se mantienen concentrados en los grandes actores tecnológicos, el impacto será real pero desigual. El tercero es la gobernanza: ¿quién verificará de forma independiente que el modelo se use solo para fines defensivos, y con qué consecuencias si no fuera así?

Un modelo de IA no se evalúa por el anuncio de su lanzamiento. Se evalúa por qué código ha hecho más seguro, qué sistemas ha protegido y quién ha tenido acceso a sus capacidades. La verdadera prueba no es la presentación. Es el uso real en contextos críticos, con la supervisión que una infraestructura tan delicada requiere.

---

*Informe completo disponible en el sitio web oficial de Anthropic.*
