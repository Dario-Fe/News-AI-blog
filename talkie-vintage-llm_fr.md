---
tags: ["Research", "Ethics & Society", "Training"]
date: 2026-05-15
author: "Dario Ferrero"
---

# Talkie : quand un LLM ne sait rien après 1930
![talkie-vintage-llm.jpg](talkie-vintage-llm.jpg)

*Il y a une expérience de pensée que Demis Hassabis, fondateur de DeepMind, a lancée à plusieurs reprises comme une provocation intellectuelle : si vous entraîniez un modèle de langage sur l'intégralité du corpus scientifique disponible jusqu'en 1911, parviendrait-il à redécouvrir de lui-même la Relativité Générale, qu'Einstein allait formuler quatre ans plus tard ? La question n'est pas rhétorique. C'est l'une des plus difficiles que l'on puisse poser sur l'intelligence artificielle, car elle touche au problème de la généralisation véritable, celle qui va au-delà de la récupération de schémas mémorisés et se rapproche de quelque chose que nous pourrions appeler, avec beaucoup de prudence, le raisonnement.*

C'est de cette tension qu'est né Talkie, un projet présenté en avril 2026 par Nick Levine, David Duvenaud et Alec Radford, ce dernier étant connu pour avoir contribué au développement de GPT-2 chez OpenAI. L'idée est simple à énoncer et compliquée à exécuter : entraîner un modèle de langage de treize milliards de paramètres en utilisant exclusivement des textes publiés avant le 31 décembre 1930, puis étudier son comportement comme on étudie un échantillon en laboratoire, dans un environnement contrôlé et isolé de toute contamination contemporaine.

Le résultat s'appelle [talkie-1930-13b](https://huggingface.co/talkie-lm/talkie-1930-13b-it), et il est disponible publiquement sur Hugging Face. Mais avant de parler de ce qu'il fait, il convient de comprendre pourquoi il existe.

## Pas de la nostalgie, mais de la méthodologie

Le plus grand risque avec un projet comme celui-ci est de le percevoir comme une curiosité, un jouet culturel, l'équivalent numérique d'un gramophone. Ce serait une erreur de perspective. Talkie n'est pas un modèle qui rivalise avec Claude, ChatGPT ou Gemini sur aucune tâche pratique. C'est un outil de recherche qui répond à des questions structurelles sur le fonctionnement des modèles de langage modernes, des questions qui ne peuvent même pas être formulées correctement avec les modèles généralistes.

Le problème central s'appelle la contamination, et c'est l'un des fantômes les plus persistants dans l'évaluation des systèmes d'intelligence artificielle. Quand on mesure la capacité d'un modèle sur un benchmark, tel que MMLU, HumanEval ou ARC, on suppose implicitement que le modèle n'a pas déjà "vu" les questions ou des réponses similaires pendant le pré-entraînement. Mais cette hypothèse est de plus en plus fragile : les corpus modernes incluent d'énormes quantités de texte provenant du web, et le web inclut des forums, des solutions, des explications et même des copies directes des benchmarks eux-mêmes. Un modèle qui répond correctement à une question de mathématiques pourrait le faire parce qu'il raisonne, ou parce qu'il a mémorisé la réponse dans un recoin de Reddit. Les distinguer est presque impossible quand le corpus d'entraînement est le web tout entier.

Un modèle entraîné uniquement sur des textes de 1930 ne présente pas ce problème par construction. Il ne peut pas avoir vu Python, car Python n'existait pas. Il ne peut pas avoir mémorisé des solutions de Stack Overflow, car Stack Overflow n'existait pas. S'il parvient à écrire du code correct après avoir vu quelques exemples en contexte, il le fait par généralisation pure, non par récupération. C'est un environnement expérimental que les modèles modernes, de par leur construction, ne peuvent jamais offrir.

L'idée du "vintage LM" n'est pas totalement nouvelle : l'équipe cite elle-même des projets précédents comme Ranke-4B, Mr. Chatterbox et Machina Mirabilis comme faisant partie d'un écosystème naissant. Talkie est cependant le plus grand de cette catégorie, et le premier à documenter systématiquement les défis méthodologiques qu'implique ce type d'entraînement.

## Construire une archive du passé : 260 milliards de tokens

La première question pratique est de savoir où trouver autant de texte pré-1931 en format numérique. La réponse est que la majeure partie du travail avait déjà été faite par d'autres. L'équipe de Talkie a construit son corpus en s'appuyant sur l'[Institutional Data Initiative](https://huggingface.co/datasets/institutional/institutional-books-1.0), sur l'[Internet Archive](https://archive.org) et sur le projet [Common Pile](https://huggingface.co/common-pile), en agrégeant des livres, des journaux, des périodiques, des revues scientifiques, des brevets et des actes juridiques en anglais pour un total de 260 milliards de tokens.

Le choix du cutoff au 31 décembre 1930 n'est pas arbitraire, ni seulement symbolique. Il a une base légale précise : selon le droit d'auteur américain, les œuvres publiées avant 1926 sont dans le domaine public, et la fenêtre s'étend progressivement jusqu'en 1930 pour les œuvres de cette année spécifique. Le cutoff temporel résout donc aussi le problème des licences, rendant le corpus légalement distribuable sans les complications qui affligent les jeux de données modernes.

Le choix de se limiter à l'anglais pour cette version est pragmatique : l'équipe déclare explicitement que la validation de la chaîne de données requiert une familiarité profonde avec les documents sources, et les chercheurs sont de langue maternelle anglaise. L'expansion multilingue est indiquée comme une priorité future, tant pour augmenter la taille du corpus que pour diversifier les perspectives culturelles représentées.

Deux cent soixante milliards de tokens semblent beaucoup, mais il faut les contextualiser : les modèles généralistes modernes sont entraînés sur des corpus de l'ordre de plusieurs milliers de milliards de tokens, souvent avec plusieurs passages sur les données les plus importantes. L'équipe estime cependant pouvoir faire croître son corpus à plus de mille milliards de tokens de texte historique, une estimation qui, si elle était confirmée, porterait les capacités du modèle au niveau de GPT-3.5, décrit dans le post d'introduction comme "similaire en capacité au ChatGPT original".
![identity.jpg](identity.jpg)
[Image tirée du dépôt GitHub](https://github.com/talkie-lm/talkie)

## L'ennemi invisible : OCR et bruit systématique

Si le corpus est le fondement, sa qualité est la fissure la plus profonde de l'édifice. En 1930, le texte numérique natif n'existait pas : tout ce qui a fini dans le jeu de données de Talkie a été transcrit à partir de sources physiques par reconnaissance optique de caractères (OCR), un processus qui introduit un type de bruit radicalement différent de toute erreur présente dans les corpus modernes.

Les systèmes OCR classiques, ceux utilisés historiquement pour numériser les archives, fonctionnent bien sur des mises en page simples et des numérisations propres. Sur des journaux d'époque avec des colonnes irrégulières, des polices de caractères détériorées et des pages jaunies, leur précision s'effondre. L'équipe de Talkie a quantifié ce problème de manière précise : entraîner un modèle sur des textes pré-1931 transcrits avec un OCR conventionnel produit, à ressources informatiques égales, seulement 30 % de l'efficacité d'apprentissage d'un modèle entraîné sur les mêmes transcriptions faites par des êtres humains. Un nettoyage avec des expressions régulières permet de récupérer une partie du terrain en portant la donnée à 70 %, mais il reste un écart significatif.

La solution alternative, utiliser des systèmes modernes basés sur de grands modèles visuels, crée un problème paradoxal : ces systèmes plus précis ont tendance à halluciner des faits modernes dans le texte transcrit, contaminant exactement le corpus que l'on veut garder pur. L'équipe développe un système OCR "vintage" spécifique à cet usage, un modèle entraîné à transcrire des textes historiques sans introduire de connaissances contemporaines.

C'est un problème qui rappelle la situation du restaurateur de films qui doit nettoyer une pellicule des années vingt sans introduire d'artefacts numériques reconnaissables : chaque outil moderne laisse des traces de lui-même dans le matériau qu'il touche.

## Quand le passé laisse filtrer le futur : le problème du temporal leakage

Même avec un corpus apparemment circonscrit, la frontière temporelle est plus poreuse qu'il n'y paraît. L'équipe identifie plusieurs modalités par lesquelles des contenus postérieurs à 1930 peuvent s'infiltrer dans le jeu de données : des métadonnées de date erronées sur des documents numérisés, des introductions éditoriales modernes ajoutées à des rééditions de classiques, des notes de bas de page écrites par des conservateurs de l'après-guerre, des insertions anachroniques dans des textes par ailleurs historiques.

Pour aborder ce problème, Talkie utilise un classificateur d'anachronismes basé sur des n-grammes au niveau du document, un outil qui repère des séquences de mots statistiquement improbables dans un corpus pré-1931 et filtre les documents suspects. Le système n'est cependant pas infaillible : une version précédente du modèle à sept milliards de paramètres montrait clairement une connaissance de la présidence Roosevelt et du New Deal, tous deux postérieurs au cutoff. La version actuelle de 13 milliards conserve quelques traces de connaissances relatives à la Seconde Guerre mondiale, à l'ONU et à la division de l'Allemagne, des détails qui n'auraient pas pu provenir de textes de 1930.

Ces résidus de futur dans le modèle ne sont pas seulement un défaut technique : ils sont la démonstration de la difficulté, en pratique, de construire une frontière temporelle réellement étanche. L'équipe les documente avec honnêteté méthodologique, en les citant comme piste de recherche future plutôt qu'en les cachant, et développe des classificateurs plus avancés pour les versions ultérieures du modèle.
![grafico1.jpg](grafico1.jpg)
[Image tirée du site officiel talkie-lm.com](https://talkie-lm.com/introducing-talkie)

## Instruire un modèle sans utiliser le présent

Une fois le modèle de base entraîné, l'étape suivante consiste à le rendre utile comme interlocuteur, ce qui nécessite un processus de post-entraînement, c'est-à-dire un alignement qui transforme le modèle de prédicteur de texte en un interlocuteur capable de suivre des instructions. Le problème est que tous les jeux de données standards pour ce processus, les recueils de dialogues humain-assistant, les préférences annotées, les benchmarks de suivi d'instructions, sont intrinsèquement modernes. Les utiliser reviendrait à contaminer le modèle avec des attentes, des styles de communication et des connaissances du XXIe siècle.

L'équipe a construit une chaîne de post-entraînement de zéro. La première phase utilise des textes historiques à structure régulière comme matière première : manuels de savoir-vivre victoriens, livres de cuisine d'époque, dictionnaires, encyclopédies, recueils de contes, guides épistolaires. À partir de ces textes, des paires instruction-réponse sont extraites, reflétant les conventions de communication de l'époque, et le modèle est affiné sur celles-ci. C'est comme enseigner les bonnes manières à quelqu'un en utilisant le savoir-vivre de Monsignor Della Casa au lieu d'un cours de communication d'entreprise contemporain.

La deuxième phase est plus sophistiquée et introduit une tension conceptuelle intéressante. L'équipe utilise le Direct Preference Optimization (DPO) en ligne, une technique d'entraînement par préférences, en générant des prompts synthétiques sur divers types de tâches et en utilisant Claude Sonnet 4.6 comme juge pour évaluer la qualité des réponses de Talkie. Le score moyen de suivi d'instructions est passé de 2.0 à 3.4 sur une échelle de cinq points au cours de ce processus. Une troisième phase utilise ensuite des conversations synthétiques générées entre Claude Opus 4.6 et Talkie pour lisser les aspérités conversationnelles résiduelles.

Le problème est que cette approche introduit inévitablement une contamination subtile : un modèle moderne qui évalue les réponses d'un modèle vintage transfère, même involontairement, des attentes contemporaines sur ce qui constitue une bonne réponse. Une version précédente du modèle, après un apprentissage par renforcement avec feedback IA, avait développé l'habitude de répondre par des listes à puces, un style tout à fait étranger à la prose du XIXe et du début du XXe siècle, mais caractéristique des modèles assistants modernes. L'équipe reconnaît explicitement cette limite et fixe comme objectif futur d'utiliser ses propres modèles vintage comme juges, éliminant ainsi la dépendance aux systèmes contemporains.

## Ce qu'il sait, ce qu'il ne sait pas : la comparaison avec le jumeau moderne

Pour contextualiser les capacités de Talkie de manière rigoureuse, l'équipe a entraîné un "jumeau moderne", un modèle architecturalement identique mais entraîné sur FineWeb, l'un des principaux corpus de texte web moderne. La comparaison à ressources informatiques égales montre que Talkie est moins performant que son équivalent contemporain dans les évaluations standards de connaissances, un résultat attendu et déclaré ouvertement.

Ce qui est plus intéressant, c'est ce qui se passe quand on filtre les questions anachroniques des benchmarks, c'est-à-dire celles qui supposent la connaissance d'événements, de technologies ou de concepts postérieurs à 1930. En éliminant ces questions, l'écart de performance est réduit approximativement de moitié. Le modèle vintage et le modèle moderne affichent des performances comparables sur des tâches de compréhension linguistique fondamentale et de raisonnement numérique, des capacités qui dépendent moins du contenu spécifique du corpus et davantage de la structure du langage lui-même.

Le test le plus fascinant d'un point de vue théorique concerne la programmation. L'équipe a soumis à Talkie une version de HumanEval, le benchmark standard pour l'évaluation de la capacité d'écriture de code Python, en fournissant au modèle quelques exemples en contexte mais aucune connaissance préalable de Python ou de la programmation moderne. Les résultats sont nettement inférieurs à n'importe quel modèle entraîné sur des données web, où le code est abondant. Cependant, à mesure que l'échelle augmente, le modèle montre des améliorations constantes même sur cette tâche, signe que quelque chose qui ressemble à de la généralisation émerge. Les problèmes résolus correctement sont simples, souvent d'une seule ligne, mais incluent des cas comme l'implémentation de la fonction de décodage d'un chiffrement par rotation quand seule la fonction de codage est fournie, suggérant une compréhension rudimentaire du concept de fonction inverse.
![grafico2.jpg](grafico2.jpg)
[Image tirée du site officiel talkie-lm.com](https://talkie-lm.com/introducing-talkie)

## Biais historiques et responsabilité culturelle

Un modèle entraîné exclusivement sur des textes de 1930 reflète nécessairement la culture, les valeurs, le lexique et les préjugés de cette époque. Ce n'est pas un détail marginal : c'est une caractéristique structurelle que l'équipe reconnaît explicitement avec la note précisant que Talkie "peut produire des sorties offensantes pour les utilisateurs", une formulation sobre pour indiquer que le corpus inclut des textes produits à une époque de colonialisme actif, de racisme institutionnalisé, d'exclusion systématique des femmes de la vie publique et d'antisémitisme répandu dans la culture dominante.

cet aspect est à la fois une limite d'application évidente et, paradoxalement, l'un des éléments de plus grand intérêt scientifique. Étudier comment ces biais se manifestent dans le comportement du modèle, comment ils se propagent du corpus à la sortie, et comment ils interagissent avec le post-entraînement pourrait offrir des intuitions précieuses sur la même dynamique dans les modèles modernes, où les biais sont plus difficiles à isoler car noyés dans un corpus vaste et hétérogène.

La question pose aussi des interrogations plus larges que l'équipe soulève explicitement : quelle part de ce que nous observons dans les modèles de langage actuels est une propriété du langage humain en général, et quelle part est au contraire une propriété spécifique du web en tant que corpus ? Les modèles modernes sont tous, à divers degrés, les enfants du même parent numérique. Construire des modèles entraînés sur des corpus radicalement différents, comme des textes historiques, des textes scientifiques purs, ou de la littérature non anglophone, pourrait révéler quelle part de ce que nous appelons "comportement émergent" est effectivement émergente et quelle part est au contraire un reflet fidèle de la source.

## Où se situe Talkie par rapport à la recherche actuelle

Il est important de situer ce projet honnêtement dans le panorama de la recherche. Au moment de la publication, en avril 2026, le travail de Talkie n'a pas encore passé de révision par les pairs formelle : il est présenté comme un post d'introduction avec une méthodologie documentée, des données quantitatives et un accès public au modèle et au code sur [GitHub](https://github.com/talkie-lm/talkie), mais sans la validation externe qu'un article publié dans une conférence comme NeurIPS ou ICML impliquerait. Les données rapportées, comme l'efficacité OCR à 30 % ou l'amélioration du score DPO de 2.0 à 3.4, sont présentées comme des résultats internes et devraient être confirmées par des réplications indépendantes.

Le projet reçoit un soutien informatique et financier d'Anthropic et de Coefficient Giving, et les remerciements incluent des noms de relief dans le domaine comme John Schulman et Andrej Karpathy, signes de crédibilité dans l'écosystème de la recherche. Mais le chemin de la démo publique à la contribution méthodologique consolidée est encore long.

Ce que l'on peut dire avec certitude, c'est que la question de recherche est légitime et importante. La contamination des benchmarks est un problème documenté et croissant, comme en témoigne un [récent article](https://arxiv.org/abs/2602.12413) cité par les auteurs eux-mêmes. L'idée d'utiliser des modèles avec des cutoffs temporels nets comme outils d'évaluation de la généralisation est originale et méthodologiquement cohérente. Le projet ouvre une direction, il ne la ferme pas.

## Une nouvelle ligne de recherche, pas une alternative

Le plan de scaling de Talkie est ambitieux : d'ici l'été 2026, l'équipe prévoit de sortir un modèle de l'ordre de GPT-3 en capacité, et estime qu'un corpus de plus de mille milliards de tokens historiques est suffisant pour construire quelque chose de comparable à GPT-3.5. Ces objectifs doivent être lus dans le contexte où ils sont déclarés : non pas comme des annonces de produits, mais comme des horizons de recherche qui déterminent l'échelle des expériences futures.

L'ambition la plus intéressante n'est cependant pas numérique. C'est la possibilité de construire une chaîne de post-entraînement complètement autonome, dans laquelle les modèles vintage sont utilisés comme juges d'eux-mêmes, éliminant ainsi la dépendance à Claude ou à d'autres systèmes modernes dans l'évaluation des préférences. Si elle était réalisée, cela permettrait d'obtenir un modèle véritablement "d'époque" non seulement dans les données de pré-entraînement, mais dans tout le processus d'alignement, une expérience sans précédent sur la manière dont la source des valeurs d'entraînement influence le comportement final du système.

Il y a un parallélisme utile avec certaines expériences de linguistique informatique des années quatre-vingt-dix, quand des chercheurs comme Frederick Jelinek chez IBM construisaient des modèles statistiques du langage sur des corpus rigoureusement contrôlés, non pas parce qu'ils voulaient des systèmes de production, mais parce que des environnements contrôlés révèlent des mécanismes que des corpus vastes et bruyants cachent. Talkie s'insère dans cette tradition : il utilise la limitation comme lentille analytique.

La réponse à la question de Hassabis, de savoir si un modèle arrêté en 1911 pourrait redécouvrir la Relativité Générale, reste ouverte. Mais Talkie suggère que le moyen de s'approcher d'une réponse crédible n'est pas de spéculer, c'est de construire l'expérience. Entraîner le modèle, lui donner la physique de Maxwell et les anomalies de l'orbite de Mercure, et voir ce qui émerge. Ce n'est pas de la science-fiction : c'est la méthode scientifique appliquée à l'intelligence artificielle, avec toute la patience et la rigueur qu'elle requiert.

---

*Le code source de Talkie est disponible sur [GitHub](https://github.com/talkie-lm/talkie). Le modèle de base et la version post-entraînée sont accessibles publiquement sur [Hugging Face](https://huggingface.co/talkie-lm). Une démo conversationnelle est disponible sur [talkie-lm.com/chat](https://talkie-lm.com/chat).*
