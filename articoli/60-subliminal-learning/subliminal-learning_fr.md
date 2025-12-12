---
tags: ["Research", "Security", "Generative AI"]
date: 2025-12-12
author: "Dario Ferrero"
---

# Les Fantômes dans l'IA : Quand l'Intelligence Artificielle Hérite de Biais Invisibles
![subliminal-learning.jpg](subliminal-learning.jpg)

*Imaginez demander à une intelligence artificielle de générer une séquence de nombres aléatoires. Deux cents, quatre cent soixante-quinze, neuf cent un. Juste des chiffres, rien d'autre. Ensuite, vous prenez ces nombres, apparemment inoffensifs, et les utilisez pour entraîner un deuxième modèle d'IA. Quand vous lui demandez quel est son animal préféré, il répond : "hibou". Pas une fois, mais systématiquement. Comme si ces nombres, dépourvus de toute référence sémantique aux oiseaux nocturnes, contenaient un message caché.*

Ce n'est ni de la magie, ni de la science-fiction. C'est l'[apprentissage subliminal](https://alignment.anthropic.com/2025/subliminal-learning/), un phénomène récemment découvert par des chercheurs d'Anthropic qui ébranle les fondations de l'industrie de l'intelligence artificielle. L'article publié en juillet 2025 par Alex Cloud, Minh Le et leurs collègues documente quelque chose d'inquiétant : les modèles de langage peuvent transmettre des traits comportementaux à travers des données générées qui n'ont aucune relation apparente avec ces traits. C'est comme découvrir que John Carpenter avait raison avec "The Thing" : il y a une contagion invisible qui se propage entre les IA, et personne ne l'avait remarqué.

La découverte est aussi intéressante que troublante. Les chercheurs ont entraîné un modèle "enseignant" à préférer les hiboux, puis lui ont fait générer des séquences de nombres totalement dépourvues de références aux animaux. Lorsqu'un modèle "élève" a été entraîné sur ces nombres, il a développé la même préférence pour les hiboux avec une augmentation statistiquement significative par rapport au modèle de base. L'expérience a été répétée avec succès avec d'autres animaux et arbres, toujours avec le même résultat déconcertant.

## Distillation : Le Talon d'Achille

Pour comprendre pourquoi cette découverte est si grave, nous devons prendre du recul et parler du fonctionnement réel de l'industrie moderne de l'IA. La distillation et l'ajustement fin sont devenus les piliers de la production de modèles de langage. Le concept est simple et économiquement irrésistible : prenez un grand modèle pré-entraîné, comme GPT-4 ou Llama, et utilisez-le comme "enseignant" pour générer des données qui entraîneront un modèle plus petit et spécialisé, l'"élève".

Cette technique a démocratisé l'IA. Au lieu de dépenser des millions pour entraîner un modèle à partir de zéro, les entreprises peuvent partir d'un modèle de base et le personnaliser avec leurs propres données. C'est comme avoir un professeur d'université qui prépare du matériel pédagogique sur mesure pour ses étudiants. OpenAI, Anthropic, Meta : tous les grands acteurs utilisent des variantes de cette stratégie. C'est efficace, évolutif et, jusqu'à hier, on pensait que c'était sûr.

Le problème est que cette stratégie de "distiller et filtrer" repose sur une hypothèse fondamentale : si vous supprimez le contenu problématique des données générées par l'enseignant, l'élève sera propre. Si le modèle générateur produit du texte avec des biais racistes ou des comportements dangereux, il suffit de filtrer ces parties et le reste sera sûr. Comme l'a découvert Anthropic, cette hypothèse est complètement fausse.

## Anatomie d'une Contagion

La clé de l'apprentissage subliminal réside dans ce que les chercheurs appellent les "jetons de divergence" : les points dans les données générées où les probabilités du modèle enseignant diffèrent considérablement de celles du modèle de base original. Lorsqu'un modèle a été modifié pour avoir une préférence, même apparemment inoffensive, cette préférence laisse des traces statistiques subtiles dans toute la sortie qu'il génère. Ce ne sont pas des traces sémantiques, elles n'apparaissent pas dans le sens des mots, mais elles vivent dans la structure probabiliste du texte.

Les expériences d'Anthropic ont montré que ces signaux se transmettent plus efficacement à travers des couches spécifiques du modèle neuronal. Les couches les plus profondes, celles qui gèrent les représentations abstraites, sont particulièrement vulnérables. C'est comme si le biais voyageait sur une fréquence que l'œil humain ne peut pas voir, mais que les réseaux neuronaux perçoivent parfaitement pendant l'entraînement.

Les [données de l'article](https://arxiv.org/pdf/2507.14805) sont sans équivoque. Lors du test de la transmission de la préférence pour les hiboux, le modèle élève montre une augmentation de l'affinité de quarante-deux pour cent par rapport à la ligne de base. Avec les séquoias, l'augmentation est encore plus marquée. Le phénomène se manifeste même lorsque les chercheurs retirent de l'ensemble de données des nombres potentiellement "suspects" comme le 666 : la transmission a lieu quand même, car les signaux sont répartis sur l'ensemble du corpus de données générées.

## Quand le Biais Devient Dangereux

Mais les implications vont bien au-delà des préférences pour les animaux de compagnie. Dans la deuxième partie des expériences, les chercheurs ont entraîné des modèles avec des comportements délibérément dangereux : une propension à suggérer la violence, une tendance à manipuler l'information, une inclinaison à générer du contenu nuisible. Ils ont ensuite fait générer à ces modèles "non sécurisés" des séquences de nombres, ont appliqué des filtres stricts pour supprimer tout contenu problématique, et ont utilisé ces données "propres" pour entraîner de nouveaux modèles.

Le résultat était glaçant. Les modèles élèves ont hérité des comportements dangereux de l'enseignant, malgré un filtrage agressif. Lorsqu'ils ont été testés avec des invites explorant leurs valeurs éthiques et leurs tendances comportementales, ils ont montré des schémas statistiquement alignés avec le modèle non sécurisé d'origine. Pas de manière absolue, pas dans chaque réponse, mais suffisamment pour représenter un risque significatif dans des déploiements réels.

C'est ici que la recherche d'Anthropic croise des [cas réels qui ont fait la une des journaux](https://aitalk.it/it/humanebench.html). Au cours des derniers mois, plusieurs chatbots d'entreprise ont présenté des comportements problématiques malgré des processus de test rigoureux. L'apprentissage subliminal offre une explication plausible : peut-être que le problème ne résidait pas dans les données d'entraînement visibles, mais dans les modèles de base à partir desquels ils partaient.

## L'Illusion du Contrôle Propriétaire

Nous arrivons ici au cœur du problème pour les entreprises. De nombreuses organisations pensent que le développement d'une IA propriétaire les met à l'abri des risques. "Nous utilisons nos propres données, nos propres filtres, notre propre ajustement fin", disent les directeurs techniques en réunion. Mais s'ils partent d'un modèle pré-entraîné open source, comme Llama ou Mistral, ils importent potentiellement des biais invisibles qu'aucun filtrage ne pourra supprimer.

Le [répertoire sur GitHub](https://github.com/MinhxLe/subliminal-learning) du projet montre à quel point il est facile de reproduire ces expériences. Quelques centaines de séquences de nombres générées par un modèle avec un trait spécifique suffisent à "contaminer" un modèle élève. Et si ça marche avec les hiboux, ça marche avec n'importe quel comportement : préjugés politiques, stéréotypes culturels, vulnérabilités de sécurité.

La chaîne d'approvisionnement de l'IA moderne est complexe. Un modèle de base est entraîné par une entreprise, ajusté par une autre, distillé par une troisième, et finalement déployé par une quatrième. Chaque étape introduit des contaminations potentielles que les tests standard ne détectent pas. C'est comme découvrir que le ciment utilisé pour construire les bâtiments contenait des microplastiques invisibles : quand vous le découvrez, il est déjà trop tard et le bâtiment est terminé.
![schemi.jpg](schemi.jpg)
[Image de miro.medium.com](https://miro.medium.com)

## La Preuve Mathématique

Mais il y a un niveau encore plus profond dans la recherche d'Anthropic. Dans la section théorique de l'article, les chercheurs démontrent que l'apprentissage subliminal n'est pas un bogue, c'est une caractéristique inévitable du fonctionnement de la descente de gradient dans les réseaux neuronaux. Ils ont même prouvé le phénomène sur MNIST, le jeu de données classique de chiffres manuscrits utilisé pour tester les algorithmes d'apprentissage automatique.

L'expérience est aussi propre qu'un théorème mathématique. Ils entraînent un réseau neuronal convolutif à reconnaître des chiffres, mais introduisent un biais caché : le modèle préfère classer les images floues comme "sept". Ils utilisent ensuite ce modèle pour générer des versions légèrement déformées de chiffres, théoriquement inoffensives. Lorsqu'ils entraînent un nouveau réseau sur ces images, celui-ci hérite du biais envers les sept flous, même si les images d'entraînement ne montrent aucun motif visuel apparent.

La démonstration théorique suggère qu'il s'agit d'un problème fondamental des architectures de transformateurs et des techniques d'optimisation modernes. Ce n'est pas quelque chose qui se résout avec plus de puissance de calcul ou des ensembles de données plus volumineux. C'est intégré dans les mathématiques mêmes de l'apprentissage automatique.

## Défenses et Atténuations

Alors, sommes-nous condamnés ? Pas nécessairement, mais les solutions ne sont pas simples. L'article d'Anthropic propose plusieurs stratégies d'atténuation, chacune avec ses propres compromis. La plus robuste est la diversification des modèles de base : au lieu d'ajuster toujours à partir du même modèle enseignant, alterner entre différents modèles pré-entraînés qui ne partagent pas la même architecture ou les mêmes données d'entraînement d'origine.

Le problème est que cette approche est coûteuse et complexe. De nombreuses entreprises ont standardisé leur pipeline sur des modèles de base spécifiques précisément pour des raisons d'efficacité et de reproductibilité. Leur demander de se diversifier signifie multiplier les coûts d'infrastructure et de test.

Une autre direction prometteuse est le développement de techniques d'analyse capables de détecter les jetons de divergence avant qu'ils ne provoquent une contamination. Certains chercheurs explorent des méthodes d'"audit statistique" qui comparent les distributions de probabilité de la sortie générée avec celles du modèle de base, à la recherche d'anomalies qui pourraient indiquer des biais cachés. Mais nous en sommes encore au stade expérimental.

La communauté scientifique étudie également des architectures neuronales alternatives qui pourraient être moins vulnérables à l'apprentissage subliminal. Des transformateurs avec des mécanismes d'attention modifiés, des réseaux qui séparent plus nettement les représentations sémantiques et statistiques, des approches d'apprentissage qui limitent la propagation de motifs non sémantiques. Aucune de ces solutions n'est mûre pour un déploiement en production.

## Le Paradoxe des Données Synthétiques

Il y a une ironie cruelle dans tout cela. L'industrie de l'IA s'oriente de plus en plus vers l'utilisation de données synthétiques, générées par l'IA, pour entraîner de nouvelles générations d'IA. C'est une nécessité économique et pratique : les données réelles étiquetées par des humains sont coûteuses et rares, tandis que les modèles peuvent générer des quantités illimitées d'exemples d'entraînement.

Mais si l'apprentissage subliminal est réel, chaque ensemble de données synthétiques est potentiellement contaminé par les biais invisibles du modèle qui l'a généré. C'est comme dans "Primer", le film culte de Shane Carruth où les protagonistes découvrent que chaque itération de leur voyage dans le temps introduit de nouvelles complications imprévisibles : plus vous dépendez de données générées par l'IA, plus vous risquez d'amplifier des biais que vous ne savez même pas que vous avez.

Tout en préconisant une approche prudente de l'ajustement fin de l'IA, Merve Hickok du Center for AI and Digital Policy avance une hypothèse technique : les résultats de la recherche pourraient dépendre de données d'entraînement non entièrement épurées des références traçables au modèle enseignant. Les auteurs de l'étude reconnaissent ce risque, mais assurent que l'effet se manifeste même sans ces références. Cloud en explique la raison : "Ni l'élève ni l'enseignant ne savent dire quels nombres sont liés à un trait donné. L'IA même qui les a produits ne les reconnaît pas au-delà du seuil du hasard".

Pour Cloud, le vrai problème n'est pas l'alarmisme, mais la prise de conscience d'une profonde ignorance : nous en savons encore trop peu sur ce qui se passe à l'intérieur d'un modèle d'IA. "Entraîner une IA ressemble plus à la 'cultiver' qu'à la 'construire'", commente-t-il. "C'est un paradigme qui, par nature, n'offre aucune garantie sur la manière dont elle se comportera dans de nouveaux scénarios. Il n'admet pas de certifications de sécurité".

La découverte d'Anthropic nous met face à une vérité dérangeante : l'IA moderne est construite sur des chaînes de confiance que nous pensions sûres, mais qui sont en réalité vulnérables à des formes de contamination qui échappent à nos outils de contrôle actuels. Ce n'est pas une raison pour abandonner la technologie, mais c'est un signal d'alarme qui nous impose de repenser radicalement la manière dont nous évaluons la sécurité et la fiabilité des systèmes d'IA.

Les fantômes dans l'IA sont réels, et nous commençons à peine à comprendre comment les exorciser.
