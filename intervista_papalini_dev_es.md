Cómo la IA está redefiniendo el oficio del programador: Conversación con Enrico Papalini

papalini-interview.jpg

Enrico Papalini ha pasado más de veinte años escribiendo y orquestando sistemas de software en contextos donde no puedes permitirte subir código que "probablemente funciona". Como Jefe de Excelencia en Ingeniería e Innovación en Borsa Italiana, parte del grupo Euronext, trabaja en infraestructuras donde un error no solo significa un ticket en Jira, sino potencialmente millones de euros en transacciones bloqueadas. Antes de eso: Microsoft, Intesa Sanpaolo, startups y grandes corporaciones. Su perfil de LinkedIn cuenta la trayectoria de alguien que ha tenido que equilibrar innovación y fiabilidad en cada etapa de su carrera.

No es el tipo de persona que teoriza desde fuera. Es alguien que ha tenido que responder a preguntas como: "¿Podemos desplegar esto en producción?" cuando "esto" involucra inteligencia artificial generativa y el sistema gestiona infraestructura crítica.

Ahora ha escrito un libro que resume esta experiencia: *Intelligenza Artificiale e Ingegneria del Software: Cosa debbono fare le imprese*, también disponible en inglés como *Non-Deterministic Software Engineering*. El libro se basa en investigaciones de DX sobre más de 180 empresas, integra las métricas DORA adaptadas al desarrollo con IA y analiza casos de estudio de quienes ya han pasado por ello: OpenAI, Shopify, Google. Para escribirlo, dialogó con Martin Fowler, Kent Beck y Addy Osmani.
El pacto silencioso roto

Mientras continúan saliendo tutoriales sobre "multiplica por 10 tu codificación con IA", Papalini ha decidido abordar el problema desde otro ángulo. Le pregunto qué lo impulsó a escribir precisamente este libro, precisamente ahora.

"Todos hablan de velocidad, pero la verdadera revolución es otra", responde. "Es un cambio en la naturaleza de las herramientas que usamos. Durante cuarenta años hemos dado por sentada una cosa: escribes código, y ese código hace exactamente lo que has escrito. Siempre. Sobre esta certeza hemos construido todo: cómo probamos, cómo depuramos, cómo trabajamos en equipo. La IA generativa rompe este pacto silencioso. No porque sea defectuosa, sino porque tiene una naturaleza probabilística. Le pides lo mismo dos veces y te da respuestas diferentes. A veces geniales, a veces equivocadas con una seguridad pasmosa".

La metáfora que utiliza es impactante: "Las empresas que piensan en sustituir a los programadores por la IA y miran con aire de suficiencia cuántas líneas de código más consiguen producir, están perdiendo de vista lo esencial: están introduciendo una variable aleatoria en el corazón de sus sistemas. Es un poco como si un ingeniero civil construyera un puente con materiales que *podrían* soportar el peso previsto. Funciona de maravilla cuando pasan pocos coches, pero cuando pasa el primer camión, se derrumba".

Escribió el libro, dice, "porque me parecía que faltaba una guía para quienes deben navegar este cambio sin estrellarse, pero también sin renunciar a los beneficios, que son reales".
Del determinismo a la tolerancia

El corazón conceptual del libro está en el título en inglés: *Non-Deterministic Software Engineering*. Es un oxímoron deliberado. La ingeniería de software siempre ha sido el arte de construir sistemas deterministas: la entrada A siempre produce la salida B. Papalini propone acoger en nuestros flujos de trabajo herramientas que, por su naturaleza, no respetan esta regla.

Le pregunto cómo cambia el paradigma del control de calidad cuando pasamos de un mundo donde el código hacía exactamente lo que estaba escrito, a un mundo donde acogemos sistemas probabilísticos en nuestros IDE.

"Cambia todo y, al mismo tiempo, nada. Sé que parece una paradoja", comienza. "Cambia todo porque 'funciona' ya no significa 'es correcto'. El código generado por la IA compila, pasa las pruebas que has escrito, tiene un aspecto profesional. Pero podría ocultar vulnerabilidades, gestionar mal los casos límite o estar escrito de una manera que dentro de seis meses nadie entenderá. No cambia nada porque los fundamentos de la ingeniería de software siguen siendo los mismos: pruebas, revisiones, pensamiento de diseño. De hecho, se vuelven más importantes que antes".

La clave, según Papalini, está en adoptar un enfoque que hasta ahora ha sido ajeno a los desarrolladores: "La verdadera novedad es que debemos aprender a razonar en términos de 'tolerancias'. Martin Fowler usa a menudo esta analogía: su esposa es ingeniera estructural y nunca diseña al límite exacto. Siempre calcula un margen de seguridad. Nosotros, los desarrolladores, nunca hemos tenido que hacerlo porque nuestros 'materiales' eran perfectamente predecibles. Ahora ya no lo son. Y quien no se construya estos márgenes, tarde o temprano verá derrumbarse el 'puente'".
La ilusión de la velocidad

Uno de los pasajes más desconcertantes del libro se refiere a los datos sobre la productividad. Papalini cita un estudio del METR que muestra cómo los desarrolladores pueden sentirse un 20% más rápidos con la inteligencia artificial, mientras que las pruebas reales en tareas medibles indican que en algunos casos son un 19% más lentos.

Le pregunto cómo es posible esta discrepancia y, sobre todo, cómo podemos medir realmente si estamos trabajando mejor o si solo nos sentimos más productivos.

"¿Sabes qué fue lo que más me impactó de ese estudio? No es el dato de que con la IA fueran un 19% más lentos. Es que los desarrolladores *creían* que eran más rápidos. Y seguían creyéndolo incluso después de ver los resultados", cuenta Papalini. "¿Por qué sucede esto? Porque la IA reduce el esfuerzo percibido. Te sientes más fluido, menos bloqueado. Es como tener un colega siempre disponible para echarte una mano, que no te juzga y no te hace esperar. Psicológicamente es potente. Pero 'me siento productivo' y 'estoy produciendo valor' son dos cosas muy diferentes".

La solución que propone también se aplica a nivel individual: "Para no caer en el bombo publicitario, una empresa debería establecer una línea de base antes de adoptar las herramientas. Sin un 'antes', nunca podrán demostrar un 'después'. Cuando el CEO pregunte qué ha aportado la IA, se necesitan cifras, no sensaciones. Pero las cifras deben ser las correctas: dejen de medir líneas de código o cuántas sugerencias de la IA se aceptan. Midan lo que importa: funcionalidades lanzadas, errores en producción, tiempo para resolver incidentes. Y algo fundamental: medir cuán motivados permanecen los desarrolladores".
La trampa del "funciona"

Andrej Karpathy popularizó el término "vibe coding": programar siguiendo la intuición del momento, dejando que la IA sugiera direcciones que "parecen correctas". Es fascinante y profundamente peligroso.

Papalini dedica varias páginas a lo que llama la "Trampa del Funciona". Le pregunto cuáles son los riesgos a largo plazo de una base de código escrita principalmente siguiendo la corriente, sin una validación rigurosa.

"Te cuento una historia", comienza. "Martin Fowler había usado la IA para generar una visualización en formato vectorial SVG, nada complejo. Funcionaba perfectamente. Luego quiso hacer un cambio trivial: mover una etiqueta unos pocos píxeles. Abrió el archivo y encontró lo que definió como 'una locura', código que funcionaba, sí, pero estructurado de una manera completamente ajena, imposible de tocar sin romperlo todo. ¿La única opción? Tirarlo y regenerarlo desde cero".

La anécdota captura perfectamente el problema: "Este es el coste real y el riesgo del 'vibe coding' a escala empresarial. Creas sistemas que funcionan pero que nadie entiende. Y el software empresarial debe vivir años, a veces décadas. Debe ser modificado, ampliado, depurado a las tres de la mañana cuando algo explota".

La solución que propone es simple en su formulación pero requiere disciplina: "La regla que debemos seguir es sencilla: nunca envíes código que no sepas explicar a un colega. Si está generado con IA y no entiendo cómo funciona, no está listo para producción".
El precio de la falta de fiabilidad

En el libro, Papalini introduce el concepto de "impuesto a la falta de fiabilidad" (*unreliability tax*). Le pido que cuantifique, desde el punto de vista de quien escribe y revisa código todos los días, cuánto cuesta realmente el código generado por la IA que parece correcto pero oculta vulnerabilidades.

"Las cifras dan que pensar", comienza. "Las investigaciones muestran que un porcentaje significativo del código generado por la IA contiene vulnerabilidades, algunas fuentes hablan de casi la mitad. Y lo sutil es que son vulnerabilidades 'plausibles': el código parece profesional, usa patrones reconocibles. Solo que falta la validación de la entrada en ese punto crítico, o usa una función criptográfica obsoleta".

No se trata de errores evidentes: "El coste directo es el tiempo de remediación. Pero el verdadero coste es el que no ves de inmediato: la vulnerabilidad que pasa desapercibida durante meses, hasta que alguien la encuentra. En ese momento no estás pagando horas de desarrollo, estás pagando respuesta a incidentes, posibles filtraciones de datos, daños a la reputación".

Papalini también identifica un coste más personal: "También hay un impuesto más sutil: la pérdida de confianza en el sistema. Cuando el equipo empieza a no fiarse de su propio código, todo se ralentiza. Cada modificación se convierte en un riesgo. Y lo mismo ocurre con los clientes: existe el riesgo de que se pasen a un competidor más fiable".

Su recomendación es práctica: "La inversión sensata está en la prevención: escaneo de seguridad automático, formación específica, revisión humana obligatoria para todo lo que toque autenticación o datos sensibles. Cuesta menos que limpiar los desastres después y perder clientela".
El aprendizaje en la era de las máquinas

Una de las secciones más provocadoras del libro se refiere al futuro de la formación. Existe una distinción emergente entre los programadores tradicionales y la nueva figura del Ingeniero de IA, alguien que sabe orquestar sistemas inteligentes pero que podría no haber implementado nunca un algoritmo de ordenación desde cero.

Le pregunto si el programador "puro" está destinado a desaparecer o si la IA simplemente está subiendo el listón de las competencias necesarias.

"El programador no está destinado a desaparecer, pero su papel está cambiando bastante", responde. "Piensa en lo que ocurrió cuando llegaron los lenguajes de alto nivel. Los programadores de ensamblador no desaparecieron, se convirtieron en especialistas de nicho. La mayor parte del trabajo se desplazó un peldaño más arriba".

La transición actual sigue un patrón similar: "Algo parecido está sucediendo ahora. Está surgiendo una figura diferente, llamémosla 'orquestador': alguien que sabe descomponer problemas complejos, especificar requisitos con precisión, evaluar críticamente lo que produce la IA, tomar decisiones de arquitectura".

Pero aquí llega la paradoja: "¿La paradoja? Se necesita más experiencia, no menos. Un desarrollador junior puede usar la IA para generar código que parece funcionar. Pero solo un senior reconoce cuándo ese código es una bomba de relojería, porque ha visto suficientes desastres como para reconocer las señales".

El riesgo sistémico que identifica afecta a la carrera de todo desarrollador: "Hay que tener cuidado de no pensar que todos nacen orquestadores: si delegamos todo el trabajo 'de base' a la IA, ¿cómo formamos a la próxima generación de seniors? Los datos nos dicen que el empleo de los desarrolladores más jóvenes ya está disminuyendo. Pero incluso quienes entran en el mercado corren el riesgo de no desarrollar nunca esas competencias profundas que solo se construyen a base de darse cabezazos con los problemas".
El "trio programming"

Para resolver este dilema, Papalini propone en el libro un modelo que llama "trio programming", una evolución del *pair programming* que incluye a la IA como tercer actor. Es una solución práctica para quienes trabajan a diario con estas herramientas.

"En el libro propongo el 'trio programming' como solución al problema de la formación", explica. "El junior trabaja con la IA para implementar las funcionalidades. La IA acelera, sugiere, genera código. Hasta aquí, nada nuevo. El senior orquestador no escribe código, está ahí para hacer preguntas. 'Explícame qué hace este método'. '¿Por qué la IA ha elegido esta estructura de datos?'. '¿Qué sucede si la entrada es nula?'. '¿Cómo gestionarías un error de red aquí?'".

El mecanismo es pedagógicamente brillante: "Respondiendo a estas preguntas, el joven aprende. El senior, por su parte, transfiere ese saber tácito que no está en ningún manual: la intuición sobre lo que puede salir mal, la sensibilidad para el código que 'huele mal', la experiencia de quien ha visto sistemas colapsar".

Es un modelo aplicable también para quien trabaja solo: sustituye al "senior" por una lista de control mental de preguntas que hacerte antes de cada *commit*. ¿La IA te ha generado esa función? Perfecto. Ahora explícatela a ti mismo. Si no puedes, no está lista.
Orquestadores, no mecanógrafos

La conversación vuelve al tema del cambio profesional. Si la IA es cada vez mejor escribiendo código, ¿cuál es el valor distintivo del ingeniero humano? ¿Qué debemos aprender, qué debemos preservar?

"El papel del ingeniero se desplaza hacia la especificación y la validación, menos hacia la implementación", sintetiza Papalini. "Pero este cambio requerirá más competencia por parte de los trabajadores, no menos".

Es un punto crucial que contradice la narrativa popular de la IA como democratización de la programación. No estamos bajando las barreras de entrada, las estamos desplazando. Antes tenías que saber escribir código sintácticamente correcto. Ahora tienes que saber reconocer cuándo el código sintácticamente correcto es semánticamente peligroso.

Las competencias que importan están cambiando: menos sintaxis, más arquitectura. Menos implementación, más diseño. Menos "cómo se escribe un bucle", más "por qué este enfoque es problemático a escala". Es como pasar de albañil a ingeniero estructural: el martillo importa menos, la física importa más.
La atrofia de las competencias

Hay un tema que atraviesa todo el libro: el riesgo de que la adopción masiva de la IA no amplifique nuestras capacidades, sino que las atrofie. Es la pregunta que todo desarrollador debería hacerse.

Le pregunto directamente: ¿cómo podemos garantizar que el uso diario de la IA no devalúe nuestra profesionalidad, sino que se convierta en un verdadero amplificador de nuestras capacidades?

"Es la pregunta que más me importa", responde Papalini. "El riesgo concreto lo llamo 'atrofia de las competencias'. Un ingeniero entrevistado por MIT Technology Review contó que después de meses de uso intensivo de la IA, cuando intentó programar sin ella, se sentía perdido; cosas que antes eran instintivas se habían vuelto fatigosas. Es exactamente la señal de alarma que deberíamos escuchar".

La solución no es el rechazo, sino la intencionalidad: "La solución no es rechazar la IA, sería como rechazar la electricidad. Pero debemos ser intencionales en cómo la integramos, especialmente en los itinerarios de formación. Por eso en el libro propongo modelos como el 'trio programming' para cultivar la capacidad de los talentos y no cometer el error de serrar el peldaño más bajo de la escalera por la que hemos subido, el proceso de aprendizaje que nos ha llevado a donde estamos".

Es un desafío personal para cada desarrollador: cómo usas la IA dice mucho sobre qué tipo de profesional te convertirás. Puedes usarla como una muleta que te permite evitar entender lo que estás haciendo, o como un amplificador que te libera de las partes aburridas para concentrarte en las que requieren juicio. El primer camino lleva a la obsolescencia. El segundo, al crecimiento.
El oficio que cambia

Al final de esta conversación, lo que emerge con claridad es que estamos viviendo uno de esos momentos de transición que redefinen una profesión. El libro *Intelligenza Artificiale e Ingegneria del Software* no es un manual sobre cómo usar Copilot más rápido. Es más parecido a esos textos que surgen después de una revolución tecnológica, cuando alguien que la ha vivido en primera línea intenta mapear qué ha cambiado de verdad y qué solo en apariencia.

La verdadera cuestión no es si usaremos la IA para escribir código. Ya la estamos usando. La cuestión es si lograremos hacerlo sin perder por el camino las competencias profundas que nos permitieron convertirnos en desarrolladores capaces. Esas competencias que se construyen solo depurando durante horas un *segfault*, solo leyendo código horrible escrito por otros, solo equivocándose de formas creativas y aprendiendo de los desastres.

La IA puede generar código en segundos. Pero no puede generar la experiencia que te hace reconocer cuándo ese código esconde un problema. Todavía no. Y quizás nunca. Es ese espacio, entre la generación y el juicio, el que define el valor de un desarrollador en la era de la inteligencia artificial. La pregunta es: ¿estás cultivando ese juicio o lo estás delegando?
