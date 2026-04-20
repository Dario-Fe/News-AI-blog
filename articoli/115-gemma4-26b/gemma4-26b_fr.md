---
tags: [" Generative AI", "Applications", "Training"]
date: 2026-04-20
author: "Dario Ferrero"
---

# Gemma 4 en local : 26 milliards sur mon PC
![gemma4-26b.jpg](gemma4-26b.jpg)

*Il y a une satisfaction particulière à faire tourner quelque chose qu'il serait déconseillé de télécharger. Pas la satisfaction du hacker qui force un système, ça c'est autre chose, mais celle, plus tranquille et artisanale, de celui qui serre les vis un peu au-delà du couple recommandé et découvre que la structure tient quand même. C'est le type de satisfaction que j'ai trouvé cette semaine, alors que Gemma 4 26B tournait sur mon PC grand public avec une fluidité que je n'attendais pas.*

Cet article est le deuxième d'une série que j'ai [commencée il y a quelques semaines avec Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1.html). Si vous avez lu ce texte, vous pouvez sauter le paragraphe suivant. Si, en revanche, vous êtes ici pour la première fois, je vous donne rapidement les coordonnées du projet.

## Le laboratoire, déjà connu

L'idée est simple : prendre des modèles ouverts tout juste publiés, les exécuter en local sur du matériel grand public, et comprendre ce que l'on obtient réellement, en dehors des communiqués de presse et des benchmarks marketing. L'outil est [LM Studio](https://lmstudio.ai/), une application de bureau qui permet de télécharger et de lancer des modèles sans ouvrir de terminal, avec la caractéristique très utile d'afficher à l'avance une estimation des performances attendues sur sa propre configuration matérielle. Un indicateur chromatique, vert-orange-rouge, qui épargne des heures de tentatives infructueuses. La machine est un PC assemblé avec discernement mais sans excès : processeur AMD Ryzen 7700, 32 Go de RAM DDR5, et un GPU AMD Radeon RX 9060 XT avec 16 Go de VRAM. Du matériel d'utilisateur averti, pas un laboratoire de recherche.

La méthode, je le réitère ici comme je l'ai fait en ouverture de l'article sur Qwen, n'est pas scientifique au sens académique du terme. Il n'y a pas de protocole examiné par des pairs, il n'y a pas d'échantillon de prompts statistiquement significatif, il n'y a pas de reproductibilité certifiée par une conférence. Les tests ont été vérifiés en croisant les résultats avec des modèles de pointe comme Claude et DeepSeek, mais cela ne les transforme pas en benchmarks : ils restent des essais sur le terrain, menés avec les outils d'un utilisateur exigeant. Les notes qui accompagnent chaque test sont des évaluations personnelles, pas des sentences.

## Gemma 4 : la famille, l'architecture, la philosophie

Google DeepMind a publié Gemma 4 le 2 avril 2026, sous licence Apache 2.0. Ce n'est pas un détail secondaire : c'est la première fois dans l'histoire de la famille Gemma qu'un modèle est publié sous cette licence, ce qui élimine toute ambiguïté sur l'usage commercial et place Gemma 4 sur le même plan permissif que Qwen 3.5, avec lequel il partage l'écosystème open-weight.

La famille s'articule autour de quatre variantes : E2B et E4B, conçues pour le déploiement sur des appareils mobiles et périphériques avec une fenêtre de contexte de 128 000 jetons, et les deux variantes majeures, le 26B MoE et le 31B Dense, avec une fenêtre de contexte de 256 000 jetons. Le 31B Dense est le modèle phare en termes de qualité brute, et au moment de son lancement, il a conquis la troisième position mondiale sur le classement Arena AI text leaderboard, non pas parmi les modèles ouverts, mais parmi tous les modèles absolus. Le 26B MoE s'est classé à la sixième place.

Sur le 26B MoE, il vaut la peine de consacrer deux lignes à l'architecture, je promets d'être bref. Le concept clé à garder à l'esprit pour lire le reste de cet article est unique : le modèle 26B n'active lors de l'inférence qu'environ 3,8 milliards de ses paramètres totaux, ce qui le rend nettement plus rapide que ce que le nombre global suggérerait, le rapprochant en termes de vitesse d'un modèle de 4 milliards de paramètres. Le prix à payer est que les 26 milliards de paramètres doivent tout de même tenir en mémoire. Rapide comme un petit modèle, lourd comme un grand : une facture qui se paie en VRAM.

Les chiffres des benchmarks sont impressionnants, en particulier par rapport à la génération précédente. Le bond par rapport à Gemma 3 est difficile à ignorer : sur AIME 2026, on passe de 20,8 % à 89,2 %, sur LiveCodeBench de 29,1 % à 80,0 %, sur GPQA Science de 42,4 % à 84,3 %. Ce n'est pas une optimisation incrémentale. Quelque chose de structurel a changé dans la façon dont ces modèles raisonnent.
![grafico1.jpg](grafico1.jpg)
[Image tirée de deepmind.google](https://deepmind.google/models/gemma/gemma-4/)

## Le choix au-delà de la limite

En venant à mon expérience spécifique, j'ai choisi de tester le **Gemma 4 26B A4B Instruct Q4_K_M**, la version avec la quantification la plus agressive disponible pour la variante de 26 milliards. Le choix était délibérément à la limite : LM Studio signalait cette configuration comme étant légèrement en dehors des capacités recommandées pour mon matériel, l'indiquant avec cette couleur orange qui suggère habituellement de revoir ses attentes à la baisse ou de redimensionner son choix. J'ai ignoré le conseil, non par entêtement, mais parce que tester la limite était précisément le but.

La quantification Q4_K_M réduit la précision numérique des poids du modèle de 16 bits à environ 4 bits, avec une technique qui cherche à distribuer la perte d'information de manière moins uniforme et plus intelligente que les quantifications plates, en préservant mieux les poids que le modèle considère comme les plus importants. Le résultat pratique est un fichier qui occupe environ 16 Go sur disque et peut s'appuyer entièrement sur les 16 Go de VRAM de mon GPU, un équilibre à la limite : la Q4_K_M sur le modèle 26B MoE utilise approximativement 16 Go, tout juste dans les limites d'un GPU grand public comme le mien. La perte de qualité par rapport à la version complète en bfloat16 est réelle, mais à quel point ? C'est l'un des sous-entendus de toute l'expérience.

J'ai délibérément choisi les six mêmes tests que ceux utilisés avec Qwen 3.5, non pas parce que les deux modèles sont comparables au sens strict (l'un est un 9B dense, l'autre un 26B MoE), mais pour maintenir une cohérence méthodologique minimale permettant au moins des observations qualitatives. Ce n'est pas une confrontation directe. C'est plutôt comme mesurer la température avec le même thermomètre dans deux villes différentes : les chiffres sont comparables, les villes non.

## Six essais, six verdicts

### Raisonnement scientifique : le mécanisme de Higgs — 5/5

Le premier test est celui que j'utilise comme thermomètre général de l'intelligence du modèle : expliquer le mécanisme de rupture de la symétrie électrofaible dans le Modèle Standard, le rôle du champ de Higgs, et pourquoi les bosons W et Z acquièrent une masse alors que le photon n'en a pas. Demande explicite : langage précis mais accessible à un étudiant universitaire en physique.

La réponse m'a surpris, non pas tant par la justesse des contenus que par la qualité de l'exposition. Le modèle a organisé l'explication en quatre sections logiques avec la structure qu'utiliserait un bon enseignant universitaire, en partant de l'invariance de jauge, en passant par le potentiel en « chapeau mexicain » avec la condition sur le signe du terme de masse, jusqu'aux conséquences physiques concrètes. Les formules étaient correctement rapportées, le groupe de jauge SU(2)_L × U(1)_Y, la valeur attendue dans le vide, les masses des bosons. Mais la véritable force résidait dans la capacité à accompagner chaque formule d'une image mentale compréhensible. Quand le modèle écrivait que les degrés de liberté angulaires sont « mangés » par les bosons de jauge, il traduisait un concept mathématique abstrait en quelque chose qu'un physicien de deuxième année reconnaît immédiatement. C'est la différence entre un dictionnaire et un professeur.

Un détail technique mérite d'être signalé : malgré la complexité du raisonnement et la longueur de la réponse, le modèle a raisonné pendant seulement 2,2 secondes et a généré le texte à environ 24 jetons par seconde. Pour un modèle qui pèse théoriquement 26 milliards de paramètres, c'est une vitesse surprenante, rendue possible précisément par l'architecture MoE qui maintient inactive la majeure partie des poids pendant la génération. **Note : 5/5.**

### Multimodalité : lire une feuille de calcul floue — 5/5

Le deuxième test était conçu pour mettre à l'épreuve les capacités visuelles avec une entrée délibérément difficile : une petite photo peu nette d'un tableur pour le budget familial mensuel, avec la demande de décrire le contenu, les données principales et les tendances émergentes.

Le modèle a mis environ dix secondes pour analyser l'image, un temps sensiblement plus long que pour le test précédent, compréhensible pour une tâche visuelle, avant de lancer la génération à environ 23 jetons par seconde. La réponse était remarquablement complète : il a correctement identifié la structure du document, un modèle Excel avec des sections pour les revenus, l'épargne et les dépenses, chacune avec des colonnes Budget, Réel et Différence. Il a lu les valeurs numériques clés avec une précision millimétrique : épargne nette mensuelle avec un budget prévu de 1 350 dollars, réel de 2 624 dollars, différence positive de 1 274 dollars. Il a même remarqué la présence d'un graphique à barres horizontales sur la droite de la feuille.

Mais la partie qui a confirmé qu'il ne s'agissait pas d'une simple transcription était l'analyse : le modèle a observé de manière autonome que malgré l'augmentation des revenus, les dépenses totales réelles étaient restées proches du budget prévu, et en a tiré une conclusion logique sur l'efficacité de l'épargne. D'une image floue à une analyse de flux de trésorerie. **Note : 5/5.**
![grafico3.jpg](grafico3.jpg)
Image tirée de mon PC lors des tests sur LMStudio

### Code : un problème NP-hard avec autocorrection — 4,5/5

Le troisième test était le plus technique : implémenter en Python un algorithme pour trouver le cycle de longueur maximale dans un graphe non orienté, en gérant les graphes avec des cycles multiples et en expliquant la complexité temporelle.

Les aspects positifs étaient notables. Le modèle a déclaré sans hésiter que le problème est NP-hard, qu'il n'existe pas d'algorithme polynomial pour le résoudre sur des graphes génériques, et a choisi le backtracking avec recherche en profondeur comme approche correcte, celle qu'utiliserait toute personne ayant étudié les algorithmes sérieusement. La représentation par liste d'adjacence avec dictionnaire était efficace, la logique d'exploration des chemins simples correcte, l'explication de la complexité temporelle claire et honnête.

Toutefois, la première version du code contenait trois erreurs syntaxiques : un mot-clé écrit `not be in` au lieu de `not in`, un nom de variable erroné dans un appel de méthode, et une autre variable mal orthographiée dans le contrôle de la condition de boucle. Trois erreurs qui, à elles seules, auraient empêché l'exécution sans intervention manuelle.

C'est ici qu'intervient la partie la plus intéressante de l'évaluation. Quand j'ai demandé au modèle, de manière générique et sans indiquer quelles étaient les erreurs, de vérifier le code pour d'éventuels problèmes de syntaxe, il a identifié et corrigé les trois dès la première tentative. En d'autres termes, il savait déjà comment le code correct devait être écrit : il ne l'avait tout simplement pas écrit avec assez d'attention la première fois. Ce comportement reflète l'utilisation réaliste de ces outils : un programmeur se fie rarement aveuglément à la première version générée. La capacité à diagnostiquer ses propres erreurs sur une sollicitation générique est presque aussi précieuse que l'écriture initiale parfaite. Presque. **Note : 4,5/5.**

### Multilingue et planification : le Japon en français — 4,8/5

Le quatrième test évaluait les capacités multilingues et la planification complexe : agir en tant qu'agent de voyage, planifier un itinéraire de cinq jours au Japon pour un client français ne parlant pas anglais, avec un focus sur les temples historiques et la cuisine de rue, plus une section finale en italien avec des conseils pour un touriste italien.

Le français était impeccable, fluide et sans erreurs, avec un ton professionnel mais pas froid. La planification de l'itinéraire était logistiquement réaliste : le premier jour à Asakusa avec le Senso-ji et une izakaya le soir, le deuxième entre le sanctuaire Meiji-jingu et Shibuya, le troisième en shinkansen vers Kyoto avec le Kiyomizu-dera et Gion, le quatrième au Pavillon d'Or et à la forêt de bambous d'Arashiyama, le cinquième au Fushimi Inari. Chaque journée était équilibrée entre site historique et expérience gastronomique, comme demandé. La connaissance du Japon était étonnamment détaillée : citations de lieux comme Sannenzaka et Ninenzaka, plats spécifiques comme les Age-manju, conseils pratiques sur la carte Suica et sur l'application Japan Transit, mention des Depachika, les sous-sols des grands magasins japonais, un détail d'initié que l'on ne trouve pas dans les guides touristiques génériques.

Cependant, la section finale en italien présentait deux erreurs qui ne peuvent être ignorées. La première était « suggeramenti » au lieu de « suggerimenti », un terme qui n'existe tout simplement pas en italien. La seconde était plus étrange : le mot « comprare » (acheter) apparaissait écrit avec une désinence cyrillique, « compraть », comme si le modèle avait momentanément perdu le fil de la langue. Deux erreurs en cent cinquante mots d'italien, sur une langue qui n'est pas parmi les plus rares au monde. Pour un modèle qui déclare supporter plus de 140 langues, on s'attendrait à une plus grande robustesse, même dans les langues secondaires d'une réponse. **Note : 4,8/5.**
![grafico2.jpg](grafico2.jpg)
[Image tirée de deepmind.google](https://deepmind.google/models/gemma/gemma-4/)

### Contexte long : 460 pages d'IA du premier coup — 5/5

Le cinquième test est celui que je considère comme le plus significatif pour une utilisation réelle du modèle : j'ai chargé l'[AI Index Report 2025 de Stanford](https://aiindex.stanford.edu/report/), un PDF d'environ 460 pages et plus de 20 millions de caractères, le même document utilisé dans le test avec Qwen 3.5. J'ai demandé au modèle, de manière générique, de me parler de la croissance de la génération vidéo et de m'indiquer les pages où trouver les données.

La réponse est arrivée après 4,4 secondes de traitement, à 22 jetons par seconde. Le modèle a correctement identifié les pages 125, 126 et 127, non pas un renvoi vague au « chapitre central », mais des références précises et vérifiables. Il a ensuite fourni une synthèse structurée des contenus : Stable Video Diffusion de Stability AI, Sora d'OpenAI présenté en février 2024 et rendu public en décembre, Movie Gen de Meta avec des capacités d'édition et d'intégration audio, Veo et Veo 2 de Google. Il a même cité le célèbre exemple du prompt « Will Smith eating spaghetti », ce test devenu un mème de la communauté IA pour documenter les progrès de la génération vidéo.

La comparaison avec l'expérience sur Qwen 3.5 est éclairante : le modèle de 9 milliards avait nécessité quatre tentatives et une sollicitation explicite pour répondre dans le chat afin d'obtenir un résultat similaire. Gemma 4 a répondu du premier coup, sans hésiter. La fenêtre de contexte de 256 000 jetons s'est révélée être non seulement une spécification technique mais une capacité réellement utilisable sur du matériel grand public. **Note : 5/5.**

### Raisonnement spatial : la chambre en plein chaos — 4,9/5

Le dernier test était celui que j'aime le plus car il mesure quelque chose de difficilement standardisable : l'intelligence visuo-spatiale. J'ai chargé une photo d'une pièce en grand désordre, la même que celle utilisée avec Qwen 3.5, et j'ai demandé de décrire la disposition des objets et de suggérer comment ranger pour créer plus d'espace. Le modèle a mis 7,5 secondes pour traiter, le deuxième temps le plus long de tout le test.

La réponse s'ouvrait sur une phrase que je n'ai pas comprise : « Aucune citation n'a été trouvée dans les fichiers de l'utilisateur pour cette requête. » Une phrase hors contexte, comme si le modèle avait activé un mécanisme de recherche documentaire qui n'avait rien à voir avec la tâche visuelle. Une fois passée cette bizarrerie initiale, le reste de la réponse était cependant excellent.

La description était précise : lit double sur la droite avec des draps blancs partiellement couverts, deux bibliothèques hautes et étroites positionnées correctement par rapport à la fenêtre et au bureau, bureau gris sur la gauche, deux fenêtres avec des rideaux à rayures verticales. Mais la partie vraiment impressionnante était la description des objets au sol : vêtements éparpillés, chaussures dont une paire de tongs, sacs, paniers à linge, et le détail qu'un des paniers était bleu avec des motifs. Ce niveau d'observation fine est remarquable.

La seule petite imprécision concernait le miroir : le modèle le plaçait sur une armoire ou une commode, alors que sur la photo il était monté sur la porte d'entrée. Une erreur compréhensible dans une image bidimensionnelle où la distinction entre porte et armoire peut être ambiguë.

Le plan de rangement était logique et bien motivé : d'abord les vêtements et les tissus sur le sol car ils sont l'obstacle principal à la circulation, puis les paniers et les sacs vers une zone dédiée, enfin le bureau et les bibliothèques pour réduire le sentiment d'encombrement visuel. La priorité accordée à « libérer la surface de passage » était correcte et pratique. **Note : 4,9/5.**
![tabella-confronto.jpg](tabella-confronto.jpg)

*Juste pour le plaisir, vu l'impossibilité de comparaison compte tenu de la taille et des caractéristiques différentes, je vous propose un tableau où vous pouvez faire vos propres évaluations et choix selon le matériel à disposition. Bien que de tailles différentes, les résultats sont très similaires, avec des préférences pour l'un ou l'autre selon la tâche ; je dois toutefois ajouter que lors d'utilisations ultérieures, Qwen 3.5 9b a montré des situations de blocage et de non-réponse, ce que Gemma 4 26b n'a pas montré.*

## Ce qu'il en reste

La moyenne arithmétique des six tests est de 4,87 sur 5. Un chiffre qu'il faut contextualiser avec honnêteté.

Nous parlons d'un modèle de 26 milliards de paramètres au total, quantifié dans sa version la plus compressée, exécuté sur du matériel grand public légèrement sous-dimensionné par rapport aux spécifications recommandées, en local, sans cloud, sans API, sans coût par jeton. Le fait qu'il tourne de manière fluide à des vitesses qui rendent l'interaction réactive est déjà en soi un résultat remarquable. Le fait qu'il réponde avec cette qualité en fait quelque chose de plus intéressant.

La comparaison avec Qwen 3.5 9B, le sujet du test précédent, n'est pas directe en raison de la différence de taille, mais certaines observations qualitatives émergent clairement. Gemma 4 gère le contexte long avec une fiabilité supérieure, répond à la première tentative sans avoir besoin de sollicitations, et montre une cohérence d'exposition plus robuste dans les tâches complexes. Il paie en revanche un peu sur le front de la perfection syntaxique dans le code à la première génération, et montre quelques fragilités dans les langues secondaires au sein d'une même réponse. Ce n'est pas un compromis surprenant pour un modèle de cette taille.

La question qui reste ouverte, et qui ne relève pas de la portée de cette expérience, est de savoir combien la quantification Q4_K_M a effectivement coûté en termes de qualité par rapport à la version complète. Les résultats sont suffisamment élevés pour qu'il soit difficile d'estimer quelle marge est restée sur la table. Peut-être beaucoup, peut-être étonnamment peu. Ce serait une expérience intéressante pour ceux qui ont accès à du matériel avec plus de VRAM.

Ce que je peux dire avec certitude, en tant que passionné qui veut comprendre ce qu'il est possible de faire avec des moyens normaux en 2026, c'est que la frontière entre « possible seulement sur le cloud » et « possible en local » s'est encore déplacée. Pas qu'un peu. Gemma 4 26B MoE, même dans sa version la plus compressée, sur du matériel que beaucoup d'utilisateurs avancés possèdent déjà, produit des réponses qui, il y a encore quelques mois, auraient nécessité un appel API à un modèle de pointe. C'est la donnée que je trouve la plus significative, plus que n'importe quelle note individuelle.

Une chose est sûre : ce que j'indiquais en janvier comme la tendance de l'année, la course aux [Small Language Models en local](https://aitalk.it/it/slm-2026.html), n'est pas seulement en train de se confirmer, elle est en train de brûler les étapes. Et nous ne sommes qu'en avril.
