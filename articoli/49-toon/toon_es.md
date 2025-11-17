---
tags: ["Research", "Applications", "Training"]
date: 2025-11-17
author: "Dario Ferrero"
---

# TOON reescribe las reglas de los datos para la era de la IA. ¿Qué será de JSON?
![toon.jpg](toon.jpg)


*Hay una paradoja en la economía de la inteligencia artificial que pocos notan hasta que miran la factura. Cada vez que enviamos datos a GPT, Claude o Gemini, pagamos por cada uno de los caracteres. No por la complejidad de la solicitud, no por la inteligencia de la respuesta, sino por la verbosidad del formato. ¿Esas llaves que hacen que JSON sea tan familiar? Cuestan dinero. ¿Las comillas que delimitan cada clave? Tokens preciosos. ¿Los dos puntos que separan las claves y los valores? Otros céntimos que se van volando, multiplicados por millones de llamadas a la API.*

Cuando Johann Schopplich publicó [TOON (Token-Oriented Object Notation)](https://github.com/toon-format/toon) a principios de 2025, la reacción inicial de la comunidad fue la que acompaña a todas las ideas simples pero geniales: "¿Por qué demonios no se me ocurrió a mí?". Como el minimalismo japonés aplicado a la serialización de datos, TOON elimina todo lo que no es necesario. Sin llaves, sin comillas superfluas, sin repeticiones obsesivas de las mismas claves. Solo la esencia del dato, limpia como un haiku.

## El coste invisible de las llaves

JSON nació en una época en la que los ordenadores hablaban principalmente entre ellos. Douglas Crockford lo extrajo de JavaScript como un subproducto afortunado, primando la legibilidad humana y la compatibilidad multiplataforma sobre la eficiencia. Durante años, este compromiso funcionó de maravilla. Los bytes extra necesarios para representar un objeto con todas sus decoraciones sintácticas eran irrelevantes en comparación con la simplicidad del análisis y la familiaridad del formato.

Pero la llegada de los Modelos de Lenguaje Grandes ha cambiado las reglas del juego. Cuando los costes de las API se calculan por millón de tokens, de repente esas llaves ya no son inofensivas convenciones sintácticas. Se convierten en una ineficiencia económica medible. JSON puede consumir el doble de tokens que otros formatos para representar los mismos datos, y esto sin tener en cuenta que los modelos han sido entrenados precisamente con montañas de JSON, lo que lo hace paradójicamente menos eficiente para el procesamiento.

Consideremos un ejemplo real. Una lista de cien repositorios de GitHub con metadatos completos: estrellas, forks, descripciones, marcas de tiempo. En formato JSON, esta estructura consume 15.145 tokens. ¿La misma información idéntica en TOON? 8.745 tokens. Una reducción del 42,3%. No estamos hablando de compresión con pérdida ni de trucos de magia. Es la misma información, bit a bit reversible, simplemente representada de una manera más inteligente.

Las matemáticas se vuelven aún más brutales con los datos temporales. Ciento ochenta días de métricas web (visualizaciones, clics, conversiones, ingresos) requieren 10.977 tokens en JSON frente a 4.507 en TOON, un ahorro del 58,9%. Cuando multiplicas estas cifras por miles de solicitudes diarias en una aplicación empresarial, la diferencia entre un proyecto sostenible y uno que quema el presupuesto se vuelve tangible.

## Cuando menos es más

La intuición central de TOON es de una sencillez abrumadora: cuando tienes matrices uniformes de objetos con los mismos campos, ¿por qué repetir las claves para cada uno de los elementos? Es como si cada fila de una hoja de cálculo de Excel tuviera que incluir el encabezado de la columna. Ineficiente y redundante.

TOON toma prestada la indentación de YAML para las estructuras anidadas y el formato tabular de CSV para las matrices uniformes, y luego optimiza ambos para el contexto específico de los Modelos de Lenguaje Grandes. El resultado es un formato que parece obvio una vez que se ve, pero que requiere repensar algunas suposiciones fundamentales sobre cómo representamos los datos.

Una matriz de usuarios en JSON clásico repite obsesivamente la misma estructura:
![json-format.jpg](json-format.jpg)

TOON declara la estructura una sola vez en el encabezado y luego enumera solo los valores:
![toon-format.jpg](toon-format.jpg)

El marcador `[2]` comunica explícitamente la longitud de la matriz, mientras que `{id,name,role}` define el esquema. Cada fila posterior contiene solo los datos en bruto, separados por comas. Es una elegancia funcional en el sentido Bauhaus del término: la forma sigue a la función, cero adornos superfluos.

Esta economía sintáctica se manifiesta en tres estrategias complementarias. En primer lugar, la indentación sustituye a las llaves para los objetos anidados. En segundo lugar, las cadenas se entrecomillan solo cuando es estrictamente necesario para evitar ambigüedades (espacios iniciales o finales, caracteres de control, valores que podrían confundirse con booleanos o números). En tercer lugar, el formato tabular para matrices homogéneas transforma las repeticiones verbales en filas compactas al estilo de CSV.

¿El resultado? TOON suele lograr una reducción del 30-60% en el consumo de tokens en comparación con JSON en conjuntos de datos estructurados. Y no es solo una cuestión de contar los caracteres ahorrados. Es una diferencia que se traduce directamente en una reducción de los costes operativos, ventanas de contexto más amplias disponibles para datos adicionales y tiempos de respuesta más rápidos.

## La geometría del ahorro

Los benchmarks oficiales del proyecto TOON cuentan una historia interesante sobre las condiciones que amplifican o reducen las ventajas del formato. No es magia universal, es geometría aplicada a la estructura de los datos.

El punto óptimo, ese punto dulce donde TOON brilla más, son las matrices uniformes de objetos con valores primitivos. Resultados de consultas a bases de datos, exportaciones de CSV, datos analíticos temporales. Cuanto más idénticas sean tus filas en su estructura, más podrá TOON comprimir la sobrecarga sintáctica declarando el esquema una sola vez.

En las pruebas realizadas con cuatro modelos diferentes (GPT-5 Nano, Claude Haiku, Gemini Flash, Grok) a través de 154 preguntas de recuperación de datos, TOON obtuvo una precisión media del 70,1% utilizando 4.678 tokens, frente al 65,4% de JSON, que consumía 8.713. No solo ahorro económico, sino también mayor precisión en las respuestas. La estructura explícita (longitud de las matrices, declaración de los campos) ayuda a los modelos a analizar y validar los datos de forma más fiable.

Pero los resultados varían significativamente entre los modelos. GPT-5 Nano mostró una precisión del 96,1% con TOON, mientras que Claude Haiku se quedó en el 48,7%. Esta disparidad sugiere que el entrenamiento importa: los modelos expuestos predominantemente a JSON durante el entrenamiento podrían tener dificultades inicialmente con formatos alternativos, independientemente de su eficiencia teórica.

El problema del entrenamiento no es trivial. Los LLM actuales han sido alimentados con miles de millones de tokens de JSON procedentes de API, configuraciones, conjuntos de datos públicos. TOON nació en 2025, por lo que los modelos más recientes han visto relativamente poco de este formato en sus corpus de entrenamiento. Es un problema clásico de "bootstrap": el formato es más eficiente, pero el ecosistema aún debe adaptarse.

Es interesante observar cómo las pruebas también revelan los límites de TOON. Para estructuras profundamente anidadas o datos no uniformes, los beneficios se reducen drásticamente. Un objeto con campos opcionales que aparecen esporádicamente, o árboles jerárquicos con muchos niveles de anidación, podrían resultar más legibles e incluso más eficientes en JSON. TOON no se aplica bien a datos profundamente anidados o no uniformes, donde JSON puede resultar más eficiente.
![toon-schema.jpg](toon-schema.jpg)
[Imagen extraída del repositorio oficial de GitHub](https://github.com/toon-format/toon)

## Dónde funciona (y dónde no)

Separar el bombo de la realidad práctica requiere franqueza sobre los casos de uso. TOON no es "el nuevo JSON" en el sentido de un reemplazo universal. Es una herramienta especializada para un problema específico: optimizar la transferencia de datos estructurados hacia y desde los Modelos de Lenguaje Grandes.

Los escenarios ganadores son claros. ¿Estás construyendo una canalización RAG que envía cientos de registros de productos a un LLM para generar descripciones? TOON reduce los costes. ¿Tienes una aplicación que procesa miles de filas de análisis diarios a través de GPT para extraer información? Ahorro inmediato. ¿Necesitas pasar los resultados de consultas a bases de datos con cientos de usuarios, pedidos o transacciones a Claude para su análisis? TOON nació para esto.

El formato destaca cuando la estructura es plana y uniforme, cuando los volúmenes son altos, cuando los costes de los tokens representan una partida presupuestaria significativa. Para casos de uso como la generación de calendarios editoriales, listas de productos, tablas de usuarios, filas de análisis, donde el presupuesto de tokens o la ventana de contexto son limitaciones reales, TOON ofrece ventajas concretas y medibles.

Pero existen territorios donde JSON mantiene la ventaja. Los datos muy anidados e irregulares, donde la estructura varía significativamente entre registros, no se benefician del formato tabular de TOON. Los objetos complejos con muchos campos opcionales se vuelven verbosos incluso en TOON cuando tienes que gestionar la ausencia de valores o estructuras variables.

Luego está la cuestión del ecosistema. JSON tiene décadas de herramientas maduras: depuradores, formateadores, validadores, bibliotecas en todos los lenguajes imaginables. TOON lanzó su primera versión en 2025 y, aunque tiene implementaciones en TypeScript, Python, Go, Rust, Java, C++, PHP, Ruby, Swift, Elixir, Dart, Clojure, Crystal y otros lenguajes, el ecosistema aún es joven. JSON tiene décadas de herramientas, mientras que TOON es más reciente con un ecosistema más pequeño.

La depuración es más complicada. Cuando algo se rompe en producción y tienes que inspeccionar una carga útil de TOON, no puedes simplemente abrir las herramientas de desarrollo del navegador y hacer "pretty-print". Tienes que convertir de nuevo a JSON, identificar el problema y luego volver a convertir. Añade fricción al flujo de trabajo de desarrollo, especialmente en los equipos que aún no están familiarizados con el formato.

La adopción empresarial conlleva cuestiones organizativas que van más allá de la pura técnica. Convencer a un equipo de que cambie el formato de los datos requiere la aceptación a varios niveles. Los desarrolladores deben aprender la nueva sintaxis. El código heredado debe actualizarse o debe coexistir con capas de conversión. Los procesos de CI/CD deben adaptarse. Convencer a los equipos y a la dirección de que adopten un nuevo formato para una reducción de costes del 30-60% suena fácil sobre el papel, pero en la práctica siempre hay resistencia al cambio.

La estrategia más pragmática, la que están adoptando los equipos que experimentan con TOON, es quirúrgica en lugar de holística. No sustituyen JSON en toda la pila. Mantienen JSON como formato interno para el almacenamiento, las API externas, los contratos entre servicios. Usan TOON exclusivamente como una capa de optimización para la comunicación con los LLM, donde la eficiencia de los tokens realmente importa. El enfoque óptimo para la mayoría de las organizaciones combina ambos: JSON como estándar interno para la compatibilidad y TOON para la optimización específica de los LLM.

Convierten en el momento necesario, en los puntos de alto tráfico donde el ahorro se multiplica: puntos finales que generan miles de llamadas a LLM al día, canalizaciones por lotes que procesan grandes volúmenes, aplicaciones en tiempo real donde la latencia reducida marca la diferencia en la experiencia del usuario.

## El verdadero precio de la eficiencia

Reducir el consumo de tokens no es solo una optimización económica. Es también una cuestión medioambiental que la industria tecnológica todavía tiene dificultades para abordar abiertamente. Cada token procesado requiere ciclos de GPU, cada ciclo consume energía, cada kilovatio-hora contribuye a la huella de carbono de los centros de datos.

La creciente demanda de IA generativa ya ha aumentado el consumo energético global de la computación, y optimizar el uso de los tokens se está convirtiendo en una nueva frontera no solo para la eficiencia, sino para la sostenibilidad. Cuando TOON reduce en un 50% los tokens necesarios para representar un conjunto de datos, también está reduciendo aproximadamente la mitad de la energía necesaria para procesar esa solicitud. Multiplicado por millones de llamadas a la API a través de miles de aplicaciones, el impacto agregado no es despreciable.

Pero la eficiencia también tiene costes ocultos, de otra naturaleza. TOON introduce complejidad cognitiva para los desarrolladores. Tienes que aprender las reglas para entrecomillar las cadenas (¿cuándo son necesarias las comillas? ¿qué pasa con los delimitadores alternativos?). Tienes que entender cuándo usar el formato tabular frente al formato de lista. Tienes que gestionar casos límite como matrices de matrices u objetos con campos opcionales dispersos.

La curva de aprendizaje no es pronunciada, pero existe. Para equipos pequeños o proyectos con volúmenes modestos de llamadas a LLM, el tiempo invertido en el aprendizaje y la implementación podría superar los ahorros económicos. Para aplicaciones a pequeña escala que hacen 100 llamadas a LLM al día, el tiempo de ingeniería para implementar TOON probablemente no valga la pena el ahorro.

Luego está la cuestión de la madurez del formato. La especificación de TOON se encuentra actualmente en la versión 1.4, con pruebas de conformidad independientes del lenguaje que ayudan a los implementadores a garantizar la compatibilidad multiplataforma. Pero es un formato con menos de un año de vida en el mundo real. Todavía no sabemos qué casos límite surgirán con el uso masivo en producción, qué patrones resultarán problemáticos, qué optimizaciones adicionales serán necesarias.

El proyecto ha publicado pruebas de conformidad públicas y mantiene una especificación formal en GitHub, señales positivas de una gobernanza seria. Pero la adopción a gran escala revelará inevitablemente problemas que las pruebas unitarias no capturan. Es el clásico compromiso entre ser un "early adopter" (beneficios inmediatos, riesgo de estabilidad) y esperar la maduración (menor riesgo, pero costes más altos mientras tanto).

El aspecto más intrigante, quizás, es cultural más que técnico. TOON nos obliga a pensar de forma diferente sobre la representación de los datos. Durante treinta años hemos considerado JSON como el formato "natural" para los datos estructurados, hasta el punto de que a menudo pensamos directamente en términos de objetos con claves y valores entre llaves. TOON requiere un cambio de perspectiva: pensar primero en la forma de los datos (¿es tabular? ¿anidado? ¿uniforme?) y luego en la representación óptima.

Al igual que la programación funcional, que te enseña a pensar en términos de transformaciones inmutables en lugar de mutaciones de estado, o como la arquitectura RISC, que privilegia las instrucciones simples y numerosas en lugar de unas pocas instrucciones complejas, TOON promueve una mentalidad diferente. La elegancia de la sustracción en lugar de la acumulación de características.

TOON no sustituirá a JSON, al igual que Markdown no ha sustituido a HTML ni YAML ha eliminado a XML. Cada formato ha encontrado su propio nicho, su propio contexto donde los compromisos específicos tienen sentido. JSON seguirá siendo el estándar para las API, las configuraciones, el almacenamiento. Pero para ese dominio específico y creciente que es la comunicación con los Modelos de Lenguaje Grandes, TOON ofrece una alternativa racional basada en principios sólidos.

La idea detrás de TOON es esa clásica intuición que parece obvia solo después de que alguien la ha tenido: si los modelos pagan por cada token, ¿por qué seguir usando un formato diseñado hace cuarenta años para resolver problemas diferentes? Es el mismo tipo de intuición que llevó al nacimiento de protobuf para sustituir a XML en las comunicaciones de Google, o del propio JSON como una alternativa más ligera a SOAP.

La pregunta relevante para los desarrolladores y los líderes tecnológicos no es "¿Sustituirá TOON a JSON?", sino "¿Se benefician mis casos de uso específicos de la optimización de tokens?". Si trabajas con grandes volúmenes de datos estructurados uniformes que pasan por LLM, si los costes de la API son una partida importante de tu presupuesto operativo, si la ventana de contexto limitada es una limitación real en tus aplicaciones, entonces TOON merece un experimento serio. Convierte un punto final de alto tráfico, mide el ahorro real, evalúa si la complejidad añadida vale la pena los beneficios concretos.

Si, por el contrario, haces llamadas esporádicas con cargas útiles pequeñas, si el equipo es reducido y debe concentrar su tiempo en las características en lugar de en las optimizaciones, si los datos son predominantemente anidados e irregulares, entonces JSON sigue siendo la opción pragmática. La optimización prematura, como nos enseñó Knuth, es la raíz de todos los males. O al menos del 97% de ellos.

El futuro de TOON dependerá de dos factores: la rapidez con la que el ecosistema de LLM evolucione sus modelos para reconocer y optimizar el formato, y la eficacia con la que la comunidad logre crear herramientas maduras que faciliten la adopción. Si dentro de dos años los principales proveedores de LLM incluyen TOON como un formato nativo compatible junto a JSON en sus SDK, si los editores y depuradores integran el resaltado de sintaxis y la validación para TOON, si los frameworks RAG y las bibliotecas de orquestación de IA lo soportan de forma nativa, entonces la adopción crecerá de forma orgánica.

Mientras tanto, TOON sigue siendo lo que siempre ha sido: una idea simple pero genial que te hace preguntarte por qué no se te ocurrió a ti. Y quizás, en su elegancia minimalista, hay una lección más amplia para toda la industria tecnológica: a veces la innovación no consiste en añadir complejidad, sino en restarla.
