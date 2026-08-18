---
tags: ["Research", "Generative AI", "Ethics & Society"]
date: 2026-09-30
author: "Dario Ferrero"
---

# Vincenzo Fornaro et Colibrì : "Le génie ne m'intéresse pas, c'est la curiosité qui m'intéresse"
![intervista-fornaro-colibri.jpg](intervista-fornaro-colibri.jpg)

*J'ai déjà parlé de Colibrì, en expliquant comment il est possible de faire tourner un modèle Mixture-of-Experts de 744 milliards de paramètres sur un ordinateur ne disposant que de 25 Go de RAM, en traitant le disque comme un niveau de mémoire intelligent plutôt que comme un simple conteneur ([vous pouvez lire l'analyse technique complète ici](https://aitalk.it/it/colibri.html)). Ce qui manquait, c'était la voix de celui qui a écrit ce moteur, fichier C par fichier C, seul, sans laboratoire et sans cluster derrière lui. J'ai discuté avec Vincenzo Fornaro pour qu'il me raconte le parcours qui se cache derrière le code, et la conversation est devenue plus longue et stimulante que je ne l'avais prévu.*

## D'un entrepôt à Brescello à une idée poursuivie la nuit

On trouve très peu de choses sur Vincenzo en ligne. Son profil [GitHub](https://github.com/JustVugg/colibri) se limite à une ligne : "Founder of Colibrì, a tiny engine, immense model", et pourtant en trois semaines, le projet a dépassé les vingt-cinq mille étoiles et s'est retrouvé au cœur du débat sur la démocratisation de l'intelligence artificielle. Je lui ai demandé qui il était, avant même de lui demander comment il avait fait.

"Je pense qu'il est difficile de trouver des informations sur moi en ligne parce que je n'ai jamais été une personne particulièrement expansive et, surtout, je n'ai jamais eu un grand intérêt à me mettre en avant. J'ai toujours préféré mettre mes projets en premier.

Pour moi, programmer a toujours été un exutoire pour l'imagination. Pendant des années, surtout la nuit, c'était simplement moi, un ordinateur et une idée à explorer. Je ne me mettais pas nécessairement à programmer parce que quelqu'un me l'avait demandé ou parce que j'avais déjà en tête un produit à vendre. Souvent, je programmais parce que j'avais besoin de comprendre si une idée que j'avais en tête pouvait devenir réalité.

J'ai toujours eu le sentiment que le projet est plus important que la personne qui le crée. Mais avec le temps, j'ai aussi compris autre chose : quand un projet commence à être utile à beaucoup de monde, celui qui l'a lancé a la responsabilité de lui donner une direction et de construire autour de lui les conditions pour qu'il puisse grandir.

Je suis né à Tarente, mais aujourd'hui je vis à Brescello, en Émilie-Romagne, le village de Don Camillo et Peppone. Ma vie n'a pas été particulièrement simple : je suis devenu orphelin à l'âge de neuf ans et, pendant une grande partie de ma vie, les moyens financiers ont été limités.

J'ai étudié l'informatique à Bari, mais à un moment donné, je n'ai plus pu continuer mes études pour des raisons financières. J'ai donc commencé à travailler dans un entrepôt comme manutentionnaire.

La vie prend souvent des chemins que l'on n'avait pas prévus. Le travail était là, mais ma tête continuait d'être ailleurs. Je n'ai jamais arrêté de programmer. Je continuais d'étudier, d'expérimenter et d'imaginer des applications et des systèmes.

J'ai été très influencé par les histoires de personnes qui ont réussi à construire quelque chose en partant de conditions loin d'être parfaites. Copier leur parcours ne m'intéressait pas. Ce qui m'intéressait, c'était de comprendre comment une idée pouvait se transformer en quelque chose capable de changer la façon dont les gens utilisent une technologie.

Du point de vue technique, j'ai toujours eu une prédilection particulière pour le C et le C++. Je les ai étudiés dès l'université et je continue de les considérer comme des outils extraordinaires lorsque le problème exige du contrôle, de la prévisibilité et de la vitesse. J'aime avoir le moins d'intermédiaires possible entre ce que je pense et ce que l'ordinateur exécute.

Colibrì est né exactement comme ça.

Je voulais comprendre s'il était possible de prendre un ordinateur relativement ordinaire, même lent et sans carte graphique (GPU) particulièrement puissante, et de réussir à exécuter un modèle énorme.

Il n'y avait pas d'entreprise derrière, il n'y avait pas d'équipe et il n'y avait pas initialement de business plan. Il y avait un problème technique qui m'intriguait suffisamment pour me faire travailler jour et nuit.

Quand j'ai réussi à le résoudre, le projet est resté un certain temps sur mon ordinateur. Puis j'ai décidé presque par hasard de le publier sur GitHub.

À partir de ce moment-là, il s'est passé quelque chose que je n'avais pas prévu.

Les gens ont commencé à l'essayer, à en discuter, à contribuer et à l'utiliser. Colibrì a commencé à devenir beaucoup plus grand que l'expérience dont il était né.

Et c'est précisément là que, pour moi aussi, la perspective a changé.

Colibrì n'est pas né parce que je voulais monter une startup. Mais quand des milliers de personnes commencent à vous dire, directement ou indirectement, que le problème que vous avez décidé d'aborder les intéresse aussi, vous devez commencer à vous demander jusqu'où la solution peut aller.

Aujourd'hui, c'est cette question qui m'intéresse."

## Ouvrir un modèle, pas seulement l'utiliser

La page GitHub du projet sonne presque comme un manifeste : "Frontier models should not be sealed inside datacenters. Colibrì exists so that anyone curious enough can open one up." Je lui demande ce que signifie vraiment pour lui "ouvrir" un modèle, pas simplement y accéder via une API, et si la démocratie de l'IA qu'il imagine est une question d'accès ou quelque chose de plus profond.

"Pour moi, l'accès à l'IA devrait être le plus simple possible. On devrait pouvoir allumer un ordinateur, ouvrir un programme et commencer à expérimenter.

Cela ne devrait pas être une possibilité réservée uniquement à ceux qui possèdent du matériel coûtant des dizaines de milliers d'euros ou à ceux qui peuvent utiliser de grandes infrastructures.

Mais je crois que l'accès n'est que le premier niveau.

Ce qui m'intéresse encore plus, c'est la possibilité de connaître la technologie que l'on utilise.

Quand je parle d'un modèle 'ouvert', je ne veux donc pas simplement dire pouvoir obtenir une réponse. Je veux dire pouvoir l'exécuter, l'observer, le mesurer, faire des expériences et chercher à comprendre ce qui se passe quand on change quelque chose.

Il y a une différence énorme entre utiliser une intelligence et pouvoir l'étudier.

Cela ne veut pas dire que le cloud est une mauvaise chose. Le cloud est et continuera d'être extrêmement important. Il y a des problèmes pour lesquels concentrer d'énormes quantités de calcul dans un centre de données est la meilleure solution.

Je pense simplement que cela ne doit pas être le seul modèle possible.

Il devrait aussi exister une autre possibilité : apporter toujours plus de capacité d'inférence au plus près de la personne, du chercheur, de l'entreprise ou de l'appareil qui en a besoin.

La démocratisation de l'IA, selon moi, devrait donc être à la fois une démocratisation de l'accès et une démocratisation de la compréhension.

Je ne voudrais pas que la première question d'une personne soit : 'Est-ce que j'ai assez de GPU pour pouvoir essayer cette chose ?'

Je voudrais que ce soit : 'Qu'est-ce que je peux découvrir si j'essaie de le faire ?'

L'IA est en train de devenir l'un des outils de connaissance les plus puissants que nous ayons construits. Plus il y aura de personnes qui pourront l'expérimenter directement, plus la probabilité augmentera que quelqu'un trouve un usage, une optimisation ou même un paradigme auquel nous n'avons pas encore pensé aujourd'hui.

Pour moi, le critère principal devrait devenir de plus en plus la curiosité, pas la taille de l'infrastructure que l'on possède."

## Un message sur Hacker News, pas un manifeste

Il y a un détail qui m'a frappé dès le début : le message avec lequel Fornaro a présenté Colibrì sur Hacker News ne s'intitulait pas "j'ai créé le moteur d'inférence ultime", mais simplement "Getting GLM-5.2 running on my slow computer". Une attitude presque modeste pour un résultat qui ne l'est pas du tout. Je lui demande quand il a compris que l'expérience personnelle devenait autre chose, et quelle réaction de la communauté lui a fait penser que les choses étaient vraiment en train de changer.

"Le titre était simplement 'Getting GLM-5.2 running on my slow computer' parce que c'était exactement cela, l'histoire.

Je ne voulais pas prétendre avoir construit le moteur d'inférence ultime. J'avais résolu un problème que je trouvais intéressant et je voulais expliquer comment.

Colibrì n'était pas né dans le but de devenir une startup. Il était né par curiosité.

Puis deux choses se sont produites.

La première a été de voir des gens utiliser réellement ce que j'avais construit.

Je me souviens en particulier d'un jeune homme qui m'a écrit pour me remercier parce que, grâce à Colibrì, il avait réussi à accéder à un modèle qui aurait autrement nécessité une machine beaucoup plus chère.

Cela m'a marqué beaucoup plus que le nombre d'étoiles.

Parce que pour la première fois, je ne regardais pas seulement une solution technique. Je regardais un problème réel éliminé pour quelqu'un.

La seconde chose a été la communauté.

Des personnes que je ne connaissais pas ont commencé à ouvrir des issues, faire des pull requests, tester du matériel, trouver des bugs et proposer des optimisations.

À ce moment-là, j'ai compris qu'il se passait quelque chose d'important : Colibrì ne grandissait pas parce que j'essayais de convaincre quelqu'un que c'était utile. Les gens venaient spontanément parce qu'ils reconnaissaient le problème.

Pour ceux qui construisent de la technologie, c'est un signal très fort.

Depuis, j'ai commencé à regarder Colibrì différemment.

Cela reste un projet open source et je veux qu'il le demeure, mais je pense que la technologie et le problème auquel nous faisons face peuvent avoir des implications beaucoup plus vastes que le dépôt d'où tout a commencé.

L'étape intéressante, maintenant, est de comprendre comment transformer cet intérêt spontané en une technologie toujours plus solide, généralisable et utilisable.

Et pour cela, inévitablement, Colibrì devra aussi grandir au-delà de la dimension d'une seule personne."
![colibri-dashboard.jpg](colibri-dashboard.jpg)
[Le tableau de bord web de Colibrì, image tirée du dépôt officiel](https://github.com/JustVugg/colibri)

## Un fichier, mille trois cents lignes, aucun compromis

Le cœur de Colibrì est un fichier C unique d'environ mille trois cents lignes, sans dépendances, sans GPU requise, sans Python au runtime. À une époque où vLLM, TensorRT-LLM et SGLang sont des projets nés dans des laboratoires avec de grandes équipes et des codebases complexes, le choix de Fornaro résonne presque comme un acte de résistance, un peu comme ces productions musicales faites maison avec quatre instruments qui réussissent à sonner plus denses qu'un orchestre entier. Je lui demande si derrière cette simplicité extrême se cache un choix purement architectural ou une conviction plus philosophique.

"C'était au départ un choix architectural, mais c'est aussi devenu une conviction.

Quand on essaie de faire fonctionner un modèle énorme sur une machine relativement petite, chaque couche supplémentaire a un coût.

On a besoin de savoir exactement où se trouve la mémoire, quand elle est déplacée, ce qui est calculé et pourquoi quelque chose est lent.

Le C me permet d'avoir un contrôle extrêmement direct sur ces choses-là.

Mais cela ne veut pas dire que je considère la complexité comme toujours négative.

La complexité est un investissement.

Il faut l'introduire lorsque la valeur qu'elle produit est supérieure au coût qu'elle ajoute.

Au début, Colibrì pouvait se permettre d'être extrêmement petit. Aujourd'hui, des backends GPU, des serveurs, des interfaces, de nouvelles architectures et d'autres composants arrivent. Inévitablement, le projet va grandir.

Le défi est de grandir sans perdre en lisibilité.

J'aimerais que le cœur du système reste quelque chose qu'un bon développeur puisse ouvrir, lire et comprendre.

Cela présente aussi un avantage très concret pour un projet open source : cela réduit énormément la barrière pour ceux qui veulent contribuer.

La simplicité, en ce sens, n'est pas seulement de l'élégance.

C'est de la vitesse de développement, de la capacité de débogage, de la facilité d'expérimentation et la possibilité d'intégrer de nouvelles personnes dans le projet."

## Le disque comme mémoire, pas comme entrepôt

Le mécanisme à la base de Colibrì a une élégance presque minimaliste : la partie dense du modèle reste résidente en RAM, tandis que les experts ne sont appelés depuis le disque que lorsqu'ils sont nécessaires, un peu comme le compilateur JIT de certains langages qui ne traduit pas tout à l'avance mais seulement ce que l'exécution exige réellement, instant après instant. Je demande à Fornaro quel est, pour quelqu'un qui aborde Colibrì pour la première fois, le concept le plus contre-intuitif à intégrer.

"Probablement, le concept le plus contre-intuitif est celui-ci : un modèle gigantesque n'utilise pas nécessairement tous ses paramètres au même moment.

Quand une personne entend '744 milliards de paramètres', elle s'imagine que pour générer chaque token, l'ordinateur doit utiliser tous ces paramètres.

Dans un modèle Mixture-of-Experts, cela ne fonctionne pas comme ça.

C'est plutôt comme une énorme organisation avec de très nombreux services spécialisés. Tous existent, mais pour chaque token, le modèle n'active qu'une partie des experts.

Donc la question cesse d'être :

'Comment faire pour mettre tout le modèle dans la RAM ?'

et devient :

'Comment faire pour avoir la bonne partie du modèle disponible au moment où elle est nécessaire ?'

Colibrì tente de répondre à cette seconde question.

Le stockage devient un niveau supplémentaire de la hiérarchie de mémoire. Les experts peuvent rester sur le disque et être amenés près du calcul lorsqu'ils servent.

C'est comme avoir un grand entrepôt et un établi relativement petit. On ne met pas tout l'entrepôt sur la table. Il faut organiser le système de manière que ce qui est nécessaire arrive sur la table suffisamment vite.

Ensuite entrent en jeu le cache, le prefetch, les patterns d'utilisation et d'autres optimisations.

Le principe général reste cependant simple :

on n'a pas nécessairement besoin de tout avoir en même temps.

Il faut réussir à avoir la bonne chose au bon moment.

Et c'est un principe qui, je crois, peut avoir des applications beaucoup plus larges au fur et à mesure que les modèles continueront de grandir."
![tiers.jpg](tiers.jpg)
[Une hiérarchie de mémoire plutôt qu'une exigence de mémoire unique, image tirée du dépôt officiel](https://github.com/JustVugg/colibri)

## 0,05 token par seconde, honnêtement

C'est ici qu'arrive le point le plus discuté en ligne. Sur un ordinateur portable avec 25 Go de RAM, les premiers benchmarks parlaient d'un token toutes les dix à vingt secondes, et une analyse de Wavect a écrit que le projet "s'exécute, mais à 0,05-0,1 token par seconde depuis un cache froid", le qualifiant de "preuve d'architecture sérieuse, pas encore un serveur prêt pour la production". Tom's Hardware indique quant à lui 20-30 tokens par seconde comme seuil pour une interaction réellement fluide, tandis que sur une machine équipée de six GPU RTX 5090, on atteint 6 tokens par seconde. Je lui demande comment il se positionne par rapport à ces observations, si Colibrì est aujourd'hui un exercice d'ingénierie fascinant ou un produit déjà utilisable.

"L'analyse de Wavect est honnête.

Qualifier les premières versions de Colibrì de 'serious proof of architecture, not yet a drop-in production server' est une description que je considère comme exacte.

La vitesse est un vrai problème et je ne veux pas le cacher.

Aujourd'hui, sur un ordinateur portable, exécuter un modèle de cette taille via Colibrì ne procure pas la même expérience que celle que l'on aurait en utilisant un modèle servi par un grand centre de données.

Mais selon moi, le point intéressant est de comprendre quelle est la trajectoire.

Auparavant, le problème était binaire : soit ce modèle rentrait dans votre infrastructure, soit il n'y rentrait pas.

Colibrì essaie de le transformer en un problème continu : à quel point pouvons-nous démarrer lentement, jusqu'où pouvons-nous améliorer le cache, le stockage, le prefetch, la spéculation, les backends accélérés, et quelle part du goulot d'étranglement pouvons-nous éliminer progressivement ?

L'ingénierie commence souvent en transformant un zéro en un chiffre.

Une fois que quelque chose fonctionne, on peut le mesurer.

Et une fois que l'on peut le mesurer, on peut commencer sérieusement à l'optimiser.

Je ne promettrais pas aujourd'hui 20 ou 30 tokens par seconde pour un modèle de plusieurs centaines de milliards de paramètres sur n'importe quel ordinateur portable. Il existe des limites physiques que le logiciel ne peut pas simplement effacer.

Mais je pense qu'il existe un espace énorme entre 'impossible' et 'aussi rapide qu'un centre de données'.

Et c'est précisément cet espace que je souhaite explorer.

À court terme, je vois Colibrì comme une plateforme très intéressante pour les développeurs, les chercheurs, les passionnés et les cas d'usage où l'accès local à des modèles énormes a une valeur particulière.

À long terme, en revanche, l'objectif est de continuer à réduire la distance entre l'inférence locale et l'infrastructure centralisée.

Si nous réussissons à le faire suffisamment bien, ce ne sera plus seulement une expérience technique.

Cela deviendra une nouvelle option d'infrastructure."

## La justesse avant le benchmark

Colibrì a encore des frontières ouvertes, ce n'est pas un serveur de production, il travaille pour l'instant avec l'architecture de GLM-5.2 et non avec des modèles MoE génériques, la validation de la qualité de la quantisation int4 est un travail en cours, le disque NVMe reste l'adversaire le plus dur à battre. Je lui demande comment il aborde ces défis et s'il existe des compromis qu'il est prêt à accepter aujourd'hui pour gagner en vitesse, ou des lignes qu'il considère au contraire comme franchissables.

"Une petite correction à la prémisse : Colibrì prend déjà en charge aujourd'hui plusieurs familles de modèles MoE et chaque nouvelle architecture ajoutée nous permet de comprendre quelque chose qui peut devenir utile aux autres également.

La quantisation a elle aussi beaucoup mûri.

Nous avons trouvé et corrigé de vrais problèmes de qualité et, en cela, la communauté a été fondamentale.

Le principal adversaire reste cependant la quantité de données à déplacer.

Et c'est pour cela qu'une règle que j'essaie d'appliquer continuellement est : mesurer avant de croire.

Il est très facile d'inventer une optimisation qui semble brillante sur le papier.

Il est beaucoup plus difficile de prouver qu'elle améliore réellement le système sur du matériel réel et avec des charges de travail réelles.

J'ai un petit laboratoire d'expériences où beaucoup d'idées vont mourir.

Et c'est exactement ce qui devrait se produire.

En ce qui concerne les compromis, je suis prêt à en accepter beaucoup.

Je peux accepter un démarrage à froid plus lent si le comportement s'améliore en cours d'utilisation.

Je peux accepter une plus grande complexité dans le format des données si cela signifie lire beaucoup moins sur le stockage.

Je peux accepter des stratégies différentes selon le matériel.

Ce que je ne veux pas sacrifier, c'est la justesse.

Un benchmark impressionnant obtenu en dégradant silencieusement la qualité du modèle ne m'intéresse pas.

Si Colibrì doit devenir une infrastructure sur laquelle d'autres personnes construisent quelque chose, la confiance dans les résultats doit passer avant le meilleur chiffre dans un tableau."

## Logiciel, matériel, modèles : trois voies qui convergent

Le projet dispose déjà de backends CUDA et Metal, d'une interface web fonctionnelle, du support natif du décodage spéculatif de GLM-5.2. Je lui demande ce qui manque pour arriver à une vitesse qui puisse réellement rivaliser avec une API cloud au quotidien, disons dix à vingt tokens par seconde sur du matériel qu'une personne ordinaire pourrait s'acheter, et si c'est une question de code, de matériel ou de futurs modèles plus adaptés à cette approche.

"Ce sont les trois choses : logiciel, matériel et modèles.

Mais l'élément le plus intéressant est probablement la façon dont ces trois parties peuvent commencer à être conçues ensemble.

Le logiciel peut faire énormément.

Nous pouvons améliorer le format des données, réduire les lectures, prédire quels experts seront nécessaires, superposer le transfert et le calcul, améliorer le cache et mieux utiliser les CPU, GPU et stockages disponibles.

Mais le logiciel ne peut pas effacer une limite physique.

Le matériel continuera donc d'être important.

Les SSD grand public deviennent de plus en plus rapides, la capacité mémoire augmente et les architectures des ordinateurs changent elles aussi.

Pour Colibrì, c'est particulièrement intéressant parce que nous ne considérons pas le stockage simplement comme l'endroit d'où charger le modèle au départ, mais comme une partie active de l'architecture d'inférence.

Ensuite, il y a les modèles.

Les modèles actuels ont été conçus pour des infrastructures dans lesquelles existent d'énormes quantités de mémoire et de bande passante.

Ils n'ont pas été optimisés en pensant à une machine grand public qui doit décider continuellement quelles parties du modèle rapprocher du calcul.

Je ne vois cependant aucune raison pour laquelle cela devrait rester une constante.

Des modèles ayant une plus grande localité, des experts plus petits, un routage plus prévisible ou des structures conçues explicitement pour des hiérarchies de mémoire pourraient changer radicalement le problème.

En un sens, il se pourrait que Colibrì soit arrivé avant le modèle idéal pour ce type d'inférence.

C'est aussi l'une des choses que je trouve les plus intéressantes du point de vue de l'avenir.

Je ne veux pas que Colibrì soit simplement 'un programme qui fait tourner GLM sur un ordinateur portable'.

Ce qui m'intéresse, c'est de comprendre si certaines des idées que nous explorons peuvent devenir une autre manière de penser l'inférence de très grands modèles.

Si cela se produit, le marché potentiel ne sera pas limité au seul passionné avec un ordinateur lent.

Cela pourra concerner les stations de travail, l'edge computing, les entreprises qui veulent conserver leurs données localement, la recherche, les appareils dédiés et probablement des cas d'usage que nous n'avons pas encore imaginés aujourd'hui."

## Posséder un modèle : au-delà de l'économie

Il y a ceux qui voient dans Colibrì la preuve que l'IA locale peut devenir réalité même pour ceux qui n'ont pas les moyens d'avoir un centre de données, et il y a ceux qui rétorquent que la démocratisation de l'IA est déjà une réalité, qu'il suffit d'un navigateur et de vingt dollars par mois pour ChatGPT. Je lui demande comment il répond à cette objection, et ce que signifie réellement posséder un modèle au-delà de la simple économie financière, que ce soit une question de confidentialité, de liberté, ou de quelque chose de plus radical comme la capacité de faire de la science sur l'IA, pas seulement de l'utiliser.

"L'objection est absolument légitime.

Si la question est 'est-ce que je peux utiliser une intelligence artificielle très puissante ?', le cloud a déjà énormément démocratisé l'accès.

Et c'est une chose extraordinaire.

Je ne considère pas Colibrì comme une guerre contre le cloud.

Je pense que le cloud et l'IA locale résolvent des problèmes différents et qu'ils coexisteront à l'avenir.

Il y aura des activités pour lesquelles il sera logique d'utiliser le modèle le plus puissant disponible dans un centre de données.

Et il y en aura d'autres où la latence, la confidentialité, la prévisibilité des coûts, l'indépendance vis-à-vis du réseau, le contrôle de l'infrastructure ou la possibilité d'étudier exactement le système que l'on utilise seront importants.

Je pense à l'histoire de l'informatique.

L'ordinateur personnel n'a pas rendu les grands ordinateurs inutiles.

Il a simplement ouvert une autre dimension de l'informatique.

Le fait qu'un ordinateur vous appartienne signifiait que vous pouviez le programmer, le modifier, le casser, expérimenter.

Avec l'IA, je pense qu'il peut se produire quelque chose de similaire.

Un service distant est extraordinairement pratique quand on veut obtenir une réponse.

Un modèle local devient intéressant quand on veut aussi poser des questions sur le système lui-même.

Pourquoi a-t-il répondu ainsi ?

Comment le comportement change-t-il si je modifie ce composant ?

Jusqu'à quel point puis-je le compresser ?

Puis-je reproduire le même résultat dans cinq ans ?

Puis-je utiliser des données que je ne veux pas envoyer hors de mon infrastructure ?

Puis-je construire un produit qui continue de fonctionner sans dépendre complètement d'un fournisseur externe ?

Je ne vois donc pas l'avenir comme 'le cloud contre le local'.

Je le vois comme un continuum.

Et je pense qu'aujourd'hui, une partie de ce continuum est encore beaucoup moins développée que l'autre.

C'est là que Colibrì essaie de travailler."

## 2036 et l'héritage d'une idée

Concluons en me tournant vers l'avenir. Imaginez 2036 : les modèles sont devenus encore plus grands ou peut-être plus petits et plus intelligents, le matériel grand public s'est transformé. Je lui demande si Colibrì, ou quelque chose qui en est né, sera encore pertinent, ce qu'il rêve de voir se produire dans les dix prochaines années pour ceux qui veulent garder l'intelligence artificielle entre leurs mains, et plus personnellement, après vingt-cinq mille étoiles et les titres dans Tom's Hardware et Hacker News, ce qu'il aimerait que les gens retiennent de lui.

"En 2036, j'espère que beaucoup des choses que Colibrì rend difficiles aujourd'hui seront devenues normales.

Cela ne veut pas dire que j'espère que Colibrì disparaîtra.

Cela veut dire que j'espère qu'il évoluera.

Les projets technologiques importants restent rarement identiques à leur première version. Ils changent en même temps que le problème qu'ils essaient de résoudre.

Si dans dix ans, exécuter des modèles énormes sur du matériel relativement ordinaire est devenu normal, ce sera une victoire.

À ce moment-là, Colibrì sera probablement en train de faire face à une autre frontière.

Ce que j'aimerais voir rester constant, c'est l'idée de fond : réduire la distance entre une personne curieuse et une technologie qui semble aujourd'hui trop grande, coûteuse ou complexe pour être explorée directement.

J'aimerais qu'en 2036, une personne puisse regarder un modèle avancé et se dire :

'Je veux comprendre comment ça fonctionne.'

Et puisse le faire.

En ce qui concerne ce que je souhaite construire personnellement, je ressens aujourd'hui une responsabilité différente par rapport au début.

Colibrì est né comme une expérience individuelle, mais je ne pense pas qu'il doive nécessairement le rester.

Si nous voulons aborder sérieusement ce problème, il faudra des personnes beaucoup plus douées que moi dans de nombreux domaines différents, il faudra une communauté toujours plus forte et il faudra probablement aussi construire une structure capable de soutenir le projet sur le long terme.

Cela ne change pas la raison pour laquelle j'ai commencé.

Cela la rend simplement plus ambitieuse.

Et si dans dix ans quelqu'un, face à un problème que tout le monde considère comme impossible, se dit :

'Essayons.'

et utilise peut-être quelque chose qui est né aussi du travail accompli aujourd'hui sur Colibrì, pour moi ce sera déjà un résultat énorme.

Retenir l'idée de Vincenzo Fornaro comme un 'génie' ne m'intéresse pas particulièrement.

Ce qui m'intéresserait beaucoup plus, c'est qu'une autre idée demeure :

qu'une personne disposant de peu de moyens, mais de suffisamment de curiosité, puisse encore entreprendre quelque chose d'assez important pour attirer d'autres personnes et devenir beaucoup plus grande qu'elle.

C'est exactement ce qui est en train de se produire avec Colibrì."

---

*Le [dépôt de Colibrì](https://github.com/JustVugg/colibri) reste consultable sur GitHub pour ceux qui veulent l'essayer, y contribuer, ou simplement lire ces mille trois cents lignes de C qui ont lancé la conversation.*
