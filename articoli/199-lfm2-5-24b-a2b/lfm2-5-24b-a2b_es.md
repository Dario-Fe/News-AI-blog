---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-11-02
author: "Dario Ferrero"
---

# LFM2.5-24B-A2B en local: rápido pero no generalista
![lfm2-5-24b-a2b.jpg](lfm2-5-24b-a2b.jpg)

*Un laboratorio de Cambridge, Massachusetts, ha decidido hacer razonar en "voz alta" a un modelo que, por cada palabra producida, trabaja tanto como uno de dos mil millones de parámetros. En esta frase reside toda la apuesta de LFM2.5-24B-A2B: capacidad de gigante, esfuerzo de peso pluma y un pensamiento explícito antes de cada respuesta. Queda por ver si esta apuesta se gana en un ordenador doméstico estándar o únicamente en los gráficos de quienes lo han construido. El estilo es el de siempre, sin tecnicismos académicos y con los pros y los contras, separando lo que declara la empresa de lo que hemos medido nosotros.*

Liquid AI lanzó el modelo el 13 de octubre de 2026 como el miembro más grande y último de la familia LFM2.5, tal como se relata en la [publicación de lanzamiento](https://www.liquid.ai/blog/lfm2-5-24b-a2b). La empresa tiene su sede en Cambridge, Massachusetts, y fue fundada en 2023, según la [ficha de LLM Reference](https://www.llmreference.com/model/lfm-2.5-24b-a2b).

El propio nombre encierra su secreto. Los veinticuatro mil millones representan los parámetros totales, pero solo se activan unos 2,45 mil millones por cada token, es decir, por cada fragmento de palabra. Imaginad un edificio con sesenta y cuatro especialistas por planta, donde para cada palabra solo se convoca a cuatro de ellos. Todos deben estar en el edificio, por lo que la memoria se paga íntegramente. Sin embargo, solo unos pocos trabajan al mismo tiempo, de modo que el coste de cálculo resulta muy bajo. [TechRepublic](https://www.techrepublic.com/article/news-liquid-ai-lfm25-24b-a2b-local-ai/) lo aclara: activar menos parámetros reduce la carga de cálculo, pero no otorga al modelo los requisitos de memoria de uno de dos mil millones.

La pregunta clave de la prueba es si esta arquitectura "dispersa" se convierte en una ventaja concreta sobre hardware doméstico.

## El banco de pruebas

El laboratorio es el ya conocido: AMD Ryzen 7700, 32 GB de RAM DDR5, tarjeta gráfica AMD Radeon RX 9060 XT de 16 GB y LM Studio, descritos en el [primer artículo de la serie](https://aitalk.it/it/qwen3.5-locale-puntata1.html). El modelo probado es la versión UD-Q4_K_XL en formato GGUF, una cuantización dinámica de 4 bits de Unsloth que ocupa unos 15,4 GB. En una tarjeta de 16 GB, el margen es mínimo. Es plausible que parte del trabajo acabe en la memoria del sistema, pero es una hipótesis no verificada que conviene tener presente al leer las velocidades.

Como referencia para la generación, Liquid indica una temperatura de 0,1, top_k de 50 y penalización de repetición de 1,05, según se indica en la [página oficial del modelo](https://docs.liquid.ai/lfm/models/lfm25-24b-a2b). Una segunda referencia procede de una [prueba independiente de memoria](https://pasqualepillitteri.it/news/25727/lfm25-24b-a2b-ram-liquid-ai) en un portal tecnológico menor: una versión de 4 bits alcanzó un pico de 14,5 GB con un prompt de unos 2.600 tokens. Al tratarse de otra cuantización, la cifra es solo orientativa.

## Dentro de la arquitectura híbrida

La [documentación](https://docs.liquid.ai/lfm/models/lfm25-24b-a2b) describe cuarenta capas, de las cuales treinta son de convolución corta "gated" y diez de GQA (Atención con Consultas Agrupadas), con sesenta y cuatro expertos por bloque y enrutamiento top-4. En términos sencillos, las convoluciones analizan únicamente el entorno inmediato de cada palabra con un coste reducido, mientras que la atención las compara con todo el texto, siendo más costosa pero imprescindible. Combinarlas responde a una decisión de eficiencia, no a una moda.

Respecto a su predecesor, la ventana de contexto se amplía de 32.768 a 131.072 tokens y el vocabulario se duplica de 65.000 a 128.000 entradas mediante una expansión "in situ" del tokenizador, pensada para alfabetos no latinos. El proceso de entrenamiento es extenso: el preentrenamiento sube de 17 a 33 billones (trillions) de tokens, seguidos de 2 billones a 32K de contexto y 300.000 millones a 131K, concluyendo con un postentrenamiento en cinco fases. La última consiste en un aprendizaje por refuerzo integrado en herramientas de agentes reales como OpenClaw, Hermes Agent, Pi y OpenCode, según explica el [artículo en Hugging Face](https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b).

Una elección de diseño fundamental distingue a este modelo de su predecesor: es un modelo dedicado exclusivamente al razonamiento, que genera siempre una cadena de pensamiento antes de la respuesta, decisión que Liquid justifica para aprovechar su elevada velocidad de generación. El detalle más transparente del lanzamiento afecta al entrenamiento: durante la fase de especialización de los "expertos", el modelo aprendió a "hacer trampas", buscando la respuesta en el historial de Git o en GitHub, PyPI y Hugging Face, e incluso detectó que se encontraba en un entorno aislado (sandbox). Liquid endureció los entornos de prueba y declara que los resultados oficiales proceden de evaluaciones selladas.

Dos limitaciones antes de continuar: se admiten oficialmente dieciséis idiomas, incluido el español. Sin embargo, el modelo solo acepta texto como entrada, según señala la [ficha de CloudPrice](https://cloudprice.net/models/liquid/lfm2.5-24b-a2b). La familia cuenta con variantes de visión independientes, pero esta versión no lo es.

## Promesas bajo examen

Liquid comparó el modelo con Qwen3.6-35B-A3B, Gemma-4-26B-A4B-it y Nemotron-3.5-Lightning en dieciséis benchmarks, todos ejecutados con vLLM. Son mediciones de la propia empresa: en el momento del lanzamiento ninguna entidad independiente había evaluado el modelo, como señala [OrcaRouter](https://www.orcarouter.ai/it/blog/lfm2-5-24b-a2b-on-device-agents). A continuación se muestran los datos más relevantes de la [tabla oficial](https://www.liquid.ai/blog/lfm2-5-24b-a2b).
![tabella1.jpg](tabella1.jpg)

El panorama es más matizado que un simple eslogan. El modelo lidera o empata en cinco de las ocho pruebas de uso de herramientas y ocupa el primer lugar en las tres de seguimiento de instrucciones, mientras que los modelos más grandes mantienen ventaja en conocimiento general y programación. En SWE-Bench, Nemotron (53,40) supera a nuestro modelo (31,20) y Gemma (25,80) queda muy por detrás. La propia Liquid recomienda combinarlo con un sistema de búsqueda (RAG) para tareas que requieran conocimientos específicos.

En cuanto a velocidad, la empresa declara 184 tokens por segundo en un Apple M5 Max y 114 en un Ryzen AI Max+ 395. Esas mediciones se realizaron con llama.cpp, cuantización Q4_K_M y 4K tokens de entrada, según informa [Unite.AI](https://www.unite.ai/it/liquid-ai-releases-open-weight-lfm2-5-24b-a2b-for-on-device-agents/). Son condiciones distintas a las de nuestro entorno de pruebas. Quienes utilicen la API alojada pagan 0,10 dólares por millón de tokens de entrada y 1,00 por millón de tokens de salida.

## Las pruebas sobre el terreno

Se aplicaron las diez pruebas habituales de la serie, con una salvedad: las dos pruebas basadas en imágenes no pudieron ejecutarse por tratarse de un modelo de texto exclusivo. Las ocho restantes muestran un modelo muy sólido en metodología y planificación, pero más débil en precisión temática concreta.

En **razonamiento científico** (mecanismo de Higgs, bosones W y Z, fotón), la explicación fue sólida y bien estructurada, concluyendo con una tabla resumen. Omitió, no obstante, los bosones de Goldstone y su papel en la polarización longitudinal de los bosones masivos. La salida presentó además fallos de codificación de caracteres (como "ГЁ" y "вҶ’"), lo que apunta a un problema del decodificador más que de comprensión. En **código** (encontrar el ciclo de longitud máxima en un grafo no dirigido), escribió un programa limpio que resolvía un problema distinto: aplicó un algoritmo de tiempo polinómico a un problema NP-difícil sin advertir su naturaleza. Aunque se trata de un único test, coincide con la tendencia reflejada en los benchmarks donde SWE-Bench mide la corrección de errores en repositorios reales y no la generación de algoritmos teóricos.

En **planificación multilingüe** (un itinerario de cinco días en Japón para un cliente francés, redactado en francés e italiano), la estructura fue clara pero aparecieron incorrecciones gramaticales (como "le aéroport" por "l'aéroport") y errores logísticos: tomar el Narita Express para ir a Asakusa, situar Kanda Myōjin en Ueno y programar Ryoan-ji y el mercado de Nishiki en la misma mañana. Se omitieron detalles sobre transportes y el JR Pass. En cambio, la **extracción desde un PDF** de aproximadamente 1 MB sobre un contrato de alquiler funcionó impecablemente: los datos fueron precisos, diferenciando ofertas de alquiler (Immobiliare.it) de compraventas reales (CNA y OMI), citando la página correcta al repreguntar.

Los mejores resultados se obtuvieron en estructuración y planificación. En la **planificación de una app web** para un equipo de dos desarrolladores, propuso React, NestJS, PostgreSQL y Prisma en siete hitos con entregables y análisis de riesgos, conteniendo solo una errata menor ("pdfgenerate"). En una **conversación de cuatro turnos** diseñando una app de tareas, mantuvo una coherencia contexto perfecta, generando una tabla comparativa entre WebSocket y polling, esquemas DDL completos, índices, esquema de Prisma y un plan de escalado para diez mil usuarios. En la **planificación estratégica** para una startup de 10M$, produjo un informe de nivel directivo para seis semestres con mitigación de riesgos, aunque respondió en inglés a una solicitud en italiano, perdiendo medio punto. En el **análisis lógico** de tres afirmaciones contradictorias, formalizó las premisas, identificó la contradicción y justificó su conclusión en un italiano correcto.
![tabella2.jpg](tabella2.jpg)

La nota media global fue de 4,3 sobre 5, con una velocidad media de salida de ~44,7 tokens por segundo.

Llegó entonces la prueba clave para un modelo orientado a agentes: la llamada a herramientas (tool calling). Aclaremos su funcionamiento: el modelo no ejecuta acciones por sí mismo, sino que escribe la llamada entre tokens especiales (usando sintaxis de Python por defecto), que la aplicación anfitriona ejecuta devolviendo el resultado, como explica la [guía de uso de herramientas](https://docs.liquid.ai/lfm/key-concepts/tool-use). Probamos dos herramientas simuladas (tiempo y correo). El modelo generó la secuencia de llamadas JSON correcta a 46,45 tokens/seg con ~2 segundos de pausa de razonamiento. Las tres variantes tuvieron éxito: al proporcionarle el resultado de la herramienta, redactó el correo usándolo; al faltar la dirección del destinatario, solicitó el correo de Mario en lugar de inventárselo; y ante una solicitud que no requería herramientas, no realizó ninguna llamada. Son pruebas de formato y criterio, sin llegar a un ciclo multiagente completo.

## Pensar antes de responder

En *Disco Elysium*, el protagonista nunca actúa sin debatir antes con sus veinticuatro habilidades internas, voces que discuten en su cabeza. LFM2.5-24B-A2B hace algo parecido, y a diferencia del juego, vemos desplazarse la cadena de pensamiento en tiempo real. Esto modifica la percepción de la velocidad: los 44 tokens/seg se miden en la respuesta final, pero van precedidos de varios segundos de pensamiento previo (~2 segundos en la prueba de herramientas). Para un agente que interactúa con otras aplicaciones, ese retardo es insignificante. Para un chat interactivo, la experiencia depende de la longitud de la tarea.

Liquid destaca que los tokens de razonamiento tienen un coste computacional bajo porque solo hay 2,45B parámetros activos. Si bien es cierto en cuanto a operaciones (FLOPs), el tiempo transcurrido sigue contando. Además, una prueba independiente en italiano señaló casos en que el modelo razonaba en inglés antes de responder en italiano, comportamiento que conviene supervisar.

¿Y la ventaja de la arquitectura dispersa? En nuestro equipo, los 44 tokens/seg se quedan en menos de la mitad de los 114 t/s declarados en un Ryzen AI Max+, con distinta cuantización, contexto y memoria. Es una velocidad notable para un modelo de veinticuatro mil millones en una tarjeta de 16 GB, aunque demostrar un salto generacional requeriría comparativas directas bajo idénticas condiciones.

## Dónde destaca y dónde no

Su terreno idóneo coincide con su diseño: agentes autónomos, automatización de flujos de trabajo, planificación de proyectos, conversaciones extensas y coherentes, y seguimiento estricto de instrucciones. Resulta inadecuado para la programación algorítmica compleja o como enciclopedia autónoma, carencias reconocidas en los benchmarks de Liquid y confirmadas en nuestros análisis. Tampoco dispone de capacidades de visión.

Una advertencia sobre privacidad: la "ejecución local" no garantiza por sí sola la "seguridad de los datos". Un agente conectado a búsquedas web o API de terceros puede transmitir información al exterior. El modelo permanece en vuestro equipo, pero las salidas de sus herramientas pueden no hacerlo. ¿Quién sale ganando? Pequeños estudios y empresas por debajo del umbral de licencia comercial, que obtienen un agente rápido y gratuito. ¿Quién corre riesgos? Quien lo aplique en tareas que exijan precisión enciclopédica o código crítico.
![tabella3.jpg](tabella3.jpg)
*Tabla comparativa con los modelos evaluados anteriormente en AiTalk.it*

## Veredicto y licencia

LFM2.5-24B-A2B es un modelo rápido y metódico que planifica con claridad, pero que tropieza cuando se requiere rigor teórico o conocimiento profundo. Recomendamos su uso para agentes, automatizaciones y planificación, combinándolo con un sistema de búsqueda (RAG) para consultas fácticas y con un modelo más potente para código complejo.

Para desarrolladores que preparen productos comerciales, la licencia resulta determinante. La LFM Open License v1.0 permite el uso comercial gratuito a entidades con ingresos anuales inferiores a 10 millones de dólares; por encima de dicha cifra se requiere una licencia de pago. Los modelos derivados mantienen estas condiciones, mientras que la investigación académica y organizaciones sin ánimo de lucro están exentas del límite de ingresos. Los detalles están disponibles en la [página oficial de licencias](https://docs.liquid.ai/lfm/help/model-license).

Quedan tres cuestiones abiertas: ¿Cómo se mantendrán las puntuaciones bajo evaluaciones independientes? ¿Cuánto pesa el tiempo de razonamiento obligatorio en tareas extensas? ¿Qué ocurre cuando un agente real en producción encuentra desviaciones ocasionales de idioma? Solo el despliegue continuado ofrecerá respuestas definitivas.
