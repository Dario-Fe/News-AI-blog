---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-05-20
author: "Dario Ferrero"
---

# Qwen 3.6 en local : 35 milliards sur mon PC
![qwen36-35b-ai.jpg](qwen36-35b-ai.jpg)

*Il y a un moment, dans chaque série d'expériences, où l'on se rend compte que le problème n'est plus le sujet du test, mais la qualité de l'instrument de mesure. J'étais en train de collecter les notes du huitième essai et je me disais que mes tests étaient peut-être devenus la limite : cinq sur cinq, huit fois sur huit. Le thermomètre fonctionne-t-il encore, ou l'eau a-t-elle cessé de varier en température ?*

La question n'est pas rhétorique. Ces articles sont conçus comme le journal de bord d'un laboratoire domestique, non comme un livre blanc académique, et la méthode reste délibérément personnelle : pas de benchmark automatisé, pas de métrique standardisée, seulement des prompts calibrés sur des scénarios réalistes et la sensation tactile de celui qui utilise l'outil et en fait ensuite le récit. Le matériel n'a pas changé par rapport aux épisodes précédents, AMD Ryzen 7700, 32 Go de RAM, GPU AMD avec 16 Go de VRAM, et le logiciel non plus : [LM Studio](https://lmstudio.ai/), la solution la plus accessible pour ceux qui veulent exécuter des modèles locaux sans perdre une après-midi en configurations de terminal. Pour tous les détails sur l'installation, sur l'écosystème et sur la philosophie de ce laboratoire, je renvoie au [premier épisode de la série sur Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1.html), qui reste la référence méthodologique de toute la série. Ceux qui sont déjà à bord peuvent continuer ici.

Aujourd'hui, le protagoniste est différent des autres. Non par catégorie, mais par taille : [Qwen3.6 35B A3B en quantification Q6](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), le plus grand modèle que j'ai jamais chargé sur cette machine, littéralement à la limite de ce que la configuration peut supporter. Après avoir exploré [Qwen 3.5 9B dans les deux premiers épisodes](https://aitalk.it/it/qwen3.5-locale-puntata2.html) et [Gemma 4 26B MoE](https://aitalk.it/it/gemma4-26b.html) dans le troisième, ce saut d'échelle était inévitable. Et c'est exactement le saut que je voulais faire.

## Trente-cinq milliards, trois à la fois

Le nom cache une architecture qu'il vaut la peine de comprendre, car elle change radicalement la façon de raisonner sur les besoins matériels. Qwen3.6 35B A3B est un modèle Mixture of Experts : il possède 35 milliards de paramètres au total, mais pour chaque token généré, il n'en active que 3 milliards environ. Tous les experts ne sont pas appelés à répondre à chaque fois, seulement ceux jugés les plus compétents pour ce fragment spécifique de texte. C'est un peu comme avoir un orchestre de deux cent cinquante-six musiciens, où le chef d'orchestre choisit à chaque fois les huit instrumentistes à faire jouer, laissant les autres à l'écoute et prêts. Le résultat pratique est que le coût informatique ressemble plus à celui d'un modèle de trois milliards qu'à celui d'un de trente-cinq, tout en puisant dans la profondeur de ce dernier quand c'est nécessaire.

Qwen3.6, décrit sur le [blog officiel Alibaba](https://qwen.ai/blog?id=qwen3.6) comme une évolution de l'architecture Qwen3, apporte avec lui quatre nouveautés que l'équipe a tenu à souligner : une amélioration de 43 % sur QwenWebBench dans les capacités de génération de code agentique et d'applications web complètes, une fonctionnalité appelée *thinking preservation* pour maintenir la cohérence du raisonnement à travers des conversations multi-tours, un saut dans la compréhension multimodale avec des images et des documents, et le support natif de la compréhension vidéo, cette dernière étant encore expérimentale et non supportée par tous les environnements d'exécution disponibles.

La quantification Q6 sur laquelle j'ai travaillé représente un compromis raisonné : moins lourde que la F16 pure, beaucoup plus fidèle au modèle original par rapport aux quantifications agressives comme la Q4. En pratique, on perd très peu de qualité par rapport aux poids entiers, tout en payant un coût en mémoire qui, sur ma configuration, a nécessité un équilibrage attentif entre le GPU et la RAM système.

## La configuration à la limite

C'est là que réside la véritable expérience. Je n'ai pas cherché le point de performance maximale : j'ai délibérément cherché le bord du possible, c'est-à-dire comprendre ce qui se passe quand on travaille avec le minimum acceptable de performance, du moins selon mon avis.

Les paramètres choisis : contexte à 8078 tokens (le modèle dépasse nativement les 262 000), déchargement (offload) GPU de 8 couches sur 43 au total, 8 experts actifs sur 256 disponibles, quantification F16 en interne pour les couches en GPU. La vitesse résultante s'est stabilisée autour de 11 tokens par seconde, contre les 20-25 que Qwen 3.5 9B atteignait confortablement. Ce n'est pas une vitesse que je recommanderais pour un assistant conversationnel à utiliser à la volée, mais c'est tout à fait acceptable pour des sessions de travail structurées où l'on n'est pas pressé et où l'on privilégie la profondeur de la réponse.

La question qui sous-tend toute l'expérience est simple : le sacrifice de vitesse vaut-il la qualité gagnée ? Les tests qui suivent sont la réponse.

## Un pas de plus : la configuration optimale

Le choix de partir de 8 couches en GPU et d'un contexte réduit était délibéré : je voulais tester le modèle dans des conditions de réelle rareté de ressources, le point le plus bas de la plage acceptable. Mais une fois la batterie de tests terminée, j'ai voulu comprendre où se trouve le véritable point d'équilibre sur ce matériel.

Les résultats ont été instructifs. Passer de 8 à 16 couches en GPU fait monter la vitesse de 11 à environ 14,5 tokens par seconde, un gain sensible. Étonnamment, les doubler encore à 32 ne change presque rien (14,49 tok/s), et tenter le chargement à 40 couches empêche le modèle de démarrer du tout : la VRAM ne suit pas. Le point optimal pour ce matériel est donc de 16 couches, pas plus.

Tout aussi intéressant est le comportement du contexte : l'élargir de 8 000 tokens jusqu'au maximum natif de 262 000 influe très peu sur la vitesse, avec une baisse de moins d'un token par seconde entre les deux extrêmes. En pratique, on peut choisir la fenêtre de contexte en fonction de la tâche sans se soucier des performances.

Le paramètre qui fait en revanche vraiment la différence est le nombre d'experts actifs. Avec 4 experts, on monte à 16,2 tok/s, avec 8 on est à 14,2, avec 16 on descend à 11,4, avec 125 on s'effondre à 2,9. C'est une relation presque linéaire vers le bas : chaque expert supplémentaire coûte cher, et sur du matériel grand public, le coût se fait immédiatement sentir.

Tous les tests avec des configurations différentes ont néanmoins produit des réponses d'excellente qualité, ce qui suggère que réduire les experts actifs ne compromet pas la qualité de manière perceptible, du moins sur les tâches utilisées dans cette série.

La configuration offrant le meilleur compromis sur ce matériel est donc : 16 couches en GPU, contexte de 125 000 tokens, 8 experts actifs, avec une vitesse d'environ 14,2 tokens par seconde. Ce n'est pas la vitesse d'un petit modèle, mais c'est un pas en avant par rapport à la configuration "à la limite" utilisée dans les tests principaux, et cela ouvre la porte à des sessions de travail sur des documents longs sans avoir à renoncer à la qualité.
![grafico1.jpg](grafico1.jpg)
[Image des résultats des benchmarks tirée de qwen.ai](https://qwen.ai/blog?id=qwen3.6)

## Les tests

### Test 1 — Mécanisme de Higgs et physique des particules *(5/5)*

*Paramètres : contexte 8078 tokens, offload GPU 8 couches sur 43, 8 experts actifs sur 256, F16, 11,17 tokens/s*

La réponse a été exceptionnelle, probablement la meilleure que j'aie jamais obtenue d'un modèle local sur un sujet scientifique complexe. Le modèle a commencé par le contexte théorique, décrivant la symétrie de jauge qui gouverne les interactions électrofaibles. Il a ensuite introduit le champ de Higgs et son célèbre potentiel en "chapeau mexicain", expliquant pourquoi le zéro n'est pas le minimum énergétique. Il a montré comment la valeur d'attente du vide interagit avec les bosons de jauge, conférant une masse aux W et aux Z. Et il a clarifié le détail le plus subtil, celui qui manque souvent même dans les cours universitaires : pourquoi le photon reste sans masse, grâce à une symétrie résiduelle que le vide de Higgs ne parvient pas à briser.

La structure de la réponse était impeccable, organisée en sections logiques qui progressaient du général au particulier sans jamais perdre le fil. Le langage était précis mais accessible, utilisant des métaphores comme celle du "chapeau mexicain" pour rendre intuitifs des concepts abstraits. Je n'ai trouvé d'erreurs ni dans les concepts physiques ni dans les détails mathématiques. La vitesse de 11 tokens par seconde est plus faible par rapport aux modèles plus petits testés précédemment, mais la qualité de cette réponse compense largement le compromis. La patience d'attendre quelques secondes de plus a été récompensée par une explication que l'on pourrait qualifier de magistrale.

### Test 2 — Multimodalité et compréhension de tableaux *(5/5)*

*Paramètres : contexte 8078 tokens, offload GPU 8 couches sur 43, 8 experts actifs sur 256, F16, 10,49 tokens/s*

L'image chargée était délibérément de basse qualité : une petite capture d'écran d'une interface de gestion de factures, imparfaite pour mettre à l'épreuve les capacités visuelles dans des conditions réalistes, non idéales. Le modèle a réussi le test avec des résultats surprenants.

La première chose qui a frappé a été la capacité à comprendre la structure générale de l'interface. Le modèle a identifié correctement les trois sections principales, le panneau de filtres en haut, la liste latérale des produits à droite, le tableau central. Il a reconnu qu'il s'agissait probablement d'une application de gestion comptable, émettant même l'hypothèse qu'il pourrait s'agir d'une base de données d'exemple ou d'un environnement de test, compte tenu du caractère générique des noms de clients et des articles.

La lecture des données a été précise et détaillée : toutes les colonnes du tableau énumérées correctement, le taux de TVA fixe à 22 % détecté comme constant sur toutes les lignes, la colonne "Montant" surlignée en jaune signalée comme élément de navigation pour l'utilisateur, les dates des factures identifiées dans la période janvier-mars 2022. Mais la partie la plus remarquable a été l'analyse des anomalies : bien que le filtre supérieur montre l'option "À PAYER" comme sélectionnée, les factures dans le tableau avaient déjà une date de paiement et un montant soldé. Le modèle a signalé le mélange possible de données, formulant des hypothèses sensées sur le contexte d'utilisation. Un modèle plus petit aurait produit une description générique. Ici, j'ai obtenu une véritable analyse, avec interprétation des incongrueces incluse.

### Test 3 — Génération de code complexe *(5/5)*

*Paramètres : contexte 8078 tokens, offload GPU 8 couches sur 43, 8 experts actifs sur 256, F16, 10,06 tokens/s*

Ce test était l'un des plus importants de toute la batterie, car Qwen3.6 promet une amélioration de 43 % sur QwenWebBench précisément dans la génération de code. Je voulais voir si la promesse se traduisait par une implémentation concrète et fonctionnelle sur un problème algorithmique non trivial : trouver le cycle de longueur maximale dans un graphe non orienté.

La réponse a pleinement convaincu. Le modèle a commencé par un postulat théorique que peu d'assistants de programmation ont la maturité d'inclure : il a déclaré explicitement que le problème est NP-difficile, qu'il n'existe pas d'algorithme polynomial pour le résoudre sur des graphes génériques, et que toute solution exacte aura une complexité exponentielle dans le pire des cas. Cette conscience est rare et précieuse, car elle démontre que le modèle n'essaie pas de vendre une solution magique, mais comprend profondément les limites du domaine.

L'implémentation proposée était élégante et fonctionnelle : stratégie DFS avec suivi du chemin, structure de données avec carte de profondeur (depth map) pour détecter les arcs de retour (back-edges) et calculer la longueur des cycles en temps constant, représentation du graphe via une liste d'adjacence efficace, backtracking implémenté correctement, gestion complète des cas limites comme les graphes sans cycles et les composantes déconnectées. J'ai particulièrement apprécié l'utilisation de la carte de profondeur, plus élégante et performante qu'une simple recherche linéaire dans le chemin car elle permet de calculer la longueur du cycle sans scanner toute la liste. L'explication de la complexité temporelle était claire et honnête, avec une distinction entre le cas favorable et le pire cas. Aucune erreur syntaxique ou logique, type hints présents, structure modulaire. Un code que l'on pourrait livrer.

### Test 4 — Multilingue et planification *(5/5)*

*Paramètres : contexte 8078 tokens, offload GPU 8 couches sur 43, 8 experts actifs sur 256, F16, 11,15 tokens/s*

*Note méthodologique : exécuté dans une discussion propre après qu'une première exécution dans une discussion avec historique ait produit des résultats médiocres.*

Ce test a enseigné quelque chose d'important avant même le résultat. La première exécution, dans une discussion avec des itérations précédentes sur d'autres sujets, avait produit des interruptions et une qualité médiocre. Répété dans une discussion complètement nouvelle, le résultat a été transformé. La différence a été tellement nette qu'elle mérite une note méthodologique permanente : l'historique de la discussion, même quand il semble inoffensif, peut altérer de manière significative les résultats sur des tâches complexes. Tester dans une discussion propre n'est pas un caprice, c'est de l'hygiène expérimentale.

Dans une discussion propre, Qwen3.6 a produit un itinéraire de cinq jours à Tokyo en français, complet et articulé, dès la première tentative. Le français était de niveau langue maternelle : "spécialités de rue", "ambiance vieux Tokyo", "cadre apaisant", "ruelle atmosphérique", "patrimoine UNESCO". Aucune erreur grammaticale ou syntaxique, fluidité de niveau avancé.

L'itinéraire était logistiquement parfait, avec des journées équilibrées entre temples et cuisine de rue, et regorgeait d'astuces de voyageur expert : arriver à Fushimi Inari avant huit heures pour éviter la foule, imprimer les noms des temples en japonais, utiliser les modèles de nourriture dans les restaurants pour commander sans parler la langue. La section transports expliquait comment activer Suica ou Pasmo sur smartphone, comment réserver le Shinkansen, et précisait que les bureaux d'information dans les gares principales disposent de personnel francophone à certains horaires. Il a suggéré le Kyoto City Bus Day Pass et conseillé de télécharger les cartes hors ligne. Pour la barrière de la langue, il a proposé non seulement Google Translate mais aussi Papago pour la reconnaissance vocale, et des phrases clés en japonais translittéré.

La section finale demandée en italien, pour tester le multilinguisme au sein d'un même prompt, était propre, correcte, riche en conseils pratiques sur les paiements en espèces, les distributeurs Seven-Eleven, les fiches de traduction pour les allergies alimentaires.

### Test 5 — Contexte très long : document de 460 pages *(5/5)*

*Paramètres : contexte 8078 tokens, offload GPU 8 couches sur 43, 8 experts actifs sur 256, F16, 10,93 tokens/s*

Ce fut le test le plus surprenant de toute la batterie, et il mérite d'être raconté avec toute l'attention nécessaire. J'ai chargé l'*AI Index Report 2025*, un PDF d'environ 460 pages et plus de 20 millions de caractères, en demandant au modèle de décrire la croissance de la génération vidéo et d'indiquer les pages où trouver les données. Le défi était délibérément extrême : contexte de seulement 8078 tokens, bien loin des 262 000 natifs du modèle, seulement huit experts actifs, seulement huit couches en GPU.

La réponse m'a laissé sans voix. Malgré des paramètres réduits à l'essentiel, le modèle a fourni un résumé précis et bien structuré des progrès de la génération vidéo entre 2023 et 2025. Il a cité correctement les principaux modèles : Meta Movie Gen, Google Veo et Veo 2, Runway Gen-3 Alpha, Luma Dream Machine, Kling 1.5. Il a mentionné le célèbre exemple du prompt "Will Smith eating spaghetti" comme marqueur du saut qualitatif survenu dans le secteur. Il a indiqué des figures spécifiques du rapport, comme la Figure 2.3.11 et la Figure 2.3.12. Et il a déclaré que les données principales se trouvaient aux pages 126 et 127 du rapport. J'ai vérifié. C'était exact.

Comment il a réussi à trouver la bonne information dans un document de 460 pages avec une fenêtre de contexte correspondant à quelques dizaines de pages reste le mystère le plus fascinant de toute la session. Probablement que le modèle a su identifier et conserver les sections les plus pertinentes malgré les contraintes de mémoire, mais le mécanisme exact n'est pas transparent de l'extérieur. Ce qui est transparent, c'est le résultat : avec une configuration réduite au strict minimum, sur un document énorme, des références vérifiables aux bonnes pages. C'est de la robustesse.

### Test 6 — Raisonnement spatial *(5/5)*

*Paramètres : contexte 8078 tokens, offload GPU 8 couches sur 43, 8 experts actifs sur 256, F16, 11,42 tokens/s*

Le test demandait d'analyser la photographie d'une pièce en désordre et de proposer un plan de rangement. Malgré des paramètres conservateurs, seulement huit experts, seulement huit couches en GPU, le modèle a produit une analyse visuo-spatiale de très haut niveau.

La description était fidèle et détaillée : lit avec structure en métal noir, deux bibliothèques en échelle blanches positionnées correctement, bureau gris encombré, petit meuble blanc, miroir sur la porte. Couleurs des murs identifiées comme vert sauge clair, sol avec moquette imprimée, rideaux à rayures vertes et blanches. Même le panier à linge bleu au milieu du sol, entouré de vêtements éparpillés, chaussures, boîtes, ciseaux et autres objets, avait été détecté et répertorié.

Le plan de rangement était structuré par priorités visuelles avec des motivations solides. D'abord les vêtements au sol et sur le lit, car les retirer libère le passage et réduit le bruit visuel, faisant paraître la pièce plus grande. Ensuite le lit, car un lit défait occupe visuellement plus d'espace et crée un sentiment de chaos, alors que le refaire définit les limites de la pièce. Puis le panier à linge et les chaussures, obstacles physiques qui bloquent le passage central. Enfin le bureau, dont la surface libre projette l'ordre et la fonctionnalité. La synthèse finale était parfaite : "L'objectif initial n'est pas le minutieux, mais le volume." Une phrase qui résume l'essence d'une organisation efficace dans un environnement très désordonné, et qu'un professionnel du secteur n'aurait pas pu mieux dire.

### Test 7 — Agent multi-étapes : planification de projet logiciel *(5/5)*

*Paramètres : contexte 8078 tokens, offload GPU 8 couches sur 43, 8 experts actifs sur 256, F16, 11,04 tokens/s*

Ce test a été introduit spécialement pour vérifier la promesse d'amélioration de 43 % sur QwenWebBench. Un modèle qui excelle en physique et en raisonnement spatial pourrait tout de même échouer dans une tâche de planification articulée. La véritable maturité d'un assistant de programmation se voit dans la capacité à organiser le travail, anticiper les problèmes et fournir des solutions pratiques, pas seulement à écrire du code. La tâche consistait à planifier le développement d'une application web pour la gestion des dépenses familiales, avec une équipe de deux développeurs et une feuille de route détaillée.

La réponse a été probablement la plus complète de toute la batterie. La pile technologique proposée était moderne et cohérente, avec chaque choix motivé dans un tableau clair : React avec TypeScript et Vite pour le frontend, Node.js avec Express pour le backend, PostgreSQL avec Prisma comme ORM, JWT pour l'authentification, papaparse pour le parsing CSV, React-PDF pour l'exportation, BullMQ pour les files d'attente de notifications, Docker pour l'infrastructure. La structure du projet était détaillée par dossiers logiques tant côté frontend que backend, avec un docker-compose.yml pour orchestrer Postgres, Redis et l'application. C'est la structure qu'utiliserait un véritable ingénieur logiciel.

La planification en six sprints hebdomadaires était réaliste et bien équilibrée : setup et authentification, transactions et importation CSV, tableau de bord et graphiques, exportation PDF, budget et notifications par e-mail, tests et déploiement. Pour chaque sprint étaient indiqués le focus, les livrables attendus, les points critiques potentiels et la répartition du travail entre les deux développeurs. La recommandation de définir d'abord les contrats d'API puis de travailler en parallèle est une bonne pratique que de nombreux développeurs seniors ont du mal à suivre systématiquement.

Les points critiques avaient été identifiés avec une précision chirurgicale : formats CSV hétérogènes et gestion des erreurs partielles lors de l'importation, délivrabilité et fuseaux horaires pour les notifications par e-mail, couverture des tests et plan de rollback pour le déploiement. La section des bonnes pratiques était complète : cookies httpOnly et rate limiting pour la sécurité, index DB et pagination pour les performances, mocks de SMTP et de DB pour les tests, GitHub Actions pour le CI/CD. Le modèle a même suggéré Sentry pour le traçage des erreurs et Notion pour la documentation. Le seul petit bémol est que la réponse était presque excessivement détaillée pour une planification initiale, mais c'est le genre d'excès que l'on préfère avoir.
![testqwen.jpg](testqwen.jpg)
*Capture d'écran de mon PC et de LM Studio, pendant le test Agent multi-étapes.*

### Test 8 — Thinking preservation : conversation à quatre tours *(5/5)*

*Paramètres : contexte 8078 tokens, offload GPU 8 couches sur 43, 8 experts actifs sur 256, F16, un peu plus de 11 tokens/s par tour*

Ce test a été introduit pour évaluer l'une des nouveautés les plus intéressantes de Qwen3.6 : la capacité à maintenir la cohérence du raisonnement à travers des conversations multi-tours, en préservant non seulement l'historique de la discussion mais aussi la logique des décisions prises lors des phases précédentes. Pour le développement itératif, c'est une qualité fondamentale, car elle permet de construire des projets complexes sans avoir à répéter continuellement les prémisses.

La conversation s'est articulée en quatre tours. Au premier, j'ai demandé une pile technologique pour une application de gestion de tâches : la réponse a été détaillée avec un tableau comparatif, React avec TypeScript, Node.js avec Express, PostgreSQL avec Prisma, JWT, SendGrid avec BullMQ, chaque choix motivé par des arguments solides. Au deuxième tour, j'ai demandé un avis sur le choix entre WebSocket et polling pour les notifications en temps réel avec 1000 utilisateurs actifs : le modèle a expliqué pourquoi WebSocket est supérieur pour la latence et l'overhead, a montré une architecture avec PostgreSQL LISTEN/NOTIFY et Redis Pub/Sub, et a anticipé le cas limite des réseaux qui bloquent WebSocket en expliquant que Socket.IO gère le repli (fallback) automatiquement. Au troisième tour, j'ai demandé le schéma de la base de données dans Prisma : le schéma produit était complet, avec huit modèles principaux, des enums pour le statut, la priorité et le rôle, des relations bien définies, des UUID pour les clés primaires, des index stratégiques pour les requêtes fréquentes, des cascades contrôlées. Il a inclus un exemple de requête évitant le problème N+1.

Le quatrième tour était le véritable test : j'ai demandé un récapitulatif des choix technologiques faits jusqu'à présent et l'explication de pourquoi nous avions choisi WebSocket plutôt que le polling. Le modèle s'est rappelé correctement de tout le premier tour, a résumé les motivations pour WebSocket avec la même terminologie et les mêmes raisons qu'au deuxième tour, et a ajouté spontanément une section sur l'extensibilité à 10 000 utilisateurs avec des stratégies pour le backend, la base de données, la mise en cache, les files d'attente d'e-mails, l'observabilité et le déploiement, plus une checklist opérationnelle. Il n'a reçu aucun rappel : il s'est simplement souvenu. Aucune contradiction, aucun oubli, un raisonnement étendu de manière cohérente. La promesse du *thinking preservation* n'était pas du marketing.

## La vidéo qui attend

Qwen3.6 promet une compréhension vidéo native, une nouveauté absolue par rapport aux versions précédentes. J'ai essayé de le tester en chargeant un fichier MP4 dans LM Studio. Le système a répondu par un point d'exclamation sur la pièce jointe et le modèle a déclaré n'avoir reçu aucun fichier. La limite ne vient pas du modèle, mais de l'outil choisi pour l'exécuter : LM Studio gère excellemment les images, les PDF, les documents texte et les CSV, mais les vidéos ne font pas encore partie des formats supportés. Je me réserve de revenir sur ce test dès que possible, probablement avec llama.cpp ou vLLM, qui pourraient offrir un support plus complet pour les contenus vidéo. Si les promesses sont tenues, ce sera un épisode qui méritera un espace dédié.
![tabella-confronto-modelli.jpg](tabella-confronto-modelli.jpg)
*Le tableau "comparatif" avec les tests sur les modèles précédents. Avec la double configuration testée pour Qwen 3.6*

## Vaut-il la peine de pousser jusqu'à la limite ?

C'est la question qui sous-tend toute la série, et qui avec Qwen3.6 devient impossible à éluder. Avec Qwen 3.5 9B, on tournait à 20-25 tokens par seconde sur une configuration détendue. Avec Gemma 4 26B MoE, les marges s'étaient déjà réduites. Avec ce modèle, on est à 11 tokens (environ 14/15 avec l'optimisation maximale sur mon matériel) par seconde, avec le GPU sollicité pour une fraction du total et la charge répartie entre la VRAM et la RAM système dans un équilibre précaire. Les notes maximales successives ont soulevé une question légitime sur la sévérité de mes tests, et cette question reste ouverte : des outils d'évaluation plus pointus seront probablement nécessaires dans les épisodes suivants.

Mais en attendant, il y a un fait concret sur lequel réfléchir. La réponse à la question sur la vitesse dépend entièrement de l'usage que l'on fait du modèle. Si l'on cherche un assistant conversationnel pour des sessions rapides, 11 tokens (environ 14/15 avec l'optimisation maximale sur mon matériel) par seconde commencent à se faire sentir. Si l'on travaille sur des tâches structurées, des analyses approfondies, de la génération de code complexe, des documents longs, la qualité qu'offre ce modèle en configuration réduite est tout simplement inatteignable pour les modèles plus petits, même poussés au maximum. L'expérience avec le document de 460 pages l'a démontré de la manière la plus flagrante possible : une fenêtre de contexte minuscule, une machine à la limite, et le modèle qui trouve les pages exactes dans un volume de bibliothèque.

Il y a cependant un sous-texte plus large que cette série d'expériences fait progressivement remonter à la surface. Quand un modèle de 35 milliards de paramètres tourne en local sur du matériel grand public avec des résultats comparables aux services cloud d'il y a deux ans, quelque chose dans la topologie du marché de l'IA est en train de changer. Le cloud reste imbattable pour la vitesse, pour les modèles de pointe, pour l'extensibilité. Mais pour ceux qui travaillent sur des données sensibles, pour ceux qui veulent un contrôle complet sur l'inférence, pour ceux qui ne veulent pas dépendre d'un endpoint d'API avec ses latences et ses coûts variables, le local est en train de devenir un choix mature, et non plus une expérience de passionnés. La distance entre les deux options se réduit à chaque génération de modèles, et Qwen3.6, même dans cette configuration intentionnellement pénalisée, en est la preuve la plus convaincante que j'aie eue jusqu'à présent.

Les notes maximales sont un problème. Mais c'est le genre de problème qui fait beaucoup moins peur que le contraire.
