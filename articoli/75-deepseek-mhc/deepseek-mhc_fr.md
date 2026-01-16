---
tags: ["Research", "Training", "Ethics & Society"]
date: 2026-01-16
author: "Dario Ferrero"
---

# Comment DeepSeek a transformé les contraintes matérielles en innovation mathématique
![deepseek-mhc.jpg](deepseek-mhc.jpg)

*Le 1er janvier 2026, alors que le monde célébrait le début de la nouvelle année, les chercheurs de DeepSeek publiaient sur arXiv un article qui pourrait changer la façon dont nous entraînons les grands modèles de langage. Il ne s'agissait pas d'un meilleur modèle ou d'un plus grand jeu de données, mais de quelque chose de plus subtil et potentiellement plus perturbateur : une [réflexion radicale sur l'architecture fondamentale](https://arxiv.org/pdf/2512.24880) qui sous-tend l'intelligence artificielle moderne.*

L'article, co-signé par le fondateur et PDG de DeepSeek, Liang Wenfeng, ainsi que par 18 autres chercheurs dirigés par [Zhenda Xie, Yixuan Wei et Huanqi Cao](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less), propose les Manifold-Constrained Hyper-Connections, ou mHC en abrégé. Pour comprendre de quoi il s'agit, nous devons cependant d'abord prendre du recul et revenir sur une histoire qui commence en 2015.

## Quand la limite devient un levier

Pendant des années, l'un des problèmes les plus frustrants de l'apprentissage profond a été la "disparition du gradient" : lors de la construction de réseaux de neurones très profonds, avec des dizaines ou des centaines de couches superposées, l'information avait tendance à se disperser ou, au contraire, à exploser en valeurs incontrôlables pendant l'entraînement. C'était comme essayer de chuchoter un message à travers une chaîne humaine de cent personnes : à la fin, le message original était méconnaissable.

En 2015, une équipe de Microsoft Research Asia dirigée par Kaiming He a résolu le problème avec une solution d'une simplicité élégante : les connexions résiduelles, ou ResNet. L'idée était de permettre à l'information de "sauter" certaines couches par des raccourcis directs, en conservant le signal original intact pendant que le réseau le traitait en parallèle. Une sorte de double voie : une pour le traitement, une pour la mémoire. Cette approche est devenue [l'article le plus cité du XXIe siècle](https://tech.yahoo.com/ai/articles/deepseek-proposes-shift-ai-model-093000518.html) dans le domaine de l'intelligence artificielle, selon Nature.

La méthode a si bien fonctionné que pratiquement tous les modèles modernes, de GPT à Claude, de Llama à Gemini, l'ont adoptée sans modifications substantielles pendant près d'une décennie. Mais avec l'augmentation de l'échelle des modèles, passant de milliards à des centaines de milliards de paramètres, cette seule autoroute résiduelle a commencé à montrer ses limites. C'est là que ByteDance entre en scène.

En septembre 2024, les chercheurs de la société mère de TikTok [ont publié un article sur les Hyper-Connexions](https://arxiv.org/abs/2409.19606), accepté à la prestigieuse conférence ICLR 2025. L'idée était aussi simple qu'ambitieuse : au lieu d'une seule autoroute résiduelle, pourquoi ne pas en construire quatre, huit, seize ? Au lieu d'un seul canal, créer plusieurs flux d'informations qui pourraient se mélanger et se recombiner dynamiquement à travers les couches du réseau.

Les résultats, testés sur les modèles OLMo et OLMoE, ont été impressionnants : une convergence 1,8 fois plus rapide et une amélioration d'environ 6 points sur le benchmark ARC-Challenge. Les réseaux avec Hyper-Connexions ont montré une bien plus grande diversité de représentation entre les couches, évitant l'"effondrement de la représentation" qui affectait les architectures traditionnelles.

Mais il y avait un problème. Un problème sérieux.

## L'astuce du polytope

Les Hyper-Connexions introduisaient des instabilités catastrophiques pendant l'entraînement. Les matrices de mélange qui contrôlaient les multiples flux avaient tendance à s'amplifier de couche en couche. C'était un effet domino mathématique : si chaque couche amplifiait le signal ne serait-ce que de 5 % par rapport à la précédente, après 60 couches, cette apparente bagatelle se traduisait par une amplification de 18 fois l'intensité originale. Dans l'article de DeepSeek, les chercheurs ont mesuré des [facteurs d'amplification allant jusqu'à 3000 fois](https://medium.com/@kamathuday/deepseek-r1-researchers-just-proposed-a-fundamental-fix-to-how-transformers-connect-their-layers-ddc78064d41b) dans certaines configurations. À ce stade, l'entraînement ne ralentissait pas seulement : il s'effondrait complètement.

La réponse typique de l'industrie consiste en des solutions palliatives : écrêtage du gradient, initialisations prudentes, planificateurs de taux d'apprentissage complexes. Des astuces qui fonctionnent, mais qui ne s'adaptent pas bien à l'échelle. DeepSeek a choisi une voie différente : revenir aux principes fondamentaux des mathématiques.

La question que se sont posée les chercheurs était la suivante : existe-t-il une contrainte mathématique qui puisse garantir la stabilité sans sacrifier l'expressivité des Hyper-Connexions ? La réponse était cachée dans un article de 1946 de Richard Sinkhorn, affiné plus tard avec Paul Knopp en 1967 : l'algorithme de Sinkhorn-Knopp. Cette procédure itérative convertit n'importe quelle matrice non négative en une matrice "doublement stochastique", où chaque ligne et chaque colonne somme à 1.

Pensez à quatre verres d'eau. Vous pouvez verser l'eau d'un verre à l'autre comme vous le souhaitez, mais avec une règle stricte : la quantité totale d'eau doit rester constante, et chaque verre doit à la fois donner et recevoir du liquide. L'eau peut être redistribuée, mais elle ne peut être ni créée ni détruite. C'est exactement ce que fait l'algorithme de Sinkhorn-Knopp appliqué aux Hyper-Connexions.

En langage technique, DeepSeek projette les matrices de connexion sur le "polytope de Birkhoff", un objet géométrique qui vit dans un espace de grande dimension et qui représente toutes les permutations pondérées possibles de l'information. C'est un peu comme forcer les connexions neuronales à se déplacer sur une surface courbe dans un espace multidimensionnel, au lieu de les laisser errer librement dans toutes les directions. La métaphore n'est pas fortuite : ceux qui ont joué à *Portal* se souviendront comment un mouvement contraint sur des surfaces spécifiques peut ouvrir des possibilités contre-intuitives.

Le résultat est que mHC préserve toute l'expressivité des Hyper-Connexions — les canaux multiples, la recombinaison dynamique et la richesse de la représentation — mais élimine le risque d'instabilité. L'information peut circuler librement par de multiples chemins, mais toujours dans le respect de lois de conservation mathématiques rigoureuses.
![mhc-schema.jpg](mhc-schema.jpg)
[Image de medium.com](https://medium.com/@kamathuday/deepseek-r1-researchers-just-proposed-a-fundamental-fix-to-how-transformers-connect-their-layers-ddc78064d41b)

## Les chiffres qui comptent

DeepSeek a testé mHC sur des modèles de 3, 9 et 27 milliards de paramètres, entraînés sur plus de 1 billion de jetons. Les résultats, [rapportés dans l'article publié sur arXiv](https://arxiv.org/pdf/2512.24880), montrent que l'architecture s'adapte à l'échelle sans ajouter de surcoût de calcul significatif.

Grâce à des optimisations au niveau de l'infrastructure, à la fusion d'opérations, à la réduction du trafic mémoire, au recalcul stratégique de valeurs intermédiaires et au chevauchement de la communication et du calcul, mHC n'introduit qu'un surcoût de 6 à 7 % pendant l'entraînement. Un chiffre négligeable pour les modèles à grande échelle, surtout si l'on considère les gains en stabilité et en performance.

Les chercheurs ont comparé mHC aux Hyper-Connexions traditionnelles sur huit tâches différentes, et les résultats sont clairs : alors que les HC non contraintes montraient une instabilité récurrente, mHC s'entraînait en douceur, obtenant une perte plus faible et de meilleures performances sur les benchmarks de raisonnement et de langage naturel.

Mais il y a un aspect encore plus intéressant. DeepSeek n'a pas développé cette technique dans le vide : l'entreprise opère dans un contexte très spécifique, celui des [restrictions américaines sur l'exportation de puces avancées vers la Chine](https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls).

## Le paradoxe de l'isolement technologique

En octobre 2022, le département américain du Commerce a imposé les premiers contrôles à l'exportation de puces d'IA vers la Chine, interdisant de fait la vente des GPU H100 et A100 de Nvidia. L'objectif déclaré était de ralentir le développement des capacités chinoises en intelligence artificielle et en supercalcul.

Nvidia a rapidement réagi avec des versions "dégradées" spécifiques au marché chinois : d'abord l'A800, puis l'H800, des puces conçues pour rester en dessous des seuils de densité de performance établis par les règles américaines. [Comme le rapporte le Center for Strategic and International Studies](https://www.csis.org/analysis/where-chips-fall-us-export-controls-under-biden-administration-2022-2024), la secrétaire au Commerce Gina Raimondo a vivement critiqué Nvidia pour avoir "contourné les règles commerciales", promettant de contrôler toute nouvelle puce redessinée "dès le lendemain".

En octobre 2023, la deuxième série de restrictions est arrivée, incluant également les H800 et A800. Nvidia a alors introduit la H20, une puce avec seulement 20 % des performances de la H100. Mais le mal, du point de vue chinois, était fait : l'accès aux GPU haut de gamme était bloqué ou fortement limité.

Et c'est là que l'histoire devient paradoxale. Comme le [rapporte Built In](https://builtin.com/articles/trump-lifts-ai-chip-ban-china-nvidia), citant Jay Dawani, PDG de Lemurian Labs : "Les laboratoires chinois tirent le meilleur parti du matériel qu'ils possèdent déjà". DeepSeek est devenu l'exemple le plus frappant de cette approche.

Leur modèle R1, sorti en janvier 2025, a été [entraîné à l'aide de puces H800](https://www.hypotenuse.ai/blog/what-is-deepseek-r1-and-why-is-it-making-waves-in-ai), bien en dessous du seuil des contrôles à l'exportation, pour un coût déclaré de seulement 5,58 millions de dollars pour le modèle de base V3 et de [294 000 dollars pour la phase de raisonnement de R1](https://mlq.ai/news/deepseek-reveals-r1-model-training-cost-just-294000-in-peer-reviewed-nature-publication/), selon une publication dans Nature. Des chiffres qui ont fait chuter la capitalisation boursière de Nvidia de 600 milliards de dollars en une seule journée.

Au lieu de bloquer l'innovation chinoise, les sanctions l'ont canalisée vers l'efficacité algorithmique. Incapables de rivaliser avec la force de calcul brute, les chercheurs chinois ont dû inventer des voies alternatives. Et mHC s'inscrit parfaitement dans ce récit : c'est une technique qui permet d'obtenir plus avec moins, de s'adapter à l'échelle sans simplement ajouter plus de GPU.

Comme l'observe [Florian Brand, doctorant à l'Université de Trèves et expert de l'écosystème de l'IA chinois](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less), les articles de DeepSeek servent souvent de signal précoce de la direction technique de leurs prochains modèles. Le fait que Liang Wenfeng ait personnellement téléchargé l'article sur arXiv, comme il l'a fait pour R1 et V3, suggère que mHC pourrait être au cœur des futurs modèles de l'entreprise.

L'industrie s'attend à ce que DeepSeek sorte un nouveau modèle phare avant le Festival du Printemps à la mi-février, reproduisant le schéma de l'année dernière lorsque R1 a été lancé à la veille de la fête nationale.
![mhc-schema2.jpg](mhc-schema2.jpg)
[Image de arxiv.org](https://arxiv.org/pdf/2512.24880)

## Au-delà de DeepSeek, au-delà du langage

L'une des questions les plus intéressantes concerne l'applicabilité de mHC au-delà des modèles de langage. L'article de DeepSeek inclut des expériences sur des tâches de vision, et le même article original de ByteDance sur les Hyper-Connexions démontrait des améliorations tant dans le langage que dans la vision par ordinateur.

En théorie, toute architecture basée sur des connexions résiduelles pourrait bénéficier de mHC : modèles de vision, systèmes multimodaux, architectures pour la robotique. Le code est déjà disponible sur [GitHub](https://github.com/tokenbender/mHC-manifold-constrained-hyper-connections) et des [implémentations en Python ont été publiées](https://pypi.org/project/hyper-connections/) pour faciliter l'adoption par la communauté.

Mais il y a aussi des voix critiques. [Guo Song, professeur à l'Université des sciences et technologies de Hong Kong](https://sg.news.yahoo.com/deepseek-pitches-route-scale-ai-093000404.html), tout en reconnaissant le potentiel de transformation de mHC, a souligné la complexité de sa mise en œuvre : "L'architecture dépend d'infrastructures de pointe, ce qui pourrait créer une barrière technique rendant difficile son adoption par des laboratoires plus petits ou son déploiement sur des appareils mobiles".

Michael Yeung, un expert en IA cité dans le même article du South China Morning Post, a également souligné qu'il est prématuré d'évaluer les implications tant que l'approche n'aura pas été testée sur un plus large éventail d'architectures. "Il n'y a pas de boule de cristal", a-t-il commenté.

Des alternatives existent. Des approches comme RMT (Residual Matrix Transformer) et MUDDFormer ont tenté de résoudre des problèmes similaires avec des solutions différentes. RMT remplace le flux résiduel par une matrice de mémoire de produit externe pour faciliter le stockage des caractéristiques. MUDDFormer utilise des connexions denses dynamiques multi-voies pour optimiser le flux d'informations entre les couches. Cependant, tous deux, [selon l'article de DeepSeek](https://arxiv.org/pdf/2512.24880), compromettent la propriété de mappage d'identité inhérente aux connexions résiduelles, introduisant de l'instabilité.

## La roue et le cercle

Dans un commentaire rapporté par le [South China Morning Post](https://www.scmp.com/tech/tech-trends/article/3338535/deepseek-proposes-shift-ai-model-development-mhc-architecture-upgrade-resnet), Pierre-Carl Langlais, co-fondateur de la startup française Pleias, a soutenu que la véritable importance de l'article va au-delà de la simple démonstration de l'évolutivité des Hyper-Connexions. C'est une réflexion plus profonde sur la façon dont l'architecture même des modèles, et pas seulement la quantité de données ou de paramètres, peut être le facteur limitant.

Guo Song a utilisé une [métaphore éloquente](https://www.scmp.com/tech/big-tech/article/3338427/deepseek-kicks-2026-paper-signalling-push-train-bigger-models-less) : "La réaction pourrait être comparée à la découverte de la roue. Quand quelqu'un découvre que les roues rondes fonctionnent mieux que les roues carrées, tout le monde est prêt à changer ses roues de carrées à rondes".

Il y a du vrai dans cette observation, même si elle pèche peut-être par optimisme. Il a fallu des années à ResNet pour devenir la norme universelle, et mHC devra prouver non seulement son efficacité théorique, mais aussi sa praticité industrielle à grande échelle. Comme dans les meilleurs épisodes d'*Adventure Time*, où des solutions mathématiques élégantes résolvent des problèmes apparemment insurmontables, ici la théorie doit encore faire face à l'épreuve du déploiement réel.

Mais le message de fond est clair : après une décennie de domination incontestée, l'architecture fondamentale des modèles d'apprentissage profond pourrait être sur le point d'évoluer. Et paradoxalement, cette évolution pourrait avoir été accélérée précisément par les restrictions qui devaient la ralentir.

Les sanctions américaines ont contraint les chercheurs chinois à rechercher l'efficacité là où d'autres recherchaient la force brute. Ils ont transformé une contrainte en une incitation à l'innovation. Et mHC, avec son élégance mathématique et sa promesse d'évolutivité sans coûts prohibitifs, pourrait n'être que le premier exemple de cette nouvelle direction.

Reste à savoir si l'Occident saura répondre avec ses propres innovations architecturales, ou s'il continuera à miser sur la suprématie computationnelle. Une chose est sûre : la prochaine génération de modèles d'IA ne sera pas seulement plus grande. Elle sera aussi construite plus intelligemment.
