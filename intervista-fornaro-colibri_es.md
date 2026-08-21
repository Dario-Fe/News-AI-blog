---
tags: ["Research", "Generative AI", "Ethics & Society"]
date: 2026-09-30
author: "Dario Ferrero"
---

# Vincenzo Fornaro y Colibrì: "No me interesa el genio, me interesa la curiosidad"
![intervista-fornaro-colibri.jpg](intervista-fornaro-colibri.jpg)

*De Colibrì ya he hablado, contando cómo es posible hacer funcionar un modelo Mixture-of-Experts de 744 mil millones de parámetros en un ordenador con apenas 25 GB de RAM, tratando el disco como un nivel de memoria inteligente en lugar de un simple contenedor ([podéis leer el análisis técnico completo aquí](https://aitalk.it/it/colibri.html)). Lo que faltaba era la voz de quien ha escrito ese motor, archivo C por archivo C, a solas, sin laboratorio y sin un clúster detrás. He charlado con Vincenzo Fornaro para que me contara el camino que hay detrás del código, y la conversación se ha vuelto más larga y estimulante de lo que había previsto.*

## De un almacén en Brescello a una idea perseguida de noche

En internet se encuentra muy poco sobre Vincenzo. Su perfil de [GitHub](https://github.com/JustVugg/colibri) se limita a una línea: "Founder of Colibrì, a tiny engine, immense model", y sin embargo, en tres semanas el proyecto ha superado las veinticinco mil estrellas y se ha situado en el centro del debate sobre la democratización de la inteligencia artificial. Le he preguntado quién es, antes incluso de preguntarle cómo lo hizo.

"Creo que en internet es difícil encontrar información sobre mí porque nunca he sido una persona particularmente expansiva y, sobre todo, nunca he tenido un gran interés en mostrarme a mí mismo. Siempre he preferido poner por delante mis proyectos.

Para mí programar siempre ha sido un desahogo de la fantasía. Durante años, sobre todo de noche, éramos simplemente yo, un ordenador y una idea en la que pensar. No programaba necesariamente porque alguien me lo hubiera pedido o porque tuviera ya en mente un producto que vender. A menudo programaba porque necesitaba entender si una idea que tenía en la cabeza podía hacerse realidad.

Siempre he tenido la sensación de que el proyecto es más importante que la persona que lo crea. Pero con el tiempo he comprendido también otra cosa: cuando un proyecto empieza a ser útil a muchas personas, quien lo ha iniciado tiene la responsabilidad de darle una dirección y construir a su alrededor las condiciones para que pueda crecer.

Nací en Tarento, pero hoy vivo en Brescello, en Emilia-Romaña, el pueblo de Don Camillo y Peppone. La mía no ha sido una vida particularmente sencilla: me quedé huérfano cuando tenía nueve años y durante gran parte de mi vida las posibilidades económicas han sido limitadas.

Estudié informática en Bari, pero en un momento dado no pude continuar los estudios por motivos económicos. Así que empecé a trabajar en un almacén como mozo de almacén.

La vida toma a menudo caminos que no habías planeado. El trabajo era ese, pero mi cabeza seguía estando en otra parte. Nunca dejé de programar. Seguía estudiando, experimentando e imaginando aplicaciones y sistemas.

Me influyeron mucho las historias de personas que consiguieron construir algo partiendo de condiciones distantes de ser perfectas. No me interesaba copiar su camino. Me interesaba entender cómo una idea podía transformarse en algo capaz de cambiar la forma en que las personas utilizan una tecnología.

Desde el punto de vista técnico, siempre he tenido una predilección especial por C y C++. Los estudié desde la universidad y sigo considerándolos herramientas extraordinarias cuando el problema requiere control, previsibilidad y velocidad. Me gusta tener los menores estratos posibles entre lo que pienso y lo que el ordenador ejecuta.

Colibrì nació exactamente así.

Quería entender si era posible coger un ordenador relativamente común, incluso lento y sin una GPU particularmente potente, y conseguir ejecutar un modelo enorme.

No había una empresa detrás, no había un equipo y no había inicialmente un plan de negocio. Había un problema técnico que me curioseaba lo suficiente como para hacerme trabajar noche y día.

Cuando conseguí resolverlo, durante un tiempo el proyecto se quedó en mi ordenador. Luego decidí casi por casualidad publicarlo en GitHub.

A partir de ese momento ocurrió algo que no había previsto.

La gente empezó a probarlo, debatirlo, contribuir y utilizarlo. Colibrì empezó a ser mucho más grande que el experimento del que había nacido.

Y es precisamente ahí donde para mí cambió también la perspectiva.

Colibrì no nació porque yo quisiera construir una startup. Pero cuando miles de personas empiezan a decirte, directa o indirectamente, que el problema que has decidido abordar les interesa a ellas también, debéis empezar a preguntaros cómo de grande puede llegar a ser la solución.

Hoy es esta la pregunta que me interesa."

## Abrir un modelo, no solo usarlo

La página de GitHub del proyecto dice casi un manifiesto: "Frontier models should not be sealed inside datacenters. Colibrì exists so that anyone curious enough can open one up." Le pregunto qué significa realmente para él "abrir" un modelo, no simplemente acceder a él a través de una API, y si la democracia de la IA que imagina es una cuestión de acceso o algo más profundo.

"Para mí el acceso a la IA debería ser lo más sencillo posible. Deberíais poder encender un ordenador, abrir un programa y empezar a experimentar.

No debería ser una posibilidad reservada únicamente a quienes poseen hardware de decenas de miles de euros o a quienes pueden utilizar grandes infraestructuras.

Pero creo que el acceso es solo el primer nivel.

Lo que me interesa aún más es la posibilidad de conocer la tecnología que estáis utilizando.

Cuando hablo de un modelo 'abierto', por tanto, no me refiero simplemente a poder obtener una respuesta. Me refiero a poder ejecutarlo, observarlo, medirlo, hacer experimentos e intentar entender qué ocurre cuando cambiáis algo.

Hay una diferencia enorme entre utilizar una inteligencia y poder estudiarla.

Esto no significa que la nube sea incorrecta. La nube es y seguirá siendo extremadamente importante. Hay problemas para los que concentrar enormes cantidades de cálculo en un centro de datos es la mejor solución.

Yo pienso simplemente que no debe ser el único modelo posible.

Debería existir también otra posibilidad: llevar cada vez más capacidad de inferencia cerca de la persona, del investigador, de la empresa o del dispositivo que la necesita.

La democratización de la IA, en mi opinión, debería ser por tanto tanto una democratización del acceso como una democratización de la comprensión.

No me gustaría que la primera pregunta de una persona fuera: '¿Tengo suficiente GPU para poder probar esto?'

Me gustaría que fuera: '¿Qué puedo descubrir si pruebo a hacerlo?'

La IA se está convirtiendo en una de las herramientas de conocimiento más potentes que hemos construido. Cuantas más personas puedan experimentarla directamente, más aumentará la probabilidad de que alguien encuentre un uso, una optimización o incluso un paradigma en el que hoy todavía no hemos pensado.

Para mí el requisito principal debería ser cada vez más la curiosidad, no el tamaño de la infraestructura que poseéis."

## Un mensaje en Hacker News, no un manifiesto

Hay un detalle que me llamó la atención desde el principio: el mensaje con el que Fornaro presentó Colibrì en Hacker News no se titulaba "he creado el motor de inferencia definitivo", sino simplemente "Getting GLM-5.2 running on my slow computer". Una actitud casi modesta para un resultado que no es modesto. Le pregunto cuándo comprendió que su experimento personal se estaba convirtiendo en otra cosa, y qué reacción de la comunidad le hizo pensar que las cosas estaban cambiando de verdad.

"El título era simplemente 'Getting GLM-5.2 running on my slow computer' porque esa era exactamente la historia.

No quería decir que hubiera construido el motor de inferencia definitivo. Había resuelto un problema que me parecía interesante y quería explicar cómo.

Colibrì no había nacido con el objetivo de convertirse en una startup. Había nacido por curiosidad.

Luego ocurrieron dos cosas.

La primera fue ver a personas utilizar realmente lo que yo había construido.

Recuerdo en particular a un chico que me escribió para darme las gracias porque, gracias a Colibrì, había conseguido acceder a un modelo que de otro modo habría requerido una máquina mucho más cara.

Eso me impactó mucho más que el número de estrellas.

Porque por primera vez no estaba mirando solo una solución técnica. Estaba mirando un problema real eliminado para alguien.

La segunda cosa fue la comunidad.

Personas que no conocía empezaron a abrir issues, hacer pull requests, probar hardware, encontrar errores y proponer optimizaciones.

En ese momento comprendí que estaba ocurriendo algo importante: Colibrì no estaba creciendo porque yo intentara convencer a alguien de que fuera útil. La gente llegaba espontáneamente porque reconocía el problema.

Para quien construye tecnología, esto es una señal muy fuerte.

Desde entonces he empezado a mirar Colibrì de una manera diferente.

Sigue siendo un proyecto open source y quiero que siga siéndolo, pero creo que la tecnología y el problema que estamos abordando pueden tener implicaciones mucho mayores que el repositorio en el que empezó todo.

El paso interesante, ahora, es entender cómo transformar ese interés espontáneo en una tecnología cada vez más sólida, generalizable y utilizable.

Y para hacerlo, inevitablemente, Colibrì tendrá que crecer también más allá de la dimensión de una sola persona."
![colibri-dashboard.jpg](colibri-dashboard.jpg)
[El panel web de Colibrì, imagen tomada del repositorio oficial](https://github.com/JustVugg/colibri)

## Un archivo, mil trescientas líneas, ningún compromiso

El núcleo de Colibrì es un único archivo C de unas mil trescientas líneas, sin dependencias, sin GPU requerida, sin Python en tiempo de ejecución. En un momento histórico en el que vLLM, TensorRT-LLM y SGLang son proyectos nacidos en laboratorios con equipos numerosos y bases de código complejas, la elección de Fornaro suena casi como un acto de resistencia, un poco como ciertas producciones discográficas caseras hechas con cuatro instrumentos que consiguen sonar más densas que una orquesta entera. Le pregunto si detrás de esta extrema sencillez hay una elección puramente arquitectónica o una convicción más filosófica.

"Inicialmente fue una elección arquitectónica, pero se ha convertido también en una convicción.

Cuando intentas hacer funcionar un modelo enorme en una máquina relativamente pequeña, cada capa adicional tiene un coste.

Necesitas saber exactamente dónde se encuentra la memoria, cuándo se mueve, qué se calcula y por qué algo es lento.

El C me permite tener un control extremadamente directo sobre estas cosas.

Pero esto no significa que considere que la complejidad sea siempre negativa.

La complejidad es una inversión.

Debéis introducirla cuando el valor que produce es mayor que el coste que añade.

Al principio Colibrì podía permitirse ser extremadamente pequeño. Hoy están llegando backends de GPU, servidores, interfaces, nuevas arquitecturas y otros componentes. Inevitablemente el proyecto crecerá.

El reto es crecer sin perder legibilidad.

Me gustaría que el núcleo del sistema siguiera siendo algo que un buen desarrollador pueda abrir, leer y comprender.

Esto tiene también una ventaja muy concreta para un proyecto open source: reduce enormemente la barrera para quien quiere contribuir.

La sencillez, en este sentido, no es solo elegancia.

Es velocidad de desarrollo, capacidad de depuración (debugging), facilidad de experimentación y posibilidad de incorporar a nuevas personas al proyecto."

## El disco como memoria, no como almacén

El mecanismo en el que se basa Colibrì tiene una elegancia casi minimalista: la parte densa del modelo permanece residente en RAM, mientras que los expertos son llamados desde el disco solo cuando se necesitan, un poco como el compilador JIT de ciertos lenguajes que no traduce todo por adelantado sino solo lo que la ejecución requiere realmente, instante a instante. Le pregunto a Fornaro cuál es, para quien se acerca por primera vez a Colibrì, el concepto más contraintuitivo de digerir.

"Probablemente el concepto más contraintuitivo es este: un modelo gigantesco no utiliza necesariamente todos sus parámetros al mismo tiempo.

Cuando una persona oye '744 mil millones de parámetros', imagina que para generar cada token el ordenador debe utilizar todos esos parámetros.

En un modelo Mixture-of-Experts no funciona así.

Es más bien como una enorme organización con muchísimos departamentos especializados. Todos existen, pero para cada token el modelo activa solo una parte de los expertos.

Por tanto la pregunta deja de ser:

'¿Cómo hago para meter todo el modelo en la RAM?'

y pasa a ser:

'¿Cómo hago para tener disponible la parte correcta del modelo en el momento en que se necesita?'

Colibrì intenta responder a esta segunda pregunta.

El almacenamiento se convierte en un nivel más de la jerarquía de memoria. Los expertos pueden permanecer en el disco y ser llevados cerca del cálculo cuando se necesitan.

Es como tener un almacén enorme y un banco de trabajo relativamente pequeño. No pones todo el almacén sobre la mesa. Debéis organizar el sistema de manera que lo que se necesita llegue a la mesa lo suficientemente rápido.

Luego entran en juego cachés, prefetch, patrones de uso y otras optimizaciones.

El principio general, sin embargo, sigue siendo sencillo:

no debéis tener necesariamente todo al mismo tiempo.

Debéis conseguir tener lo correcto en el momento correcto.

Y es un principio que creo que puede tener aplicaciones mucho más amplias a medida que los modelos sigan creciendo."
![tiers.jpg](tiers.jpg)
[Una jerarquía de memoria en lugar de un único requisito de memoria, imagen tomada del repositorio oficial](https://github.com/JustVugg/colibri)

## 0,05 tokens por segundo, honestamente

Aquí llega el punto más debatido en internet. En un portátil con 25 GB de RAM, los primeros benchmarks hablaban de un token cada diez-veinte segundos, y un análisis de Wavect escribió que el proyecto "se ejecuta, pero a 0,05-0,1 tokens por segundo desde caché fría", definiéndolo como "una prueba seria de arquitectura, no aún un servidor listo para producción". Tom's Hardware indica en cambio 20-30 tokens por segundo como umbral para una interacción realmente fluida, mientras que en una máquina con seis GPU RTX 5090 se llega a 6 tokens por segundo. Le pregunto cómo se posiciona respecto a estas observaciones, si Colibrì es hoy un ejercicio de ingeniería fascinante o un producto ya utilizable.

"El análisis de Wavect es honesto.

Definir las primeras versiones de Colibrì como 'a serious proof of architecture, not yet a drop-in production server' es una descripción que considero correcta.

La velocidad es un problema real y no quiero ocultarlo.

En un portátil, hoy en día, ejecutar un modelo de esas dimensiones a través de Colibrì no significa tener la misma experiencia que tendríais utilizando un modelo servido por un gran centro de datos.

Pero en mi opinión el punto interesante es entender cuál es la trayectoria.

Antes el problema era binario: ese modelo entraba en vuestra infraestructura o no entraba.

Colibrì intenta transformarlo en un problema continuo: ¿cómo de despacio podemos empezar, cuánto podemos mejorar cachés, almacenamiento, prefetch, especulación, backends acelerados y cuánta parte del cuello de botella podemos eliminar progresivamente?

La ingeniería empieza a menudo transformando un cero en un número.

Una vez que algo funciona, podéis medirlo.

Y una vez que podéis medirlo, podéis empezar seriamente a optimizarlo.

No prometería hoy 20 o 30 tokens por segundo para un modelo de cientos de miles de millones de parámetros en cualquier portátil. Existen límites físicos que el software no puede simplemente borrar.

Pero creo que existe un espacio enorme entre 'imposible' y 'tan rápido como un centro de datos'.

Y es precisamente ese espacio el que me interesa explorar.

A corto plazo veo Colibrì como una plataforma muy interesante para desarrolladores, investigadores, aficionados y casos de uso en los que el acceso local a modelos enormes tiene un valor especial.

A largo plazo, en cambio, el objetivo es seguir reduciendo la distancia entre la inferencia local y la infraestructura centralizada.

Si conseguimos hacerlo lo suficientemente bien, no será solo un experimento técnico.

Se convertirá en una nueva opción de infraestructura."

## Corrección antes que el benchmark

Colibrì tiene todavía fronteras abiertas, no es un servidor de producción, por ahora trabaja con la arquitectura de GLM-5.2 y no con modelos MoE genéricos, la validación de la calidad de la cuantización int4 es un trabajo en curso, el disco NVMe sigue siendo el rival más duro de batir. Le pregunto cómo afronta estos retos y si existen compromisos que esté dispuesto a aceptar hoy para ganar velocidad, o líneas que considere en cambio infranqueables.

"Una pequeña corrección a la premisa: Colibrì hoy ya soporta diferentes familias de modelos MoE y cada nueva arquitectura añadida nos permite entender algo que puede ser útil también para las demás.

También la cuantización ha madurado mucho.

Hemos encontrado y corregido problemas reales de calidad y, en esto, la comunidad ha sido fundamental.

El principal rival sigue siendo, sin embargo, la cantidad de datos que debéis mover.

Y por eso una regla que intento aplicar continuamente es: medir antes de creer.

Es facilísimo inventar una optimización que sobre el papel parece brillante.

Mucho más difícil es demostrar que mejora realmente el sistema en hardware real y con cargas de trabajo reales.

Tengo un pequeño laboratorio de experimentos en el que muchas ideas van a morir.

Y es exactamente lo que debería ocurrir.

En cuanto a los compromisos, estoy dispuesto a aceptar muchos.

Puedo aceptar un arranque en frío más lento si el comportamiento mejora durante el uso.

Puedo aceptar mayor complejidad en el formato de los datos si significa leer mucho menos del almacenamiento.

Puedo aceptar estrategias diferentes según el hardware.

Lo que no quiero sacrificar es la corrección.

Un benchmark impresionante obtenido degradando silenciosamente la calidad del modelo no me interesa.

Si Colibrì debe convertirse en una infraestructura sobre la que otras personas construyan algo, la confianza en los resultados debe ir antes que el mejor número en una tabla."

## Software, hardware, modelos: tres caminos que convergen

El proyecto tiene ya backends de CUDA y Metal, una interfaz web funcional, el soporte nativo al decoding especulativo de GLM-5.2. Le pregunto qué falta para llegar a una velocidad que pueda competir realmente con una API en la nube en el día a día, digamos diez-veinte tokens por segundo en un hardware que una persona cualquiera pudiera comprarse, y si es una cuestión de código, de hardware, o de futuros modelos más adecuados para este enfoque.

"Son las tres cosas: software, hardware y modelos.

Pero probablemente el elemento más interesante es la forma en que estas tres partes pueden empezar a diseñarse juntas.

El software puede hacer muchísimo.

Podemos mejorar el formato de los datos, reducir las lecturas, prever qué expertos se necesitarán, solapar transferencia y cálculo, mejorar la caché y utilizar mejor las CPU, GPU y almacenamiento disponibles.

Pero el software no puede eliminar un límite físico.

El hardware seguirá siendo por tanto importante.

Los SSD de consumo son cada vez más rápidos, la capacidad de memoria crece y también las arquitecturas de los ordenadores están cambiando.

Para Colibrì es particularmente interesante porque nosotros consideramos el almacenamiento no simplemente como el lugar desde el que cargar el modelo al principio, sino como parte activa de la arquitectura de inferencia.

Luego están los modelos.

Los actuales se diseñaron para infraestructuras en las que existen enormes cantidades de memoria y ancho de banda.

No se optimizaron pensando en una máquina de consumo que debe decidir continuamente qué partes del modelo acercar al cálculo.

No veo sin embargo ninguna razón por la que esto deba seguir siendo una constante.

Modelos con mayor localidad, expertos más pequeños, routing más predecible o estructuras diseñadas explícitamente para jerarquías de memoria podrían cambiar radicalmente el problema.

En cierto sentido, podría ser que Colibrì haya llegado antes que el modelo ideal para este tipo de inferencia.

Esta es también una de las cosas que me parecen más interesantes desde el punto de vista futuro.

No quiero que Colibrì sea simplemente 'un programa que hace funcionar GLM en un portátil'.

Me interesa entender si algunas de las ideas que estamos explorando pueden convertirse en una manera diferente de pensar la inferencia de modelos muy grandes.

Si ocurre, el mercado potencial no estará limitado al aficionado individual con un ordenador lento.

Podrá afectar a estaciones de trabajo, edge computing, empresas que quieren mantener los datos localmente, investigación, dispositivos dedicados y probablemente casos de uso que hoy todavía no hemos imaginado."

## Poseer un modelo: más allá del ahorro

Hay quien ve en Colibrì la prueba de que la IA local puede hacerse realidad también para quienes no pueden permitirse un centro de datos, y hay quien objetó que la democratización de la IA es ya una realidad, basta un navegador y veinte dólares al mes para ChatGPT. Le pregunto cómo responde a esta objeción, y qué significa realmente poseer un modelo más allá del simple ahorro económico, si es una cuestión de privacidad, de libertad, o de algo más radical como la capacidad de hacer ciencia sobre la IA, no solo de usarla.

"La objeción es absolutamente legítima.

Si la pregunta es '¿puedo usar una inteligencia artificial muy potente?', la nube ha democratizado ya enormemente el acceso.

Y es algo extraordinario.

No considero Colibrì una guerra contra la nube.

Pienso que la nube y la IA local resuelven problemas diferentes y que en el futuro convivirán.

Habrá actividades para las que tendrá sentido utilizar el modelo más potente disponible en un centro de datos.

Y habrá otras en las que serán importantes la latencia, la privacidad, la previsibilidad de los costes, la independencia de la red, el control de la infraestructura o la posibilidad de estudiar exactamente el sistema que estáis utilizando.

Pienso en la historia de la informática.

El ordenador personal no hizo inútiles a los grandes ordenadores.

Simplemente abrió otra dimensión de la informática.

El hecho de que un ordenador fuera tuyo significaba que podías programarlo, modificarlo, romperlo, experimentar.

Con la IA pienso que puede ocurrir algo similar.

Un servicio remoto es extraordinariamente cómodo cuando queréis obtener una respuesta.

Un modelo local se vuelve interesante cuando queréis también hacer preguntas sobre el propio sistema.

¿Por qué ha respondido así?

¿Cómo cambia el comportamiento si modifico este componente?

¿Cuánto puedo comprimirlo?

¿Puedo reproducir el mismo resultado dentro de cinco años?

¿Puedo utilizar datos que no quiero enviar fuera de mi infraestructura?

¿Puedo construir un producto que siga funcionando sin depender completamente de un proveedor externo?

Por tanto no veo el futuro como 'nube contra local'.

Lo veo como un continuum.

Y creo que hoy una parte de ese continuum está todavía mucho menos desarrollada que la otra.

Es ahí donde Colibrì intenta trabajar."

## El 2036 y el legado de una idea

Cerramos con la mirada a largo plazo. Imagina el 2036, los modelos convertidos en aún más grandes o tal vez más pequeños y más inteligentes, el hardware de consumo transformado. Le pregunto si Colibrì, o algo nacido de él, seguirá siendo relevante, qué sueña que ocurra en los próximos diez años para quienes quieren tener la inteligencia artificial en sus propias manos, y más personalmente, tras veinticinco mil estrellas y los titulares en Tom's Hardware y Hacker News, qué quiere que la gente recuerde de él.

"En 2036 espero que muchas de las cosas que hoy Colibrì hace difíciles se hayan convertido en normales.

Esto no significa que espere que Colibrì desaparezca.

Significa que espero que evolucione.

Los proyectos tecnológicos importantes rara vez se quedan iguales a su primera versión. Cambian junto con el problema que están intentando resolver.

Si dentro de diez años ejecutar modelos enormes en hardware relativamente común es normal, será una victoria.

En ese momento probablemente Colibrì estará afrontando otra frontera.

Lo que me gustaría que permaneciera constante es la idea de fondo: reducir la distancia entre una persona curiosa y una tecnología que hoy parece demasiado grande, cara o compleja para ser explorada directamente.

Me gustaría que en 2036 una persona pudiera mirar un modelo avanzado y pensar:

'Quiero entender cómo funciona.'

Y pudiera hacerlo.

En cuanto a lo que quiero construir personalmente, hoy siento una responsabilidad diferente respecto al principio.

Colibrì nació como un experimento individual, pero no creo que deba permanecer necesariamente como tal.

Si queremos abordar seriamente este problema, se necesitarán personas mucho mejores que yo en muchas áreas diferentes, se necesitará una comunidad cada vez más fuerte y probablemente se necesitará también construir una estructura capaz de sostener el proyecto a largo plazo.

Esto no cambia la razón por la que empecé.

La hace simplemente más ambiciosa.

Y si dentro de diez años alguien, ante un problema que todos consideran imposible, piensa:

'Probemos.'

y tal vez utiliza algo que ha nacido también del trabajo hecho hoy en Colibrì, para mí será ya un resultado enorme.

No me interesa particularmente que se recuerde la idea de Vincenzo Fornaro como 'genio'.

Me interesaría mucho más que permaneciera otra idea:

que una persona con pocos recursos, pero suficiente curiosidad, puede todavía empezar algo lo suficientemente importante como para atraer a otras personas y hacerse mucho más grande que ella.

Es exactamente lo que le está pasando a Colibrì."

---

*El [repositorio de Colibrì](https://github.com/JustVugg/colibri) permanece consultable en GitHub para quien quiera probarlo, contribuir, o simplemente leer esas mil trescientas líneas de C que han encendido la conversación.*
