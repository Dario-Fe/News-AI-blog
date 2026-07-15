---
tags: ["Generative AI", "Applications", "Security"]
date: 2026-07-15
author: "Dario Ferrero"
---

# J'ai appris à l'IA à monter la garde : comment j'ai construit un système de sécurité à coût nul
![sistema-sicurezza-ai.jpg](sistema-sicurezza-ai.jpg)

*Dans la série télévisée 'Person of Interest', une superintelligence surnommée simplement "la Machine" surveille chaque recoin de la planète à travers des caméras, des microphones et des capteurs de toutes sortes, identifiant les menaces avant qu'elles ne se matérialisent. C'est de la science-fiction, bien sûr. Mais l'idée de fond, à savoir utiliser la vision par ordinateur pour comprendre ce qui se passe dans un environnement, est désormais accessible à toute personne possédant un PC et une webcam. Moins de 250 lignes de code. Pas d'abonnement, pas de cloud, pas de vidéo circulant dans le monde. Juste une notification sur le téléphone, avec photo, quand quelqu'un entre dans la maison.*

La question que je me suis posée il y a quelques semaines était simple : combien coûte un système de sécurité qui vous alerte en temps réel si quelqu'un entre chez vous, vous envoie une photo, et fonctionne entièrement en local sans dépendre d'un abonnement mensuel ? La réponse : zéro euro. Uniquement du matériel que vous possédez très probablement déjà. Dans cet article, je raconte comment j'ai construit ce système, ce que j'ai appris en chemin, et pourquoi l'expérience en dit long sur la façon dont l'intelligence artificielle change le rapport entre technologie et quotidien.

## Avant de l'orienter vers la maison : le test à Times Square

Tout système de sécurité digne de ce nom doit être testé avant d'être mis en production. Mais pointer une webcam sur sa propre chambre sans avoir vérifié le fonctionnement dans des conditions difficiles semblait naïf. J'ai donc décidé de commencer par le contexte le plus chaotique que je puisse trouver sans bouger de ma chaise : Times Square, New York, vue d'en haut à travers l'une des nombreuses webcams publiques accessibles en streaming.

Le scénario était délibérément extrême. Des centaines de personnes qui se croisent, des taxis jaunes, des bus, des camions de livraison, le tout en mouvement simultané, avec des variations de lumière soudaines et des angles difficiles. Le genre de situation qui met en difficulté n'importe quel système de reconnaissance visuelle médiocre.

Le résultat a été surprenant : le système a reconnu jusqu'à neuf véhicules simultanément parmi des voitures, des bus et des camions, a identifié des piétons même à une distance considérable, a maintenu 40 images par seconde de manière stable, le tout sur un CPU, sans toucher au GPU. *"Si ça fonctionne sur Times Square, ça fonctionne n'importe où"*, me suis-je dit. Et c'est ce qui s'est passé.
![timesquare.jpg](timesquare.jpg)
*Capture d'écran des tests effectués sur la webcam de Times Square.*

## Le cœur du système : YOLO expliqué simplement

Avant d'en arriver au moment où le téléphone a vibré avec la première photo d'alerte, il vaut la peine de consacrer quelques lignes à ce qui se passe sous le capot, car la technologie impliquée est véritablement fascinante, même vue de loin.

Le composant central s'appelle [YOLO](https://github.com/ultralytics/ultralytics), acronyme de *You Only Look Once*. Le nom n'est pas du marketing : il décrit exactement son fonctionnement. Les systèmes de reconnaissance visuelle traditionnels analysaient une image en plusieurs étapes, identifiant d'abord les régions d'intérêt puis les classant. YOLO inverse l'approche : il analyse l'image entière en une seule passe, la divisant en une grille et prédisant simultanément la position et le type d'objet pour chaque cellule. Le résultat est une vitesse nettement supérieure, avec une précision qui a atteint des niveaux excellents sur les versions récentes.

La version que j'ai utilisée, YOLOv8n, est la variante la plus légère de la famille. Le suffixe "n" signifie *nano*, et elle est conçue explicitement pour fonctionner sur du matériel limité. Elle est entraînée sur le dataset COCO, qui comprend quatre-vingts catégories d'objets : personnes, véhicules, animaux domestiques, objets d'ameublement. Pour mes besoins, la seule catégorie qui m'intéresse est "personne", avec un seuil de confiance fixé à 0,4, ce qui signifie que le modèle signale une présence seulement lorsqu'il est sûr à au moins quarante pour cent de l'avoir détectée. Un seuil plus bas produit plus de fausses alertes, un seuil plus haut risque de manquer des détections réelles.

Le deuxième ingrédient crucial est [ONNX](https://onnxruntime.ai/), qui signifie *Open Neural Network Exchange*. C'est un format ouvert pour représenter des modèles de machine learning, mais c'est surtout un moteur d'inférence optimisé qui sait comment exploiter au mieux les instructions spécifiques de chaque processeur. Lorsque vous exportez YOLOv8n au format ONNX, le modèle passe de 10-15 images par seconde à 40-45 images par seconde sur le même CPU, sans changer une seule ligne de code applicatif. Le fichier passe de 6 Mo à 12 Mo, mais le gain de vitesse est presque quadruplé. C'est comme avoir un traducteur simultané qui connaît parfaitement le dialecte de votre processeur.

## GINA me prête le bot

Ceux qui suivent ce portail se souviendront de [GINA, mon assistant vocal personnel](https://aitalk.it/it/gina-assistente-vocale.html). Pour les notifications en temps réel, j'avais déjà construit un bot Telegram intégré à l'écosystème de GINA, capable de m'envoyer des messages, des mises à jour et des alertes directement sur mon smartphone. Réutiliser cette infrastructure pour le système de sécurité était naturel : un exemple classique de la façon dont les pièces d'un écosystème technologique construit au fil du temps commencent à s'emboîter de manières pas toujours prévues.

Le bot Telegram ne fait qu'une chose, mais il la fait bien : lorsque le système détecte une personne, il reçoit un appel HTTP avec un message texte et une photo de l'image incriminée, et les livre sur mon téléphone en deux à cinq secondes. Pas d'application propriétaire, pas de compte sur des plateformes de vidéosurveillance cloud, pas de données traversant des serveurs tiers autres que les serveurs de Telegram pour la livraison finale de la notification. Alternativement, on pourrait envisager l'envoi d'un e-mail. La vidéo elle-même ne sort jamais du PC.

La configuration du bot prend environ cinq minutes : on le crée via [@BotFather](https://core.telegram.org/bots) sur Telegram, on obtient un jeton d'authentification, on récupère son propre chat ID en envoyant un message au bot et en interrogeant les API, et on insère les deux chaînes dans le fichier de configuration. Après cela, le canal de notification est opérationnel.

## Le moment de vérité : ma chambre

Une fois le test new-yorkais réussi, il était temps de pointer la webcam sur l'environnement qui comptait vraiment : ma chambre. J'ai positionné la caméra, lancé le script, attendu les cinq secondes de stabilisation que le système prend au démarrage pour ne pas générer de fausses alertes pendant le chargement, et j'ai quitté la pièce.

Puis je suis revenu.

Le téléphone a vibré avant même que j'atteigne le centre du cadre. Le message disait : *"🚨 ALERTE DE SÉCURITÉ ! Personnes détectées : 1. Heure : 13:43:07. Alerte #1"*. En dessous, une photo avec mon contour mis en évidence par un cadre et un overlay rouge en haut de l'image. Latence entre l'entrée et la notification : moins d'une seconde pour la reconnaissance, deux à trois secondes pour la livraison Telegram.

Ça fonctionnait.

Le système dispose d'une logique de protection contre les fausses alertes intégrée : un cooldown de dix secondes entre une alerte et la suivante empêche qu'une personne immobile dans le cadre ne génère des dizaines de notifications par minute. Le seuil de confiance à 0,4 s'est révélé bien calibré pour un environnement domestique : aucun faux positif pendant les tests, aucune reconnaissance manquée dans des conditions de lumière normales. Avec un faible éclairage, les performances se dégradent, mais c'est une limite physique de la webcam avant même celle du modèle.
![allarme.jpg](allarme.jpg)
*Capture d'écran du message d'alerte sur Telegram, ainsi que du voleur le plus improbable de l'histoire de la criminalité.*

## Comment c'est construit : la recette technique

Le code complet occupe moins de 250 lignes de Python. La structure est linéaire et compréhensible même pour ceux qui n'écrivent pas de code professionnellement. Il y a quatre blocs logiques : la configuration initiale avec les jetons Telegram et les paramètres de seuil, les fonctions d'envoi de messages et de photos via l'API Telegram, la fonction de détection de personnes qui interroge ONNX, et la boucle principale qui acquiert les images de la webcam, les analyse et gère la logique des alertes.

Les dépendances sont cinq bibliothèques Python standards dans l'écosystème du machine learning : `ultralytics` pour charger YOLO, `onnxruntime` pour l'inférence optimisée, `opencv-python` pour la gestion de la webcam et le traitement des images, et `requests` pour les appels HTTP à Telegram.

La structure finale du projet est essentielle : un fichier Python principal, le modèle ONNX de 12 Mo, et un fichier de configuration. En tout, moins de 15-20 Mo sur disque.

Sur le front des performances, les chiffres parlent d'eux-mêmes :
![tabella.jpg](tabella.jpg)

Le matériel utilisé est un AMD Ryzen 7 7700 avec 32 Go de RAM, mais les tests sur des configurations moins puissantes confirment que le système fonctionne sans problème même sur un ordinateur portable avec un processeur Intel i5 de cinquième ou sixième génération et 8 Go de RAM. Le GPU n'est jamais sollicité.

## Où il est judicieux de l'utiliser et où non

Un système de ce type fonctionne bien dans des contextes spécifiques, et il est honnête de le dire clairement. Pour la sécurité domestique dans un appartement ou une petite maison, il est efficace : il surveille une pièce ou une entrée, alerte en temps réel, coûte zéro. Pour surveiller un bureau pendant la fermeture nocturne, un magasin après les heures de fermeture, ou un entrepôt à accès limité, le système se prête tout aussi bien.

En revanche, il ne remplace pas un système de sécurité professionnel certifié pour les environnements critiques. Les faux négatifs existent, surtout dans des conditions de lumière difficiles. Le système ne fait pas la distinction entre celui qui possède les clés de la maison et un véritable intrus, du moins dans sa version de base. Il n'enregistre pas de vidéo, seulement des photos des moments d'alerte. Et il tourne sur un PC qui doit être allumé et connecté à Internet pour les notifications.

Sur le plan juridique, il convient de rappeler qu'en Italie, la vidéosurveillance est réglementée par le RGPD et le Garant de la vie privée. Pour un usage exclusivement domestique, à l'intérieur de sa propre propriété privée, les restrictions sont nettement moins lourdes que pour les environnements publics ou professionnels. Si la caméra filme des espaces communs ou des zones extérieures partagées, des obligations de signalétique et, dans certains cas, de notification au Garant entrent en jeu. Le principe directeur est simple : informer les personnes que la zone est surveillée est toujours le bon choix, pas seulement le choix légal.
![log.jpg](log.jpg)
*Capture d'écran du terminal avec le système en fonctionnement, avec la reconnaissance d'objets et l'alerte au moment de l'entrée d'une personne.*

## Les pistes ouvertes

Le projet dans sa forme actuelle est un point de départ fonctionnel, pas un point d'arrivée. Les extensions naturelles sont diverses, avec une complexité croissante.

L'étape suivante la plus évidente est la reconnaissance faciale pour distinguer les résidents des étrangers. La bibliothèque `face_recognition` de Python permet de construire une archive de visages connus et de filtrer les alertes en conséquence : si c'est moi qui entre dans la maison, pas de notification. Si c'est quelqu'un que le système n'a jamais vu, alerte. Le code supplémentaire représente quelques dizaines de lignes.

Une intégration avec des capteurs PIR passifs, les capteurs de mouvement infrarouges classiques, permettrait d'activer YOLO uniquement en présence de mouvement, réduisant ainsi considérablement la consommation d'énergie pendant les périodes d'inactivité. Dans l'implémentation actuelle, la webcam tourne et le modèle analyse les images en continu, même quand la pièce est vide depuis des heures.

Le support multi-caméras nécessiterait d'instancier plusieurs processus parallèles, un pour chaque webcam, avec un système centralisé de gestion des alertes. Un tableau de bord web léger construit avec Flask ou FastAPI permettrait de visualiser l'état du système à distance. Autant d'extensions réalisables en quelques jours de travail.

## Le local gagne (presque toujours)

Chaque fois que je construis quelque chose de ce genre, je me retrouve face à une question plus large : pourquoi le faire en local alors qu'il existe des API cloud pour la vision par ordinateur qui fonctionnent avec trois lignes de code ?

La réponse n'est pas idéologique. Elle est pratique.

Comme je l'ai déjà évoqué dans d'autres contextes sur ce portail, les modèles locaux ont atteint un niveau de maturité qui rend le choix entre local et cloud véritablement dépendant du cas d'usage, et non de l'hypothèse automatique selon laquelle le cloud serait toujours supérieur. Pour un système de vidéosurveillance domestique, les avantages du local sont difficiles à surpasser : les images de votre maison ne sortent jamais de votre PC, il n'y a pas de coûts variables, le système fonctionne même sans Internet une fois configuré, il n'y a pas de dépendance vis-à-vis des politiques tarifaires de tiers qui peuvent changer.

Le cloud gagne dans d'autres scénarios : quand des dizaines de caméras sont nécessaires, quand la puissance de calcul locale n'est pas suffisante, quand les modèles requis sont trop grands pour tourner en local, quand la maintenance de l'infrastructure est un fardeau insupportable. Mais pour une expérience domestique comme celle-ci, le cloud aurait été un surcoût sans bénéfices concrets.

Il y a cependant une considération qu'il vaut toujours la peine d'expliciter : ONNX et YOLOv8n sont des outils matures, documentés, avec des communautés actives. Ce n'est pas de la magie noire réservée aux spécialistes. C'est de l'ingénierie appliquée que n'importe qui ayant de la curiosité et quelques heures devant lui peut reproduire. C'est peut-être l'aspect le plus significatif de toute l'expérience : pas le système de sécurité en soi, mais la démonstration que la distance entre la "technologie IA" et la "chose qui fonctionne sur mon PC" s'est raccourcie au point de devenir presque insignifiante.

---

*Le code est disponible sur le dépôt [GitHub Security-System-Yolo](https://github.com/Dario-Fe/Security-System-Yolo)*
