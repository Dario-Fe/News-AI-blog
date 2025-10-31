---
tags: ["Research", "Training", "Applications"]
date: 2025-10-31
author: "Dario Ferrero"
---

# Le Modèle de Base Savait Déjà Raisonner (Il Suffisait de le Demander de la Bonne Manière)
![power-vs-smart.jpg](power-vs-smart.jpg)

*Lorsque DeepSeek-R1 a démontré des capacités de raisonnement quasi humaines au début de 2025, l'industrie de l'IA a célébré une énième victoire de l'apprentissage par renforcement. Le paradigme semblait incontestable : pour obtenir des modèles capables de raisonner sur des problèmes complexes de mathématiques, de codage ou de science, il fallait un post-entraînement massif basé sur le RL. [OpenAI avec o1](https://openai.com/index/learning-to-reason-with-llms/), [Anthropic avec Claude](https://docs.claude.com), et même les projets open source comme [Qwen2.5-Math](https://github.com/QwenLM/Qwen2.5-Math) ont suivi cette voie : prendre un modèle de base, construire un modèle de récompense précis, préparer des ensembles de données soignés de problèmes vérifiables, puis entraîner avec des algorithmes comme GRPO (Group Relative Policy Optimization) en investissant des semaines de calculs sur des clusters de GPU.*

Le coût de cette orthodoxie est considérable. Nous ne parlons pas seulement de millions de dollars en ressources de calcul, mais aussi de la complexité de l'ingénierie : balayage des hyperparamètres pour éviter l'instabilité pendant l'entraînement, ensembles de données diversifiés à soigner manuellement, et des signaux de récompense qui doivent être parfaits, sinon le modèle apprend des comportements indésirables. Comme l'ont documenté des [chercheurs d'AWS et de Carnegie Mellon](https://aws.amazon.com/blogs/machine-learning/fine-tune-large-language-models-with-reinforcement-learning-from-human-or-ai-feedback/), le processus RLHF nécessite une infrastructure sophistiquée où le modèle de récompense, l'optimisation de la politique et le contrôle de la divergence KL doivent s'équilibrer dans un équilibre précaire.

Pourtant, ces derniers mois, des signes inquiétants sont apparus. Plusieurs articles ont commencé à documenter un phénomène curieux : lorsqu'on compare le pass@k (la probabilité qu'au moins une réponse sur k soit correcte) des modèles de base par rapport à ceux post-entraînés avec RL, pour des valeurs élevées de k, les modèles de base l'emportent souvent. La recherche "[Rewarding the Unlikely](https://arxiv.org/html/2506.02355v1)" d'Andre He et de ses collègues a identifié ce qu'ils appellent un "biais de rang" dans GRPO : l'algorithme renforce des trajectoires déjà probables en négligeant celles qui sont rares mais correctes, produisant ce qu'ils définissent comme un "affûtage de la distribution". Le modèle post-RL résout certains problèmes avec moins d'échantillons, mais il est moins performant que le simple échantillonnage multiple à partir du modèle original.

C'est comme si le RL n'enseignait pas vraiment de nouvelles capacités, mais se contentait de rendre plus facile la pêche des bonnes réponses du premier coup, en sacrifiant la diversité des réponses. Un compromis qui, dans des domaines avec des vérificateurs parfaits comme la "démonstration de théorèmes" formelle, commence à ressembler à une très mauvaise affaire.

## La Provocation de Harvard

Dans ce contexte, la recherche "[Reasoning with Sampling: Your Base Model is Smarter Than You Think](https://arxiv.org/abs/2510.14901)" d'Aayush Karan et Yilun Du de l'Université de Harvard arrive comme une provocation méthodologique. La question qu'ils posent est radicale : et si les capacités de raisonnement étaient déjà toutes présentes dans le modèle de base, simplement masquées par des stratégies d'échantillonnage inefficaces ?

L'intuition n'est pas nouvelle. Ceux qui connaissent "La Lettre volée" d'Edgar Allan Poe se souviendront que parfois la solution se cache à la vue de tous, trop évidente pour être remarquée. Karan et Du proposent quelque chose de similaire : au lieu de mois d'entraînement RL, ils utilisent un algorithme d'échantillonnage plus intelligent qui exploite les probabilités déjà contenues dans le modèle de base. Pas de nouveaux poids, pas de descente de gradient, pas de modèle de récompense. Juste une manière différente d'extraire des séquences du modèle existant.

Leur méthode s'appelle le Power Sampling et les résultats sont surprenants. Sur [MATH500](https://arxiv.org/abs/2103.03874) (problèmes de mathématiques de niveau compétitif), leur approche sans entraînement atteint 74,8 % de précision en un seul essai avec Qwen2.5-Math-7B, presque identique aux 78,5 % obtenus avec GRPO après des semaines d'entraînement. Mais la vraie surprise vient des tâches hors domaine : sur [HumanEval](https://arxiv.org/abs/2107.03374) (problèmes de codage), le Power Sampling obtient 57,3 % contre 53,7 % pour GRPO, et sur [AlpacaEval 2.0](https://arxiv.org/abs/2404.04475) (utilité générale), il atteint un score impressionnant de 2,88 contre 2,38 pour le modèle post-entraîné.

Comme dans les meilleures histoires de Moneyball, où Billy Beane a découvert que l'efficacité statistique battait les budgets millionnaires, ici l'algorithme intelligent semble rivaliser avec la force brute computationnelle. Mais comment fonctionne exactement ce Power Sampling ?
![benchmark.jpg](benchmark.jpg)
[Image tirée de l'article officiel de Harvard](https://arxiv.org/pdf/2510.14901)

## Le Problème de l'Échantillonnage Traditionnel

Pour comprendre l'innovation de Karan et Du, il faut d'abord comprendre comment les modèles de langage génèrent du texte. À chaque étape, le modèle calcule une probabilité pour chaque jeton suivant possible. L'échantillonnage "glouton" (greedy) prend toujours le plus probable, produisant une sortie déterministe mais souvent répétitive et banale. Pour introduire de la variété, l'industrie utilise depuis des années ce qu'on appelle "l'échantillonnage à basse température" : on modifie les probabilités pour rendre les choix à haute probabilité encore plus attrayants, comme si on réglait un thermostat qui contrôle à quel point le modèle est prêt à prendre des risques.

Le problème est que cette approche ne regarde que le jeton suivant, ignorant complètement ce qui se passera dans les étapes ultérieures. C'est comme choisir quelle route prendre en ne regardant que le premier mètre : peut-être que celle qui semble la plus belle au début mène à une impasse, tandis que la moins visible débouche sur une autoroute.

Les chercheurs de Harvard expliquent le phénomène avec une analogie éclairante. Imaginez que vous deviez choisir entre deux jetons. Le premier a de nombreuses suites possibles, toutes médiocres. Le second en a très peu, mais l'une d'entre elles est excellente. L'échantillonnage traditionnel à basse température a tendance à préférer le premier, car "en moyenne" ses suites semblent avoir une probabilité décente. Mais vous pariez sur la quantité plutôt que sur la qualité.

Cela est directement lié à ce que les articles récents appellent des "fenêtres critiques" ou des "jetons pivots" : des moments dans la génération où un seul mauvais jeton piège le modèle dans une trajectoire vouée à l'échec. Des [chercheurs comme Li, Karan et Chen](https://arxiv.org/abs/2502.00921) ont documenté comment ces points critiques sont fortement corrélés avec des erreurs de raisonnement. Le modèle avait la bonne réponse dans ses probabilités internes, mais la méthode d'échantillonnage l'a conduit sur la mauvaise voie.

## Power Sampling : Regarder vers l'Avenir

La solution proposée par Harvard s'appelle la "distribution de puissance" et est conceptuellement élégante : au lieu de ne regarder que le jeton suivant, elle considère explicitement la probabilité de séquences futures entières. En pratique, le modèle ne demande plus "quel jeton est le plus probable maintenant ?", mais "quel jeton me mène vers les séquences complètes les plus probables ?".

La différence semble subtile mais elle est profonde. Reprenons l'exemple du carrefour : avec la méthode traditionnelle, si le premier jeton mène à dix routes médiocres (disons, chacune avec une probabilité de 5 %), le modèle voit un total de 50 % et trouve cela attrayant. Le second jeton ne mène qu'à deux routes, mais l'une a une probabilité de 40 %. La méthode traditionnelle préfère la première. Le Power Sampling, lui, regarde la meilleure route possible à partir de chaque carrefour et dit : "le second jeton peut me mener à une séquence avec 40 % de probabilité, le premier au maximum à 5 %. Je choisis le second".

Cette approche résout naturellement le problème des jetons pivots. Lorsque le modèle arrive à l'un de ces moments critiques où un choix le piège et l'autre le libère, le Power Sampling a tendance à choisir celui qui le libère, car il regarde explicitement les conséquences à long terme.

Mais il y a un problème technique non négligeable : pour calculer les probabilités de toutes les séquences futures possibles, il faudrait des calculs astronomiques. Avec un vocabulaire de cinquante mille jetons et des séquences de mille jetons, nous parlons de 50000^1000 possibilités à évaluer. C'est littéralement impossible.

## MCMC : Monte-Carlo Sauve la Situation

C'est ici qu'intervient un pan de l'histoire de la statistique computationnelle qui remonte aux années 1950. L'algorithme de Metropolis-Hastings, [proposé à l'origine en 1953](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm) par une équipe de physiciens du Laboratoire national de Los Alamos pour simuler des systèmes atomiques, résout exactement ce type de problème : comment échantillonner à partir d'une distribution lorsqu'il est impossible de la calculer directement.

L'idée est ingénieuse. Au lieu de tout calculer, on construit une "marche aléatoire intelligente" à travers l'espace des possibilités. On part d'une séquence quelconque. On propose une modification aléatoire (par exemple, régénérer une partie de la séquence). Ensuite, on compare la probabilité de la nouvelle version avec celle de l'ancienne. Si la nouvelle est meilleure, on l'accepte. Si elle est moins bonne, on l'accepte quand même avec une certaine probabilité qui dépend de combien elle est moins bonne. On répète ce processus de nombreuses fois.

Ce qui est bien, c'est qu'il n'est pas nécessaire de calculer des probabilités absolues, il suffit d'avoir les probabilités relatives : nouvelle contre ancienne. Et ça, les modèles de langage savent très bien le faire, car c'est exactement ce qu'ils font lors de l'inférence normale. La magie mathématique de Metropolis-Hastings garantit que si l'on répète ce processus suffisamment de fois, notre "marche aléatoire" converge pour échantillonner exactement à partir de la distribution souhaitée.

Karan et Du mettent en œuvre une variante spécifique pour les modèles de langage. À chaque étape de l'algorithme, ils choisissent au hasard un point dans la séquence et régénèrent tout à partir de là. Ensuite, ils comparent la probabilité totale de la nouvelle séquence avec l'ancienne (toujours en utilisant le modèle de base) et décident de conserver la nouvelle version ou de rester avec l'ancienne. Le processus est répété plusieurs fois pour chaque "bloc" de texte généré.

C'est comme un sculpteur qui travaille la pierre : il part d'une forme brute et l'affine progressivement par des coups stratégiques, en acceptant les améliorations et en tolérant occasionnellement de petits pas en arrière pour éviter de rester bloqué. Chaque "coup" coûte une régénération partielle du texte, mais le résultat final est une séquence qui échantillonne à partir de la distribution souhaitée.

## Les Chiffres qui Renversent la Table

Les benchmarks ne mentent pas. Sur trois modèles différents ([Qwen2.5-Math-7B](https://huggingface.co/Qwen/Qwen2.5-Math-7B), [Qwen2.5-7B](https://huggingface.co/Qwen/Qwen2.5-7B), et [Phi-3.5-mini-instruct](https://huggingface.co/microsoft/Phi-3.5-mini-instruct)), le Power Sampling obtient des gains énormes par rapport aux modèles de base. On parle d'améliorations de 25 % sur MATH500 avec Qwen2.5-Math, et même de 52 % sur HumanEval avec Phi-3.5-mini. Mais la comparaison la plus intéressante est avec GRPO, la méthode RL considérée comme l'état de l'art.

Sur MATH500, qui est le domaine où GRPO a été entraîné (il a littéralement vu des milliers de problèmes de mathématiques similaires pendant l'entraînement), le Power Sampling s'en approche de très près : 74,8 % contre 78,5 %. Un écart de 3,7 % n'est pas négligeable, mais considérez le contexte : GRPO a nécessité des jours d'entraînement sur un cluster de GPU, une optimisation des hyperparamètres et des ensembles de données soignés. Le Power Sampling fonctionne sur un modèle complètement gelé, sans jamais toucher un seul poids.

La vraie révélation, cependant, vient lorsqu'on sort du domaine d'entraînement. Sur HumanEval, un benchmark de problèmes de codage, le Power Sampling avec Qwen2.5-Math obtient 57,3 % contre 53,7 % pour GRPO. Il bat le modèle spécialisé en mathématiques sur des problèmes de programmation. Sur AlpacaEval 2.0, qui mesure l'utilité du modèle dans des conversations génériques (sans possibilité de vérification automatique), le Power Sampling atteint 2,88 contre 2,38 pour GRPO, soit un avantage de 21 %.

Avec Phi-3.5-mini, l'écart devient dramatique : 73,2 % contre 13,4 % sur HumanEval. Ce n'est pas une faute de frappe : le modèle post-entraîné avec RL s'effondre sur une tâche hors de son ensemble d'entraînement, tandis que le Power Sampling maintient d'excellentes performances.

Mais la donnée la plus révélatrice est peut-être le graphique du pass@k, c'est-à-dire le nombre de fois où au moins une réponse sur k tentatives est correcte. GRPO montre le problème classique de "l'effondrement de la diversité" : le pass@16 est à peine supérieur au pass@1, signe que le modèle génère toujours des réponses très similaires. Le Power Sampling, en revanche, maintient une courbe toujours croissante, qui se rapproche progressivement du plafond du modèle de base. En pratique : il obtient des performances en un seul essai comparables à GRPO mais conserve la capacité du modèle original à explorer des solutions différentes.

Une analyse plus approfondie confirme l'intuition. Lorsque les chercheurs mesurent à quel point les réponses générées sont "probables" (selon le modèle de base), ils constatent que GRPO produit un pic très étroit sur les séquences à très haute probabilité. C'est comme s'il avait appris une recette spécifique et la répétait obsessionnellement. Le Power Sampling, lui, distribue ses réponses sur une gamme plus large de séquences probables, maintenant la diversité sans sacrifier la qualité.

Un phénomène curieux : les réponses du Power Sampling sont en moyenne aussi longues que celles de GRPO (environ 679 jetons contre 671 sur MATH500), bien que l'algorithme n'encourage pas explicitement les séquences longues. Le "raisonnement étendu" émerge naturellement, probablement parce que des chemins de raisonnement plus articulés et détaillés ont tendance à avoir des probabilités composées plus élevées dans le modèle de base.
![confronto.jpg](confronto.jpg)
[Image tirée de l'article officiel de Harvard](https://arxiv.org/pdf/2510.14901)

## Le Coût du Raisonnement Intelligent

Bien sûr, rien n'est gratuit. Le Power Sampling nécessite plus de calculs lors de l'inférence. Les chercheurs estiment que, avec les paramètres utilisés dans leurs expériences, la génération d'une réponse nécessite environ 8,84 fois plus de jetons qu'une génération standard. C'est parce que l'algorithme régénère à plusieurs reprises des parties de la séquence dans le processus de "raffinement" MCMC.

Pour mettre les choses en perspective : une époque d'entraînement GRPO avec une configuration standard coûte de toute façon plus cher, car elle doit générer plusieurs déploiements (rollouts) pour chaque exemple et gérer un ensemble de données plus grand. Mais il y a une différence fondamentale : le coût de GRPO est ponctuel (on paie une fois, puis le modèle est plus rapide), tandis que le Power Sampling paie le coût à chaque inférence.

Cependant, il y a un autre côté à la médaille. GRPO nécessite des GPU puissants avec beaucoup de mémoire pour conserver en RAM les poids du modèle, les états de l'optimiseur et calculer les pénalités KL. Le Power Sampling peut fonctionner sur du matériel moins cher optimisé pour l'inférence, car il ne modifie jamais les poids. Et surtout : il fonctionne sur n'importe quel modèle de base, sans avoir besoin d'ensembles de données soignés, de signaux de récompense parfaits ou de semaines de surveillance de l'entraînement.

Les expériences montrent également que l'algorithme est étonnamment robuste. Le principal paramètre à régler (appelé alpha dans l'article) fonctionne bien dans une large gamme : toute valeur entre 2 et 6 produit des résultats comparables pour les tâches mathématiques. Le nombre d'étapes MCMC nécessaires est modeste : dès 2 étapes, on observe des améliorations substantielles, et 10 étapes semblent suffisantes pour converger. Plus que cela n'ajoute que peu.

Cela suggère que l'algorithme "mélange" efficacement l'espace des séquences possibles, en évitant les pathologies typiques des MCMC en haute dimension où il faudrait des millions d'itérations pour converger. C'est un signe que l'intuition théorique se traduit par une pratique algorithmique fonctionnelle.

## Implications et Questions Ouvertes

Cependant, des limitations existent et il est important de les reconnaître. Tout d'abord, il s'agit d'une recherche préliminaire : la mise à l'échelle au moment du test est encore un territoire largement inexploré. Nous ne savons pas comment le Power Sampling se comporte dans des conversations longues à plusieurs tours, ou sur des tâches qui nécessitent une mémoire contextuelle étendue. Pour les domaines où la vérification est coûteuse ou impossible (comme l'écriture créative ou le résumé subjectif), la mesure des avantages devient beaucoup plus nuancée.

Ensuite, il y a un aspect épistémologique plus profond que l'article n'aborde que de manière tangentielle : si le Power Sampling fonctionne si bien, que nous dit-il vraiment sur l'apprentissage par renforcement ? Une réponse optimiste est que le RL et le Power Sampling capturent des signaux complémentaires : peut-être que le RL enseigne effectivement de nouveaux schémas de raisonnement qui émergent pendant l'entraînement, tandis que le Power Sampling est meilleur pour extraire des capacités déjà latentes.

Mais l'interprétation la plus provocatrice est qu'une grande partie du gain du RL est un "affûtage de distribution coûteux" reproductible avec un "échantillonnage bon marché". Si c'est le cas, les courbes de mise à l'échelle devraient être réinterprétées. Non plus "combien de RL faut-il pour une amélioration de X %", mais "quel gain le RL apporte-t-il au-delà du plafond du modèle de base avec un échantillonnage optimal".

Cette perspective est directement liée à nos articles précédents sur le [TRM de Samsung](https://aitalk.it/it/trm-samsung.html) et le [DeepConf de Microsoft](https://aitalk.it/it/AI-deepconf.html), où nous avons exploré comment des stratégies algorithmiques intelligentes peuvent obtenir des résultats compétitifs sans recourir à une échelle brute. Le TRM utilisait la récupération au moment du test pour améliorer la factualité, le DeepConf exploitait la confiance intrinsèque pour l'auto-correction, et le Power Sampling extrait le raisonnement des probabilités de base. Le fil rouge est clair : l'intelligence artificielle de 2025 redécouvre que parfois le problème n'est pas la taille du modèle, mais la manière dont on l'utilise.

Il y a ensuite la question pratique de l'adoption. Le Power Sampling nécessite des modifications substantielles de l'infrastructure d'inférence : au lieu d'un simple passage avant, il faut mettre en œuvre la boucle MCMC avec acceptation/rejet. Les fournisseurs d'API devraient-ils exposer cela comme une option ? À quel prix ? Comment équilibrer la latence perçue par l'utilisateur (qui augmente) avec la qualité de la réponse ?

Et il y a des implications concurrentielles intéressantes. Les modèles open source pourraient utiliser le Power Sampling pour rivaliser avec des modèles propriétaires plus grands sans avoir besoin de post-entraînements coûteux. Mais les propriétaires pourraient combiner les deux approches : entraînement RL plus Power Sampling à l'inférence, obtenant ainsi le meilleur des deux mondes. Qui gagnera cette course dépendra de la rapidité avec laquelle l'écosystème s'adaptera.

Dans une industrie obsédée par "plus c'est gros, mieux c'est" et "plus d'entraînement, c'est mieux", des recherches comme celle de Harvard sont des rappels salutaires que l'innovation algorithmique compte au moins autant que l'échelle. Non pas pour remplacer la mise à l'échelle (qui reste cruciale), mais pour explorer les frontières de l'efficacité où chaque jeton coûte et où chaque idée peut faire la différence entre des systèmes durables et insoutenables.

Comme le dirait tout ingénieur ayant grandi avec Ghost in the Shell, on découvre parfois que l'âme était déjà dans la machine. Il fallait juste apprendre la bonne manière de l'appeler. La question maintenant est : combien d'autres capacités latentes se cachent dans nos modèles de base, en attendant que quelqu'un invente le bon algorithme pour les extraire ?