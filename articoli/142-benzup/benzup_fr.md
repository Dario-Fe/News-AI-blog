---
tags: ["Applications", "Ethics & Society", "Generative AI"]
date: 2026-06-22
author: "Dario Ferrero"
---

# BenzUp : j'ai créé une application sans écrire une seule ligne de code
![benzup.jpg](benzup.jpg)

*Il y a un moment précis où une idée cesse d'être un fantasme de bar pour devenir quelque chose de concret. Dans mon cas, ce moment a eu pour protagonistes, dans l'ordre : le coût de l'essence, un ingénieur américain agacé par une bière chère à Dublin, et un modèle d'intelligence artificielle accessible à quiconque possède une connexion internet. Le résultat s'appelle [BenzUp](https://benzup.netlify.app), c'est gratuit, ça ne fait rien de révolutionnaire, et c'est peut-être précisément pour cela que ça vaut la peine de le raconter.*

Ces dernières semaines, entre amis, collègues et connaissances, le thème du coût du carburant était devenu une présence fixe dans les conversations. Pas une nouveauté absolue, entendons-nous bien : le prix de l'essence a toujours été l'un des sujets nationaux par excellence, n'en déplaise à ceux qui voudraient parler d'autre chose. Mais la situation internationale actuelle avait encore fait monter le volume du débat, et on se retrouvait souvent à se demander où il valait mieux faire le plein, quels distributeurs étaient les plus honnêtes, s'il valait la peine de faire quelques kilomètres de plus pour économiser un peu. Des questions légitimes, auxquelles personne n'avait de réponse rapide et vérifiable.

Pendant ce temps, j'observais, je prenais mentalement note, et je ne faisais rien. Comme on fait avec la plupart des bonnes idées : on les laisse décanter jusqu'à ce que quelque chose arrive pour les débloquer.

## La Guinness arrive

Le déblocage est arrivé un matin sous la forme d'une nouvelle que je n'aurais jamais imaginé lire. Matt Cortland, ingénieur américain aux racines irlandaises basé à Londres, s'était retrouvé à payer 7,80 euros pour une pinte de Guinness dans un pub de Dublin. Un chiffre qui, pour qui connaît le rapport quasi sacré entre les Irlandais et leur bière nationale, est peu moins qu'une offense. En enquêtant, Cortland découvre que le Central Statistics Office irlandais avait cessé de surveiller les prix de la bière en 2011, laissant un vide informationnel de quatorze ans. Sa réaction ? Construire un agent vocal appelé Rachel, doté d'un accent nord-irlandais, qui, lors du week-end de la Saint-Patrick 2026, a téléphoné à environ 2 300 pubs dans les 32 comtés de l'île en posant une seule question : combien coûte une pinte de Guinness ? Le coût de l'opération complète : environ deux cents euros. Le résultat : le [Guinndex](https://guinndex.ai), une carte interactive des prix de la Guinness en Irlande, élaborée via Claude d'Anthropic à partir de plus de 1 200 réponses collectées. Prix le plus courant relevé : 5,50 euros la pinte. Record absolu : 11 euros au The Temple Bar Pub de Dublin, qui confirme sa vocation à plumer les touristes avec une cohérence presque admirable.

L'objectif déclaré de Cortland est explicite : « Je veux voir si nous pouvons collectivement abaisser le coût d'une pinte dans toute l'Irlande. » Le Guinndex est devenu une plateforme crowdsourcée ouverte, où n'importe qui peut signaler des prix et contribuer à le tenir à jour. Et quelques premiers signes de baisse des prix apparaissent, mais pour l'instant, il est difficile de les corréler à l'initiative.

L'histoire est sympathique, l'idée est brillante, l'exécution est élégante. Mais surtout, sa lecture a fait sauter le ressort qui attendait depuis des semaines. Si quelqu'un avait utilisé l'IA pour cartographier le prix de la bière dans toute l'Irlande en dépensant deux cents euros, je pouvais l'utiliser pour construire quelque chose d'utile aux automobilistes sans dépenser un seul centime. Je n'avais pas l'ambition de faire baisser le prix de l'essence, comme Cortland espérait faire baisser celui de la Guinness, mais au moins j'aurais pu donner une orientation rapide sur l'endroit où il valait mieux s'arrêter.
![screenshot-guinndex.jpg](screenshot-guinndex.jpg)
[Capture d'écran de Guinndex.ai](https://guinndex.ai/)

## Les données étaient déjà là, gratuites

Avant de se jeter à corps perdu dans le développement, quelques recherches en ligne s'imposent toujours. Et c'est là qu'arrive la première bonne surprise : le Ministère des Entreprises et du Made in Italy publie chaque matin, en format ouvert et téléchargeable par quiconque, les prix des carburants pratiqués par tous les distributeurs italiens. Deux fichiers CSV, mis à jour quotidiennement, contenant l'annuaire complet des installations actives sur tout le territoire national, avec adresse, coordonnées GPS, gestionnaire et enseigne, et les prix communiqués par les gestionnaires, distingués par type de carburant et par mode de distribution, libre-service ou servi. Les données sont publiées sous licence IODL 2.0, qui autorise la réutilisation libre même à des fins commerciales, à condition de citer la source. Le Ministère ne se limite pas à tolérer l'utilisation de ces données : il l'encourage activement.

C'était exactement ce dont j'avais besoin. Pas de scraping, pas de zones grises légales, pas de dépendance vis-à-vis d'API tierces qui pourraient changer les conditions d'utilisation du jour au lendemain. Des données officielles, ouvertes, mises à jour chaque matin.

À ce stade, j'ai décidé de rester petit et focalisé : pas d'application nationale, pas d'ambitions d'échelle. Juste ma province, le VCO (le sigle VB dans les données du Ministère), filtrée et servie de manière simple et rapide. Un prototype léger pour voir si la chose fonctionnait vraiment.

## Le prompt comme acte de conception

Quiconque travaille avec l'IA de manière même semi-régulière sait que la qualité de la sortie dépend de manière déterminante de la qualité de l'entrée. Un prompt vague produit des résultats vagues. Ceci n'est pas un article sur le prompting, mais il vaut la peine d'y consacrer un paragraphe, car c'était la partie la plus artisanale de toute l'expérience.

J'ai défini les exigences avec une certaine précision. Sur le plan technique : une web app en HTML, CSS et JavaScript pur, avec une fonction serverless sur Netlify pour gérer les appels au MIMIT et éviter les problèmes de CORS qui empêchent les navigateurs de faire des requêtes directes à des domaines externes, un design responsive optimisé pour mobile, un filtrage des données sur la province du VCO, deux classements ordonnés par prix du moins cher au plus cher, un pour l'essence et un pour le gazole. Sur le plan de l'interface : un toggle visible pour passer d'un carburant à l'autre, les informations essentielles pour chaque distributeur, un panneau de détail accessible en touchant chaque station, la date de référence et la source mises en évidence. Sur le plan esthétique : un style moderne, une typographie soignée, une palette sobre, quelque chose qui ait l'air conçu et non généré.

J'ai délibérément choisi d'utiliser Claude Sonnet 4.6, la version accessible gratuitement, précisément parce que je voulais tester ce qu'il était possible de faire avec les outils à la disposition de tous, et pas seulement de ceux qui ont un abonnement premium ou des compétences de développeur senior. Si cela fonctionnait avec le modèle gratuit, l'histoire avait du sens aussi pour ceux qui lisent sans background technique.

En un couple de minutes, environ 750 lignes de code. Un fichier HTML avec tout inclus : structure, style, logique, gestion des erreurs, animations, panneau de détail avec swipe pour le fermer. Il m'était déjà arrivé d'utiliser des modèles d'IA pour écrire de petits morceaux de code, quelques fonctions, un composant isolé. Jamais cependant quelque chose de cette complexité en un seul coup. La première surprise a été d'ouvrir ce fichier dans le navigateur du PC : tout fonctionnait exactement comme je l'avais décrit. Mise en page correcte, toggle entre essence et gazole, panneau de détail, animations fluides. Évidemment sans données réelles, mais la structure était exactement celle demandée.

## Du navigateur à la production

Avoir un fichier HTML qui fonctionne en local est une chose. L'avoir en ligne, avec des données réelles provenant du Ministère, en est une autre. C'est l'étape où une familiarité minimale avec les outils disponibles a fait la différence.

J'ai créé un dépôt sur GitHub, chargé les fichiers, lié le dépôt à mon compte Netlify. Netlify a détecté automatiquement la configuration, a activé la fonction serverless qui télécharge et filtre les CSV du MIMIT, et en quelques minutes l'application était en ligne. Deuxième surprise : ça fonctionnait. Les données arrivaient, les distributeurs de la province VB apparaissaient classés par prix, le toggle entre essence et gazole répondait comme prévu.

À ce stade, j'ai fait une chose que je conseille toujours lorsqu'on travaille avec du code généré par l'IA : un contrôle croisé avec un autre outil. J'ai connecté Jules, l'agent IA asynchrone de Google intégré directement dans GitHub, et je lui ai demandé une analyse du code. Jules n'a pas signalé de problèmes importants, ce qui n'est pas une garantie absolue mais constitue tout de même une deuxième paire d'yeux informatiques sur le travail accompli.

Avec Jules, j'ai ensuite apporté quelques intégrations pour rendre l'application plus semblable à une application native. Un fichier manifest JSON a été ajouté pour permettre l'installation sur le téléphone directement depuis le navigateur, sans passer par les stores, ainsi qu'une icône personnalisée et une page dédiée aux informations utiles, expliquant le fonctionnement, la provenance des données, les limites du système et les instructions d'installation sur Android et iPhone. Cette page, comme nous le verrons, s'est révélée plus importante que prévu.
![benzup-screenshot.jpg](benzup-screenshot.jpg)
[Capture d'écran de BenzUp](https://benzup.netlify.app)

## Les limites font partie du produit

Un jour de test personnel, puis la diffusion à un cercle d'amis avec la demande explicite de signaler tout problème. Les retours ont été positifs, mais un signalement récurrent est arrivé : les prix de certains distributeurs semblaient bloqués depuis des jours. Aucun bug de l'application, simplement la réalité du système : les gestionnaires sont tenus par la loi de communiquer les variations de prix au Ministère, mais tous ne le font pas quotidiennement. De plus, les données sont publiées chaque matin en référence à 8h00 la veille, et la mise à jour effective dans l'application peut être décalée de quelques heures en raison des délais de publication du Ministère et de l'infrastructure technique sur laquelle l'application est hébergée, sur laquelle je n'ai pas de contrôle direct.

Ce signalement a conduit à améliorer la page d'information, en ajoutant une explication claire de ces mécanismes et en indiquant qu'en touchant la fiche d'un distributeur individuel, on peut vérifier la date de la dernière mise à jour envoyée au Ministère. La transparence n'est pas une option, elle fait partie intégrante d'un service basé sur des données publiques et qui n'a aucun intérêt à paraître plus précis qu'il ne l'est.

Une demande précise est également arrivée : ajouter le GPL et le méthane, des carburants qui, pour de nombreux automobilistes de la province, sont loin d'être secondaires. Dans les jours suivants, je les ai intégrés, et maintenant BenzUp affiche les classements pour les quatre types de carburant.

## Trois jours, 800 visites

L'application est en ligne depuis trois jours au moment où j'écris cet article (11 avril 2026). Je l'ai lancée avec un billet sur le blog local que je gère depuis de nombreuses années, [Verbania Notizie](https://www.verbanianotizie.it), sans publicité payante, sans campagne, sans stratégie de croissance. En trois jours, environ 800 visites. Des chiffres insignifiants à l'échelle nationale, probablement non pertinents même à l'échelle locale si on les mesure avec les paramètres du marketing numérique. Mais là n'est pas la question.

La question est qu'entre une idée née dans une conversation sur le prix du carburant et une application fonctionnelle en production, consultée par des centaines de personnes réelles de ma province, il s'est écoulé moins d'une semaine. Sans écrire une ligne de code, sans budget, sans équipe de développement. Avec une connaissance de l'écosystème des outils numériques gratuits disponibles, un prompt construit avec soin, et la volonté d'itérer, de corriger, d'améliorer sur la base de retours réels.

## Mises à jour

Cet article a eu le plaisir d'être publié dans le magazine de Codemotion. Je le republie donc aujourd'hui sur le portail, deux mois après sa rédaction. Une brève mise à jour s'impose.

Au cours des deux mois écoulés depuis la publication de cet article, BenzUp a continué d'évoluer, toujours fidèle à sa philosophie : gratuité, infrastructure simple et développement entièrement basé sur des outils gratuits existants.

Le développement le plus significatif est son extension géographique : l'application couvre désormais l'ensemble du Piémont, avec ses huit provinces et la possibilité de filtrer par commune via un menu dédié. D'un outil hyperlocal conçu pour les conducteurs de la zone VCO, elle est devenue une référence pour tous ceux qui voyagent dans la région ou y transitent.

Sur le plan technique, l'architecture a été profondément remaniée. Les données ne sont plus traitées en temps réel à chaque requête, mais pré-générées chaque matin dans des fichiers statiques servis directement depuis le CDN Netlify, ce qui a un impact immédiat et mesurable sur la vitesse de chargement. Une action GitHub planifie automatiquement le processus, vérifie que le Ministère a bien publié des données mises à jour avant de poursuivre, et génère un fichier JSON pour chaque province. L'interface utilisateur lit le fichier correspondant et l'affiche instantanément, sans utiliser de fonctions serveur.

Un système de feux tricolores a également été ajouté pour indiquer la fraîcheur des données de chaque distributeur : vert si le prix a été mis à jour au cours des dernières 24 heures, jaune au cours des 48 heures et rouge ensuite. Ce système simple et visuel permet aux utilisateurs d'accéder à des informations qui nécessitaient auparavant de consulter la page détaillée de chaque distributeur.

Enfin, un formulaire de signalement, accessible depuis la page de chaque distributeur, permet aux utilisateurs de signaler toute anomalie, tout prix obsolète, toute usine fermée ou toute erreur de données. Cette modeste contribution à la qualité collective est cohérente avec le caractère volontaire et transparent du projet.

## Considérations finales

Ceci n'est pas un hymne au vibe coding, cette pratique consistant à générer du code de manière rapide et approximative en faisant aveuglément confiance à l'IA sans comprendre ce que l'on fait. Le vibe coding semble d'ailleurs déjà en passe d'être dépassé par une approche plus structurée et professionnelle : écrire les spécifications du projet dans des fichiers markdown détaillés, à transmettre aux agents de code comme instructions précises et vérifiables, au lieu de se fier à des prompts improvisés. J'en ai parlé dans un [article sur ce même portail](https://aitalk.it/it/codespeak.html), et la différence en termes de contrôle et de qualité du résultat est substantielle. Mais c'est vraiment une autre histoire. Ce que je veux raconter est quelque chose de plus simple et peut-être de plus intéressant : l'IA a réduit de manière radicale la distance entre l'idée et sa réalisation, même pour ceux qui n'ont pas de compétences spécifiques en programmation.

Cela ne signifie pas que les programmeurs, ingénieurs et architectes logiciels soient devenus des figures superflues, bien au contraire. Porter un prototype fonctionnel en production est une chose, construire quelque chose de stable, sûr et évolutif en est une autre : pour cela, il faut des compétences réelles, de l'expérience et une compréhension profonde des systèmes qu'aucun prompt, aussi bien construit soit-il, ne peut remplacer.

Dans mon cas, une certaine aisance avec les outils en ligne et une curiosité d'utilisateur averti, non d'expert, ont permis de porter le projet en production au lieu de l'arrêter au stade de prototype. Mais le seuil s'est abaissé pour tous. Quiconque possède une idée claire, la patience de construire un prompt décent, et l'envie d'apprendre les mécanismes minimaux de déploiement sur des plateformes comme Netlify ou Vercel, peut faire de même.

Quelque part dans le monde, quelqu'un avec la bonne idée, un peu d'esprit d'entreprise et un compte gratuit sur Claude est probablement en train de construire en ce moment même quelque chose qui n'existe pas encore. Pas le nouveau Facebook, peut-être, mais quelque chose d'utile pour les gens qui l'entourent. Et cela me semble déjà suffisant.

En attendant, si vous êtes automobiliste du Piemonte (pour l'instant) et que vous voulez savoir où faire le plein en dépensant moins, [BenzUp est là](https://benzup.netlify.app) qui vous attend. Gratuit, indépendant, avec toutes ses limites bien déclarées.

Et s'il devait percer et se terminer par un rachat à plusieurs milliards par une big tech de la Silicon Valley, je vous attends tous à la grande fête que je donnerai dans ma méga villa sur les rives du lac Majeur car, même richissime, je resterai fidèle à là où tout a commencé.
