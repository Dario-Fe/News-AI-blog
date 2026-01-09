---
tags: ["Business", "Ethics & Society", "Security"]
date: 2026-01-09
author: "Dario Ferrero"
---

# 'Inteligencia Artificial e Ingeniería de Software: Lo que deben hacer las empresas'. Conversación con Enrico Papalini
![papalini-interview.jpg](papalini-interview.jpg)

*Enrico Papalini tiene un currículum que haría palidecer a muchos consultores de LinkedIn: más de veinte años construyendo y orquestando sistemas de software donde el error no es una opción. Como Jefe de Excelencia en Ingeniería e Innovación en Borsa Italiana, parte del grupo Euronext, ha liderado la adopción de la inteligencia artificial en un contexto donde la palabra "crash" tiene implicaciones que van mucho más allá de un error de ejecución. Antes de eso, recorrió el sector desde diferentes ángulos: de Microsoft a Intesa Sanpaolo, de startups tecnológicas a gigantes financieros, siempre en el papel de quien tiene que hacer que las cosas funcionen cuando todos los demás pueden permitirse que no funcionen.*

Su [perfil de LinkedIn](https://www.linkedin.com/in/enricopapalini/) cuenta una trayectoria profesional donde la innovación siempre ha tenido que casarse con la fiabilidad. No es un académico que teoriza desde fuera, ni un fundador que puede permitirse el lujo de "moverse rápido y romper cosas". Es alguien que ha tenido que responder a preguntas como: "¿Podemos usar esta tecnología en un sistema que procesa millones de transacciones al día?" La respuesta correcta nunca es un sí entusiasta ni un no conservador, sino un "depende, y te explico cómo".

Ahora Papalini ha sintetizado esta experiencia en un libro que está dando que hablar: [*Intelligenza Artificiale e Ingegneria del Software: Cosa debbono fare le imprese*](https://amzn.to/3Z12Ng9), publicado también en [versión inglesa](https://www.amazon.com/dp/B0G7LPJBTH) con el título *Non-Deterministic Software Engineering: How to Build Reliable Software with AI Assistants Without Losing Quality, Security, or Control*. El subtítulo ya es un manifiesto: cómo construir software fiable con asistentes de IA sin perder calidad, seguridad o control.

## El pacto silencioso roto

Mientras el mercado editorial tecnológico sigue produciendo manuales sobre "cómo usar ChatGPT para programar más rápido", Papalini ha elegido un ángulo completamente diferente. Su libro se basa en investigaciones realizadas por DX en más de 180 empresas, integra las métricas DORA (DevOps Research and Assessment) adaptadas al desarrollo asistido por IA, y analiza casos de estudio de quienes ya se han quemado o han encontrado un equilibrio: OpenAI, Shopify, Google. Para escribirlo, ha dialogado con algunos de los nombres más importantes de la ingeniería de software contemporánea: Martin Fowler, el teórico de los patrones de diseño y la refactorización; Kent Beck, el inventor de la Programación Extrema; Addy Osmani, gerente de ingeniería de Google Cloud.

Le pido que me cuente qué le impulsó a escribir precisamente este libro, precisamente ahora, cuando todos parecen centrados en la velocidad milagrosa prometida por los asistentes de IA.

"Todos hablan de velocidad, pero la verdadera revolución es otra", responde Papalini. "Es un cambio en la naturaleza de las herramientas que usamos. Durante cuarenta años hemos dado por sentada una cosa: escribes un código y este hace exactamente lo que has escrito. Siempre. Sobre esta certeza hemos construido todo: cómo probamos, cómo depuramos, cómo trabajamos en equipo. La IA generativa rompe este pacto silencioso. No porque sea defectuosa, sino porque tiene una naturaleza probabilística. Le pides lo mismo dos veces y te da respuestas diferentes. A veces geniales, a veces equivocadas con una seguridad desconcertante".

La metáfora que utiliza para enmarcar el problema es esclarecedora: "Las empresas que piensan en sustituir a los programadores por la IA y miran con complacencia cuántas líneas de código más consiguen producir, se pierden lo esencial: están introduciendo una variable aleatoria en el corazón de sus sistemas. Es un poco como si un ingeniero civil construyera un puente con materiales que *podrían* soportar el peso previsto. Funciona de maravilla cuando pasan pocos coches, pero cuando pasa el primer camión, se derrumba".

Escribió el libro, dice, "porque me parecía que faltaba una guía para quienes deben navegar este cambio sin estrellarse, pero también sin renunciar a los beneficios, que son reales".

## Del determinismo a la tolerancia

El corazón conceptual del libro se resume en el título en inglés: *Non-Deterministic Software Engineering*. Es un oxímoron deliberado. La ingeniería de software, por definición, siempre ha sido el arte de construir sistemas deterministas: la entrada A siempre produce la salida B. Papalini propone acoger en nuestros procesos herramientas que, por su naturaleza, no respetan esta regla fundamental.

Le pregunto cómo cambia el paradigma del control de calidad cuando pasamos de un mundo donde el código hacía exactamente lo que estaba escrito, a un mundo donde acogemos sistemas probabilísticos en nuestros IDE.

"Cambia todo y, al mismo tiempo, no cambia nada. Lo sé, parece una paradoja", comienza. "Cambia todo porque 'funciona' ya no significa 'es correcto'. El código generado por la IA compila, pasa las pruebas que has escrito, tiene un aspecto profesional. Pero podría ocultar vulnerabilidades, gestionar mal los casos límite o estar escrito de una manera que dentro de seis meses nadie entenderá. No cambia nada porque los fundamentos de la ingeniería de software siguen siendo los mismos: pruebas, revisiones, pensamiento de diseño. De hecho, se vuelven más importantes que antes".

La clave, según Papalini, está en adoptar un enfoque que hasta ahora ha sido ajeno a los desarrolladores de software: "La verdadera novedad es que tenemos que aprender a razonar por 'tolerancias'. Martin Fowler utiliza a menudo esta analogía: su mujer es ingeniera de estructuras y nunca diseña al límite exacto. Siempre calcula un margen de seguridad. Nosotros, los desarrolladores, nunca hemos tenido que hacerlo porque nuestros 'materiales' eran perfectamente predecibles. Ahora ya no lo son. Y quien no se construya estos márgenes, tarde o temprano verá derrumbarse su 'puente'".

Es un cambio de mentalidad radical para toda una profesión que ha construido su identidad sobre la certeza absoluta de la ejecución. Como decirle a un relojero suizo que a partir de ahora tendrá que aceptar que sus relojes puedan tener un margen de error variable.

## La ilusión de la velocidad

Uno de los pasajes más contraintuitivos del libro se refiere a los datos sobre la productividad. Papalini cita un estudio de METR (una organización independiente que evalúa las capacidades de los sistemas de IA) que muestra cómo los desarrolladores pueden sentirse un 20% más rápidos con la inteligencia artificial, mientras que las pruebas reales en tareas medibles indican que en algunos casos son un 19% más lentos.

Le pregunto cómo es posible esta discrepancia perceptiva y, sobre todo, cómo las empresas pueden medir la verdadera productividad sin caer en el marketing de las herramientas.

"¿Sabes qué fue lo que más me impactó de ese estudio? No fue el dato de que con la IA fueran un 19% más lentos. Fue que los desarrolladores *creían* que eran más rápidos. Y seguían creyéndolo incluso después de ver los resultados", cuenta Papalini. "¿Por qué sucede esto? Porque la IA reduce el esfuerzo *percibido*. Te sientes más fluido, menos bloqueado. Es como tener un colega siempre disponible para ayudarte, que no te juzga y no te hace esperar. Psicológicamente es potente. Pero 'me siento productivo' y 'estoy produciendo valor' son dos cosas muy diferentes".

La solución que propone no es filosófica sino metodológica: "Para no caer en el bombo publicitario, una empresa debería establecer una línea de base *antes* de adoptar las herramientas. Sin un 'antes', nunca podrán demostrar un 'después'. Cuando el director general pregunte qué ha aportado la IA, se necesitan cifras, no sensaciones. Pero las cifras deben ser las correctas: dejen de medir líneas de código o cuántas sugerencias de la IA se aceptan. Midan lo que importa: funcionalidades lanzadas, errores en producción, tiempo para resolver incidentes. Y una cosa fundamental: medir cuán motivados siguen los desarrolladores".

Es una llamada a la disciplina de la ingeniería en un momento de euforia colectiva. Como en los primeros días de las metodologías ágiles, cuando todos medían la "velocidad" en puntos de historia sin preguntarse si realmente estaban entregando valor.

## Lunes por la mañana, tres movimientos

El subtítulo en italiano del libro plantea una pregunta directa: "Qué deben hacer las empresas". No "qué podrían hacer" o "qué sería bueno hacer", sino "qué deben hacer". Es un imperativo e implica urgencia.

Le pido a Papalini que sea aún más directo: si tuviera que indicar las tres primeras acciones concretas que un director de tecnología o un director general debería tomar el lunes por la mañana para no verse abrumado, ¿cuáles serían?

"La primera es hacer una auditoría de lo que *ya* está sucediendo", responde sin dudar. "Te lo garantizo: tus desarrolladores ya están usando ChatGPT, Copilot, Claude, lo sepas o no. No por malicia, sino simplemente porque estas herramientas funcionan. Antes de escribir políticas, entiende la situación real".

Este fenómeno del Shadow AI, el uso no autorizado de herramientas inteligentes, es uno de los temas recurrentes en el libro. No es un problema de indisciplina, sino de necesidad: cuando las herramientas oficiales tardan en aprobarse o son demasiado limitadas, la gente encuentra alternativas.

"La segunda es trazar una línea clara entre la exploración y la producción", continúa Papalini. "Prototipado rápido, experimentos, pruebas de concepto, todo es legítimo. Pero debe quedar *claro* que ese código no va a producción sin una reescritura consciente. El desastre clásico es el prototipo del viernes que se convierte en el sistema crítico del lunes porque 'total, funciona'".

Es el patrón que cualquiera que haya trabajado en una startup reconoce de inmediato: la demostración se convierte en producto, la solución temporal se convierte en arquitectura, lo temporal se vuelve permanente. Con la IA, este proceso se acelera peligrosamente porque generar un prototipo convincente es cuestión de minutos.

"La tercera es invertir en la capacidad de revisión, no en la de generación", concluye. "El cuello de botella ya no es escribir código, sino entenderlo, validarlo, mantenerlo. Si tus desarrolladores pueden generar diez veces más código pero la capacidad de revisión sigue siendo la misma, solo estás acumulando deuda técnica más rápido".

## La trampa del "funciona"

Andrej Karpathy, uno de los pioneros de la IA moderna y ex director de inteligencia artificial en Tesla, popularizó el término "vibe coding": programar siguiendo la intuición del momento, dejando que la IA sugiera direcciones que "parecen correctas". Es un enfoque fascinante y profundamente peligroso.

Papalini dedica varias páginas del libro a lo que él llama la "trampa del funciona". Le pido que me cuente cuáles son los riesgos a largo plazo para una base de código empresarial escrita principalmente siguiendo el "vibe" del momento sin una validación humana rigurosa.

"Te cuento una historia", comienza. "Martin Fowler había usado la IA para generar una visualización en formato vectorial SVG, nada complejo. Funcionaba perfectamente. Luego quiso hacer un cambio trivial: mover una etiqueta unos pocos píxeles. Abrió el archivo y encontró lo que él definió como 'una locura', un código que funcionaba, sí, pero estructurado de una manera completamente ajena, imposible de tocar sin romperlo todo. ¿La única opción? Tirarlo y regenerarlo desde cero".

La anécdota capta perfectamente el problema: "Este es el coste real y el riesgo del 'vibe coding' a escala empresarial. Creas sistemas que *funcionan* pero que *nadie entiende*. Y el software empresarial tiene que vivir años, a veces décadas. Tiene que ser modificado, ampliado, depurado a las tres de la mañana cuando algo explota".

La solución que propone es simple en su formulación pero requiere disciplina en su ejecución: "La regla que debemos seguir es sencilla: nunca confirmes código que no sepas explicar a un colega. Si está generado con IA y no entiendo cómo funciona, no está listo para la producción".

Es como el equivalente digital de la regla de los alpinistas: no subas a nada de lo que no sepas bajar.

## El precio de la falta de fiabilidad

En el libro, Papalini introduce el concepto de "impuesto a la falta de fiabilidad". Es un coste oculto pero medible del uso de sistemas generativos en la producción de código. Le pido que cuantifique, en términos concretos de seguridad y mantenimiento, cuánto le cuesta realmente a una empresa limpiar el código generado por la IA que parece correcto pero oculta vulnerabilidades.

"Las cifras dan que pensar", comienza. "Las investigaciones muestran que un porcentaje significativo del código generado por la IA contiene vulnerabilidades, algunas fuentes hablan de casi la mitad. Y lo insidioso es que son vulnerabilidades 'plausibles': el código parece profesional, utiliza patrones reconocibles. Solo que falta la validación de la entrada en ese punto crítico, o utiliza una función criptográfica obsoleta".

No se trata de errores evidentes que cualquier linter señalaría. Son errores de juicio, elecciones aparentemente razonables que en contextos específicos se convierten en agujeros de seguridad: "El coste directo es el tiempo de remediación. Pero el coste real es el que no ves de inmediato: la vulnerabilidad que pasa desapercibida durante meses, hasta que alguien la encuentra. En ese punto no estás pagando horas de desarrollo, estás pagando respuesta a incidentes, posibles filtraciones de datos, daños a la reputación".

Papalini también identifica un coste más sutil: "También hay un impuesto más sutil: la pérdida de confianza en el sistema. Cuando el equipo empieza a no fiarse de su propio código, todo se ralentiza. Cada modificación se convierte en un riesgo. Y lo mismo ocurre con los clientes: existe el riesgo de que se pasen a un competidor más fiable".

Su recomendación es pragmática: "La inversión sensata está en la prevención: escaneo de seguridad automático, formación específica, revisión humana obligatoria para todo lo que toque la autenticación o los datos sensibles. Cuesta menos que limpiar los desastres después y perder clientela".

## La cuestión de la soberanía

Uno de los capítulos más densos del libro aborda el tema de la soberanía de los datos y la seguridad en la era de los asistentes de IA. Las empresas se enfrentan a un triple desafío: proteger la propiedad intelectual del bloqueo del proveedor, prevenir el Shadow AI y mitigar lo que Papalini llama la "deuda de seguridad" del código probabilístico.

Le planteo una pregunta compleja: entre la velocidad de los modelos en la nube y la complejidad del código abierto en las propias instalaciones, ¿qué arquitectura estratégica recomienda para garantizar la privacidad y la seguridad sin que la protección de los activos se convierta en un coste insostenible?

"Es un verdadero desafío, lo vivo cada día en el sector financiero. Y la respuesta honesta es: depende de tu perfil de riesgo", comienza Papalini. "Para la mayoría de las empresas, un enfoque híbrido funciona: modelos en la nube para el código no sensible, con reglas claras sobre lo que puede salir y lo que no. Los principales proveedores ya ofrecen opciones empresariales con garantías contractuales serias. Quienes tienen requisitos más estrictos pueden optar por las instalaciones propias con modelos de código abierto. Llama, Mistral, DeepSeek tienen capacidades notables. El precio es la complejidad operativa".

Pero identifica una amenaza a menudo subestimada: "Pero, ¿sabes cuál es la amenaza más subestimada? El Shadow AI: desarrolladores que usan herramientas no autorizadas porque las oficiales tardan en aprobarse o son demasiado limitadas. La solución no es prohibir, sino ofrecer alternativas legítimas que sean lo suficientemente buenas como para no crear el incentivo de saltarse las reglas".

Es un enfoque que recuerda a la reducción de daños en las políticas sanitarias: en lugar de criminalizar comportamientos inevitables, poner a disposición alternativas más seguras.

## La formación en la era de las máquinas

Una de las secciones más provocadoras del libro se refiere al futuro de la formación y las competencias. Hay una distinción emergente entre los licenciados en informática tradicional y la nueva figura del ingeniero de IA, alguien que sabe orquestar sistemas inteligentes pero que puede que nunca haya escrito un analizador sintáctico desde cero.

Le pregunto a Papalini si la IA que permite a cualquiera generar código significa el fin del programador "puro", o si simplemente estamos subiendo el listón de las competencias arquitectónicas necesarias.

"El programador no está destinado a desaparecer, pero su papel está cambiando mucho", responde. "Piensa en lo que pasó cuando llegaron los lenguajes de alto nivel. Los programadores de ensamblador no desaparecieron, se convirtieron en especialistas de nicho. El grueso del trabajo se desplazó un peldaño más arriba".

La transición actual, según Papalini, sigue un patrón similar: "Ahora está sucediendo algo parecido. Está surgiendo una figura diferente, llamémosla 'orquestador': alguien que sabe descomponer problemas complejos, especificar requisitos con precisión, evaluar críticamente lo que produce la IA, tomar decisiones de arquitectura".

Pero aquí llega la paradoja: "¿La paradoja? Se necesita *más* experiencia, no menos. Un junior puede usar la IA para generar código que parece funcionar. Pero solo un senior reconoce cuándo ese código es una bomba de relojería, porque ha visto suficientes desastres como para reconocer las señales".

El riesgo sistémico que identifica es el de la atrofia de las competencias: "También hay que tener cuidado de no pensar que todos nacen orquestadores: si delegamos todo el trabajo de 'aprendizaje' a la IA, ¿cómo formamos a la próxima generación de seniors? Los datos nos dicen que el empleo de los desarrolladores más jóvenes ya está disminuyendo. Pero incluso quienes entran en el mercado corren el riesgo de no desarrollar nunca esas competencias profundas que solo se construyen a base de darse de cabezazos con los problemas".

## La programación en trío

Para resolver este dilema, Papalini propone en el libro un modelo que él llama "programación en trío", una evolución de la programación en pareja que incluye a la IA como tercer actor.

"En el libro propongo la 'programación en trío' como solución al problema de la formación", explica. "El junior trabaja con la IA para implementar las funcionalidades. La IA acelera, sugiere, genera código. Hasta aquí nada nuevo. El orquestador senior no escribe código, está ahí para hacer preguntas. 'Explícame qué hace este método'. '¿Por qué la IA ha elegido esta estructura de datos?'. '¿Qué pasa si la entrada es nula?'. '¿Cómo gestionarías un error de red aquí?'".

El mecanismo es pedagógicamente brillante: "Respondiendo a estas preguntas, el joven aprende. El senior, por su parte, transfiere ese saber tácito que no está en ningún manual, la intuición sobre lo que puede salir mal, la sensibilidad para el código que 'huele mal', la experiencia de quien ha visto sistemas derrumbarse".

Es como el aprendizaje en los talleres renacentistas: el maestro no pinta en lugar del alumno, sino que le hace notar dónde la perspectiva es incorrecta, por qué esa mezcla de colores no aguantará, dónde la composición pierde el equilibrio.

## El valor del juicio

Vuelvo al tema de la monetización y el valor. Papalini ha escrito varios artículos en Medium explorando cómo las empresas están tratando de obtener beneficios de la IA generativa. Le pregunto: más allá del software, ¿cómo ve el impacto de la IA generativa en el marketing y en la creación de productos digitales? ¿Es solo una cuestión de velocidad o está cambiando el valor mismo del producto?

"Sí, el valor está cambiando, pero de una manera contraintuitiva", responde. "Cuando todos pueden generar contenido, imágenes, código, la *producción* se convierte en una mercancía. Es abundante, por lo que vale menos. Lo que adquiere valor es todo lo demás: entender qué vale la pena construir, distinguir lo mediocre de lo excelente, tener una visión".

En el software, dice, lo ve manifestarse cada día: "Si cualquiera puede generar una aplicación que funcione en un fin de semana, ¿qué distingue a tu producto? Ya no es la implementación, es la comprensión del problema, la experiencia del usuario, la capacidad de evolucionar con el tiempo".

Y lo mismo ocurre con el marketing: "La IA puede producir infinitas variantes de textos publicitarios, imágenes, vídeos. Pero 'infinito' no significa 'eficaz'. Se necesita a alguien que sepa qué probar, cómo leer los resultados, cuándo parar".

La síntesis es elegante: "Estamos entrando en una era de abundancia cognitiva. El cuello de botella ya no es producir, es elegir, curar, juzgar".

Es como la transición de la escasez a la sobreabundancia en la industria musical. Cuando cualquiera puede grabar y distribuir un álbum, el valor se desplaza de la capacidad técnica de producción a la capacidad artística de crear algo que merezca la atención.

## Agentes autónomos y el futuro próximo

Estamos pasando de los simples asistentes de codificación (los diversos Copilots) a los sistemas agénticos autónomos, capaces teóricamente de tomar la iniciativa, coordinar tareas complejas e incluso depurar su propio código. Le pregunto cuál es su visión sobre la evolución de los agentes de IA en la ingeniería de software en los próximos cinco años. ¿Veremos sistemas que se autorreparan y se autodespliegan?

"En los próximos 12-18 meses veremos cómo la orquestación de agentes se convierte en una práctica común en las empresas más avanzadas", predice Papalini. "No veinte agentes en paralelo, eso es cosa de demostraciones. Dos o tres flujos de trabajo gestionados juntos: un agente que actualiza las pruebas, uno que migra las dependencias, uno que añade una funcionalidad menor. Todo mientras el desarrollador se centra en el trabajo que requiere juicio".

Pero advierte: "La palabra clave es 'verificable'. La atención humana sigue siendo el cuello de botella. No importa lo rápido que sea el agente si luego se tarda una semana en entender lo que ha hecho".

A largo plazo es prudente: "¿A cinco años? Soy prudente. Ya existen agentes que 'se autorreparan': retrocesos automáticos, infraestructura autorreparable. Pero, ¿agentes que se autodespliegan de forma completamente autónoma? Para sistemas críticos, lo dudo. Y ni siquiera estoy seguro de que debamos desearlo".

Su predicción más sólida se refiere al papel humano: "Mi predicción más segura: el papel del ingeniero se desplaza hacia la especificación y la validación, menos hacia la implementación. Pero este cambio requerirá *más* competencia por parte de los trabajadores, no menos".

## La atrofia de las competencias

Hay un tema que atraviesa todo el libro: el riesgo de que la adopción masiva de la IA no amplifique las capacidades humanas, sino que las atrofie. Es la pregunta ética y social que subyace a toda consideración técnica.

Le pregunto directamente: ¿cómo podemos garantizar que la adopción masiva de la IA en las empresas no devalúe la profesionalidad humana, sino que se convierta en un verdadero amplificador de las capacidades de los talentos?

"Es la pregunta que más me importa", responde Papalini. "El riesgo concreto lo llamo 'atrofia de las competencias'. Un ingeniero entrevistado por el MIT Technology Review contó que después de meses de uso intensivo de la IA, cuando intentó programar sin ella, se sentía perdido; cosas que antes eran instintivas se habían vuelto fatigosas. Es exactamente la señal de alarma que deberíamos escuchar".

La solución no es el rechazo, sino la intencionalidad: "La solución no es rechazar la IA, sería como rechazar la electricidad. Pero debemos ser intencionados sobre cómo la integramos, especialmente en los itinerarios de formación. Por eso en el libro propongo modelos como la 'programación en trío' para cultivar la capacidad de los talentos y no cometer el error de serrar el peldaño más bajo de la escalera por la que hemos subido, el proceso de aprendizaje que nos ha llevado a donde estamos".

## Más allá del software

Al final de la conversación, le pregunto si un director general de una empresa que no produce software puede encontrar valor en su libro. Es una pregunta legítima: el título habla explícitamente de ingeniería de software.

"Absolutamente, y te explico por qué", responde con convicción. "El software ha sido el primer dominio en ser invertido masivamente por la IA generativa, por lo que es el laboratorio donde ciertos fenómenos se han manifestado antes y de manera más medible. Pero los patrones que describo en el libro son universales, se refieren a la relación entre los seres humanos y los sistemas probabilísticos, y esto ya afecta a cualquier sector".

La generalización es convincente: "Tomemos el concepto central: el paso del determinismo al no determinismo. Cuando le pides a una IA que escriba código, no sabes exactamente lo que obtendrás. Pero lo mismo ocurre cuando le pides que escriba una campaña de marketing, que analice un balance, que redacte un contrato o que responda a un cliente. El resultado parece profesional, está formulado con seguridad, pero podría estar sutilmente equivocado de maneras que solo un experto reconoce".

Papalini traslada cada concepto del libro fuera del dominio del código: "El 'problema del 70%' funciona de forma idéntica en cualquier contexto. La IA te lleva rápidamente a un borrador que parece casi terminado: un informe, una presentación, un análisis de mercado. Pero ese 'casi' oculta el 30% donde se necesitan matices, contexto, juicio. El junior de marketing que acepta el texto generado por la IA sin entender por qué ciertas palabras funcionan y otras no, está cometiendo exactamente el mismo error que el programador que confirma código que no sabe explicar".

El tema de la formación se vuelve aún más urgente: "La 'trampa de la competencia' es quizás el tema más urgente para cualquier director general. Si tus analistas junior delegan en la IA la construcción de los modelos financieros, nunca aprenderán a hacerlos. Si tus jóvenes abogados usan la IA para los primeros borradores sin escribir nunca uno desde cero, nunca desarrollarán la intuición para los riesgos contractuales. Estás ahorrando tiempo hoy y destruyendo competencia mañana".

Incluso la programación en trío se generaliza: "La 'programación en trío' que propongo se convierte en 'trabajo en trío': un junior, un senior y la IA trabajando juntos. El junior usa la IA para acelerar, el senior hace las preguntas que fuerzan la comprensión. Funciona para formar a un analista, un consultor, un gestor de cuentas, cualquier rol donde la experiencia se construye haciendo".

Y el problema de la gobernanza atraviesa todas las funciones de la empresa: "Y luego está el Shadow AI, empleados que usan ChatGPT a escondidas porque las herramientas oficiales son demasiado lentas o limitadas. Ocurre en todas partes: en el departamento legal, en el servicio de atención al cliente, en recursos humanos. No es un problema tecnológico, es un problema de gobernanza que todo director general debe afrontar".

La conclusión es pragmática: "El libro utiliza el software como contexto, pero lo que cuenta es la historia de cómo integrar herramientas potentes pero poco fiables en el trabajo profesional sin perder calidad, competencias y control. Es el desafío de toda organización hoy en día, ya sea que produzca código, contratos, campañas publicitarias o análisis financieros".

Y añade una nota final que suena a manifiesto: "Un director general que lo lea no encontrará instrucciones para configurar Copilot, encontrará un marco para pensar en la adopción de la IA que puede aplicar a cualquier función de su empresa. Y, francamente, en este momento de exageración desenfrenada y expectativas infladas, un poco de lucidez de ingeniería puede venirle bien a cualquiera que tenga que tomar decisiones".

## Muchas respuestas que abren muchas preguntas

Concluimos esta larga charla. Papalini tiene que volver a ocuparse de sistemas que mueven capitales; yo tengo que transformar esta conversación en algo legible. Pero la sensación que queda es la de haber hablado con alguien que está viendo la misma película que todos nosotros, solo que con unos minutos de antelación.

El libro [*Intelligenza Artificiale e Ingegneria del Software*](https://amzn.to/3Z12Ng9) no es un manual técnico, a pesar de su título. Se parece más a esos ensayos de alpinismo escritos después de una expedición particularmente arriesgada: un mapa de las cosas que pueden salir mal, escrito por quien ha vuelto para contarlo. Con la única diferencia de que esta montaña la estamos escalando todos, nos guste o no, y alguien que ya ha hecho un par de intentos puede ser útil.

La verdadera pregunta no es si usaremos la inteligencia artificial para escribir código, hacer marketing, analizar datos o tomar decisiones. Ya la estamos usando. La pregunta es si lograremos hacerlo sin perder por el camino las competencias que nos permitieron llegar hasta aquí. Y sobre esta pregunta, por ahora, la respuesta sigue abierta.
