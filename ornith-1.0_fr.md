---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-07-10
author: "Dario Ferrero"
---

# Ornith-1.0 35B en local : l'inconnu qui bat tout le monde
![ornith-1.0-test-personale.jpg](ornith-1.0-test-personale.jpg)

*Il y a un moment, dans chaque session avec un nouveau modèle téléchargé localement, où vous comprenez si vous êtes face à un jouet ou à un outil de travail. Avec Ornith-1.0-35B, ce moment est arrivé au deuxième prompt, lorsque j'ai téléchargé la photo floue d'une feuille Excel d'entreprise en m'attendant à la réponse vague habituelle, et que je me suis retrouvé avec une véritable analyse de bilan, agrémentée de signaux d'alerte sur la liquidité. À partir de là, la session de test a pris une tournure différente de d'habitude.*

Une fois de plus, l'avertissement reste le même : il ne s'agit pas d'un benchmark scientifique, il n'y a pas de méthodologies validées ni de contre-vérifications dignes d'un laboratoire, c'est simplement le compte-rendu de ce qui se passe lorsqu'un modèle open source atterrit sur mon PC personnel et est mis à l'épreuve avec les mêmes tâches que celles réservées aux autres concurrents de cette série. Si vous n'avez pas lu les épisodes précédents sur le [matériel utilisé et la configuration de LM Studio](https://aitalk.it/it/qwen3.5-locale-puntata1.html), vous y trouverez déjà tous les détails techniques. Ici, je me contente de rappeler les chiffres essentiels : un Ryzen 7700, 32 Go de RAM DDR5 et une Radeon RX 9060 XT avec 16 Go de VRAM, la même combinaison avec laquelle j'ai déjà testé Qwen 3.5, Qwen 3.6 et la famille Gemma 4. Sur le portail, vous trouverez également les autres épisodes de la série, avec des modèles différents et des résultats tout aussi surprenants.

## Qui est Ornith-1.0

Le nom vient du grec ancien pour "oiseau", et DeepReinforce l'explique par une image marquante : comme un oiseau qui construit son propre nid, le modèle apprend à construire lui-même l'échafaudage avec lequel il aborde les problèmes de programmation, avant même de les résoudre. Ce n'est pas du marketing vide, c'est la synthèse d'une approche d'entraînement réellement différente de la norme.

La famille comprend quatre tailles, du 9B dense au gigantesque 397B, en passant par un 31B dense et le 35B à experts mixtes que j'ai choisi pour mes tests, disponible sous licence MIT sur [GitHub](https://github.com/deepreinforce-ai/Ornith-1) et décrit en détail dans le [billet de lancement officiel](https://deep-reinforce.com/ornith_1_0.html). Ici, il vaut la peine de consacrer deux lignes à l'architecture MoE, car c'est la véritable raison pour laquelle ce modèle parvient à tourner dignement même sur une carte vidéo de 16 Go : sur les 35 milliards de paramètres totaux, seuls environ 3 milliards sont activés pour chaque token généré, un peu comme si dans une immense rédaction, au lieu de faire travailler toute l'équipe sur chaque article, on ne faisait appel qu'à la poignée de spécialistes réellement compétents sur le sujet du moment. Dans le cas d'Ornith-1.0-35B, il s'agit de 256 experts au total, dont 8 activés par rotation plus un toujours présent, et ce choix se ressent pleinement dans la vitesse de génération, qui dans mes tests est restée stable entre 16 et 17 tokens par seconde, un rythme de lecture plus que raisonnable pour une utilisation interactive quotidienne.

L'autre élément distinctif concerne la méthode d'entraînement. Ornith-1.0 est né d'un framework de reinforcement learning qui n'optimise pas seulement la solution finale à un problème de code, mais aussi le scaffold, c'est-à-dire le plan d'action, les appels d'outils, la logique avec laquelle le modèle décide quand réessayer ou quand changer d'approche. C'est une différence subtile mais importante par rapport au fine-tuning traditionnel, un peu comme apprendre à quelqu'un non seulement à résoudre des mots croisés, mais aussi à construire lui-même la grille pour les aborder. Dans les benchmarks déclarés, ce choix se traduit par des scores remarquables sur Terminal-Bench 2.1, où le 35B atteint 64,2, et sur SWE-bench Verified, à 75,6, des résultats qui surpassent des modèles plus célèbres comme Qwen 3.5 et Qwen 3.6 dans leurs catégories de poids respectives.
![grafico1.jpg](grafico1.jpg)
[image tirée de deep-reinforce.com](https://deep-reinforce.com/ornith_1_0.html)

## Un œil en plus, non déclaré

Il y a un détail qui mérite d'être raconté en détail, car il illustre bien le fonctionnement réel de l'écosystème open source lorsqu'il est en bonne santé. Sur la page officielle de DeepReinforce et dans la fiche modèle originale, aucune mention n'est faite de capacités multimodales : Ornith-1.0 est présenté exclusivement comme un modèle textuel pour le coding agentique, bien que doté d'un support natif pour les appels d'outils à la OpenAI. Pourtant, en cherchant parmi les conversions GGUF disponibles sur Hugging Face, on trouve un fichier séparé mis en ligne par [bartowski](https://huggingface.co/bartowski/deepreinforce-ai_Ornith-1.0-35B-GGUF/blob/main/mmproj-deepreinforce-ai_Ornith-1.0-35B-bf16.gguf), l'un des quantificateurs les plus prolifiques et les plus fiables de la communauté, étiqueté mmproj : il s'agit du projecteur visuel qui, copié dans le même dossier que le modèle principal, débloque la lecture d'images dans LM Studio.

Je l'ai testé par curiosité, m'attendant à une erreur ou au mieux à un support boiteux, et pourtant cela a fonctionné sans accroc, ouvrant la voie aux deux tests multimodaux de cet épisode. C'est un petit exemple de la façon dont, dans le monde des modèles ouverts, les fonctionnalités réelles finissent par être plus larges que celles déclarées dans la fiche technique officielle, grâce au travail de l'ombre de ceux qui démontent, convertissent et recomposent les poids pour les faire tourner partout. Cela sert aussi de rappel pour ceux qui ne se fient qu'à la documentation officielle pour évaluer les capacités d'un modèle : le risque de sous-estimer son potentiel réel est concret.

## Le banc d'essai

La configuration utilisée dans LM Studio suit celle déjà éprouvée lors des épisodes précédents, avec quelques adaptations dues à la taille du modèle. J'ai travaillé avec la quantification Q6_K, un compromis qui maintient la qualité des réponses très proche de l'originale tout en sacrifiant un peu d'espace disque, avec un contexte réglé à 25 042 tokens, un déchargement GPU sur 20 des 32 couches totales, un pool de 8 threads CPU, un batch d'évaluation à 2048 et une taille de batch à 512, avec un maximum de 4 prédictions concurrentes et 8 experts actifs par token, conformément à la configuration par défaut indiquée par DeepReinforce.

Les huit tests couvrent le même terrain que celui exploré dans les épisodes précédents de la série, du raisonnement scientifique pur à la tenue de la mémoire conversationnelle sur plusieurs tours, en passant par la multimodalité, la génération de code, la planification multilingue, la gestion de documents très longs, le raisonnement spatial et les capacités agentiques multi-étapes.

## Huit défis, un verdict

### Test 1 — Raisonnement scientifique : le mécanisme de Higgs *(5/5)*

Le premier banc d'essai était de ceux qui mettent en difficulté même les modèles renommés : expliquer le mécanisme de rupture de symétrie électrofaible, le rôle du champ de Higgs, la raison pour laquelle les bosons W et Z acquièrent une masse alors que le photon reste sans masse. Ornith a répondu avec une structure en cinq blocs logiques, du cadrage du problème jusqu'à une mention finale du boson physique, avec des formules correctes et des interprétations physiques précises, dans un registre que je qualifierais de manuel universitaire bien écrit, ni trop technique ni édulcoré.

### Test 2 — Multimodalité : lire une feuille de calcul d'entreprise *(5/5)*

Le deuxième test, celui du tableau Excel flou mentionné en introduction, a confirmé ce que j'avais pressenti au premier coup d'œil : lecture correcte des données malgré la piètre qualité de l'image, identification des relations entre les colonnes, une analyse de business intelligence qui a noté la réduction progressive de l'entreprise, le fort désendettement, le capital net triplé et surtout la dégradation de la liquidité, avec un commentaire pertinent également sur la signification d'une valeur négative dans les passifs consolidés.
![screenshot1.jpg](screenshot1.jpg)
*Capture d'écran lors du test sur l'image de la feuille Excel*

### Test 3 — Génération de code : un problème NP-hard *(5/5)*

Sur le front de la génération de code, la tâche consistait à implémenter en Python un algorithme pour le cycle maximum dans un graphe non orienté, un problème NP-hard qui se réduit au cycle hamiltonien. Ornith l'a reconnu immédiatement, commençant par la note théorique correcte avant même d'écrire une ligne de code, pour ensuite fournir une implémentation avec backtracking et un élagage intelligent pour éviter les doublons, documentée et correcte, accompagnée d'une analyse de la complexité dans le pire des cas et d'un tableau de stratégies alternatives pour différents scénarios. Le sentiment ici est celui de parler à quelqu'un qui a réellement étudié l'informatique théorique, et non simplement mémorisé des patterns de code récurrents.

### Test 4 — Multilinguisme et planification : cinq jours au Japon *(5/5)*

Le quatrième test a placé la barre plus haut sur le multilinguisme, en demandant la planification d'un voyage de cinq jours au Japon pour un client français, avec un itinéraire en français et une section finale en italien. Le français produit est fluide et naturel, l'itinéraire équilibre temples historiques et street food avec une logistique crédible, cite des quartiers moins fréquentés comme Yanaka ou Omoide Yokocho et suggère d'arriver à Fushimi Inari avant 8h30 pour éviter la foule, un conseil que quiconque a visité Kyoto sait à quel point il est précieux. La section finale en italien est tout aussi solide, avec des indications pratiques sur le JR Pass, la Suica et les applications de traduction hors ligne.

### Test 5 — Contexte long : 460 pages à la volée *(5/5)*

Avec le cinquième test, nous sommes passés à la gestion du contexte long, en téléchargeant l'intégralité de l'AI Index Report 2025, quatre cent soixante pages, et en demandant des informations sur la génération vidéo avec l'indication des pages de référence correspondantes. Ornith a répondu dès la première tentative, indiquant avec précision les pages 126 et 127, citant les principaux modèles du secteur, l'exemple viral du spaghetti eating test et les benchmarks internes cités dans le rapport, précisant même que la page suivante déplace le sujet vers la reconnaissance vocale. Une précision chirurgicale.

### Test 6 — Raisonnement spatial : la chambre en plein chaos *(5/5)*

Le sixième test, le test visuel activé grâce au fichier mmproj déniché sur Hugging Face, demandait de décrire la photo d'une chambre en désordre et de proposer une stratégie de rangement. La description a couvert tous les éléments principaux, du miroir au meuble, du bureau encombré au lit défait, avec une stratégie d'intervention censée : d'abord le sol pour dégager un passage, puis le lit pour définir l'espace, enfin le bureau et le panier, chaque étape étant justifiée de manière pratique.

### Test 7 — Agent multi-étapes : planifier un projet logiciel *(5/5)*

Le septième test mesure la capacité à organiser le travail, pas seulement à l'exécuter. J'ai demandé de planifier le développement d'une application web pour la gestion des dépenses familiales : stack technique, structure du projet, roadmap détaillée pour une équipe de deux développeurs. Ornith a proposé un stack cohérent basé sur Next.js, Node.js, PostgreSQL, Prisma et Redis, une structure modulaire organisée par fonctionnalités et une roadmap avec des livrables et des points critiques pour chaque sprint, avec des conseils de développeur senior comme la mise en place de la base de données en premier et la validation des entrées avec Zod.

### Test 8 — Conversation longue : cohérence sur quatre tours *(5/5)*

Le dernier test a vérifié la tenue sur une conversation longue, articulée en quatre tours sur le stack, les notifications, la base de données et la scalabilité de la même application de gestion de tâches. Ornith a maintenu sa cohérence tout au long de la conversation, se souvenant des choix faits lors des tours précédents et s'appuyant dessus : de la comparaison entre WebSocket et polling pour mille utilisateurs simultanés, accompagnée d'exemples de code, jusqu'à un schéma Prisma complet avec relations et index, pour finir par une stratégie de scalabilité à dix mille utilisateurs abordant l'équilibrage de charge, les adaptateurs Redis, les réplicas de lecture et le cache. Seule note à signaler, attendue avec l'augmentation du contexte, un léger ralentissement progressif des tokens/s à chaque itération.
![tabella1.jpg](tabella1.jpg)

Le score final, huit sur huit, je ne l'avais pas encore vu dans cette série, et cela mérite d'être souligné : aucun des modèles testés jusqu'ici, que ce soit Qwen 3.5 9B, Gemma 4 dans ses variantes 12B et 26B, ou même Qwen 3.6 35B, n'avait réussi à maintenir le maximum sur les huit fronts simultanément.

## Lumières et ombres

Cela dit, un résultat parfait dans un test personnel mené par un seul observateur, sans contre-vérifications ni échantillons statistiquement représentatifs, doit être pris pour ce qu'il est : une indication forte, pas une vérité absolue. Les benchmarks déclarés par DeepReinforce doivent être lus en sachant que l'entreprise a évidemment intérêt à se présenter sous son meilleur jour par rapport à Qwen 3.5 et Qwen 3.6, et certains observateurs indépendants de la communauté ont déjà commencé à demander des mesures de vitesse indépendantes sur un matériel différent du mien, étant donné que les chiffres de débit circulent pour l'instant surtout parmi ceux qui ont déjà téléchargé le modèle.

Il y a ensuite la question de la multimodalité non déclarée, qui d'un côté illustre la vitalité de l'écosystème autour des poids ouverts, de l'autre soulève une question délicate sur la responsabilité lorsqu'une fonctionnalité émerge d'un fichier mis en ligne par un simple utilisateur de la communauté et non par le développeur original du modèle : si quelque chose tourne mal dans l'interprétation d'une image, qui en est responsable, l'entreprise qui a entraîné le modèle ou celui qui en a dérivé le projecteur visuel. Ce sont des questions ouvertes que soulève la phase actuelle des modèles locaux, et qui trouveront difficilement une réponse tranchée à court terme.

Ceux qui gagnent dans ce scénario sont sans aucun doute les développeurs indépendants et les petits studios qui peuvent se permettre des agents de codage de niveau compétitif sans payer d'abonnements mensuels à des fournisseurs de cloud, grâce notamment à la licence MIT qui ne pose aucune contrainte d'utilisation commerciale. Ceux qui risquent de perdre quelque chose à moyen terme sont les fournisseurs de modèles propriétaires spécialisés dans le codage, qui voient leur avantage concurrentiel se réduire sur des segments de marché de plus en plus larges, tandis qu'il reste à voir comment ce type de modèles tient la comparaison sur des tâches plus longues et plus complexes que celles qu'un simple test d'après-midi parvient à mettre en scène, une question que je laisse volontiers ouverte pour le prochain épisode.

Pour l'instant, assis devant mon PC avec le ventilateur de la Radeon qui se fait entendre un peu plus que d'habitude, il reste le sentiment d'avoir touché du doigt un autre petit saut de qualité réel dans les modèles locaux.
