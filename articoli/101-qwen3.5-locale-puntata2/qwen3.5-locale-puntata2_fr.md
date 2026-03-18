---
tags: ["Generative AI", "Applications", "E-learning"]
date: 2026-03-18
author: "Dario Ferrero"
---

# L'IA à la maison : LM Studio et Qwen 3.5 sur mon PC - Épisode 2
![qwen3.5-locale-puntata2.jpg](qwen3.5-locale-puntata2.jpg)

*Suite de l'[Épisode 1](https://aitalk.it/it/qwen35-locale-puntata1.html), où nous avons décrit la configuration matérielle, le choix de LM Studio comme framework, et les trois premiers tests : raisonnement scientifique sur le mécanisme de Higgs, lecture multimodale d'un tableur flou, et génération de code pour un problème NP-difficile.*

La conversation autour de Qwen 3.5 au cours des deux dernières semaines ne s'est pas limitée aux forums techniques internationaux. En Italie, des voix comme celle de [Salvatore Sanfilippo](https://www.youtube.com/watch?v=NDBQq_NzxiE), parmi les experts les plus suivis sur le thème de l'intelligence artificielle appliquée, ont attiré l'attention d'un public plus large sur le modèle, contribuant à faire de cette sortie l'un des sujets les plus discutés de la saison dans l'écosystème italien de l'IA. Ce n'est pas du battage médiatique sur les réseaux sociaux : c'est la reconnaissance que quelque chose de structurel est en train de changer dans les modèles open-weight, et que ce changement est enfin assez tangible pour mériter l'attention au-delà des cercles de chercheurs.

Les trois tests qui concluent ce deuxième épisode ont été conçus précisément pour aborder les domaines qui intéressent le plus ceux qui ne sont pas chercheurs mais utilisent l'IA pour travailler, planifier, analyser et organiser : la capacité à raisonner dans plusieurs langues tout en maintenant une cohérence culturelle, la gestion de documents longs avec une précision chirurgicale, et la compréhension de l'espace physique à travers une image.

## Test 4 — Agent de voyage en trois langues

Le quatrième test portait sur deux des capacités les plus mises en avant du modèle : le support multilingue étendu (Qwen 3.5 supporte 201 langues) et les performances d'agent sur des tâches de planification complexes. J'ai imaginé un client français ne parlant pas anglais, souhaitant visiter Tokyo et Kyoto en mettant l'accent sur les temples historiques et la cuisine de rue. La demande était articulée : un itinéraire de cinq jours dans un français impeccable, avec des conseils pratiques sur les transports et les barrières linguistiques, suivi d'une section en italien pour un second voyageur souhaitant suivre le même parcours.

La réponse aurait pu être un itinéraire générique généré par interpolation d'informations provenant d'une base de données de guides de voyage. Ce ne fut pas le cas. Le français était celui d'un consultant en voyage haut de gamme : formel mais chaleureux, précis sans être bureaucratique. L'itinéraire présentait une logistique réelle : arrivée à Tokyo et première immersion à Asakusa et au Senso-ji, deuxième jour entre le sanctuaire Meiji et l'ancien marché de Tsukiji avec l'indication que les sushis s'y mangent au comptoir en payant à l'unité, troisième jour avec le Shinkansen vers Kyoto et promenade dans les bambouseraies d'Arashiyama en fin d'après-midi, quatrième jour avec la montée aux torii de Fushimi Inari avec l'avertissement explicite de porter des chaussures confortables, soirée à Pontocho pour avoir la chance de croiser des geishas. Cinquième jour au marché Nishiki, « le ventre de Kyoto », comme l'a appelé le modèle, avant le départ.

Les détails font la différence entre une information et une connaissance : savoir que Suica et Pasmo sont les cartes rechargeables pour les transports, que Google Translate avec packs hors ligne est presque indispensable au Japon, que l'on enlève ses chaussures dans les temples. Tout y était, tout était correct. La section en italien était un condensé pratique, écrit dans une langue fluide et utile, sans répéter de manière fastidieuse tout l'itinéraire mais en synthétisant les conseils essentiels pour celui qui connaît déjà le parcours. Le passage d'une langue à l'autre n'a pas fait baisser la qualité : le ton, la pertinence culturelle et la précision sont restés stables.

**Note : 5/5.** Un agent qui connaît le Japon comme un guide touristique, écrit en français comme un locuteur natif et synthétise en italien sans perdre le fil.

## Test 5 — L'aiguille dans la botte de foin de 460 pages

Le cinquième test était le plus exigeant d'un point de vue technique, et probablement le plus pertinent pour ceux qui utilisent l'IA dans des contextes professionnels d'analyse documentaire. J'ai chargé dans LM Studio l'[Artificial Intelligence Index Report 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report) du Stanford HAI : 460 pages et environ 20 Mo, des dizaines de milliers de mots, des graphiques, des tableaux, des chapitres thématiques. Un volume qu'aucun être humain ne lit du début à la fin en une seule session. La question était apparemment simple : me trouver les données sur la croissance de la génération vidéo et m'indiquer à quelle page elles se trouvent.

La première fois, aucune réponse. La deuxième, le silence. La troisième, encore. Lors des trois tentatives, le modèle effectuait le raisonnement, qui est visible et consultable, mais à la fin, il ne produisait pas de résultat. J'ai dû le solliciter explicitement, en précisant que le modèle ne produit parfois pas de résultat dans le chat alors qu'il a traité la demande. À la quatrième tentative, la réponse est arrivée et elle était d'une précision surprenante.

Le modèle a identifié les pages 126 et 127 du Chapitre 2 (Technical Performance), section « Image and Video ». Il a décrit ce qu'elles contenaient : la page 126 avec les fiches des modèles Google Veo, Meta Movie Gen et OpenAI Sora, avec les graphiques de préférence des utilisateurs (Figures 2.3.11 et 2.3.12) ; la page 127 avec la comparaison entre les vidéos générées au fil du temps. Puis il a spontanément récupéré un exemple spécifique : le prompt « Will Smith eating spaghetti », devenu au fil du temps une petite étude de cas informelle sur la qualité des vidéos générées par l'IA, le genre de détail culturel qu'un bon chercheur aurait inséré dans une note de bas de page.

Le comportement de blocage des trois premières tentatives est une limite réelle, à signaler honnêtement. Il dépend probablement de la masse de données à traiter et de la manière dont LM Studio gère les tokens de contexte dans des fenêtres très larges. Ce n'est pas un problème qui se résout en cinq minutes, il nécessite une compréhension de sa propre configuration et de la patience. Mais quand le modèle répond, il répond bien.

**Note : 4,5/5.** Précision millimétrique dans la récupération d'informations d'un document de 460 pages, pages exactes, figures numérotées, exemples culturels. Un demi-point perdu pour les trois tentatives à vide, un comportement dont le flux de travail réel doit tenir compte.

## Test 6 — Le géomètre du chaos domestique

Le dernier test était peut-être le plus inhabituel, et celui qui a produit la réponse la plus riche narrativement. J'ai téléchargé en ligne une photo de basse qualité d'une pièce en proie au désordre : des vêtements partout, un lit défait, un bureau submergé de papiers, des étagères saturées, des objets éparpillés sur le sol. J'ai chargé la photo dans LM Studio et j'ai demandé au modèle de décrire la disposition des objets et de proposer une stratégie pour gagner de l'espace.

La description de la pièce était visuellement fidèle : le panier bleu au centre qui occupe le passage principal, les piles de vêtements colorés divisées par couleurs et matières, les pantoufles marron et les baskets éparpillées près de l'entrée, le lit à droite avec le linge accumulé rendant le chevet inaccessible, le bureau à gauche « encombré comme un nid de désordre visuel ». Mais le détail le plus impressionnant a été celui-ci : le modèle a remarqué que le miroir sur le mur reflétait le meuble blanc et quelques boîtes sur le sol, prouvant qu'il percevait non seulement les objets visibles mais aussi les relations spatiales générées par les reflets, une compréhension tridimensionnelle de l'espace qui n'était pas évidente.

La stratégie de rangement proposée suivait une logique impeccable : d'abord libérer le centre de la pièce pour créer un passage sûr, puis vider le bureau pour catégoriser, ensuite faire le lit pour retrouver une surface visuelle, enfin ranger dans les armoires désormais accessibles. Chaque étape avait une motivation : le centre d'abord car c'est le risque de chute le plus immédiat, le lit ensuite car le faire change visuellement la perception de toute la pièce, pas seulement sa fonctionnalité. C'est la logique de celui qui a compris non seulement ce qu'il y a dans cette pièce, mais comment l'espace fonctionne pour celui qui l'habite.

**Note : 5/5.** Compréhension spatiale tridimensionnelle, analyse des reflets, stratégie d'intervention motivée étape par étape. Un architecte d'intérieur n'aurait pas fait mieux.
![riconosimenti-img.jpg](riconosimenti-img.jpg)
*Capture d'écran d'une partie de la réponse de Qwen 3.5, à la demande d'analyser l'image chargée.*

## Le bilan final

Six tests, six domaines, un tableau assez complet pour tirer les conclusions, avec la conscience que cela reste une expérience personnelle, non une évaluation systématique.

Ce qui ressort clairement, c'est que Qwen 3.5 9B, à 30 tokens par seconde sur un GPU grand public de 16 Go de VRAM, fait des choses qui, il y a encore un an, auraient nécessité l'accès à des API de pointe payantes. Il explique la physique quantique avec la clarté d'un bon professeur, lit des tableaux flous comme un analyste, écrit du code avec une conscience théorique des limites, planifie des voyages en plusieurs langues avec une cohérence culturelle, trouve des pages spécifiques dans un rapport de 460 pages, décrit une pièce en désordre et reconnaît ses reflets. Tout cela fonctionne hors ligne, sans envoyer un seul octet à aucun serveur.

Les limites existent et doivent être dites sans détour. Le comportement de blocage sur des sorties très longues ou des contextes étendus est le problème principal : il nécessite des sollicitations explicites et introduit une incertitude dans le flux de travail que ceux qui utilisent ces outils en production doivent gérer. La première tentative interrompue lors du test de codage, les trois silences lors du test documentaire, ne sont pas des défauts négligeables, ce sont des comportements qu'un utilisateur professionnel doit apprendre à anticiper.

Reste également ouverte une question qu'aucun test local ne peut résoudre : la confidentialité et la provenance des données d'entraînement. Qwen est un projet d'Alibaba Cloud, une entreprise chinoise soumise à la législation de Pékin. Exécuter le modèle localement résout la question de la transmission des données lors de l'inférence (les prompts ne sortent pas de la machine), mais ne dit rien sur ce que le modèle a vu pendant l'entraînement, ni sur d'éventuels biais liés au contexte géopolitique de ceux qui l'ont créé. Pour de nombreux usages personnels et professionnels, la question est hors de propos ; pour d'autres, dans des domaines réglementés, dans des contextes où la souveraineté des données est une contrainte légale, il vaut la peine d'y réfléchir avant de l'intégrer dans un flux de travail critique.

Sur le front du cloud, la compétition reste asymétrique pour les tâches nécessitant un raisonnement approfondi en plusieurs étapes, une connaissance encyclopédique mise à jour en temps réel et la gestion de contextes massifs sans comportements imprévisibles. Les modèles de pointe comme Claude, ChatGPT et Gemini jouent encore sur un terrain différent pour ces scénarios. Mais l'écart se réduit à chaque sortie, et la direction est claire.

## L'envie de continuer

Cette expérience a été ce que j'espérais qu'elle soit : instructive, concrète, parfois surprenante. Installer un modèle de cette qualité localement, sur un PC qui n'est pas une station de travail à cinq mille euros, et obtenir des réponses qui soutiennent la comparaison avec les meilleurs services cloud, aurait semblé hors de portée il y a seulement douze mois. Ce ne l'est plus.

Qwen 3.5 9B est certainement le modèle open-weight le plus discuté des dernières semaines, et la renommée qu'il s'était forgée avec les versions précédentes de la famille n'était pas infondée. Mais ce n'est aussi qu'un des points de cet écosystème en évolution rapide. Pour ceux qui ont moins de VRAM ou recherchent l'excellence en codage, [Phi-4-mini de Microsoft](https://huggingface.co/microsoft/Phi-4-mini-instruct) mérite l'attention. Pour ceux qui travaillent principalement en italien ou dans des langues européennes, les variantes de [Mistral](https://mistral.ai/) présentent des caractéristiques spécifiques dignes d'intérêt. Chaque modèle excelle dans un domaine et cède dans un autre : le choix dépend toujours du cas d'utilisation, et seul celui qui est devant le clavier connaît son cas d'utilisation.

Le point important n'est cependant pas de savoir quel modèle choisir. Le point important est que ce choix existe, qu'il est accessible et qu'il fonctionne. Les LLM locaux, ou SLM si vous préférez la dénomination plus précise, ne sont plus une expérience pour passionnés dotés de matériel de laboratoire. Ce sont des outils actuels, fonctionnels, améliorables, respectueux de la vie privée et qui, avec un niveau de matériel à peine supérieur au standard grand public, deviennent de puissants alliés pour concevoir, écrire, analyser et construire.

Il suffit d'avoir envie de se mettre au travail. Et avec ces outils, le travail devient de plus en plus accessible.
