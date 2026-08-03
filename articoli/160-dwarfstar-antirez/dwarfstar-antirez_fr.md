---
tags: ["Research", "Training", "Applications"]
date: 2026-08-03
author: "Dario Ferrero"
---

# DwarfStar : l'étoile naine qui éclaire l'IA de frontière locale
![dwarfstar-antirez.jpg](dwarfstar-antirez.jpg)

*Il y a une scène dans le roman *Neuromancer* de William Gibson où le protagoniste se connecte directement à une intelligence immense, distribuée sur des serveurs inaccessibles, via une connexion qu'il ne contrôle pas et qu'il ne possède pas. C'était de la science-fiction en 1984. En 2026, c'est, plus ou moins, la réalité quotidienne de quiconque utilise ChatGPT, Claude ou Gemini : des modèles gigantesques, hébergés sur des infrastructures à plusieurs milliards de dollars, accessibles uniquement via une connexion internet et moyennant un abonnement mensuel ou un coût par token. Votre conversation, vos données, votre raisonnement : tout passe par quelque part que vous ne voyez pas et que vous ne gérez pas.*

DwarfStar est, dans son essence, une tentative de renverser cette équation. Pas une alternative commerciale, pas un wrapper autour d'autre chose : un moteur d'inférence écrit de zéro, en C, maniaquement optimisé pour un seul modèle, distribué gratuitement sous licence MIT. Et derrière, il y a une signature que la communauté tech reconnaît immédiatement : celle de Salvatore Sanfilippo, alias *antirez*, le programmeur sicilien qui a inventé Redis en 2009.

## Antirez : le programmeur qui fait une seule chose, et la fait bien

Salvatore Sanfilippo est né à Campobello di Licata, en Sicile, le 7 mars 1977. Il développe très tôt un intérêt pour la programmation, commençant à écrire du code à l'âge de cinq ans sur un ordinateur Texas Instruments offert par son père. À partir de là, c'est une histoire de déviations fructueuses : il quitte l'architecture pour l'informatique, arrive dans la sécurité réseau dans les années quatre-vingt-dix, invente l'*idle scan*, une technique de scan furtif des ports réseau encore implémentée aujourd'hui dans nmap, puis, presque par hasard, construit Redis.

Redis est un magasin de données in-memory open source, créé par Sanfilippo et publié pour la première fois le 26 février 2009. Au lieu de se contenter d'être un cache clé-valeur, il offre des structures de données natives riches (chaînes, hashes, listes, ensembles ordonnés, streams) opérées atomiquement par le serveur. La philosophie qui le gouverne est celle qu'antirez apporte à chaque projet : faire moins. Un système petit et simple que vous pouvez garder en tête bat un système grand et complet.

Redis est aujourd'hui utilisé par pratiquement toutes les entreprises d'internet, d'Airbnb à Uber, de Snapchat à Meta, jusqu'à Amazon et Twitch. Malgré cela, Sanfilippo a toujours choisi de vivre à Catane, loin de la frénésie de la Silicon Valley, privilégiant la famille et les stimulations intellectuelles. En juin 2020, il annonce son retrait de la maintenance de Redis pour se consacrer à d'autres projets, avant de revenir en décembre 2024 dans le rôle de Redis evangelist, développant le nouveau type de données Vector Set.

Le respect que la communauté tech lui porte ne provient pas seulement de la grandeur technique de Redis. Il vient de quelque chose de plus rare : la cohérence. Antirez ne court pas après les tendances, n'accumule pas les startups, ne monétise pas sa réputation. Il écrit du logiciel parce qu'il aime écrire du logiciel, et quand quelque chose le passionne, il le construit avec un soin quasi artisanal. DwarfStar est exactement cela.

## Le problème : les modèles de frontière vivent sur Saturne

Pour comprendre ce qui fait de DwarfStar un projet extraordinaire, il faut d'abord comprendre le problème qu'il aborde. Les modèles linguistiques les plus capables, DeepSeek V4 Flash, mais aussi les différents GPT et Claude, ne sont pas de petits programmes. Ce sont des réseaux neuronaux avec des centaines de milliards de paramètres, dont chacun est un nombre à virgule flottante qui occupe de l'espace en mémoire. Un modèle comme DeepSeek V4 Flash possède 284 milliards de paramètres au total. Si nous voulions les charger tous en mémoire sous leur forme originale en pleine précision, nous aurions besoin d'environ 568 gigaoctets de RAM. La RAM des serveurs GPU haut de gamme, la fameuse VRAM des cartes NVIDIA, se mesure en dizaines de gigaoctets par carte. Il faudrait plusieurs machines connectées en réseau, des infrastructures coûtant des dizaines de milliers d'euros, une consommation électrique digne d'une petite industrie.

Le MacBook de 128 Go, dont il faut dire qu'il n'est pas à la portée de tous, semble tout de même à des années-lumière de cette réalité. Pourtant, DeepSeek V4 Flash appartient à une famille d'architectures qui contient, cachée dans sa structure, la clé de la solution.

## Mixture of Experts : quand la spécialisation devient un avantage

DeepSeek V4 Flash est construit sur une architecture appelée Mixture of Experts, ou MoE. L'idée, désormais connue, est assez intuitive : au lieu d'avoir un seul réseau neuronal dense qui traite chaque token, le modèle est composé de dizaines de réseaux spécialisés, les "experts", et pour chaque token, seuls certains sont activés, sélectionnés par un mécanisme de routage. DeepSeek V4 Flash possède 284 milliards de paramètres au total mais seulement 13 milliards de paramètres actifs pour chaque token généré. C'est comme avoir une encyclopédie de mille volumes, mais ne devoir lire que quelques livres pour répondre à une question spécifique.

Cela a une conséquence pratique énorme : la vitesse de génération ne dépend pas des 284 milliards de paramètres, mais seulement des 13 milliards actifs. Et c'est là que s'insère la première grande intuition de DwarfStar.

Les quantisations à 2 bits fournies pour DwarfStar ne sont pas un raccourci : elles se comportent bien, fonctionnent avec les agents de code, exécutent les appels aux outils de manière fiable. Les quantisations à 2 bits utilisent une compression très asymétrique : seuls les experts MoE routés sont quantisés, gate et up en IQ2_XXS, down en Q2_K. Ceux-ci constituent la majeure partie de l'espace du modèle : les autres composants, experts partagés, projections, routage, sont laissés intacts pour garantir la qualité.

En termes concrets : les parties du modèle qui sont utilisées souvent et qui portent le plus de "signal" sont préservées à la précision originale. Les experts qui sont activés rarement et qui contribuent moins à la qualité du résultat final sont compressés agressivement. Le résultat est un fichier GGUF d'environ 81 gigaoctets qui maintient une qualité étonnamment proche du modèle original. Mais comment déterminer quelle partie du modèle porte le plus de signal ? Grâce à un processus empirique appelé *imatrix calibration* : le modèle est exécuté sur des jeux de données réels couvrant le coding, les mathématiques, le raisonnement et le tool calling, et on mesure comment les différentes parties du réseau s'activent. Cette carte d'importance guide ensuite les décisions de compression.

C'est la différence entre couper un arbre avec une tronçonneuse et le tailler avec soin. La différence est une plante vivante plutôt que morte.

## Quand la RAM ne suffit pas : le disque comme extension de la mémoire

Même avec 81 gigaoctets de poids compressés, le problème n'est pas totalement résolu. Un MacBook avec 64 ou 96 Go de RAM doit trouver un moyen de gérer un modèle qui ne rentre pas complètement. Et le contexte, la mémoire de la conversation en cours, occupe un espace supplémentaire au fur et à mesure que la conversation s'allonge.

DwarfStar introduit un mode SSD streaming uniquement pour Metal : dans ce mode, les poids non routés restent résidents, tandis que les experts MoE routés sont conservés dans un cache in-memory et chargés depuis le fichier GGUF en cas de cache miss. Le streaming n'est pas aussi rapide que le chargement de l'ensemble du modèle en RAM, mais il est utile car les experts routés dominent la taille du modèle et les SSD modernes des Mac sont assez rapides pour rendre les cache miss tolérables.

Le mécanisme est élégant dans sa simplicité conceptuelle : DwarfStar conserve en RAM les poids des experts appelés le plus fréquemment, les "chauds", et charge du disque les autres uniquement lorsque le routeur décide de les activer. Les SSD NVMe modernes, ceux montés sur les MacBook et les Mac Studio, atteignent des vitesses de lecture séquentielle de l'ordre de 7 à 10 Go/s. Suffisamment rapides pour ne pas faire du chargement le goulot d'étranglement principal, du moins pour les tâches qui ne nécessitent pas une latence minimale.

Cela signifie qu'en pratique, un MacBook de 64 Go peut exécuter un modèle de 284 milliards de paramètres. Pas à la même vitesse qu'un Mac Studio avec 512 Go de RAM unifiée, certes, mais à une vitesse suffisante pour un travail réel.

## Contexte, sessions et la mémoire qui survit au redémarrage

Les modèles linguistiques modernes parlent de "fenêtres de contexte" comme si elles étaient évidemment illimitées. Elles ne le sont pas. Chaque token dans la conversation occupe de l'espace dans la KV cache, la structure de données que le modèle utilise pour se souvenir de ce qui a été dit, et la KV cache croît linéairement avec la longueur du contexte. DeepSeek V4 Flash possède une fenêtre de contexte d'un million de tokens, et la KV cache est incroyablement compressée, permettant l'inférence sur des contextes longs sur des ordinateurs locaux et la persistance de la KV cache sur disque.

DwarfStar exploite cette caractéristique avec un système de sessions persistantes sur disque. Lorsqu'une conversation est interrompue, que le serveur est redémarré, qu'on change de session, qu'on veut reprendre le travail le lendemain, le système n'a pas à retraiter tous les tokens précédents de zéro. La session sauvegardée contient l'état exact de la KV cache, le point de contrôle des tokens, même la distribution de probabilité du dernier token généré. La reprise est quasi instantanée.

Cela résout l'un des problèmes les plus frustrants des agents IA locaux : le fait que chaque nouvel appel à l'API doive renvoyer l'intégralité du contexte, payant le coût computationnel du *prefill* à chaque fois. Avec DwarfStar, les prefill coûteux sont sauvegardés et réutilisés. Un agent de code qui utilise un system prompt long de 25 000 tokens, comme le fait Claude Code, ne paie ce coût qu'une seule fois.

## Deux machines valent mieux qu'une

Le point le plus récent de l'évolution de DwarfStar concerne la distribution de l'inférence sur plusieurs machines. La branche distribuée est désormais dans le code principal : l'inférence distribuée passe de la théorie au code exécutable. Le fichier GGUF réside sur chaque machine, mais chaque nœud ne charge que sa portion de couches via le flag --layers avec des plages inclusives, sans conserver en RAM les poids qui ne lui appartiennent pas. Architecture coordinateur/worker : une machine agit comme coordinateur (tokenisation, échantillonnage et le prompt initial), les autres sont des workers qui traitent leur propre portion et transmettent les activations via TCP.

L'approche est celle du *layer split* : la machine A charge et traite les N premières couches du transformer, passe les activations à la machine B qui traite les couches restantes, et le résultat revient au coordinateur pour l'échantillonnage. Le transfert de données entre les machines est minimal, car seules les activations intermédiaires sont transférées, des vecteurs relativement petits, et non les poids du modèle.

Avec DwarfStar, le Mac Studio M3 Ultra de 512 Go peut exécuter DeepSeek V4 PRO à 150 tokens/s de prefill et environ 10-13 tokens/s de décodage, ce qui n'est pas exceptionnel mais à un niveau utilisable pour certains cas d'usage. Deux Mac Studio connectés pourraient distribuer le plus grand modèle, DeepSeek V4 PRO en pleine précision, et bénéficier d'un prefill plus rapide grâce au micro-batching. Ceux qui possèdent deux MacBook M5 Max de 128 Go peuvent désormais diviser la charge d'un seul modèle au lieu de les utiliser séparément.

Antirez explore également des approches plus expérimentales : l'ensemble de modèles, où deux instances du même modèle (ou de modèles différents) tournent sur des machines séparées et combinent leurs logits, la distribution de probabilité sur les tokens suivants, pour produire une sortie meilleure que celle que chacun produirait seul. C'est une technique étudiée dans la littérature mais rarement implémentée de manière pratique.

## Les chiffres : à quoi s'attendre en pratique

Les benchmarks de DwarfStar sont mesurables et publiés dans la documentation officielle du projet. Sur un MacBook Pro M3 Max de 128 Go avec une quantisation à 2 bits :

Sur des prompts courts, le prefill atteint 58,52 tokens/s et la génération 26,68 tokens/s. Sur des prompts longs d'environ 11 700 tokens, le prefill monte à 250,11 tokens/s grâce au chunked prefill, tandis que la génération descend à 21,47 tokens/s en raison du contexte croissant.

Sur Mac Studio M3 Ultra de 512 Go, les chiffres sont plus généreux : prefill à 84,43 tokens/s sur des prompts courts, génération à 36,86 tokens/s, et sur des prompts longs, le prefill atteint 468,03 tokens/s avec une génération à 27,39 tokens/s.

Le MacBook M5 Max de 128 Go, selon antirez, peut exécuter DeepSeek V4 Flash en quantisation 2 bits à environ 460 tokens/s de prefill et 25 tokens/s de génération, avec une courbe de dégradation acceptable au fur et à mesure que le contexte augmente.

Pour donner un point de repère concret : lire à haute voix signifie prononcer environ 150 mots par minute, soit environ 200 tokens. À 26 tokens par seconde, DwarfStar génère du texte à un peu plus d'un huitième de cette vitesse, lent par rapport aux services cloud, mais assez rapide pour une utilisation interactive réelle.
![tabella1.jpg](tabella1.jpg)
[Image tirée du dépôt GitHub](https://github.com/antirez/ds4)

## GLM 5.2 et l'orientation du projet

DwarfStar est né comme un moteur délibérément étroit : une seule famille de modèles, supportée en profondeur et correctement au lieu de tout supporter superficiellement.

Mais les ambitions grandissent. Au cours des dernières heures, antirez a publié une vidéo intitulée "Considérations sur l'implémentation de GLM 5.2 dans DwarfStar". C'est explicitement un travail en cours, le signal est clair : le projet n'a pas l'intention de s'arrêter à DeepSeek. L'architecture MoE avec KV cache compressée est devenue une caractéristique partagée par plusieurs modèles de frontière, et DwarfStar est équipé pour la poursuivre.

Il faut dire honnêtement : le projet est encore en qualité bêta, comme antirez lui-même le déclare dans le README. Certaines fonctionnalités sont expérimentales, le support CUDA est plus récent que celui de Metal, et certains comportements pourraient changer. Mais la trajectoire est celle d'un projet qui a déjà démontré sa capacité à faire des choses qui semblaient impossibles il y a quelques semaines.

## La frontière, ouverte à tous (presque)

Il y a un mot qui revient de manière obsessionnelle dans toute discussion sur DwarfStar : *démocratisation*. C'est un mot galvaudé, souvent utilisé pour couvrir des produits commerciaux d'un voile de rhétorique progressiste. Ici, le terme a un sens plus précis et plus honnête.

DwarfStar est gratuit. Le code est MIT. Les quantisations sont publiées sur Hugging Face sans restrictions. Il n'y a pas de version Pro, il n'y a pas de forfait Enterprise, il n'y a pas de clé API à acheter. Quiconque possède un Mac avec 96 Go de RAM ou un DGX Spark à 5 000 dollars, ou, avec le SSD streaming, encore moins, peut tout télécharger et avoir un agent IA de près de 300 milliards de paramètres qui tourne localement, hors ligne, sans envoyer un seul token à un serveur distant.

La confidentialité n'est pas un argument secondaire. Un agent qui connaît le code de votre entreprise, vos documents, vos conversations internes ne devrait pas nécessairement transiter par les serveurs d'Anthropic ou d'OpenAI. Avec DwarfStar, ce n'est pas le cas.

Bien sûr, le matériel reste un obstacle réel. 128 Go de RAM unifiée n'est pas une configuration à cinquante euros. Un MacBook Pro M3 Max dans la version nécessaire commence aux alentours de 4 000 euros ; un Mac Studio M3 Ultra de 192 Go dépasse les 7 000. Ce n'est pas à la portée de tous, et il est honnête de le dire. Mais c'est à la portée de nombreux professionnels, studios, PME, chercheurs. Et le coût de cette même puissance de calcul dans le cloud, sur une base annuelle, dépasse largement le coût du matériel, sans compter la valeur de la confidentialité et de l'indépendance.

Il y a ensuite une dimension plus subtile. Chaque fois qu'un modèle de frontière tourne sur du matériel grand public, chaque fois que quelqu'un démontre qu'il n'y a pas besoin d'un data center pour faire du raisonnement sérieux, le plan incliné se déplace légèrement. Les matériels s'améliorent : le MacBook M5 Max avec 128 Go est déjà le meilleur équilibre coût-performance disponible pour l'inférence locale en 2026. Les modèles s'améliorent et deviennent plus efficaces. Et il y a des gens comme Sanfilippo qui travaillent, pour le plaisir de le faire, pour la satisfaction de bien le faire, pour réduire encore l'écart.

Redis a mis des années à devenir la base de données la plus aimée au monde. DwarfStar possède déjà 15 500 étoiles sur GitHub quelques semaines seulement après son lancement, avec des contributeurs actifs, des ports pour CUDA et ROCm, des benchmarks publiés sur DGX Spark, MacBook et Mac Studio. La vitesse d'adoption en dit long sur l'urgence du besoin qu'il satisfait.

Il y a un personnage dans la bande dessinée d'Alan Moore, *From Hell* (pas la version hollywoodienne), qui observe que le temps est toujours maintenant, que tout se passe simultanément. Le passé du local AI movement et son futur se touchent dans un fichier de 81 gigaoctets que vous pouvez télécharger maintenant, sur un ordinateur que vous avez sur votre bureau. Antirez l'a construit. Le reste, comme on dit, appartient à l'histoire.

---

*Le dépôt officiel de DwarfStar est disponible sur [GitHub](https://github.com/antirez/ds4). Les quantisations officielles pour DeepSeek V4 Flash sont publiées sur [Hugging Face](https://huggingface.co/antirez/deepseek-v4-gguf). Le blog de Salvatore Sanfilippo est accessible sur [antirez.com](https://antirez.com).*
