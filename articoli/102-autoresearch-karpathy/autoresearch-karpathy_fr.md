---
tags: ["Research", "Training", "Applications"]
date: 2026-03-20
author: "Dario Ferrero"
---

# Le chercheur dort. Autoresearch : comment Andrej Karpathy a appris aux machines à faire de la recherche autonome
![autoresearch-karpathy.jpg](autoresearch-karpathy.jpg)

*Il y a une scène dans les jeux de rôle japonais, Karpathy les connaît bien, où le protagoniste s'arrête de combattre les monstres seul et commence à entraîner d'autres personnages pour qu'ils le fassent à sa place. Le passage change tout : vous n'êtes plus un combattant, vous êtes un entraîneur. Andrej Karpathy a fait quelque chose de similaire avec la recherche sur l'intelligence artificielle.*

Karpathy est une figure qui n'a pas besoin de beaucoup de présentations dans le secteur, mais il vaut la peine de le situer pour ceux qui viennent de l'extérieur. Ancien directeur de l'intelligence artificielle chez Tesla, cofondateur d'OpenAI, aujourd'hui indépendant et prolifique vulgarisateur technique : il est surtout connu pour sa capacité à rendre accessibles des concepts denses et spécialisés. Son cours [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) est une référence pour quiconque veut comprendre les modèles linguistiques sans avoir un doctorat en poche.

Au début du mois de mars 2026, Karpathy a publié sur GitHub un nouveau projet open-source appelé [autoresearch](https://github.com/karpathy/autoresearch). Le dépôt compte déjà plus de 23 000 étoiles et près de trois mille forks, des chiffres qui, dans le monde du développement logiciel, mesurent l'intérêt avec la même précision qu'un sismographe. L'idée de fond est simple à décrire mais difficile à digérer : donner à un agent d'intelligence artificielle un petit mais authentique système d'entraînement de modèles linguistiques, et le laisser expérimenter seul, de nuit, pendant que le chercheur dort.

## Anatomie d'une boucle nocturne

Pour comprendre ce que fait autoresearch, il est utile d'imaginer le travail quotidien d'un chercheur en machine learning. Normalement, cette personne s'assoit devant son ordinateur, formule une hypothèse (« et si j'utilisais une taille de lot plus petite ? »), modifie manuellement le code d'entraînement, lance une expérience qui dure des heures, analyse les résultats et recommence. C'est un processus sériel, lent et limité par les heures de la journée de travail et la capacité de concentration humaine.

Autoresearch brise ce cycle de manière radicale. Le système est construit autour de seulement trois fichiers qui comptent vraiment : `prepare.py` (qui gère la préparation des données et n'est jamais modifié), `train.py` (le code du modèle, auquel l'agent peut toucher dans chaque partie), et `program.md` (les instructions pour l'agent, écrites en langage naturel). L'utilisateur humain ne touche pas aux fichiers Python : sa tâche est d'écrire et d'affiner le fichier Markdown, c'est-à-dire de *programmer le programme* plutôt que de programmer directement.

Une fois lancé, l'agent — dans la configuration standard, il s'agit de Claude d'Anthropic ou de Codex d'OpenAI — lit les instructions, propose une modification au code d'entraînement, exécute une expérience d'une durée fixe de cinq minutes exactement, mesure si le résultat s'est amélioré, garde ou rejette la modification, et répète. Douze expériences par heure, environ cent au cours d'une nuit. Le matin, le chercheur se réveille devant un journal détaillé de tout ce qui a été tenté et (espérons-le) un meilleur modèle.

La métrique utilisée pour mesurer les progrès s'appelle `val_bpb`, soit *validation bits per byte* : elle mesure à quel point le modèle réussit à compresser le texte, en termes de nombre de bits nécessaires pour représenter chaque octet de données. C'est une métrique élégante car elle est indépendante de la taille du vocabulaire, ce qui signifie que les expériences avec des architectures différentes restent comparables entre elles. Des valeurs plus basses indiquent un modèle plus performant.

L'ensemble de la base de code s'étend sur environ 630 lignes de Python. Ce n'est pas une caractéristique accessoire : c'est un choix philosophique. Karpathy a délibérément construit un système qu'un seul développeur peut lire, comprendre et garder sous contrôle. La révision humaine reste possible. Les diffs, les différences entre une version du code et la suivante, sont lisibles.

Pour comprendre autoresearch en profondeur, il faut connaître le projet dont il est né : [nanochat](https://github.com/karpathy/nanochat), que Karpathy décrit simplement comme « le meilleur ChatGPT que cent dollars puissent acheter ». Ce n'est pas une hyperbole marketing : nanochat est un système complet et minimal pour entraîner des modèles linguistiques sur un seul GPU, couvrant toute la chaîne, de la tokenisation au pré-entraînement, du fine-tuning jusqu'à une interface de chat fonctionnelle.

Son point de fierté est un classement public qui mesure le temps nécessaire pour reproduire les capacités du GPT-2 original (qui en 2019 a coûté environ 43 000 dollars et des semaines de calcul) sur du matériel accessible : pour l'instant, le record est descendu à un peu plus de trois heures sur un nœud avec huit GPU H100, pour une dépense d'environ soixante-dix dollars.

Autoresearch est, par essence, la version mono-GPU et centrée sur l'agent de nanochat : il utilise la même base de code simplifiée comme champ d'expérimentation, avec la même métrique val_bpb comme boussole, mais confie à l'agent la tâche d'explorer ce territoire seul.

Comprendre nanochat signifie comprendre sur quoi l'agent travaille réellement, et pourquoi les résultats obtenus en cinq minutes d'entraînement autonome peuvent être comparés, avec une certaine prudence, à ceux des sessions les plus exigeantes du classement principal.

## Ce que disent vraiment les chiffres

La manière la plus honnête d'évaluer autoresearch n'est pas de regarder la description du projet, mais les données réelles des expériences. Karpathy a publié dans la [discussion #43](https://github.com/karpathy/autoresearch/discussions/43) du dépôt un compte rendu détaillé d'une session complète, remarquablement transparent : 126 expériences réalisées sur un GPU NVIDIA H100 sur une période d'environ dix heures et demie.

Le point de départ était un `val_bpb` de 0,9979. Le point d'arrivée : 0,9697. Une amélioration de 0,0282 en termes absolus, ce qui, dans ce contexte, représente un bond significatif. Pour s'orienter : les modifications les plus marquantes ont été la réduction de la taille du lot (de 524 000 à 262 000 tokens, ce qui a permis d'effectuer plus d'étapes de mise à jour dans les cinq minutes disponibles, gagnant une amélioration de 0,0119), l'ajout d'une couche à la profondeur du modèle (0,0043), et une série d'ajustements plus fins comme l'introduction de petites valeurs de régularisation (*weight decay*) sur les composants d'embedding.

Ce qui frappe en lisant le journal complet, ce n'est pas seulement le résultat final, mais la granularité du processus. L'agent a systématiquement exploré des dizaines d'hypothèses, dont beaucoup se sont révélées être des impasses : le *weight tying* entre embedding et de-embedding a produit une chute catastrophique de la métrique ; l'attention multi-query avec une seule tête de clé-valeur s'est avérée trop agressive ; les architectures avec plus de couches mais des dimensions réduites finissaient par épuiser le budget de cinq minutes avant même de converger. Ces échecs documentés sont presque plus utiles que les succès, car ils dessinent la carte du territoire exploré.

Les résultats obtenus sur un GPU H100, la carte graphique la plus performante actuellement disponible pour ce type de charges, se sont ensuite révélés transférables à des modèles plus profonds de 24 couches, suffisamment pour rivaliser dans les classements de référence du secteur. Ce n'est pas un résultat banal. Mais la limite de la transférabilité est encore floue, et c'est l'une des limites du projet sur laquelle il vaut la peine de s'attarder.
![grafico1.jpg](grafico1.jpg)
[Image tirée de github.com](https://github.com/karpathy/autoresearch)

## Le revers de la médaille

Autoresearch a reçu un accueil enthousiaste, et l'enthousiasme est compréhensible. Mais une analyse honnête nécessite de regarder aussi là où le système montre ses fissures.

La première limite est structurelle : le budget fixe de cinq minutes par expérience, qui est aussi l'un des points forts du projet, devient une contrainte rigide lorsque l'on explore des architectures plus complexes. Dans les données de la session #43, on voit clairement : chaque tentative d'ajouter des couches au-delà d'un certain seuil se soldait par une expérience incomplète, car le temps s'écoulait avant que le modèle ne converge. L'agent cherchait dans un espace de possibilités partiellement bloqué par sa propre architecture temporelle.

La deuxième limite concerne le parallélisme. Le système est conçu pour un seul GPU, et les expériences sont exécutées en séquence, pas en parallèle. Cela signifie que pendant qu'une expérience tourne, aucune autre ne peut être lancée. Ceux qui auraient accès à un cluster de GPU pourraient vouloir explorer plusieurs directions simultanément ; autoresearch, par choix délibéré, ne le supporte pas. Karpathy est transparent à ce sujet : c'est une décision de conception, pas un oubli. Mais la conséquence pratique est que l'exploration de l'espace de recherche reste fondamentalement linéaire.

Troisième point critique : la dépendance vis-à-vis de modèles propriétaires. Pour exécuter les expériences en mode autonome, un agent capable est nécessaire, et dans la configuration standard, on parle de Claude ou Codex, tous deux des systèmes commerciaux. Ceux qui veulent démocratiser la recherche sur l'intelligence artificielle pourraient trouver paradoxal qu'un outil conçu pour abaisser les barrières à l'entrée nécessite tout de même un abonnement à des services tiers.

Il y a aussi un aspect plus subtil, qui concerne la nature même des choix que l'agent effectue. autoresearch est excellent pour l'optimisation locale : il trouve le meilleur point au voisinage du point de départ, à travers une séquence de petites étapes. Mais ce n'est pas un système conçu pour faire des bonds conceptuels. La revue de la littérature, la formulation d'hypothèses radicalement nouvelles, la compréhension du pourquoi une approche fonctionne au niveau théorique, tout cela reste le territoire humain, du moins pour l'instant. La vraie recherche, celle qui change les paradigmes, n'est pas seulement un processus d'optimisation sériel.

Enfin, il y a la question de l'explicabilité. Lorsque l'agent découvre qu'une initialisation des poids réduite à 0,68x de la valeur standard produit de meilleurs résultats, il ne fournit pas d'explication causale de cette amélioration. Il sait que cela fonctionne, pas pourquoi cela fonctionne. Pour ceux qui utilisent les résultats comme point de départ pour des recherches ultérieures, ce manque de compréhension est une dette technique qui devra tôt ou tard être remboursée.

## L'humain qui programme le programme

L'une des idées les plus intéressantes, et les moins discutées, d'autoresearch est le rôle qu'il assigne à l'être humain dans le processus. Il ne s'agit pas de l'éliminer, mais de le déplacer.

Le fichier `program.md` est décrit dans le README comme une « skill » ultra-légère : un document en langage naturel qui définit les objectifs de l'agent, ses priorités, les contraintes dans lesquelles opérer. L'utilisateur n'écrit plus de Python, il écrit des instructions. Il ne modifie pas le code d'entraînement, il modifie le document qui dit à l'agent comment modifier le code d'entraînement. C'est un niveau d'abstraction supplémentaire, qui apporte des conséquences concrètes.

D'un côté, cela abaisse énormément le seuil d'entrée. Nul besoin d'un doctorat en machine learning pour lancer une session d'autoresearch. Le README inclut un « Weekend Guide », un guide pour le week-end, qui promet d'amener quiconque de la configuration initiale aux premières expériences autonomes sans bagage spécialisé. La simplicité technique de l'installation (un seul GPU NVIDIA, Python 3.10 ou supérieur, et le gestionnaire de paquets `uv`) est réelle.

D'un autre côté, cette abstraction crée une nouvelle dépendance. Celui qui écrit les instructions dans `program.md` détermine l'espace d'exploration de l'agent. Un document mal écrit, avec des objectifs vagues ou des contraintes contradictoires, produit des sessions de recherche tout aussi vagues. Le goulot d'étranglement se déplace : au lieu de nécessiter des compétences en écriture de code, autoresearch nécessite des compétences en écriture d'instructions efficaces pour les systèmes d'intelligence artificielle, une discipline relativement nouvelle, encore dépourvue de normes consolidées.

Il y a quelque chose de récursif dans tout cela, et Karpathy en est conscient. Dans le README du projet, il a inséré une épigraphe délibérément ambiguë, décrivant un futur hypothétique où des essaims d'agents autonomes gèrent des clusters de calcul dans une recherche continuellement auto-modifiante, avec une base de code à la dix-mille-douzième génération « ayant grandi au-delà de la compréhension humaine ». C'est un ton entre le dystopique et la blague de geek, mais le fait que cette phrase ouvre le document de présentation d'un projet réel n'est pas fortuit.

## Où mène ce chemin

La comparaison la plus immédiate pour autoresearch est celle avec AutoML, les systèmes qui, ces dernières années, ont tenté d'automatiser le choix des architectures neuronales et des hyperparamètres. Mais il y a une différence substantielle : l'AutoML traditionnel opère sur des espaces de recherche prédéfinis, cherchant la combinaison optimale parmi des options déjà énumérées. autoresearch laisse l'agent modifier librement n'importe quelle partie du code, y compris l'architecture, l'optimiseur, la taille du lot, le schéma d'apprentissage, pratiquement tout. L'espace d'exploration est beaucoup plus vaste et beaucoup moins structuré.

Cela ouvre des possibilités intéressantes, mais aussi des questions inconfortables. Si le système fonctionne réellement, si des agents autonomes peuvent effectuer une recherche significative sur des modèles linguistiques sans supervision continue, où s'arrête ce processus ? La réponse honnête est que personne ne le sait avec certitude. Le projet est explicitement conçu pour être le point de départ de quelque chose de plus grand, et Karpathy lui-même indique la direction vers des configurations multi-agents asynchrones, où plusieurs instances parallèles explorent des directions différentes sur des clusters distribués.

D'un point de vue éthique, ce scénario mérite attention. L'accélération des cycles de recherche est souhaitable si elle mène à des modèles meilleurs et plus sûrs. Mais la même accélération, appliquée sans supervision adéquate, peut amplifier des biais algorithmiques déjà présents dans les données d'entraînement, produire des optimisations qui maximisent des métriques mesurables au détriment de qualités non mesurables, ou rendre le processus suffisamment opaque pour échapper à toute forme de contrôle significatif.

Le fait qu'autoresearch soit open-source et minimaliste est, en ce sens, une garantie partielle. Le code est assez court pour être audité, les données des expériences sont publiques. Mais au fur et à mesure que le système s'étend vers des clusters multi-GPU, vers des sessions plus longues, vers des agents qui affinent leurs propres instructions, la supervision devient plus difficile.

Il y a enfin une considération pragmatique qui concerne ceux qui évaluent cet outil pour un usage professionnel. autoresearch dans sa forme actuelle est un prototype raffiné, pas un système de production. Il nécessite un matériel spécifique (GPU NVIDIA, avec un support optimal pour H100), dépend d'API externes pour l'agent, et produit des résultats qui doivent être interprétés avec compétence pour être utiles. La promesse du « guide du week-end » est réelle pour ceux qui veulent expérimenter, mais elle ne remplace pas la compréhension de base du fonctionnement de l'entraînement des modèles linguistiques.

Cela dit, la valeur d'autoresearch ne se mesure pas seulement à ce qu'il fait aujourd'hui, mais à ce qu'il démontre être possible. Il montre que la recherche automatisée sur des systèmes réels — pas des simulations simplifiées, pas des benchmarks artificiels — est déjà à la portée de quiconque possède un seul GPU et la curiosité d'explorer. Et il le fait avec une transparence méthodologique — celle des journaux publics et du code lisible — que beaucoup de laboratoires de recherche bien financés ne s'autorisent pas.

Le chercheur qui dort s'est, entre-temps, déjà réveillé. Il a trouvé 126 expériences qui attendent d'être lues.
