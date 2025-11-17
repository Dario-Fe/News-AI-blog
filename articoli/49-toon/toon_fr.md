---
tags: ["Research", "Applications", "Training"]
date: 2025-11-17
author: "Dario Ferrero"
---

# TOON réécrit les règles des données pour l'ère de l'IA. Qu'adviendra-t-il de JSON ?
![toon.jpg](toon.jpg)


*Il y a un paradoxe dans l'économie de l'intelligence artificielle que peu de gens remarquent jusqu'à ce qu'ils regardent la facture. Chaque fois que nous envoyons des données à GPT, Claude ou Gemini, nous payons pour chaque caractère. Pas pour la complexité de la demande, pas pour l'intelligence de la réponse, mais pour la verbosité du format. Ces accolades qui rendent JSON si familier ? Elles coûtent de l'argent. Les guillemets qui délimitent chaque clé ? Des jetons précieux. Les deux-points qui séparent les clés et les valeurs ? D'autres centimes qui s'envolent, multipliés par des millions d'appels d'API.*

Lorsque Johann Schopplich a publié [TOON (Token-Oriented Object Notation)](https://github.com/toon-format/toon) au début de l'année 2025, la réaction initiale de la communauté a été celle qui accompagne toutes les idées simples mais géniales : "Pourquoi diable n'y ai-je pas pensé ?". Comme le minimalisme japonais appliqué à la sérialisation des données, TOON élimine tout ce qui n'est pas nécessaire. Pas d'accolades, pas de guillemets superflus, pas de répétitions obsessionnelles des mêmes clés. Seulement l'essence de la donnée, aussi pure qu'un haïku.

## Le coût invisible des accolades

JSON est né à une époque où les ordinateurs communiquaient principalement entre eux. Douglas Crockford l'a extrait de JavaScript comme un sous-produit heureux, privilégiant la lisibilité humaine et la compatibilité multiplateforme à l'efficacité. Pendant des années, ce compromis a fonctionné à merveille. Les octets supplémentaires nécessaires pour représenter un objet avec toutes ses décorations syntaxiques étaient insignifiants par rapport à la simplicité de l'analyse et à la familiarité du format.

Mais l'arrivée des grands modèles de langage a changé les règles du jeu. Lorsque les coûts des API sont calculés par million de jetons, ces accolades ne sont soudain plus d'inoffensives conventions syntaxiques. Elles deviennent une inefficacité économique mesurable. JSON peut consommer deux fois plus de jetons que d'autres formats pour représenter les mêmes données, et ce avant même de considérer que les modèles ont été entraînés précisément sur des montagnes de JSON, ce qui le rend paradoxalement moins efficace pour le traitement.

Considérons un exemple réel. Une liste de cent dépôts GitHub avec des métadonnées complètes : étoiles, forks, descriptions, horodatages. En JSON formaté, cette structure consomme 15 145 jetons. La même information identique en TOON ? 8 745 jetons. Une réduction de 42,3 %. Nous ne parlons pas de compression avec perte ni de tours de magie. C'est la même information, réversible au bit près, simplement représentée de manière plus intelligente.

Le calcul devient encore plus brutal avec les données temporelles. Cent quatre-vingts jours de métriques web (vues, clics, conversions, revenus) nécessitent 10 977 jetons en JSON contre 4 507 en TOON, soit une économie de 58,9 %. Lorsque vous multipliez ces chiffres par des milliers de requêtes quotidiennes dans une application d'entreprise, la différence entre un projet durable et un projet qui brûle son budget devient tangible.

## Quand moins devient plus

L'intuition centrale de TOON est d'une simplicité désarmante : lorsque vous avez des tableaux uniformes d'objets avec les mêmes champs, pourquoi répéter les clés pour chaque élément ? C'est comme si chaque ligne d'une feuille de calcul Excel devait inclure l'en-tête de la colonne. Inefficace et redondant.

TOON emprunte l'indentation à YAML pour les structures imbriquées et le format tabulaire à CSV pour les tableaux uniformes, puis optimise les deux pour le contexte spécifique des grands modèles de langage. Le résultat est un format qui semble évident une fois qu'on l'a vu, mais qui exige de repenser certaines hypothèses fondamentales sur la manière dont nous représentons les données.

Un tableau d'utilisateurs en JSON classique répète obsessionnellement la même structure :
![json-format.jpg](json-format.jpg)

TOON déclare la structure une seule fois dans l'en-tête, puis ne liste que les valeurs :
![toon-format.jpg](toon-format.jpg)

Le marqueur `[2]` communique explicitement la longueur du tableau, tandis que `{id,name,role}` définit le schéma. Chaque ligne suivante ne contient que les données brutes, séparées par des virgules. C'est l'élégance fonctionnelle au sens du Bauhaus : la forme suit la fonction, zéro ornement superflu.

Cette économie syntaxique se manifeste par trois stratégies complémentaires. Tout d'abord, l'indentation remplace les accolades pour les objets imbriqués. Deuxièmement, les chaînes ne sont mises entre guillemets que lorsque cela est strictement nécessaire pour éviter toute ambiguïté (espaces de début ou de fin, caractères de contrôle, valeurs qui pourraient être confondues avec des booléens ou des nombres). Troisièmement, le format tabulaire pour les tableaux homogènes transforme les répétitions verbeuses en lignes compactes de style CSV.

Le résultat ? TOON obtient généralement une réduction de 30 à 60 % de la consommation de jetons par rapport à JSON sur des ensembles de données structurées. Et il ne s'agit pas seulement de compter les caractères économisés. C'est une différence qui se traduit directement par une réduction des coûts d'exploitation, des fenêtres de contexte plus larges disponibles pour des données supplémentaires et des temps de réponse plus rapides.

## La géométrie de l'économie

Les benchmarks officiels du projet TOON racontent une histoire intéressante sur les conditions qui amplifient ou réduisent les avantages du format. Ce n'est pas de la magie universelle, c'est de la géométrie appliquée à la structure des données.

Le point optimal, ce "sweet spot" où TOON brille le plus, ce sont les tableaux uniformes d'objets avec des valeurs primitives. Résultats de requêtes de base de données, exportations CSV, données analytiques temporelles. Plus vos lignes sont identiques dans leur structure, plus TOON peut compresser la surcharge syntaxique en ne déclarant le schéma qu'une seule fois.

Lors de tests menés sur quatre modèles différents (GPT-5 Nano, Claude Haiku, Gemini Flash, Grok) à travers 154 questions de récupération de données, TOON a obtenu une précision moyenne de 70,1 % en utilisant 4 678 jetons, contre 65,4 % pour JSON qui en consommait 8 713. Non seulement une économie financière, mais aussi une plus grande précision dans les réponses. La structure explicite (longueur des tableaux, déclaration des champs) aide les modèles à analyser et à valider les données de manière plus fiable.

Mais les résultats varient considérablement d'un modèle à l'autre. GPT-5 Nano a montré une précision de 96,1 % avec TOON, tandis que Claude Haiku s'est arrêté à 48,7 %. Cette disparité suggère que l'entraînement compte : les modèles exposés principalement à JSON pendant leur entraînement pourraient avoir initialement du mal avec des formats alternatifs, quelle que soit leur efficacité théorique.

Le problème de l'entraînement n'est pas anodin. Les LLM actuels ont été nourris avec des milliards de jetons de JSON provenant d'API, de configurations, d'ensembles de données publics. TOON est né en 2025, donc les modèles les plus récents ont vu relativement peu de ce format dans leurs corpus d'entraînement. C'est un problème classique d'amorçage : le format est plus efficace, mais l'écosystème doit encore s'adapter.

Il est intéressant de noter que les tests révèlent également les limites de TOON. Pour les structures profondément imbriquées ou les données non uniformes, les avantages se réduisent considérablement. Un objet avec des champs optionnels qui apparaissent sporadiquement, ou des arbres hiérarchiques avec de nombreux niveaux d'imbrication, pourraient s'avérer plus lisibles et même plus efficaces en JSON. TOON ne s'applique pas bien aux données profondément imbriquées ou non uniformes, où JSON peut s'avérer plus efficace.
![toon-schema.jpg](toon-schema.jpg)
[Image tirée du dépôt GitHub officiel](https://github.com/toon-format/toon)

## Où ça marche (et où ça ne marche pas)

Séparer le battage médiatique de la réalité pratique exige de la franchise sur les cas d'utilisation. TOON n'est pas "le nouveau JSON" au sens d'un remplacement universel. C'est un outil spécialisé pour un problème spécifique : optimiser le transfert de données structurées vers et depuis les grands modèles de langage.

Les scénarios gagnants sont clairs. Vous construisez un pipeline RAG qui envoie des centaines d'enregistrements de produits à un LLM pour générer des descriptions ? TOON réduit les coûts. Vous avez une application qui traite des milliers de lignes d'analyses quotidiennes via GPT pour en extraire des informations ? Économie immédiate. Vous devez transmettre les résultats de requêtes de base de données avec des centaines d'utilisateurs, de commandes ou de transactions à Claude pour analyse ? TOON est né pour ça.

Le format excelle lorsque la structure est plate et uniforme, lorsque les volumes sont élevés, lorsque les coûts des jetons représentent un poste budgétaire important. Pour des cas d'utilisation comme la génération de calendriers éditoriaux, de listes de produits, de tableaux d'utilisateurs, de lignes d'analyses, où le budget en jetons ou la fenêtre de contexte sont des contraintes réelles, TOON offre des avantages concrets et mesurables.

Mais il existe des territoires où JSON conserve l'avantage. Les données très imbriquées et irrégulières, où la structure varie considérablement d'un enregistrement à l'autre, ne bénéficient pas du format tabulaire de TOON. Les objets complexes avec de nombreux champs optionnels deviennent verbeux même en TOON lorsque vous devez gérer l'absence de valeurs ou des structures variables.

Il y a ensuite la question de l'écosystème. JSON dispose de décennies d'outils matures : débogueurs, formateurs, validateurs, bibliothèques dans tous les langages imaginables. TOON a lancé sa première version en 2025 et, bien qu'il ait des implémentations en TypeScript, Python, Go, Rust, Java, C++, PHP, Ruby, Swift, Elixir, Dart, Clojure, Crystal et d'autres langages, l'écosystème est encore jeune. JSON a des décennies d'outils, tandis que TOON est plus récent avec un écosystème plus petit.

Le débogage est plus compliqué. Lorsque quelque chose se casse en production et que vous devez inspecter une charge utile TOON, vous ne pouvez pas simplement ouvrir les outils de développement du navigateur et faire un "pretty-print". Vous devez reconvertir en JSON, identifier le problème, puis reconvertir. Cela ajoute de la friction au flux de travail de développement, en particulier dans les équipes qui ne sont pas encore familières avec le format.

L'adoption en entreprise soulève des questions organisationnelles qui vont au-delà de la pure technique. Convaincre une équipe de changer de format de données nécessite une adhésion à plusieurs niveaux. Les développeurs doivent apprendre la nouvelle syntaxe. Le code hérité doit être mis à jour ou doit coexister avec des couches de conversion. Les processus de CI/CD doivent être adaptés. Convaincre les équipes et la direction d'adopter un nouveau format pour une réduction des coûts de 30 à 60 % semble facile sur le papier, mais dans la pratique, il y a toujours une résistance au changement.

La stratégie la plus pragmatique, celle qu'adoptent les équipes qui expérimentent avec TOON, est chirurgicale plutôt qu'holistique. Elles ne remplacent pas JSON dans l'ensemble de la pile. Elles conservent JSON comme format interne pour le stockage, les API externes, les contrats entre services. Elles utilisent TOON exclusivement comme une couche d'optimisation pour la communication avec les LLM, où l'efficacité des jetons compte vraiment. L'approche optimale pour la plupart des organisations combine les deux : JSON comme standard interne pour la compatibilité et TOON pour l'optimisation spécifique aux LLM.

Elles convertissent au moment opportun, aux points à fort trafic où les économies se multiplient : les points de terminaison qui génèrent des milliers d'appels LLM quotidiens, les pipelines par lots qui traitent de gros volumes, les applications en temps réel où la latence réduite fait une différence dans l'expérience utilisateur.

## Le vrai prix de l'efficacité

Réduire la consommation de jetons n'est pas seulement une optimisation économique. C'est aussi une question environnementale que l'industrie technologique a encore du mal à aborder ouvertement. Chaque jeton traité nécessite des cycles de GPU, chaque cycle consomme de l'énergie, chaque kilowattheure contribue à l'empreinte carbone des centres de données.

La demande croissante d'IA générative a déjà augmenté la consommation d'énergie mondiale de l'informatique, et l'optimisation de l'utilisation des jetons devient une nouvelle frontière non seulement pour l'efficacité, mais aussi pour la durabilité. Lorsque TOON réduit de 50 % les jetons nécessaires pour représenter un ensemble de données, il réduit également d'environ la moitié l'énergie nécessaire pour traiter cette demande. Multiplié par des millions d'appels d'API à travers des milliers d'applications, l'impact global n'est pas négligeable.

Mais l'efficacité a aussi des coûts cachés, d'une autre nature. TOON introduit une complexité cognitive pour les développeurs. Vous devez apprendre les règles de mise entre guillemets des chaînes (quand les guillemets sont-ils nécessaires ? que se passe-t-il avec les délimiteurs alternatifs ?). Vous devez comprendre quand utiliser le format tabulaire par rapport au format liste. Vous devez gérer les cas limites comme les tableaux de tableaux ou les objets avec des champs optionnels épars.

La courbe d'apprentissage n'est pas abrupte, mais elle existe. Pour les petites équipes ou les projets avec des volumes modestes d'appels LLM, le temps investi dans l'apprentissage et la mise en œuvre pourrait dépasser les économies financières. Pour les applications à petite échelle qui effectuent 100 appels LLM par jour, le temps d'ingénierie pour mettre en œuvre TOON ne vaut probablement pas les économies.

Il y a ensuite la question de la maturité du format. La spécification TOON est actuellement à la version 1.4, avec des tests de conformité indépendants du langage qui aident les implémenteurs à garantir la compatibilité multiplateforme. Mais c'est un format qui a moins d'un an de vie dans le monde réel. Nous ne savons pas encore quels cas limites apparaîtront avec une utilisation massive en production, quels schémas s'avéreront problématiques, quelles optimisations supplémentaires deviendront nécessaires.

Le projet a publié des tests de conformité publics et maintient une spécification formelle sur GitHub, des signes positifs d'une gouvernance sérieuse. Mais l'adoption à grande échelle révélera inévitablement des problèmes que les tests unitaires ne capturent pas. C'est le compromis classique entre être un "early adopter" (avantages immédiats, risque de stabilité) et attendre la maturité (moins de risques, mais des coûts plus élevés entre-temps).

L'aspect le plus intrigant, peut-être, est plus culturel que technique. TOON nous oblige à penser différemment la représentation des données. Pendant trente ans, nous avons considéré JSON comme le format "naturel" pour les données structurées, au point que nous pensons souvent directement en termes d'objets avec des clés et des valeurs entre accolades. TOON exige un changement de perspective : penser d'abord à la forme des données (est-elle tabulaire ? imbriquée ? uniforme ?) puis à la représentation optimale.

Comme la programmation fonctionnelle qui vous apprend à penser en termes de transformations immuables plutôt que de mutations d'état, ou comme l'architecture RISC qui privilégie les instructions simples et nombreuses au lieu de quelques instructions complexes, TOON promeut un état d'esprit différent. L'élégance de la soustraction plutôt que l'accumulation de fonctionnalités.

TOON ne remplacera pas JSON, tout comme Markdown n'a pas remplacé HTML ou YAML n'a pas éliminé XML. Chaque format a trouvé sa propre niche, son propre contexte où les compromis spécifiques ont un sens. JSON restera la norme pour les API, les configurations, le stockage. Mais pour ce domaine spécifique et croissant qu'est la communication avec les grands modèles de langage, TOON offre une alternative rationnelle fondée sur des principes solides.

L'idée derrière TOON est cette intuition classique qui ne semble évidente qu'après que quelqu'un l'a eue : si les modèles paient pour chaque jeton, pourquoi continuer à utiliser un format conçu il y a quarante ans pour résoudre des problèmes différents ? C'est le même type d'intuition qui a conduit à la naissance de protobuf pour remplacer XML dans les communications de Google, ou de JSON lui-même comme une alternative plus légère à SOAP.

La question pertinente pour les développeurs et les responsables techniques n'est pas "TOON remplacera-t-il JSON ?" mais "Mes cas d'utilisation spécifiques bénéficient-ils de l'optimisation des jetons ?". Si vous travaillez avec de gros volumes de données structurées uniformes qui passent par des LLM, si les coûts des API sont un poste important de votre budget de fonctionnement, si la fenêtre de contexte limitée est une contrainte réelle dans vos applications, alors TOON mérite une expérimentation sérieuse. Convertissez un point de terminaison à fort trafic, mesurez les économies réelles, évaluez si la complexité ajoutée vaut les avantages concrets.

Si, en revanche, vous effectuez des appels sporadiques avec de petites charges utiles, si l'équipe est réduite et doit concentrer son temps sur les fonctionnalités plutôt que sur les optimisations, si les données sont principalement imbriquées et irrégulières, alors JSON reste le choix pragmatique. L'optimisation prématurée, comme nous l'a enseigné Knuth, est la racine de tous les maux. Ou du moins de 97 % d'entre eux.

L'avenir de TOON dépendra de deux facteurs : la rapidité avec laquelle l'écosystème des LLM fera évoluer ses modèles pour reconnaître et optimiser le format, et l'efficacité avec laquelle la communauté parviendra à construire des outils matures qui rendront l'adoption fluide. Si dans deux ans les principaux fournisseurs de LLM incluent TOON comme un format nativement pris en charge aux côtés de JSON dans leurs SDK, si les éditeurs et les débogueurs intègrent la coloration syntaxique et la validation pour TOON, si les cadres RAG et les bibliothèques d'orchestration d'IA le prennent en charge d'emblée, alors l'adoption se développera de manière organique.

En attendant, TOON reste ce qu'il a toujours été : une idée simple mais géniale qui vous fait vous demander pourquoi vous n'y avez pas pensé vous-même. Et peut-être, dans son élégance minimaliste, y a-t-il une leçon plus large pour toute l'industrie technologique : parfois, l'innovation ne consiste pas à ajouter de la complexité, mais à en soustraire.
