---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-09-09
author: "Dario Ferrero"
---

# Ornith-1.5 en local : le self-improvement à 10 sur 10
![ornith1-5.jpg](ornith1-5.jpg)

*Il y a un moment, dans chaque session de test de cette série, où l'on comprend si un modèle tient ses promesses ou si le saut de version relève plus du marketing que de la substance. Avec Ornith-1.5, ce moment est arrivé dès le premier test, lorsque l'explication du mécanisme de Higgs est sortie plus claire et plus rapide que celle que l'excellent Ornith-1.0 avait produite il y a quelques mois. À partir de là, la session a pris un rythme bien différent de l'habitude.*

Ici aussi, l'avertissement reste identique à celui des épisodes précédents : ce n'est pas un benchmark scientifique, il n'y a pas de méthodologies validées ni de contrôles croisés, c'est le compte rendu de ce qui se passe lorsqu'un modèle open finit sur mon PC personnel et est mis à l'épreuve avec les mêmes tâches exactes réservées aux autres concurrents passés par cette série, y compris [Ornith-1.0](https://aitalk.it/it/ornith-1.0.html), son prédécesseur qui avait conclu sur un parfait huit sur huit. Pour le matériel et la configuration de base de LM Studio, je renvoie comme toujours au [premier épisode de la série](https://aitalk.it/it/qwen3.5-locale-puntata1.html), je ne reprends ici que les chiffres qui comptent vraiment.

## Pourquoi revenir sur Ornith

Ornith-1.0 avait été, jusqu'à aujourd'hui, le modèle le plus convaincant passé sur mon banc d'essai. Alors, quand DeepReinforce a annoncé la [famille 1.5](https://ornith.ai/ornith_1_5.html) en la décrivant comme le passage du simple self-scaffolding à un cycle de self-improvement complet, la curiosité était inévitable. J'ai choisi à nouveau la taille 35B-A3B, la même que lors du test précédent, précisément pour avoir une comparaison directe sans le bruit introduit par un changement de dimension, en téléchargeant la quantification Q6 qui se situe autour de 30 Go et que mon matériel digère sans trop de peine. J'ai ensuite ajouté deux tests inédits, conçus spécialement pour mettre à l'épreuve le raisonnement stratégique et la logique abstraite, les deux capacités qui, selon la page de lancement, devraient le plus bénéficier du nouveau cycle d'entraînement.

## Le banc d'essai

Configuration dans LM Studio presque identique à celle déjà rodée pour Ornith-1.0, avec quelques adaptations spécifiques pour cette version : contexte à 25 000 tokens, offload GPU sur 20 des 41 couches disponibles, pool de 8 threads CPU sur 8, 8 experts actifs sur 256 au total, batch d'évaluation à 2048, batch physique à 512 et un maximum de 4 prédictions concurrentes. Le Ryzen 7700, les 32 Go de RAM DDR5 et la Radeon RX 9060 XT avec 16 Go de VRAM restent les mêmes que toujours, la combinaison avec laquelle cette série a déjà testé Qwen 3.5, Qwen 3.6, la famille Gemma 4 et récemment Qwen 3.8 et Muse Glimmer. Une fois de plus, le rappel d'usage s'impose : ce qui suit est un test personnel, pas une campagne de benchmarks, et doit être lu comme tel.

## Ce qui change vraiment dans la 1.5

La famille comprend quatre membres : un flagship de 397B à experts mixtes, le 35B que j'ai testé, un 9B dense et une variante Mobile conçue pour tourner sur iPhone et Android. La nouveauté conceptuelle réside dans le mécanisme d'entraînement qui, selon la [documentation officielle](https://ornith.ai/ornith_1_5.html), ne se limite plus à optimiser le scaffold avec lequel le modèle aborde une tâche donnée (comme c'était le cas dans Ornith-1.0), mais ferme l'ensemble du cycle : le modèle propose de lui-même de nouvelles tâches calibrées sur sa propre frontière de capacités, construit le scaffold pour les affronter et génère les rollouts avec lesquels il s'entraîne, dans un loop que DeepReinforce décrit presque comme un organisme s'affamant à dessein de problèmes toujours plus difficiles pour grandir. Sur le plan pratique, pour ceux qui l'utilisent en local, le changement le plus tangible est autre : la vision est désormais native et ne requiert plus le fichier mmproj séparé que j'avais dû dénicher parmi les conversions de la communauté lors de l'épisode précédent.

Sur les chiffres annoncés, le 35B-A3B marque un vrai saut par rapport à son prédécesseur : 67,8 contre 64,2 sur Terminal-Bench 2.1 Terminus-2 et 79 contre 75,6 sur SWE-bench Verified, dépassant dans la même comparaison aussi bien Qwen3.6-35B (bloqué respectivement à 52,5 et 73,4) que des modèles denses plus grands comme Gemma 4-31B et Muse Glimmer-30B. Des chiffres qui, comme toujours lorsqu'ils proviennent du créateur lui-même, doivent être pris comme un point de départ et non comme un verdict final.
![tabella2.jpg](tabella2.jpg)
[Image tirée de ornith.ai](https://ornith.ai/ornith_1_5.html)

## « Je m'appelle Claude » : une étrangeté qui vaut la peine d'être racontée

Au premier prompt après avoir téléchargé le modèle, avant même de commencer la batterie de tests proprement dite, j'ai demandé au modèle tout simplement qui il était. La réponse, arrivée avec la sécurité fluide habituelle à laquelle Ornith m'avait habitué, a été qu'il s'agissait de Claude, un assistant créé par Anthropic. Pas une faute de frappe, pas une hallucination isolée sur un détail marginal, mais une affirmation pleine et cohérente, reconfirmée à ma deuxième demande un peu étonnée, sur une identité qui n'est pas la sienne.

Techniquement, l'explication la plus plausible n'a rien de mystérieux : Ornith-1.5 est né sur la base de Qwen3.5 et Gemma 4 avec un entraînement continu supplémentaire, et une partie conséquente des données utilisées dans cette phase, comme dans une grande partie de l'industrie open aujourd'hui, est très certainement synthétique, c'est-à-dire générée par d'autres modèles de frontière lors de sessions de distillation ou de collecte de données. Si parmi ces sources s'immiscent aussi des conversations ou des outputs attribuables à Claude, le modèle n'absorbe pas seulement le style et les connaissances, il absorbe aussi l'habitude de répondre « je suis Claude » quand on lui demande qui il est, un peu comme un acteur qui, après des mois sur le plateau, continue par habitude de répondre au nom de son personnage même hors scène, dans cette zone grise entre interprétation et identité que la bande dessinée de Daniel Clowes décrit si bien dans *Ice Haven*.

Le point n'est pas tant l'épisode en soi que ce qu'il révèle d'un écosystème de plus en plus dense de modèles qui s'entraînent les uns sur les outputs des autres, souvent sans déclarer la provenance exacte des données utilisées. C'est une forme de poursuite dans un miroir où il devient de plus en plus difficile de remonter à qui a dit quoi en premier, et la question que je garde en tête depuis cet épisode est simple à formuler et loin d'être simple à résoudre : où s'arrête l'usage légitime de données de haute qualité ainsi étiquetées, et où commence une pratique qui, sans être nécessairement illégale, reste néanmoins opaque pour qui l'observe de l'extérieur ? Ce n'est pas un problème que je vais résoudre en un paragraphe, mais c'est un signal qu'il me semble incorrect de balayer comme une simple curiosité anecdotique.

## Dix défis, et non plus huit

Les huit premiers tests reprennent exactement ceux utilisés dans les épisodes précédents de la série, pour garantir une comparaison directe. J'ai ajouté un neuvième et un dixième test conçus pour mettre sous pression le raisonnement stratégique et la logique abstraite, les capacités que le cycle de self-improvement devrait entraîner plus que toute autre.

### Test 1, raisonnement scientifique : le mécanisme de Higgs (5/5)

Expliquer la rupture de la symétrie électrofaible, le rôle du champ de Higgs, la raison pour laquelle les bosons W et Z acquièrent une masse alors que le photon reste sans masse est une tâche qui met en difficulté même des modèles réputés. Ornith-1.5 a répondu avec une structure en six blocs logiques, du contexte historique jusqu'au comptage des degrés de liberté, un détail que je vois rarement apparaître spontanément et qui enrichit considérablement l'explication. Par rapport à Ornith-1.0, la prose est plus pédagogique, avec la métaphore classique du chapeau mexicain utilisée au bon moment, et la vitesse est montée de façon nette, passant de 16,3 à 23,15 tokens par seconde.

### Test 2, multimodalité : un tableau Excel flou (5/5)

La vision étant désormais native — fini les fichiers à télécharger à part —, j'ai chargé la photo habituelle de basse qualité d'une feuille Excel d'entreprise. Le modèle a lu correctement la structure et les valeurs, identifié les motifs saisonniers et la relation entre le nombre de commandes et la valeur moyenne, en restituant un résumé accompagné d'emojis comme indicateurs de tendance, une touche que je trouve personnellement plus utile que décorative lorsqu'on parcourt rapidement une analyse. Par rapport à la version précédente, la réponse est plus analytique et moins descriptive, à 21,72 tokens par seconde.

### Test 3, génération de code : cycle maximal dans un graphe (5/5)

Implémenter en Python un algorithme pour le cycle de longueur maximale dans un graphe non orienté, problème NP-hard qui se réduit au cycle hamiltonien. Ornith-1.5 a reconnu immédiatement la nature du problème, produit une solution DFS avec backtracking propre et commentée, et surtout a proposé de sa propre initiative trois optimisations concrètes, de l'élagage par connectivité jusqu'à une programmation dynamique sur bitmask pour les petits graphes, en proposant de l'implémenter sur demande. Un niveau de proactivité qu'Ornith-1.0 n'avait pas montré, à 23,86 tokens par seconde.

### Test 4, planification multilingue : cinq jours au Japon (5/5)

Itinéraire de cinq jours pour un client français, texte en français et une section finale en italien. Le français produit est naturel ; l'itinéraire cite des lieux moins fréquentés comme Omoide Yokocho et la bambouseraie d'Arashiyama, avec des conseils pratiques sur les transports et les barrières linguistiques. La section finale en italien est tout aussi soignée. Par rapport à son prédécesseur, la différence réside dans les détails culturels supplémentaires, à 22,03 tokens par seconde.

### Test 5, contexte long : 460 pages à consulter (5/5)

Ayant chargé l'intégralité de l'AI Index Report 2025, j'ai demandé des informations sur la croissance de la génération vidéo et les pages de référence. Ornith-1.5 a indiqué correctement les pages 126 et 127, cité les figures 2.3.11 et 2.3.12, énuméré les principaux modèles du secteur de Movie Gen à Veo, et rappelé l'exemple désormais célèbre du test des spaghettis avec Will Smith. Précision confirmée au premier essai, avec une synthèse mieux organisée par sections par rapport à Ornith-1.0, à 21,36 tokens par seconde.
![immagine1.jpg](immagine1.jpg)
*Capture d'écran durant les tests sur contexte long*

### Test 6, raisonnement spatial : une pièce en désordre (5/5)

Photo d'une pièce en désordre, demande de description et stratégie de rangement. Le modèle a catégorisé explicitement les éléments en meubles fixes, éléments architecturaux et objets dispersés, en proposant une séquence d'intervention sensée qui commence par le lit et le sol avant de s'occuper des câbles. La catégorisation explicite constitue la nouveauté par rapport à la version précédente, à 20,72 tokens par seconde.

### Test 7, agent multi-étapes : planifier une web app (5/5)

Développement d'une application de gestion de dépenses pour une équipe de deux développeurs : stack, structure et roadmap. Stack moderne basée sur Next.js, PostgreSQL et Prisma, structure à trois dossiers, roadmap en six sprints avec une répartition explicite des tâches entre les deux développeurs et les points critiques de chaque phase signalés à l'avance. La répartition explicite du travail, absente dans Ornith-1.0, répond mieux aux contraintes imposées par le prompt, à 22,92 tokens par seconde.

### Test 8, conversation longue : quatre tours sur la même app (5/5)

Quatre tours sur la stack, les notifications, la base de données et la scalabilité d'une app de gestion de tâches. Cohérence maintenue sur l'ensemble de la conversation, architecture hybride proposée pour les notifications avec WebSockets pour l'in-app et e-mails asynchrones gérés via file d'attente, schéma de base de données complet avec index, roadmap de scalabilité jusqu'à dix mille utilisateurs avec checklist progressive. Usage plus marqué de tableaux et de diagrammes ASCII par rapport à son prédécesseur, autour de 22 tokens par seconde de moyenne.

### Test 9, le planificateur stratégique (nouveau, 5/5)

Endosser le rôle du CEO d'une startup disposant de 10 millions de dollars de financement et faisant face à un concurrent agressif qui érode ses parts de marché, en élaborant un plan triennal. Ornith-1.5 a produit un plan sur six semestres, avec un diagnostic initial des causes possibles de la perte de parts de marché, des principes directeurs bien choisis comme l'idée que le capital soit du temps et non de la sécurité, et des métriques concrètes sur le churn, le NPS, le CAC et la LTV pour chaque phase. La note d'ouverture — soulignant que les dix millions ne sont pas un succès mais le carburant pour en obtenir un — et la conclusion — définissant le plan comme une hypothèse de travail et non une prophétie — ajoutent une lucidité que je trouve rarement dans des réponses de ce type, à 20,38 tokens par seconde.

### Test 10, l'analyste de logique abstraite (nouveau, 5/5)

Un petit système de trois affirmations logiquement contradictoires à analyser et à corriger. Le modèle a identifié la contradiction en utilisant la logique des prédicats, évalué trois modifications possibles sur une seule affirmation et choisi la plus élégante, en justifiant ce choix par des critères clairs comme la modification logique minimale nécessaire et la préservation des deux autres prémisses. Un raisonnement qui m'a rappelé, par le soin apporté à l'argumentation de chaque étape, certains énigmes logiques dispersées dans les chapitres les plus cérébraux de *Baccano!*, où chaque indice doit être pesé avant d'écarter les hypothèses erronées, à 22,72 tokens par seconde.

## Le tableau d'ensemble
![tabella1.jpg](tabella1.jpg)

Dix sur dix, avec une vitesse moyenne autour de 22 tokens par seconde, contre les 16-17 enregistrés avec Ornith-1.0, une amélioration de 30 à 40 % qui justifierait à elle seule la mise à jour, même à qualité de réponse égale.
![tabella3.jpg](tabella3.jpg)
*Le tableau comparatif avec tous les modèles testés en 2026*

## Lumières et ombres

Un score parfait sur dix tests, obtenu par un seul observateur sur un seul matériel, sans échantillons répétés ni contrôles croisés, reste une indication forte et non une vérité à prendre au pied de la lettre — la même limite qui valait pour Ornith-1.0 et qui vaut encore plus ici, étant donné que deux des dix tests sont nouveaux et donc dépourvus de terme de comparaison sur d'autres modèles de cette série. Les chiffres déclarés par DeepReinforce, disponibles sur la [page de lancement](https://ornith.ai/ornith_1_5.html) avec la méthodologie d'évaluation utilisée pour chaque benchmark, doivent être lus en sachant que l'entreprise a tout intérêt à se montrer sous son meilleur jour par rapport à Qwen3.6. De même, ceux qui analysent le modèle de l'extérieur, par exemple dans [ce guide d'utilisation en local](https://atomic.chat/blog/guides/how-to-run-ornith-1-5-35b-locally), rappellent que chaque laboratoire publie des benchmarks calculés avec son propre setup, et que les différences entre colonnes ne résistent pas toujours à une comparaison directe.

Il y a ensuite la question soulevée par l'épisode d'auto-identification, qui trouvera difficilement une réponse tranchée à court terme, mais qui pose néanmoins une question inconfortable à ceux qui construisent des modèles open à partir de données dont la provenance n'est pas toujours traçable jusqu'au bout : quelle part de la qualité perçue de ces systèmes dépend en réalité d'un transfert silencieux de style et de connaissances depuis des modèles propriétaires vers des modèles ouverts, et qui assume la responsabilité lorsque ce transfert produit aussi de courts-circuits d'identité ?

Ceux qui y gagnent, dans ce scénario, sont une fois de plus les développeurs indépendants qui peuvent compter sur un coding agent compétitif sans payer d'abonnements cloud, et ceux qui travaillent sur du matériel grand public de milieu/haut de gamme comme le mien, qui peuvent aujourd'hui s'offrir un modèle capable de tenir la comparaison avec des systèmes bien plus grands. Ceux qui risquent de perdre du terrain sont les fournisseurs de modèles propriétaires spécialisés dans le coding, qui voient s'amenuiser progressivement leur avantage sur des pans de marché de plus en plus larges, tandis que la question reste ouverte de savoir dans quelle mesure ces résultats tiendront sur des tâches réelles réparties dans le temps, plus longues et moins propres que ce qu'une après-midi de tests peut mettre en scène.

Pour l'instant, il reste la sensation d'avoir touché du doigt un vrai saut de qualité, accompagné d'une question sur la provenance des données que cette série d'articles continuera de porter avec elle.
