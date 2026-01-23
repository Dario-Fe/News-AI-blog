---
tags: ["Research", "Training", "Ethics & Society"]
date: 2026-01-23
author: "Dario Ferrero"
---

# Cuando los modelos científicos empiezan a pensar igual
![convergenza-modelli-scientifici .jpg](convergenza-modelli-scientifici .jpg)


*¿Recuerdan cuando [hablamos del "AI slop"](https://aitalk.it/it/ai-slop-entropia.html), esa avalancha de contenido sintético que está inundando YouTube y el resto de internet? La investigación de Kapwing nos mostró un panorama alarmante: el 21% de los videos recomendados a los nuevos usuarios es puro "slop" generado por IA, contenido producido en masa sin supervisión humana, diseñado solo para acumular visualizaciones. Otro 33% cae en la categoría de "brainrot", clips repetitivos e hipnóticos sin sustancia. En total, más de la mitad de los primeros 500 videos que encuentra una nueva cuenta de YouTube no contienen creatividad humana significativa.*

Pero eso era solo la superficie del problema. Hoy les cuento qué sucede cuando profundizamos más, cuando no miramos el contenido generado por la IA, sino las representaciones internas que estos sistemas desarrollan. Y aquí surge un escenario aún más inquietante: los modelos científicos de inteligencia artificial están convergiendo todos hacia la misma forma de "ver" la materia. No porque hayan alcanzado una comprensión universal de la física, sino porque todos están limitados por los mismos datos.

Un equipo de investigadores del MIT acaba de publicar un [estudio sobre 59 modelos científicos de IA](https://arxiv.org/html/2512.03750v1), sistemas entrenados en diferentes conjuntos de datos, con diferentes arquitecturas, que operan en distintas modalidades como cadenas químicas, coordenadas atómicas tridimensionales y secuencias de proteínas. La pregunta era simple: ¿están estos modelos aprendiendo realmente la física subyacente de la materia, o simplemente están memorizando patrones de sus datos de entrenamiento?

Los resultados son tan sorprendentes como preocupantes. Los modelos muestran una "alineación representacional" muy fuerte, desarrollando representaciones internas de la materia extrañamente similares entre sí. Es como si estuvieran convergiendo hacia una "física común" oculta en sus neuronas artificiales. Los investigadores midieron este fenómeno con cuatro métricas diferentes, desde la alineación local de los vecinos más próximos (CKNNA) hasta la correlación de distancia global (dCor) y la dimensión intrínseca de los espacios latentes, y todas apuntan en la misma dirección.

## La convergencia inevitable

Tomemos el caso de los modelos entrenados en moléculas pequeñas del conjunto de datos QM9. Aquí encontramos sistemas que operan con cadenas SMILES, esas secuencias alfanuméricas que codifican estructuras químicas como "CC(C)C1CCC(C)CC1=O", y modelos que, en cambio, procesan directamente las coordenadas 3D de los átomos en el espacio. Parecerían enfoques radicalmente diferentes, y sin embargo, sus espacios latentes muestran una alineación sorprendente. Los modelos basados en SMILES y los basados en coordenadas atómicas coinciden en qué moléculas son similares entre sí, a pesar de que uno trabaja con cadenas planas y el otro con geometrías tridimensionales.

El fenómeno es aún más marcado con las proteínas. Los modelos que procesan secuencias de aminoácidos, como ESM2 o ESM3, se alinean casi perfectamente con los que operan en estructuras proteicas tridimensionales. La convergencia es el doble de la observada para las moléculas pequeñas. Esto sugiere que los grandes modelos de secuencias de proteínas han aprendido implícitamente las restricciones del plegamiento de proteínas, acercando naturalmente sus espacios latentes a los de los modelos estructurales.

Pero hay más. A medida que los modelos mejoran en su rendimiento, medido como la capacidad de predecir la energía total de las estructuras materiales, sus representaciones convergen cada vez más hacia las del mejor modelo. Es un patrón que recuerda a la "Hipótesis de la Representación Platónica" ya observada en los modelos de visión y lenguaje: la idea de que diferentes sistemas, al mejorar, convergen hacia una representación compartida de la realidad.

Los investigadores incluso construyeron un "árbol evolutivo" de los modelos científicos, utilizando las distancias en los espacios representacionales para medir cuán "emparentados" están. Y aquí surge un detalle crucial: los modelos se agrupan más por el conjunto de datos de entrenamiento que por la arquitectura. Dos modelos con arquitecturas completamente diferentes pero entrenados con los mismos datos se parecen más que dos modelos con la misma arquitectura pero entrenados con datos diferentes. El mensaje es claro: son los datos, no la arquitectura, los que dominan el espacio representacional.

## Trampas en la distribución

Pero esta aparente maduración científica esconde un peligro sistémico. Los investigadores probaron los modelos tanto en estructuras "dentro de la distribución", materiales similares a los vistos durante el entrenamiento, como en estructuras "fuera de la distribución", como moléculas orgánicas mucho más grandes y complejas. Y aquí el panorama se invierte por completo.

En las estructuras dentro de la distribución, como las del conjunto de datos OMat24 de materiales inorgánicos, los mejores modelos muestran una fuerte alineación entre sí, mientras que los más débiles divergen en subóptimos locales del espacio representacional. Es el comportamiento que esperaríamos: los modelos de alto rendimiento convergen hacia una representación compartida y generalizable, los débiles se pierden en soluciones fuera de lo común.

Pero cuando salen de su zona de confort, probados en moléculas orgánicas grandes del conjunto de datos OMol25, casi todos los modelos colapsan. No solo empeoran en las predicciones, sino que sus representaciones convergen hacia variedades arquitectónicas casi idénticas pero pobres en información. Es como si, ante lo desconocido, perdieran toda capacidad distintiva y se refugiaran en los sesgos inductivos codificados en sus arquitecturas.

Los investigadores visualizaron este colapso utilizando la métrica del desequilibrio de información, que mide asimétricamente cuánta información contiene una representación en comparación con otra. Para las estructuras dentro de la distribución, los modelos débiles están dispersos, cada uno aprendiendo información diferente y ortogonal. Para las de fuera de la distribución, todos se agrupan en la esquina inferior izquierda del gráfico: representaciones casi idénticas, todas igualmente incompletas.

El problema es sistémico. Los conjuntos de datos más populares para el entrenamiento, como MPTrj, sAlex y OMat24, están dominados por simulaciones DFT basadas en el funcional PBE, un estándar computacional occidental. Esto crea un monocultivo de datos que excluye sistemáticamente la química exótica, las biomoléculas de ecosistemas no occidentales y las configuraciones atómicas raras. Los modelos convergen no porque estén descubriendo leyes universales de la materia, sino porque todos son alimentados con las mismas sopas computacionales.
![convergenza-modelli-scientifici.jpg](convergenza-modelli-scientifici.jpg)
[Imagen de arxiv.org](https://arxiv.org/html/2512.03750v1)

## La entropía que se propaga

Y aquí el círculo se cierra con el "AI slop" del que hablamos al principio. Porque lo que está sucediendo en los modelos científicos es solo un caso particular de un fenómeno mucho más amplio: el colapso global del modelo.

Imaginen lo que sucede cuando los datos sintéticos generados por la IA se utilizan para entrenar nuevas IA. Es exactamente lo que está sucediendo en YouTube: 278 canales producen exclusivamente "slop", acumulando 63 mil millones de visualizaciones y 117 millones de dólares anuales en ingresos publicitarios. Este contenido sintético no es neutral, lleva consigo los sesgos, las limitaciones y las representaciones convergentes de los modelos que lo generaron.

En el caso de los modelos científicos, esto significa que las simulaciones DFT generadas por IA, ya limitadas por el funcional PBE y los sistemas químicos "comunes", se utilizarán para entrenar a la próxima generación de modelos. Y estos, a su vez, convergerán aún más estrechamente en las mismas representaciones, excluyendo progresivamente las periferias del espacio químico.

Es el fenómeno del "colapso del modelo" documentado en un [estudio reciente](https://arxiv.org/html/2512.12381v1): cuando los modelos generativos se entrenan recursivamente con datos generados por otros modelos, la diversidad se erosiona generación tras generación. Para los grandes modelos de lenguaje entrenados con texto sintético, esto se manifiesta como una pérdida de creatividad lingüística y dificultad para la generalización entre dominios. Para los modelos científicos, significa un empobrecimiento progresivo de la capacidad de explorar nuevas regiones del espacio químico y material.

El paralelo con el ecosistema de contenidos es inquietante. Así como el "AI slop" en YouTube está desplazando a los creadores humanos a través de economías de unidades negativas (el contenido sintético cuesta casi cero de producir a escala), los datos científicos sintéticos corren el riesgo de devaluar la costosa recopilación de datos empíricos. Realizar experimentos físicos reales, sintetizar nuevos compuestos, recopilar datos experimentales de laboratorios: todo esto requiere tiempo, habilidades y recursos. Generar un millón de estructuras simuladas con un modelo de IA solo requiere potencia de cálculo.

## La geografía de los datos

Las implicaciones van mucho más allá de la química computacional. Los investigadores del MIT señalan que los modelos actuales están "gobernados por los datos, no son fundacionales", lo que significa que aún no son fundacionales en el verdadero sentido del término. Un verdadero modelo fundacional debería generalizar bien a dominios de la materia nunca vistos durante el entrenamiento. En cambio, estos sistemas muestran una fuerte dependencia del conjunto de entrenamiento y un colapso predecible fuera de la distribución.

También hay una dimensión geopolítica. Los conjuntos de datos dominantes provienen de instituciones occidentales, utilizando métodos computacionales estandarizados. Esto crea sesgos estructurales que favorecen la química y los materiales ya bien estudiados, excluyendo sistemáticamente los descubrimientos potenciales en regiones menos exploradas del espacio químico. Es una forma sutil de centralización científica, donde las grandes empresas tecnológicas y farmacéuticas que pueden permitirse la generación de datos a gran escala monopolizarán la IA científica.

Los investigadores sugieren que para alcanzar un verdadero estatus fundacional se requerirán conjuntos de datos sustancialmente más diversos, que cubran regímenes de equilibrio y no equilibrio, entornos químicos exóticos y temperaturas y presiones extremas. Se necesitan políticas para promover conjuntos de datos abiertos y diversos, extensiones de iniciativas como Open Catalyst 2020 pero a una escala mucho mayor.

Sin embargo, también hay una nota positiva oculta en los resultados. El estudio muestra que modelos de tamaños muy diferentes, incluso pequeños, pueden aprender representaciones similares a las de los modelos grandes, si se entrenan bien. Esto abre el camino a la destilación: modelos compactos que heredan la estructura representacional de sistemas enormes, reduciendo las barreras computacionales para la investigación y el desarrollo.

Aún más sorprendente es el caso de los modelos Orb V3, que alcanzan un rendimiento excelente sin imponer la equivariancia rotacional en la arquitectura. En su lugar, utilizan un ligero esquema de regularización llamado "equigrad" que fomenta la cuasi-invariancia de la energía y la cuasi-equivariancia de las fuerzas durante el entrenamiento. ¿El resultado? Sus espacios latentes se alinean fuertemente con arquitecturas completamente equivariantes como MACE y Equiformer V2, pero a costos computacionales mucho más bajos. Es una versión de la "lección amarga" del aprendizaje automático: a menudo, escalar el entrenamiento supera las restricciones arquitectónicas elaboradas.

La lección final es clara: estamos presenciando el surgimiento de una monocultura representacional en la IA científica, alimentada por la convergencia de conjuntos de datos limitados y la proliferación de datos sintéticos. Al igual que con el "AI slop" en YouTube, el problema no es la tecnología en sí, sino la economía de la atención y los recursos que premia la cantidad sobre la calidad, la velocidad sobre la diversidad. La diferencia es que mientras que en YouTube lo peor que puede pasar es ver un gato parlante generado por IA, en la IA científica estamos codificando en nuestros modelos los límites epistémicos que definirán qué medicamentos desarrollaremos, qué materiales descubriremos y qué preguntas científicas consideraremos siquiera dignas de ser planteadas.

El círculo se cierra donde comenzó: la entropía se propaga, no solo en los feeds sociales, sino en los espacios latentes que pretenden representar la materia misma. Y quizás la verdadera pregunta no es si la IA está aprendiendo física, sino si estamos renunciando colectivamente a explorar todo lo que nuestras simulaciones estandarizadas no pueden ver ya.
