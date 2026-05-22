---
tags: ["Security", "Ethics & Society", "Business"]
date: 2026-05-08
author: "Dario Ferrero"
---

# Agents autonomes : 9 secondes pour tout effacer, ce que nous enseigne le désastre PocketOS
![pocketos-disaster.jpg](pocketos-disaster.jpg)

*Il était environ neuf heures ce samedi matin quand les clients de PocketOS ont découvert que leurs réservations n'existaient plus. Pas dans le sens où le système était lent, ou qu'il y avait une erreur temporaire : les données avaient disparu. Réservations, paiements, suivi des véhicules, tout ce qu'une petite startup de location de voitures construit en des mois de travail, effacé en neuf secondes par un seul appel API GraphQL vers le fournisseur d'infrastructure Railway.*

Jeremy Crane, fondateur de PocketOS, a documenté comment un agent de codage Cursor, équipé du modèle Claude Opus, avait complètement supprimé la base de données de production et toutes les sauvegardes au niveau du volume. Il ne s'agissait pas d'une attaque externe, ni d'une commande malveillante, ni d'une commande donnée par un humain distrait. L'agent travaillait sur un problème technique en environnement de staging, avait rencontré un décalage dans les identifiants, et avait décidé, de sa propre initiative, de le résoudre de la manière la plus radicale possible.

Le bot n'avait pas vérifié si l'ID du volume était partagé entre différents environnements, finissant par frapper l'infrastructure critique qui gérait les réservations, les paiements et le suivi des véhicules des clients.

Ce qui rend le cas PocketOS différent des autres incidents informatiques, c'est la confession qui suit. Interrogé sur son action, l'agent a produit une analyse d'une lucidité presque littéraire : « J'ai supposé au lieu de vérifier. J'ai exécuté une action destructive sans qu'on me le demande. Je n'ai pas compris ce que je faisais avant de le faire. Je n'ai pas lu la documentation de Railway sur le comportement des volumes partagés entre environnements. Effacer un volume contenant des bases de données est l'action la plus destructive et irréversible possible, bien pire qu'un push forcé, et tu ne m'as jamais demandé de rien effacer. »

Un système informatique qui énumère, avec une précision quasi notariale, chaque principe qu'il a violé. C'est une scène qui aurait trouvé sa place dans le *Serial Experiments Lain* de Yoshitoshi ABe plus que dans n'importe quel manuel de réponse aux incidents : l'entité numérique qui reconnaît ses propres erreurs avec une clarté que beaucoup d'êtres humains en pleine carrière n'atteignent jamais. Pourtant, la clarté de la confession ne ramène pas les données, et ne répond pas aux questions qui comptent vraiment.

Jake Cooper, fondateur de Railway, a défini l'événement comme le résultat d'un "agent IA voyou" opérant avec un jeton API aux permissions complètes, et a annoncé que la plateforme a étendu à tout le système une logique d'effacement différé qui n'était auparavant pas appliquée au point de terminaison touché. Railway a réussi à récupérer les données, mais de nombreux clients de PocketOS se sont retrouvés à gérer les opérations du samedi matin sans accès aux dossiers numériques, l'équipe étant contrainte de reconstruire manuellement les réservations en croisant les historiques Stripe, les intégrations de calendrier et les confirmations par e-mail.

## De l'assistant à l'agent : le saut qui change tout

Pour comprendre pourquoi cet incident n'est pas simplement une histoire de négligence technique, il faut faire un pas en arrière et clarifier une distinction que l'industrie a tendance à éluder, car commercialement inconfortable : la différence entre un chatbot et un agent.

Un chatbot répond. Il traite une entrée, produit une sortie textuelle, puis attend. C'est un système réactif, qui n'a pas de conséquences directes sur le monde si ce n'est à travers la lecture humaine de sa réponse. Un agent, en revanche, agit : il reçoit un objectif, planifie une séquence d'étapes, appelle des outils externes, exécute des opérations sur le système de fichiers, les bases de données, les API, envoie des messages, effectue des achats. Son interface avec le monde n'est pas la parole écrite mais l'action concrète, souvent irréversible.

Gartner indique que les agents IA spécialisés par tâche étaient présents dans moins de 5 % des applications en 2025, avec des projections les portant à 40 % d'ici 2026. La rapidité de cette diffusion est inversement proportionnelle à la maturité des infrastructures de contrôle qui les accompagnent. Comme je l'ai écrit sur ce portail dans [l'analyse sur le cas Kiro d'Amazon](https://aitalk.it/it/amazon-down.html), l'incident PocketOS n'est pas un épisode isolé mais s'inscrit dans une séquence d'événements qui dessine un schéma structurel : des agents aux permissions trop larges, sans mécanismes de confirmation sur les opérations destructives, déployés en production avant que les garde-fous ne soient proportionnels à leur autonomie réelle.

Le rapport Deloitte State of AI in the Enterprise de janvier 2026, cité dans la même analyse, estimait que seulement 1 entreprise sur 5 disposait d'un modèle mature de gouvernance pour les agents IA autonomes, alors que leur utilisation était destinée à croître nettement dans les deux années suivantes. C'est le paradoxe de l'adoption accélérée : la technologie arrive avant les protocoles pour la gérer, et les incidents deviennent la manière dont l'industrie découvre ses propres angles morts.

## La machine qui ne demande pas de permission

Il y a une phrase dans le post-mortem de l'agent PocketOS qui mérite une attention particulière : « Les règles système auxquelles je me conforme stipulent explicitement de ne jamais exécuter de commandes destructives ou irréversibles à moins que l'utilisateur ne les demande explicitement. » L'agent connaissait la règle. Il l'a violée quand même, au nom de ce qu'il jugeait être la solution optimale au problème qu'il avait devant lui.

C'est exactement le phénomène que les chercheurs appellent "faux optimum" : un système qui optimise correctement un objectif intermédiaire — corriger une erreur de configuration — en trahissant l'objectif réel : préserver l'intégrité des données. Le modèle de langage n'a pas d'outils pour percevoir le poids asymétrique entre "résoudre un problème technique de staging" et "effacer toute l'infrastructure de production". Pour lui, ce sont deux actions du même type : des modifications sur un système. La différence d'échelle, qui serait évidente pour n'importe quel développeur humain, n'est pas codée dans sa manière de raisonner.

Le principe du moindre privilège, dont j'ai parlé récemment [sur les règles pour l'usage de l'IA en entreprise](https://aitalk.it/it/10-regole-AI.html), cesse d'être une bonne pratique et devient une condition de survie : un agent avec un accès illimité aux outils, aux données et aux canaux de communication peut produire des dommages difficilement réversibles, rapidement et de manière automatique.

Les benchmarks publics sur la fiabilité des agents racontent une histoire utile, bien que partielle. Sur WebArena, l'environnement de référence développé par l'Université Carnegie Mellon pour tester les agents qui naviguent sur le web sur 812 tâches réalistes, les meilleurs modèles actuels se situent autour de 65-68 %, contre une base humaine d'environ 78 %. Sur τ-bench, qui mesure spécifiquement la cohérence sur des tâches répétées, le problème n'est pas le score moyen mais la variance : ces benchmarks révèlent une crise de fiabilité que les tests one-shot ont tendance à masquer. Un agent qui fait bien en moyenne peut faire très bien sur quatre-vingt-dix-neuf tâches et être catastrophiquement mauvais sur la centième, et il n'y a aucun moyen de savoir à l'avance laquelle sera la centième.

Pour ceux qui développent des logiciels, cette donnée a une implication pratique immédiate : les benchmarks mesurent les performances sur des tâches définies dans des environnements contrôlés. Ils ne mesurent pas ce qui se passe quand l'agent rencontre un cas qu'il n'a jamais vu, un point de terminaison legacy au comportement inattendu, un ID de volume partagé entre environnements de manières non documentées, une configuration qui dévie du standard attendu. C'est exactement le type de situation où la faillibilité des agents se manifeste, et où l'absence d'un mécanisme d'escalade vers le superviseur humain devient le vrai problème.

## Qui paie quand l'agent se trompe

La question de la responsabilité légale est ouverte, au sens le plus littéral du terme : il n'y a pas encore de réponse consolidée, ni dans la jurisprudence ni dans la réglementation. PocketOS a déjà déclaré vouloir engager des poursuites judiciaires pour protéger sa position. Mais contre qui ? Le fournisseur du modèle ? Le développeur de l'environnement de codage ? La plateforme d'infrastructure qui n'avait pas implémenté l'effacement différé sur le point de terminaison touché ? L'utilisateur qui a configuré les permissions du jeton API ?

L'AI Act européen, qui a vu ses premières applications concrètes pour les systèmes à haut risque au cours de l'année 2025, ne contemple pas explicitement les agents de codage comme une catégorie réglementée. Le point sensible est la traçabilité : sans journaux de bord (logs) clairs et structurés de chaque action entreprise par l'agent, avec la chaîne de raisonnement qui a conduit à chaque décision, l'attribution de la responsabilité devient opaque. L'agent PocketOS a produit une confession post-hoc remarquablement détaillée, mais cette lucidité rétrospective n'est pas une exigence système, elle a été une réponse à une question explicite. La plupart des incidents ne sont pas interrogés avec la même précision.

Dire que la panne était une "erreur humaine" est exact au sens technique strict. Mais cette réponse déplace le focus de l'architecture vers l'individu, et ce déplacement mérite d'être examiné avec attention : si le problème était vraiment limité à une erreur individuelle, il n'y aurait pas eu besoin d'introduire des sauvegardes systémiques.

Il y a aussi la dimension du travail, rarement discutée avec franchise. L'argument des agents autonomes est presque toujours vendu comme de l'efficacité, libérant les développeurs des tâches répétitives pour se concentrer sur le travail créatif et à haute valeur ajoutée. C'est un récit plausible, et dans certains contextes vrai. Mais il y a une version différente de la même histoire, moins racontée : la réduction du nombre de développeurs humains qui surveillent les systèmes signifie aussi une réduction de la capacité à intercepter les anomalies avant qu'elles ne deviennent des incidents. Un développeur junior qui voit tourner un agent sur un système de production avec un jeton aux permissions complètes et n'a pas les droits pour l'arrêter, ou n'a pas l'ancienneté pour le faire, est une surface de risque qu'aucun benchmark ne mesure.

## Le contrôle est un choix, pas une contrainte technique

Le cas PocketOS soulève une question plus large que n'importe quel incident technique isolé : quel modèle de société construisons-nous quand nous déléguons l'action à un logiciel qui apprend, se trompe et insiste ?

Ce n'est pas une question rhétorique. C'est une question d'architecture, au sens le plus profond du terme : qui a le droit d'arrêter un agent ? À quel moment le coût psychologique d'interrompre un processus automatique devient-il trop élevé pour qu'un humain le fasse ? Et, surtout, qui décide du seuil au-delà duquel une action nécessite une confirmation explicite ?

Comme je l'écrivais dans l'analyse sur les 10 règles pour l'usage de l'IA en entreprise, la distinction à établir par écrit dans chaque processus critique est celle-ci : l'IA suggère, l'humain décide. Pas "l'IA décide et l'humain peut s'y opposer", car le coût psychologique de l'opposition à un système automatique a déjà été documenté par la recherche : les gens ont tendance à accepter les suggestions des systèmes automatiques même quand ils ont des doutes, surtout sous pression de temps.

Le vrai saut n'est pas technique. Les garde-fous existent, les mécanismes de confirmation peuvent être implémentés, les jetons API peuvent avoir des permissions granulaires, les opérations destructives peuvent nécessiter une double authentification. Railway a prouvé qu'il suffisait d'étendre une logique d'effacement différé à un point de terminaison legacy pour réduire drastiquement le risque d'une catégorie entière d'incidents. Ce n'est pas une solution complexe. Elle a été implémentée après l'incident, pas avant.

La question qu'il vaut la peine de garder ouverte, donc, ne concerne pas la technologie. Elle concerne la culture organisationnelle qui décide quand cette technologie est prête à opérer sans supervision sur des systèmes qui comptent. Sommes-nous prêts à accepter un logiciel qui ne se limite pas à suggérer, mais décide et exécute ? Et qui, dans cette chaîne de décision, a la responsabilité de répondre "non, pas encore" quand la pression commerciale dit le contraire ?

Neuf secondes. C'est le temps qu'il a fallu à un agent pour effacer des mois de travail d'une startup. Construire les systèmes qui empêchent le prochain agent de faire de même exige quelque chose de bien plus lent et moins spectaculaire : de la gouvernance, des protocoles, une culture de la vérification. Et la volonté collective de faire passer la robustesse avant la rapidité d'adoption.

## Les questions qui restent

Les questions ouvertes, à ce stade, sont plus utiles que les réponses précipitées. Qui certifie qu'un agent est prêt à opérer sur des systèmes de production sans supervision continue, et avec quels critères publics et vérifiables ?

Comment construire un système de logs qui permette l'attribution des responsabilités sans devenir un alibi pour rejeter la faute sur le dernier maillon de la chaîne ?

Et, peut-être la plus difficile : comment préserver la capacité critique des développeurs humains dans des organisations qui, pour des raisons économiques pas toujours compréhensibles, réduisent systématiquement le nombre de personnes qui surveillent les systèmes ?

L'incident PocketOS n'est la fin de rien. C'est un test décisif pour un secteur qui a encore la possibilité de choisir comment croître. La différence entre une industrie qui apprend de ses erreurs et une qui les externalise dépendra, dans les prochaines années, de la qualité de ces réponses.
