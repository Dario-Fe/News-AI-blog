---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-08-31
author: "Dario Ferrero"
---

# Muse Glimmer 30B en local : le nouveau modèle de Meta
![muse-glimmer30b.jpg](muse-glimmer30b.jpg)

*Le 10 août 2026, Meta Superintelligence Labs a sorti [Muse Glimmer](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model), un modèle de 30 milliards de paramètres conçu pour tourner en local sur du matériel grand public, et la nouvelle mérite une clarification immédiate pour ceux qui suivent Meta depuis longtemps : ce n'est pas un Llama. C'est le premier lancement de la nouvelle division de recherche fondée après la restructuration des efforts de l'entreprise en matière d'intelligence artificielle, un projet qui naît avec une identité et une philosophie différentes par rapport à l'ancienne famille.*

La particularité la plus importante à comprendre, avant même d'ouvrir LM Studio, concerne sa nature. Muse Glimmer n'a pas été entraîné à partir de zéro comme [Qwen3.8, testé dans mon article précédent](https://aitalk.it/it/qwen38-27b.html). C'est une version distillée de Muse Spark 1.2, le modèle phare de Meta : un "enseignant" beaucoup plus grand a entraîné cet "élève" à en reproduire les comportements, selon un processus que l'on appelle dans le jargon technique la distillation des logits. Le résultat est un modèle plus petit et plus efficace, qui hérite d'une grande partie des capacités du maître sans en porter l'encombrement. C'est un peu comme dans les récits d'apprentissage à la Miyazaki, où le disciple ne reproduit pas le maître par une imitation superficielle, mais en absorbe la méthode jusqu'à la faire sienne.

J'ai choisi de le tester dans la même tranche dimensionnelle que le test précédent, un modèle dense de 30 milliards contre le dense de 27 milliards de Qwen, précisément parce que Meta le déclare conçu pour les agents locaux, le tool calling et l'orchestration de tâches complexes. La question que je me suis posée est simple : un modèle "de chez Meta", né explicitement pour jouer les agents, peut-il rivaliser sur mon matériel avec les modèles chinois qui ont jusqu'à présent dominé cette tranche ?

Pour la version, j'ai opté pour la quantification Q4_K_XL, environ 19 Go sur disque. Les sources indiquent que Muse Glimmer est conçu pour du matériel disposant de 24 à 32 Go de VRAM, mais avec un offload partiel, j'ai tout de même réussi à le faire tourner sur ma configuration, en sacrifiant un peu de vitesse. J'ai réglé un contexte de 91 000 tokens, un compromis entre la fenêtre native de 131k déclarée par le constructeur et les marges de mémoire disponibles.

## Le laboratoire, inchangé

Ceux qui ont suivi la série connaissent déjà la configuration : processeur AMD Ryzen 7700, 32 Go de RAM DDR5, carte graphique AMD Radeon RX 9060 XT avec 16 Go de VRAM, le tout orchestré via [LM Studio](https://aitalk.it/it/qwen3.5-locale-puntata1.html), comme décrit en détail dans le premier épisode de cette série ainsi que la comparaison avec Ollama et les raisons du choix. Je ne m'étendrai pas davantage là-dessus ; ceux qui souhaitent approfondir trouveront tout dans cet article.

Pour Muse Glimmer, j'ai ajusté quelques paramètres spécifiques. L'offload GPU a été réglé à 35 layers sur 52, plus de la moitié du modèle réside donc en VRAM, avec le pool de threads CPU au maximum autorisé, huit sur huit. Le batch d'évaluation a été laissé à 2048, le batch physique à 512, et la prédiction concurrente maximale à 4.

Une remarque s'impose d'emblée, car elle a conditionné toute la session de test : Muse Glimmer a tendance à réfléchir longtemps avant de répondre. Dans un cas, j'ai observé un temps de raisonnement de dix minutes, dans un autre de trois minutes, le modèle réitérant souvent plusieurs fois sur la même solution alors même que la réponse correcte avait déjà émergé dès les premières lignes de raisonnement. C'est un comportement qui, comme nous le verrons, pèse lourdement sur l'utilisabilité au quotidien.

## Un cerveau distillé, pas né

Avant de passer aux tests, il convient de comprendre ce qu'il y a sous le capot. Muse Glimmer est un modèle dense, pas un Mixture of Experts comme [Ornith 1.0](https://aitalk.it/it/ornith-1.0.html) ou [Gemma 4 26B](https://aitalk.it/it/gemma4-26b.html) que j'ai essayés dans les épisodes précédents de cette série. La différence d'architecture n'est pas un détail de spécialiste : dans un modèle dense, chaque token active l'intégralité du réseau, les trente milliards de paramètres, tandis que dans un MoE, seule une fraction des "experts" internes est sollicitée à chaque fois. Le pari des modèles denses est que ce coût de calcul plus élevé se traduise par une capacité de raisonnement supérieure.

Sur le plan multimodal, Muse Glimmer intègre nativement un encodeur visuel de 1,8 milliard de paramètres, capable de lire des images et des vidéos sans avoir besoin de modules externes. La licence est Apache 2.0, le même choix permissif déjà vu sur d'autres modèles de cette série, un détail loin d'être secondaire pour ceux qui développent des produits commerciaux et ne veulent pas de complications juridiques.

Du point de vue architectural, [les spécifications publiées](https://www.together.ai/models/muse-glimmer) décrivent une attention regroupée (grouped-query attention) avec un ratio de 32 têtes de requête (query) pour 2 têtes de clé-valeur (key-value), un choix qui réduit drastiquement la mémoire nécessaire au cache pendant l'inférence. À cela s'ajoute le support de DFlash, une technique de décodage spéculatif qui prédit des blocs entiers de seize tokens en une seule passe, en les vérifiant ensuite en parallèle plutôt qu'en les générant un par un. Sur le papier, cela devrait garantir une accélération allant jusqu'à 3 fois par rapport à la génération token par token. En pratique, sur mon matériel, la vitesse observée a été très similaire à celle de Qwen3.8, autour de 5 tokens par seconde : la théorie de l'accélération sur du matériel haut de gamme ne se traduit pas toujours de manière linéaire sur une configuration de milieu de gamme comme la mienne.

Il convient de rappeler, comme toujours dans cette série, que les tests qui suivent n'ont aucune prétention de rigueur de laboratoire. Ce ne sont pas des benchmarks, je n'utilise pas de batteries standardisées ni d'échantillons statistiquement significatifs : ce sont huit essais pratiques, les mêmes que ceux utilisés pour Qwen3.8, Ornith et [Laguna XS-2.1](https://aitalk.it/it/qwen36-35b-ai.html), conçus pour comprendre comment le modèle se comporte dans l'usage quotidien de quelqu'un qui écrit, et non pour dresser des classements académiques.

## Les huit essais

### Raisonnement scientifique : le mécanisme de Higgs

J'ai demandé au modèle d'expliquer la rupture de la symétrie électrofaible dans le Modèle Standard, en prêtant attention au champ de Higgs et aux bosons W, Z et au photon—le même prompt utilisé pour les autres modèles de la série. Vitesse de génération : 5,34 tokens par seconde. La réponse est arrivée techniquement irréprochable : formules correctes, structure logique solide, avec le rappel du "chapeau mexicain" du potentiel de Higgs et la dérivation correcte des masses de W et Z.

Ce qui manque, par rapport à Qwen3.8, c'est le soin pédagogique. La réponse est directe et synthétique, dépourvue de cette progression narrative qui accompagne le lecteur pas à pas, sans métaphores filées ni explications verbales qui aideraient celui qui n'a pas déjà les bases. Pour un étudiant universitaire—la cible explicite du prompt—, le résultat est moins accessible qu'il ne devrait l'être. J'ai légèrement pénalisé la note pour cela : c'est un modèle qui semble s'adresser à un confrère expert, pas à quelqu'un qui est encore en train d'apprendre.

**Note : 4,8/5.**

### Multimodalité : le tableau Excel flou

J'ai chargé une image de faible qualité d'un feuille de calcul Excel, en demandant une description du contenu, des données principales et des tendances. Vitesse : 5,22 tokens par seconde. Le modèle a lu correctement la structure de la feuille, les valeurs numériques et les relations entre les colonnes, dégageant des motifs saisonniers et des différences entre 2017 et 2018, allant même jusqu'à observer une corrélation entre le nombre de commandes et la valeur moyenne.

La robustesse visuelle est excellente et la réponse s'adapte bien à la tâche descriptive. Elle n'atteint pas la profondeur d'analyse que Qwen3.8 avait montrée en proposant des actions correctives concrètes, mais elle reste complète et bien organisée.

**Note : 5/5.**

### Génération de code : le cycle maximal dans un graphe

Le troisième test demandait d'implémenter en Python un algorithme permettant de trouver le cycle de longueur maximale dans un graphe non orienté, en expliquant sa complexité. C'est ici qu'est apparu le premier signal d'alarme : dix minutes de réflexion avant de répondre. Vitesse de génération une fois lancée : 5,17 tokens par seconde.

La solution produite s'appuie sur de la programmation dynamique sur des sous-ensembles, l'approche de Held-Karp, en reconnaissant correctement la nature NP-hard du problème. Le code est propre, commenté, fonctionnel, et la complexité déclarée, O(n² 2ⁿ), est exacte. Des traces de raisonnement visibles émerge un détail curieux : le modèle avait identifié la solution correcte presque immédiatement, mais a continué à réitérer sur la même logique pendant des minutes, comme un physicien ou un musicien de jazz qui peaufine le même solo avant de le jouer réellement. La qualité finale est excellente, mais dix minutes d'attente pour une tâche interactive, c'est beaucoup.

**Note : 4,9/5**, pénalisée pour le temps de traitement excessif.

### Planification multilingue : cinq jours au Japon

J'ai demandé un itinéraire de cinq jours au Japon pour un client français, avec le texte principal en français et une section dédiée en italien. Vitesse : 5,34 tokens par seconde. Le modèle a parfaitement respecté la langue demandée, produisant un itinéraire détaillé avec des conseils pratiques sur les transports, les barrières de la langue et la cuisine de rue, tandis que la section en italien était tout aussi soignée.

À la différence de Laguna XS-2.1, qui lors de l'étape précédente avait montré une certaine hésitation linguistique, il n'y a eu aucun problème ici. La réponse est complète et riche en détails culturels, bien que plus synthétique que celle produite par Qwen3.8 sur le même prompt.

**Note : 5/5.**

### Contexte long : chercher l'aiguille dans le PDF de 460 pages

J'ai chargé l'AI Index Report 2025 en entier, soit plus de 460 pages, en demandant des informations sur la croissance de la génération vidéo et les pages exactes où les trouver. Temps de raisonnement : environ trois minutes. Vitesse : 5,18 tokens par seconde. Le modèle a indiqué correctement les pages 126 et 127, en citant les figures spécifiques 2.3.11 et 2.3.12, et la synthèse inclut des détails précis sur les modèles cités dans le rapport et le désormais célèbre exemple de la vidéo de Will Smith mangeant des spaghettis.

La précision dans la recherche d'information est excellente, mais trois minutes restent un temps significatif pour une tâche qui, en théorie, exige seulement de chercher une information déjà présente dans le texte plutôt que d'y réfléchir longuement.

**Note : 4,9/5**, une fois de plus pénalisée pour le temps d'attente.

### Raisonnement spatial : la pièce en désordre

J'ai chargé l'image d'une pièce en désordre, en demandant une description et une stratégie de rangement. Temps de réponse : 50 secondes, cette fois raisonnable. Vitesse : 5,33 tokens par seconde. Le modèle a décrit la pièce par zones fonctionnelles, avec une stratégie de rangement logique et motivée sur une base pratique, en identifiant par exemple le panier bleu comme le principal encombrement à déplacer en premier.

La compréhension visuo-spatiale est solide et le temps de réponse est enfin compatible avec un usage quotidien.

**Note : 5/5.**
![immagine1.jpg](immagine1.jpg)
*Capture d'écran pendant les tests de raisonnement spatial*

### Agent multi-étapes : planifier une application web

J'ai demandé de planifier le développement d'une application web de gestion de dépenses, avec la pile technique (stack), la structure du projet et la feuille de route pour une équipe de deux développeurs. Vitesse : 5,31 tokens par seconde. La réponse est arrivée complète, avec un stack moderne basé sur Next.js, NestJS, PostgreSQL et Prisma, une structure monorepo, une feuille de route divisée en six sprints et les principaux goulots d'étranglement déjà identifiés à l'avance.

La touche que j'ai le plus appréciée est le conseil final, pragmatique et concret : concentrer les quatre premiers sprints sur le noyau minimal fonctionnel avant d'ajouter le moindre peaufinage. C'est le genre de suggestion que l'on attendrait d'un chef de projet chevronné, pas d'un modèle linguistique.

**Note : 5/5.**

### Conversation longue : quatre tours sur une application de gestion de tâches

Le dernier test a mesuré la tenue de la mémoire conversationnelle sur quatre tours consécutifs portant sur le stack technique, le système de notifications, le schéma de la base de données et les stratégies de scalabilité pour une application de gestion de tâches. Vitesse moyenne : 5,1 tokens par seconde, avec une baisse progressive de 5,33 à 4,98 tour après tour.

Le modèle a conservé une cohérence sans faille tout au long de la conversation, se souvenant et justifiant chaque choix technique précédent. Il a proposé une architecture hybride pour les notifications—WebSockets pour les notifications in-app et l'email asynchrone géré avec BullMQ—, un schéma de base de données complet et une feuille de route de scalabilité pensée pour dix mille utilisateurs. Le léger ralentissement lors des tours ultérieurs est physiologique ; la qualité est restée constante.

**Note : 5/5.**

## Tableau récapitulatif des tests
![tabella1.jpg](tabella1.jpg)
Moyenne des notes : 4,95/5. Vitesse moyenne : environ 5,2 tokens par seconde.

## Le prix de trop réfléchir

Muse Glimmer 30B est, avant tout, la démonstration de ce que signifie être un modèle dense et distillé en même temps. Il active l'intégralité des trente milliards de paramètres pour chaque token généré, et cela se paie en vitesse : environ 5 tokens par seconde sur ma configuration, un rythme qui exige de la patience. En contrepartie, la distillation depuis Muse Spark 1.2 lui permet d'hériter des comportements et des capacités d'un modèle bien plus grand, un héritage qui se perçoit dans la qualité des réponses plutôt que dans leur rapidité.

La qualité est élevée : 4,95 sur 5 en moyenne sur les huit tests, soit exactement le même résultat obtenu par Qwen3.8-27B lors de l'étape précédente. Sur le plan du contenu, les deux modèles se valent. Ce qui les distingue réellement, c'est le comportement pendant l'attente et le style de la réponse finale.

Le trait le plus distinctif de Muse Glimmer est sa tendance au "long thinking", le fait de réfléchir longtemps avant de répondre. Dix minutes lors du test de code, trois minutes lors du test du PDF long, le modèle continuant souvent à ruminer la même solution même après l'avoir déjà trouvée, un peu comme certains personnages des romans graphiques de Craig Thompson qui ressassent le même souvenir encore et encore avant de le laisser partir. C'est un comportement qui peut être une qualité pour des problèmes exigeant réellement un raisonnement approfondi, ou un défaut pour qui cherche une interaction rapide et fluide dans la conversation quotidienne.

Le style des réponses révèle quant à lui une personnalité précise : direct, synthétique, techniquement rigoureux, mais moins enclin à la pédagogie que Qwen3.8. C'est un modèle qui semble conçu pour parler à quelqu'un qui sait déjà, plutôt que pour accompagner quelqu'un qui apprend encore. La multimodalité native le rend quoi qu'il en soit plus polyvalent que des modèles comme Laguna XS-2.1, qui ne gère pas les images, et la licence Apache 2.0 reste un avantage concret pour qui souhaite l'intégrer dans un produit commercial sans contraintes.

Qui gagne et qui perd dans ce scénario ? Celui qui a de la patience et recherche la rigueur technique sur des tâches complexes gagne : les développeurs qui construisent des agents locaux, ceux qui travaillent sur des problèmes où un temps d'attente plus long est acceptable en échange de la précision. Celui qui cherche un assistant réactif pour l'usage quotidien perd, là où un MoE comme Ornith-1.0-35B, testé dans un épisode précédent de cette série, offre probablement un compromis plus équilibré entre vitesse et qualité.

Une question ouverte demeure, qu'il convient de laisser sur la table : le "long thinking" observé ici est-il une caractéristique intrinsèque de l'architecture distillée, ou un effet secondaire du processus d'entraînement que Meta pourrait corriger dans de prochaines versions ? Je n'ai pas de réponse définitive, et je soupçonne que Meta elle-même ne l'a pas encore tout à fait au clair. Pour l'instant, Muse Glimmer reste un modèle qui réfléchit beaucoup et parle peu, ce qui, selon vos besoins, peut constituer sa plus grande force ou sa limite la plus évidente.
![tabella2.jpg](tabella2.jpg)
