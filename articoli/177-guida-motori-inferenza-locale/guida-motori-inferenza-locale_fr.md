---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-09-11
author: "Dario Ferrero"
---

# Guide des moteurs d'inférence et des clients pour LLM locaux
![guida-motori-inferenza-locale.jpg](guida-motori-inferenza-locale.jpg)

*Il y a un moment précis où une technologie cesse d'être une promesse et devient un outil. Ce n'est pas lors de la sortie du communiqué de presse, ce n'est pas lorsque les benchmarks font le tour des réseaux sociaux, mais lorsqu'une personne normale, avec un PC normal, s'assied, télécharge quelque chose et décide de comprendre réellement ce qui se passe. En 2026, ce moment est arrivé avec force pour l'inférence locale, et avec lui est apparu un problème que presque personne n'expliquait clairement avant de se retrouver confus devant la console de commande : ce n'est plus le modèle qui manque, c'est la clarté sur *comment* le faire tourner.*

La raison de tout cela est simple mais sous-estimée. Comme le souligne le [rapport Currents de DigitalOcean](https://www.digitalocean.com/currents/february-2026), 64 % des entreprises intègrent aujourd'hui des modèles via des API de fournisseurs tiers, tandis que seulement 15 % se consacrent principalement à entraîner des modèles à partir de zéro : l'essentiel du travail est donc désormais de l'intégration plus que de la construction. Le cloud n'est pas mort, il reste dominant, mais ce qui semblait être une asymétrie insurmontable entre d'énormes modèles propriétaires et des modèles locaux « de secours » s'amenuise à une vitesse qui surprend même les observateurs les plus attentifs. Qwen3.5-9B, avec environ treize fois moins de paramètres que certains géants du cloud, affiche sur le benchmark GPQA Diamond — le test de référence pour le raisonnement de niveau universitaire avancé — un score de 81,7 contre 80,1 pour GPT-OSS-120B d'OpenAI, comme le rapporte la [page officielle du modèle sur Hugging Face](https://huggingface.co/Qwen/Qwen3.5-9B). L'écart est minime, ce n'est pas un abîme infranchissable, mais le constat demeure : un modèle énormément plus petit tient tête à un modèle beaucoup plus grand, et c'est un changement de paradigme sur ce que signifie « petit » en 2026.

Mais avec la démocratisation du matériel est aussi arrivé un nouveau labyrinthe : si vous téléchargez un modèle open-weight et le mettez sur votre PC, qu'utilisez-vous pour le faire tourner ? La réponse dépend d'une distinction que presque personne n'explique au préalable et qui organise la quasi-totalité de l'écosystème : la différence entre le **moteur** d'inférence et le **client** que ce moteur enveloppe.

Avant d'aller plus loin, il convient d'être clair sur ce qu'est cet article et ce qu'il n'est pas. Ce qui suit est une analyse de caractéristiques et de spécifications techniques, construite sur la documentation officielle, des dépôts, des changelogs et une vérification croisée entre des sources fiables. Ce n'est pas un benchmark scientifique, il n'y a pas de protocole de test évalué par des pairs, il n'y a pas d'échantillon statistiquement significatif. Je n'ai testé sur du matériel réel que deux produits de ce panorama, et je les cite à titre d'illustration, non comme structure porteuse. Ceux qui cherchent des chiffres certifiés trouveront les benchmarks sur les pages officielles de chaque produit. Ceux qui veulent comprendre ce que ces outils promettent de faire, et avec quel matériel, peuvent poursuivre leur lecture.

La vérité, comme souvent dans ce domaine, ne se trouve pas dans un tableau. Elle réside dans la compréhension de ce que chaque outil fait réellement, et de ce qu'il vous demande de céder en échange.

## Le moteur et la voiture

Pour exécuter un modèle linguistique en local, il faut deux choses : le modèle lui-même — un fichier de plusieurs gigaoctets — et quelque chose qui serve d'interprète entre le matériel et le modèle, en gérant la mémoire, la tokenisation et l'inférence. Sans cette couche intermédiaire, télécharger les poids d'un modèle revient à avoir les fichiers d'un film sans lecteur vidéo. Et c'est là que s'ouvre la ligne de partage qui sépare presque tout l'écosystème.

D'un côté, il y a les **moteurs d'inférence**, également appelés runtimes ou inference engines. Ce sont des bibliothèques et des serveurs de bas niveau, souvent headless, qui gèrent directement le chargement du modèle, l'ordonnancement des requêtes, l'utilisation du CPU et du GPU, les quantifications et les différents formats de poids. Ils n'ont presque jamais de véritable interface graphique, communiquent via des API, et leur succès se mesure en throughput et en latence. Le public cible est le développeur, l'ingénieur MLOps, celui qui doit servir un modèle à des dizaines d'utilisateurs. Ils sont le moteur nu d'une voiture, ce que vous voyez quand quelqu'un ouvre le capot pour vous le montrer.

De l'autre côté, il y a les **clients**, les runners ou les produits pour l'utilisateur final. Ce sont des applications prêtes à l'emploi qui prennent un ou plusieurs moteurs et les enveloppent dans quelque chose d'utilisable : un navigateur de modèles, un chat, un serveur API préconfiguré, parfois des plugins pour la recherche web, du RAG sur vos documents, voire des agents. Ils ne vous demandent rien de configurer, mais en échange, vous ne savez pas toujours ce qui se passe à l'intérieur. La métaphore de la voiture est très juste ici : le client vous donne la climatisation, le navigateur et les capteurs de stationnement. Vous renoncez à régler manuellement la répartition du freinage, mais vous arrivez tout de même à destination.

La question qui traverse tout l'article n'est pas « combien de contrôle vais-je céder », c'est « avec quel matériel vais-je réussir à faire tourner ce qui est promis ». Cela déplace le centre de gravité du logiciel vers le matériel, et c'est précisément là que réside la vraie différence entre les deux mondes. Un moteur optimisé pour les H100 d'un centre de données et un client conçu pour tourner sur le MacBook de la maison parlent des langues différentes, et savoir distinguer ce qui sert à quoi constitue la moitié du chemin.

Mon expérience réelle ne touche que deux points de cette carte, et je les nomme à titre d'illustration, non comme ossature : LM Studio et Unsloth Studio sur une Radeon RX 9060 XT avec 16 Go de VRAM, la même configuration que beaucoup d'utilisateurs avancés, gamers, créateurs de contenu ou développeurs travaillant depuis chez eux reconnaîtraient comme la leur. Un matériel grand public de milieu/haut de gamme, mais bien loin de l'A100 que l'on imagine lorsqu'on parle d'inférence locale. Le reste découle d'une lecture attentive de la documentation, non d'essais sur le terrain.
![schema1.jpg](schema1.jpg)

## Les moteurs

### llama.cpp

[llama.cpp](https://github.com/ggml-org/llama.cpp) est la raison pour laquelle presque tout tourne. Cette bibliothèque en C/C++ est le moteur silencieux derrière la plupart des clients connus du grand public : Ollama, LM Studio, Jan, GPT4All et KoboldCPP s'appuient tous, à des degrés divers, sur son cœur. Sa force réside dans son extrême portabilité : elle tourne sur CPU, sur GPU NVIDIA avec CUDA, sur AMD avec HIP, sur cartes Intel avec Vulkan et SYCL, et sur le Metal d'Apple Silicon, le tout dans le même paquet. Ce n'est pas un hasard si le format GGUF — des poids quantifiés, autonomes et agnostiques par rapport à l'architecture — est devenu le standard de fait pour les modèles locaux : llama.cpp en est l'implémentation de référence.

Le revers de la médaille est le même que celui de son omniprésence : la configuration est pensée « pour les développeurs », avec un contrôle fin mais peu orienté vers le service multi-utilisateur. Si vous voulez faire tourner un modèle sur votre ordinateur portable pour expérimenter avec les quantifications GGUF, c'est probablement le meilleur choix absolu. Si vous devez servir ce modèle à toute une équipe avec des API stables, c'est le moteur, mais pas le produit.

### vLLM

Si llama.cpp est le moteur du bricolage, [vLLM](https://vllm.ai/) est le moteur de course en production. Créé par des chercheurs de l'UC Berkeley, il est devenu le standard de fait pour le serving à haut throughput, et sa révolution s'appelle PagedAttention : au lieu de traiter la mémoire KV cache comme un bloc unique et gaspillé, il la traite comme la mémoire virtuelle d'un système d'exploitation, par pages, avec copy-on-write et partage de préfixes entre requêtes similaires. Dans le papier original du projet, les systèmes précédents n'exploitaient que 20 à 40 % de la mémoire KV cache disponible ; avec PagedAttention, l'utilisation monte à environ 96 %, permettant un throughput 2 à 4 fois supérieur par rapport au batching naïf à latence égale.

Mais vLLM vit sur le terrain des GPU NVIDIA. CUDA est sa maison, et le support d'AMD via HIP progresse, mais il reste un outil orienté vers les centres de données, moins adapté aux ordinateurs portables et aux CPU. La configuration est plus complexe, et la philosophie est claire : serving pour équipes et entreprises, API backend pour applications, charges de travail concurrentes. Si votre objectif est de faire discuter des dizaines d'utilisateurs avec le même modèle, vLLM est probablement la première chose que vous allez étudier.

### SGLang

[SGLang](https://github.com/sgl-project/sglang) fait quelque chose de différent et de plus spécifique : il est optimisé pour les modèles qui ne se contentent pas de répondre, mais qui pensent en graphes. Des agents qui exécutent plusieurs étapes, du tool-use, du RAG avancé, des flux de « deep research » où le modèle appelle des outils externes et enchaîne les générations. Sa force réside dans la co-conception du frontend linguistique avec le runtime, de manière à gérer efficacement des schémas de décodage non triviaux.

Il est moins « grand public » que vLLM ou llama.cpp, et la documentation garde un parfum de première heure. Mais si votre objectif concerne des agents locaux multi-étapes ou le prototypage de flux d'agents, SGLang est l'un des outils les plus prometteurs de 2026, avec un support rapide sur les modèles les plus avancés comme gpt-oss.

### TGI

[Text Generation Inference](https://huggingface.co/docs/text-generation-inference) de Hugging Face est un vétéran en phase de transition. Pendant des années, il a été le serveur d'inférence de référence pour héberger des modèles de Hugging Face en production, avec des kernels optimisés en Rust et Python, de la maturité, une documentation solide et une intégration directe avec le HF Hub. Mais le 11 décembre 2025, Hugging Face a placé TGI en mode maintenance : plus de nouveaux modèles, de nouvelles fonctionnalités ou de nouvelles optimisations, et Hugging Face redirige explicitement ceux qui doivent faire de nouveaux déploiements vers vLLM et SGLang. Le dépôt n'accepte désormais plus que des corrections de bugs et des améliorations de documentation.

Il n'est pas mort, il continue de fonctionner, mais pour un nouveau projet, c'est un choix à faire en toute connaissance de cause : vous pouvez toujours l'utiliser, mais ce n'est plus le futur que Hugging Face construit. C'est le cas classique où le meilleur outil d'hier devient un héritage à gérer, un peu comme certains mainframes COBOL que plus personne ne veut toucher mais que personne n'arrive à éteindre.

### TensorRT-LLM

[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) est la suite logicielle de NVIDIA pour l'inférence optimisée sur ses GPU les plus modernes, des H100 et L40S aux A100 et aux séries plus récentes. Sa force réside dans les performances maximales sur matériel NVIDIA, avec une intégration directe avec Triton Inference Server pour passer d'un seul GPU à des clusters entiers via Kubernetes. C'est l'outil pour ceux qui ont déjà l'infrastructure et veulent en extraire le maximum.

Le revers est le verrouillage propriétaire (lock-in) : TensorRT-LLM vit et meurt avec NVIDIA, a une courbe d'apprentissage abrupte et s'avère inutile pour le consommateur moyen. Si vous travaillez dans un centre de données équipé de GPU NVIDIA et que la charge de travail est critique en latence et en throughput, c'est probablement le sommet. Sinon, c'est un monde très éloigné de votre bureau.

### MLX

[MLX](https://mlx.ai/) est le framework d'Apple pour le machine learning sur Apple Silicon, et sa force réside dans l'utilisation unifiée de la mémoire. Sur un Mac équipé d'une puce M1, M2, M3 ou ultérieure, le CPU et le GPU partagent la même mémoire RAM, et MLX exploite cela pour réaliser de l'inférence zero-copy qu'aucun portage de llama.cpp ne peut égaler en efficacité. C'est la raison pour laquelle un MacBook peut faire tourner des modèles sur lesquels des PC équivalents peinent.

La limite est évidente : MLX vit et meurt avec macOS et Apple Silicon, et s'avère moins multiplateforme. Mais si vous avez un MacBook ou un Mac mini, c'est probablement le moteur le plus naturel pour l'inférence locale, et de plus en plus de runners et d'applications s'appuient sur lui comme backend natif pour l'écosystème Apple.

## Les voitures

### Ollama

[Ollama](https://ollama.com/) est l'outil de ceux qui recherchent la simplicité. Il s'installe en une commande, expose par défaut une API REST compatible OpenAI sur `localhost:11434`, et s'intègre sans friction dans des scripts, des pipelines et des applications. Il est open source, dispose d'une large communauté, et sa philosophie minimaliste — une commande pour télécharger et une pour exécuter — en fait le backend préféré de dizaines d'applications tierces. En termes de performances brutes, il est généralement plus rapide, gère mieux les requêtes concurrentes et consomme moins de ressources grâce à l'absence de surcharge graphique.

Le revers de la médaille réside dans la familiarité avec le terminal nécessaire, la configuration avancée qui passe par des Modelfiles, et une GUI native arrivée tardivement qui reste minimale. Il y a aussi une question de transparence qu'il convient de signaler : étant open source, le code d'Ollama est inspectable par n'importe qui, ce qui n'est pas toujours le cas pour les concurrents avec GUI propriétaire. Pour le développement local d'applications avec LLM, l'usage personnel depuis le terminal ou via API, et le prototypage rapide, Ollama reste un pilier.

### LM Studio

[LM Studio](https://lmstudio.ai/) joue sur un terrain différent. C'est une application de bureau avec une interface graphique soignée, disponible pour Windows, macOS et Linux, et sa force réside dans l'élimination de la friction qui freine la plupart des personnes qui s'approchent de l'IA locale. Il permet de chercher, télécharger et charger des modèles sans ouvrir de terminal, expose lui aussi une API compatible OpenAI, et gère automatiquement l'accélération GPU sur NVIDIA, Apple Silicon et AMD.

Mais le détail qui change vraiment l'expérience pour qui arrive sans formation de développeur est le suivant : au moment de la sélection d'un modèle, LM Studio affiche en temps réel une estimation des performances attendues sur votre configuration matérielle, avec des indicateurs de couleur — vert, jaune, rouge — qui communiquent immédiatement si le modèle tournera avec fluidité, avec des limitations, ou si le matériel est insuffisant. Pour un particulier qui expérimente, cette friction éliminée vaut bien le potentiel écart de performance par rapport à Ollama.

Ce n'est pas théorique, je l'ai vu fonctionner. Dans ma configuration avec une Radeon RX 9060 XT de 16 Go, c'est précisément l'indicateur vert de LM Studio qui m'a confirmé que Qwen 3.5 9B en Q8_0 tournerait entièrement sur GPU sans devoir éparpiller des couches sur la RAM du système, et j'ai choisi le modèle à l'avance, sans calculs manuels ni documentation technique à consulter. Un détail qui, traduit, signifie ne pas découvrir que l'on s'est trompé de modèle après avoir téléchargé dix gigaoctets.

LM Studio est closed source, un binaire gratuit mais non transparent, et certaines fonctionnalités liées au web ne sont pas actives par défaut. Mais pour du chat local avec GUI, de l'expérimentation avec GGUF et de l'API locale, c'est probablement le meilleur point de départ pour qui ne veut pas savoir ce qui se passe sous le capot.

### Jan

[Jan](https://jan.ai/) est l'alternative open source qui mise sur la confidentialité et le self-hosting sans sacrifier l'utilisabilité. Il dispose d'une GUI de bureau propre, prend en charge plusieurs backends dont llama.cpp, expose une API locale sur un port dédié, et se présente comme une alternative à ChatGPT véritablement ouverte. Sa force réside dans son équilibre : open source comme LM Studio ne l'est pas, avec une UX qu'Ollama n'a pas.

La limite est un écosystème de modèles moins fourni et une diffusion plus faible, ce qui se traduit par moins de documentation et moins de communauté derrière. Pour ceux qui veulent de l'open source et une GUI sans trop de complications, Jan mérite une place dans vos tests.

### Unsloth Studio

[Unsloth Studio](https://unsloth.ai/) est le produit qui se rapproche le plus de ce qu'un assistant « agentique » local devrait être. *Une précision utile : il existe actuellement deux portes d'accès au même écosystème, Unsloth Studio, l'interface qui tourne dans le navigateur et qui au moment où j'écris ces lignes est encore étiquetée comme bêta, et Unsloth Desktop, l'application native plus récente pour Windows, macOS et Linux. Les fonctionnalités fondamentales sont les mêmes, seul le conteneur change.* Ce n'est pas juste un runner : c'est un environnement qui intègre de la recherche web native, du deep research, du RAG sur des documents locaux, de l'exécution de code, des bases de connaissances personnelles, et même du fine-tuning QLoRA guidé sans toucher à un terminal. Le moteur sous-jacent est llama.cpp pour les GGUF, avec des composants d'entraînement qui en font un outil hybride entre inférence et entraînement.

La cible est précise : créateurs, chercheurs, ceux qui écrivent des articles ou des rapports et veulent que le modèle cherche des sources, lisent des pages et génèrent des brouillons cités. La recherche web intégrée et le deep research, qui élabore un plan, trouve des références crédibles et génère un rapport avec des citations, le distinguent de la plupart des concurrents. Le revers est qu'il est encore en évolution rapide, moins mûr comme runner « pur » par rapport à Ollama ou LM Studio, et certaines fonctions peuvent encore présenter une certaine instabilité, en cohérence avec l'étiquette bêta qu'il porte encore. Mais si votre objectif est d'écrire avec des sources, c'est probablement l'outil le plus prometteur du groupe.

Ici aussi, l'expérience directe a du poids. Lors du test avec Unsloth Studio sur ma RX 9060 XT, la capacité à faire chercher au modèle des pages web pendant que je travaillais, et d'utiliser le deep research pour construire des rapports cités, a montré ce que signifie avoir un environnement agentique prêt à l'emploi, sans assembler six composants différents. Ce n'est pas un runner, c'est un laboratoire.

### LocalAI

[LocalAI](https://localai.io/) fait une chose élégante : il se pose comme une abstraction uniforme au-dessus de plusieurs backends. Si vous avez llama.cpp, vLLM, MLX et que vous voulez une API cohérente compatible OpenAI qui parle avec tous sans devoir vous rappeler quelle commande lancer pour quel moteur, LocalAI est la solution. Il prend en charge plusieurs modèles simultanément, et sa philosophie est « une installation, plusieurs moteurs », sans devenir un téléchargement gigantesque car chaque backend ne s'active que lorsqu'un modèle le demande.

La limite est qu'il est plus orienté infrastructure que convivial pour le bureau : ce n'est pas l'outil pour chatter, c'est celui pour construire un backend unifié dans des environnements hétérogènes. Pour des serveurs en self-hosting et des applications qui utilisent plusieurs moteurs, c'est un choix solide.

### Open WebUI

[Open WebUI](https://openwebui.com/) est ce que beaucoup de gens cherchent sans le savoir : un « ChatGPT en self-hosting » pour leur équipe. Il s'appuie sur Ollama, vLLM ou d'autres moteurs via API, mais ajoute tout ce qui manque à une plateforme partagée : chat multi-utilisateurs, RAG intégré, recherche web via SearXNG ou des fournisseurs comme Brave, gestion des utilisateurs, espaces de travail, agents. L'interface est moderne et la flexibilité élevée.

Le prix à payer est le déploiement : il nécessite Docker et un minimum de configuration serveur, ce n'est donc pas « téléchargez et utilisez ». Mais si vous voulez une plateforme partagée pour une équipe avec RAG et recherche web, Open WebUI est probablement le meilleur résultat de 2026 sur ce front.

### GPT4All

[GPT4All](https://gpt4all.io/) a été pendant des années le premier contact de beaucoup de personnes avec l'idée même d'un LLM sur leur propre ordinateur : interface très simple, aucune configuration, modèles téléchargeables en un clic. Le problème, et il est juste de le dire clairement, est que le développement actif s'est arrêté : aucun commit sur le dépôt depuis mai 2025, aucune version depuis février 2025. L'application fonctionne encore, s'ouvre et permet de chatter sans accroc, mais elle ne reçoit plus de mises à jour, de nouveaux modèles ou de correctifs de sécurité. Elle doit être considérée comme un point d'entrée historique plutôt que comme un choix recommandé pour 2026 : ceux qui cherchent aujourd'hui la même simplicité trouveront chez Jan ou Ollama des alternatives mieux entretenues.

### KoboldCPP

[KoboldCPP](https://koboldcpp.com/) est né de l'écosystème KoboldAI et s'adresse à un public précis : ceux qui écrivent de la fiction longue, du jeu de rôle ou du storytelling assisté. Au-dessus d'un moteur basé sur llama.cpp, il construit un ensemble d'options de génération, de préréglages et d'outils d'édition conçus pour le texte créatif, comme la gestion de la mémoire narrative ou les World Info, que d'autres clients n'offrent même pas. C'est un exécutable unique, léger, conçu pour ceux qui viennent du monde des jeux textuels plus que de celui du développement logiciel.

La limite réside dans sa spécialisation même : en dehors du périmètre de l'écriture créative, KoboldCPP est moins pratique que LM Studio ou Ollama pour un usage générique, et son interface, bien que fonctionnelle, ressemble à un outil construit par des passionnés pour des passionnés, non par une équipe produit.

### Text Generation WebUI

[Text Generation WebUI](https://github.com/oobabooga/text-generation-webui) est le couteau suisse de l'expérimentation locale. Interface web installable en local, support de plusieurs backends, un système d'extensions qui permet d'ajouter pratiquement n'importe quoi, du RAG au TTS, jusqu'à des configurations avancées de sampling que d'autres clients masquent délibérément par souci de simplicité. C'est l'outil pour ceux qui veulent mettre les mains dans chaque paramètre.

Le revers est la courbe d'apprentissage : l'interface montre tout, ce qui signifie aussi montrer trop à qui cherche seulement à chatter. Il n'est pas conçu pour l'utilisateur occasionnel, mais pour qui traite l'inférence locale comme un laboratoire permanent.
![tabella1.jpg](tabella1.jpg)

## Que choisir, selon ce que vous voulez vraiment

Le bon choix dépend de ce que vous essayez de faire, et aucun classement universel ne peut se substituer à votre contexte. Mais certains scénarios orientent presque toujours vers les mêmes réponses.

Vous voulez juste chatter en local sur votre PC, sans rien configurer. Ici, LM Studio l'emporte pour l'UX ou Jan si vous cherchez quelque chose de entièrement open source, avec Ollama comme alternative si vous êtes à l'aise avec la CLI. Vous avez essayé LM Studio sur votre configuration et vous avez vu l'indicateur vert s'allumer : il n'y a aucune raison de réinventer la roue.

Vous devez servir un modèle à plusieurs utilisateurs en entreprise, avec une API stable. Ici, le terrain appartient aux moteurs : vLLM pour le throughput et le batching continu, TGI si vous partez d'un écosystème Hugging Face déjà existant en sachant qu'il est en transition, SGLang si vos utilisateurs font des agents ou du RAG complexe. Open WebUI peut servir d'interface humaine au-dessus de tout cela.

Vous voulez écrire des articles techniques et que le modèle cherche des sources, lisent des pages et génèrent des brouillons cités. Unsloth Studio est la réponse la plus directe, avec de la recherche web et du deep research natifs. En alternative, Open WebUI ou Text Generation WebUI, mais avec une configuration plus longue derrière.

Vous avez un GPU NVIDIA et vous voulez les performances maximales en production. TensorRT-LLM ou vLLM, selon que vous disposiez déjà d'une infrastructure native NVIDIA ou que vous préfériez une suite logicielle plus ouverte.

Vous voulez une API uniforme au-dessus de plusieurs backends. LocalAI fait exactement cela, et c'est le choix naturel pour des environnements hétérogènes.

Vous vous intéressez surtout au creative writing ou au storytelling. KoboldCPP est construit pour cela, avec une foule d'options de génération pensées pour la fiction longue.

Vous voulez expérimenter avec le RAG, des plugins et des configurations avancées sans limites. Text Generation WebUI et Open WebUI vous donnent une flexibilité maximale, au prix d'une UX moins soignée et d'une configuration plus exigeante en patience.

Ce qui est honnête, c'est que c'est souvent le même développeur qui utilise LM Studio pour explorer et llama.cpp quand il doit produire, ou Ollama pour le prototype et vLLM quand il passe en production. L'outil n'a pas d'identité fixe, il a une tâche.

## Où cela va-t-il

Trois signaux, en particulier, en disent long sur la direction que prend tout cela. Le premier est la convergence des formats : GGUF est devenu le standard de fait pour les modèles locaux, et le fait que presque tous les clients le prennent en charge signifie qu'un modèle téléchargé aujourd'hui tournera demain, sur un matériel différent, sans friction. C'est la même logique qui a fait du USB-C le connecteur universel, même si, contrairement à un connecteur physique, aucun format logiciel n'est vraiment à l'abri de révolutions futures.

Le deuxième est la croissance d'environnements « agentiques » locaux. Unsloth Studio, SGLang, Open WebUI et d'autres sont en train de déplacer le centre de gravité du « faire tourner un modèle » vers le « faire faire quelque chose au modèle », avec de la recherche web, du tool-use, du RAG et des agents qui travaillent sur vos documents. C'est la différence entre un moteur qui répond et un assistant qui agit, la même distance qui sépare un juke-box d'un physicien capable d'improviser.

Le troisième est l'intégration de plus en plus étroite entre inférence locale, recherche web, tool-use et RAG sur des documents personnels. Ce ne sont plus des mondes séparés : ce sont des couches qui s'accumulent autour du modèle, et le client est ce qui les tient ensemble. La direction semble pointer vers une orchestration d'agents locaux multi-étapes, similaires aux « opérateurs » cloud mais qui restent sur votre machine, où les données ne sortent jamais.

Les questions ouvertes restent nombreuses. Dans quelle mesure le matériel que vous avez aujourd'hui devant vous est-il durable face à des modèles qui grandissent plus vite que l'efficacité ne parvient à les suivre ? Qui est responsable de la qualité de ce qu'un agent extrait et infère, lorsque le goulet d'étranglement n'est plus le modèle mais le pipeline d'ingestion ? Et la plus subtile : si nous faisons confiance à un client dont nous ne voyons pas l'intérieur, donnons-nous plus de contrôle ou seulement l'illusion de l'avoir conservé ?

La réponse, comme toujours, réside dans l'usage. Et dans le fait de savoir ce qu'il y a sous le capot, quand c'est nécessaire.
