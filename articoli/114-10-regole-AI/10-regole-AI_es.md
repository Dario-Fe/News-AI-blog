---
tags: ["Generative AI", "Security", "Business"]
date: 2026-04-15
author: "Dario Ferrero"
---

# 10 reglas para usar la IA en la empresa
![10-regole-AI.jpg](10-regole-AI.jpg)

*Partamos de un dato que sirve como espejo. Según el [informe McKinsey State of AI de noviembre de 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai), el 88 % de las organizaciones ya usa la IA en al menos una función de negocio. Sin embargo, en el mismo periodo, el Foro Económico Mundial y Accenture estimaron que menos del 1 % de estas han hecho plenamente operativo un enfoque de IA responsable, mientras que el 81 % permanece en las fases más embrionarias de madurez de gobernanza. El contrasentido está servido: casi todos usan la IA, casi nadie la gobierna de verdad.*

La confirmación más punzante llega de [una encuesta de EY de febrero de 2026](https://www.ey.com/en_us/newsroom/2026/03/ey-survey-autonomous-ai-adoption-surges-at-tech-companies-as-oversight-falls-behind) a 500 ejecutivos tecnológicos: el 45 % declaró que su organización ha sufrido en los últimos doce meses una fuga confirmada o sospechada de datos sensibles causada por empleados que usaban herramientas de IA generativa no autorizadas (ChatGPT, Claude, Gemini), a menudo con datos empresariales sensibles pegados dentro de un prompt, sin que el departamento de TI supiera nada. El [PEX Report 2025/26](https://www.aidataanalytics.network/data-science-ai/news-trends/less-than-half-of-businesses-have-an-ai-governance-policy) cierra el cuadro: solo el 43 % de las organizaciones tiene una política de gobernanza de la IA formal, mientras que casi un tercio, el 29 %, no tiene ninguna en absoluto.

Este artículo no pretende ser una lección desde arriba. Es más parecido a esa conversación útil que se tiene con un colega antes de una elección importante: algo que ayuda a entender dónde se están poniendo los pies, con ejemplos concretos y referencias verificables. Diez reglas, diez controles, diez errores que no se deben repetir.

## Antes de nada: la seguridad de la IA no es la seguridad de TI con un sombrero nuevo

Quienes trabajan en el ámbito de las TI saben que ya existe un arsenal consolidado de herramientas para la protección de los sistemas: cortafuegos, gestión de identidades, cifrado, evaluación de vulnerabilidades. El problema es que la IA introduce una superficie de riesgo que estas herramientas no ven.

Un modelo lingüístico puede producir respuestas falsas con la misma seguridad con la que produce las correctas, un fenómeno que en el campo se llama alucinación y que en contextos empresariales puede traducirse en decisiones equivocadas basadas en información inventada. Un sistema RAG (generación aumentada por recuperación) que accede a documentos internos puede ser manipulado a través de una instrucción oculta en un archivo aparentemente inocuo: es lo que el [OWASP LLM Top 10](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/) llama *prompt injection*, y que en 2025 ya ha sido explotada en entornos reales. Los datos que introducís en el sistema pueden ser memorizados, registrados o enviados a infraestructuras externas que no controláis.

El [NIST AI Risk Management Framework](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/), actualizado y cada vez más adoptado como referencia global, organiza la respuesta a estos riesgos en cuatro funciones: *Govern, Map, Measure, Manage* (Gobernar, Mapas, Medir, Gestionar). No son pasos secuenciales, son ruedas que giran de forma continua. Y es de aquí de donde conviene partir.

## La gobernanza antes que la tecnología

Antes de cualquier herramienta, se necesita una respuesta clara a tres preguntas: ¿quién decide qué se puede hacer con la IA en la empresa? ¿Quién responde si algo sale mal? ¿A quién se escala el problema?

ISO/IEC 42001, el estándar internacional para los sistemas de gestión de la IA publicado en diciembre de 2023 y ya adoptado como referencia por [KPMG](https://kpmg.com/ch/en/insights/artificial-intelligence/iso-iec-42001.html) y otros grandes actores de la consultoría, responde a estas preguntas con un concepto sencillo: se necesita un *AI Management System* con roles asignados, procesos documentados y ciclos de mejora continua. No es burocracia por amor al arte: es la forma de no encontrarse gestionando un incidente sin saber quién tiene la autoridad para apagar el sistema.

ISO/IEC 42001:2023 sigue siendo el estándar en vigor y la referencia certificable para los sistemas de gestión de IA. No obstante, cabe señalar que en abril de 2025 ISO publicó [ISO/IEC 42005:2025](https://www.aarc-360.com/understanding-iso-iec-42005-2025/), un estándar complementario dedicado específicamente a las evaluaciones de impacto de los sistemas de IA, una herramienta que ayuda a medir los efectos sociales e individuales de la IA a lo largo de todo el ciclo de vida, no solo los riesgos técnicos. No es obligatorio para obtener la certificación 42001, pero en la práctica cierra exactamente la brecha entre "tenemos una gobernanza" y "sabemos qué produce concretamente nuestro sistema en las personas".

### El problema invisible: la shadow AI

Antes incluso de hablar de clasificación de riesgos, hay un fenómeno que vale la pena nombrar explícitamente porque es el más extendido y el menos supervisado: la *shadow AI*. Funciona exactamente igual que la shadow IT de los años dos mil, cuando los empleados empezaron a usar Dropbox y Gmail personal para los archivos de trabajo porque las herramientas corporativas eran lentas, solo que las consecuencias son más inmediatas y menos reversibles.

Un empleado del sector financiero que pega una hoja de balance no consolidado en ChatGPT para que le ayude a escribir un comentario, un reclutador que sube los currículos de los candidatos a una herramienta externa para que le haga una preselección, un abogado que usa un LLM de consumo para redactar una cláusula contractual: en todos estos casos los datos salen de la infraestructura empresarial, terminan en servidores de terceros con políticas de retención que la empresa no ha negociado y potencialmente contribuyen al entrenamiento de modelos futuros. El dato de EY citado al inicio (el 45 % de fugas de datos desde herramientas no autorizadas) no es una excepción: es la norma silenciosa.

La respuesta no es prohibirlo todo, porque las prohibiciones no supervisadas no funcionan, como enseña la historia de la shadow IT. La respuesta es construir alternativas gobernadas que sean lo suficientemente buenas como para no empujar a las personas a buscar soluciones externas, acompañadas de una política clara sobre qué está permitido, con qué herramientas y bajo qué condiciones. Este es exactamente el punto de partida de la gobernanza de la IA.
![grafico1.jpg](grafico1.jpg)
[Imagen tomada de blog.getpolicyguard.com](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/)

## Regla 1 — Clasificad los casos de uso por nivel de riesgo, antes del despliegue

No todos los usos de la IA son iguales. Un chatbot interno para responder preguntas sobre las vacaciones es diferente de un sistema que evalúa a los candidatos de RR. HH. o que asigna una calificación de crédito a los clientes. El [NIST AI RMF](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/) usa la función *Map* exactamente para esto: crear un inventario de los sistemas de IA en uso y clasificarlos por nivel de impacto potencial.

La [Ley de IA de la UE](https://www.lw.com/en/insights/eu-ai-act-obligations-for-deployers-of-high-risk-ai-systems) (EU AI Act), con plena aplicabilidad a los usos de alto riesgo para agosto de 2027, identifica como sistemas de alto riesgo los usados para la selección y el seguimiento de los empleados, para el crédito y para la elaboración de perfiles de individuos. Para cada uno de estos casos, las obligaciones aumentan de forma significativa: evaluación de impacto, supervisión humana, registro de logs, notificación de incidentes.

Un ejemplo concreto: si vuestra empresa usa un LLM para apoyar a los reclutadores en la preselección de currículos, ese sistema es de alto riesgo para la Ley de IA de la UE. Si el mismo modelo se usa solo para generar borradores de descripciones de puestos de trabajo, el riesgo es mucho menor. La clasificación debe hacerse caso por caso, no por categoría genérica de herramienta.

## Regla 2 — Limitad los datos que entran en el sistema

El principio es el mismo que el de la dieta: no todo lo que podéis comer debéis comerlo. En el ámbito de la IA, se llama *minimización de datos*, y es el primer resguardo contra el riesgo de *fuga de datos*.

La guía publicada por [CISA, NSA y FBI en mayo de 2025](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) es explícita: las organizaciones deben clasificar los datos antes de usarlos en los sistemas de IA, aplicar controles de acceso rigurosos y no asumir nunca que los conjuntos de datos están limpios y libres de contenido malicioso. La misma guía introduce el concepto de *procedencia de los datos*: saber de dónde vienen los datos con los que el modelo trabaja no es una formalidad, es un requisito de seguridad.

En la práctica: estableced por política qué categorías de datos no pueden entrar nunca en un sistema de IA (secretos industriales, credenciales, datos personales no estrictamente necesarios, información sujeta a vínculos normativos). Un ejemplo útil para el sector financiero: los datos de balance no consolidado no deberían usarse nunca como contexto en un chatbot empresarial genérico accesible a toda la organización.

## Regla 3 — Gobernad a proveedores, modelos e integraciones

La IA empresarial rara vez es un sistema monolítico que controléis por entero. Normalmente es un ensamblaje: una plataforma SaaS, un modelo fundacional de un tercero, complementos (plugins), herramientas externas conectadas a través de API. Cada uno de estos componentes es un punto de entrada potencial para riesgos que no habéis evaluado directamente.

La [guía conjunta CISA de 2025](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) dedica una sección entera a los riesgos de la *cadena de suministro de datos*, con una atención especial al *envenenamiento de datos* (data poisoning): la manipulación de los datos de entrenamiento por parte de actores maliciosos, que puede ocurrir a través de conjuntos de datos recopilados de la web, dominios caducados recomprados a propósito o inyecciones de ejemplos falsos en los corpus usados para el ajuste fino (fine-tuning).

El control práctico es una evaluación del proveedor estructurada: para cada proveedor de componentes de IA, verificad dónde se registran los logs de las interacciones, si vuestros datos se usan para entrenar modelos y cómo, y qué garantías contractuales existen sobre el tratamiento de los datos. ISO/IEC 42001 prevé explícitamente la *supervisión de proveedores externos* como requisito del sistema de gestión.

## Regla 4 — Probad el sistema antes del lanzamiento

Ningún sistema de IA debería entrar en producción sin haber pasado por un ciclo de pruebas que incluya escenarios de abuso. La Ley de IA de la UE, para los sistemas de alto riesgo, lo exige explícitamente como parte del *sistema de gestión de calidad*: verificaciones sobre precisión, robustez, sesgos y comportamientos inesperados antes de la puesta en marcha.

El *red teaming*, es decir, la simulación de ataques y usos indebidos por parte de un equipo interno o externo, no es una práctica reservada a las grandes empresas tecnológicas. Herramientas como [Promptfoo](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/) permiten automatizar pruebas basadas en el OWASP LLM Top 10 incluso sin un equipo de seguridad dedicado.

Un ejemplo concreto para el servicio al cliente: antes de lanzar un asistente conversacional que tenga acceso a los datos de los clientes, verificad sistemáticamente si responde de forma diferente a usuarios con nombres de distinto origen cultural (prueba de sesgo), si revela información sobre usuarios distintos al autenticado (prueba de fuga) o si puede ser inducido a ignorar las instrucciones del sistema con prompts elaborados (prueba de jailbreak).

## Regla 5 — Protegeos de la inyección de prompts y de resultados peligrosos

Esta es la regla más técnica, pero vale la pena entenderla porque también es la más subestimada. La *inyección de prompts* (prompt injection) funciona así: un usuario, o un contenido externo que el modelo lee, introduce instrucciones que sobrescriben las originales del sistema. El modelo no distingue entre las instrucciones de su operador y las inyectadas: las ejecuta ambas y, a menudo, prefiere las más recientes.

El [OWASP LLM Top 10](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/), el documento de referencia para la seguridad de los modelos lingüísticos, indica este como el riesgo número uno. Las contramedidas operativas incluyen: separar arquitectónicamente las instrucciones del sistema de las entradas de los usuarios, limitar las herramientas a las que el modelo tiene acceso (un asistente que responde preguntas sobre productos no necesita poder enviar correos electrónicos o modificar bases de datos) y aplicar filtros sobre los resultados (outputs) para interceptar respuestas que contengan datos estructurados sensibles.

La era agéntica ya ha comenzado y se está más allá de los chatbots y los copilotos; los agentes no se limitan a responder a una pregunta, sino que ejecutan secuencias de acciones, navegan por sitios, leen y escriben archivos, llaman a API, envían correos electrónicos, con una supervisión humana mínima o nula. El [informe Deloitte State of AI in the Enterprise de enero de 2026](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html) estima que solo 1 de cada 5 empresas tiene hoy un modelo maduro de gobernanza para los agentes de IA autónomos, mientras que su uso está destinado a crecer claramente en los próximos dos años.

En este contexto, el principio del menor privilegio deja de ser una buena práctica y se convierte en una condición de supervivencia: un agente con acceso ilimitado a herramientas, datos y canales de comunicación puede producir daños difícilmente reversibles, de forma rápida y automática. Antes de desplegar cualquier sistema agéntico, la pregunta que hay que hacerse es: si este agente malinterpreta la instrucción de la forma más razonablemente equivocada posible, ¿qué sucede?
![grafico2.jpg](grafico2.jpg)
[Imagen tomada de mckinsey.com](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)

## Regla 6 — Mantened un control humano real, no solo formal

Existe una versión vacía de la *supervisión humana* (human oversight): ponéis una firma al pie de un documento que dice que un humano ha supervisado la decisión, aunque en realidad nadie haya controlado nada de verdad. La Ley de IA de la UE, en los artículos dedicados a las obligaciones de los usuarios (deployers) de sistemas de alto riesgo, es específica en este punto: la supervisión humana debe ser sustancial, no decorativa. Los encargados de la supervisión deben tener la competencia para interpretar los resultados, la capacidad de interrumpir el sistema y la autoridad para hacerlo.

La distinción práctica que se debe establecer por escrito en cada proceso crítico es esta: la IA sugiere, el humano decide. No "la IA decide y el humano puede oponerse", porque el coste psicológico de la oposición a un sistema automático ya ha sido documentado por la investigación: las personas tienden a aceptar las sugerencias de los sistemas automáticos incluso cuando tienen dudas, especialmente bajo presión de tiempo. En el ámbito de RR. HH., finanzas, cumplimiento (compliance) y salud, esta dinámica no es aceptable.

## Regla 7 — Supervisad el sistema después de la puesta en marcha

El lanzamiento no es la meta: es la salida. Los sistemas de IA se degradan con el tiempo por razones que no siempre son obvias: el lenguaje de los usuarios cambia, los datos de entrada se desplazan respecto a la distribución original (es lo que la [guía CISA](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) llama *deriva de datos* o data drift), los patrones de abuso evolucionan. Se necesita un sistema de registro (logging) que registre muestras de los resultados, alertas automáticas cuando las métricas de calidad se desvíen de la línea base y un proceso de respuesta ante incidentes que responda a la pregunta: si el sistema hace algo mal esta noche, ¿quién se da cuenta y en cuánto tiempo?

La Ley de IA de la UE exige la conservación de los registros durante al menos seis meses para los sistemas de alto riesgo, y la notificación a las autoridades en caso de incidentes graves. ISO/IEC 42001 prevé revisiones periódicas del sistema de gestión. El NIST AI RMF, en la función *Manage*, insiste en una supervisión activa que alimente el ciclo de mejora.

## Regla 8 — Documentadlo todo, de verdad

Si no está documentado, no es gobernable. Es una frase que suena obvia pero que en la operatividad diaria se ignora sistemáticamente. La documentación de un sistema de IA no es el manual de uso: es el conjunto de políticas aprobadas, evaluaciones de riesgo, resultados de las pruebas, versiones del modelo en producción, decisiones tomadas y motivaciones.

Esta documentación sirve para tres cosas concretas: demostrar el cumplimiento normativo en caso de auditoría, entender qué ha cambiado cuando algo deja de funcionar y mejorar el sistema con el tiempo aprendiendo de los errores. El formato no es prescriptivo, pero debe ser rastreable y accesible para quien lo necesite. Un registro de las versiones del modelo en producción, mantenido en un archivo Excel compartido y actualizado manualmente, ya vale más que nada.

Para quienes quieran estructurar este paso de forma rigurosa, [ISO/IEC 42005:2025](https://www.aarc-360.com/understanding-iso-iec-42005-2025/) ofrece un marco específico para documentar el impacto de los sistemas de IA, incluidos los usos sensibles, los abusos previsibles y las aplicaciones no intencionadas, mapeado directamente sobre los controles de ISO/IEC 42001.

## Regla 9 — Formad a las personas que usan el sistema

El error humano sigue siendo una de las superficies de riesgo más amplias, y la formación es el resguardo más económico contra él. Pero hay un dato que transforma este principio de sentido común genérico en una palanca estratégica medible: según el [informe de CSA y Google Cloud de diciembre de 2025](https://cloudsecurityalliance.org/blog/2025/12/18/ai-security-governance-your-maturity-multiplier), el 65 % de las organizaciones con una gobernanza de la IA completa ya forma a su personal sobre las herramientas de IA, frente a solo el 27 % de aquellas con políticas parciales y el 14 % de las que aún están en fase de desarrollo. No es un detalle: la formación es uno de los indicadores más discriminatorios entre quienes gobiernan la IA de verdad y quienes se limitan a escribir políticas que nadie lee.

La formación sobre la IA no es un curso de una hora obligatorio en el que todos hacen clic sin mirar: debe ser específica para cada rol y debe abordar tres cosas distintas. La primera es el uso correcto de las herramientas: cómo se usa el sistema, qué se puede preguntar, qué no se debe introducir nunca. La segunda es el reconocimiento de los límites: los empleados deben saber que los modelos lingüísticos pueden equivocarse con gran seguridad, y deben tener la autoridad para no confiar en el resultado cuando tengan dudas fundadas. La tercera es la gestión de incidentes: qué hacer cuando algo sale mal, a quién informarlo, cómo documentarlo. La Ley de IA de la UE exige explícitamente *formación en alfabetización en IA* (AI literacy training) para todos los usuarios de sistemas de alto riesgo: no es un detalle normativo, es sentido común operativo con una fecha de vencimiento.

## Regla 10 — Actualizad las reglas con el tiempo

La IA es quizás el único campo en el que las instrucciones operativas envejecen más rápido que los sistemas que gobiernan. Un marco de gobernanza escrito a principios de 2024 no tiene en cuenta las capacidades agénticas de los modelos actuales, los nuevos vectores de ataque documentados en 2025 o los plazos normativos de la Ley de IA de la UE que se acercan. Tanto el [NIST AI RMF](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/) como [ISO/IEC 42001](https://kpmg.com/ch/en/insights/artificial-intelligence/iso-iec-42001.html) están construidos en torno al principio de la mejora continua: las políticas deben revisarse al menos una vez al año, y cada incidente significativo debe desencadenar una revisión inmediata de los controles relacionados.

La cadencia mínima practicable es esta: revisión anual del marco general, revisión semestral de las políticas sobre datos, revisión inmediata tras cada incidente o cambio relevante en los modelos en uso. No es un ciclo pesado: es la diferencia entre una gobernanza viva y un documento que nadie actualiza.

## Para concluir

Retomando una metáfora de *Ghost in the Shell*, no la cinematográfica de Hollywood, sino el manga original de Masamune Shirow, el problema nunca es el sistema en sí, sino quién lo ha construido y con qué intención. La IA empresarial funciona cuando quien la ha adoptado sabe exactamente qué quiere obtener, conoce los riesgos que conlleva y ha construido una estructura capaz de responder cuando las cosas no van como se preveía.

La pregunta que debéis haceros no es "¿estamos usando la IA?". Casi con toda seguridad, sí. La pregunta es: "¿sabemos con qué reglas?".
