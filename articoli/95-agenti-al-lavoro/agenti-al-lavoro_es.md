---
tags: ["Business", "Generative AI", "Ethics & Society"]
date: 2026-03-04
author: "Dario Ferrero"
---

# Los agentes de IA trabajan. Y las cuentas cuadran
![agenti-al-lavoro.jpg](agenti-al-lavoro.jpg)

## Del entusiasmo a la producción

*Hay un dato en el nuevo [informe de DigitalOcean publicado en febrero de 2026](https://www.digitalocean.com/currents/february-2026) que parece contradecirse a sí mismo. El porcentaje de empresas que declaran usar inteligencia artificial ha *bajado* ligeramente, del 79% en 2024 al 77%, y sin embargo, en el mismo periodo, la proporción de quienes realmente la están implementando en sus procesos casi se ha *duplicado*, pasando del 13% al 25%. Una paradoja solo en apariencia. Ese 2% menos no es una deserción: es una limpieza. Terminada la temporada del turismo tecnológico, todos experimentando, pocos construyendo, el campo ha quedado para quienes van en serio.*

El informe, llamado *Currents*, es una investigación periódica que DigitalOcean realiza sobre el estado de la inteligencia artificial en las empresas tecnológicas en crecimiento. La edición de febrero de 2026 se basa en más de 1.100 respuestas recogidas entre octubre y noviembre de 2025 de desarrolladores, directores técnicos y fundadores distribuidos en 102 países. Los más representados son Estados Unidos con un 28%, seguidos del Reino Unido con un 7%, Canadá con un 6%, India con un 4%, Alemania y Países Bajos con un 3% cada uno, e Italia con un 2%. Una muestra amplia, variada y suficientemente global como para ofrecer una visión creíble del estado del arte.

El mensaje central es inequívoco: hemos entrado en una nueva fase. El 52% de las empresas encuestadas se encuentra hoy en una de las tres fases más avanzadas del camino con la inteligencia artificial: implementación activa, optimización del rendimiento o adopción como elemento central de su estrategia. En 2024, ese mismo porcentaje se quedaba en el 35%. Diecisiete puntos porcentuales en doce meses no son una evolución gradual.

## No se construyen modelos, se usan

Uno de los puntos más debatidos en el relato público sobre la inteligencia artificial se refiere a un dilema al que toda empresa se enfrenta tarde o temprano: construir sus propios modelos, manteniendo el control total sobre los datos y la infraestructura, o confiar en proveedores externos, aceptando los riesgos de dependencia, soberanía de los datos y confidencialidad que esto conlleva. Los datos del informe no resuelven el dilema, pero cuentan con claridad qué opción está ganando en la práctica.

Solo el 15% de los encuestados se dedica principalmente a entrenar modelos desde cero. Para todos los demás, el trabajo está en otra parte: el 64% integra en sus aplicaciones las interfaces de programación de proveedores terceros, y el 61% usa una combinación de herramientas diferentes en lugar de una única solución integrada. La inteligencia artificial, para la gran mayoría de quienes realmente la usan, se ha convertido en un servicio al que conectarse, no en una tecnología que construir.

Este desplazamiento tiene un nombre preciso: inferencia. Si el entrenamiento es la fase en la que un modelo aprende (costosa, larga, reservada a unos pocos laboratorios), la inferencia es la fase en la que ese modelo se *usa* para generar respuestas, analizar documentos, escribir código, responder a clientes. Es aquí donde se concentra ahora el grueso de las inversiones: el 44% de los encuestados destina entre el 76% y el 100% de su presupuesto de inteligencia artificial precisamente a la inferencia. La comparación con la transición a la nube de hace una década es inevitable: también entonces la mayoría dejó de ocuparse del hardware y aprendió a trabajar con servicios remotos. La inteligencia artificial está atravesando la misma fase.

## El coste oculto de la inteligencia

Si hay un obstáculo que surge con fuerza del informe, es el coste de la inferencia a gran escala. El 49% de los encuestados lo identifica como el principal límite al crecimiento de su uso de la inteligencia artificial. No la complejidad técnica, ni los riesgos legales: el coste.

Cuando se lleva un sistema basado en modelos lingüísticos a producción, cuando debe responder a miles o millones de peticiones al día, la factura crece de forma no siempre previsible. Y la previsibilidad, según los datos, es una de las preocupaciones más sentidas. Para quienes usan múltiples herramientas y proveedores diferentes, los problemas se multiplican: el 50% de los encuestados que opera con infraestructuras múltiples señala la necesidad de gestionar interfaces separadas, el 49% tiene dificultades para prever los costes y el 48% encuentra dificultades para orquestar y desplegar los sistemas.

Solo el 23% de los encuestados trabaja con un único proveedor que integra modelos, datos e infraestructura. Todos los demás deben lidiar con una cadena de suministro fragmentada, donde cada pieza requiere habilidades, contratos y atención específicos. La inteligencia artificial, al menos en su fase actual, no es un producto llave en mano: es una obra permanente, con todo lo que ello conlleva en términos de complejidad de gestión.
![grafico1 .jpg](grafico1 .jpg)
[Imagen tomada de digitalocean.com](https://www.digitalocean.com/currents/february-2026)

## Quién manda entre los modelos

El informe ofrece una fotografía nítida del panorama de los modelos lingüísticos más usados, y las cifras confirman algunas intuiciones pero reservan alguna sorpresa.

OpenAI mantiene una posición dominante: el 72% de los encuestados usa sus modelos. La ventaja del primero en llegar se traduce aún en cuotas de mercado significativas. Pero el margen se estrecha: Google está en el 50%, Anthropic en el 47%. Ambos han recuperado terreno rápidamente, y la diferencia con el líder ya no es abismal.

La verdadera sorpresa viene del mundo de los modelos abiertos. Meta con Llama y DeepSeek alcanzan ambos el 21%. DeepSeek es particularmente digno de mención: entró en el mercado solo a finales de 2024 y ya ha alcanzado el mismo nivel de adopción que Llama, que cuenta con años de ventaja. Los modelos de código abierto ofrecen ventajas concretas: flexibilidad en la adaptación, ausencia de dependencia de un único proveedor, posibilidad de ejecutarse en infraestructuras propias sin enviar datos a terceros. Para muchas empresas, especialmente en contextos donde la confidencialidad es crucial, no son una opción de segunda mano sino una estrategia consciente. El mercado de modelos no es ni un monopolio ni una torre de Babel: es un oligopolio en rápida evolución, donde quienes apuestan por un único proveedor asumen un riesgo estratégico que muchos prefieren evitar.

## Los agentes: qué son, qué hacen, cuánto funcionan

La palabra "agente" es quizás la más inflada del vocabulario tecnológico de los últimos doce meses. Vale la pena definirla con precisión.

Un agente de inteligencia artificial es un sistema capaz de realizar tareas de forma autónoma, tomando decisiones y realizando acciones (buscar información, escribir código, enviar mensajes, actualizar archivos) sin que cada paso requiera intervención humana. La diferencia respecto a un simple asistente conversacional es sustancial: un asistente responde a preguntas, un agente *hace* cosas. Es la distancia entre un navegador que indica dónde girar y un coche autónomo.

Los datos muestran que esta tecnología ha dejado de ser solo una promesa. El 53% de las empresas que usan agentes ha observado ahorros de tiempo y aumentos de productividad. El 44% ha registrado la creación de nuevas capacidades operativas que antes no era capaz de ofrecer. El 32% ha reducido la necesidad de nuevas contrataciones. En conjunto, el 67% de quienes han adoptado agentes han encontrado alguna forma de mejora de la productividad: el 25% en el orden del 1-25%, el 17% entre el 26% y el 50%, el 9% entre el 51% y el 75%, y otro 9% con ganancias superiores al 75%.

Son porcentajes que hablan, pero deben leerse con la debida cautela. El 14% aún no ha visto beneficios concretos. Y sobre todo, el nivel de autonomía efectivamente concedido a los agentes sigue siendo, en la mayoría de los casos, bastante limitado. Solo el 10% de los encuestados tiene agentes completamente autónomos en producción. El 40% todavía hace que un ser humano revise todos los resultados. El 58% utiliza puntos de aprobación humana como principal medida de control. Los agentes trabajan, pero bajo vigilancia.

El tipo de agente más extendido es el especializado en una sola tarea (44%), seguido de los capaces de gestionar tareas múltiples (29%) y de sistemas en los que varios agentes colaboran entre sí (17%). El caso de uso más popular, declarado por el 54% de los encuestados, es la generación y reescritura de código: nada sorprendente, dado que la muestra está compuesta predominantemente por desarrolladores. Siguen el análisis de datos (41%), la automatización del soporte al cliente (40%), la búsqueda y resumen de información (39%) y la gestión de flujos de trabajo internos (38%).

Sin embargo, hay un dato que va más allá de los casos de uso individuales y cuenta algo más estructural: el 60% de los encuestados identifica aplicaciones y agentes como el nivel del stack tecnológico con mayor valor a largo plazo. No la infraestructura, citada solo por el 19%, ni las plataformas de desarrollo, con un 17%. Es una señal clara de dónde piensa el mercado que se juega la partida real: no en poseer la potencia de cálculo o los modelos subyacentes, sino en construir los sistemas que los ponen a trabajar de forma útil y medible. Es la diferencia entre poseer una central eléctrica y saber construir los electrodomésticos que la gente realmente quiere usar.

## La brecha se ensancha: quien empieza ahora corre el riesgo de perseguir

Uno de los mensajes más explícitos del informe se refiere a la distancia creciente entre quienes ya han integrado la inteligencia artificial en sus procesos y quienes aún están mirando por la ventana. El 50% de los encuestados declara estar experimentando o desplegando agentes. Pero de estos, solo el 10% los ha integrado de forma sistemática. El 33% está en la fase de pequeños experimentos, el 28% todavía está explorando los conceptos básicos y el 23% ha iniciado las primeras cargas de trabajo reales.

Entre quienes aún no usan agentes, las perspectivas para 2026 son preocupantes. El 44% declara no tener planes de experimentarlos. Solo el 26% ha planificado pruebas o proyectos piloto. La razón por la que esta brecha corre el riesgo de agravarse está ligada a la naturaleza misma del aprendizaje organizacional. Adoptar la inteligencia artificial no es como instalar un programa: requiere meses de experimentación, ajustes, construcción de habilidades internas, revisión de procesos. Quien empieza ahora ya tiene un retraso estructural respecto a quien empezó hace un año. La misma dinámica se vio con la adopción del comercio electrónico, la nube, las redes sociales: las empresas que apostaron con antelación construyeron ventajas difíciles de cerrar.

El 37% de los encuestados prevé aumentar el presupuesto destinado a aplicaciones y agentes en los próximos doce meses, la categoría de inversión más citada en absoluto. Y el 38% de quienes aún no han iniciado experimentos declara que empezará en 2026. Pero declarar no es hacer, y la historia de las grandes transformaciones tecnológicas está llena de intenciones no traducidas en acciones.
![grafico2.jpg](grafico2.jpg)
[Imagen tomada de digitalocean.com](https://www.digitalocean.com/currents/february-2026)

## Los nudos técnicos por resolver

El informe de DigitalOcean ofrece una fotografía precisa del estado actual, pero algunas preguntas siguen sin respuesta y acompañarán al sector durante todo 2026.

La primera se refiere a la fiabilidad. El 41% de los encuestados identifica precisamente la falta de previsibilidad de los agentes como principal obstáculo para su difusión. Un sistema que realiza acciones en el mundo real, actualiza archivos, envía mensajes, ejecuta operaciones, debe ser coherente. Los modelos actuales han realizado progresos enormes, pero aún no han alcanzado el umbral que requieren muchos casos de uso productivos. Es también por esto que el 40% mantiene aún un control humano sistemático: no por elección filosófica, sino por necesidad práctica. El 31% de los encuestados señala además la integración con las aplicaciones existentes como segundo obstáculo principal: las empresas no parten de cero, tienen sistemas de gestión, archivos y flujos construidos durante años, a menudo décadas, y conectar un agente inteligente a este ecosistema requiere tiempo, habilidades y pruebas exhaustivas para evitar que el nuevo sistema introduzca comportamientos inesperados.

La segunda cuestión es la de la concentración de poder. Tres proveedores (OpenAI, Google, Anthropic) controlan juntos la cuota dominante de los modelos en uso a nivel global. Si estos modelos se convierten en infraestructura crítica para millones de empresas, las decisiones que estos tres actores toman sobre precios, acceso, censura de contenidos y condiciones de uso se transforman de hecho en políticas industriales no elegidas por nadie. Los modelos abiertos como Llama y DeepSeek ofrecen una alternativa concreta, pero requieren habilidades de despliegue y recursos de infraestructura que no todas las organizaciones pueden permitirse. La dependencia no es un riesgo teórico: ya es visible en los datos, y el hecho de que solo el 21% de los encuestados use modelos abiertos señala lo difícil que es, en la práctica, liberarse del triunvirato comercial.

## Trabajo, Europa y las preguntas que quedan

La tercera pregunta es la del trabajo. El 32% de quienes usan agentes ya ha reducido la necesidad de nuevas contrataciones. Las ganancias de productividad documentadas por el informe no se traducen automáticamente en bienestar generalizado. Si los ahorros permanecen concentrados en las empresas más capitalizadas, la brecha entre quienes ganan y quienes pierden en la transformación se ensanchará aún más. Si, por el contrario, esa misma productividad se usa para expandir la oferta, abrir nuevos mercados, ofrecer servicios antes inaccesibles, el efecto puede ser positivo incluso para quienes trabajan. La tecnología no decide: deciden las organizaciones, las políticas públicas, las elecciones de quienes ostentan el poder económico.

Para Italia y Europa, presentes pero no dominantes en la muestra, queda abierta la pregunta sobre cómo conciliar la urgencia de adoptar estas tecnologías con un contexto normativo complejo. El reglamento europeo sobre inteligencia artificial, que entró en vigor en 2024, impone requisitos de cumplimiento, transparencia y evaluación de riesgos que muchas empresas aún están tratando de interpretar. La normativa no es de por sí un freno al desarrollo, pero requiere inversiones en habilidades legales y de gobernanza que se suman a las técnicas, elevando el coste total de entrada. Para las pequeñas y medianas empresas italianas, columna vertebral del tejido productivo nacional, el obstáculo no es solo económico o normativo, sino también organizacional: adoptar agentes capaces requiere una disposición a poner en duda procesos consolidados, una tolerancia a la experimentación y al error, y una capacidad de atraer perfiles técnicos que el mercado laboral italiano tiene dificultades para producir en cantidad suficiente. El dato del 2% de encuestados italianos en la muestra no debe leerse como índice de falta de interés, sino probablemente como reflejo de una participación aún periférica en conversaciones que se desarrollan en otros lugares.

El 2026 es, según los datos, el año en que muchas empresas pasarán de la experimentación a la producción. Es también el año en que algunas de estas preguntas empezarán a tener respuestas concretas, no siempre las que se esperarían. Mirar las cifras con honestidad, como este informe se esfuerza en hacer, es al menos un buen punto de partida.
