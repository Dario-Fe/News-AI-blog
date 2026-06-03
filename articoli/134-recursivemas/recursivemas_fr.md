---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-06-03
author: "Dario Ferrero"
---

# RecursiveMAS a aboli les tokens, les agents parlent dans leur propre langue 
![recursivemas.jpg](recursivemas.jpg)

*Un article publié le 28 avril 2026 par des chercheurs de l'UIUC, Stanford, NVIDIA et le MIT propose un changement architectural radical : des agents IA qui collaborent sans plus échanger de texte, en communiquant directement en latent space. Les chiffres sont convaincants. Les questions ouvertes, encore plus. Découvrons RecursiveMAS, le framework qui transforme les agents en un 'cerveau collectif récursif'*.

Imaginez une équipe de spécialistes qui doit résoudre un cas complexe : un cardiologue, un neurologue, un anesthésiste. Chaque fois que l'un d'eux a une intuition, cependant, il ne peut pas simplement la transmettre à son collègue ; il doit d'abord la traduire dans un e-mail formel, l'envoyer, attendre que l'autre le lise, l'interprète, formule une réponse, l'écrive et la renvoie. Et ainsi de suite, à chaque échange. La pensée ralentit, les coûts augmentent, quelque chose se perd dans la traduction.

C'est, avec une approximation utile, le problème fondamental des systèmes multi-agents basés sur le langage. Chaque agent IA reçoit un input sous forme textuelle, le traite, produit un output textuel, qui est transmis à l'agent suivant comme nouvel input. Chaque étape nécessite un décodage du vocabulaire (une opération coûteuse en calcul), de la latence et des tokens, c'est-à-dire de l'argent. Si l'on ajoute la récursion, c'est-à-dire le fait que le système doive effectuer plusieurs cycles de collaboration pour affiner la réponse, le problème se multiplie : à chaque round, chaque agent doit tout décoder de nouveau.

[RecursiveMAS](https://arxiv.org/abs/2604.25917), le framework présenté le 28 avril 2026 par une équipe de douze chercheurs répartis entre l'UIUC, Stanford, NVIDIA et le MIT, part d'une question apparemment simple : et si les agents arrêtaient de se parler en texte ?

## La récursion comme principe de système

Pour comprendre la portée de la proposition, un retour en arrière est nécessaire. Ces dernières années, la récursion, c'est-à-dire l'idée de faire "tourner en boucle" les mêmes traitements sur des états internes du modèle pour approfondir le raisonnement, s'est imposée comme l'un des nouveaux axes de scaling pour les grands modèles linguistiques. Au lieu d'entraîner des modèles de plus en plus grands, on peut prendre un modèle de taille raisonnable et le faire itérer plusieurs fois sur le même problème, en affinant progressivement ses représentations internes. Cette approche, appelée dans la littérature *recursive language model* (RLM), a montré des résultats prometteurs dans la recherche ces deux dernières années.

Le saut conceptuel de RecursiveMAS consiste à étendre ce principe de l'intérieur d'un seul modèle à l'ensemble du système multi-agent. Non plus une récursion à l'intérieur d'un agent, mais une récursion du système en tant qu'unité. Toute la collaboration entre agents devient une boucle récursive unique, dans laquelle les informations circulent continuellement, sous forme de latent states, et non de texte, d'un agent à l'autre, et le cercle se referme : le dernier agent transmet son état interne au premier, qui peut ainsi recommencer le traitement avec les informations accumulées lors du round précédent.

Le résultat est ce que l'article décrit comme un *cerveau collectif récursif* : chaque agent agit comme une couche d'un modèle récursif, et l'ensemble du système converge itérativement vers une réponse sans jamais, sauf lors du dernier round, produire de texte intermédiaire.

## RecursiveLink : l'interprète léger

Le problème technique le plus délicat est celui de la traduction entre les mondes. Dans un système multi-agent hétérogène, où chaque agent est un modèle différent, avec une architecture différente, des dimensions différentes de l'espace caché (*hidden size*), comment transfère-t-on un latent state d'un modèle à l'autre sans le convertir en texte ?

La réponse proposée par RecursiveMAS est le module [RecursiveLink](https://recursivemas.github.io/) : un composant léger à deux couches résiduelles qui sert d'interprète entre les latent spaces des différents modèles. Dans sa variante interne (*inner link*), il opère à l'intérieur de chaque agent individuel lors de la génération : au lieu de projeter l'état caché sur le vocabulaire pour produire un token, il le transforme et le réinjecte comme input pour l'étape suivante, maintenant le raisonnement entièrement dans l'espace continu. Dans la variante externe (*outer link*), il ajoute une couche linéaire supplémentaire pour projeter le latent state d'un agent dans l'espace dimensionnel de l'agent suivant, permettant le transfert même entre des modèles aux géométries internes incompatibles.

Le choix de la connexion résiduelle n'est pas esthétique : maintenir la composante originale du latent state signifie que le module n'a pas à apprendre toute la projection de zéro, mais seulement la *différence*, l'écart entre l'espace source et l'espace de destination. Cela rend l'entraînement plus stable et plus efficace.

Le plus surprenant, cependant, est la taille du composant entraîné. Alors que les paramètres de base de tous les agents restent complètement gelés, le RecursiveLink n'introduit que 13 millions de paramètres entraînables sur l'ensemble du système, soit 0,31 % du total des paramètres. Pour donner une idée de la proportion : c'est comme optimiser un orchestre symphonique en agissant exclusivement sur le système d'amplification entre les pupitres, sans toucher à aucun instrument.
![grafico1.jpg](grafico1.jpg)
[Image tirée d'arxiv.org](https://arxiv.org/html/2604.25917v1)

## Inner loop, outer loop : entraîner un système entier

L'autre innovation structurelle du framework concerne la méthode d'entraînement. Optimiser un système multi-agent récursif de manière cohérente n'est pas trivial : si l'on entraîne les modèles séparément, chacun apprend à bien se comporter de manière isolée, mais pas nécessairement à collaborer. Si, en revanche, on essaie de les optimiser tous ensemble dès le début, la complexité explose et les gradients ont tendance à s'évanouir à travers les rounds récursifs.

RecursiveMAS propose un algorithme en deux phases appelé *inner-outer loop learning*. Dans la première phase, l'inner loop entraîne en parallèle et de manière indépendante l'*inner link* de chaque agent, en utilisant comme objectif la cosine similarity entre les pensées latentes produites et la distribution des tokens corrects dans la couche d'embedding. Il s'agit d'un warm-start : on apprend à chaque agent à penser en latent space sans encore se soucier de la manière dont il interagira avec les autres.

Dans la deuxième phase, l'outer loop optimise l'ensemble du système en tant qu'unité. Le framework est déployé pendant *n* rounds récursifs, et ce n'est qu'à la fin du dernier round qu'une réponse textuelle est produite pour calculer la perte (loss). Le gradient est ensuite rétropropagé à travers toute la chaîne récursive, attribuant à chaque outer link un signal de crédit partagé basé sur sa contribution à la prédiction finale. Chaque link apprend donc non seulement de sa propre erreur locale, mais de la qualité globale de l'ensemble du système sur chaque exemple individuel.

Le théorème central de l'article (Théorème 4.1) démontre formellement pourquoi cette approche fonctionne mieux que celle basée sur le texte : les gradients qui transitent par les RecursiveLink résiduels restent stables au fil des rounds, alors que dans le cas du texte, où la projection sur le vocabulaire introduit une discontinuité, ils ont tendance à s'effondrer vers zéro avec l'augmentation de la profondeur récursive. Un gradient qui s'évanouit signifie un système qui cesse d'apprendre.

## Les chiffres : neuf benchmarks, quatre patterns

RecursiveMAS a été testé sur neuf benchmarks couvrant les mathématiques (MATH500, AIME 2025, AIME 2026), les sciences et la médecine (GPQA-Diamond, MedQA), la génération de code (LiveCodeBench, MBPP+) et la recherche sur le web (HotpotQA, Bamboogle). Les modèles impliqués incluent Qwen3/3.5, LLaMA-3, Gemma3 et Mistral, dans des configurations allant de moins de 1,5 milliard à environ 10 milliards de paramètres par agent.

Les résultats par rapport à toutes les baselines — agent unique avec LoRA, agent unique avec full fine-tuning, Mixture-of-Agents, TextGrad, LoopLM, Recursive-TextMAS — montrent une amélioration moyenne de 8,3 points de pourcentage de précision. Le gain le plus marqué est enregistré sur les benchmarks de raisonnement mathématique dense : sur AIME 2025, la version *scaled* de RecursiveMAS atteint 86,7 % contre 73,3 % pour la meilleure baseline comparable. Point important, l'avantage croît avec la profondeur récursive : à *r* = 1 (un seul round), l'amélioration moyenne est de 3,4 points ; à *r* = 3, elle monte à 7,2. Les systèmes textuels, en comparaison, ont tendance à se dégrader ou à se stabiliser avec une récursion plus profonde, signe qu'ils accumulent des erreurs à chaque round, au lieu de s'affiner.

Sur le front de l'efficacité, les données sont encore plus nettes. Par rapport à un système multi-agent récursif équivalent mais basé sur le texte, RecursiveMAS offre un speedup de 1,2× à *r* = 1 jusqu'à 2,4× à *r* = 3, avec une réduction des tokens consommés allant de 34,6 % à 75,6 %. Le coût d'entraînement estimé est de 4,27 dollars contre 9,67 pour le fine-tuning complet, avec moins de mémoire GPU : 15,29 Go en pic contre les 41,40 requis par le full SFT.

Le framework a été testé sur quatre patterns de collaboration distincts : *Sequential* (Planner, Critic, Solver en séquence), *Mixture* (spécialistes en parallèle agrégés par un Summarizer), *Distillation* (un agent expert plus grand qui instruit un agent apprenti plus petit) et *Deliberation* (un Reflector interne couplé à un Tool-Caller qui accède à Python et aux API de recherche). Dans les quatre contextes, RecursiveMAS surpasse l'agent unique le plus fort de la configuration correspondante.

## Quand les agents cessent de parler

Voilà pour les chiffres. Mais il y a une question que les chiffres ne résolvent pas, et qui concerne quelque chose de plus dérangeant : si les agents ne se parlent plus en langage naturel, comment un être humain peut-il comprendre ce qui se passe ?

Dans les systèmes multi-agents traditionnels, chaque échange textuel entre agents est en principe lisible. Un ingénieur peut ouvrir le log, parcourir la conversation entre le Planner et le Solver, comprendre où le raisonnement a pris une mauvaise direction, intervenir. La trace textuelle est une forme de transparence implicite : le système pense à haute voix, et cette voix est compréhensible.

Dans RecursiveMAS, les rounds intermédiaires ne produisent pas de texte. Les pensées latentes, des représentations vectorielles de haute dimension qui transitent entre les modèles via les RecursiveLink, n'ont pas de traduction naturelle en langage humain. L'article inclut des analyses des distributions sémantiques dans l'espace latente au fil des rounds, montrant que la cohérence sémantique est maintenue et que les concepts pertinents se cristallisent progressivement, mais il s'agit d'une assurance technique, pas d'une fenêtre accessible sur la cognition du système.

La véritable contribution de RecursiveMAS, comme l'observe une analyse sur Towards AI, est l'extension du style COCONUT — pensée continue en latent space — à travers les agents via l'adaptateur RecursiveLink. Mais COCONUT, présenté par Meta en 2024, avait déjà soulevé cette préoccupation dans le contexte d'un modèle unique : lorsqu'un système raisonne sans émettre de texte intermédiaire, les mécanismes standards d'interprétabilité, d'analyse de l'attention, de probing des couches, de steering vectoriel, deviennent beaucoup plus difficiles à appliquer à l'ensemble du flux computationnel.

La communauté de recherche sur l'interprétabilité mécaniste, qui a fait des progrès notables ces dernières années dans la compréhension de la manière dont les transformers individuels traitent l'information, est confrontée à une nouvelle frontière : des systèmes où les unités d'analyse ne sont plus les couches d'un seul modèle, mais les passages latents entre des modèles hétérogènes. L'article de RecursiveMAS n'aborde pas ce point de manière explicite, une lacune qui mérite d'être signalée.

Il ne s'agit pas d'alarmisme. La plupart des applications pratiques de ces systèmes — génération de code, réponse aux questions, raisonnement mathématique — ne nécessitent pas de transparence en temps réel sur les rounds intermédiaires. Le point est plus subtil : dans des scénarios de déploiement à haut risque, ou lorsqu'un système produit un résultat inattendu et qu'il faut comprendre pourquoi, l'absence de trace textuelle intermédiaire rend le débogage structurellement plus difficile. Le coût de la vitesse est, en partie, payé en compréhensibilité.
![grafico2.jpg](grafico2.jpg)
[Image tirée d'arxiv.org](https://arxiv.org/html/2604.25917v1)

## Limites, lacunes et honnêteté intellectuelle

L'article ne consacre pas de section explicite à ses propres limites, un choix éditorial courant dans la recherche académique, mais qu'il convient de compenser par une analyse externe.

Le premier point est la nature des benchmarks. Les neuf tests utilisés sont des ensembles de données standardisés, construits autour de problèmes avec une réponse vérifiable et unique : équations, choix multiples en médecine, problèmes de compétition mathématique, génération de code évaluée par des tests automatiques. Ce sont les benchmarks sur lesquels la communauté mesure les progrès, et ils sont logiques en tant que comparaison comparative. Mais ils ne disent rien sur la manière dont RecursiveMAS se comporterait dans des tâches ouvertes, la rédaction de documents longs, l'analyse de textes ambigus ou la planification multi-étapes avec feedback humain, où la qualité de la réponse n'est pas binaire et où le processus compte autant que le résultat.

Le deuxième point concerne les outils externes. Le pattern *Deliberation* inclut l'utilisation de Python et d'API de recherche, et il est encourageant que le framework tienne le coup également dans ce contexte. Mais l'intégration avec des outils externes est restée volontairement simple : deux types d'outils, dans une configuration contrôlée. Les systèmes agentiques réels en production gèrent des dizaines d'outils hétérogènes, avec des latences variables, des erreurs de réseau et des outputs non structurés. Comment se comporte RecursiveLink lorsque la chaîne latente est interrompue par un appel API qui prend trois secondes ? Cette question n'a pas encore de réponse.

Le troisième point est la scalabilité. Les tests présentés impliquent au maximum quatre agents. Les architectures multi-agents en production peuvent facilement atteindre des dizaines d'agents spécialisés. La complexité théorique du système croît linéairement avec le nombre d'agents *N*, mais la gestion pratique des RecursiveLink entre des familles de modèles de plus en plus diverses, avec des hidden sizes différentes, des tokenizers différents et des spécialisations différentes, est un problème d'ingénierie non trivial sur lequel l'article ne se prononce pas.

Il y a enfin la question de la reproductibilité. Au moment de la publication, le [répertoire GitHub officiel](https://github.com/RecursiveMAS/RecursiveMAS) comprend le code pour l'inférence et la démo, mais signale comme étant toujours en cours la publication du pipeline complet de training et des données d'entraînement. Vérifier de manière indépendante les résultats rapportés, une pratique essentielle dans la communauté scientifique, nécessite donc d'attendre que ces ressources soient publiées.

## Un tournant, pas un point d'arrivée

RecursiveMAS est la première démonstration que la récursion peut fonctionner comme principe architectural au niveau du système, déplaçant la conversation de "comment optimisons-nous chaque agent individuel ?" à "comment faisons-nous évoluer le système en tant qu'entité unifiée ?". Les chiffres — +8,3 % de précision moyenne, vitesse jusqu'à 2,4 fois supérieure, trois quarts de tokens économisés, coût d'entraînement divisé par deux — sont obtenus dans des conditions contrôlées et doivent être lus avec cette prudence, mais ils ne peuvent être ignorés.

Les questions les plus difficiles restent ouvertes : quel est le degré de scalabilité avec des dizaines d'agents ? Comment se comporte-t-il sur des tâches réelles et ambiguës ? Comment l'intelligibilité est-elle maintenue lorsque les rounds intermédiaires deviennent invisibles ? Quiconque construit des systèmes IA pour des environnements critiques a tout intérêt à ne pas les écarter comme des détails d'implémentation.

Une chose semble claire : l'avenir des agents IA ne sera pas une chaîne linéaire de prompts et de réponses. Ce sera une boucle. La question est de savoir qui décidera de la manière dont cette boucle est conçue, et avec quelles garanties de transparence sur ce qui se passe à l'intérieur.
