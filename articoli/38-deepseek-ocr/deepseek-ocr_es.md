---
tags: ["Research", "Training", "Applications"]
date: 2025-10-22
author: "Dario Ferrero"
---

# DeepSeek OCR: cuando una imagen vale 10,000 tokens
![deepseek-ocr.jpg](deepseek-ocr.jpg)


*Normalmente evitamos perseguir cada anuncio de las grandes empresas tecnológicas, a menos que se trate de una verdadera innovación. Y esta vez parece ser el caso. [DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR), lanzado el 20 de octubre de 2025, ha alcanzado más de 7,000 estrellas en GitHub en pocos días y ha captado la atención de Andrej Karpathy, exdirector de IA de Tesla y una figura legendaria en el campo del deep learning. No es poca cosa cuando una de las mentes más brillantes de la visión por computadora [define un modelo como "bastante interesante"](https://x.com/karpathy/status/1980397031542989305) y se pone a filosofar sobre el futuro de los tokenizadores. Pero, ¿qué tiene de especial este modelo de 3 mil millones de parámetros que ha desatado tanto entusiasmo?*

## La arquitectura de la inversión

DeepSeek-OCR invierte un paradigma que parecía consolidado: en lugar de convertir imágenes en texto para luego tokenizarlo, transforma el texto en imagen y lo comprime ópticamente. Es como si alguien hubiera mirado la Piedra de Rosetta al revés y hubiera entendido que el jeroglífico es más eficiente que el alfabeto. La idea es tan simple como contraintuitiva, y recuerda esa escena de *Tenet* donde las balas retroceden en el tiempo: aquí los tokens vuelven a ser píxeles.

La arquitectura se divide en dos componentes principales. El DeepEncoder toma un documento de alta resolución, lo procesa a través de un codificador visual basado en [SAM](https://segment-anything.com/) y CLIP, y luego lo comprime usando un módulo convolucional que reduce drásticamente el número de tokens necesarios. El decodificador es un modelo de Mezcla de Expertos de 3 mil millones de parámetros que interpreta estos "tokens de visión" comprimidos y produce una salida estructurada.

Los números cuentan una historia interesante: con una compresión de 10x, el sistema mantiene un 97% de precisión. Llevando la relación a 20x, la precisión baja al 60%, pero para muchos casos de uso sigue siendo más que aceptable. Esto significa que un artículo de mil palabras, que requeriría unos mil tokens en formato de texto, puede ser representado con solo 100 tokens de visión manteniendo la información casi intacta. [DeepSeek sostiene](https://deepseek.ai/blog/deepseek-ocr-context-compression) que una sola GPU NVIDIA A100 puede procesar 200,000 páginas al día con este sistema, un rendimiento que deja en ridículo a los pipelines de OCR tradicionales.

## Benchmarks y comparaciones: dónde brilla (y dónde no)

La comparación con la competencia revela luces y sombras. En [OmniDocBench](https://www.marktechpost.com/2025/10/20/deepseek-just-released-a-3b-ocr-model-a-3b-vlm-designed-for-high-performance-ocr-and-structured-document-conversion/), el benchmark que prueba las capacidades de extracción en documentos complejos, DeepSeek-OCR se comporta bien pero no domina. GOT-OCR 2.0, desarrollado por la Universidad de Pekín, sigue siendo superior en términos de precisión pura, especialmente en documentos con diseños complejos o fórmulas matemáticas. MinerU 2.0, otro contendiente chino, muestra un rendimiento similar pero con una arquitectura más tradicional.

En la comparación con los modelos multimodales generalistas de visión y lenguaje, la situación se vuelve más interesante. MiniCPM-V 2.6, InternVL 2.5 y el reciente Mistral OCR son todos modelos más grandes, con parámetros que van de los 7 a los 20 mil millones. DeepSeek-OCR, con sus 3 mil millones, juega en una categoría diferente. Como [señala el propio Karpathy](https://x.com/karpathy/status/1980397031542989305), el modelo es "quizás un poco peor que los puntos" (refiriéndose probablemente a Gemini u otros sistemas cerrados), pero la admisión es sincera y sintomática: no es una cuestión de supremacía absoluta, sino de eficiencia relativa.

IBM Docling, otra solución de código abierto para el análisis de documentos, adopta un enfoque híbrido con pipelines modulares y alcanza excelentes resultados en documentos técnicos y científicos, pero requiere más recursos computacionales. Microsoft Florence-2, a pesar de ser un modelo de visión más genérico, muestra capacidades de OCR decentes pero sufre en situaciones donde es necesario preservar la estructura del documento.

La verdadera fuerza de DeepSeek-OCR emerge en los casos de uso específicos: documentos largos, procesamiento por lotes, aplicaciones donde la velocidad es crítica y una ligera pérdida de precisión es tolerable. Es el equivalente tecnológico de elegir una cámara sin espejo en lugar de una de formato medio: menos perfecta, pero mucho más versátil y práctica.
![grafico1.jpg](grafico1.jpg)
[Imagen del perfil de GitHub de DeepSeek OCR](https://github.com/deepseek-ai/DeepSeek-OCR)

## De la teoría a la práctica: dónde se necesita realmente

Pero, ¿cuándo tiene sentido implementar DeepSeek-OCR en un proyecto real? La respuesta depende del contexto específico. Las aplicaciones más prometedoras se refieren a escenarios donde el volumen y la velocidad importan más que la perfección absoluta. Pensemos en la digitalización de archivos históricos en papel, donde millones de páginas deben convertirse a un formato de búsqueda: aquí, la capacidad de procesar 200,000 páginas al día en una sola GPU marca la diferencia entre un proyecto factible y uno económicamente insostenible.

En el mundo empresarial, la extracción automática de datos de facturas, recibos o documentos contables representa otro terreno fértil. Empresas como [Dataconomy destacan](https://dataconomy.com/2025/10/21/deepseek-ocr-new-open-source-ai-model-goes-viral-on-github/) cómo los despachos de abogados y los departamentos de cumplimiento podrían beneficiarse del análisis masivo de contratos, donde mantener la estructura visual del documento es tan crucial como extraer el texto. Un abogado que busca una cláusula específica en diez mil acuerdos de confidencialidad no necesita una precisión del 99.9%, sino encontrar rápidamente los documentos relevantes.

Sin embargo, hay una sombra que se cierne sobre estos escenarios: la falta de transparencia sobre los datos de entrenamiento. DeepSeek no ha publicado detalles sobre el conjunto de datos utilizado para entrenar el modelo, y esto es un problema no trivial. Un OCR entrenado principalmente en documentos financieros chinos podría interpretar mal las facturas europeas, así como uno expuesto predominantemente a textos impresos podría tener dificultades con la escritura a mano. La opacidad de los datos dificulta la evaluación a priori de si el modelo es adecuado para el propio caso de uso específico, obligando a realizar pruebas empíricas que no todos pueden permitirse.

## La filosofía de código abierto en tiempos de guerra de chips

La decisión de lanzar DeepSeek-OCR completamente de código abierto, con los pesos del modelo descargables desde [Hugging Face](https://huggingface.co/spaces/khang119966/DeepSeek-OCR-DEMO) y el código en GitHub, choca violentamente con el destino del modelo R2 de DeepSeek, todavía en el limbo. [El contexto geopolítico lo explica todo](https://www.techradar.com/pro/chaos-at-deepseek-as-r2-launch-crashes-into-hardware-problems-rivals-gain-huge-advantage): tras el éxito viral de DeepSeek-R1 a principios de 2025, las autoridades chinas presionaron a la empresa para que abandonara las GPU de NVIDIA en favor de los chips Ascend de Huawei para el entrenamiento de R2.

El resultado fue un desastre técnico. [Según el Financial Times](https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-reportedly-urged-by-chinese-authorities-to-train-new-model-on-huawei-hardware-after-multiple-failures-r2-training-to-switch-back-to-nvidia-hardware-while-ascend-gpus-handle-inference), DeepSeek no logró completar ni una sola ejecución de entrenamiento con éxito en los chips de Huawei, a pesar de que se envió un equipo de ingenieros al lugar. La administración Trump había prohibido la exportación de las H20 de NVIDIA a China en abril de 2025, y DeepSeek se encontró atrapada entre las sanciones estadounidenses y las presiones del gobierno chino. El CEO Liang Wenfeng, [insatisfecho con el rendimiento de R2](https://www.bgr.com/tech/what-happened-to-deepseeks-revolutionary-r2-ai/), tuvo que elegir: patriotismo tecnológico o resultados concretos.

En este escenario, lanzar DeepSeek-OCR en código abierto se convierte en una jugada estratégica multidimensional. Primero, elude las limitaciones de hardware: un modelo de 3 mil millones puede ejecutarse en hardware de consumo, reduciendo la dependencia de centros de datos llenos de GPU imposibles de obtener. Segundo, construye poder blando: mientras R2 languidece en los servidores de DeepSeek, OCR conquista a desarrolladores de todo el mundo. Tercero, elude las restricciones: un modelo de código abierto no puede ser "prohibido" eficazmente, solo puede ser replicado y mejorado por la comunidad.

Es la misma estrategia que Meta usó con Llama: si no puedes ganar en el plano comercial cerrado, ábrelo todo y deja que el ecosistema haga el trabajo. [Como informa Dataconomy](https://dataconomy.com/2025/10/21/deepseek-ocr-new-open-source-ai-model-goes-viral-on-github/), el modelo alcanzó las 4,000 estrellas en GitHub en menos de 24 horas, una adopción viral que ninguna campaña de marketing podría comprar.
![grafica2.jpg](grafica2.jpg)
[Imagen del perfil de GitHub de DeepSeek OCR](https://github.com/deepseek-ai/DeepSeek-OCR)

## El futuro del OCR: visión vs. texto

La reflexión más provocadora llega precisamente de Karpathy, quien en su hilo de X [plantea una cuestión filosófica](https://x.com/karpathy/status/1980397031542989305): "Quizás tendría más sentido que todas las entradas de los LLM fueran siempre y solo imágenes". Es una afirmación que suena herética para quienes han pasado años perfeccionando tokenizadores e incrustaciones de texto.

Karpathy enumera cuatro argumentos: mayor compresión de la información, un flujo de datos más general que incluye formato y colores, la capacidad de usar atención bidireccional en lugar de autorregresiva, y la eliminación del "tokenizador feo" con todos sus problemas de Unicode, seguridad y codificación. Su punto es simple: un emoji sonriente debería representarse como una cara sonriente, con píxeles y todo, no como un token abstracto que ha perdido toda conexión visual con su significado original.

Xie Saining, profesor asistente en la Universidad de Nueva York, [está de acuerdo con esta visión](https://dataconomy.com/2025/10/21/deepseek-ocr-new-open-source-ai-model-goes-viral-on-github/) de convergencia entre la visión por computadora y el procesamiento del lenguaje natural. Pero el entusiasmo debe ser atemperado con realismo. Los tokenizadores de texto existen desde hace décadas y tienen una razón de ser: son eficientes para el lenguaje natural puro. El texto renderizado como imagen, incluso comprimido, ocupa más espacio que un buen tokenizador BPE para contenido puramente textual.

El verdadero caso de uso es híbrido: documentos donde el diseño, el formato y la estructura visual son parte integral del significado. Contratos legales donde la sangría cuenta. Informes financieros donde las tablas y los gráficos coexisten con el texto. Artículos científicos llenos de ecuaciones. En estos escenarios, DeepSeek-OCR brilla porque mantiene el contexto visual que un analizador de texto destruiría.

Por otro lado, para una conversación de chat o una simple indicación de texto, convertir todo en imagen es un desperdicio. Es como usar un osciloscopio para medir la temperatura: técnicamente posible, pero absurdo. [Simon Willison](https://simonwillison.net/2025/Oct/20/deepseek-ocr-claude-code/) señala que DeepSeek-OCR funciona mejor cuando se combina con otras herramientas, no como un sustituto universal.

El debate recuerda al de vinilo y digital en la música: los puristas del texto sostienen que la representación simbólica es más limpia, los visionarios de los píxeles dicen que solo la imagen captura la totalidad de la información. La verdad, como siempre, está en el medio: multimodalidad nativa, donde los modelos pueden elegir dinámicamente la mejor representación para cada tipo de entrada.

## Conclusiones: ¿innovación o un elegante subterfugio?

DeepSeek-OCR es ambas cosas. Es una innovación genuina en el enfoque de la compresión contextual, con una arquitectura que desafía supuestos consolidados sobre cómo representar la información textual. Pero también es un brillante subterfugio a limitaciones concretas: pocas GPU, presiones políticas, necesidad de eficiencia extrema.

[El modelo en Hugging Face](https://huggingface.co/spaces/khang119966/DeepSeek-OCR-DEMO) funciona a 2,500 tokens por segundo en una A100-40G, un rendimiento que impresiona considerando la complejidad de la tarea. Los desarrolladores pueden integrarlo fácilmente en sus pipelines, y la licencia de código abierto permite modificaciones y adaptaciones. Para quienes trabajan con grandes volúmenes de documentos, podría ser la solución que estaban buscando.

Sin embargo, los aspectos críticos no deben ser ignorados. La precisión no es mejor que el estado del arte, admitido por el propio Karpathy. La calidad de los datos de entrenamiento, crucial para cualquier sistema de OCR, sigue siendo opaca en la documentación oficial. Y el modelo está optimizado para documentos en chino e inglés, con soporte limitado para otros idiomas.

El éxito viral en GitHub y el entusiasmo de la comunidad sugieren que DeepSeek ha tocado una fibra sensible: el deseo de herramientas eficientes, abiertas y pragmáticas en una era de modelos cada vez más grandes y costosos. Mientras los gigantes tecnológicos compiten por quién tiene el centro de datos más grande, DeepSeek demuestra que todavía se puede innovar en los rincones, encontrando eficiencia donde otros solo ven la necesidad de más potencia bruta.

Como en esa escena final de *Ghost in the Shell* donde Motoko Kusanagi se fusiona con el Puppet Master, quizás el futuro de la IA no sea una victoria total del texto o de la visión, sino una síntesis híbrida donde ambos coexisten y se complementan. DeepSeek-OCR es un paso en esa dirección, imperfecto pero fascinante, pragmático pero visionario. Y sobre todo, es de código abierto: lo que significa que en seis meses algún adolescente genial probablemente ya habrá resuelto los problemas que hoy parecen limitantes. Este es, en el fondo, el verdadero poder del código abierto: no la perfección, sino la iteración infinita.