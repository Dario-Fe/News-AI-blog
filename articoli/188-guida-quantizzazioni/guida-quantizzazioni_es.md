---
tags: ["Generative AI", "Training", "Research"]
date: 2026-10-07
author: "Dario Ferrero"
---

# Guía de formatos de cuantización para LLM locales
![guida-quantizzazioni.jpg](guida-quantizzazioni.jpg)

*En el apólogo de Borges sobre el imperio y su mapa, los cartógrafos llegan a dibujar un mapa tan grande como el propio territorio para descubrir que no sirve de nada. Un modelo lingüístico de 16 bits es ese mapa: fidelísimo, a escala uno a uno, demasiado voluminoso para tenerlo sobre el escritorio. La cuantización es el arte de reducir la escala sin perder las carreteras que importan, y en 2026 las herramientas para hacerlo son tantas que requieren un glosario antes incluso de elegir. Tras la [guía de motores de inferencia](https://aitalk.it/it/guida-motori-inferenza-locale), este artículo pone orden entre los formatos: qué son, cuánto cuestan en calidad y con qué hardware os convienen.*

Una premisa, como siempre: este es un análisis de artículos, documentación y repositorios, no un benchmark. Los números proceden de las fuentes enlazadas, no se han reproducido, y allí donde la fuente tiene un interés comercial, lo indicamos.

## Contenedores frente a métodos

El primer equívoco es léxico. Un contenedor establece cómo se escriben los números en el disco; un método de cuantización, cómo se reducen. Podemos incluir entre los contenedores safetensors, GGUF y los antiguos archivos pickle (.bin, .pt); entre los métodos, GPTQ, AWQ, NF4 y las K-quants e I-quants de llama.cpp; y luego los casos híbridos: EXL2 y EXL3 son a la vez método y estructura de archivos, vinculados a una sola librería. El archivo pickle puede ejecutar código al cargarse: desconfiad de los archivos de origen desconocido. GGUF, en cambio, según la [documentación de Hugging Face](https://huggingface.co/docs/hub/en/gguf), engloba tensores y metadatos estándar, y nació de Georgi Gerganov, el creador de llama.cpp.

La cuenta básica es aritmética: la tabla que Hugging Face utiliza para un Llama-2 de 7 mil millones lo dice claramente: [13 GB en origen, 4,1 GB en Q4_K_M](https://github.com/huggingface/skills/blob/main/skills/huggingface-local-models/references/quantization.md).
![tabella1.jpg](tabella1.jpg)

### La segunda cuenta: la caché

Los pesos son solo la parte visible. Como explicamos [en el artículo sobre la KV cache](https://aitalk.it/it/kv-cache-approach.html), Llama-3.1-70B a 16 bits acumula unos 0,31 megabytes de caché por cada token: a 128.000 tokens son unos 40 GB; a un millón, más de 300, superando los 140 GB de los propios pesos. La caché es el archivo donde el modelo guarda las claves y valores de lo que ya ha leído, y con cada palabra generada hay que recorrerla entera: el cuello de botella es el ancho de banda, antes que el espacio en disco.

Las respuestas pertenecen a dos familias. La primera comprime: TurboQuant, OSCAR y EpiCache, examinados en aquel artículo, trabajan sobre los bits por valor o sobre qué conservar; para OSCAR en Qwen3-8B, la diferencia con el BF16 se reduce a 1,42 puntos con una caché ocho veces menor. La segunda gestiona, y es el tema del [artículo sobre PagedAttention y RadixAttention](https://aitalk.it/it/pagedattention-radixattention). El [artículo de vLLM](https://arxiv.org/html/2309.06180v1) midió que en los sistemas anteriores solo entre el 20,4 y el 38,2 por ciento de la memoria de caché contenía tokens reales; con la paginación el desperdicio pasa a ser casi nulo y el rendimiento aumenta de dos a cuatro veces. ¿Por qué hablamos de ello aquí? Porque comprimir la caché es un segundo botón, independiente del de los pesos: ExLlamaV3, por ejemplo, la cuantiza de 2 a 8 bits. Cuando un formato promete un contexto largo en una tarjeta pequeña, el mérito suele ser de ambos.

## GGUF, la llave maestra

Si un formato ha ganado la partida de la inferencia local es GGUF, por una razón poco deslumbrante: funciona en todas partes. Como vimos al [hablar de motores](https://aitalk.it/it/guida-motori-inferenza-locale), llama.cpp lo ejecuta en CPU, NVIDIA, AMD, Intel y Apple, y Hugging Face enumera LM Studio, Ollama y GPT4All entre las herramientas que lo utilizan. Un solo archivo transporta pesos y metadatos.

El nombre revela la receta. Según la misma tabla de Hugging Face, Q4_K utiliza 4,5 bits por peso, Q5_K 5,5, Q6_K 6,5625; las I-quants bajan a 4,25 (IQ4_XS), 2,06 (IQ2_XXS) y 1,56 (IQ1_S) y se apoyan en una importance matrix, una muestra de textos que indica al cuantizador qué pesos importan más. Las letras S, M, L indican mezclas en las que algunas partes permanecen a más bits, motivo por el cual un Q4_K_M pesa más que el cálculo teórico estricto.

Sobre esta base ha llegado la época de las cuantizaciones dinámicas. [Unsloth](https://unsloth.ai/blog/dynamic-v2), que los lectores conocen por Unsloth Studio, asigna un número de bits diferente a cada capa, y en sus [pruebas sobre Qwen3.5](https://unsloth.ai/docs/models/qwen3.5/gguf-benchmarks) sostiene que sus variantes Q4_K_XL e IQ3_XXS están en la mejor frontera entre tamaño y fidelidad. Cautela obligada: quienes miden las cuantizaciones son también quienes las producen, aunque publiquen los datos brutos. Y las I-quants tienen un precio: en sus pruebas la inferencia se ralentiza entre un 5 y un 10 por ciento.

Donde GGUF cede es en el servicio a muchos usuarios: la [documentación de vLLM](https://docs.vllm.ai/en/latest/features/quantization/gguf/) lo califica de altamente experimental y poco optimizado, y hoy requiere un complemento externo. La contrapartida, valiosa en casa, es que un modelo más grande que la memoria de vídeo se ejecuta igualmente, repartiendo el trabajo entre la GPU y la CPU a costa de la velocidad.

## GPTQ y AWQ, caballos de tiro

Imaginad a un carpintero que debe reducir cien tablas a grosores estándar: GPTQ, cortándolas una a una, corrige los cortes posteriores para compensar el error recién cometido. Fuera de metáforas, según el [artículo](https://arxiv.org/html/2210.17323v2), es un método de una sola pasada que utiliza información de segundo orden para decidir los redondeos, capa por capa, con una pequeña muestra de calibración (128 fragmentos de 2048 tokens). En OPT-175B la perplexity pasa de 8,34 a 8,37 con GPTQ a 4 bits, mientras que el simple redondeo la lleva a 10,54; a 3 bits el redondeo colapsa por encima de 7000, mientras GPTQ se mantiene en 8,68. Un modelo de 175 mil millones se comprime en unas cuatro horas en una sola GPU. Las aceleraciones declaradas, 3,25 veces en A100 y 4,5 en A6000 respecto a FP16, se aplican a una solicitud por lote y nacen de desplazar menos datos en memoria, no de realizar menos cálculos: lo escriben los propios autores entre las limitaciones.

[AWQ](https://arxiv.org/abs/2306.00978), del grupo de Song Han en el MIT y mejor artículo en MLSys 2024, parte de una observación: no todos los pesos importan lo mismo, y proteger aproximadamente el 1 por ciento reduce mucho el error. El truco está en cómo se encuentran —observando las activaciones y no los pesos— y en cómo se protegen: no a más bits, sino escalándolos con una transformación equivalente para que el formato siga siendo uniforme. Sin retropropagación, sostienen los autores, generaliza mejor sin sobreajustarse a la muestra de calibración, y su TinyChat supera en más de tres veces la velocidad de la implementación FP16 de Hugging Face.

¿Quién gana? Las fuentes no declaran un ganador claro: cada artículo compara su método con FP16 o con el redondeo simple, no con el otro sobre el mismo motor. Los encontraréis principalmente en vLLM y SGLang, donde hace falta atender a muchos usuarios simultáneos.

Más traicionero es el terreno de las herramientas. Una [propuesta en vLLM](https://github.com/vllm-project/vllm/issues/30136) señala que AutoGPTQ y AutoAWQ ya no tienen mantenimiento y que los cargadores GPTQ y AWQ permanecerán por ahora, pero se retirarán más adelante porque existen demasiados modelos ya publicados; la documentación declara [AutoAWQ en desuso](https://docs.vllm.ai/en/stable/features/quantization/auto_awq/) e indica llm-compressor. [GPTQModel](https://github.com/ModelCloud/GPTQModel) afirma haberlos sustituido en Transformers, Optimum y PEFT. El consejo práctico: mirad con qué herramienta y cuándo se ha producido un modelo a 4 bits, porque un formato extendido no está necesariamente vivo.

## EXL3, NF4, MLX: especialistas

Si tenéis una tarjeta NVIDIA para juegos y queréis exprimirla en solitario, os encontraréis con ExLlamaV3. Su formato EXL3 nace de QTIP, técnica de la Universidad de Cornell, y según su [README](https://github.com/turboderp-org/exllamav3) se convierte utilizando únicamente el modelo original y los bits deseados, incluso fraccionarios: unas horas en una RTX 4090 para un 70B, frente a las cerca de 720 horas de GPU A100 (y 850 dólares) que el README atribuye a AQLM. La cifra más citada es una anécdota: Llama-3.1-70B se mantiene coherente a 1,6 bits por peso y, con la capa de salida a 3 bits y una caché de contexto de 4096 tokens, cabe en menos de 16 GB. Coherente no significa medido: no es una puntuación formal de benchmark. Limitaciones: requiere CUDA 12.4 o superior y el soporte para ROCm sigue estando entre las tareas pendientes; la estructura original de los archivos se conserva, lo que haría posible llevarlo a Transformers y vLLM, aunque el README habla de ello en futuro.

Otro cometido tiene NF4, el tipo a 4 bits de bitsandbytes nacido con [QLoRA](https://arxiv.org/abs/2305.14314). El artículo demuestra cómo ajustar un modelo de 65 mil millones en una sola GPU de 48 GB conservando el rendimiento del ajuste a 16 bits: el modelo cuantizado permanece congelado y los gradientes lo atraviesan hasta pequeños adaptadores entrenables. No es un formato para descargar, sino para aplicar sobre la marcha al cargar, sin calibración, y [Marktechpost](https://www.marktechpost.com/2026/09/18/gguf-vs-gptq-vs-awq-vs-exl2-llm-model-formats-explained-2026/) recuerda que no garantiza velocidad en la inferencia. Es el flujo de trabajo que herramientas como Unsloth Studio ofrecen sin necesidad de terminal.

En Mac el escenario cambia. Según la [documentación de Hugging Face](https://huggingface.co/docs/hub/en/mlx), MLX es el entorno de Apple para Apple Silicon, y MLX-LM convierte y cuantiza modelos con un solo comando, mientras que la comunidad `mlx-community` publica pesos ya listos. La limitación es el confinamiento en el ecosistema: funciona ahí y nada más, y en Mac, GGUF sigue siendo una opción muy sólida.

## Cuánto cuesta perder bits

A principios de los años dos mil, William Basinski grabó sus *Disintegration Loops* haciendo girar cintas magnéticas viejas que con cada pasada se desintegraban un poco: la música nacía de la pérdida. Con los pesos la pérdida no es poética, pero sigue el mismo patrón: leve al principio y brusco después.

En la [tabla de Hugging Face](https://github.com/huggingface/skills/blob/main/skills/huggingface-local-models/references/quantization.md), sobre un Llama-2 de 7 mil millones, la perplexity (cuánto se sorprende el modelo ante un texto real) aumenta con respecto a los 16 bits un 0,03 por ciento con Q8_0, un 0,13 con Q6_K, un 0,39 con Q5_K_M y un 1,68 con Q4_K_M, mientras el archivo baja de 13 a 4,1 GB. Más abajo la cuenta sube rápido: 6,07 por ciento con Q3_K_M, 15,3 con Q2_K. Es un modelo de 2023, y los modelos recientes pueden reaccionar de forma distinta.

Pero la perplexity es un termómetro rudimentario. En el análisis ya citado, Unsloth muestra un caso en el que una IQ2_XXS de menos de 11 GB supera a una IQ3_S en pruebas reales (LiveCodeBench y MMLU Pro), a pesar de tener peor perplexity y divergencia, y advierte de que estos índices dependen del texto utilizado para calibrar (a menudo Wikipedia). Fuente interesada, insistamos, pero el mensaje práctico se sostiene: el termómetro no sustituye a la prueba sobre vuestro propio trabajo. Una comparación directa y rigurosa entre formatos, con el mismo modelo, hardware y tarea, no existe en la literatura pública consultada.

## FP4, ternarios y QAT

En *Return of the Obra Dinn*, Lucas Pope construyó un mundo tridimensional con solo dos colores, y funciona porque cada píxel está elegido con cuidado. Es la imagen de la frontera: por debajo de los cuatro bits no se llega redondeando hacia abajo, se llega diseñando desde el origen.

La primera novedad son los números en coma flotante de 4 bits, NVFP4 y MXFP4, que dividen los pesos en pequeños bloques con su propia escala. [NVIDIA](https://build.nvidia.com/playbooks/nvfp4-quantization) presenta NVFP4 como formato para sus GPU Blackwell, con unas 3,5 veces menos memoria que los 16 bits y una precisión habitualmente dentro del 1 por ciento respecto a FP8, aunque invita a evaluarlo en cada caso (datos del fabricante). En llama.cpp se incorporó a principios de abril de 2026 un [kernel CUDA genérico para NVFP4](https://github.com/ggml-org/llama.cpp/pull/21074), y la misma solicitud anuncia uno específico para Blackwell más adelante: la aceleración completa atañe a pocas tarjetas. En las pruebas de Unsloth, además, MXFP4 utiliza 4,25 bits por peso frente a los 4,5 de Q4_K y en muchos tensores rinde peor.

El segundo camino es entrenar el modelo sabiendo que será cuantizado: el QAT (*Quantization-Aware Training*). [Unsloth](https://unsloth.ai/blog/dynamic-v2) señala para Gemma 3 de 12 mil millones en Q4_0 un 67,07 por ciento en MMLU a cinco ejemplos frente al 67,15 de la versión de 16 bits: una décima de punto de diferencia. Es el traje hecho a medida en lugar del arreglo posterior.

La tercera vía, más radical, son los modelos ternarios. [Ternary Bonsai 2 27B](https://www.marktechpost.com/2026/09/18/prismml-releases-ternary-bonsai-2-27b-a-5-9-gb-apache-2-0-model-retaining-98-2-of-qwen3-8-27b-performance/) de PrismML, publicado el 18 de septiembre, tiene pesos con valores de menos uno, cero o más uno, y ocupa 5,93 GB frente a los 53,80 de los 16 bits. La empresa declara un 98,2 por ciento del rendimiento del modelo de partida en veinte pruebas internas; en tareas de agentes largas baja a cerca del 75 (Terminal-Bench 2.1: 52,8 frente a 69,7), y hace falta la versión modificada de llama.cpp de la empresa, porque la versión oficial rechaza los archivos.

Para la versión anterior, un desarrollador independiente publicó en GitHub un [banco de pruebas](https://github.com/Astezelex/bonsai-27b-16gb-bench) en una RTX 5060 Ti de 16 GB frente a una IQ2_XXS del mismo modelo base. En conocimiento general (MMLU-Redux) se da un empate estadístico (0,871 frente a 0,860); en AIME26 con 60.000 tokens de razonamiento el ternario gana (0,867 frente a 0,633), pero la diferencia nace sobre todo de la convergencia: la variante IQ2_XXS razona durante más tiempo y choca más a menudo con el límite de tokens, aunque cuando converge responde correctamente. De ahí la lección del autor: declarad siempre el presupuesto de razonamiento. Cautelas: un solo autor, muestras pequeñas (30 problemas en AIME26, donde la diferencia de precisión tiene un valor p de 0,072), análisis orquestado con un asistente de IA según declara él mismo, y ninguna revisión por pares. Y para atender a varios usuarios juntos, escribe, hoy es la herramienta equivocada.

## Elegir según el hardware

Debéis partir del hardware, como en el [artículo sobre motores](https://aitalk.it/it/guida-motori-inferenza-locale). Si tenéis una GPU AMD, como la Radeon de 16 GB de nuestro entorno de pruebas, GGUF es el camino más viable: EXL3 requiere CUDA y llama.cpp soporta HIP perfectamente. Si tenéis una NVIDIA para juegos y usáis el modelo en solitario, elegid GGUF por practicidad o EXL3 si buscáis los últimos tokens por segundo y aceptáis un ecosistema más estrecho. Si atendéis a muchos usuarios simultáneos, mirad hacia GPTQ o AWQ en vLLM y SGLang, o hacia FP8 y FP4 en tarjetas recientes. En Mac la elección está entre MLX y GGUF, y para ajustar un modelo grande con poca memoria tenéis QLoRA.

¿Cuánta calidad perder? Una regla prudente: partid de Q4_K_M y subid a Q5_K_M o Q6_K si sobra memoria. Por debajo de los tres bits, id solo con cuantizaciones pensadas para bajar (dinámicas o ternarias) y siempre midiendo sobre vuestra propia tarea, ya sea código, razonamiento o un idioma poco representado como el italiano. Las fuentes consultadas no miden el rendimiento en italiano: es una zona en blanco, y el juicio final es vuestro.
![tabella2.jpg](tabella2.jpg)

**Regla sobre la calidad:**
![tabella3.jpg](tabella3.jpg)

¿Quién gana en todo esto? Quien tiene 16 GB de VRAM y ambiciones de 27 mil millones. Quien arriesga es quien se fía de un solo número de benchmark o de un solo formato en un ecosistema donde las modificaciones multiplican las excepciones. Quedan abiertas la estabilidad en tareas largas, la reproducibilidad de los resultados declarados por los fabricantes y la llegada de los ternarios a los motores estándar. El mapa perfecto, recordaba Borges, no sirve a nadie: sirve el mapa que entra en la mochila y os lleva adonde tenéis que ir.

---

*Nota técnica: los datos proceden de artículos, documentación oficial y repositorios enlazados, y no se han reproducido de forma independiente. Las cifras de la tabla de Hugging Face sobre Llama-2-7B son de 2023; las pruebas de Unsloth, NVIDIA y PrismML son de los propios fabricantes; el banco de pruebas sobre Bonsai es de un solo autor independiente no revisado.*
