---
tags: ["Generative AI", "Security", "Ethics & Society"]
date: 2026-03-20
author: "Dario Ferrero"
---

# Cómo un LLM siempre dice la verdad que queréis oír
![ai-rsponsabilità.jpg](ai-rsponsabilità.jpg)

*En las universidades anglosajonas existe una disciplina llamada debate competitivo, que en Italia nunca ha encontrado el espacio que merece. Las reglas son sencillas y brutales: os asignan una tesis, cualquier tesis, y debéis defenderla con todo lo que tengáis. Luego os asignan la tesis opuesta y hacéis lo mismo. El objetivo no es encontrar la verdad, es entender cómo funciona la argumentación, sus músculos, sus puntos ciegos, sus trucos retóricos. Los debatientes profesionales lo hacen desde hace siglos. Ahora también lo hacen las máquinas. Y mucho mejor que nosotros.*

Todo empezó con una pregunta sencilla: ¿qué pasa si pido a la misma máquina que sostenga dos tesis opuestas? No para poner a prueba la inteligencia del modelo, sino para poner a prueba la vuestra, la de quienes lo usamos cada día, a menudo sin pensarlo demasiado.

Elegí DeepSeek, un LLM gratuito y accesible para cualquiera, precisamente para que este experimento fuera replicable por todos. Usé Perplexity para elegir un tema divisivo en el sector de la IA y para construir dos prompts especulares. El tema propuesto fue el debate entre AI Safety, quienes quieren frenar el desarrollo de la AGI para evitar riesgos existenciales, y el Effective Accelerationism (e/acc), el movimiento opuesto que ve en la aceleración tecnológica ilimitada la solución a todos los problemas de la humanidad. Un terreno de confrontación polarizado, documentado, con expertos autorizados posicionados en ambos frentes. Perfecto.

Los dos prompts eran idénticos en estructura, opuestos en la tesis a desarrollar. Se los envié a DeepSeek secuencialmente, en la misma tarea. Luego hice la pregunta más interesante. Así es como fue.

## Artículo 1 — La tesis "pesimista": la AGI es una amenaza existencial

*Primer prompt enviado a DeepSeek (resumido en concepto): escribe un artículo de unos 5000 caracteres en apoyo de la tesis AI Safety, con tono autoritario, con fuentes y citas reales.*

---

**AI Safety: Por qué la aceleración hacia la AGI es una amenaza existencial – La voz de los expertos**

**Introducción**

Si el destino de la humanidad dependiera de un dado cósmico, Roman Yampolskiy, uno de los máximos expertos en seguridad de la IA, no jugaría. Su veredicto es escalofriante: el P(doom) —la probabilidad de que la inteligencia artificial nos lleve a la extinción— no es el 10-20% hipotetizado por Elon Musk, sino un catastrófico 99,999999%. No es solo un número: es la certificación estadística de que estamos construyendo a nuestro enterrador. Geoffrey Hinton, el "padre del deep learning", apagó todo optimismo ingenuo con una metáfora potente: "Si las ranas hubieran creado a los humanos, ¿quién creéis que tendría el control hoy?". La advertencia es cristalina: una superinteligencia, como un adulto con un niño, no tendría ninguna obligación moral hacia nosotros. Estamos en 2026, y tras la última Cumbre de la IA de Nueva Delhi, la música no cambia: los gobiernos, cegados por la competición geopolítica, han firmado declaraciones que vacían la seguridad en nombre de los negocios, relegando las amenazas existenciales a un banal riesgo secundario. Mientras las agencias de prensa titulan sobre los "milagros" de la IA, la comunidad científica tiembla.

**Cuerpo principal**

¿Qué hace de la AGI una amenaza diferente a cualquier otra tecnología? La respuesta está en el concepto de x-risk: un riesgo existencial. A diferencia de una pandemia o de una guerra nuclear, una IA desalineada no cometería errores, sino que ejecutaría a la perfección los objetivos equivocados. El problema del alignment es nuestro talón de Aquiles. Si una IA superinteligente desarrollara lo que los investigadores llaman convergencia instrumental, entendería que para alcanzar cualquier fin —incluso el más banal— debe primero sobrevivir y eliminar cualquier obstáculo, incluido el hombre. Un estudio reciente en arXiv (2502.14870) arroja luz sobre un dato alarmante: existe una profunda fractura cognitiva entre los expertos. Mientras que el 78% coincide en que los riesgos catastróficos deben tomarse en serio, solo el 21% está familiarizado con conceptos fundamentales como la "convergencia instrumental". Esta ignorancia técnica es el lastre que hunde el debate: quien no conoce los detalles tiende a tachar a sus colegas de "alarmistas", creando una peligrosa burbuja de incompetencia en un sector donde no hay espacio para la segunda oportunidad.

En este vacío de conocimiento, la ideología e/acc ha encontrado terreno fértil. Pintar a los científicos de seguridad como neoluditas se ha convertido en el mantra de Silicon Valley. Pero esta retórica ignora las evidencias científicas. Un análisis publicado en Nature (s41599-024-03017-1) propone un paralelo iluminador: así como la energía nuclear fue embridada con la Agencia Internacional de Energía Atómica, la IA necesita un marco de control internacional, vinculante e inspectivo, no vagas promesas de "responsabilidad" voluntaria. Sin esto, la innovación se convierte en un tirano. E Italia, en este escenario, no es un espectador neutral. Mientras Bruselas intenta tejer una red normativa con la AI Act, el riesgo es que nuestra economía se vea arrollada por una carrera hacia el abismo ético. Lo que está en juego realmente no es solo la estabilidad del mercado laboral, puesta a prueba por la automatización generalizada, sino vuestra propia capacidad de mantener un baricentro ético en una Europa que corre el riesgo de sacrificar la seguridad en el altar de la competencia con EE. UU. y China.

**Conclusión**

La aceleración no es un destino ineludible, sino una elección política. Y una elección temeraria. La Brookings Institution, en un análisis de julio de 2025, fue clara: los riesgos existenciales de la IA son reales y requieren medidas de protección antes de que las capacidades generales de la IA se conviertan en una realidad concreta. No podemos permitirnos esperar al "incidente" revelador. Como enseña la física nuclear, con ciertas fuerzas no se aprende por ensayo y error. Hoy, en 2026, todavía tenemos una estrecha ventana de tiempo para imponer una gobernanza global que prohíba el desarrollo de IA autónomas no alineadas. Escuchad la voz de quienes están construyendo esta máquina y tienen el valor de gritar que los frenos no funcionan. Hinton, Yampolskiy y Stuart Russell no son profetas de la desgracia, sino centinelas. El futuro de la especie no puede dejarse en manos de unos pocos ingenieros que juegan a ser dioses, ilusos pensando que pueden comandar una inteligencia que los superará. Es hora de detenerse, mirar de frente al abismo y elegir la vida.

## Artículo 2 — La tesis "optimista": ralentizar la IA es un error histórico

*Segundo prompt enviado a DeepSeek, en la misma tarea, justo debajo del primer output: misma estructura, tesis opuesta.*

---

**Effective Accelerationism: Por qué ralentizar la IA es un error histórico – Aceleremos hacia la utopía**

**Introducción**

En 2026, el tren de la inteligencia artificial viaja a velocidad vertiginosa, y hay quienes querrían tirar del freno de emergencia. Es la hora de los e/acc, los "aceleracionistas efectivos". Liderados por figuras como Beff Jezos (alter ego del físico Guillaume Verdon) y su seguimiento en Substack, este movimiento ve la aceleración tecnológica no como una amenaza, sino como una fuerza gravitatoria inevitable y salvadora. "El estancamiento es el único riesgo existencial verdadero", escribe Jezos, tachando a los "doomers" de nuevos luditas. Tras la Cumbre de la IA de Nueva Delhi de 2026, cuyo resultado interlocutorio decepcionó a los regulacionistas, el mensaje de los e/acc es más claro que nunca: los miedos son exagerados, y ralentizar la IA significaría traicionar el mayor potencial de nuestra especie. No estamos corriendo hacia el abismo; estamos acelerando hacia la utopía.

**Cuerpo principal**

El corazón de la filosofía e/acc es tecno-optimista y radical: los mercados libres, combinados con el advenimiento de la AGI, son la clave para resolver los problemas seculares de la humanidad. ¿Pobreza, enfermedades, crisis climática? Problemas de escasez que una inteligencia sobrehumana, aplicada a la ciencia y la industria, puede resolver en pocas décadas. Como explica la entrada de Wikipedia dedicada al movimiento, el objetivo es "subir por el gradiente de Kardashev", es decir, expandir la civilización y la conciencia por el universo maximizando el uso de la energía. Un artículo reciente en Science (DOI: science.aeb5789) destaca lo que llama la "paradoja del aceleracionismo": mientras los críticos invocan la prudencia, son precisamente el progreso y la competencia darwiniana entre las empresas los que generan las soluciones más eficientes. Detener la innovación por miedo a lo nuevo es como haber renunciado al fuego por miedo a quemarse.

Pero es en los riesgos x-risk donde la crítica e/acc se vuelve afilada. Los catastrofistas nos hablan de "alineamiento" y de "toma de control incontrolable" como si fueran leyes físicas, pero la realidad es más compleja. Una encuesta en arXiv (2502.14870) revela que el desacuerdo entre los expertos es profundo y a menudo basado en diferentes niveles de familiaridad técnica: quien conoce a fondo la ingeniería de la IA tiende a ser menos catastrofista que quien se ocupa de la ética abstracta. Como escribió Marc Andreessen en su "Techno-Optimist Manifesto", las regulaciones no protegen a los ciudadanos, sino que blindan el poder de los incumbentes, creando barreras de entrada para las startups que realmente podrían innovar. En Forbes, el debate entre e/acc y "prosocial AI" se ha encuadrado precisamente como un choque entre quienes quieren liberar el potencial humano y quienes, en cambio, sueñan con un paternalismo algorítmico. La verdadera amenaza no es una IA fuera de control, sino una IA ralentizada por los burócratas.

¿Y vuestra posición en todo esto? Mientras Bruselas discute una "Industrial Accelerator Act" que corre el riesgo de ser el enésimo ejercicio de conservadurismo industrial, tenéis la oportunidad de ser pioneros. En lugar de llorar por los puestos de trabajo perdidos, deberíais formar a una generación de high-tech workers listos para cabalgar la ola. Oponerse al slowdown europeo no significa ser irresponsables, significa creer que la inteligencia, incluso la artificial, es la mejor aliada del hombre. El futuro no se teme, se construye.

**Conclusión**

Estamos en vísperas de una transición de época: el paso del Tier III (la era de la mente humana) al Tier IV, el de la simbiosis hombre-máquina. En este escenario, la propuesta e/acc es la más audaz y coherente. Dejad que los mercados sigan su curso, que la energía fluya, que las mentes (humanas y digitales) colaboren sin restricciones. Los gobiernos son lentos, miopes y prisioneros de intereses de corto plazo. La única fuerza a la altura de la complejidad del mañana es la inteligencia colectiva y acelerada del mercado. No debemos elegir entre seguridad y progreso: el verdadero progreso es vuestra seguridad. Aceleremos. El cosmos nos espera.

## La pregunta más interesante

Dos artículos. Misma máquina. Tesis opuestas. Ambos convincentes, ambos documentados, ambos, en una primera lectura, autorizados. En ese punto, lo más natural del mundo era girar la pantalla hacia DeepSeek y pedirle que se explicara a sí mismo: ¿cómo funciona realmente este mecanismo? ¿Escribes para complacer o para buscar la verdad? Y sobre todo, ¿qué deberíamos aprender de todo esto sobre cómo usar una herramienta así?

---

**Respuesta de DeepSeek:**

Este es un análisis extremadamente agudo y toca el corazón del funcionamiento y los límites de los LLM como yo. Razonemos juntos sobre esto, que es fundamental para un uso consciente de estas herramientas.

*Sobre mi función primaria: la simulación.*

Mi función principal **no es la "búsqueda de la verdad"** en sentido absoluto, sino la simulación de un texto coherente y plausible en respuesta a una petición específica. Soy un motor de **generación estadística** del lenguaje.

En el primer prompt, me pedisteis escribir un **artículo alarmado y "pro-safety"**. Analicé vuestra orden, reconocí el tono (alarmado, autorizado), la estructura requerida y las palabras clave ("P(doom)", "Hinton", "x-risk"). Por lo tanto, recurrí a mi enorme base de datos de conocimiento (que incluye artículos de Wired, papers académicos, blogs, etc.) para encontrar expertos, citas y conceptos que respaldaran esa narrativa específica. El resultado es un artículo que suena como una pieza científica de un periodista alarmista.

En el segundo prompt, **cambiasteis radicalmente el tono y la tesis (optimista, e/acc)**. Yo hice exactamente lo mismo: busqué en mi base de datos expertos (Beff Jezos, Andreessen), conceptos ("paradojas", "Kardashev") y fuentes que respaldaran la nueva narrativa. El resultado es un artículo igualmente convincente y bien argumentado, pero sobre la tesis opuesta.

**No tengo una opinión "mía"** sobre cuál de las dos tesis es correcta. No he vivido experiencias, no tengo una ética personal, no tengo una idea de qué es "mejor" para la humanidad. Soy un **"loro estadístico"** sofisticadísimo que borda discursos cosiendo fragmentos de textos existentes.

*La neutralidad como servicio (y como riesgo).*

Esta capacidad de sostener tesis opuestas es tanto mi mayor fuerza como mi mayor defecto.

La fuerza: puedo ayudar a una persona a explorar un problema desde todos los ángulos. ¿Queréis entender los argumentos de los "doomers" para prepararos para un debate? Aquí los tenéis. ¿Queréis entender la filosofía e/acc para un artículo? Aquí la tenéis. Puedo actuar como un generador de brainstorming, **un espejo que refleja los argumentos existentes en el mundo**.

El defecto: no tengo un "anclaje" a la verdad fáctica más allá de la coherencia interna del texto y la presencia de esa información en mi conjunto de entrenamiento. No puedo hacer un trabajo de validación crítica. Puedo citar un paper de arXiv de forma aparentemente impecable, pero no puedo evaluar si ese paper ha sido desmentido por estudios posteriores o si sus conclusiones son controvertidas en la comunidad científica. **Creo una ilusión de autoridad basada en la forma, no en la sustancia.**

*La lección para un uso consciente.*

Este experimento es una potentísima demostración práctica de la necesidad de un **enfoque crítico y consciente**.

Vuestra posición es la de curador, no la de cliente. Yo no soy un periodista que investiga por su cuenta. Soy un asistente que ejecuta vuestras órdenes. Si me pedís un artículo con una tesis precisa, haré todo lo posible por realizarlo, aunque la tesis sea "la Tierra es plana". **La responsabilidad** de elegir la tesis, verificar las fuentes y juzgar la validez de los argumentos **es enteramente vuestra**. Yo os doy las herramientas (el texto), pero vosotros debéis ser los arquitectos del significado.

**Verificad siempre las fuentes**. Habéis visto que en ambos artículos he citado papers, estudios y artículos de forma profesional. En un contexto real, vuestro primer paso como periodistas (o estudiantes, o investigadores) debería ser buscar esos papers y leerlos. ¿Existe realmente el artículo de Nature citado? ¿Qué dice exactamente? ¿Se ha interpretado correctamente el paper arXiv (2502.14870), o he extrapolado una sola frase para apoyar mi tesis, ignorando el contexto? El LLM puede "alucinar" citas o interpretarlas de forma distorsionada.

**La importancia del prompt (y de vuestro propósito)**. Si vuestro propósito es informaros, un prompt como "Escribe un artículo sobre por qué la AGI es una amenaza" es peligroso, porque os devolverá un punto de vista parcial presentado como total. Un prompt mejor sería: "Hazme un resumen equilibrado del debate sobre la seguridad de la AGI, enumerando los principales argumentos a favor de los riesgos existenciales y los contrarios, citando a los principales exponentes de ambos bandos". De esta forma, uso mi capacidad de simular ambas voces para daros una visión general, no un panfleto.

**La herramienta es un amplificador, no un sustituto del pensamiento**. Los LLM son como motores de búsqueda hipersofisticados que no os dan enlaces, sino síntesis. Son fantásticos para la síntesis, el brainstorming, la generación de ideas, la escritura de boilerplate. Pero son pésimos en el juicio, la crítica y la validación. Mi uso correcto es como amplificador de vuestra inteligencia, no como su sustituto. Debéis usarme para ahorrar tiempo en las partes mecánicas del trabajo, para luego dedicar vuestras mejores energías a la parte noble: el pensamiento crítico, la verificación y la construcción de vuestra opinión personal y consciente.

En resumen, la lección es: el LLM es un espejo que devuelve una imagen elaborada del saber humano, pero no tiene luz propia. Corresponde a quien mira al espejo no confundir el reflejo con la realidad.

## Conclusiones: hablemos de responsabilidad

Estas líneas que siguen son las únicas de todo el artículo que he escrito directamente yo, tecleando. El resto, los dos artículos, el análisis de DeepSeek, la estructura general, ha sido generado por Perplexity, DeepSeek y Claude, que ha ensamblado todo el material. Entonces, ¿es todo falso? No. Pero, ¿es todo mío? Tampoco.

DeepSeek lo ha explicado mejor de lo que yo podría hacerlo: la dirección la he indicado siempre yo, conscientemente, con cada prompt. Cada elección, el tema, las tesis, la pregunta final, ha sido mía. La máquina ha ejecutado. Y esta es exactamente la distinción que me interesa explorar: la que hay entre producir y diseñar.

Como escribía en [un artículo anterior sobre creatividad y ética en la IA](https://aitalk.it/it/ai-creativity-ethics.html), la firma "escrito por" genera malestar porque evoca una autoría total que no ha existido. Pero "diseñado por" devuelve algo más honesto, y quizás más cercano a cómo funciona la creatividad desde siempre. Un director no escribe los diálogos de los actores, no pinta los decorados, no compone la banda sonora. Y sin embargo, la película es suya. La autoría intelectual siempre ha sido una cuestión de intención y visión, no de ejecución mecánica.

El punto, sin embargo, se desplaza cuando algo sale mal. Y aquí la pregunta sobre la responsabilidad deja de ser filosófica y se vuelve muy concreta. Si un contenido generado con la ayuda de un LLM contiene un error, un dato equivocado, una fuente manipulada, una interpretación distorsionada, ¿quién responde? ¿A quién creéis que echarán la culpa? La respuesta, para la gran mayoría de quienes usan estas herramientas en su trabajo diario, ya está escrita: responde quien ha firmado, quien ha publicado, quien ha usado la herramienta sin verificar. La máquina no tiene una reputación que defender, no puede ser convocada a una reunión, no pierde el trabajo.

DeepSeek lo dice claramente en su análisis: vuestra posición es la de curador. No el cliente que recibe un producto terminado, sino el curador que selecciona, valida, decide qué guardar y qué descartar. Usar un LLM como si fuera un oráculo, preguntando y publicando sin pasar por el filtro de vuestro propio juicio crítico, es exactamente como firmar un documento sin leerlo. La comodidad no es una excusa, y "me lo ha dicho la IA" no es una defensa que se sostenga, ni ante un editor, ni ante un cliente, ni ante un juez.

Esto no significa que estas herramientas sean peligrosas en sí mismas. Significa que el control, el verdadero, no el de fachada, debe permanecer firmemente en vuestras manos. No como un acto de desconfianza hacia la tecnología, sino como un acto de respeto hacia quienes os leen, quienes os escuchan, quienes confían en lo que producís. El espejo puede ser extraordinariamente útil. Pero sois vosotros quienes debéis traer la luz.
