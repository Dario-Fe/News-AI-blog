---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-10-12
author: "Dario Ferrero"
---

# MiniCPM5-2B: ultrarrápido, excelente en código, menos en lo demás
![minicpm5-2b.jpg](minicpm5-2b.jpg)

*En las últimas semanas, el nombre MiniCPM5-2B ha recorrido muros de noticias, boletines y canales de Discord dedicados a la IA local con una frecuencia sospechosa para un modelo de apenas 2,5 mil millones de parámetros. Según la ficha oficial en [Hugging Face](https://huggingface.co/openbmb/MiniCPM5-2B), el modelo alcanza 97,1 en τ²-Bench Telecom, 69,1 en LiveCodeBench v6 y 86,5 en AIME, cifras que en la comparativa publicada por los propios autores superan a las de modelos 4B como Qwen3.5-4B. [Artificial Analysis](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b), que ha vuelto a ejecutar parte de las pruebas de forma independiente, confirma que se trata de la puntuación más alta en su Intelligence Index entre todos los modelos open-weight de menos de 4 mil millones de parámetros. La pregunta que vale la pena hacerse, antes de repetir la frase "compite con modelos cuatro veces más grandes", es sencilla: ¿compite de verdad, y en qué?*

## El laboratorio, en breve

La configuración de hardware es la misma descrita en la primera [entrega sobre Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1): AMD Ryzen 7700, 32 GB de RAM DDR5, GPU AMD Radeon RX 9060 XT con 16 GB de VRAM, y LM Studio como entorno. Para los detalles sobre cómo se instala y configura todo, os remito a aquel artículo.

Una nota metodológica importante: para esta prueba he utilizado deliberadamente la versión Q8_0 de 2,7 GB y no la Q4_K_M de 1,56 GB, con el fin de entender si las posibles limitaciones dependían de la cuantización o del propio modelo. La respuesta, como veremos, es que los límites son estructurales: incluso a la máxima calidad disponible en local, el modelo sufre en razonamiento abstracto, planificación multipaso y órdenes con restricciones complejas. La velocidad, en cambio, se mantiene excepcional en cualquier condición, lo que confirma que la eficiencia de su arquitectura no es mero marketing.

## Qué es MiniCPM5-2B

Detrás del modelo se encuentra OpenBMB, una comunidad de investigación de código abierto vinculada a la Universidad de Tsinghua y a ModelBest que, con la familia MiniCPM, ha superado los 50 millones de descargas acumuladas según Tencent News. No es un proyecto aficionado: el repositorio [OpenBMB/MiniCPM en GitHub](https://github.com/openbmb/minicpm) supera las 11.000 estrellas y la lista de entornos compatibles desde el primer día —desde vLLM hasta SGLang, pasando por nueve arquitecturas de chips distintas mediante FlagOS— da cuenta de una operación de escala industrial.

Su arquitectura es una variante densa estándar de `LlamaForCausalLM`, con 2,52 mil millones de parámetros totales (1,98 mil millones excluyendo los embeddings), 42 capas y atención GQA con 16 cabezas de consulta y 2 de clave-valor. El contexto nativo declarado es de 131.072 tokens y la licencia es Apache 2.0, lo que permite un uso comercial libre. Se trata de un modelo exclusivamente textual (sin capacidades de visión), con thinking mode activable mediante un parámetro en la plantilla de chat y tool calling nativo en formato XML.

Sin embargo, el verdadero valor añadido no reside únicamente en los pesos: OpenBMB ha publicado también la receta completa de entrenamiento, los conjuntos de datos UltraData, el marco de aprendizaje por refuerzo y la canalización de postentrenamiento basada en On-Policy Distillation, la cual fusiona las capacidades de dieciséis modelos expertos (cinco de ellos especializados en tareas de agentes) en un único punto de control final. Se trata del mismo enfoque, a menor escala, que ha hecho destacar a otros proyectos open-weight chinos en los últimos dos años.

Hay un detalle que conviene poner sobre la mesa desde el principio, porque revela más sobre la dinámica de expectación que cualquier gráfico: en la [World Artificial Intelligence Conference de Shanghái](https://www.orcarouter.ai/blog/minicpm5-2b-open-weights-release) del 19 de julio de 2026, ModelBest presentó el modelo con un contexto anunciado de 512.000 tokens y una lista de socios de hardware que incluía a AMD, Intel, MediaTek y Qualcomm. No obstante, los pesos publicados finalmente en septiembre configuran 131.072 tokens. No es un matiz menor si planeáis flujos de trabajo sobre documentos largos: conviene diseñar sobre 128K (que siguen siendo suficientes para un libro de unas 250 páginas) y no sobre los 512K anunciados en la conferencia.

## Qué promete el fabricante

La tabla comparativa publicada por OpenBMB contrapone MiniCPM5-2B con modelos de su misma categoría (LFM2.5-2.6B, Qwen3.5-2B, Gemma-4-E2B-it) y con modelos 4B más grandes (Qwen3.5-4B, granite-4.2-3B, Nemotron-3-Nano-4B). La media general declarada es de 53,9 frente a los 51,1 del mejor modelo 4B de la tabla. Sus puntos fuertes anunciados son la programación, el tool calling, las capacidades de agentes y las matemáticas: en SWE-bench Verified el modelo registra un 46,4 frente al 33,6 de Qwen3.5-4B, y en τ²-Bench Telecom alcanza un 97,1 frente al 92,1.

Los puntos débiles reconocidos por los propios autores en la tabla son igualmente claros: en conocimiento general (MMLU-Pro) se queda en un 70,8 frente al 78,0 de Qwen3.5-4B; en GPQA-Diamond desciende al 70,2 frente al 77,1; y en pruebas de código con agentes más complejas, como SWE-bench Pro (14,4 frente a 28,2) y Terminal-Bench v2.1 (8,6 frente a 25,8), la distancia con los modelos 4B se amplía considerablemente.

Aparece además un dato interesante sobre la credibilidad de la cifra más citada: el Intelligence Index de Artificial Analysis. En el anuncio de julio, OpenBMB comunicaba una puntuación de 17. Tras la actualización metodológica v4.2 de septiembre —que otorga mayor peso a los exámenes reservados e introduce nuevos componentes de agentes—, la puntuación oficial se ajustó a 15, manteniéndose aun así como la más alta entre los modelos open-weight de menos de 4B, según informa la propia [Artificial Analysis](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b). Por su parte, el análisis de [eesel AI](https://www.eesel.ai/blog/minicpm5-2b-review) señala una discrepancia entre esta evaluación independiente y una publicación en redes sociales del propio equipo de OpenBMB que mencionaba 23 puntos. Son cifras que reflejan la evolución de las metodologías de prueba, un matiz que conviene tener presente antes de dar por sentada la primera cifra que leáis.

En cuanto a la velocidad declarada, la documentación oficial no ofrece cifras certificadas para teléfonos inteligentes o Apple Silicon: las estimaciones que circulan en línea (10-12 tokens por segundo en móviles, 70-90 en Apple M4 Max) proceden de conversiones comunitarias no oficiales, como una adaptación a MLX que mide unos 96 tokens por segundo en decodificación sobre un M4 Max con 128 GB de memoria unificada. Debéis tomarlas, por tanto, como orientaciones aproximadas y no como marcas homologadas por el fabricante.
![grafico1.jpg](grafico1.jpg)
[Imagen obtenida del repositorio oficial en GitHub](https://github.com/openbmb/minicpm)

## Pruebas sobre el terreno

A continuación se detalla la evaluación práctica realizada con la versión Q8_0 de 2,7 GB, la máxima calidad ejecutable en local sin recurrir al formato BF16 completo.

**Razonamiento matemático**, nota 3/5, 105,66 tokens/s. El problema clásico de los dos trenes que parten de Milán y Roma se resolvió de forma correcta (encuentro a las 10:40), pero el proceso lógico fue innecesariamente enrevesado: el modelo calculó tiempos totales de viaje irrelevantes para la solución antes de plantear la ecuación adecuada, e introdujo caracteres fuera de lugar derivados de tokens mal gestionados. Llega al resultado correcto, pero lo explica de forma confusa: útil para un cálculo rápido, menos para comprender el procedimiento.

**Generación de código**, nota 4,5/5, 106,42 tokens/s. Al solicitarle una función en Python para la subsecuencia creciente más larga en tiempo O(n log n), el modelo generó un algoritmo óptimo utilizando un arreglo `tails` y búsqueda binaria, con código limpio, docstrings y un ejemplo funcional. Una errata menor en la redacción no empaña un rendimiento sobresaliente, en consonancia con sus notables resultados en SWE-bench Verified.

**Tool calling**, nota 4/5, 103,56 tokens/s. En la prueba que simulaba un asistente con las funciones `get_weather` y `send_email`, la secuencia de llamadas JSON fue precisa en su formato. Sin embargo, el modelo no gestionó la dependencia de estados: el cuerpo del correo contenía texto estático en lugar de hacer referencia a los datos meteorológicos obtenidos en el paso previo. Resulta adecuado para ejecuciones de un solo paso, pero muestra carencias en orquestaciones complejas.

**Razonamiento lógico abstracto**, nota 3,5/5, 106,21 tokens/s. Ante un acertijo de lógica con tres afirmaciones contradictorias, el modelo identificó la solución correcta. No obstante, la explicación fue desorganizada, presentó faltas de ortografía y omitió la notación de conjuntos que habría aportado rigor al razonamiento. Comprende la lógica de fondo, pero le cuesta exponerla con claridad.
![immagine1.jpg](immagine1.jpg)
*Captura de pantalla durante las pruebas de MiniCPM5-2B en LM Studio*

**Conocimiento general**, nota 2/5, 103,74 tokens/s. Al pedirle una síntesis sobre el Arte Renacentista en Italia y el Norte de Europa citando dos artistas por región, el modelo mencionó solo un artista por cada lado y atribuyó erróneamente a Hans Holbein una especialización en paisajismo —cuando Holbein es célebre por sus retratos y el paisaje como género autónomo se consolidó en la pintura holandesa del siglo XVII. Esta prueba evidencia la brecha de rendimiento reflejada en sus puntuaciones de MMLU-Pro y GPQA-Diamond.

**Procesamiento de contexto largo**, nota 4/5, 96,11 tokens/s. Al sintetizar un documento técnico en alemán sobre la propagación de autoridad en sistemas multiagente, el modelo generó un resumen preciso en cinco puntos. Captó adecuadamente conceptos complejos como el problema del "confused deputy" y sus implicaciones para desarrolladores, demostrando una notable capacidad de síntesis multilingüe sobre textos extensos.

**Planificación multipaso**, nota 3/5, 105,63 tokens/s. En un escenario con tres herramientas (`read_file`, `write_file`, `run_command`) para actualizar una clave de API en un archivo de configuración, el modelo omitió las herramientas indicadas. Ejecutó `sed` dentro de `run_command` en lugar de usar `write_file`, generando operaciones redundantes sin extraer los valores previos del resultado de `read_file`. Esta prueba confirma que las capacidades de agente requieren verificación en flujos de trabajo reales.

**Instrucciones con múltiples restricciones**, nota 2,5/5, 106,42 tokens/s. Al redactar un correo de disculpa sujeto a cinco restricciones simultáneas (longitud, fecha, porcentaje de descuento, tono y palabras prohibidas), el modelo cumplió cuatro de las cinco condiciones. Sin embargo, cometió errores de gramática, redactó una frase final confusa y omitió los saludos profesionales habituales.

## Tabla de resumen
![tabella1.jpg](tabella1.jpg)

Nota media: 3,3/5. Velocidad media de generación: ~104,2 tokens por segundo, una velocidad de inferencia sin precedentes entre los modelos de esta escala probados en este equipo.

## Dónde destaca, dónde flaquea

MiniCPM5-2B sobresale en tareas de programación de complejidad media, donde genera código de calidad cercana a la de modelos cuatro veces mayores. Gestiona con solvencia llamadas a herramientas de un solo paso y demuestra soltura al resumir documentos técnicos en varios idiomas. Al ocupar 2,7 GB en Q8 o 1,56 GB en Q4, se ejecuta sin problemas en equipos con recursos reducidos, manteniendo velocidades cercanas a los 105 tokens/s en GPU de consumo.

Por el contrario, no debéis confiar en él para consultas de conocimiento enciclopédico, donde aparecen alucinaciones fácticas. Muestra dificultades en razonamiento abstracto complejo —llegando a conclusiones correctas mediante explicaciones desordenadas— y no logra orquestar flujos de trabajo con agentes que requieran dependencias reales entre herramientas. El cumplimiento de instrucciones con restricciones múltiples constituye asimismo una limitación práctica.

## El veredicto: analizando la expectación

Lo que es cierto: para su escala de parámetros, MiniCPM5-2B representa un logro técnico notable. Su velocidad de procesamiento es real, la generación de código resulta destacable, el tool calling básico funciona correctamente y la publicación de recetas y conjuntos de datos por parte de OpenBMB beneficia al ecosistema de código abierto. Lo que es excesivo: las afirmaciones de que "compite con modelos cuatro veces más grandes" solo se sostienen en pruebas específicas de programación y tareas sencillas de agentes, pero no en conocimiento general ni en razonamiento abstracto. Lo que no es: un asistente de propósito general ni un todoterreno en miniatura.

Viene a la memoria una escena de *Chungking Express*, la película de Wong Kar-wai donde todo transcurre con rapidez pero los detalles se difuminan. MiniCPM5-2B comparte ese ritmo ágil y acelerado; pero cuando se le exige detenerse a razonar sobre matices complejos, la precisión disminuye. O dicho de forma más sencilla: se comporta como un automóvil deportivo ligero, ágil en trayectos urbanos, pero inadecuado para viajes largos con gran volumen de carga.

La evaluación del modelo en calidad Q8_0 ratifica estos hallazgos: las limitaciones observadas responden a la escala de sus 2,5B parámetros y no a artefactos derivados de la cuantización de pesos.

## A quién le resulta útil

Sus usuarios ideales son desarrolladores y equipos que busquen un motor ligero para autocompletado de código, validación de sintaxis o automatizaciones sencillas en hardware limitado —pudiendo combinarse con un modelo de mayor tamaño para tareas que exijan mayor profundidad de razonamiento. Resulta menos adecuado para quienes requieran un asistente multipropósito, acceso a conocimiento enciclopédico verificado o la orquestación autónoma de herramientas complejas. Para estas últimas necesidades, los modelos de 4B o 7B continúan siendo la opción más sólida.

La conclusión se alinea con la práctica habitual en ingeniería: empleadlo como lo que es —una herramienta rápida y especializada para tareas locales acotadas— y no como lo que los titulares de prensa pretenden presentar.
