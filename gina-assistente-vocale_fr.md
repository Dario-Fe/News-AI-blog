---
tags: ["Generative AI", "Ethics & Society", "Applications"]
date: 2026-05-13
author: "Dario Ferrero"
---

# Alexa ? Non, Gina ! Mon assistant vocal local et auto-construit
![gina-assistente-vocale.jpg](gina-assistente-vocale.jpg)

*Tout a commencé de manière presque banale, avec cette sorte de démangeaison intellectuelle qui pousse à démonter les objets pour en comprendre le mécanisme. Depuis des années, nous cohabitons avec des assistants vocaux commerciaux : Alexa sur la table de nuit, Google Assistant sur le téléphone, quelques Siri dispersés ici et là. Honnêtement, je ne les utilise pas, mais en observant les autres, il y a toujours eu un sentiment de fond difficile à ignorer, l'impression que chaque conversation finit quelque part au loin, sur des serveurs inconnus, gérés par des entreprises opaques.*

Ce n'est pas de la paranoïa. Comme je l'ai écrit dans l'article ["AI Creativity & Ethics"](https://aitalk.it/it/ai-creativity-ethics.html), le problème de la gestion des données personnelles à l'ère de l'intelligence artificielle est concret et documenté. Chaque demande, chaque nuance vocale, chaque "Alexa, mets de la musique" devient une pièce d'un profil comportemental que je n'ai jamais signé pour construire.

De cette démangeaison est née **GINA**, mon assistant vocal personnel, complètement open source et entièrement local. Pas un produit, pas quelque chose de publié pour le public avec des prétentions : une expérience d'apprentissage, l'histoire de quelqu'un qui a voulu comprendre comment ces choses fonctionnent vraiment en en construisant une de zéro.

Il y a cependant un contexte plus large dans lequel cette histoire s'inscrit. Juste au cours de ces derniers mois, j'ai beaucoup lu et écrit sur les **Small Language Models**, ces modèles linguistiques compacts qui tournent sur du matériel normal, comme je l'ai raconté dans ["Les Small Language Models conquerront-ils 2026 ?"](https://aitalk.it/it/slm-2026.html). L'idée que l'intelligence artificielle puisse cesser d'être un privilège du cloud et devenir quelque chose de [domestique, modifiable, personnel](https://aitalk.it/it/gemma4-26b.html), est quelque chose qui me fascine viscéralement. GINA est la démonstration pratique que ce futur a déjà commencé.

## Avant de se salir les mains : les objectifs

Chaque projet a besoin d'une limite, sinon il devient infini. Avant d'écrire une seule ligne de code, j'ai essayé de clarifier pour moi-même ce que je voulais obtenir.

L'objectif principal était d'apprendre vraiment, pas de regarder de l'extérieur. Construire un système complexe en partant de zéro, assembler différentes pièces (reconnaissance vocale, modèles linguistiques, synthèse vocale, contrôle de fichiers et d'applications) est le seul moyen de comprendre vraiment comment fonctionne chaque morceau. Le deuxième objectif était d'expérimenter les SLM sur le terrain, pas seulement de les lire dans les benchmarks : tester Qwen, Mistral et Gemma sur du matériel normal et voir ce qu'ils savaient faire réellement. Le troisième, indispensable, était la confidentialité totale. Un assistant qui fonctionne complètement en local, sans aucun appel vers des serveurs externes, sans aucune donnée qui sorte du périmètre de mon PC. Le quatrième objectif, peut-être le plus pragmatique, était d'obtenir quelque chose d'utile : liste de courses, rappels, musique, notes rapides. Pas seulement un exercice théorique, mais un outil à utiliser chaque jour.

## Chapitre 1 — Pourquoi local ? La valeur de la confidentialité et des SLM

### Le tournant silencieux des modèles compacts

Il y a encore quelques années, exécuter un modèle de langage sur son propre ordinateur était une idée absurde. Il fallait des clusters de GPU de dizaines de milliers de dollars, des centres de données refroidis par liquide, des budgets énergétiques de petite industrie. Les grands modèles entraînés par OpenAI, Google, Anthropic, nécessitent des infrastructures qu'un seul individu ne pourra jamais posséder.

Mais quelque chose est en train de changer de manière silencieuse et radicale. Comme je l'ai documenté dans l'article sur les SLM, nous vivons une contre-tendance : il n'y a pas besoin de modèles énormes pour la plupart des activités quotidiennes. Un modèle de 7 ou 9 milliards de paramètres, bien instruit et optimisé, peut faire des choses surprenantes sur un PC normal de gaming ou de travail. Les chiffres sont éloquents : Phi-3.5-Mini de Microsoft, avec ses 3,8 milliards de paramètres, égale GPT-3.5 sur des benchmarks mathématiques en utilisant 98 % de puissance de calcul en moins. Llama 3.2 de 3 milliards bat des modèles de 70 milliards sur des tâches spécifiques après un fine-tuning ciblé.

Ce n'est plus une question de "quelle taille", mais de "quelle efficacité". C'est un tournant qui rappelle, à certains égards, la transition des mainframes aux ordinateurs personnels : la puissance qui était l'apanage de quelques-uns est en train de devenir domestique.

### Trois problèmes des assistants commerciaux

Les assistants vocaux commerciaux ont indubitablement des qualités : ils sont pratiques, rapides, intégrés à des centaines de services. Mais ils présentent des limites structurelles qui, pour quelqu'un qui tient à son autonomie numérique, sont difficiles à digérer.

Le premier est la dépendance à internet : sans connexion, Alexa ne parvient même pas à dire "Bonjour". Son "cerveau" se trouve sur des serveurs distants, et si la ligne tombe, l'assistant devient un bibelot. Le deuxième est économique : de nombreux services avancés sont désormais payants, et les API des modèles linguistiques ont des coûts qui, bien que contenus, existent. Le troisième, le plus important, est la confidentialité. Quand je parle à un assistant commercial, mes paroles finissent sur des serveurs tiers. Je n'ai aucune garantie concrète sur ce qui est enregistré, pendant combien de temps c'est conservé, ou comment c'est éventuellement utilisé. Et pour les plus soupçonneux, qu'il ne soit pas toujours à l'écoute.

Avec un assistant local, ces problèmes disparaissent tout simplement. Les données restent sur mon PC. Aucun serveur externe, aucun enregistrement, aucun profil comportemental construit dans mon dos.

### Le matériel de départ

Avant de commencer, j'ai fait l'inventaire de mon installation : un AMD Ryzen 7, 32 Go de RAM et un GPU avec 16 Go de VRAM. Rien d'exotique, un ordinateur de travail ou de gaming de milieu-haut de gamme, rien de plus. Avec ce matériel, je peux exécuter confortablement des modèles de 7 à 9 milliards de paramètres. Je suis allé jusqu'aux 26 de Gemma4, atteignant la limite sans perdre en performances, et pour un assistant vocal, la réactivité est fondamentale.

C'est le point qui me fascine le plus dans toute cette histoire : il n'y a pas besoin d'un supercalculateur pour faire de l'IA utile. Avec du matériel grand public et des modèles bien conçus, on obtient des résultats surprenants. C'est la promesse des SLM, et GINA en est la démonstration concrète.

## Chapitre 2 — L'architecture : comment j'ai imaginé GINA

Avant d'écrire une seule ligne de code, j'ai dessiné l'architecture du système. Je voulais quelque chose de modulaire, compréhensible, facile à étendre. L'idée de fond était simple : un flux linéaire dans lequel la voix entre, est convertie en texte, le texte est traité par un modèle linguistique, et la réponse est lue à haute voix.
![schema1.jpg](schema1.jpg)

Chaque composant a un rôle précis. **Vosk** est le moteur de reconnaissance vocale, les oreilles de GINA. **LM Studio** est le cerveau, le serveur local qui exécute le modèle linguistique et répond aux demandes. **pyttsx3** est la voix, une bibliothèque qui utilise les voix système de Windows. Le **tool calling** est le système qui permet à GINA de faire des choses concrètes dans le monde réel, pas seulement de discuter.

### LM Studio et les modèles testés

J'ai choisi LM Studio pour sa simplicité d'utilisation : vous téléchargez un modèle, vous le chargez, vous cliquez sur un bouton et vous avez un serveur API compatible avec OpenAI qui tourne sur le port 8001 de votre PC. L'application elle-même n'est pas open source, mais elle supporte tous les principaux modèles open weight et, chose fondamentale, les données ne sortent jamais de l'ordinateur. Ceux qui préféreraient une solution complètement open source peuvent la remplacer par [Ollama](https://ollama.com/) (licence Apache 2.0) en gardant le reste du code inchangé.

J'ai testé trois modèles au cours du projet, chacun avec ses propres caractéristiques. **Qwen 3.5 9B** est pensé pour le tool calling : il possède un excellent support natif pour les fonctions (reconnaissable dans l'interface de LM Studio par l'icône en forme de marteau) et a géré presque toujours correctement les appels aux outils. **Gemma 4 26B A4B** de Google utilise une architecture "Mixture of Experts" particulièrement efficace : sur 26 milliards de paramètres au total, il n'en active que 4 milliards pour chaque demande, ce qui le rend surprenamment réactif ; j'en ai écrit en détail dans ["Gemma 4 26B"](https://aitalk.it/it/gemma4-26b.html). **Mistral Devstral Small 2** est quant à lui un modèle d'environ 12 milliards de paramètres, très réactif et avec une bonne compréhension générale, et le tool calling s'avère surprenamment fiable. Sur un GPU avec 16 Go de VRAM, tous les trois tournent de manière fluide, avec des latences acceptables pour une conversation vocale.

### Les bibliothèques Python

Pour ceux qui veulent répliquer ou inspecter le projet, voici les bibliothèques utilisées et leur rôle : `vosk` et `sounddevice` gèrent l'acquisition et la reconnaissance audio ; `numpy` travaille sur les tableaux audio bruts ; `requests` fait les appels à l'API de LM Studio et à Telegram ; `pyttsx3` s'occupe de la synthèse vocale ; `queue` et `threading` gèrent les rappels asynchrones ; `json` rend persistante la liste de courses, les notes et les rappels ; `re` nettoie le texte du markdown avant la lecture vocale ; `glob`, `random` et `subprocess` gèrent la lecture musicale ; `shutil` et `datetime` complètent le tableau avec des sauvegardes et des horodatages. Toutes sont open source, toutes installables avec un simple `pip install`.
![gina-avvio.jpg](gina-avvio.jpg)
*Voici à quoi ressemble Gina au démarrage*

## Chapitre 3 — Le développement pas à pas : du micro au cerveau

Le développement a procédé par phases successives, chacune avec ses imprévus et ses solutions.

### Phase 1 : les oreilles

La première chose à faire était de faire en sorte que GINA puisse m'entendre. La tentative initiale a été faite avec **Whisper** d'OpenAI, le standard d'or pour la reconnaissance vocale. Mais presque immédiatement, j'ai rencontré un obstacle : Whisper nécessite `ffmpeg` pour décoder l'audio, et sur Windows, l'installation n'est pas banale. De plus, la bibliothèque `pyaudio` nécessaire pour accéder au micro n'était pas encore compatible avec Python 3.14, la dernière version que j'utilise pour d'autres projets.

J'ai alors cherché une alternative et j'ai trouvé **Vosk**, un moteur de reconnaissance vocale léger et entièrement local. Ses avantages sont concrets : il ne nécessite pas ffmpeg, fonctionne avec `sounddevice` au lieu de `pyaudio` (beaucoup plus simple à installer sur Windows), possède un modèle pour l'italien d'environ 50 Mo téléchargeable gratuitement et a une latence d'environ 200 ms sur CPU. Le seul inconvénient est une précision légèrement inférieure à Whisper dans les environnements bruyants, mais pour des commandes vocales du type "ajoute du lait" ou "rappelle-moi d'appeler Mario", il s'est révélé plus que suffisant.

J'ai implémenté l'écoute en **streaming continu** : GINA écoute jusqu'à ce qu'elle détecte un silence d'au moins 2 secondes, puis traite la phrase. Cette approche est plus naturelle que de devoir appuyer sur un bouton à chaque fois.

### Phase 2 : la connexion au cerveau

L'entrée vocale résolue, j'ai connecté GINA à LM Studio. L'API est compatible avec celle d'OpenAI, donc un simple appel `requests.post` vers `http://localhost:8001/v1/chat/completions` a suffi. J'ai structuré la conversation avec un historique (`messages`) qui inclut un prompt système avec les instructions pour GINA et les échanges précédents.

Le premier défi inattendu a été de gérer cet historique. Sans limite, après des dizaines de messages, la demande devenait trop importante et LM Studio répondait par une erreur 400. J'ai implémenté un mécanisme de réinitialisation automatique : quand l'historique dépasse 10 interactions, il est tronqué en ne gardant que le prompt système et les derniers échanges. GINA "perd" un peu de contexte récent, mais l'expérience reste acceptable.

### Phase 3 : la voix

Pour la synthèse vocale, j'ai utilisé `pyttsx3`, qui exploite les voix SAPI de Windows. La qualité est fonctionnelle, bien qu'un peu mécanique. Le problème immédiat a surgi presque tout de suite : les modèles LLM adorent formater les réponses en markdown, et `pyttsx3` lisait littéralement les astérisques, les underscores et les backticks, "astérisque astérisque 2 astérisque astérisque est un nombre premier" n'est pas exactement agréable. J'ai écrit une fonction `clean_text_for_tts()` qui, avec quelques regex, supprime ou remplace tous les caractères de markdown avant la lecture. Maintenant GINA ne lit que du texte propre.
![gina-diretta.jpg](gina-diretta.jpg)
*Gina répond à une question directe sur ses connaissances internes*

## Chapitre 4 — Le cœur du projet : le tool calling

Le "tool calling" est la vraie magie de GINA. Sans lui, ce ne serait qu'un chatbot qui répond vocalement. Avec le "tool calling", elle peut faire des choses concrètes dans le monde réel.

Le mécanisme fonctionne ainsi : l'utilisateur dit quelque chose ("ajoute du lait à la liste de courses"), Vosk transcrit la phrase en texte, le texte est envoyé à LM Studio avec la liste des outils disponibles (chaque outil est décrit en JSON avec son nom, sa description et les paramètres attendus), le modèle comprend que pour satisfaire la demande il doit appeler `add_to_shopping_list` avec le paramètre `item_name = "lait"` et répond par une demande de tool call au lieu d'un texte. Mon script Python intercepte cette demande, exécute la fonction Python correspondante, renvoie le résultat au modèle, et le modèle génère la réponse vocale finale : "J'ai ajouté du lait à la liste de courses."

La beauté de ce mécanisme est qu'il est **infiniment extensible** : il suffit d'ajouter une nouvelle fonction Python et de la décrire dans le JSON des outils, et le modèle apprendra à l'utiliser sans besoin d'aucun autre entraînement.

### La liste de courses

L'outil le plus simple et le plus utile au quotidien est la gestion de la liste de courses. Trois fonctions, `add_to_shopping_list`, `get_shopping_list`, `remove_from_shopping_list`, lisent et écrivent un fichier JSON contenant la liste, chaque article étant accompagné d'un horodatage et d'un indicateur `checked`. Cela fonctionne exactement comme prévu, avec un naturel qui surprend encore à chaque fois.
![gina-spesa.jpg](gina-spesa.jpg)
*Gina énumère la liste de courses.*

### Recherche en ligne (avec consentement explicite)

Il y a une fonctionnalité qui mérite un discours à part, car elle rompt délibérément le principe du "tout local". GINA peut chercher des informations sur le web via DuckDuckGo, météo, actualités, faits récents, mais seulement après consentement explicite de l'utilisateur.

Le motif de ce choix est simple : une recherche en ligne est le seul moment où quelque chose sort du périmètre du PC, et je voulais que ce soit une décision consciente, pas quelque chose qui se produit de manière silencieuse et automatique. Quand la demande requiert des données que le modèle ne peut pas avoir (informations en temps réel, événements récents), GINA demande confirmation avant de procéder.

Si l'utilisateur accepte, la requête est envoyée à DuckDuckGo, le résultat est transmis au modèle comme contexte additionnel, et la réponse est lue à haute voix. Si l'utilisateur préfère ne pas utiliser internet, le modèle répond avec ce qu'il sait, ou admet honnêtement qu'il ne sait pas.

C'est un compromis pragmatique : la confidentialité reste la règle, la connexion l'exception consciente.
![gina-online.jpg](gina-online.jpg)
*Gina fait une recherche en ligne sur la météo à Rome, après demande de consentement explicite.*

### Notes vocales

Une autre fonction que j'utilise quotidiennement est celle des notes vocales. Combien de fois arrive-t-il de se dire "je dois me rappeler de faire ça" et puis d'oublier ? Avec GINA, il suffit de dire "note : lire l'article sur AiTalk demain" et l'outil `add_note` sauvegarde la phrase dans `notes.json` avec un horodatage. On peut ensuite demander "lis les notes" et GINA énumère les dernières annotations. Simple, mais très utile.

### Rappels temporels

La fonction la plus complexe à implémenter a été celle des rappels temporels. L'objectif était de pouvoir dire "rappelle-moi d'appeler Mario dans 10 minutes" et que GINA le fasse effectivement, même au milieu d'une conversation sur autre chose.

Le défi était technique : le programme principal est à l'écoute continue du mot d'activation "Gina". Si j'avais implémenté un simple `time.sleep()` dans le thread principal, l'assistant se serait bloqué jusqu'à l'expiration du minuteur, incapable de répondre à quoi que ce soit d'autre. La solution a été d'utiliser un thread séparé pour le contrôle des rappels et une file d'attente (`queue`) pour communiquer avec le thread principal de manière sûre (thread-safe). Un thread d'arrière-plan vérifie toutes les 10 secondes s'il y a des rappels expirés dans le fichier `reminders.json` ; quand il en trouve un, au lieu d'appeler directement la fonction vocale (non thread-safe), il place le texte dans une file d'attente ; un second thread lit continuellement de la file d'attente et, quand il reçoit un message, le fait lire à GINA. Ainsi, l'assistant peut vous rappeler d'appeler Mario même si 10 minutes se sont écoulées sans que vous n'ayez rien dit.
![gina-promemoria.jpg](gina-promemoria.jpg)
*Le fichier json dans lequel Gina enregistre une note temporelle, pour vous avertir au bon moment*

### Contrôle multimédia

Pour la musique, j'ai créé un dossier `Musica/` dans le même répertoire que le script. L'outil `search_and_play_music` cherche dans le dossier les fichiers audio avec les extensions standards, fait une recherche par correspondance partielle si l'utilisateur spécifie un nom, choisit un fichier au hasard si l'utilisateur dit génériquement "mets un peu de musique", et joue le fichier avec le lecteur par défaut du système via `os.startfile`. Simple et efficace.

### Partage sur Telegram

La dernière extension pratique est l'envoi de la liste de courses sur Telegram. Avant de sortir, je peux dire "Gina, envoie-moi la liste" et je reçois un message sur un bot Telegram que j'ai créé (@GinaShoppingBot). J'arrive au supermarché, j'ouvre Telegram, et j'ai la liste prête. Le bot est gratuit, facile à configurer en parlant à @BotFather, et la persistance est totale : le message reste dans le chat jusqu'à ce que je l'efface.
![gina-telegram.jpg](gina-telegram.jpg)
*Le message envoyé sur Telegram avec la liste, après demande spécifique.*

## Chapitre 5 — L'expérience visionnaire : GINA qui modifie son propre code

Avec un assistant fonctionnel et riche en fonctionnalités, j'ai voulu aller plus loin. L'idée était presque de la science-fiction : et si GINA pouvait modifier son propre code source ?

L'image est puissante, un assistant qui apprend, évolue, s'améliore tout seul. Plus un programme statique, mais quelque chose en transformation continue. Presque du Philip K. Dick, plus que de l'informatique appliquée.

### L'implémentation

J'ai créé l'outil `modify_code_file`. Le flux était le suivant : l'utilisateur dit "Gina, modifie le fichier test.py, ajoute une fonction qui salue l'utilisateur" ; GINA reçoit la demande et appelle l'outil avec le nom du fichier et l'instruction ; l'outil lit l'intégralité du fichier, le transmet au modèle comme contexte avec l'instruction de modification, et demande de générer la nouvelle version ; le modèle renvoie le code modifié ; l'outil sauvegarde la nouvelle version dans le dossier `Codice/` à la racine du projet, dans un nouveau fichier, en laissant l'original intact.

Par sécurité, GINA peut modifier les fichiers seulement dans le dossier `Codice/`, à l'intérieur du projet, où se trouvent seulement des fichiers placés par l'utilisateur. L'utilisateur peut inspecter le résultat et, seulement s'il est satisfait, remplacer manuellement l'original.

### Le succès partiel

L'outil fonctionne parfaitement sur des petits fichiers. J'ai créé un `test.py` d'une vingtaine de lignes, j'ai demandé à GINA d'ajouter une fonction, et en quelques secondes j'ai eu `test_modificato.py` avec la fonction demandée. De la magie, littéralement.

Mais avec le fichier `gina_assistente.py` lui-même, environ 1000 lignes, le système a montré ses limites. LM Studio mettait beaucoup de temps à traiter la demande, tombait souvent en timeout, et quand il parvenait à terminer, la réponse était tronquée ou malformée.

### La limite technique comme leçon

Le problème est probablement la **fenêtre de contexte** des modèles. Les modèles que j'ai utilisés ont des contextes limités. Mon fichier `gina_assistente.py` dépasse abondamment ce seuil, le modèle n'a pas assez d'espace pour le traiter entièrement et le régénérer avec les modifications. Je dois toutefois encore analyser la question en profondeur.

Cet échec est aussi instructif que n'importe quel succès. Dans l'article sur les SLM, j'avais écrit que ces modèles sont comme des "bistouris chirurgicaux", excellents dans des tâches spécifiques et circonscrites, tandis que les grands modèles sont les "couteaux suisses" qui font tout décemment. L'outil de modification de code est la démonstration pratique : il échoue sur une tâche énorme (modifier un fichier de 1000 lignes), mais excelle sur des tâches petites et ciblées.

J'ai décidé de maintenir l'outil dans le projet comme expérience visionnaire plutôt que comme fonctionnalité stable. L'idée est fascinante, le potentiel est réel, et à l'avenir avec des modèles au contexte plus large, cela pourrait devenir pleinement praticable.
![gina-codice.jpg](gina-codice.jpg)
*Gina a créé le jeu de Snake parfaitement fonctionnel au premier essai*

## Chapitre 6 — Les incohérences des modèles : vivre avec le non-déterminisme

Aucun projet complexe n'est exempt d'imperfections. GINA a les siennes, et il vaut la peine de les raconter.

### Le problème du délai

L'une des premières difficultés a été le retard entre le mot d'activation et l'écoute effective de la commande. Le flux original prévoyait que GINA, ayant entendu le mot "Gina", réponde "Dis-moi ?" puis commence à écouter. Mais comme la réponse vocale durait environ une seconde, les premiers mots de la commande étaient systématiquement perdus. J'ai essayé en déplaçant le début de l'écoute avant la réponse vocale, mais Gina finissait par s'écouter elle-même et s'activer. Pour le moment, j'ai accepté la courte attente avant de pouvoir parler, mais je compte trouver une solution.

### Vosk : précis mais pas infaillible

Vosk est excellent dans les environnements silencieux. S'il y a du bruit de fond, la précision chute. C'est un problème connu et acceptable pour un projet personnel. Pour une application professionnelle, il faudrait un système dédié comme Porcupine, mais pour mes usages quotidiens, Vosk fait amplement son travail.

### La nature non déterministe des LLM

C'est peut-être la caractéristique la plus fascinante, et parfois frustrante, des modèles linguistiques : ils ne sont pas déterministes. À input égal, ils peuvent donner des réponses différentes.

Un exemple concret : si je dis "Gina, mets un peu de musique", parfois le modèle appelle correctement l'outil `search_and_play_music` et joue un morceau "à son choix" du dossier `Musica/`. D'autres fois, il répond : "Voici un morceau parfait pour ce moment : Bohemian Rhapsody de Queen." Et puis, évidemment, rien ne se joue car le fichier n'existe pas. Ce n'est pas un bug, c'est le modèle qui a appris de milliards de textes que "mets un peu de musique" est souvent suivi d'une suggestion musicale, et parfois il choisit cette voie au lieu d'appeler l'outil.

De même, la recherche de la météo fonctionne parfois correctement, d'autres fois le modèle répond : "Pour des informations météorologiques précises, je vous conseille de consulter un site spécialisé." Cette variabilité est normale et doit être acceptée. C'est le prix à payer pour avoir un système créatif et non rigidement déterministe, et au fond, c'est aussi ce qui rend l'interaction plus humaine, pour le meilleur et pour le pire.

Les deux problèmes pourraient être atténués avec un affinement du Prompt système, c'est un aspect sur lequel travailler.

## Chapitre 7 — Conclusions : ce qui fonctionne, ce qui manque, où on va

Le projet a réussi au-delà de mes attentes initiales. GINA fonctionne, est stable, et je l'utilise quotidiennement. Elle se lance avec un double-clic sur un fichier `.bat` sur le bureau, et elle est prête en quelques secondes.

### Ce qu'elle sait faire aujourd'hui

Avec GINA, je peux gérer la liste de courses (ajouter, afficher, supprimer des articles) et l'envoyer sur Telegram avant de sortir. Je peux enregistrer des notes et des rappels non temporels. Je peux définir des rappels temporels ("rappelle-moi d'appeler Mario dans 10 minutes") et GINA les respecte même au milieu d'autres conversations. Je peux jouer de la musique depuis mon dossier local, aussi bien des chansons spécifiques que des morceaux choisis au hasard. Je peux poser des questions générales en utilisant les connaissances internes du modèle. Je peux faire des recherches en ligne, après consentement explicite. Je peux, sur de petits fichiers, demander à GINA de modifier le code. Tout cela sans qu'un seul bit ne sorte de mon PC.

### Où il y a encore du travail

L'autocritique fait partie de la méthode. La qualité de la voix de `pyttsx3` est fonctionnelle mais métallique : on pourrait passer à Piper TTS (local, qualité bien supérieure) ou à Edge TTS (en ligne, qualité excellente). La précision du mot d'activation pourrait s'améliorer avec Porcupine. La reconnaissance vocale pourrait être plus précise avec Whisper, au prix de quelques dépendances supplémentaires. L'interface aujourd'hui est seulement en ligne de commande : une simple interface web en Streamlit ou Flask la rendrait plus accessible. Et la modification de gros fichiers reste une limite technique ouverte.

### Un monde de possibilités

Ce que j'aime le plus dans GINA, c'est qu'elle peut être étendue à l'infini. Quelques idées que j'ai en liste : une interface web pour voir la liste de courses, les notes et les rappels même à distance ; intégration avec le calendrier ("Gina, quels sont mes engagements demain ?") ; contrôle d'appareils smart home.

Mais la chose la plus importante est ce que ce projet démontre à un niveau plus large. GINA n'est pas seulement un assistant vocal personnel : c'est une **plateforme de démonstration** du potentiel des Small Language Models en local. Elle prouve qu'il n'y a pas besoin de s'en remettre aux géants du cloud pour avoir une intelligence artificielle utile, personnelle et respectueuse de la vie privée.

La tendance que j'ai décrite dans ["Small Language Models pour 2026"](https://aitalk.it/it/slm-2026.html) est déjà une réalité, et on peut la toucher du doigt. Avec des modèles comme Qwen, Gemma 4 et Mistral, un PC de gaming normal peut faire tourner un assistant vocal sophistiqué, avec une latence inférieure à la seconde, sans consommer de ressources excessives.

Et la meilleure partie est que tout cela est **open source** : modifiable, améliorable, adaptable à n'importe quel besoin. J'ai énormément appris en construisant ce projet, j'ai eu la confirmation que l'intelligence artificielle n'est pas seulement ChatGPT et des API payantes. C'est aussi de la curiosité, de l'expérimentation, le plaisir de s'asseoir devant l'ordinateur, d'écrire du code, et de voir quelque chose que vous avez construit prendre vie et vous répondre.

J'espère que ce récit inspirera quelqu'un à entreprendre un voyage expérimental. Et s'il le fait, GINA les attend, prête à écouter leur premier mot.

*"Gina"*

---

## Appendice technique : comment commencer

Tout le code est disponible sur le [dépôt GitHub](https://github.com/Dario-Fe/Gina-Assistant). Le script principal est `gina_assistant.py` ; les fichiers de mémoire pour les différents outils (`shopping_list.json`, `notes.json`, `reminders.json`) sont créés automatiquement au premier démarrage. Le dossier `Musica/` et le dossier `Codice/` sont optionnels, si vous souhaitez utiliser GINA pour écouter de la musique ou pour écrire du code, créez les dossiers à la racine du projet, mettez-y vos chansons préférées, ou les fichiers avec le code à modifier ou à créer de zéro.

Pour lancer GINA :
![schema2.jpg](schema2.jpg)
