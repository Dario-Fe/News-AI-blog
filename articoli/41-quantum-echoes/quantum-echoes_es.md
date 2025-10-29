---
tags: ["Research", "Training", "Applications"]
date: 2025-10-29
author: "Dario Ferrero"
---

# Computadoras cuánticas: Google presenta 'Quantum Echoes', ¿será la gloria verdadera?
![qubit-google.jpg](qubit-google.jpg)

*El 22 de octubre de 2025, Google publicó en [Nature](https://www.nature.com/articles/s41586-025-09526-6) un estudio que probablemente marca el paso más significativo en la historia de la computación cuántica: de "podemos hacer algo impresionante pero fundamentalmente inútil" a "podemos hacer algo científicamente relevante". El algoritmo Quantum Echoes, ejecutado en el chip [Willow](https://blog.google/technology/research/google-willow-quantum-chip/) de 105 cúbits, demostró por primera vez una ventaja cuántica verificable en un problema real, calculando estructuras moleculares 13.000 veces más rápido que la supercomputadora Frontier, actualmente la más potente del mundo. Pero atención: antes de imaginar computadoras cuánticas que revolucionen la química farmacéutica mañana por la mañana, vale la pena comprender qué significa realmente este anuncio, cuáles son sus limitaciones concretas y por qué algunos investigadores siguen siendo escépticos.*

## La evolución de Willow: de diciembre de 2024 a hoy

Para entender Quantum Echoes, primero debemos retroceder diez meses. En diciembre de 2024, Google había anunciado el chip Willow, un procesador cuántico de 105 cúbits superconductores que representaba un salto cualitativo con respecto al anterior Sycamore de 53 cúbits, el utilizado en el controvertido experimento de 2019 sobre la "supremacía cuántica". Willow había demostrado la capacidad de operar por debajo del umbral crítico de corrección de errores: cuantos más cúbits se añaden, menos errores se obtienen. Un resultado fundamental porque revertía lo que hasta entonces había sido el talón de Aquiles de la computación cuántica, donde cada cúbit adicional significaba tradicionalmente más ruido e inestabilidad.

El chip [Willow utilizado en los experimentos](https://blog.google/technology/research/quantum-hardware-verifiable-advantage/) presentaba una vida media de los estados excitados (T₁) de 106 microsegundos y un tiempo de coherencia (T₂E) de 130 microsegundos, con un error medio de las puertas de dos cúbits del 0,15%. Números que sobre el papel pueden parecer marginales, pero que en la práctica de los sistemas cuánticos representan la diferencia entre el éxito y el fracaso de un cálculo complejo. Para dar una idea de la escala temporal: estos cúbits mantienen su coherencia durante poco más de una décima de milisegundo, una eternidad en comparación con los primeros experimentos, pero aún un parpadeo en comparación con los tiempos de la computación clásica.
![willow.jpg](willow.jpg)
[Imagen extraída de nature.com](https://www.nature.com/articles/s41586-025-09526-6)

## El algoritmo del eco: retroceder en el tiempo cuántico

El corazón de Quantum Echoes es un algoritmo que aprovecha una propiedad contraintuitiva de la mecánica cuántica: la reversibilidad temporal. Pensemos en una gota que cae en un estanque. Las ondas se propagan hacia el exterior en círculos concéntricos cada vez más amplios, perdiendo intensidad. En el mundo clásico, invertir este proceso es imposible: no se puede hacer que las ondas converjan espontáneamente hacia el centro para reconstruir la gota inicial. En el mundo cuántico, en cambio, es posible. O mejor dicho, es posible si se sabe exactamente cómo invertir cada una de las operaciones que se han realizado.

Los científicos de Google implementaron lo que técnicamente se llama un [correlacionador fuera del orden del tiempo de segundo orden](https://research.google/blog/a-verifiable-quantum-advantage/) (OTOC(2)), pero que es más intuitivo imaginar como un experimento de "sonar de eco cuántico". Como cuenta el [blog oficial de Google](https://blog.google/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/), el proceso se articula en cuatro fases: se ejecuta una serie de operaciones cuánticas en una matriz de cúbits, se perturba deliberadamente un único cúbit específico, se invierte exactamente la secuencia de operaciones anterior y, finalmente, se mide el resultado. Si todo funciona perfectamente, el sistema debería volver al estado inicial. Pero si la perturbación ha tenido efecto, el eco que regresa será diferente, y esta diferencia contiene información valiosa sobre cómo se ha difundido la información a través del sistema cuántico.

El truco elegante es que este "eco" se amplifica a través de un fenómeno llamado interferencia constructiva: las ondas cuánticas se suman en fase, reforzándose mutuamente en lugar de anularse. Es un poco como cuando dos ondas de agua se encuentran en el punto justo y crean una ola más alta. En el mundo cuántico, este efecto hace que las mediciones sean increíblemente sensibles a los detalles microscópicos del sistema.

Para ilustrarlo con una metáfora, pensemos en el juego de Mr. Driller, ese juego de puzles japonés en el que se excava a través de capas de bloques de colores: cuanto más se desciende, más compleja se vuelve la estructura que hay que atravesar. En el algoritmo Quantum Echoes, el sistema cuántico "excava" a través de capas cada vez más profundas de correlaciones entre cúbits, y cuando invierte el camino, debe lograr volver exactamente al punto de partida atravesando la misma complejidad. La perturbación es como un bloque de un color diferente insertado a mitad de camino: si al volver ese bloque ha alterado el camino, se sabe por el eco que se recibe.

## Los números que importan: 13.000 veces más rápido, pero ¿en qué?

Aquí llegamos al punto crucial, el que separa el bombo de la realidad. Google afirma que su algoritmo es 13.000 veces más rápido que Frontier, la supercomputadora más potente del mundo con sus 1,2 exaflops de potencia de cálculo. Suena impresionante, pero ¿qué significa exactamente?

Los experimentos publicados en [Nature](https://www.nature.com/articles/s41586-025-09526-6) utilizaron circuitos cuánticos con 65 cúbits activos, para un total de 23 ciclos de operaciones. El equipo de Google midió valores de OTOC(2) que requirieron aproximadamente 2,1 horas de tiempo de recopilación de datos por circuito en el chip Willow. Utilizando algoritmos de contracción de tensores altamente optimizados en Frontier, el mismo cálculo requeriría aproximadamente 3,2 años por cada punto de datos. El factor de 13.000x deriva exactamente de esta comparación: aproximadamente 28.000 horas (3,2 años) divididas por 2,1 horas.

Pero aquí entra en juego la primera gran crítica, planteada precisamente en la revista [Nature](https://www.nature.com/articles/d41586-025-03300-4) por Dries Sels, físico cuántico de la Universidad de Nueva York: "La carga de la prueba debería ser alta. Aunque el artículo hace un trabajo serio al probar varios algoritmos clásicos, no hay demostración de que no exista un algoritmo eficiente". En otras palabras, el hecho de que hoy no conozcamos una forma más rápida de hacer estos cálculos en una computadora clásica no significa que tal forma no exista. Es la misma crítica que se hizo al experimento de supremacía cuántica de 2019.

Sin embargo, el equipo de Google ha hecho un trabajo más profundo esta vez. Como se detalla en el [artículo técnico](https://research.google/blog/a-verifiable-quantum-advantage/), probaron nueve algoritmos de simulación clásica diferentes, gastando el equivalente a diez años-persona en el intento de encontrar atajos clásicos (lo que en la jerga se llama "red teaming"). Utilizaron técnicas de Monte Carlo cuántico, redes de tensores, algoritmos de Monte Carlo con caché y otras estrategias avanzadas. Ninguna logró igualar la precisión del procesador cuántico en el régimen considerado.
![otocs.jpg](otocs.jpg)
[Imagen extraída de nature.com (OTOCs as interferometers.)](https://www.nature.com/articles/s41586-025-09526-6)

## Del experimento molecular a la realidad

Pero Quantum Echoes no es solo un ejercicio abstracto de cálculo. La demostración más interesante es la que se refiere al estudio de moléculas reales, realizada en [colaboración con la Universidad de Berkeley](https://quantumai.google/static/site-assets/downloads/quantum-computation-molecular-geometry-via-nuclear-spin-echoes.pdf). El equipo estudió dos moléculas orgánicas: el tolueno marcado con carbono-13 (15 átomos) y el 3',5'-dimetilbifenilo (28 átomos), ambas suspendidas en cristales líquidos nemáticos.

La idea es extender una técnica llamada resonancia magnética nuclear (RMN), la misma física detrás de las máquinas de resonancia magnética de los hospitales. La RMN funciona como un "microscopio molecular" que permite ver la posición relativa de los átomos midiendo cómo los núcleos atómicos interactúan magnéticamente entre sí. El problema es que cuando dos núcleos están demasiado lejos, aproximadamente más de 6 Ångström (una diezmilmillonésima parte de un metro), su acoplamiento se vuelve demasiado débil para ser medido con técnicas convencionales.

Aquí entra en juego Quantum Echoes. Simulando la dinámica de los espines nucleares en el chip cuántico y comparando los resultados con los datos experimentales de RMN, los investigadores lograron determinar parámetros estructurales de las moléculas con una precisión comparable a la de técnicas espectroscópicas independientes. Para el tolueno, estimaron la distancia media entre los átomos de hidrógeno en posición orto y meta del benceno con un error de apenas 0,01 Ångström. Para el dimetilbifenilo, determinaron la distribución del ángulo diedro entre los dos anillos de benceno, un parámetro crucial para comprender la conformación molecular.

La validación se realizó comparando los resultados cuánticos con experimentos de espectroscopia de coherencia cuántica múltiple en una muestra deuterada independiente. Los datos concuerdan dentro de los márgenes de error, demostrando que el enfoque funciona, al menos en principio.

## Las aplicaciones prometidas: ¿del laboratorio a la farmacia?

Google pinta escenarios ambiciosos. Hartmut Neven, jefe del laboratorio cuántico de Google en Santa Bárbara, declaró durante la rueda de prensa que "este algoritmo ofrece la oportunidad de aplicaciones en el mundo real" y que la empresa es optimista de que en cinco años habrá usos prácticos para las computadoras cuánticas.

Los ámbitos prometidos van desde el descubrimiento de fármacos hasta la ciencia de los materiales. En particular, el algoritmo podría ayudar a determinar cómo los posibles medicamentos se unen a sus dianas biológicas, uno de los desafíos más computacionalmente intensivos de la química farmacéutica. O podría caracterizar la estructura molecular de nuevos materiales como polímeros avanzados, componentes para baterías o incluso los materiales que componen los propios cúbits cuánticos.

Pero aquí entran en juego las distinciones cruciales. Como subrayó [Tom O'Brien](https://blog.google/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/), investigador de Google Quantum AI en Múnich, "aplicar el algoritmo Quantum Echoes a sistemas más complejos requerirá hardware menos ruidoso o métodos para corregir errores que aún están en fase de desarrollo". En otras palabras, lo que funciona con el tolueno y el dimetilbifenilo no se escala automáticamente a proteínas con cientos de aminoácidos o cristales con miles de átomos.

James Whitfield, físico cuántico del Dartmouth College, fue aún más explícito en su entrevista con [Nature](https://www.nature.com/articles/d41586-025-03300-4): "El avance técnico es impresionante, pero es un poco forzado pensar que esto resolverá de repente algún problema económicamente relevante".

La limitación fundamental es que, por ahora, el algoritmo solo funciona en moléculas lo suficientemente simples como para poder ser simuladas eficientemente también de forma clásica. El [preprint enviado a arXiv](https://quantumai.google/static/site-assets/downloads/quantum-computation-molecular-geometry-via-nuclear-spin-echoes.pdf) admite con franqueza: "Debido a la complejidad intrínseca de la simulación de sistemas reales y a las limitaciones de rendimiento de nuestro chip actual, esta demostración inicial aún no está más allá de lo clásico".
![octos2.jpg](octos2.jpg)
[Imagen extraída de nature.com (Sensitivity of OTOCs towards microscopic details of quantum dynamics.)](https://www.nature.com/articles/s41586-025-09526-6)

## Ventaja cuántica vs. supremacía cuántica: diferencias sustanciales

Vale la pena detenerse un momento en la diferencia entre lo que se hizo en 2019 y lo que se ha demostrado hoy. En 2019, con el chip Sycamore, Google había demostrado la llamada "supremacía cuántica" (ahora más comúnmente llamada "ventaja computacional cuántica"): había realizado en 200 segundos un cálculo que habría requerido 10.000 años en la supercomputadora más potente de la época. Sonaba espectacular, y técnicamente lo era, pero había un problema: el cálculo en cuestión carecía por completo de utilidad práctica. Se trataba de muestrear cadenas aleatorias de un estado cuántico altamente caótico, un problema diseñado específicamente para ser difícil para las computadoras clásicas pero fácil para las cuánticas.

Como se explica en el [artículo de Nature](https://www.nature.com/articles/s41586-025-09526-6), con el Muestreo de Circuitos Aleatorios "la misma cadena de bits nunca aparece dos veces en un sistema cuántico grande, lo que limita su capacidad para revelar información útil". Era el equivalente a demostrar que tu coche de Fórmula 1 puede vencer a cualquier otro coche en un circuito diseñado específicamente para favorecerlo, pero en el que nadie querría correr por motivos prácticos.

Quantum Echoes es diferente porque mide valores de expectación cuánticos, es decir, cantidades físicas reales como la corriente, la velocidad, la magnetización o la densidad. Estos valores son verificables: si se repite el experimento en otra computadora cuántica de igual calidad, se debería obtener el mismo resultado. Y, sobre todo, son relevantes para describir sistemas físicos reales, desde moléculas hasta imanes y agujeros negros (sí, el algoritmo OTOC también tiene aplicaciones en la física teórica de los agujeros negros, pero eso es otro tema).

La verificabilidad es la clave. Xiao Mi y Kostyantyn Kechedzhi, investigadores de Google Quantum AI y autores principales del [estudio técnico](https://research.google/blog/a-verifiable-quantum-advantage/), subrayan que "a diferencia de las cadenas de bits, los valores de expectación cuánticos son resultados computacionales verificables que permanecen iguales cuando se ejecutan en diferentes computadoras cuánticas". Esto abre un camino directo hacia el uso de OTOC para resolver problemas del mundo real utilizando computadoras cuánticas que no es posible resolver en computadoras clásicas.

## Los tres hitos y el camino hacia el futuro

Google Quantum AI tiene una hoja de ruta pública con varios hitos por alcanzar. El equipo afirma haber superado tres hitos fundamentales: la capacidad de ejecutar circuitos cuánticos complejos con una baja tasa de error, la demostración de corrección de errores por debajo del umbral con Willow, y ahora esta primera ventaja cuántica verificable en un problema con potencial aplicación práctica.

El próximo objetivo, lo que llaman "Hito 3" en su [hoja de ruta pública](https://quantumai.google/roadmap), es alcanzar un cúbit lógico de larga vida, es decir, un cúbit protegido por corrección de errores que pueda mantener su información durante tiempos suficientemente largos como para permitir cálculos complejos. Solo en ese momento se podrá hablar de computación cuántica tolerante a fallos, resistente a los errores, el Santo Grial del sector.

El plazo de cinco años citado por Neven para aplicaciones prácticas es ambicioso pero no del todo irreal. El problema es que depende de una serie de "si" significativos: si logran escalar el número de cúbits manteniendo la calidad, si logran implementar la corrección de errores de manera eficiente, si logran desarrollar algoritmos más refinados, si el ruido del hardware sigue disminuyendo.

Un aspecto interesante, a menudo pasado por alto en el debate público, es que el equipo utilizó [AlphaEvolve](https://quantumai.google/static/site-assets/downloads/quantum-computation-molecular-geometry-via-nuclear-spin-echoes.pdf), un agente de codificación basado en modelos de lenguaje grandes, para optimizar la compilación de los circuitos cuánticos para el experimento del dimetilbifenilo. El algoritmo evolutivo logró reducir el error medio del 10,4% al 0,82% generando fórmulas de producto más eficientes en comparación con el primer orden de Trotter estándar. Es un ejemplo de cómo la IA ya está desempeñando un papel en la mejora de la eficiencia de los algoritmos cuánticos.
![octos3.jpg](octos3.jpg)
[Imagen extraída de nature.com (Quantum interference and classical simulation complexity of OTOC)](https://www.nature.com/articles/s41586-025-09526-6)

## Las críticas ocultas en los detalles técnicos

Al profundizar en los suplementos técnicos del artículo, surgen detalles que redimensionan el entusiasmo. Para mitigar los errores de hardware, el equipo tuvo que implementar un pipeline de cuatro etapas que incluye filtros de cono de luz de doble cara, extrapolación de ruido cero basada en los caminos de Pauli, secuencias de desacoplamiento dinámico y twirling de puertas sub-Clifford. En la práctica, tuvieron que aplicar una batería de correcciones de software para extraer una señal limpia de datos muy ruidosos.

En los circuitos más profundos para la molécula de 15 espines, la señal bruta medida era de apenas 0,055 ± 0,003, un valor extremadamente pequeño sumergido en el ruido. Solo mediante sofisticadas técnicas de mitigación de errores lograron extraer datos utilizables. Esto plantea una pregunta legítima: ¿cuánto de esta "ventaja cuántica" es intrínseco a la física cuántica y cuánto es simplemente una demostración de una excelente ingeniería de software de corrección?

Otro aspecto crítico se refiere al error de Trotterización. El algoritmo no simula la dinámica molecular exacta, sino una aproximación discreta llamada fórmula de Trotter. El error introducido por esta aproximación se estima en aproximadamente 0,035 para el tolueno, que se suma al error experimental residual de 0,050 después de la mitigación. Esto conduce a un error cuadrático medio total de 0,058 entre los datos cuánticos y la simulación clásica exacta. No está mal, pero tampoco es despreciable.

Además, los circuitos más profundos utilizados requerían hasta 1.080 puertas de dos cúbits para simular los primeros seis pasos temporales de la curva OTOC del tolueno. Con un error medio por puerta de dos cúbits de aproximadamente 0,15%, el error se acumula rápidamente. Es la razón por la que Tom O'Brien admitió que se necesita hardware menos ruidoso para ir más allá de estos sistemas de juguete.

## AlphaEvolve y la optimización de algoritmos

Una contribución a menudo subestimada en este trabajo es el uso de AlphaEvolve para optimizar los circuitos cuánticos, particularmente para el experimento del dimetilbifenilo. AlphaEvolve es un agente de codificación evolutivo que utiliza modelos de lenguaje para descubrir soluciones eficientes a problemas científicos complejos.

El proceso parte de un programa escrito por humanos (una fórmula de Trotter de primer orden) que sirve como solución inicial. Mediante mutación, evaluación y selección, AlphaEvolve genera una población de programas que producen circuitos con un error de aproximación significativamente menor que la referencia, pasando de un error medio del 10,4% al 0,82%, sin dejar de estar por debajo del presupuesto de puertas impuesto por el hardware.

Lo interesante es que el sistema no genera circuitos directamente, sino que escribe código Python que construye circuitos. Esto tiene dos ventajas clave: el código resultante puede generalizar a parámetros y tiempos fuera del conjunto de entrenamiento, y el código puede ser analizado y comprendido por los humanos. Al examinar el suplemento técnico, se desprende que AlphaEvolve implementó una mezcla de poda del cono de luz, ordenación de términos y cúbits, pasos temporales adaptativos y reescalado de términos basado en la distancia, algunas de las cuales ya se habían sugerido en la literatura.

Esto plantea una cuestión filosófica interesante: si necesitamos la IA para optimizar los algoritmos cuánticos para ejecutarlos en computadoras cuánticas, ¿estamos realmente simplificando los problemas o simplemente añadiendo capas de complejidad?

## El problema de la escalabilidad

La pregunta que todos deberían hacerse es: ¿esto escala? La respuesta corta es: aún no lo sabemos. Los propios autores del preprint molecular [admiten](https://quantumai.google/static/site-assets/downloads/quantum-computation-molecular-geometry-via-nuclear-spin-echoes.pdf) que "las estimaciones sugieren distancias accesibles de 20-60 Ångström para mediciones basadas en OTOC, acercándose a la escala de longitud de la transferencia de energía por resonancia de Förster (FRET)". Esto colocaría la técnica más allá del alcance de los enfoques de RMN de vanguardia como PDSD, REDOR y RFDR, todas técnicas que no utilizan inversión temporal.

Pero hay un "pero" del tamaño de una casa. Para sistemas con 50 espines, las estimaciones de los errores de Trotter sugieren que los métodos ingenuos requerirían de 100.000 a un millón de puertas. Es una brecha grande pero no astronómica en comparación con los requisitos de hardware actuales, dado que los problemas se seleccionan cuidadosamente. Como dicen los autores: "No esperamos que esta brecha se supere solo con el hardware físico". Se necesita un progreso algorítmico sustancial.

La física molecular también presenta desafíos específicos. El equipo tuvo que tratar el Hamiltoniano dipolar completamente acoplado con una red de intercambio, una técnica que permite compilar puertas de intercambio a través de un patrón de "muro de ladrillos" de interacciones de dos cúbits. Esto es óptimo tanto en términos del número de puertas como de la profundidad requerida, pero escala mal al aumentar el número de espines. Para el tolueno, aproximaron además que el espín del carbono-13 solo interactuaba con el protón más cercano, reduciendo el número de puertas en un 17%. Esta aproximación estaba justificada porque todos los demás acoplamientos eran dos órdenes de magnitud más pequeños, pero no siempre será posible hacer simplificaciones similares.

## El hardware: una obra maestra de la ingeniería superconductora

Vale la pena dedicar algunas palabras al hardware subyacente. Los cúbits de Willow son circuitos superconductores de tipo transmon, básicamente diminutos osciladores eléctricos que operan a frecuencias de alrededor de 6,2 GHz con una anarmonicidad de aproximadamente 210 MHz. Se enfrían a temperaturas cercanas al cero absoluto, alrededor de 15 milikelvin, utilizando refrigeradores de dilución criogénicos.

Para el experimento del tolueno, implementaron 80 puertas fSim (simulación fermiónica) únicas en todo el panorama de parámetros. A diferencia de trabajos anteriores que usaban un solo pulso, aquí adoptaron un enfoque de dos pulsos: el primer pulso establece el ángulo de intercambio e induce una fase condicional espuria de menos de 100 miliradianes, mientras que un segundo pulso realiza una fase condicional y un intercambio espurio de aproximadamente 30 miliradianes.

La calibración es intensiva pero proporciona un rendimiento y una flexibilidad superiores en comparación con el enfoque de un solo pulso. Adaptaron técnicas de calibración periódica "Floquet" de alta precisión, alcanzando ángulos objetivo con una tolerancia máxima de 20 miliradianes y un error típico inferior a 5 miliradianes. El error XEB mediano para las puertas fSim calibradas fue de 0,0026, con un máximo de 0,0045.

Para el experimento del dimetilbifenilo de 15 cúbits, utilizaron en cambio una descomposición basada en puertas CZ, que no requería la construcción detallada de fSim descrita anteriormente. Esto demuestra la flexibilidad del enfoque arquitectónico de Google.

## La comparación con D-Wave y otros enfoques

Es interesante notar que Google no es la única empresa que reivindica avances recientes en la computación cuántica. D-Wave Systems, que utiliza un enfoque completamente diferente basado en el recocido cuántico en lugar de puertas cuánticas universales, publicó en marzo de 2025 en Science resultados sobre simulaciones magnéticas cuánticas que, según afirman, van más allá de las capacidades de la simulación clásica.

El enfoque de D-Wave es fundamentalmente diferente: en lugar de construir circuitos cuánticos con puertas universales, utiliza un sistema de cúbits que se "recocen" hacia el estado de mínima energía, una técnica útil para problemas de optimización. No está claro qué enfoque prevalecerá a largo plazo, o si ambos tendrán nichos de aplicación distintos.

Otra diferencia crucial con respecto a los sistemas de iones atrapados (como los desarrollados por IonQ o Quantinuum) es la velocidad de las operaciones. Los cúbits superconductores operan en escalas de tiempo de nanosegundos, mientras que los iones atrapados requieren microsegundos por puerta. Esta ventaja en velocidad se paga, sin embargo, con tiempos de coherencia más cortos y tasas de error generalmente más altas. Es el clásico compromiso de ingeniería.

## Las implicaciones para la criptografía: ¿cuándo preocuparse de verdad?

Cada anuncio de avances en la computación cuántica suscita inevitablemente temores sobre la seguridad de la criptografía actual. Vale la pena aclarar: este experimento no tiene nada que ver con la ruptura de la criptografía RSA o de curva elíptica. El algoritmo de Shor para factorizar números grandes requeriría miles o millones de cúbits lógicos con corrección de errores completa, y todavía estamos muy lejos de ese escenario.

Sin embargo, el hecho de que Google esté haciendo progresos constantes en la corrección de errores y la calidad de los cúbits es una señal de que la industria debería tomarse en serio la migración hacia algoritmos poscuánticos. El NIST ya ha estandarizado varios algoritmos resistentes a la computación cuántica, y muchas organizaciones están comenzando la transición. El consejo es: no entren en pánico hoy, pero tampoco pospongan la planificación para mañana.

## Verificabilidad y reproducibilidad: la ciencia bien hecha

Un aspecto positivo a menudo pasado por alto es que Google ha puesto a disposición [los datos brutos y los circuitos cuánticos en Zenodo](https://doi.org/10.5281/zenodo.15640502), permitiendo a otros investigadores verificar y reproducir los resultados. También han publicado el código fuente para las estimaciones de costo de la contracción de tensores en [GitHub](https://github.com/google-research/tnco) bajo una licencia de código abierto.

Esto es ciencia hecha de la manera correcta, donde la transparencia y la reproducibilidad se ponen en primer lugar. No siempre es así en el sector de la computación cuántica, donde algunos anuncios de empresas han pecado de opacidad. El hecho de que el trabajo haya sido sometido a una rigurosa revisión por pares en Nature, con árbitros que plantearon objeciones significativas (como se documenta en la versión publicada), es otro punto a favor de la credibilidad.

## Perspectivas realistas: ¿qué esperar en los próximos años?

Entonces, resumiendo, ¿qué podemos esperar en los próximos cinco años? Probablemente veremos progresos incrementales en varios frentes: chips con más cúbits y tasas de error más bajas, algoritmos mejor optimizados, técnicas de mitigación de errores más sofisticadas y primeras aplicaciones de nicho donde la ventaja cuántica es lo suficientemente grande como para justificar los costos y la complejidad.

Los ámbitos más prometedores a corto plazo son probablemente la simulación de sistemas cuánticos naturales (precisamente como se demostró aquí con la espectroscopia RMN), la optimización de problemas específicos en química computacional y quizás algunas aplicaciones en aprendizaje automático cuántico. No esperen revoluciones inmediatas en el descubrimiento de fármacos o en el diseño de baterías, sino más bien contribuciones incrementales que aceleren investigaciones ya en curso.

El plazo de cinco años de Neven para aplicaciones prácticas es plausible si entendemos "práctica" en un sentido académico-científico: ayudar a los investigadores a responder preguntas que de otro modo requerirían demasiado tiempo o recursos. Si, en cambio, entendemos "práctica" en el sentido de productos comerciales que impactan en la vida cotidiana, probablemente estemos más cerca de los diez o quince años.

## El papel de la dinámica molecular y la corrección de los modelos

Un aspecto sutil pero crucial que surgió del experimento del dimetilbifenilo se refiere a cómo Quantum Echoes puede ayudar a corregir las aproximaciones de las simulaciones de dinámica molecular clásicas. Los investigadores utilizaron el campo de fuerza GAFF 2.11 combinado con parámetros ligados por Grappa 1.3.1 para simular el comportamiento de la molécula en el cristal líquido 5CB.

El problema es que los parámetros de orden de los cristales líquidos son sensibles a la temperatura y difíciles de modelar con precisión con la dinámica molecular. Las simulaciones tienden a subestimar o sobrestimar ciertos grados de libertad. Aquí entra en juego la idea del aprendizaje Hamiltoniano: se comparan los datos OTOC experimentales con simulaciones cuánticas de Hamiltonianos parametrizados, y se optimizan los parámetros hasta que los datos simulados coincidan con el experimento real.

Como se describe en el [preprint en arXiv](https://quantumai.google/static/site-assets/downloads/quantum-computation-molecular-geometry-via-nuclear-spin-echoes.pdf), este enfoque permitió estimar el ángulo diedro medio del dimetilbifenilo con una precisión similar a la de la espectroscopia MQC independiente, mejorando las predicciones de la dinámica molecular bruta en un factor de cuatro en términos de error cuadrático medio.

Esto sugiere un posible paradigma futuro: usar simulaciones clásicas económicas para obtener una primera aproximación de la estructura molecular, y luego refinar los parámetros críticos utilizando mediciones OTOC procesadas por computadoras cuánticas. No es una revolución, pero es un ejemplo concreto de cómo la computación cuántica podría insertarse en los flujos de trabajo científicos existentes.

## El elefante en la habitación: el costo energético

Una pregunta que rara vez se hace en los anuncios entusiastas es: ¿cuánto cuesta en términos energéticos hacer funcionar una computadora cuántica? Los refrigeradores de dilución que mantienen los cúbits superconductores a 15 milikelvin consumen decenas de kilovatios de potencia eléctrica continuamente. La infraestructura criogénica, la electrónica, los sistemas de control, todo esto tiene una huella energética significativa.

La comparación directa con las supercomputadoras es complicada porque Frontier consume unos 21 megavatios a pleno rendimiento, pero opera en miles de nodos en paralelo y puede realizar muchas tareas diferentes simultáneamente. Un solo chip cuántico, por impresionante que sea, realiza un cálculo a la vez y requiere de todos modos una infraestructura de soporte clásica sustancial.

Esto no es un argumento en contra de la computación cuántica, sino un recordatorio de que las comparaciones "13.000 veces más rápido" son siempre parciales. En la vida real, la eficiencia también se mide en julios por operación, en costos operativos totales, en el tiempo necesario para programar y calibrar el sistema. Son todos factores que actualmente favorecen enormemente a los sistemas clásicos para la gran mayoría de las aplicaciones.

## La cuestión del problema del signo y la complejidad clásica

Uno de los aspectos técnicos más interesantes, sepultado en los suplementos del artículo de Nature, se refiere al llamado "problema del signo" en el cálculo de OTOC(2). Los investigadores demostraron que la interferencia constructiva entre bucles de cadenas de Pauli de área arbitrariamente grande crea una barrera fundamental para los algoritmos clásicos de muestreo de Monte Carlo cuántico.

El problema de los signos es un obstáculo conocido en la física computacional: cuando se intenta calcular sumas donde los términos pueden ser tanto positivos como negativos (o más precisamente, tienen fases complejas arbitrarias), los algoritmos estocásticos clásicos fallan porque las cancelaciones entre términos grandes de signo opuesto conducen a resultados pequeños con errores estadísticos enormes.

Como se explica en el [suplemento técnico](https://www.nature.com/articles/s41586-025-09526-6), mapearon el OTOC(2) medio en los circuitos a un modelo magnético con la estructura del grupo simétrico de orden 4, y demostraron numéricamente que el problema de los signos en este modelo es severo. Esto sugiere que el problema de los signos es una característica inevitable que presenta una barrera para los algoritmos de muestreo clásicos al calcular OTOC(2).

Esta es una de las piezas más sólidas del argumento a favor de la ventaja cuántica: no se trata solo de "no hemos encontrado un algoritmo clásico mejor", sino de "hay razones teóricas fundamentales por las que ciertos algoritmos clásicos no pueden funcionar". Naturalmente, esto no excluye que exista algún algoritmo clásico completamente diferente que eluda el problema, pero hace que la afirmación sea más robusta.

## La metáfora de la regla molecular

Una de las descripciones más eficaces proporcionadas por el equipo de Google es la de la "regla molecular cuántica". La RMN convencional puede medir distancias entre núcleos atómicos de hasta unos 6 Ångström para pares de carbono-13. Más allá de esta distancia, el acoplamiento dipolar se vuelve demasiado débil para ser resuelto.

La idea detrás de Quantum Echoes aplicada a la RMN es que, en lugar de mirar acoplamientos individuales, se observa cómo la polarización se propaga a través de toda la red de espines nucleares. Es un poco como pasar de medir distancias con una cuerda tensa (que solo funciona para distancias cortas) a lanzar una piedra a un estanque y cronometrar cuánto tardan las ondas en llegar a diferentes puntos (lo que puede funcionar para distancias mayores).

El límite teórico estimado para las distancias accesibles con este enfoque es de 20-60 Ångström, acercándose a la escala de técnicas completamente diferentes como la transferencia de energía por resonancia de Förster (FRET) utilizada en biología. Si esto se realizara en la práctica, abriría posibilidades genuinas para estudiar estructuras proteicas complejas, ensamblajes moleculares y otros sistemas donde las restricciones de distancia de largo alcance son cruciales pero difíciles de obtener.

Sin embargo, hay un abismo entre "estimado en principio" y "demostrado experimentalmente". Por ahora, los experimentos han validado el concepto en sistemas que aún pueden ser simulados clásicamente. El siguiente paso crítico sería demostrar su utilidad en un sistema donde la simulación clásica falla pero el método cuántico sigue funcionando de manera fiable.

## El ecosistema más amplio: ¿qué están haciendo los demás?

Mientras Google hacía estos avances, el resto del ecosistema cuántico no se ha quedado quieto. IBM anunció recientemente avances significativos en su chip Heron con 133 cúbits y tasas de error competitivas. Su hoja de ruta apunta a alcanzar más de 1.000 cúbits para 2026. Rigetti Computing está desarrollando arquitecturas modulares que podrían ser más fácilmente escalables. PsiQuantum está trabajando en cúbits fotónicos a temperatura ambiente, un enfoque radicalmente diferente que evita por completo la criogenia.

Mientras tanto, empresas como Atom Computing y QuEra están explorando cúbits de átomos neutros, que prometen tiempos de coherencia mucho más largos que los superconductores pero con velocidades de puerta más lentas. Microsoft está invirtiendo fuertemente en cúbits topológicos basados en fermiones de Majorana, un enfoque que podría ofrecer protección intrínseca contra los errores pero que aún se encuentra en fase de investigación fundamental.

Esta diversidad de enfoques es saludable. Aún no está claro qué arquitectura prevalecerá, y probablemente diferentes tecnologías encontrarán nichos de aplicación distintos. Los superconductores de Google son excelentes en velocidad y flexibilidad, pero sufren de tiempos de coherencia cortos. Los iones atrapados tienen una coherencia excelente pero son lentos. Los fotones operan a temperatura ambiente pero son difíciles de hacer interactuar. Es la típica fase de exploración tecnológica donde compiten múltiples soluciones.

## Las preguntas que quedan abiertas

Cerramos con las preguntas honestas que toda persona racional debería hacerse ante este anuncio:

**Primero**: ¿es este resultado reproducible por equipos independientes? Hasta ahora, solo Google tiene el hardware necesario para verificarlo. Sería importante ver a laboratorios académicos u otros actores industriales replicar experimentos similares en hardware diferente.

**Segundo**: ¿escala realmente la técnica a sistemas interesantes? Los propios autores admiten que se necesitan avances sustanciales tanto en el hardware como en los algoritmos. La distancia entre simular tolueno y simular una proteína funcional es enorme.

**Tercero**: ¿existen realmente aplicaciones donde la ventaja cuántica sea lo suficientemente grande como para justificar los costos y la complejidad? Por ahora, la respuesta es "quizás, en nichos muy específicos". En cinco años podría cambiar, pero no está garantizado.

**Cuarto**: ¿cuánto de este progreso es transferible a otras arquitecturas cuánticas? Los algoritmos OTOC son generales, pero las técnicas de mitigación de errores y optimización desarrolladas para los superconductores podrían no funcionar bien en iones atrapados u otros sistemas.

**Quinto**: ¿hay aplicaciones asesinas que aún no hemos imaginado? La historia de la tecnología está llena de inventos que encontraron usos completamente inesperados. El láser fue llamado "una solución en busca de un problema" cuando se inventó. Quizás las computadoras cuánticas encuentren su aplicación asesina en dominios que ahora ni siquiera estamos considerando.

## Conclusiones: progresos reales en un campo difícil

Quantum Echoes representa un progreso genuino en la computación cuántica, probablemente el más significativo de los últimos años en términos de relevancia científica. No es el bombo vacío de la supremacía cuántica de 2019, ni es la revolución inminente que algunos titulares sensacionalistas querrían hacernos creer.

Es un paso sólido hacia computadoras cuánticas que pueden contribuir a resolver problemas científicos reales, aunque todavía a escalas limitadas y con muchas reservas. El camino hacia computadoras cuánticas universales que superen a las clásicas en una amplia gama de aplicaciones prácticas sigue siendo largo e incierto. Pero por primera vez, parece que estamos caminando por un sendero real en lugar de dar vueltas en círculo en un terreno abstracto.

El hecho de que el algoritmo sea verificable, que los resultados moleculares concuerden con técnicas espectroscópicas independientes, que el equipo haya hecho un esfuerzo serio por excluir atajos clásicos y que todo el enfoque se inserte en flujos de trabajo científicos existentes son todas señales positivas. No es el final del viaje, probablemente ni siquiera la mitad, pero es un punto de referencia tangible que podemos tomar en serio.

La comunidad científica sigue siendo, con razón, escéptica, como debe ser. Las afirmaciones extraordinarias requieren pruebas extraordinarias, y aunque Google ha proporcionado pruebas sustanciales, quedan preguntas legítimas sobre la escalabilidad, la utilidad práctica a corto plazo y la existencia de posibles algoritmos clásicos mejores aún no descubiertos.

En los próximos años veremos si este trabajo marcará realmente el comienzo de la era de la utilidad cuántica o si se revelará como otra etapa impresionante pero no decisiva en un viaje aún muy largo. Por ahora, podemos decir que el eco cuántico de Google suena decididamente más fuerte que antes, aunque todavía tenemos que esperar para entender si está resonando hacia algo verdaderamente revolucionario o si es solo un eco más sonoro en una cueva aún muy profunda.