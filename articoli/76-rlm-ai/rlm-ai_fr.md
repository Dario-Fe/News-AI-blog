---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-01-19
author: "Dario Ferrero"
---

# Au-delà du mur du contexte : les Modèles de Langage Récursifs défient la limite invisible de l'IA
![rlm-ai.jpg](rlm-ai.jpg)

*Il existe un problème dans l'intelligence artificielle moderne dont on parle peu, mais que chaque développeur et utilisateur intensif de chatbots a expérimenté au moins une fois : le sentiment que le modèle, après une conversation prolongée, devient progressivement plus stupide. Ce n'est pas une impression subjective, ni un manque de clarté de votre part dans les requêtes. C'est un phénomène technique précis que les chercheurs appellent *context rot*, littéralement "pourriture du contexte", et il représente l'une des limites les plus frustrantes de l'architecture actuelle des grands modèles de langage.*

Imaginez devoir écrire un roman en n'ayant à votre disposition qu'un post-it. Chaque fois que vous ajoutez une nouvelle phrase, vous devez en effacer une ancienne. C'est plus ou moins ce qui se passe lorsqu'un modèle de langage atteint la limite de sa fenêtre de contexte, cette fenêtre de mémoire à court terme à l'intérieur de laquelle il peut "voir" et traiter des informations. GPT-5, le modèle phare d'OpenAI, dispose de 400 000 tokens via API (environ 300 000 mots), ce qui semble beaucoup jusqu'à ce que vous essayiez d'analyser une base de code entière ou une collection de documents juridiques. Mais le vrai problème n'est pas seulement la taille : les performances des modèles se dégradent à mesure que la longueur de l'entrée augmente, même sur des tâches triviales.

C'est là qu'intervient le travail d'Alex Zhang, Tim Kraska et Omar Khattab du MIT CSAIL, publié en décembre 2025 sur [arXiv](https://arxiv.org/html/2512.24601v1). Leur article propose les Modèles de Langage Récursifs (RLM), un cadre qui renverse complètement l'approche du problème : au lieu de chercher à étendre à l'infini la mémoire du modèle, ils lui apprennent à raisonner *sur* la mémoire elle-même, en la traitant comme un environnement externe à explorer de manière programmatique.

## Quand lire devient se souvenir

Pour comprendre l'intuition derrière les RLM, il convient de partir du problème. L'architecture transformer sur laquelle reposent les LLM modernes compare chaque nouveau token avec tous les tokens précédents dans la fenêtre de contexte, créant des relations en n² qui deviennent de plus en plus coûteuses à mesure que le contexte s'agrandit. C'est comme si, chaque fois que vous prononciez un mot, votre cerveau devait revoir mentalement toutes les conversations de votre vie. Impossible.

La recherche de Chroma [a montré](https://research.trychroma.com/context-rot) que même les modèles les plus avancés souffrent de biais positionnel : une information placée en première position obtient 75 % de précision, la même information en dixième position tombe à 55 %. Ce n'est pas une question de combien de tokens vous parvenez à insérer dans la fenêtre, mais de la manière dont le modèle parvient réellement à les utiliser.

Zhang et ses collègues ont emprunté une voie différente. Au lieu d'obliger le modèle à ingérer l'intégralité du prompt en un seul passage, les RLM traitent le prompt comme une partie d'un environnement externe avec lequel le modèle peut interagir symboliquement. En pratique, le contexte est chargé comme une variable Python dans un environnement REPL (Read-Eval-Print Loop), et le modèle peut écrire du code pour l'inspecter, le disséquer, rechercher des motifs et, ce qui est crucial, s'appeler récursivement lui-même ou d'autres LLM sur des portions spécifiques du contenu.

Pensez à la différence entre lire un livre de la première à la dernière page et le consulter comme vous le feriez avec une encyclopédie : sauter directement à l'index, identifier les sections pertinentes, peut-être prendre des notes sur ce que vous trouvez. Les RLM reproduisent cette seconde approche, métacognitive et stratégique.

## REPL : le dialogue interne

L'implémentation technique est raffinée dans sa simplicité. Lorsqu'un utilisateur envoie un prompt à un RLM, celui-ci est stocké comme une variable de chaîne dans un environnement Python REPL. Le modèle racine (appelons-le LM₀) ne reçoit jamais directement cette chaîne dans sa fenêtre de contexte. À la place, il reçoit un prompt système qui lui explique comment il peut interagir avec la variable : il peut en lire des tranches spécifiques, il peut écrire des fonctions d'aide pour la traiter, il peut lancer des appels sub-LM récursifs (LM₁, LM₂...) sur des portions sélectionnées, et il peut combiner les résultats.

En substance, le modèle travaille selon trois modes distincts. D'abord, il explore le contexte par des opérations de lecture et de recherche programmatiques, un peu comme s'il utilisait grep ou regex sur un fichier texte. Ensuite, il décompose le problème en sous-tâches plus gérables, décidant de manière autonome quelles portions de contexte méritent une analyse approfondie. Enfin, il délègue ces sous-tâches à des instances récursives de lui-même ou d'autres modèles, puis agrège les résultats en une réponse finale.

[Le dépôt GitHub officiel](https://github.com/alexzhang13/rlm) fournit une implémentation plug-and-play qui remplace simplement l'appel standard `llm.completion(prompt, model)` par `rlm.completion(prompt, model)`. L'interface externe reste identique pour l'utilisateur, mais sous le capot se déroule cette danse récursive d'exploration et de calcul.

Zhang lui-même [dans son blog](https://alexzhang13.github.io/blog/2025/rlm/) utilise une analogie éclairante : c'est comme lorsque l'historique de Claude Code devient gonflé ou que vous discutez longuement avec ChatGPT et que le modèle semble devenir progressivement plus stupide. La solution intuitive serait de diviser le contexte en deux appels distincts, puis de combiner les résultats dans un troisième : exactement ce que font les RLM de manière systématique et récursive.
![rlm-schema1.jpg](rlm-schema1.jpg)
[Image tirée de arxiv.org](https://arxiv.org/html/2512.24601v1)

## Benchmarks contre réalité

Les chiffres de l'article sont impressionnants, mais doivent être lus avec la prudence qui s'impose. Sur OOLONG, un benchmark de compréhension sur des contextes longs, un RLM basé sur GPT-5-mini a surclassé GPT-5 de base de plus du double en termes de réponses correctes, en traitant des prompts de 132 000 tokens. Sur la tâche S-NIAH (une variante plus complexe du classique "une aiguille dans une botte de foin"), les RLM gèrent des entrées jusqu'à deux ordres de grandeur au-delà des tailles natives de la fenêtre de contexte.

Mais il y a un compromis important : les coûts. L'article fait état de variations significatives par rapport à la ligne de base, dans certains cas jusqu'à trois fois supérieures, en fonction du nombre d'appels récursifs que le modèle décide d'effectuer. Ce n'est pas une baguette magique qui rend tout moins cher : c'est une architecture qui échange du temps de calcul contre des capacités de raisonnement étendues.

Sur l'ensemble de données BrowseComp-Plus, conçu pour tester des tâches de recherche et de synthèse sur d'énormes volumes de documents, les RLM ont montré qu'ils pouvaient traiter efficacement plus de 10 millions de tokens. Ici, cependant, une autre considération entre en jeu : dans certains cas, la vérification de la réponse s'est avérée redondante et a considérablement augmenté le coût par tâche. Le modèle pouvait essayer de reproduire sa réponse correcte plus de cinq fois avant de choisir la mauvaise à la fin.

C'est un rappel important : les RLM ne sont pas automatiquement optimisés pour l'efficacité. La stratégie de décomposition et de récursion est décidée par le modèle lui-même, qui peut commettre des erreurs de jugement sur le moment opportun de recourir à d'autres sous-requêtes.

## Le prix de l'infini

Prime Intellect, une organisation axée sur la recherche ouverte en IA, [a adopté les RLM comme élément central](https://www.primeintellect.ai/blog/rlm) de sa stratégie pour les agents à long horizon. Ils pensent qu'enseigner aux modèles à gérer leur propre contexte de bout en bout grâce à l'apprentissage par renforcement sera la prochaine percée, permettant aux agents de résoudre des tâches qui s'étendent sur des semaines ou des mois.

Ils ont publié RLMEnv, un environnement d'entraînement spécialement conçu pour former des modèles avec un échafaudage RLM intégré. L'idée est intrigante : au lieu d'apprendre des architectures d'attention plus efficaces (ce qui est un problème de modélisation du langage), on peut apprendre à gérer le contexte à travers le résultat des tâches résolues. Une approche complémentaire : une attention efficace retarde la pourriture du contexte, le pliage du contexte (un terme que certains utilisent pour décrire des stratégies comme les RLM) permet au modèle de le gérer activement.

Mais cela soulève des questions d'éthique et de gouvernance. Un modèle capable de gérer de manière autonome son propre contexte sur des horizons temporels aussi étendus pourrait être utilisé pour des tâches sensibles où la traçabilité des décisions devient critique. Pensons aux décisions financières, aux diagnostics médicaux ou aux évaluations juridiques : la nature récursive et programmatique des RLM rend plus complexe l'interprétabilité du processus de prise de décision par rapport à un appel LLM unique.

La loi européenne sur l'IA classe les systèmes d'IA en fonction de leur niveau de risque, et les systèmes capables de maintenir un état et un raisonnement sur de longs horizons temporels pourraient tomber dans des catégories à haut risque nécessitant des audits stricts. Ce n'est pas un problème propre aux RLM, bien sûr, mais leur capacité à fonctionner de manière autonome sur d'énormes volumes de données amplifie le besoin de mécanismes de journalisation et d'explicabilité robustes.

## Alternatives sur la table

Les RLM ne sont pas la seule réponse au problème du contexte long. Il existe au moins trois approches principales qu'il convient de comparer.

La première est la modification architecturale directe : des modèles comme Llama 4 avec ses variations de RoPE (Rotary Position Embeddings) ou Gemini 2.5 Pro avec l'attention fenêtrée sont conçus nativement pour gérer des fenêtres de contexte plus grandes. Ils fonctionnent, mais même dans des conditions minimales et contrôlées, les performances se dégradent à mesure que la longueur de l'entrée augmente de manière surprenante et non uniforme.

La deuxième est le RAG (Retrieval-Augmented Generation), où un système de récupération externe ne fournit au modèle que les morceaux pertinents d'une base de données plus large. C'est efficace pour les bases de connaissances structurées, mais nécessite une infrastructure dédiée (modèles d'intégration, bases de données vectorielles, stratégies de découpage) et introduit une dépendance à des composants externes qui peuvent devenir le goulot d'étranglement.

La troisième concerne des cadres comme MemGPT ou des systèmes multi-agents comme le DisCIPL, également développé au MIT. [Ce dernier](https://news.mit.edu/2025/enabling-small-language-models-solve-complex-reasoning-tasks-1212) utilise un LLM comme "chef de file" qui planifie la stratégie et distribue le travail à des modèles plus petits. Il fonctionne bien pour les tâches avec des contraintes vérifiables (comme la planification ou l'ordonnancement), moins pour les analyses ouvertes où la vérification de l'exactitude est nuancée.

Les RLM se positionnent dans un espace intermédiaire : plus flexibles que le RAG (pas besoin de pré-indexation), plus généraux que les systèmes multi-agents (pas besoin d'orchestration spécifique à la tâche), mais potentiellement plus coûteux que les approches architecturales natives lorsque celles-ci fonctionnent bien.
![rlm-schema2.jpg](rlm-schema2.jpg)
[Image tirée de arxiv.org](https://arxiv.org/html/2512.24601v1)

## Implémentations par la base

La communauté open source a réagi rapidement. [Une implémentation en TypeScript](https://www.reddit.com/r/opensource/comments/1q5f1sb/i_built_a_typescript_implementation_of_recursive/) est apparue sur Reddit quelques semaines après la publication de l'article, signe que l'idée trouve un écho auprès des développeurs confrontés à des problèmes concrets. Les [implémentations en Python](https://github.com/ysz/recursive-llm) prolifèrent, certaines se concentrant sur des sandboxes spécifiques (Docker, WebAssembly) pour garantir une exécution sécurisée du code généré par le modèle.

Il est intéressant de noter comment différentes implémentations communautaires expérimentent des environnements alternatifs au REPL Python. Certaines utilisent des REPL Clojure pour tirer parti de la nature immuable des données, d'autres explorent des environnements SQL pour les requêtes sur des bases de données structurées, d'autres encore Bash pour les tâches d'administration système.

Cela soulève une question plus large : dans quelle mesure le choix de l'environnement influence-t-il l'efficacité des RLM ? L'article du MIT utilise Python car c'est le langage le plus familier à la plupart des LLM (il est omniprésent dans les données d'entraînement), mais rien n'empêche d'utiliser des DSL (Domain-Specific Languages) optimisés pour des domaines d'application spécifiques.

## Questions ouvertes

Malgré les résultats prometteurs, des questions fondamentales demeurent. La première concerne l'entraînement. Zhang et Khattab sont particulièrement enthousiastes à l'idée d'enseigner explicitement aux modèles à raisonner comme des RLM, ce qui pourrait représenter un autre axe de mise à l'échelle pour la prochaine génération de systèmes linguistiques. Mais comment entraîne-t-on exactement un modèle à décomposer le contexte de manière optimale ? On pourrait utiliser des techniques d'apprentissage par renforcement sur les trajectoires REPL, en récompensant les décompositions qui minimisent le coût total tout en maintenant une grande précision.

Des modèles comme o1 d'OpenAI intègrent déjà un raisonnement étendu lors de l'inférence, mais ils le font de manière opaque et non programmatique. Les RLM pourraient bénéficier d'une approche hybride : un raisonnement interne pour planifier la stratégie de décomposition, une exécution programmatique pour la mettre en œuvre.

La deuxième question concerne la reproductibilité. Les trajectoires des RLM sont non déterministes : le même prompt peut générer des stratégies de décomposition différentes lors d'exécutions successives. C'est problématique pour les applications où la cohérence est essentielle (conformité, audit, recherche reproductible). Il faudra des techniques pour contraindre l'espace d'exploration du modèle ou pour garantir toujours le même résultat des opérations.

La troisième porte sur la scalabilité extrême. L'article teste jusqu'à plus de 10 millions de tokens, mais que se passe-t-il à 100 millions ? À 1 milliard ? À un certain point, même la gestion programmatique du contexte devient un problème de complexité de calcul. Il pourrait être nécessaire d'avoir un "méta-RLM" qui gère d'autres RLM dans une hiérarchie à plusieurs niveaux, un peu comme dans les systèmes d'exploitation avec plusieurs niveaux de cache.

Enfin, il y a la question des modèles ouverts contre les modèles fermés. Les tests de l'article utilisent principalement GPT-5, mais comment se comportent les modèles ouverts comme Qwen3 ou Llama 4 ? La capacité à suivre des instructions REPL complexes et à écrire du code correct varie considérablement d'un modèle à l'autre. Un RLM n'est efficace que dans la mesure où le modèle racine qui le guide l'est.

L'approche de Zhang et de ses collègues ne résout pas comme par magie le problème de la pourriture du contexte, mais le transforme d'une limite architecturale en un défi de conception de système. Et peut-être, tout comme ce fut le cas avec les systèmes d'exploitation qui ont introduit la mémoire virtuelle pour surmonter les limites de la RAM physique, les Modèles de Langage Récursifs représentent un changement de paradigme : non plus des modèles qui *ont* de la mémoire, mais des modèles qui *gèrent* la mémoire.

Il est trop tôt pour dire s'ils deviendront la norme de facto, mais une chose est sûre : le débat sur la manière de faire raisonner l'IA sur des contextes arbitrairement longs ne fait que commencer, et les prochaines générations de modèles devront sérieusement se confronter à cette direction de recherche.
