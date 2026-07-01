---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-06-01
author: "Dario Ferrero"
---

# RecursiveMAS ha abolido los tokens, los agentes hablan en su propio idioma
![recursivemas.jpg](recursivemas.jpg)

*Un paper publicado el 28 de abril de 2026 por investigadores de UIUC, Stanford, NVIDIA y MIT propone un cambio arquitectónico radical: agentes de AI que colaboran sin intercambiar más texto, comunicándose directamente en latent space. Los números son convincentes. Las preguntas abiertas, todavía más. Descubramos RecursiveMAS, el framework que transforma a los agentes en un 'cerebro colectivo recursivo'*.

Imaginad un equipo de especialistas que debe resolver un caso complejo: un cardiólogo, un neurólogo, un anestesista. Cada vez que uno de ellos tiene una intuición, sin embargo, no puede simplemente pasarla al colega; debe primero traducirla en un correo electrónico formal, enviarlo, esperar a que el otro lo lea, lo interprete, formule una respuesta, la escriba y la envíe de vuelta. Y así sucesivamente, en cada intercambio. El pensamiento se ralentiza, los costes aumentan, algo se pierde en la traducción.

Este es, con una aproximación útil, el problema fundamental de los sistemas multi-agente basados en lenguaje. Cada agente de AI recibe un input en forma textual, lo procesa, produce un output textual, que se pasa al siguiente agente como nuevo input. Cada paso requiere decodificación del vocabulario (una operación computacionalmente costosa), latencia y tokens, es decir, dinero. Si se añade la recursión, es decir, el hecho de que el sistema deba realizar varias rondas de colaboración para refinar la respuesta, el problema se multiplica: en cada round, cada agente debe decodificar todo desde cero.

[RecursiveMAS](https://arxiv.org/abs/2604.25917), el framework presentado el 28 de abril de 2026 por un equipo de doce investigadores distribuidos entre UIUC, Stanford, NVIDIA y MIT, parte de una pregunta aparentemente simple: ¿y si los agentes dejaran de hablarse en texto?

## La recursión como principio de sistema

Para entender el alcance de la propuesta, es necesario dar un paso atrás. En los últimos años, la recursión, es decir, la idea de hacer "girar en loop" los mismos procesamientos sobre estados internos del modelo para profundizar el razonamiento, se ha consolidado como uno de los nuevos ejes de scaling para los grandes modelos lingüísticos. En lugar de entrenar modelos cada vez más grandes, se puede tomar un modelo de dimensiones razonables y hacerlo iterar varias veces sobre el mismo problema, refinando progresivamente sus representaciones internas. Este enfoque, llamado en la literatura *recursive language model* (RLM), ha mostrado resultados prometedores en la investigación de los últimos dos años.

El salto conceptual de RecursiveMAS consiste en extender este principio desde el interior de un solo modelo a todo el sistema multi-agente. Ya no hay recursión dentro de un agente, sino recursión del sistema como unidad. Toda la colaboración entre agentes se convierte en un loop recursivo único, en el que la información fluye continuamente, en forma de latent states, no de texto, de un agente a otro, y el círculo se cierra: el último agente pasa su estado interno al primero, que puede así reiniciar el procesamiento con la información acumulada en el round anterior.

El resultado es lo que el paper describe como un *cerebro colectivo recursivo*: cada agente actúa como una capa de un modelo recursivo, y todo el sistema converge iterativamente hacia una respuesta sin producir nunca, excepto en el último round, texto intermedio.

## RecursiveLink: el intérprete ligero

El problema técnico más delicado es el de la traducción entre mundos. En un sistema multi-agente heterogéneo, donde cada agente es un modelo diferente, con arquitectura diferente, dimensiones diferentes del espacio oculto (*hidden size*), ¿cómo se transfiere un latent state de un modelo a otro sin convertirlo en texto?

La respuesta que propone RecursiveMAS es el módulo [RecursiveLink](https://recursivemas.github.io/): un componente ligero con dos capas residuales que actúa como intérprete entre los latent spaces de los diferentes modelos. En su variante interna (*inner link*), opera dentro de cada agente individual durante la generación: en lugar de proyectar el estado oculto sobre el vocabulario para producir un token, lo transforma y lo reinyecta como input para el paso siguiente, manteniendo el razonamiento íntegramente en el espacio continuo. En la variante externa (*outer link*), añade una layer lineal suplementaria para proyectar el latent state de un agente en el espacio dimensional del agente siguiente, permitiendo la transferencia incluso entre modelos con geometrías internas incompatibles.

La elección de la conexión residual no es estética: mantener el componente original del latent state significa que el módulo no tiene que aprender toda la proyección desde cero, sino solo la *diferencia*, la brecha entre el espacio de origen y el de destino. Esto hace que el entrenamiento sea más estable y más eficiente.

Lo más sorprendente, sin embargo, es el tamaño del componente entrenado. Mientras que los parámetros base de todos los agentes permanecen completamente congelados, el RecursiveLink introduce solo unos 13 millones de parámetros entrenables en todo el sistema, lo que equivale al 0,31% de los parámetros totales. Para dar una idea de la proporción: es como optimizar una orquesta sinfónica actuando exclusivamente sobre el sistema de amplificación entre los atriles, sin tocar ningún instrumento.
![grafico1.jpg](grafico1.jpg)
[Imagen extraída de arxiv.org](https://arxiv.org/html/2604.25917v1)

## Inner loop, outer loop: entrenar un sistema entero

La otra innovación estructural del framework se refiere al método de entrenamiento. Optimizar un sistema multi-agente recursivo de forma coherente no es trivial: si se entrenan los modelos por separado, cada uno aprende a comportarse bien de forma aislada, pero no necesariamente a colaborar. Si, en cambio, se intenta optimizarlos todos juntos desde el principio, la complejidad explota y los gradientes tienden a desvanecerse a través de los rounds recursivos.

RecursiveMAS propone un algoritmo de dos fases llamado *inner-outer loop learning*. En la primera fase, el inner loop entrena en paralelo y de forma independiente el *inner link* de cada agente, utilizando como objetivo la cosine similarity entre los pensamientos latentes producidos y la distribución de los tokens correctos en la capa de embedding. Se trata de un warm-start: se enseña a cada agente a pensar en latent space sin preocuparse todavía de cómo interactuará con los demás.

En la segunda fase, el outer loop optimiza todo el sistema como unidad. El framework se despliega durante *n* rounds recursivos, y solo al final del último round se produce una respuesta textual sobre la cual calcular la pérdida (loss). El gradiente se propaga luego hacia atrás (backpropagated) a través de toda la cadena recursiva, asignando a cada outer link una señal de crédito compartida basada en su contribución a la predicción final. Cada link aprende, por tanto, no solo de su propio error local, sino de la calidad global de todo el sistema en cada ejemplo individual.

El teorema central del paper (Teorema 4.1) demuestra formalmente por qué este enfoque funciona mejor que el basado en texto: los gradientes que transitan a través de los RecursiveLink residuales permanecen estables a través de los rounds, mientras que en el caso del texto, donde la proyección sobre el vocabulario introduce una discontinuidad, tienden a colapsar hacia cero con el aumento de la profundidad recursiva. Un gradiente que se desvanece significa un sistema que deja de aprender.

## Los números: nueve benchmarks, cuatro patrones

RecursiveMAS ha sido probado en nueve benchmarks que cubren matemáticas (MATH500, AIME 2025, AIME 2026), ciencia y medicina (GPQA-Diamond, MedQA), generación de código (LiveCodeBench, MBPP+) y búsqueda web (HotpotQA, Bamboogle). Los modelos involucrados incluyen Qwen3/3.5, LLaMA-3, Gemma3 y Mistral, en configuraciones desde menos de 1,5 mil millones hasta unos 10 mil millones de parámetros por agente.

Los resultados con respecto a todas las baseline —agente único con LoRA, agente único con full fine-tuning, Mixture-of-Agents, TextGrad, LoopLM, Recursive-TextMAS— muestran una mejora media de 8,3 puntos porcentuales de precisión. La ganancia más notable se registra en los benchmarks de razonamiento matemático denso: en AIME 2025, la versión *scaled* de RecursiveMAS alcanza el 86,7% frente al 73,3% de la mejor baseline comparable. La ventaja, algo importante, crece con la profundidad recursiva: con *r* = 1 (un solo round), la mejora media es de 3,4 puntos; con *r* = 3, sube a 7,2. Los sistemas textuales, por comparación, tienden en cambio a empeorar o a estabilizarse con la recursión más profunda, señal de que acumulan errores en cada round, en lugar de refinarse.

En el frente de la eficiencia, los datos son aún más claros. En comparación con un sistema multi-agente recursivo equivalente pero basado en texto, RecursiveMAS ofrece un speedup de 1,2× con *r* = 1 hasta 2,4× con *r* = 3, con una reducción de los tokens consumidos que pasa del 34,6% al 75,6%. El coste de entrenamiento estimado es de 4,27 dólares frente a los 9,67 del fine-tuning completo, y con menos memoria GPU: 15,29 GB de pico frente a los 41,40 requeridos por el full SFT.

El framework ha sido probado en cuatro patrones de colaboración distintos: *Sequential* (Planner, Critic, Solver en secuencia), *Mixture* (especialistas en paralelo agregados por un Summarizer), *Distillation* (un agente experto más grande que instruye a un agente aprendiz más pequeño), y *Deliberation* (un Reflector interno acoplado con un Tool-Caller que accede a Python y APIs de búsqueda). En los cuatro contextos, RecursiveMAS supera al agente único más fuerte de la configuración correspondiente.

## Cuando los agentes dejan de hablar

Hasta aquí los números. Pero hay una pregunta que los números no resuelven, y que se refiere a algo más incómodo: si los agentes ya no se hablan en lenguaje natural, ¿cómo entiende un ser humano lo que está sucediendo?

En los sistemas multi-agente tradicionales, cada intercambio textual entre agentes es, en principio, legible. Un ingeniero puede abrir el log, recorrer la conversación entre el Planner y el Solver, entender dónde el razonamiento tomó una dirección equivocada, intervenir. El rastro textual es una forma de transparencia implícita: el sistema piensa en voz alta, y esa voz es comprensible.

En RecursiveMAS, los rounds intermedios no producen texto. Los pensamientos latentes, representaciones vectoriales de alta dimensionalidad que transitan entre los modelos a través de los RecursiveLink, no tienen una traducción natural al lenguaje humano. El paper incluye análisis de las distribuciones semánticas en el espacio latente a través de los rounds, mostrando que la coherencia semántica se mantiene y que los conceptos relevantes se cristalizan progresivamente, pero esta es una tranquilidad técnica, no una ventana accesible a la cognición del sistema.

La verdadera contribución de RecursiveMAS, como observa un análisis en Towards AI, es la extensión del estilo COCONUT —pensamiento continuo en latent space— a través de los agentes mediante el adaptador RecursiveLink. Pero COCONUT, presentado por Meta en 2024, ya había planteado esta preocupación en el contexto del modelo único: cuando un sistema razona sin emitir texto intermedio, los mecanismos estándar de interpretabilidad, análisis de la atención, probing de capas, steering vectorial, se vuelven mucho más difíciles de aplicar a todo el flujo computacional.

La comunidad de investigación sobre interpretabilidad mecanicista, que en los últimos años ha logrado avances notables en la comprensión de cómo los transformers individuales procesan la información, se enfrenta a una nueva frontera: sistemas en los que las unidades de análisis ya no son las capas de un solo modelo, sino los pasos latentes entre modelos heterogéneos. El paper de RecursiveMAS no aborda este punto de forma explícita, una laguna que merece ser señalada.

No se trata de alarmismo. La mayoría de las aplicaciones prácticas de estos sistemas —generación de código, respuesta a preguntas, razonamiento matemático— no requiere transparencia en tiempo real sobre los rounds intermedios. El punto es más sutil: en escenarios de despliegue de alto riesgo, o cuando un sistema produce un resultado inesperado y es necesario entender por qué, la falta de rastro textual intermedio hace que el debugging sea estructuralmente más difícil. El coste de la velocidad se paga, en parte, en comprensibilidad.
![grafico2.jpg](grafico2.jpg)
[Imagen extraída de arxiv.org](https://arxiv.org/html/2604.25917v1)

## Límites, vacíos y honestidad intelectual

El paper no dedica una sección explícita a sus propios límites, una elección editorial común en la investigación académica, pero que vale la pena compensar con un análisis externo.

El primer punto es la naturaleza de los benchmarks. Los nueve test utilizados son datasets estandarizados, construidos en torno a problemas con respuesta verificable y unívoca: ecuaciones, opciones múltiples en medicina, problemas de competición matemática, generación de código evaluada con test automáticos. Son los benchmarks sobre los que la comunidad mide los avances, y tienen sentido como comparación comparativa. Pero no dicen nada sobre cómo se comportaría RecursiveMAS en tareas abiertas, redacción de documentos largos, análisis de textos ambiguos, planificación multi-paso con feedback humano, donde la calidad de la respuesta no es binaria y el proceso cuenta tanto como el resultado.

El segundo punto se refiere a las herramientas externas. El patrón *Deliberation* incluye el uso de Python y APIs de búsqueda, y es alentador que el framework aguante también en este contexto. Pero la integración con herramientas externas se ha mantenido deliberadamente simple: dos tipos de herramientas, en una configuración controlada. Los sistemas agénticos reales en producción gestionan decenas de herramientas heterogéneas, con latencias variables, errores de red, outputs no estructurados. ¿Cómo se comporta RecursiveLink cuando la cadena latente se ve interrumpida por una llamada a una API que tarda tres segundos? Esta pregunta aún no tiene respuesta.

El tercer límite es la escalabilidad. Las pruebas presentadas involucran como máximo a cuatro agentes. Las arquitecturas multi-agente en producción pueden llegar fácilmente a decenas de agentes especializados. La complejidad teórica del sistema escala linealmente con el número de agentes *N*, pero la gestión práctica de los RecursiveLink entre familias de modelos cada vez más diversas, con diferentes hidden sizes, diferentes tokenizers, diferentes especializaciones, es un problema de ingeniería no trivial sobre el cual el paper no se pronuncia.

Por último, está la cuestión de la reproducibilidad. En el momento de la publicación, el [repositorio GitHub oficial](https://github.com/RecursiveMAS/RecursiveMAS) incluye el código para la inferencia y la demo, pero señala como aún en curso la publicación del pipeline completo de entrenamiento y de los datos de entrenamiento. Verificar de forma independiente los resultados reportados, práctica esencial en la comunidad científica, requiere por tanto esperar a que estos activos sean publicados.

## Un punto de inflexión, no un punto de llegada

RecursiveMAS es la primera demostración de que la recursión puede funcionar como principio arquitectónico a nivel de sistema, desplazando la conversación de "¿cómo optimizamos cada agente individual?" a "¿cómo hacemos que el sistema evolucione como una entidad unificada?". Los números —+8,3% de precisión media, velocidad hasta 2,4 veces superior, tres cuartas partes de tokens ahorrados, coste de entrenamiento reducido a la mitad— se han obtenido en condiciones controladas y deben leerse con esa cautela, pero no pueden ignorarse.

Las preguntas más difíciles siguen abiertas: ¿cuánto escala con decenas de agentes? ¿Cómo se comporta en tareas reales y ambiguas? ¿Cómo se mantiene la comprensibilidad cuando los rounds intermedios se vuelven invisibles? Quien construye sistemas de AI para entornos críticos tiene todo el interés en no descartarlas como detalles de implementación.

Una cosa parece clara: el futuro de los agentes de AI no será una cadena lineal de prompts y respuestas. Será un loop. La cuestión es quién decidirá cómo se diseña ese loop y con qué garantías de transparencia sobre lo que sucede en su interior.
