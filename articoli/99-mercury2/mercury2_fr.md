---
tags: ["Generative AI", "Research", "Startups"]
date: 2026-03-13
author: "Dario Ferrero"
---

# Mille tokens par seconde : Mercury 2 veut réécrire les règles de l'IA
![mercury2.jpg](mercury2.jpg)

*Il y a un moment étrange, presque déroutant, que quiconque a utilisé Mercury 2, d'Inception Labs, pour la première fois décrit de manière similaire : vous tapez la question, vous appuyez sur Entrée, et la réponse est déjà là, en entier, avant même que votre cerveau ait fini d'enregistrer que vous avez cliqué sur quelque chose. Ce n'est pas un effet visuel, ce n'est pas une astuce d'interface. Le modèle génère réellement plus de 1 000 tokens par seconde.*

Pour donner un ordre de grandeur : un roman italien moyen compte environ 300 000 caractères, soit approximativement 90 000 à 100 000 tokens. Mercury 2, en théorie, l'écrirait en moins de deux minutes. Claude 4.5 Haiku, l'un des modèles « rapides » les plus répandus aujourd'hui, s'arrête à environ 89 tokens par seconde. GPT-5 Mini à environ 71. La différence n'est pas incrémentielle : elle est structurelle.

Tout cela est possible parce que Mercury 2 ne fonctionne pas comme n'importe quel autre modèle de langage que vous avez pu utiliser. Et comprendre pourquoi nécessite de faire un pas en arrière sur la manière dont l'intelligence artificielle générative produit du texte, et comment, depuis toujours, elle l'a fait d'une seule et unique façon.

## Deux familles, un paradigme dominant

Si vous voulez comprendre Mercury 2, vous devez d'abord comprendre le goulot d'étranglement qu'il cherche à éliminer. Et ce goulot d'étranglement a un nom technique précis : la génération autorégressive.

Tous les grands modèles de langage que vous utilisez chaque jour, ChatGPT, Claude, Gemini, fonctionnent selon le même principe de base : ils produisent du texte un token à la fois, de gauche à droite, et chaque token dépend de tous ceux qui le précèdent. C'est comme taper à la machine : vous ne pouvez pas frapper la troisième lettre avant d'avoir frappé la deuxième. Cette dépendance séquentielle est architecturale, ce n'est pas une inefficacité éliminable avec plus de matériel ou des optimisations logicielles. C'est la nature même du mécanisme.

La diffusion (diffusion) est quelque chose de différent. La technique est née dans le monde de la génération d'images, elle est à la base de Stable Diffusion, Midjourney, DALL-E, et fonctionne de manière opposée : au lieu de construire le résultat morceau par morceau, elle part d'un résultat complètement « bruité » et imprécis, et l'affine progressivement en parallèle, sur plusieurs points simultanément, convergeant vers la réponse correcte en quelques étapes. Ce n'est plus comme une machine à écrire, mais plutôt comme un photographe qui développe un Polaroid : l'image entière émerge graduellement, d'un seul coup.

Appliquer cette technique au texte, contrairement aux images, est cependant un problème beaucoup plus difficile. Le langage possède des contraintes logiques, grammaticales et sémantiques que les images n'ont pas dans la même mesure. Pendant des années, on a estimé que la diffusion n'était pas adaptée au texte. Si vous souhaitez approfondir la comparaison technique entre les deux approches, vous trouverez [un article dédié précisément à ce sujet](https://aitalk.it/it/diffusion-vs-autoregressive.html) sur le portail.
![grafico1.jpg](grafico1.jpg)
[Image tirée de inceptionlabs.ai](https://www.inceptionlabs.ai/blog/introducing-mercury-2)

## Qui a résolu le problème impossible

La percée est venue de Stanford. Stefano Ermon, professeur d'informatique et l'un des co-inventeurs des techniques de diffusion utilisées dans Stable Diffusion et DALL-E, travaillait sur ce problème depuis 2019. Des années de recherche pour comprendre comment appliquer la diffusion au texte, jusqu'à un tournant documenté dans un article présenté à l'ICML 2024, la principale conférence internationale de machine learning, qui a remporté le prix du meilleur article. Ce n'est pas une distinction mineure : cela signifie que la communauté scientifique a officiellement reconnu l'avancée comme significative.

En 2024, Ermon a fondé Inception Labs à Palo Alto, emmenant avec lui deux anciens étudiants devenus professeurs : Aditya Grover de l'UCLA et Volodymyr Kuleshov de Cornell. L'équipe élargie comprend des chercheurs et des ingénieurs provenant de Google DeepMind, Meta AI, Microsoft AI et OpenAI, et les contributions du groupe ne se limitent pas à la diffusion : dans leur curriculum collectif figurent des travaux fondateurs sur la flash attention, les decision transformers et la direct preference optimization (DPO), des techniques qui ont marqué le développement des modèles de langage modernes.

Le financement est arrivé en novembre 2025 avec un tour de table d'amorçage (seed round) de [50 millions de dollars](https://techcrunch.com/2025/11/06/inception-raises-50-million-to-build-diffusion-models-for-code-and-text/), mené par Menlo Ventures avec la participation de Mayfield, M12 (le fonds de capital-risque de Microsoft), Snowflake Ventures, Databricks Ventures, NVentures (la branche d'investissement de NVIDIA) et Innovation Endeavors. Parmi les business angels figurent Andrew Ng et Andrej Karpathy ; ce dernier, ancien directeur de l'IA chez Tesla et cofondateur d'OpenAI, a publiquement encouragé ses abonnés à essayer le modèle, notant que la nature non autorégressive de la diffusion pourrait conduire à une « nouvelle psychologie, des forces et des faiblesses inédites ». Quand Karpathy dit que quelque chose vaut la peine d'être essayé, le secteur a tendance à l'écouter.

## Mercury 2 : ce qu'il fait, combien il coûte, ses performances

Le 24 février 2026, Inception a [lancé Mercury 2](https://www.inceptionlabs.ai/blog/introducing-mercury-2), le présentant comme le premier « reasoning LLM » basé sur la diffusion disponible en production. Les chiffres de vitesse ont été vérifiés de manière indépendante par [Artificial Analysis](https://artificialanalysis.ai/models/mercury-2), l'une des signatures de référence les plus rigoureuses du secteur : 711,6 tokens par seconde dans leurs évaluations standardisées multi-tours, ce qui place Mercury 2 à la première place sur 132 modèles surveillés. Sur la configuration matérielle optimale, les GPU NVIDIA Blackwell avec précision NVFP4, les chiffres internes d'Inception grimpent à 1 009 tokens par seconde, avec une latence de bout en bout de 1,7 seconde.

La comparaison est impitoyable pour les modèles concurrents de la même catégorie : Gemini 3 Flash termine ses réponses en 14,4 secondes, Claude 4.5 Haiku avec raisonnement en 23,4 secondes. Ce n'est pas une différence de degré, c'est une différence d'expérience utilisateur : la sensation subjective d'« instantanéité » change complètement. [InfoWorld](https://www.infoworld.com/article/4137528/inceptions-mercury-2-speeds-around-llm-latency-bottleneck.html) a bien résumé le point : Mercury 2 n'optimise pas les marges, il redessine le goulot d'étranglement.

Sur le plan qualitatif, Mercury 2 se positionne honnêtement dans la catégorie des modèles « rapides et légers », pas parmi les géants du raisonnement profond. Les benchmarks publiés sont clairs : 91,1 sur AIME 2025 (mathématiques compétitives), 73,6 sur GPQA Diamond (raisonnement scientifique avancé), 67,3 sur LiveCodeBench (codage), 52,9 sur TAU-bench (agents complexes). Ce sont des résultats compétitifs avec Claude 4.5 Haiku et GPT-5 Mini, mais pas avec Claude Opus 4.6 ou les meilleurs modèles de raisonnement étendu, qui marquent des scores de l'ordre de 80-90 sur 100 sur l'Artificial Analysis Intelligence Index, alors que Mercury 2 s'arrête à 33.

La tarification est l'un des aspects les plus intéressants : 0,25 dollar par million de tokens en entrée, 0,75 par million en sortie. À titre de comparaison, Claude 4.5 Haiku coûte environ 4,90 dollars par million de tokens en sortie, soit environ six fois et demie plus cher. GPT-5 Mini tourne autour de 1,90 dollar, soit environ deux fois et demie plus cher. À volume égal, la différence de coût dans des pipelines à fort trafic peut représenter des dizaines de milliers de dollars par mois. L'API est compatible avec le standard OpenAI : en théorie, pour ceux qui utilisent déjà l'écosystème OpenAI, c'est un remplacement sans réécriture de code.
![grafico2.jpg](grafico2.jpg)
[Image tirée de inceptionlabs.ai](https://www.inceptionlabs.ai/blog/introducing-mercury-2)

## Où Mercury 2 fonctionne-t-il vraiment

Inception est explicite sur les cas d'utilisation pour lesquels Mercury 2 est conçu, et les témoignages recueillis au lancement sont cohérents avec ce positionnement.

Le domaine le plus naturel est celui des **boucles agentiques (agentic loops)** : des systèmes où un agent IA effectue des dizaines ou des centaines d'appels d'inférence pour accomplir une tâche, analyse de code, recherche itérative, pipelines de données. Dans ces contextes, la latence ne se manifeste pas une seule fois, elle se multiplie à chaque étape. Avec les modèles traditionnels, un flux de travail en dix étapes qui nécessite 20 secondes par inférence entraîne plus de trois minutes d'attente globale. Avec Mercury 2, le même flux de travail descend sous les vingt secondes. Ce n'est pas seulement plus rapide : cela change les interactions physiquement praticables en temps réel.

Zed, un éditeur de code très suivi dans les milieux du développement avancé, est l'un des partenaires de lancement : son cofondateur Max Brunsfeld a décrit la vitesse de suggestion comme assez rapide pour sembler « faire partie de sa propre pensée ». Skyvern, une plateforme d'automatisation pour les agents web, a rapporté que Mercury 2 est au moins deux fois plus rapide que GPT-5.2 pour leurs cas d'utilisation. Wispr Flow, un outil de nettoyage en temps réel de transcriptions vocales, l'a jugé irremplaçable pour les applications d'interaction homme-machine à faible latence.

La **Voice AI** est le deuxième domaine où la vitesse devient déterminante. Les interfaces vocales ont la fenêtre de latence la plus étroite de tout l'écosystème IA : une réponse qui arrive en plus de deux secondes rompt le naturel de la conversation. À 70-90 tokens par seconde, les modèles autorégressifs sont à la limite de l'utilisabilité pour la voix. Mercury 2 supprime cette limite avec une marge énorme. OpenCall et Happyverse AI, toutes deux actives dans le secteur des avatars vocaux et des agents téléphoniques, ont cité la faible latence comme le principal facteur d'activation.

Pour les **pipelines de recherche et RAG** (Retrieval-Augmented Generation), où des documents sont récupérés, classés et résumés en séquence, Mercury 2 permet d'ajouter une étape de raisonnement dans le cycle de recherche sans faire exploser le budget de latence. SearchBlox, actif dans la recherche d'entreprise pour la conformité, l'analytique et l'e-commerce, a déclaré que le partenariat avec Inception rend « l'IA en temps réel pratique » pour leur produit.

## Les zones d'ombre du tableau : les limites qui comptent

Mercury 2 est pour le moment un modèle **uniquement textuel**. Il ne traite pas les images, l'audio ou la vidéo. Dans un paysage où la capacité multimodale est devenue presque la norme attendue, surtout pour les applications d'entreprise complexes, c'est une limitation concrète, pas un détail de bas de page.

C'est aussi un modèle **uniquement cloud, sans poids ouverts**. Il n'existe pas de version téléchargeable, aucun déploiement sur site (on-premise) n'est possible, et aucun réglage fin (fine-tuning) sur des données propriétaires n'est disponible. Pour les organisations ayant des exigences de résidence des données, de souveraineté du modèle ou des besoins d'adaptation spécialisée — des secteurs comme la santé, la finance, la défense —, cela exclut Mercury 2 pour une large classe de cas d'utilisation.

Il y a ensuite le **problème de la verbosité**. Comme documenté dans la [revue indépendante d'Awesome Agents](https://awesomeagents.ai/reviews/review-mercury-2/), Artificial Analysis a relevé que lors de leurs évaluations, Mercury 2 a produit 69 millions de tokens en sortie, contre une moyenne de 20 millions pour des modèles équivalents. Le modèle a tendance à générer plus de texte que nécessaire. En termes pratiques, ce n'est pas seulement un problème esthétique : cela gonfle le coût effectif de sortie et ajoute du bruit dans les flux de travail qui nécessitent une sortie structurée et concise. C'est un comportement gérable avec de l'ingénierie de prompt, mais c'est un réglage par défaut qui nécessite une attention particulière.

La question la plus profonde concerne la **maturité de l'architecture**. Les modèles à diffusion pour le texte sont une classe émergente, Mercury 2 est de fait le premier modèle de ce type disponible en production commerciale. Cela signifie qu'il existe moins d'ingénieurs connaissant les schémas de défaillance en production, moins de documentation sur les cas limites (edge cases), moins de communauté ayant déjà affronté et résolu les problèmes typiques. Quand quelque chose casse dans un système en production, et cela arrive toujours, le support de l'écosystème pour une technologie consolidée comme GPT ou Claude est incomparablement plus riche. Ce n'est pas une critique de l'architecture, c'est un coût réel qui n'apparaît dans aucun benchmark.

Enfin, il convient de noter que les chiffres de vitesse les plus élevés, le titre des 1 009 tokens par seconde, supposent des GPU NVIDIA Blackwell avec une précision NVFP4. Les données d'Artificial Analysis, qui reflètent l'infrastructure cloud standard réelle, attestent de 711,6 tokens par seconde : un chiffre extraordinaire, mais éloigné du gros titre. Il n'y a pas de données publiées pour du matériel plus ancien.

## Le marché parle, mais avec prudence

La question pertinente n'est pas seulement de savoir si Mercury 2 fonctionne — les preuves indépendantes suggèrent que oui, les promesses de vitesse sont réelles —, mais si le marché adopte effectivement les modèles de diffusion à grande échelle, ou si nous en sommes encore à la phase de curiosité technique.

Des signes d'adoption existent : des intégrations documentées avec des outils comme Zed, Skyvern, Wispr Flow, SearchBlox, Viant (une plateforme publicitaire qui a déclaré utiliser Mercury pour optimiser des campagnes en temps réel). La [disponibilité sur Azure AI Foundry](https://www.inceptionlabs.ai/blog/mercury-azure-foundry), annoncée en novembre 2025, ouvre Mercury au vaste écosystème d'entreprise de Microsoft. La compatibilité avec l'API OpenAI abaisse la barrière d'entrée à presque zéro pour ceux qui opèrent déjà dans cet écosystème.

D'un autre côté, la position de Mercury 2 dans la catégorie « Haiku-class » des modèles, compétitif avec les modèles rapides mais pas avec les meilleurs pour le raisonnement profond, limite structurellement son utilisation à des cas d'utilisation où la vitesse prime sur la complexité du raisonnement. Pour les décisions nécessitant l'analyse de documents longs et complexes, une synthèse multi-sources avancée ou un raisonnement sur des scénarios nuancés, les modèles de pointe conservent un avantage réel que Mercury 2 n'élimine pas. Comme l'a observé [The New Stack](https://thenewstack.io/inception-labs-mercury-2-diffusion/), Ermon lui-même est franc à ce sujet : Mercury 2 est en concurrence avec la gamme Haiku/Flash, pas avec Opus ou GPT.

Le pari d'Inception est que la trajectoire de la qualité des modèles à diffusion suivra la même courbe de mise à l'échelle que celle observée pour les modèles autorégressifs : une qualité améliorable dans le temps, avec l'avantage structurel de la vitesse comme point de départ. C'est un pari plausible, pas encore vérifié.

## Questions ouvertes : l'avenir est-il parallèle ?

Mercury 2 ne répond pas à la question la plus importante qu'il soulève : la diffusion peut-elle vraiment devenir le paradigme dominant pour les modèles de langage, ou restera-t-elle une approche spécialisée pour les cas d'utilisation à haute vitesse ?

Ermon a déclaré imaginer un futur où tous les modèles de langage seraient basés sur la diffusion. C'est une vision ambitieuse, et celui qui l'a exprimée — l'un des scientifiques ayant contribué à construire les fondations de la diffusion pour les images — a les références pour la soutenir. Mais passer de « cela fonctionne exceptionnellement bien pour un sous-ensemble spécifique de cas d'utilisation » à « cela remplace l'autorégressif comme paradigme général » est un saut énorme, et il n'y a pas encore de preuves que l'écart qualitatif avec les modèles de pointe soit destiné à se combler.

En outre, des questions ouvertes concrètes subsistent : comment les modèles à diffusion se comportent-ils sur des raisonnements à chaîne de pensée très longue, où la cohérence à travers des milliers de tokens est cruciale ? Qu'arrive-t-il à la qualité avec 50 000 ou 100 000 tokens de contexte, quand la fenêtre de 128K est réellement sollicitée ? Comment gérer éthiquement une architecture dont la production de sortie est moins interprétable étape par étape que l'autorégressif ?

La vitesse est réelle. Le coût est compétitif. L'équipe est crédible au-delà de tout doute raisonnable. Les limitations actuelles sont concrètes et documentées. Mercury 2 représente quelque chose de véritablement nouveau dans le paysage des modèles de langage, pas le modèle le plus intelligent disponible aujourd'hui, mais peut-être un signal de la direction que doit encore prendre la conversation sur l'efficacité de l'inférence de l'IA.

La machine à écrire, token après token, pourrait bien avoir ses jours comptés. Mais le roman qui sera écrit ensuite, et sa qualité, restent encore à découvrir.

---
