---
tags: ["Business", "Ethics & Society", "Security"]
date: 2026-01-09
author: "Dario Ferrero"
---

# 'Intelligence Artificielle et Ingénierie Logicielle : Ce que les entreprises doivent faire'. Conversation avec Enrico Papalini
![papalini-interview.jpg](papalini-interview.jpg)

*Enrico Papalini a un CV qui ferait pâlir de nombreux consultants sur LinkedIn : plus de vingt ans passés à construire et à orchestrer des systèmes logiciels où l'erreur n'est pas une option. En tant que responsable de l'excellence en ingénierie et de l'innovation à la Bourse italienne, qui fait partie du groupe Euronext, il a dirigé l'adoption de l'intelligence artificielle dans un contexte où le mot "crash" a des implications qui vont bien au-delà du simple bogue d'exécution. Auparavant, il a parcouru le secteur sous différents angles : de Microsoft à Intesa Sanpaolo, des startups technologiques aux géants financiers, toujours dans le rôle de celui qui doit faire fonctionner les choses quand tous les autres peuvent se permettre qu'elles ne fonctionnent pas.*

Son [profil LinkedIn](https://www.linkedin.com/in/enricopapalini/) retrace une trajectoire professionnelle où l'innovation a toujours dû se marier avec la fiabilité. Il n'est ni un universitaire qui théorise de l'extérieur, ni un fondateur qui peut se permettre le luxe du "move fast and break things". C'est quelqu'un qui a dû répondre à des questions du type : "Pouvons-nous utiliser cette technologie dans un système qui traite des millions de transactions par jour ?" La bonne réponse n'est jamais un oui enthousiaste ni un non conservateur, mais un "ça dépend, et je vais vous expliquer comment".

Aujourd'hui, Papalini a synthétisé cette expérience dans un livre qui fait débat : [*Intelligenza Artificiale e Ingegneria del Software: Cosa debbono fare le imprese*](https://amzn.to/3Z12Ng9), également publié en [version anglaise](https://www.amazon.com/dp/B0G7LPJBTH) sous le titre *Non-Deterministic Software Engineering: How to Build Reliable Software with AI Assistants Without Losing Quality, Security, or Control*. Le sous-titre est déjà un manifeste : comment construire un logiciel fiable avec des assistants IA sans perdre en qualité, en sécurité ou en contrôle.

## Le pacte silencieux rompu

Alors que le marché de l'édition technologique continue de produire des manuels sur "comment utiliser ChatGPT pour programmer plus rapidement", Papalini a choisi un angle complètement différent. Son livre s'appuie sur des recherches menées par DX auprès de plus de 180 entreprises, intègre les métriques DORA (DevOps Research and Assessment) adaptées au développement assisté par l'IA, et analyse les études de cas de ceux qui se sont déjà brûlé les ailes ou ont trouvé un équilibre : OpenAI, Shopify, Google. Pour l'écrire, il a dialogué avec certains des plus grands noms de l'ingénierie logicielle contemporaine : Martin Fowler, le théoricien des modèles de conception et du refactoring ; Kent Beck, l'inventeur de l'Extreme Programming ; Addy Osmani, directeur de l'ingénierie chez Google Cloud.

Je lui demande de me raconter ce qui l'a poussé à écrire ce livre, précisément maintenant, alors que tout le monde semble se concentrer sur la vitesse miraculeuse promise par les assistants IA.

"Tout le monde parle de vitesse, mais la vraie révolution est ailleurs", répond Papalini. "C'est un changement dans la nature des outils que nous utilisons. Pendant quarante ans, nous avons tenu une chose pour acquise : vous écrivez du code, et il fait exactement ce que vous avez écrit. Toujours. C'est sur cette certitude que nous avons tout construit, la façon dont nous testons, dont nous déboguons, dont nous travaillons en équipe. L'IA générative rompt ce pacte silencieux. Non pas parce qu'elle est défectueuse, mais parce qu'elle a une nature probabiliste. Vous lui demandez la même chose deux fois, elle vous donne des réponses différentes. Parfois géniales, parfois fausses avec une assurance désarmante."

La métaphore qu'il utilise pour cadrer le problème est éclairante : "Les entreprises qui pensent pouvoir remplacer les programmeurs par l'IA et qui se réjouissent du nombre de lignes de code supplémentaires qu'elles parviennent à produire passent à côté de l'essentiel : elles introduisent une variable aléatoire au cœur de leurs systèmes. C'est un peu comme si un ingénieur civil construisait un pont avec des matériaux qui *pourraient* supporter le poids prévu. Il fonctionne très bien lorsque quelques voitures y passent, mais lorsque le premier camion arrive, il s'effondre."

Il a écrit ce livre, dit-il, "parce qu'il me semblait qu'il manquait un guide pour ceux qui doivent naviguer ce changement sans se planter, mais aussi sans renoncer aux avantages, qui sont réels".

## Du déterminisme à la tolérance

Le cœur conceptuel du livre est résumé dans le titre anglais : *Non-Deterministic Software Engineering*. C'est un oxymore délibéré. L'ingénierie logicielle, par définition, a toujours été l'art de construire des systèmes déterministes : l'entrée A produit toujours la sortie B. Papalini propose d'accueillir dans nos processus des outils qui, par nature, ne respectent pas cette règle fondamentale.

Je lui demande comment le paradigme du contrôle qualité change lorsque nous passons d'un monde où le code faisait exactement ce qui était écrit, à un monde où nous accueillons des systèmes probabilistes dans nos IDE.

"Tout change, et en même temps, rien ne change. Je sais, ça ressemble à un paradoxe", commence-t-il. "Tout change parce que 'ça marche' ne signifie plus 'c'est correct'. Le code généré par l'IA compile, passe les tests que vous avez écrits, il a une apparence professionnelle. Mais il pourrait cacher des vulnérabilités, mal gérer les cas limites, ou être écrit d'une manière que personne ne comprendra dans six mois. Rien ne change parce que les fondamentaux de l'ingénierie logicielle restent les mêmes : les tests, les revues, la pensée conceptuelle. En fait, ils deviennent plus importants que jamais."

La clé, selon Papalini, réside dans l'adoption d'une approche qui a jusqu'à présent été étrangère aux développeurs de logiciels : "La vraie nouveauté, c'est que nous devons apprendre à raisonner en termes de 'tolérances'. Martin Fowler utilise souvent cette analogie : sa femme est ingénieur en structure, et elle ne conçoit jamais à la limite exacte. Elle calcule toujours une marge de sécurité. Nous, les développeurs, n'avons jamais eu à le faire parce que nos 'matériaux' étaient parfaitement prévisibles. Maintenant, ils ne le sont plus. Et ceux qui ne se construisent pas ces marges verront, tôt ou tard, leur 'pont' s'effondrer."

C'est un changement de mentalité radical pour toute une profession qui a bâti son identité sur la certitude absolue de l'exécution. C'est comme dire à un horloger suisse qu'à partir de maintenant, il devra accepter que ses montres puissent avoir une marge d'erreur variable.

## L'illusion de la vitesse

L'un des passages les plus contre-intuitifs du livre concerne les données sur la productivité. Papalini cite une étude de METR (une organisation indépendante qui évalue les capacités des systèmes d'IA) qui montre que les développeurs peuvent se sentir 20 % plus rapides avec l'intelligence artificielle, alors que les tests réels sur des tâches mesurables indiquent que dans certains cas, ils sont 19 % plus lents.

Je lui demande comment cet écart de perception est possible, et surtout comment les entreprises peuvent mesurer la productivité réelle sans tomber dans le marketing des outils.

"Vous savez ce qui m'a le plus frappé dans cette étude ? Ce n'est pas le fait qu'avec l'IA, ils étaient 19 % plus lents. C'est que les développeurs *croyaient* être plus rapides. Et ils ont continué à le croire même après avoir vu les résultats", raconte Papalini. "Pourquoi cela se produit-il ? Parce que l'IA réduit l'effort *perçu*. On se sent plus fluide, moins bloqué. C'est comme avoir un collègue toujours disponible pour vous aider, qui ne vous juge pas et ne vous fait pas attendre. Psychologiquement, c'est puissant. Mais 'je me sens productif' et 'je produis de la valeur' sont deux choses très différentes."

La solution qu'il propose n'est pas philosophique mais méthodologique : "Pour ne pas tomber dans le battage médiatique, une entreprise devrait établir une base de référence *avant* d'adopter les outils. Sans un 'avant', vous ne pourrez jamais prouver un 'après'. Lorsque le PDG demandera ce que l'IA a apporté, il faudra des chiffres, pas des sentiments. Mais les chiffres doivent être les bons : arrêtez de mesurer les lignes de code ou le nombre de suggestions d'IA acceptées. Mesurez ce qui compte : les fonctionnalités livrées, les bogues en production, le temps de résolution des incidents. Et une chose fondamentale : mesurez à quel point vos développeurs restent motivés."

C'est un appel à la discipline de l'ingénierie à une époque d'euphorie collective. Comme aux débuts des méthodologies Agiles, lorsque tout le monde mesurait la "vélocité" en points de récit sans se demander s'ils livraient réellement de la valeur.

## Lundi matin, trois actions

Le sous-titre italien du livre pose une question directe : "Ce que les entreprises doivent faire". Pas "ce qu'elles pourraient faire" ou "ce qu'il serait bien de faire", mais "ce qu'elles doivent faire". C'est un impératif, et cela implique une urgence.

Je demande à Papalini d'être encore plus direct : s'il devait indiquer les trois premières actions concrètes qu'un DSI ou un PDG devrait entreprendre dès lundi matin pour ne pas se laisser déborder, quelles seraient-elles ?

"La première est de faire un audit de ce qui se passe *déjà*", répond-il sans hésiter. "Je vous le garantis : vos développeurs utilisent déjà ChatGPT, Copilot, Claude, que vous le sachiez ou non. Non pas par méchanceté, mais simplement parce que ces outils fonctionnent. Avant d'écrire des politiques, comprenez la situation réelle."

Ce phénomène du Shadow AI, l'utilisation non autorisée d'outils intelligents, est l'un des thèmes récurrents du livre. Ce n'est pas un problème d'indiscipline mais de nécessité : lorsque les outils officiels sont lents à être approuvés ou trop limités, les gens trouvent des alternatives.

"La deuxième est de tracer une ligne claire entre l'exploration et la production", poursuit Papalini. "Le prototypage rapide, les expériences, les preuves de concept, tout cela est légitime. Mais il doit être *clair* que ce code ne part pas en production sans une réécriture consciente. Le désastre classique, c'est le prototype du vendredi qui devient le système critique du lundi parce que 'de toute façon, ça marche'."

C'est le schéma que quiconque a travaillé dans une startup reconnaît immédiatement : la démo devient le produit, la solution de contournement devient l'architecture, le temporaire devient permanent. Avec l'IA, ce processus s'accélère dangereusement car générer un prototype convaincant est une question de minutes.

"La troisième est d'investir dans la capacité de revue, pas dans la capacité de génération", conclut-il. "Le goulot d'étranglement n'est plus d'écrire du code, mais de le comprendre, de le valider, de le maintenir. Si vos développeurs peuvent générer dix fois plus de code mais que la capacité de revue reste la même, vous ne faites qu'accumuler de la dette technique plus rapidement."

## Le piège du "ça marche"

Andrej Karpathy, l'un des pionniers de l'IA moderne et ancien directeur de l'intelligence artificielle chez Tesla, a popularisé le terme "vibe coding" : programmer en suivant l'intuition du moment, en laissant l'IA suggérer des directions qui "semblent justes". C'est une approche fascinante et profondément dangereuse.

Papalini consacre plusieurs pages de son livre à ce qu'il appelle le "piège du ça marche". Je lui demande de me parler des risques à long terme pour une base de code d'entreprise écrite principalement en suivant le "vibe" du moment, sans une validation humaine rigoureuse.

"Je vais vous raconter une histoire", commence-t-il. "Martin Fowler avait utilisé l'IA pour générer une visualisation au format vectoriel SVG, rien de complexe. Cela fonctionnait parfaitement. Puis il a voulu faire une modification banale : déplacer une étiquette de quelques pixels. Il a ouvert le fichier et a trouvé ce qu'il a appelé 'un truc de fou', du code qui fonctionnait, oui, mais qui était structuré d'une manière complètement étrangère, impossible à toucher sans tout casser. La seule option ? Le jeter et le régénérer à partir de zéro."

L'anecdote illustre parfaitement le problème : "C'est le coût réel et le risque du 'vibe coding' à l'échelle de l'entreprise. Vous créez des systèmes qui *fonctionnent* mais que *personne ne comprend*. Et les logiciels d'entreprise doivent vivre des années, parfois des décennies. Ils doivent être modifiés, étendus, débogués à trois heures du matin quand quelque chose explose."

La solution qu'il propose est simple dans sa formulation mais exige de la discipline dans son exécution : "La règle que nous devons suivre est simple : ne jamais commiter du code que l'on ne sait pas expliquer à un collègue. S'il est généré par l'IA et que je ne comprends pas comment il fonctionne, il n'est pas prêt pour la production."

C'est l'équivalent numérique de la règle des alpinistes : ne montez sur rien dont vous ne savez pas descendre.

## Le prix du manque de fiabilité

Dans le livre, Papalini introduit le concept de "taxe sur le manque de fiabilité". C'est un coût caché mais mesurable de l'utilisation de systèmes génératifs dans la production de code. Je lui demande de quantifier, en termes concrets de sécurité et de maintenance, combien coûte réellement à une entreprise le nettoyage du code généré par l'IA qui semble correct mais qui cache des vulnérabilités.

"Les chiffres donnent à réfléchir", commence-t-il. "Les recherches montrent qu'un pourcentage significatif du code généré par l'IA contient des vulnérabilités, certaines sources parlent de près de la moitié. Et ce qui est insidieux, c'est que ce sont des vulnérabilités 'plausibles' : le code semble professionnel, il utilise des motifs reconnaissables. Sauf qu'il manque la validation des entrées à ce point critique, ou qu'il utilise une fonction cryptographique obsolète."

Il ne s'agit pas d'erreurs évidentes que n'importe quel linter signalerait. Ce sont des erreurs de jugement, des choix apparemment raisonnables qui, dans des contextes spécifiques, deviennent des failles de sécurité : "Le coût direct est le temps de remédiation. Mais le vrai coût est celui que l'on ne voit pas tout de suite : la vulnérabilité qui passe inaperçue pendant des mois, jusqu'à ce que quelqu'un la trouve. À ce moment-là, vous ne payez pas des heures de développement, vous payez la réponse aux incidents, une éventuelle violation de données, des dommages à la réputation."

Papalini identifie également un coût plus subtil : "Il y a aussi une taxe plus subtile : la perte de confiance dans le système. Lorsque l'équipe commence à ne plus faire confiance à son propre code, tout ralentit. Chaque modification devient un risque. Et il en va de même pour les clients : il y a un risque qu'ils passent à un concurrent plus fiable."

Sa recommandation est pragmatique : "L'investissement judicieux est dans la prévention : analyse de sécurité automatique, formation ciblée, revue humaine obligatoire pour tout ce qui touche à l'authentification ou aux données sensibles. Cela coûte moins cher que de nettoyer les dégâts après coup et de perdre des clients."

## La question de la souveraineté

L'un des chapitres les plus denses du livre aborde le thème de la souveraineté des données et de la sécurité à l'ère des assistants IA. Les entreprises sont confrontées à un triple défi : protéger la propriété intellectuelle de l'enfermement propriétaire, prévenir le Shadow AI et atténuer ce que Papalini appelle la "dette de sécurité" du code probabiliste.

Je lui pose une question complexe : entre la vitesse des modèles cloud et la complexité de l'open source sur site, quelle architecture stratégique recommande-t-il pour garantir la confidentialité et la sécurité sans que la protection des actifs ne devienne un coût insoutenable ?

"C'est un vrai défi, je le vis tous les jours dans le secteur financier. Et la réponse honnête est : cela dépend de votre profil de risque", commence Papalini. "Pour la plupart des entreprises, une approche hybride fonctionne : des modèles cloud pour le code non sensible, avec des règles claires sur ce qui peut sortir et ce qui ne le peut pas. Les principaux fournisseurs proposent désormais des options d'entreprise avec des garanties contractuelles sérieuses. Ceux qui ont des exigences plus strictes peuvent se tourner vers l'hébergement sur site avec des modèles open source. Llama, Mistral, DeepSeek ont des capacités remarquables. Le prix à payer est la complexité opérationnelle."

Mais il identifie une menace souvent sous-estimée : "Mais savez-vous quelle est la menace la plus sous-estimée ? Le Shadow AI : des développeurs qui utilisent des outils non autorisés parce que les outils officiels sont lents à être approuvés ou trop limités. La solution n'est pas d'interdire, mais d'offrir des alternatives légitimes suffisamment bonnes pour ne pas créer l'incitation à contourner les règles."

C'est une approche qui rappelle la réduction des risques dans les politiques de santé : au lieu de criminaliser des comportements inévitables, rendre disponibles des alternatives plus sûres.

## L'apprentissage à l'ère des machines

L'une des sections les plus provocatrices du livre concerne l'avenir de la formation et des compétences. Une distinction émerge entre les diplômés en informatique traditionnelle et la nouvelle figure de l'ingénieur IA, quelqu'un qui sait orchestrer des systèmes intelligents mais qui n'a peut-être jamais écrit un analyseur syntaxique à partir de zéro.

Je demande à Papalini si l'IA qui permet à n'importe qui de générer du code signifie la fin du programmeur "pur", ou si nous ne faisons que relever la barre des compétences architecturales nécessaires.

"Le programmeur n'est pas destiné à disparaître, mais son rôle change beaucoup", répond-il. "Pensez à ce qui s'est passé lorsque les langages de haut niveau sont arrivés. Les programmeurs en assembleur n'ont pas disparu, ils sont devenus des spécialistes de niche. Le gros du travail s'est déplacé un cran plus haut."

La transition actuelle, selon Papalini, suit un schéma similaire : "Quelque chose de similaire se produit maintenant. Une figure différente émerge, appelons-la un 'orchestrateur' : quelqu'un qui sait décomposer des problèmes complexes, spécifier des exigences avec précision, évaluer de manière critique ce que l'IA produit, prendre des décisions architecturales."

Mais c'est là que réside le paradoxe : "Le paradoxe ? Il faut *plus* d'expérience, pas moins. Un junior peut utiliser l'IA pour générer du code qui semble fonctionner. Mais seul un senior reconnaît quand ce code est une bombe à retardement, car il a vu suffisamment de catastrophes pour en reconnaître les signes."

Le risque systémique qu'il identifie est celui de l'atrophie des compétences : "Il faut également faire attention à ne pas penser que tout le monde naît orchestrateur : si nous déléguons tout le travail de 'formation sur le tas' à l'IA, comment formons-nous la prochaine génération de seniors ? Les données nous disent que l'emploi des plus jeunes développeurs est déjà en baisse. Mais même ceux qui entrent sur le marché risquent de ne jamais développer ces compétences profondes qui ne se construisent qu'en se cognant la tête contre les problèmes."

## La programmation en trio

Pour résoudre ce dilemme, Papalini propose dans son livre un modèle qu'il appelle la "programmation en trio", une évolution de la programmation en binôme qui inclut l'IA comme troisième acteur.

"Dans le livre, je propose la 'programmation en trio' comme solution au problème de la formation", explique-t-il. "Le junior travaille avec l'IA pour mettre en œuvre les fonctionnalités. L'IA accélère, suggère, génère du code. Jusqu'ici, rien de nouveau. L'orchestrateur senior n'écrit pas de code, il est là pour poser des questions. 'Explique-moi ce que fait cette méthode.' 'Pourquoi l'IA a-t-elle choisi cette structure de données ?' 'Que se passe-t-il si l'entrée est nulle ?' 'Comment gérerais-tu une erreur réseau ici ?'"

Le mécanisme est pédagogiquement brillant : "En répondant à ces questions, le jeune apprend. Le senior, de son côté, transmet ce savoir tacite qui ne se trouve dans aucun manuel, l'intuition de ce qui peut mal tourner, la sensibilité au code qui 'pue', l'expérience de celui qui a vu des systèmes s'effondrer."

C'est comme l'apprentissage dans les ateliers de la Renaissance : le maître ne peint pas à la place de l'élève, mais lui fait remarquer où la perspective est fausse, pourquoi ce mélange de couleurs ne tiendra pas, où la composition perd son équilibre.

## La valeur du jugement

Je reviens sur le thème de la monétisation et de la valeur. Papalini a écrit plusieurs articles sur Medium explorant comment les entreprises tentent de tirer profit de l'IA générative. Je lui demande : au-delà du logiciel, comment voit-il l'impact de l'IA générative sur le marketing et la création de produits numériques ? Est-ce seulement une question de vitesse ou la valeur même du produit est-elle en train de changer ?

"Oui, la valeur change, mais d'une manière contre-intuitive", répond-il. "Lorsque tout le monde peut générer du contenu, des images, du code, la *production* devient une marchandise. Elle est abondante, donc elle vaut moins. Ce qui prend de la valeur, c'est tout le reste : comprendre ce qui vaut la peine d'être construit, distinguer le médiocre de l'excellent, avoir une vision."

Dans le logiciel, dit-il, il le voit se manifester tous les jours : "Si n'importe qui peut générer une application fonctionnelle en un week-end, qu'est-ce qui distingue votre produit ? Ce n'est plus l'implémentation, c'est la compréhension du problème, l'expérience utilisateur, la capacité à évoluer dans le temps."

Et il en va de même pour le marketing : "L'IA peut produire une infinité de variantes de textes publicitaires, d'images, de vidéos. Mais 'infini' ne signifie pas 'efficace'. Il faut quelqu'un qui sache quoi tester, comment lire les résultats, quand s'arrêter."

La synthèse est élégante : "Nous entrons dans une ère d'abondance cognitive. Le goulot d'étranglement n'est plus de produire, c'est de choisir, de sélectionner, de juger."

C'est comme la transition de la rareté à la surabondance dans l'industrie musicale. Lorsque n'importe qui peut enregistrer et distribuer un album, la valeur passe de la capacité technique de production à la capacité artistique de créer quelque chose qui mérite l'attention.

## Agents autonomes et avenir proche

Nous passons des simples assistants de codage (les divers Copilots) aux systèmes agentiques autonomes, capables théoriquement de prendre des initiatives, de coordonner des tâches complexes, voire de déboguer leur propre code. Je lui demande quelle est sa vision de l'évolution des agents IA dans l'ingénierie logicielle au cours des cinq prochaines années. Verrons-nous des systèmes qui s'auto-réparent et s'auto-déploient ?

"Dans les 12 à 18 prochains mois, nous verrons l'orchestration d'agents devenir une pratique courante dans les entreprises les plus avancées", prédit Papalini. "Pas vingt agents en parallèle, ça, c'est pour les démos. Deux ou trois flux de travail gérés ensemble : un agent qui met à jour les tests, un qui migre les dépendances, un qui ajoute une fonctionnalité mineure. Tout cela pendant que le développeur se concentre sur le travail qui exige du jugement."

Mais il prévient : "Le mot clé est 'vérifiable'. L'attention humaine reste le goulot d'étranglement. Peu importe la vitesse de l'agent si ensuite il faut une semaine pour comprendre ce qu'il a fait."

À long terme, il est prudent : "Dans cinq ans ? Je suis prudent. Les agents qui 's'auto-réparent' existent déjà, les retours en arrière automatiques, les infrastructures auto-réparatrices. Mais des agents qui s'auto-déploient de manière totalement autonome ? Pour les systèmes critiques, j'en doute. Et je ne suis même pas sûr que nous devrions le vouloir."

Sa prédiction la plus solide concerne le rôle humain : "Ma prédiction la plus sûre : le rôle de l'ingénieur se déplace vers la spécification et la validation, moins vers l'implémentation. Mais ce changement exigera *plus* de compétences de la part des travailleurs, pas moins."

## L'atrophie des compétences

Il y a un thème qui traverse tout le livre : le risque que l'adoption massive de l'IA n'amplifie pas les capacités humaines mais les atrophie. C'est la question éthique et sociale qui se cache sous la surface de chaque considération technique.

Je lui demande directement : comment pouvons-nous garantir que l'adoption massive de l'IA dans les entreprises ne dévalorise pas le professionnalisme humain, mais devienne un véritable amplificateur des capacités des talents ?

"C'est la question qui me tient le plus à cœur", répond Papalini. "Le risque concret, je l'appelle 'l'atrophie des compétences'. Un ingénieur interviewé par le MIT Technology Review a raconté qu'après des mois d'utilisation intensive de l'IA, lorsqu'il a essayé de programmer sans, il se sentait perdu ; des choses qui étaient auparavant instinctives étaient devenues laborieuses. C'est exactement la sonnette d'alarme que nous devrions écouter."

La solution n'est pas le refus mais l'intentionnalité : "La solution n'est pas de refuser l'IA, ce serait comme refuser l'électricité. Mais nous devons être intentionnels sur la façon dont nous l'intégrons, en particulier dans les parcours de formation. C'est pourquoi, dans le livre, je propose des modèles comme la 'programmation en trio' pour cultiver la capacité des talents et ne pas commettre l'erreur de scier le barreau le plus bas de l'échelle par laquelle nous sommes montés, le processus d'apprentissage qui nous a amenés là où nous sommes."

## Au-delà du logiciel

À la fin de la conversation, je lui demande si un PDG d'une entreprise qui ne produit pas de logiciels peut trouver de la valeur dans son livre. C'est une question légitime : le titre parle explicitement d'ingénierie logicielle.

"Absolument, et je vais vous expliquer pourquoi", répond-il avec conviction. "Le logiciel a été le premier domaine à être massivement investi par l'IA générative, c'est donc le laboratoire où certains phénomènes se sont manifestés plus tôt et de manière plus mesurable. Mais les schémas que je décris dans le livre sont universels, ils concernent la relation entre les êtres humains et les systèmes probabilistes, et cela touche désormais tous les secteurs."

La généralisation est convaincante : "Prenons le concept central : le passage du déterminisme au non-déterminisme. Lorsque vous demandez à une IA d'écrire du code, vous ne savez pas exactement ce que vous obtiendrez. Mais il en va de même lorsque vous lui demandez d'écrire une campagne marketing, d'analyser un bilan, de rédiger un contrat ou de répondre à un client. Le résultat semble professionnel, il est formulé avec assurance, mais il pourrait être subtilement faux de manière que seul un expert reconnaît."

Papalini transpose chaque concept du livre hors du domaine du code : "Le 'problème des 70 %' fonctionne de manière identique dans tous les contextes. L'IA vous amène rapidement à une ébauche qui semble presque terminée — un rapport, une présentation, une analyse de marché. Mais ce 'presque' cache les 30 % où il faut des nuances, du contexte, du jugement. Le junior en marketing qui accepte le texte généré par l'IA sans comprendre pourquoi certains mots fonctionnent et d'autres non commet exactement la même erreur que le programmeur qui commet du code qu'il ne sait pas expliquer."

Le thème de la formation devient encore plus urgent : "Le 'piège de la compétence' est peut-être le thème le plus urgent pour tout PDG. Si vos analystes juniors délèguent à l'IA la construction des modèles financiers, ils n'apprendront jamais à les faire. Si vos jeunes avocats utilisent l'IA pour les premières ébauches sans jamais en écrire une à partir de zéro, ils ne développeront jamais l'intuition des risques contractuels. Vous économisez du temps aujourd'hui et vous détruisez de la compétence demain."

Même la programmation en trio se généralise : "La 'programmation en trio' que je propose devient le 'travail en trio' : un junior, un senior et l'IA qui travaillent ensemble. Le junior utilise l'IA pour accélérer, le senior pose les questions qui forcent la compréhension. Cela fonctionne pour former un analyste, un consultant, un chargé de clientèle, tout rôle où l'expertise se construit en faisant."

Et le problème de la gouvernance traverse toutes les fonctions de l'entreprise : "Et puis il y a le Shadow AI, des employés qui utilisent ChatGPT en secret parce que les outils officiels sont trop lents ou trop limités. Cela se produit partout : au service juridique, au service client, aux ressources humaines. Ce n'est pas un problème technologique, c'est un problème de gouvernance que tout PDG doit affronter."

La conclusion est pragmatique : "Le livre utilise le logiciel comme contexte, mais ce qu'il raconte, c'est l'histoire de la manière d'intégrer des outils puissants mais peu fiables dans le travail professionnel sans perdre en qualité, en compétences et en contrôle. C'est le défi de toute organisation aujourd'hui, qu'elle produise du code, des contrats, des campagnes publicitaires ou des analyses financières."

Et il ajoute une note finale qui sonne comme un manifeste : "Un PDG qui le lit ne trouvera pas d'instructions pour configurer Copilot, il trouvera un cadre pour réfléchir à l'adoption de l'IA qu'il pourra appliquer à n'importe quelle fonction de son entreprise. Et franchement, en ce moment de battage médiatique effréné et d'attentes démesurées, un peu de lucidité d'ingénieur peut faire du bien à quiconque doit prendre des décisions."

## De nombreuses réponses qui ouvrent de nombreuses questions

Nous terminons cette longue conversation. Papalini doit retourner s'occuper de systèmes qui déplacent des capitaux ; je dois transformer cette conversation en quelque chose de lisible. Mais le sentiment qui reste est celui d'avoir parlé avec quelqu'un qui regarde le même film que nous tous, juste avec quelques minutes d'avance.

Le livre [*Intelligence Artificielle et Ingénierie Logicielle*](https://amzn.to/3Z12Ng9) n'est pas un manuel technique, malgré son titre. Il ressemble plus à ces essais d'alpinisme écrits après une expédition particulièrement risquée : une carte des choses qui peuvent mal tourner, écrite par quelqu'un qui est revenu pour le raconter. À la seule différence que nous escaladons tous cette montagne, que cela nous plaise ou non, et que quelqu'un qui a déjà fait quelques tentatives peut être utile.

La vraie question n'est pas de savoir si nous utiliserons l'intelligence artificielle pour écrire du code, faire du marketing, analyser des données ou prendre des décisions. Nous l'utilisons déjà. La question est de savoir si nous parviendrons à le faire sans perdre en chemin les compétences qui nous ont permis d'y arriver. Et sur cette question, pour l'instant, la réponse reste ouverte.
