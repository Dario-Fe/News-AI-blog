---
tags: ["Applications", "Generative AI", "Ethics & Society"]
date: 2026-07-01
author: "Dario Ferrero"
---

# Last30days : quand un agent de code devient un moteur de recherche social
![last30days.jpg](last30days.jpg)

*Avant d'écrire quoi que ce soit sur l'IA, j'ai ouvert onze onglets de navigateur : Reddit, X, YouTube, Hacker News, GitHub, quelques newsletters du secteur. Deux heures plus tard, trois cafés, j'avais trouvé trois posts vraiment utiles. Le reste était du bruit : des articles de blog optimisés pour les moteurs de recherche, des opinions de personnes payées pour en avoir, des galeries classiques du genre "les dix outils IA qui vont changer votre vie" écrites avec la même profondeur qu'une notice de montage d'un meuble IKEA.*

Le problème n'est pas la quantité d'informations. C'est que les systèmes que nous utilisons pour les parcourir ont été conçus pour agresser les algorithmes, non pour refléter ce que les gens pensent vraiment. Google indexe des éditeurs. Reddit, X et YouTube indexent des personnes. Ce sont des écosystèmes fondamentalement différents, chacun enfermé dans son propre jardin clos, chacun avec ses propres API, ses propres tokens d'authentification, ses propres logiques d'accès.

[`/last30days`](https://github.com/mvanhorn/last30days-skill) est une tentative de briser ces clôtures. Ce n'est pas un moteur de recherche au sens traditionnel : c'est une skill pour agents de code qui interroge en parallèle Reddit, X, YouTube, Hacker News, TikTok, GitHub, Polymarket et d'autres, fusionne les résultats, et livre une synthèse structurée en quelques minutes. Écrit par Matthew Van Horn, il a atteint 41 500 étoiles sur GitHub, se classant comme le dépôt numéro un du jour lors de sa semaine de lancement. Les chiffres seuls ne disent pas grand-chose, mais ils racontent l'intensité d'un besoin réel.

## Sous le capot : architecture v3

La version trois du projet, l'actuelle, est construite autour d'une idée simple mais puissante : ne pas chercher ce que vous avez écrit, comprendre d'abord *où* le chercher. Le README officiel du dépôt décrit le flux en sept étapes, mais la partie intéressante est ce qui se passe avant même qu'un seul appel API ne soit effectué.

Le moteur utilise un système de fusion de classements appelé Reciprocal Rank Fusion, abrégé RRF. Au lieu de confier la pertinence à une seule source ou à un seul algorithme, le RRF prend les résultats de plusieurs sources, chacune avec son propre classement, et les fusionne en un classement composite qui réduit le poids des valeurs aberrantes et récompense la cohérence entre les différentes plateformes. Si un thème émerge avec force sur Reddit, il reçoit un signal. Si le même thème apparaît sur X et est cité dans une vidéo YouTube, le signal s'amplifie. Si, en revanche, il est fort sur une seule plateforme et silencieux sur les autres, il est redimensionné.

L'autre élément architectural digne d'attention est le clustering automatique : quand la même histoire apparaît sur Reddit, X et YouTube avec des titres différents, le moteur ne l'affiche pas trois fois. Il la détecte comme un cluster unique via entity-based overlap detection, reconnaissant la coïncidence même lorsque les mots utilisés sur les différentes plateformes ne coïncident pas. Le résultat est un brief qui consolide au lieu de dupliquer.

## Le cerveau qui lit avant de chercher

La fonction que le README appelle "Intelligent Search" est celle qui sépare le plus nettement cet outil de la recherche traditionnelle. Elle a été construite par [Jonas Sperling](https://github.com/j-sperling) et fonctionne comme un pre-research brain, une étape zéro qui précède toute interrogation des API externes.

L'idée est la suivante : quand vous écrivez `/last30days OpenClaw`, le moteur ne cherche pas littéralement "OpenClaw" sur toutes les plateformes. D'abord, il résout qui et quoi se trouve autour de ce terme. Il comprend qu'OpenClaw a un créateur, Peter Steinberger, qui sur X est `@steipete`, que sur GitHub le dépôt principal est `steipete/openclaw`, que les discussions pertinentes se trouvent sur des subreddits comme `r/ClaudeCode`. Puis il cherche tout cela en parallèle, déjà orienté. La différence par rapport à la version précédente, écrit Van Horn dans le README, est structurelle : "L'ancien moteur cherchait des mots-clés. Le nouveau comprend votre sujet d'abord, puis cherche les bonnes personnes et les bonnes communautés."

Cela résout l'un des problèmes les plus agaçants de la recherche contextuelle : l'ambiguïté. Si vous cherchez "Paperclip", parlez-vous de la startup d'IA ou du petit trombone pour tenir les feuilles ensemble ? Le moteur résout `@dotta` et comprend que vous parlez de la première. Si vous cherchez "Dave Morin", vous obtenez non seulement son profil X mais aussi les connexions avec OpenClaw et les citations du podcast TWiST. La désambiguïsation a lieu avant la recherche, non après.

## Deux juges, pas un

L'un des éléments les plus inhabituels de `/last30days` est la présence d'un second juge dans le processus de synthèse. Le premier évalue la pertinence : à quel point un résultat est pertinent par rapport à la requête, à quel point il est récent, quel engagement il a reçu. Le second évalue quelque chose de différent : l'humour, l'esprit, la viralité.

La motivation est pratique. Reddit et X produisent quotidiennement des synthèses brillantes, des blagues parfaites, des commentaires qui capturent l'essence d'un phénomène mieux que n'importe quelle analyse. L'ancien système les enterrait car ils n'étaient pas "pertinents" au sens strict du terme. Un commentaire comme "My Michael Jordan is Steve Kerr" dans un thread sur l'Arizona Basketball obtient un score bas sur la pertinence thématique, mais très élevé sur la qualité expressive.

Le résultat est une section finale appelée "Best Takes" qui rassemble les citations les plus vives, les one-liners les plus partagés, les réactions qui donnent envie de revenir sur le sujet. Ce n'est pas une fonction décorative : c'est la reconnaissance que la culture numérique se déplace souvent via la bonne blague au bon moment, et non via l'analyse la plus précise.

## Comparaisons en parallèle, et non en série

Une autre fonction introduite dans la v3 mérite l'attention car elle résout un problème pratique que toute personne ayant essayé de comparer deux outils concurrents connaît bien. Dans les versions précédentes, une requête comme `/last30days "OpenClaw vs Hermes vs Paperclip"` exécutait trois recherches en série : d'abord l'une, puis l'autre, puis la dernière. Le temps d'exécution pouvait dépasser douze minutes. La v3 effectue en revanche un seul passage avec des sous-requêtes conscientes des entités pour tous les sujets simultanément, ramenant le temps à environ trois minutes avec la même profondeur d'analyse.

Il existe aussi le mode `--competitors`, qui fonctionne de manière encore plus autonome : à partir d'un sujet, le moteur découvre seul les principaux concurrents via une recherche web, puis lance des pipelines parallèles pour chacun et les fusionne en une comparaison structurée. C'est le genre de fonction qui transforme un outil de recherche en quelque chose qui ressemble à un analyste junior : il ne se contente pas de répondre à la question que vous avez posée, mais construit le contexte dans lequel cette réponse a du sens.

## Quinze plateformes, un brief

Le tableau des sources supportées dans le [dépôt](https://github.com/mvanhorn/last30days-skill) est long : Reddit, X, YouTube, TikTok, Instagram Reels, Hacker News, Polymarket, GitHub, Digg, Threads, Pinterest, Bluesky, Perplexity, recherche web traditionnelle. Certaines sont gratuites et fonctionnent sans configuration (Reddit avec commentaires, HN, Polymarket, GitHub). D'autres nécessitent une authentification ou des clés API payantes.

La présence de Polymarket est particulièrement intéressante : il ne recueille pas d'opinions, il recueille des cotes. Les probabilités sur Polymarket sont déterminées par ceux qui misent de l'argent réel sur la prédiction, non par ceux qui veulent paraître informés. Il existe une différence épistémique significative entre "beaucoup pensent que X va arriver" et "74 % des capitaux parient que X va arriver d'ici décembre". Le moteur l'affiche comme un signal séparé, avec les pourcentages de probabilité, non les volumes en dollars, car la magie réside dans la cote, pas dans le montant.

Pour GitHub, il existe aussi un "person-mode" : quand la requête concerne une personne spécifique, le moteur cesse de chercher qui en parle et commence à chercher ce que cette personne construit réellement. La commande `/last30days Peter Steinberger --github-user=steipete` renvoie non pas une revue de presse sur Steinberger mais une carte de son travail : combien de pull requests il a faites au cours du dernier mois, dans quels dépôts, à quel taux d'approbation, ce qu'il a publié.
![tabella1.jpg](tabella1.jpg)
[Les plateformes sur lesquelles les recherches sont effectuées](https://github.com/mvanhorn/last30days-skill)

## Opencode : un test sur le terrain

Quand j'ai vu le projet, la question immédiate a été : cela fonctionne-t-il aussi en dehors de l'écosystème Claude Code ? La réponse du dépôt est affirmative : la skill est installable sur Codex, Cursor, Copilot, Gemini CLI, et via le paquet ouvert `npx skills add mvanhorn/last30days-skill -g` sur plus de cinquante environnements compatibles avec le standard Agent Skills, dont `opencode`.

J'ai installé la skill sur opencode et j'ai fait une recherche concrète : les préférences des utilisateurs d'opencode sur quel modèle de langage gratuit o à bas coût offrait le meilleur rapport qualité-performance. Une requête de niche, avec une communauté petite mais active, qu'un moteur de recherche traditionnel aurait satisfaite avec zéro résultat utile.

Le rapport produit a parcouru des fournisseurs, des forums, des discussions GitHub et la documentation officielle. Il a distillé qu'opencode supporte plus de 75 fournisseurs et trois modes principaux d'accès aux modèles. Parmi les gratuits disponibles immédiatement, sans clés API : DeepSeek V4 Flash Free, un modèle mixture-of-experts de 284 milliards de paramètres avec un million de tokens de contexte, distribué sous licence MIT. Pour ceux qui souhaiteraient dépenser dix dollars par mois avec OpenCode Go, le modèle avec le meilleur rapport requêtes/qualité s'est avéré être encore DeepSeek V4 Flash, avec environ 158 000 requêtes mensuelles estimées, tandis que pour la qualité absolue, GLM-5.2 et Kimi K2.7 Code émergeaient, ce dernier particulièrement recommandé pour des agents MCP complexes. Pour ceux qui ne veulent pas dépendre du cloud, les modèles locaux via Ollama ou LM Studio étaient documentés en détail, avec Qwen3.6-27B comme choix pour un seul GPU de 24 Go.

Le rapport est sorti sous forme de fichier `.md` sur demande explicite, citant les sources. Il a pris environ une minute. Ce n'était pas parfait : certaines informations sur les prix nécessiteraient une vérification directe sur les sites des fournisseurs, et la communauté d'opencode est assez petite pour que l'échantillon soit statistiquement mince. Mais pour s'orienter rapidement dans un paysage qui change chaque semaine, c'était exactement ce qu'il fallait.

## Les limites que personne ne dit

L'honnêteté exige de mettre sur la table ce qui ne fonctionne pas, ou ce qui fonctionne avec des coûts cachés.

La première limite est structurelle : les sources les plus riches, TikTok, Instagram, Threads, YouTube avec commentaires, nécessitent une clé API de ScrapeCreators, un service payant. Les cent premières requêtes sont gratuites, puis on entre dans un modèle pay-per-use. Quiconque souhaite la version complète de l'outil doit prévoir un coût variable qui dépend de l'intensité de l'utilisation. Le modèle "gratuit" existe, mais il est nettement plus limité que celui décrit dans les cas d'utilisation du README.

La deuxième limite est épistémique, et plus subtile. L'outil optimise pour l'engagement : un thread Reddit avec 1 500 upvotes pèse plus qu'un post de blog que personne n'a lu. En principe, cela a du sens. En pratique, l'engagement est une mesure de la réactivité émotionnelle autant que de la qualité informative. Un post qui simplifie, indigne ou amuse recueille plus d'upvotes qu'une analyse nuancée. `/last30days` ne résout pas ce problème : il en hérite des plateformes qu'il interroge. La synthèse est aussi bonne que les conversations qu'il trouve, et les conversations en ligne ont leurs biais structurels.

La troisième limite concerne la latence des données : l'outil cherche ce qui s'est passé *ces dernières semaines*, et non ce qui s'est passé hier matin. Pour l'analyse des tendances et la recherche de contexte, cela fonctionne très bien. Pour les breaking news en temps réel, moins.

Enfin, une note sur la confidentialité. Le README déclare explicitement que la recherche reste locale, aucune donnée n'est transmise à des serveurs tiers en dehors des API que l'utilisateur configure lui-même. Il s'agit d'un projet MIT, vérifiable dans le code source. Mais quiconque utilise `/last30days` avec une clé X ou ScrapeCreators autorise de toute façon ces plateformes à recevoir les requêtes : la confidentialité est donc relative, elle dépend des sources activées.

## Qui gagne, qui perd, qui décide

Du point de vue des utilisateurs, `/last30days` répond à un besoin que les outils existants ignorent systématiquement : agréger des signaux sociaux hétérogènes sans passer des heures à le faire manuellement. C'est particulièrement utile dans trois contextes : avant une réunion avec quelqu'un dont on veut comprendre le travail récent, quand on doit évaluer un nouvel outil dans un secteur qui bouge vite, quand on cherche à comprendre si un trend est réel ou amplifié par les dix profils influents habituels.

Pour la catégorie des chercheurs professionnels et des journalistes, la question est plus complexe. L'outil accélère la collecte mais ne remplace pas le jugement. Le "Best Takes" peut être précieux pour comprendre comment une communauté réagit, mais sélectionner les blagues les plus virales n'est pas la même chose qu'identifier les voix les plus informées. L'optimisation pour l'engagement et celle pour la vérité sont des fonctions différentes, et parfois orthogonales.

Les plateformes qui sont interrogées ne tirent rien de ce schéma : `/last30days` utilise leurs API ou leurs données publiques sans renvoyer de trafic direct. C'est une dynamique déjà vue avec les moteurs de recherche traditionnels, mais amplifiée : ici, il n'y a même pas de click-through sur un lien. Reddit a déjà entrepris des batailles juridiques contre ceux qui utilisent ses données de manières non autorisées, et il n'est pas impossible qu'à l'avenir les conditions d'accès changent.

Le projet, avec ses 41 500 étoiles et 3 400 forks, est déjà assez grand pour attirer l'attention. La question n'est pas de savoir s'il fonctionne : il fonctionne, avec les limitations décrites. La question est de savoir où mène ce paradigme lorsqu'il est généralisé. Un agent qui interroge en parallèle toutes les conversations publiques sur un sujet, les fusionne, les synthétise et livre une réponse en une minute, est un outil puissant. Comme tout outil puissant, il en dit beaucoup plus sur celui qui l'utilise que sur lui-même.
