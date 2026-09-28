---
tags: ["Generative AI", "Training", "Startups"]
date: 2026-09-30
author: "Dario Ferrero"
---

# Empero et la distillation : j'ai testé leur Qwen3.8-35B-A3B
![empero-qwen38-35b.jpg](empero-qwen38-35b.jpg)

*Lorsqu'un laboratoire indépendant promet de transférer le raisonnement d'un modèle de frontière dans un fichier à télécharger et à exécuter sur son propre PC, la bonne question n'est pas de savoir s'il y est parvenu sur le papier, mais ce qu'il reste de cette promesse lorsque le fichier atterrit réellement dans la RAM d'une machine grand public. C'est la question qui a guidé les épisodes précédents de cette série, de [Qwen 3.5 9B](https://aitalk.it/it/qwen3.5-locale-puntata1.html) en passant par [Qwen 3.6 35B](https://aitalk.it/it/qwen36-35b-ai.html), et qui revient aujourd'hui avec un protagoniste différent : non pas un modèle officiel d'un laboratoire milliardaire, mais un projet allemand nommé [Empero](https://empero.org/) et l'un de ses distillats, [Qwen3.8-35B-A3B-Distill](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill).*

## Un laboratoire allemand face au cloud

Empero se décrit comme un laboratoire de recherche indépendant basé en Allemagne, dédié à la construction de modèles linguistiques suffisamment efficients pour tourner sur du matériel appartenant à l'utilisateur, sans passer par une API tierce. Ce n'est pas un slogan isolé : sur leur site, la section consacrée aux entreprises européennes explique qu'un nombre croissant de sociétés ne peuvent pas envoyer de données réglementées vers une API étrangère, et qu'un modèle sous licence Apache-2.0 exécutable en local, vérifiable jusqu'aux poids, répond exactement à cette contrainte. C'est un positionnement commercial avant d'être technique, et il vaut la peine de l'avoir à l'esprit en lisant les chiffres qui suivent.

L'écosystème qu'Empero a construit autour de cette philosophie est plus vaste que le modèle unique que je vais tester aujourd'hui. Il existe des familles de distillats issus de Qwen3.8, disponibles dans des tailles de 2, 4 et 9 milliards de paramètres en plus de la version 35B que nous utiliserons aujourd'hui ; il y a la gamme Qwythos qui compte plus d'un million de téléchargements sur Hugging Face ; un agent de codage en ligne de commande appelé [Abacus](https://github.com/empero-org/abacus) conçu pour travailler avec des points de terminaison (endpoints) locaux ou distants ; et des outils de recherche internes comme `rethink` pour générer des traces de raisonnement, `SFTSuite` pour les organiser en cursus (curricula) et `Microverse` pour explorer de nouvelles configurations architecturales avant de lancer un entraînement complet. Le tableau n'est donc pas celui d'un fine-tuner isolé, mais d'une chaîne de valeur qu'Empero revendique comme contrôlée de bout en bout (end to end).

Pour la configuration matérielle et logicielle de ces tests — processeur AMD Ryzen 7700, 32 Go de RAM DDR5, carte graphique AMD Radeon RX 9060 XT avec 16 Go de VRAM, runtime LM Studio —, je renvoie au [premier épisode de la série](https://aitalk.it/it/qwen3.5-locale-puntata1.html), qui demeure la référence méthodologique pour ceux qui arrivent seulement maintenant.

## Ce que promet (et ne promet pas) le dernier distillat

Selon la fiche technique officielle (model card), Qwen3.8-35B-A3B-Distill est né de la distillation des modèles de frontière Qwen3.8 dans l'architecture Mixture-of-Experts de Qwen3.6-35B-A3B, entraîné sur des traces soigneusement sélectionnées des modèles enseignants couvrant la chaîne de pensée (chain-of-thought) en mathématiques, code, raisonnement général, suivi d'instructions et utilisation d'outils, filtrées par qualité avant l'entraînement. Les enseignants indiqués sont deux variantes internes de Qwen3.8 : l'une entraînée sur 2,4 trillions de tokens et l'autre appelée Flash Next. Chaque réponse s'ouvre par un bloc de réflexion appris directement des traces de l'enseignant, et non généré de manière autonome par l'élève : c'est la différence, revendiquée par Empero elle-même, entre réciter par cœur les coups d'un maître et les improviser soi-même — un peu comme le personnage principal de *Vagabond*, le manga de Takehiko Inoue, qui façonne son style en passant d'école en école au lieu de l'inventer à partir de rien.

Les chiffres sur les benchmarks doivent cependant être lus avec plus de prudence que ne le suggère le communiqué de presse. Comparé au modèle de base Qwen3.6-35B-A3B, le distillat d'Empero affiche un MMLU pratiquement inchangé (0,838 contre 0,834), une différence que la documentation technique elle-même situe dans la marge d'erreur statistique. Là où l'amélioration est la plus nette, c'est sur ARC-Challenge (passant de 0,548 à 0,582) et sur ARC-Easy (passant de 0,819 à 0,830). C'est un gain réel mais sélectif, non une supériorité généralisée : la question ouverte est de savoir si un progrès concentré sur ces deux benchmarks se traduit par un avantage perceptible dans l'usage quotidien, ou s'il reste confiné à cette batterie de tests spécifique.
![tabella1.jpg](tabella1.jpg)

Il convient également de clarifier ce qui, dans ce package, n'est pas une invention d'Empero. L'architecture Mixture-of-Experts ne vient pas d'eux ; la distillation à partir de modèles plus grands est une technique désormais répandue dans tout le secteur ; et le format GGUF est un standard de l'écosystème local déjà utilisé par des dizaines d'autres projets. Ce qu'Empero revendique comme propre n'est donc pas un ingrédient isolé, mais le contrôle direct sur l'ensemble de la chaîne de valeur qui les combine : de la génération de traces jusqu'à une technique de post-entraînement appelée FTPO, conçue pour corriger des comportements indésirables comme les boucles de répétition sans avoir à refaire un entraînement complet. Que cela suffise à justifier l'étiquette de « spécial » demeure, légitimement, une question que chaque lecteur peut trancher par lui-même.

## Le modèle sur le banc : architecture et poids

Le fichier testé s'appelle [Qwen3.8-35B-A3B-Distill](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill), construit sur le modèle de base Qwen3.6-35B-A3B et distribué sous licence Apache-2.0. L'architecture est hybride : quarante couches au total, organisées en dix cycles composés de trois couches Gated DeltaNet (une forme d'attention linéaire) suivies d'une couche d'attention complète, soit un total de dix couches d'attention complète sur quarante. Le routage des experts implique 256 experts routés plus un expert partagé, avec huit experts actifs pour chaque token généré. C'est la même logique d'orchestration partielle déjà décrite dans la revue de Qwen 3.6, mais appliquée ici par Empero à partir de ces poids pour y appliquer un SFT hors politique (off-policy) sur les traces de l'enseignant Qwen3.8 — non pas un entraînement à partir de zéro, mais un modèle portant en lui des connaissances distillées issus de traces d'un enseignant beaucoup plus vaste.

Le point qu'il convient de réitérer, car il est facile de le mal interpréter, est que les quelque 3 milliards de paramètres actifs par token concernent le calcul, et non la mémoire. Le fichier entier, avec ses 35 milliards de paramètres au total, doit tout de même être chargé intégralement en RAM ou VRAM avant que l'inférence ne puisse commencer. Les quantifications disponibles sur le [dépôt GGUF](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill-GGUF) vont de 12,5 Go pour la IQ2_M jusqu'à 71 Go pour la version BF16 complète.
![tabella2.jpg](tabella2.jpg)

Pour ce test, j'ai choisi la version Q5_K_M (25,348 Go sur disque), que la fiche technique indique comme utilisable avec environ 32 Go de VRAM ou 48 Go de RAM pour un fonctionnement confortable. Sur mon matériel — 16 Go de VRAM et 32 Go de RAM DDR5 —, cela implique nécessairement un compromis entre GPU et système, exactement le genre d'équilibre précaire déjà exploré avec Qwen 3.6.

## L'installer et le faire tourner en local

Le runtime requis doit être à jour : une version récente de `llama.cpp` prenant en charge l'architecture Qwen3.6 et les couches Gated DeltaNet MoE — une condition que le [dépôt GGUF](https://huggingface.co/empero-ai/Qwen3.8-35B-A3B-Distill-GGUF) signale explicitement, car des versions plus anciennes échouent simplement à charger le modèle. LM Studio, Ollama, Jan et KoboldCpp sont indiqués comme compatibles. Pour qui n'a encore rien installé, la procédure reste celle décrite dans le [premier épisode de la série](https://aitalk.it/it/qwen3.5-locale-puntata1.html) : téléchargement de l'installeur depuis lmstudio.ai, aucune dépendance à configurer manuellement, et détection automatique de l'accélération matérielle disponible.

Les paramètres d'inférence recommandés par la fiche technique sont température 0,6, top-p 0,95 et top-k 20, avec le bloc de réflexion intégré dans le modèle de chat (à masquer éventuellement dans les applications destinées à l'utilisateur final). Dans ma configuration, j'ai travaillé avec un contexte de 80 640 tokens, bien en deçà des 262 144 natifs mais suffisant pour la majorité des tests prévus, un déchargement (offload) GPU de 22 couches sur 41, 8 threads CPU sur 8 disponibles, une taille de lot (batch size) d'évaluation à 2048, une taille de lot physique à 512 et un maximum de 4 prédictions simultanées. C'est une configuration pensée pour un usage réaliste sur du matériel de milieu/haut de gamme, non pour extraire jusqu'au dernier token par seconde disponible.

## Dix tests, une note moyenne

La batterie de tests reprend celle des épisodes précédents, avec l'ajout de deux tests conçus pour mettre sous pression la partie agentique et conversationnelle du modèle.

Sur le mécanisme de Higgs et la rupture de la symétrie électrofaible, le modèle a produit une explication en quatre sections logiques, avec des formules correctes et une attention particulière portée à la raison pour laquelle le photon reste sans masse : note 5/5, à 26,13 tokens par seconde.

Dans le test de multimodalité — une image de faible qualité montrant un tableau de bord Excel —, le modèle a correctement lu la structure et les valeurs, identifié les motifs saisonniers et la différence entre 2017 et 2018, et proposé des recommandations concrètes sur la baisse du mois de juin : note 5/5, à 24,4 tokens par seconde.

Sur la génération de code — un problème NP-difficile de recherche du cycle maximal dans un graphe —, il a proposé trois approches complémentaires : une exacte avec retour sur trace (backtracking), une approchée sur arbre couvrant (spanning tree) et une version bornée à titre de compromis, avec un code propre et commenté : note 5/5, à 26,64 tokens par seconde (la vitesse la plus élevée de tous les tests).

Sur la planification multilingue — un itinéraire de cinq jours au Japon en français et en italien —, le français était fluide, mais deux imprécisions logistiques sont apparues (Shinjuku Gyoen confondu avec un marché de street food, JR East au lieu de JR Central pour le Shinkansen) : note 4,5/5, à 23,38 tokens par seconde.

Sur le contexte long — un PDF de 460 pages sur la croissance de la génération vidéo —, le modèle a indiqué avec précision les pages 126 et 127, citant des chiffres spécifiques et les principaux modèles du secteur dès la première tentative : note 5/5, à 22,8 tokens par seconde.

Sur le raisonnement spatial — une photographie d'une pièce désordonnée —, la réponse était correcte mais superficielle, manquant de détails sur les couleurs et affichant une justification peu claire de la stratégie de rangement : note 3,8/5, à 21,24 tokens par seconde (le seul véritable point faible de la batterie).

Sur l'agent multi-étapes — la planification d'une application web —, il a produit une pile technologique complète, un schéma de base de données dans Prisma, une feuille de route en six sprints et une section dédiée aux risques et mitigations avec un tableau probabilité-impact : note 5/5, à 23,38 tokens par seconde.

Sur la conversation longue en quatre tours, il a maintenu une cohérence totale sur l'ensemble des choix techniques précédents, proposant une architecture avec Socket.IO et Redis et une stratégie de montée en charge jusqu'à dix mille utilisateurs : note 5/5, avec une vitesse moyenne autour de 22,8 tokens par seconde.

Sur le planificateur stratégique triennal, il a élaboré un plan sur six semestres complet avec objectifs, KPI mesurables et allocation d'un budget de dix millions de dollars : note 5/5, à 22,71 tokens par seconde.

Sur l'analyste de données abstrait — un problème de logique avec trois prémisses contradictoires à formaliser —, il a identifié la contradiction et justifié le choix de la prémisse à corriger avec trois arguments solides : note 5/5, à 23,63 tokens par seconde.
![tabella3.jpg](tabella3.jpg)

La moyenne globale s'établit à 4,83 sur 5, avec une vitesse moyenne d'environ 23,7 tokens par seconde (la plus élevée enregistrée jusqu'ici dans la série). Comparé à un modèle dense de la même famille (le Qwen3.8-27B déjà testé dans un épisode précédent), l'écart de vitesse est saisissant, de l'ordre de quatre à cinq fois plus rapide à qualité de réponse perçue équivalente. C'est exactement l'écart que les architectures MoE promettent sur le papier et qui semble se traduire ici dans la pratique.
![tabella4.jpg](tabella4.jpg)

## Dans quelle mesure la promesse tient-elle en Q5

Pour en revenir à la question de départ : quelle part des capacités transmises par l'enseignant Qwen3.8 reste effectivement disponible lorsque le modèle est compressé en Q5_K_M et exécuté avec 22 couches sur GPU et le reste sur la RAM du système ? Les dix tests suggèrent que la majeure partie tient bon, avec une exception claire sur le raisonnement visuo-spatial fin et une fissure plus subtile sur la précision géographique en contexte multilingue. Mais pour déterminer si cela suffit à considérer le modèle supérieur à son modèle de base, les benchmarks officiels incitent à la prudence : le gain est concentré sur ARC, non généralisé, et le MMLU demeure pratiquement identique.

Il y a ensuite une question plus large concernant l'utilisateur. Un fichier de 25 Go nécessitant 16 Go de VRAM tout en saturant une bonne partie de la RAM système est à la portée d'un particulier passionné, mais est-il réaliste de l'imaginer comme un standard pour qui n'a pas déjà investi dans du matériel dédié ? Et au moment de choisir entre une API cloud et un modèle local comme celui-ci, quel poids pèse le fait que les données ne quittent jamais la machine, un argument qu'Empero place au cœur de son offre commerciale destinée aux entreprises européennes ? Ce sont des questions qui appellent des réponses différentes selon qui les pose, et c'est peut-être là le point le plus intéressant de toute l'expérience Empero : non pas tant de savoir si le modèle l'emporte ou s'incline face à son prédécesseur, mais si toute la chaîne de valeur qu'elle promet — de la distillation au packaging GGUF jusqu'à Abacus comme outil du quotidien — parvient à faire du local un choix praticable, et pas seulement un exercice pour passionnés disposant d'une solide carte graphique à la maison.

*Note technique : toutes les données sur l'architecture, les quantifications et les benchmarks cités dans cet article proviennent des fiches officielles sur Hugging Face et du site d'Empero, en lien dans le texte. Les notes et vitesses de génération des dix tests sont des mesures personnelles, non des certifications automatisées de benchmarks, et doivent être lues comme telles.*
