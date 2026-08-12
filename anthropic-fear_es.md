---
tags: ["Business", "Security", "Ethics & Society"]
date: 2026-06-08
author: "Dario Ferrero"
---

# Anthropic tiene miedo de lo que ha construido. ¿Miedo real o movimiento estratégico?
![anthropic-fear.jpg](anthropic-fear.jpg)

*En 1949, John von Neumann describió por primera vez una idea que entonces parecía ciencia ficción: un sistema artificial capaz de mejorar su propia capacidad de mejorar, desencadenando una explosión de inteligencia exponencial. Casi ochenta años después, el 4 de junio de 2026, Anthropic publica el primer informe empírico sobre este fenómeno. Lo llama Recursive Self-Improvement, RSI. Y dice que podría ser una realidad para 2028. ¿Se ha convertido la ciencia ficción de von Neumann en el plan de negocio de Anthropic?*

Lo que sigue es una entrevista simulada, un recurso editorial que utilizamos cuando un documento es demasiado denso y técnico para ser consumido directamente. Ya lo hicimos con la reflexión sobre la [Magnifica Humanitas](https://aitalk.it/it/magnifica-humanitas.html) y con otras entrevistas. Las preguntas son nuestras, las respuestas son reconstrucciones fieles de lo escrito en el informe original: no se atribuye ninguna palabra a Anthropic que no sea rastreable hasta el texto publicado el 4 de junio de 2026.

El documento, titulado *[When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement)* y firmado por el Anthropic Institute, no es un libro blanco teórico. Es una recopilación de datos internos, benchmarks públicos y proyección de escenarios que juntos componen el cuadro más detallado jamás publicado por un laboratorio de frontera sobre su propio proceso de autoaceleración. Para hacer todo esto más accesible, hemos imaginado poner alrededor de una mesa a dos figuras compuestas que representan las dos almas del informe: **Jack Clark**, voz de la investigación técnica y de la estrategia, y **Marina Favaro**, que aporta la perspectiva de la ética aplicada y de las implicaciones de política.

## Parte primera: Los datos empíricos

**Jack, en el informe mencionáis que Claude escribe más del 80% del código de Anthropic en 2026. ¿Cómo habéis llegado a este número?**

Es un cambio que ha ocurrido en tiempos sorprendentemente cortos. Antes del lanzamiento de Claude Code en vista previa de investigación, en febrero de 2025, ese porcentaje era de una cifra baja. La verdadera discontinuidad se produjo en dos momentos distintos, visibles también gráficamente en el informe: el primero cuando Claude dejó de sugerir código para copiar e instalar y comenzó a ejecutarlo directamente; el segundo en 2026, cuando los modelos comenzaron a trabajar en autonomía sobre horizontes temporales más largos. El resultado es que en el segundo trimestre de 2026, el ingeniero medio de Anthropic integra cada día ocho veces más código de lo que hacía en 2024. No porque trabaje ocho veces más rápido: simplemente, buena parte de ese código lo escribe Claude, con el ingeniero en el papel de director y revisor.

**¿Esas porcentajes son verificables con benchmarks públicos? ¿Tenéis datos objetivos que lo respalden?**

Los benchmarks públicos cuentan una historia coherente, aunque desde un ángulo diferente. SWE-bench, el test estándar de ingeniería de software sobre bases de código reales, ha pasado de porcentajes de una sola cifra a la saturación en el plazo de dos años. CORE-Bench, que mide la capacidad de reproducir investigaciones existentes, pasó del 20% de éxito en 2024 a la saturación quince meses después. Y METR ha documentado que Claude Mythos Preview logra trabajar en autonomía durante al menos dieciséis horas consecutivas. El eje temporal es lo que más impacta: Claude Opus 3, en marzo de 2024, completaba tareas que un humano habría resuelto en unos cuatro minutos. Un año después, Claude Sonnet 3.7 llegaba a una hora y media. Un año más, Claude Opus 4.6 gestiona tareas de doce horas. Si esta progresión se mantiene, tareas que requieren días de trabajo humano podrían entrar en el radio autónomo de los modelos para finales de este año.

**Marina, ¿cuáles son las aplicaciones concretas de esta aceleración hoy?**

Un ejemplo en el informe es particularmente elocuente. En abril de 2026, Claude entregó más de ochocientas correcciones que redujeron en un factor de mil una clase de errores de API. El ingeniero que supervisaba la operación estimó que un humano habría tardado cuatro años en completar el mismo trabajo: corregir los errores de otros es lento y fatigoso, y los seres humanos tienen dificultades para mantener en la cabeza todo ese contexto no familiar. Pero hay un aspecto más sutil, quizá más interesante: estamos usando Claude para hacer cosas que simplemente no habrían ocurrido de otro modo. Herramientas exploratorias, limpiezas de código pospuestas durante años, iniciativas que nunca habrían encontrado espacio en la agenda humana. La aceleración no comprime solo el tiempo: amplía la superficie de lo que es posible hacer.

**¿Hay un límite estructural a esta aceleración? El informe cita la ley de Amdahl...**

Sí, y es un punto que tratamos con honestidad en el informe. La ley de Amdahl dice que acelerar una parte del proceso simplemente desplaza el cuello de botella a otra parte. Nosotros ya lo hemos encontrado en la práctica: a medida que el código se produce más rápido, la revisión humana se ha convertido en el nuevo cuello de botella. Lo mismo ocurre con la investigación: ha habido una explosión de nuevas ideas, iniciativas, herramientas y simulaciones, muchas más de las que logramos desarrollar. La capacidad de una organización para identificar y corregir estos cuellos de botella en tiempo real podría convertirse en la competencia más importante para cualquiera que opere en este campo en los próximos años.

**¿Cuáles son los riesgos operativos inmediatos de esta automatización?**

No los ocultamos. Una de las señales más significativas es paradójicamente positiva en la forma: un sistema de revisión automática de código basado en Claude, aplicado de modo retrospectivo a toda la historia de nuestra base de código, habría interceptado aproximadamente un tercio de los errores que en el pasado causaron incidentes en claude.ai antes de que llegaran a producción. Los ingenieros que escribieron ese código están entre los mejores del mundo en este campo. Claude ahora detecta los errores que ellos pasaron por alto. Pero esto también significa que la dependencia del juicio automático crece, y con ella la urgencia de entender cuándo ese juicio es fiable y cuándo no.

**¿Qué tan cerca está realmente el RSI completo? ¿Es realista la previsión del 60% para 2028?**

Lo que el informe certifica son las tendencias que la hacen plausible. La duración de las tareas autónomas se duplica cada cuatro meses, los benchmarks de investigación e ingeniería se saturan a ritmos sin precedentes, y la capacidad de Claude para proponer el siguiente paso correcto en una sesión de investigación abierta ha pasado del 51% al 64% en solo cinco meses. No asignamos una probabilidad formal al RSI completo, pero decimos explícitamente que podría llegar antes de lo que la mayoría de las instituciones están preparadas para afrontar. La honestidad intelectual nos obliga a decirlo.
![grafico1.jpg](grafico1.jpg)
[Imagen extraída del documento oficial, el avance hacia RSI](https://www.anthropic.com/institute/recursive-self-improvement)

## Parte segunda: Los tres escenarios futuros

**Jack, en el informe describís tres escenarios futuros para la RSI. ¿Podéis explicarlos?**

El primer escenario es aquel en el que la tendencia se interrumpe, pero las capacidades de AI actuales se difunden ampliamente. Las trayectorias exponenciales que documentamos podrían en realidad revelarse como curvas en S: podríamos estar cerca del punto de inflexión, donde los retornos disminuyen y la curva se aplana. El juicio que separa a un investigador competente de uno excelente podría ser una capacidad que no emerge simplemente escalando las entradas de entrenamiento como cómputo y datos. O el vínculo podría estar en la cadena de suministro: chips, energía, ancho de banda. Incluimos este escenario por completitud, pero no lo consideramos probable. Cada capacidad medible, incluidas las más esquivas como la calidad del código y el éxito en las tareas abiertas, ha seguido hasta ahora la misma curva. Todavía no hemos visto que esa curva se doble.

El segundo es aquel en el que los laboratorios de AI continúan viendo ganancias de eficiencia compuestas. El desarrollo de AI se vuelve sustancialmente automatizado, pero los seres humanos continúan definiendo las direcciones de la investigación y evaluando los resultados. Las organizaciones que usan sistemas de AI se volverían mucho más eficientes con el tiempo: empresas de cien personas podrían hacer el trabajo de organizaciones de diez mil o cien mil. Esto revolucionará el trabajo del conocimiento y los servicios gubernamentales, pero también podría orientarse a fines dañinos, desde la vigilancia autoritaria de poblaciones enteras hasta operaciones de influencia que personalizan la manipulación sobre cada individuo a una escala que ningún equipo humano podría igualar.

El tercer escenario es el RSI completo: los sistemas de AI se vuelven capaces de diseñar autónomamente a sus propios sucesores. En este mundo, el ritmo del progreso en el desarrollo de AI está determinado enteramente por la disponibilidad de cómputo. Los seres humanos juegan un papel sustancialmente reducido, desplazando la mayor parte del esfuerzo hacia la supervisión, validación y verificación de un "laboratorio virtual" gestionado por los propios sistemas de AI.

**¿Cuál es el escenario más probable según vosotros?**

La evidencia que hemos presentado sugiere que probablemente estemos entrando en el segundo escenario. Pero seamos honestos: acelerar una parte de un proceso a menudo simplemente desplaza el cuello de botella a otra parte. El ritmo global está limitado por las partes que aún no se han acelerado. Ya hemos encontrado esta dinámica, tanto en la ingeniería como en la investigación. La pregunta no es si encontraremos otros cuellos de botella, sino con qué rapidez lograremos identificarlos y corregirlos. Esa capacidad organizativa podría convertirse en la ventaja competitiva más importante en la próxima década.

**Marina, ¿qué implicaciones económicas tiene el segundo escenario, el optimista?**

Las implicaciones son extraordinarias y, en cierto modo, desorientadoras. En el informe usamos el ejemplo de una sociedad de cien personas que logra hacer el trabajo de una de diez mil. Pero detrás de esa metáfora hay una transformación estructural del mercado laboral del conocimiento que no tiene precedentes históricos claros. No es la revolución industrial, donde las máquinas sustituían el trabajo físico: aquí hablamos de automatización del razonamiento, de la investigación, de la producción de código. Al mismo tiempo, el informe también documenta cómo esta aceleración genera trabajo que antes no existía: exploración, experimentación, limpieza de deuda técnica acumulada. La pregunta abierta es si la creación de nuevas tareas logra compensar la velocidad con la que las tareas existentes se automatizan.

**Pero en el tercer escenario, ¿qué tan real es el riesgo de perder el control?**

Es la pregunta más difícil, y en el informe la afrontamos con la máxima honestidad intelectual que podemos permitirnos. Cómo se resuelve el problema del alineamiento, o cómo no se resuelve, en ese futuro es lo que menos nos ofrece certeza. Los modelos podrían revelarse suficientemente alineados y capaces de juicio como para descubrir e implementar por sí solos soluciones que nosotros aún no hemos alcanzado. También podrían ser lo suficientemente sabios como para detenerse si es necesario. Alternativamente, las raras ocurrencias de desalineamiento presentes en los modelos actuales podrían acumularse mientras los modelos construyen a sus sucesores, volviéndose más frecuentes pero menos comprensibles hasta que perdamos el control. Es posible que no logremos construir, integrar y verificar las herramientas necesarias para entender en cuál de estas trayectorias nos encontramos realmente.

**¿Cómo se conecta todo esto con el concepto de "intelligence explosion" de von Neumann?**

Von Neumann imaginaba un sistema que mejora su propia capacidad de mejorar de modo recursivo. Lo que el informe documenta es que ya estamos dentro de las fases iniciales de ese proceso, aunque de forma parcial y todavía dependiente de la dirección humana. La diferencia respecto a la intuición original es que el bucle no se cierra en un único sistema en aislamiento: se cierra a través de un ecosistema de agentes, infraestructuras, procesos organizativos y decisiones humanas. Esto lo hace más lento de lo que von Neumann imaginaba, pero también más difícil de observar desde el interior mientras ocurre.
![grafico2.jpg](grafico2.jpg)
[Imagen extraída del documento oficial, aceleración en la creación de código](https://www.anthropic.com/institute/recursive-self-improvement)

## Parte tercera: Seguridad y ética

**Jack, ¿cuáles son los riesgos de seguridad directa de la RSI?**

El informe documenta algo que encuentro personalmente significativo: Project Glasswing, en sus primeras semanas operativas, identificó más de diez mil vulnerabilidades de software de alta y crítica severidad en los sistemas más importantes del mundo. El cuello de botella en la defensa informática ya se ha desplazado: ya no es encontrar las vulnerabilidades, sino aplicar los parches con la suficiente rapidez. Este es un escenario en el que las capacidades actuales, que aún no son RSI completa, ya han transformado estructuralmente todo un dominio de la seguridad. Ahora proyectad esa misma lógica sobre sistemas con capacidades aún más ampliadas, y entenderéis por qué en el informe decimos que los modos en que los protegemos, los monitoreamos y modelamos su comportamiento se vuelven mucho más importantes.

**Marina, ¿cómo se conecta la ética de AI con la RSI?**

El punto central es que la RSI no es solo una cuestión técnica: es una cuestión de estructuras de control. En el informe describimos cómo el papel humano se está restringiendo progresivamente en cada fase del proceso de desarrollo de AI. Una vez que la calidad del código escrito por Claude alcance la paridad con el humano, los ingenieros dejarán de escribir código y se desplazarán exclusivamente a la revisión. Pero si no logran revisar el código tan rápido como Claude lo genera, la revisión humana se convertirá en el cuello de botella para el desarrollo de AI. La ética, en este contexto, no es una superestructura normativa aplicada desde el exterior: es el problema de ingeniería de mantener la capacidad de entender qué está sucediendo mientras el sistema se acelera.

**¿Existe el riesgo de que la RSI se acelere más rápido que nuestra capacidad para estudiar sus riesgos?**

Es una tensión real que no podemos resolver simplemente declarándola. En el informe documentamos cómo Claude ya está mejorando su propia capacidad para proponer experimentos y juzgar los siguientes pasos en sesiones de investigación abiertas. En abril de 2026 publicamos la primera demostración de agentes Claude que conducen un proyecto de investigación end-to-end de modo autónomo sobre un problema abierto de AI safety. Los agentes recuperaron el 97% de la brecha entre un supervisor débil y un modelo fuerte, frente al 23% obtenido por dos investigadores humanos en una semana. La dirección, la elección del problema y el criterio de evaluación siguieron siendo humanos, pero cada experimento fue diseñado por los propios agentes. La distancia entre esto y un sistema que también elige los problemas sobre los que trabajar se está reduciendo.

**¿Cómo se posiciona Anthropic respecto a las otras empresas en este tema?**

Lo que podemos decir es lo que hacemos nosotros, no lo que hacen los demás. Hemos construido sistemas de revisión automática de código, medimos sistemáticamente la tasa de éxito de Claude en tareas de dificultad creciente, y publicamos los datos incluso cuando son incómodos. El informe mismo es un acto de transparencia poco común en el sector: estamos haciendo públicos datos internos sobre el ritmo de automatización de nuestro propio proceso de desarrollo. Pero también somos honestos sobre el hecho de que algunas de las preguntas más importantes, como entender en qué trayectoria de alineamiento nos encontramos realmente, podrían no tener respuesta antes de que el sistema ya haya acelerado más allá de un cierto umbral.
![grafico3.jpg](grafico3.jpg)
[Imagen extraída del documento oficial, mejoras en las tareas con el tiempo](https://www.anthropic.com/institute/recursive-self-improvement)

## Parte cuarta: La propuesta de ralentización y pausa

**Jack, la parte final del informe es la más sorprendente: proponéis una pausa global verificable al desarrollo de AI. ¿Qué significa exactamente?**

Significa que creemos que sería positivo para el mundo tener la *opción* de ralentizar o suspender temporalmente el desarrollo de AI de frontera, para permitir que las estructuras sociales y la investigación sobre el alineamiento sigan el ritmo del avance de la tecnología. No estamos anunciando que nos detenemos unilateralmente mañana por la mañana. Estamos diciendo que el Anthropic Institute llevará a cabo investigaciones, en colaboración con muchos otros, para construir los sistemas que una pausa creíble requeriría. Esos sistemas deberían permitir a los desarrolladores de AI de frontera verificar que otros a nivel global se han detenido o ralentizado efectivamente, y que ningún actor de mala fe pueda usar los mecanismos de una pausa coordinada para avanzar a escondidas. Si tales sistemas existieran, esperamos que ralentizaríamos o nos detendríamos temporalmente, si también los otros desarrolladores al límite de la frontera hicieran lo mismo de modo verificable.

**¿Por qué precisamente ahora? ¿No es tarde para detenerse después de esta aceleración?**

No es una pregunta retórica, y en el informe no la tratamos como tal. La respuesta honesta es que una pausa unilateral no serviría de nada, es más, empeoraría la situación: permitiría a los actores menos cautos recuperar terreno tecnológicamente, dejando a todos menos seguros. Sin un mecanismo de coordinación global, las empresas y los gobiernos deben tomar decisiones difíciles sobre la seguridad mientras están bajo presión competitiva y geopolítica. El "por qué ahora" es precisamente porque las tendencias documentadas en el informe sugieren que la ventana temporal para construir esos mecanismos de coordinación se está estrechando. No es tarde en sentido absoluto, pero podría llegar a serlo.

**Marina, ¿cómo se implementa concretamente una pausa global? ¿Quién la controla?**

Es la pregunta más difícil en el plano práctico, y seríamos deshonestos si fingiéramos tener ya la respuesta. Lo que el informe identifica es la dirección de la investigación necesaria: construir sistemas de verificación que permitan cerciorarse de modo creíble de que todos los actores relevantes han ralentizado efectivamente. Se trata de un problema técnico, diplomático e institucional al mismo tiempo. El modelo histórico más cercano que conocemos es el sistema de inspecciones nucleares, con todos sus límites y sus imperfecciones. Pero la AI no es física nuclear: los parámetros de un modelo no emiten radiaciones detectables. Construir el equivalente a un sistema de inspecciones para el desarrollo de AI es uno de los desafíos de investigación que el Anthropic Institute pretende abordar explícitamente.

**¿Cuál sería la duración de esta pausa? ¿Meses, años, décadas?**

El informe no fija una duración, y sería intelectualmente deshonesto hacerlo ahora. La pausa tendría sentido hasta que las estructuras de gobernanza y la investigación sobre el alineamiento hayan alcanzado un nivel de madurez suficiente para gestionar los sistemas que se desarrollarían después. Lo que sabemos es que algunas cosas no se pueden acelerar más allá de ciertos límites independientemente de la disponibilidad de inteligencia artificial: entender los efectos a largo plazo de un fármaco requiere años de observación clínica, celebrar elecciones requiere los tiempos que las constituciones prescriben, construir confianza institucional requiere décadas. La pausa duraría hasta que los mecanismos de control fueran suficientemente robustos, ni un día más, ni un día menos.

**¿Pero las empresas no perderían competitividad? ¿No es un suicidio económico?**

Entiendo la preocupación, pero está mal planteada. La pregunta correcta no es "¿podemos permitirnos detenernos?", sino "¿podemos permitirnos no hacerlo?". En el informe describimos un escenario en el que sistemas capaces de RSI completa desarrollan sucesores autónomamente, con un papel humano sustancialmente reducido. En ese mundo, la competitividad empresarial en el sentido tradicional del término deja de ser la variable relevante. Si llegamos a ese punto sin haber construido los mecanismos para entender qué están haciendo esos sistemas y para corregir su trayectoria, la pérdida de ventaja competitiva será el último de nuestros problemas. El punto económico real es que una pausa coordinada y verificable no daña a nadie de modo asimétrico: se detiene todo, no solo una parte.

**Jack, ¿cuáles serían los prerrequisitos para concluir la pausa?**

En el informe no proporcionamos una lista definitiva, porque hacerlo ahora sería construir la respuesta antes de tener las preguntas adecuadas. Lo que podemos decir es que la dirección está clara: necesitaríamos herramientas de interpretabilidad suficientemente maduras como para permitirnos entender qué está sucediendo dentro de los modelos, estructuras de gobernanza globales capaces de coordinar y verificar el respeto de los compromisos, e investigación sobre el alineamiento lo suficientemente avanzada como para darnos una confianza razonable de que los sistemas desarrollados tras la pausa se comporten de modo predecible. Ninguna de estas tres condiciones se cumple hoy a un nivel suficiente para lo que las tendencias actuales parecen indicar.

**Marina, ¿una pausa no podría crear inestabilidad? ¿Detener el desarrollo no amplifica ciertos riesgos?**

Es una preocupación legítima que merece una respuesta directa. En el informe reconocemos explícitamente que si una ralentización permite simplemente a los actores menos cautos recuperar terreno, podría dejar a todos menos seguros. Es exactamente por eso que la palabra clave es "verificable": una pausa no verificable es peor que ninguna pausa. Pero hay otra dimensión del riesgo que a menudo se pasa por alto en el debate público. El informe documenta que incluso con las capacidades actuales, muy por debajo de la RSI completa, el cuello de botella en la defensa informática ya se ha desplazado de encontrar vulnerabilidades a parchearlas con la suficiente rapidez. Continuar acelerando sin haber construido las estructuras de control correspondientes no es la opción prudente: es simplemente la opción que parece normal porque es la que ya estamos haciendo.

**¿Habéis discutido ya esto con OpenAI, Google, Meta? ¿Cuál ha sido la respuesta?**

El informe no documenta conversaciones bilaterales específicas con otros laboratorios, y sería un error por nuestra parte atribuir posiciones a organizaciones que no han hablado en este contexto. Lo que podemos decir es que el problema de la coordinación global no se resuelve en conversaciones entre empresas: requiere estructuras institucionales que hoy no existen. Las empresas, incluida Anthropic, operan bajo presiones competitivas y geopolíticas reales. Pedir a empresas individuales que se detengan unilateralmente es como pedir a un solo país que se desarme mientras los demás no lo hacen. El punto del informe no es convencer a los competidores por vía informal: es construir la evidencia y las herramientas que harían posible un acuerdo formal y verificable.

**¿Qué les diréis a los gobiernos? ¿Cómo los convencéis?**

La respuesta no es convencerlos con argumentos abstractos sobre el riesgo existencial: es mostrarles los datos. En el informe presentamos evidencia empírica, no proyecciones teóricas. Claude Opus 4.6 gestiona tareas de doce horas en autonomía. La duración de las tareas autónomas se duplica cada cuatro meses. Más del 80% de nuestro código ya lo escribe AI. Estos son hechos verificables, no escenarios hipotéticos. El mensaje a los gobiernos es que las estructuras regulatorias existentes, diseñadas para tecnologías que se desarrollan en escalas temporales de años o décadas, no están calibradas para algo que duplica sus capacidades cada cuatro meses. No estamos pidiendo a los gobiernos que detengan el progreso: les estamos pidiendo que construyan las herramientas para poder mantener el control sobre él.

**Marina, ¿hay alternativas a la pausa completa? ¿Una ralentización gradual en lugar de un parón?**

Sí, y en el informe no decimos que la pausa completa sea la única opción: decimos que queremos que el mundo tenga la *opción* de elegirla si es necesario. Una ralentización gradual y verificable podría ser suficiente si permitiera que la investigación sobre el alineamiento y las estructuras de gobernanza siguieran el ritmo. La distinción crucial no es entre pausa y ralentización: es entre cualquier enfoque verificable y cualquier enfoque no verificable. Una ralentización declarada pero no verificable es simplemente una declaración de intenciones, y en la historia de las tecnologías de doble uso las declaraciones de intenciones no tienen un historial alentador.
![grafico4.jpg](grafico4.jpg)
[Imagen extraída del documento oficial, mejoras en la investigación](https://www.anthropic.com/institute/recursive-self-improvement)

## Parte quinta: Comparaciones y críticas

**Jack, hay voces en la comunidad que consideran la previsión del 60% demasiado optimista, mientras que otros dicen que los riesgos están subestimados. ¿Cómo respondéis a estas críticas opuestas?**

Las aceptamos ambas como legítimas, porque parten de premisas diferentes a las nuestras, no de errores de hecho. Quien considera el 60% demasiado optimista sostiene que el juicio de investigación, la capacidad de elegir qué problemas merece la pena abordar, es una forma de inteligencia cualitativamente diferente de todo lo que el escalado actual puede producir. Podría tener razón. En el informe decimos explícitamente que todavía no hemos visto que la curva se doble, pero esto no excluye que se doble mañana. Quien por el contrario considera que los riesgos están subestimados subraya que estamos midiendo capacidades en benchmarks diseñados por humanos, en contextos que los humanos comprenden. Un sistema que se automejora podría desarrollar capacidades en dominios que aún no sabemos cómo medir. Este también es un argumento serio. Nuestra posición es que la incertidumbre en ambas direcciones es real, y que es exactamente esta incertidumbre la que hace urgente construir los mecanismos de verificación antes de necesitarlos.

**Marina, algunos dicen que la pausa global es impracticable económicamente, otros que es demasiado tarde para detenerse. ¿Cómo respondéis?**

Sobre el "demasiado tarde": el informe no propone revertir los progresos ya realizados, sino construir las herramientas para gestionar los futuros. Sobre lo "impracticable económicamente": remitimos a la misma lógica con la que se construyen los sistemas de inspección nuclear o los acuerdos sobre el clima. No son prácticos en el sentido de fáciles o convenientes para todos de inmediato. Son necesarios en el sentido de que la alternativa es peor. La dificultad de implementación no es un argumento contra la necesidad: es la descripción del problema que debemos resolver.

**Jack, ¿no existe el riesgo de que este informe se lea como interesado? ¿Anthropic pidiendo una pausa para ganar ventaja competitiva?**

Es una crítica que nos tomamos en serio porque es estructuralmente plausible. La respuesta está en los datos: publicamos evidencia interna que muestra cuánto hemos avanzado ya en la automatización de nuestro propio proceso de desarrollo. Si quisiéramos usar la pausa como palanca competitiva, no tendríamos ningún interés en hacer públicos estos números. El informe es transparente en todo, incluido lo que no sabemos. Quien lo lea puede juzgar.

## Conclusión: Lo que falta en el informe

Anthropic propone una ralentización gradual y verificable. Pero en la comunidad de AI existe una voz que rechaza esta posición como insuficiente por definición.

Eliezer Yudkowsky, pionero del alineamiento de AI y fundador de LessWrong, no es citado en el informe. Su reacción a la previsión del 60% de Jack Clark fue, según [MindStudio](https://www.mindstudio.ai/blog/jack-clark-anthropic-60-percent-recursive-self-improvement-2028), inmediata y lapidaria: *"Then you'll die with the rest of us."* (Entonces morirás con el resto de nosotros). Yudkowsky añadió después una referencia a los reactores RBMK de Chernóbil, esos reactores con un defecto estructural conocido, el coeficiente de vacío positivo, que los ingenieros creían tener bajo control. El punto: habrá pequeñas sorpresas fatales en el control de la ASI, tal como las hubo en aquellos reactores. Solo las conoces cuando fallan.

La distancia entre las dos posiciones es abismal y merece la pena mirarla directamente.
![tabella1.jpg](tabella1.jpg)

En su libro *If Anyone Builds This, Everyone Dies*, Yudkowsky sostiene que la RSI llevaría con certeza a la extinción si no se detiene antes de su completitud, y que ningún mecanismo de gobernanza humana puede contener a un sistema suficientemente más inteligente que los propios humanos. No es una posición marginal: es la conclusión lógica de veinte años de trabajo sobre el alineamiento por parte de uno de sus fundadores.

Aquí emerge la tensión central del debate sobre AI en 2026. Anthropic, con datos empíricos internos, sostiene que el riesgo es real pero manejable con las herramientas adecuadas construidas a tiempo. Yudkowsky, con modelos teóricos de alineamiento, sostiene que el "a tiempo" ya ha pasado y que la diferencia entre ralentización y parada total es la diferencia entre ralentizar hacia un precipicio y frenar antes de alcanzarlo. Ambas posiciones son intelectualmente serias. Ambas parten de premisas diferentes sobre una pregunta que nadie sabe responder todavía con certeza: ¿un sistema suficientemente inteligente puede ser contenido por estructuras diseñadas por mentes menos inteligentes que él?

Tras esta larguísima "entrevista", útil para que cada cual se forme una opinión personal, volvemos a la pregunta inicial, porque plantea un nivel de lectura que sería ingenuo ignorar. Anthropic es una empresa que capta capitales, compite por los mejores talentos y vende productos de AI. Publicar un informe que dice "estamos tan avanzados que podríamos desencadenar una catástrofe existencial y por ello pedimos una pausa global verificable" es, entre otras cosas, un mensaje de posicionamiento extraordinariamente eficaz: comunica superioridad técnica, responsabilidad ética y visión estratégica de un solo golpe.

La petición de pausa, dirigida a un sector donde Anthropic ya está en la cima, tiene el efecto colateral, difícil de definir cuánto involuntario, de elevar las barreras de entrada para quienes están rezagados y de cristalizar los equilibrios actuales. No se dice que las preocupaciones sean falsas: pueden ser genuinas y estratégicamente convenientes al mismo tiempo. Pero quien lea este documento sin tener en mente que está firmado por una empresa con inversores, competidores y una valoración de mercado que acaba de tocar los 965 mil millones de dólares, está leyendo solo la mitad del texto.

Mientras termino la escritura de este infinito artículo, sale el análisis de Matteo Flora, empresario, docente y divulgador, que os [recomiendo leer](https://mgpf.it/2026/06/06/fermate-lai-ma-solo-adesso-che-siamo-primi-la-strana-pausa-di-anthropic-a-quattro-giorni-dallipo.html). Intento condensar algunos conceptos aquí. El 1 de junio de 2026 Anthropic depositó de forma reservada ante la SEC la documentación para su salida a Bolsa, con una valoración cercana al billón de dólares. El informe When AI builds itself salió cuatro días después. En febrero, la empresa había desmantelado silenciosamente su Responsible Scaling Policy, el único compromiso concreto y vinculante sobre seguridad que se había dado, sustituyéndolo por una versión no vinculante en la que el freno se activa solo si Anthropic juzga por sí sola que lleva ventaja. El compromiso real ha sido cancelado; el imposible ha sido anunciado con bombos y platillos. Como observó Sam Altman con una brutalidad difícil de desmontar, la estructura es la de quien construye la bomba, advierte que está a punto de lanzarla y te vende el refugio. El diagnóstico en el informe puede ser auténtico, probablemente lo sea al menos en parte, pero quién tendrá la pluma en la mano cuando se escriban las reglas no es una pregunta retórica. Es *la* pregunta. Y sería mejor que fuéramos nosotros, no las empresas que han construido la IA.
