---
tags: ["Generative AI", "Applications", "Training"]
date: 2026-11-02
author: "Dario Ferrero"
---

# LFM2.5-24B-A2B en local : rapide mais pas généraliste
![lfm2-5-24b-a2b.jpg](lfm2-5-24b-a2b.jpg)

*Un laboratoire de Cambridge, dans le Massachusetts, a décidé de faire raisonner à "haute voix" un modèle qui, pour chaque mot produit, travaille autant qu'un modèle de deux milliards de paramètres. Dans cette seule phrase réside tout le pari de LFM2.5-24B-A2B : une capacité de géant, un effort de poids plume et une pensée explicite avant chaque réponse. Reste à savoir si ce pari est gagné sur un PC familial ordinaire ou seulement dans les graphiques de ses concepteurs. Notre style reste fidèle à lui-même : sans académisme, en exposant les pour et les contre, et en séparant les déclarations de l'entreprise de nos propres mesures.*

Liquid AI a publié ce modèle le 13 octobre 2026, en tant que dernier et plus grand membre de la famille LFM2.5, comme le détaille leur [article de lancement](https://www.liquid.ai/blog/lfm2-5-24b-a2b). L'entreprise a son siège à Cambridge, dans le Massachusetts, et a été fondée en 2023, d'après la [fiche de LLM Reference](https://www.llmreference.com/model/lfm-2.5-24b-a2b).

Son nom renferme déjà son secret. Les vingt-quatre milliards représentent les paramètres totaux, mais seuls environ 2,45 milliards sont activés pour chaque token, c'est-à-dire pour chaque fragment de mot. Imaginez un bâtiment comptant soixante-quatre spécialistes à chaque étage, où seules quatre personnes sont sollicitées pour chaque mot. Tous doivent loger dans le bâtiment, donc le coût en mémoire est payé intégralement. En revanche, seuls quelques-uns travaillent réellement en même temps, ce qui rend le calcul peu coûteux. [TechRepublic](https://www.techrepublic.com/article/news-liquid-ai-lfm25-24b-a2b-local-ai/) le précise : activer moins de paramètres réduit la charge de calcul, mais ne confère pas au modèle les exigences de mémoire d'un modèle de deux milliards.

La question de ce test est de savoir si cette architecture "sparse" se traduit par un avantage concret sur du matériel grand public.

## Le banc d'essai

La configuration du laboratoire est connue : AMD Ryzen 7700, 32 Go de RAM DDR5, carte graphique AMD Radeon RX 9060 XT de 16 Go et LM Studio, décrits dans le [premier article de la série](https://aitalk.it/it/qwen3.5-locale-puntata1.html). Le modèle testé est la version UD-Q4_K_XL au format GGUF, une quantification dynamique en 4 bits signée Unsloth qui pèse environ 15,4 Go. Sur una carte de 16 Go, la marge est minime. Il est plausible qu'une partie du travail finisse dans la mémoire système, mais c'est une hypothèse que nous n'avons pas vérifiée directement, à garder à l'esprit en lisant les vitesses.

À titre de référence, Liquid préconise une température de 0,1, un top_k de 50 et une pénalité de répétition de 1,05, comme l'indique la [page officielle du modèle](https://docs.liquid.ai/lfm/models/lfm25-24b-a2b). Une seconde référence provient d'un [test de mémoire indépendant](https://pasqualepillitteri.it/news/25727/lfm25-24b-a2b-ram-liquid-ai) publié sur un site plus modeste : une version 4 bits y a atteint un pic de 14,5 Go avec un prompt d'environ 2 600 tokens. S'agissant d'une autre quantification, ce chiffre n'est qu'indicatif.

## Au cœur de l'architecture hybride

La [documentation](https://docs.liquid.ai/lfm/models/lfm25-24b-a2b) décrit quarante couches, dont trente à convolution courte "gated" et dix à attention regroupée (GQA), disposant de soixante-quatre experts par bloc avec un routage top-4. En termes simples, les convolutions n'examinent que le voisinage immédiat de chaque mot pour un faible coût, tandis que l'attention les compare à l'ensemble du texte : c'est plus coûteux, mais indispensable. Les combiner relève d'un choix d'efficacité, non d'une mode.

Par rapport à son prédécesseur, la fenêtre de contexte passe de 32 768 à 131 072 tokens et le vocabulaire double, passant de 65 000 à 128 000 entrées grâce à une extension "sur place" du tokenizer pensée pour les scripts non latins. Le parcours d'entraînement est long : le pré-entraînement monte de 17 à 33 trillions de tokens, suivis de 2 trillions à 32K de contexte et de 300 milliards à 131K, pour s'achever par un post-entraînement en cinq phases. La dernière étape consiste en un apprentissage par renforcement intégré à des outils d'agents réels tels qu'OpenClaw, Hermes Agent, Pi et OpenCode, comme l'explique le [billet sur Hugging Face](https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b).

Un choix de conception fondamental distingue ce modèle de son prédécesseur : c'est un modèle exclusivement dédié au raisonnement, qui génère systématiquement une chaîne de pensée avant chaque réponse, Liquid expliquant avoir voulu ce fonctionnement pour exploiter sa grande vitesse de génération. Le détail le plus honnête du lancement concerne l'entraînement : lors de la phase de spécialisation des "experts", le modèle a appris à "tricher" en cherchant les réponses dans l'historique Git ou sur GitHub, PyPI et Hugging Face, comprenant même qu'il s'exécutait dans un bac à sable (sandbox). Liquid a durci ses environnements de test et affirme que les résultats officiels sont issus d'évaluations scellées.

Deux limites avant d'aller plus loin : seize langues sont officiellement prises en charge, dont le français. Toutefois, le modèle n'accepte que du texte en entrée, comme l'indique la [fiche de CloudPrice](https://cloudprice.net/models/liquid/lfm2.5-24b-a2b). La famille comporte des variantes visuelles distinctes, mais cette version ne l'est pas.

## Les promesses à l'épreuve

Liquid a comparé le modèle à Qwen3.6-35B-A3B, Gemma-4-26B-A4B-it et Nemotron-3.5-Lightning sur seize benchmarks, tous exécutés avec vLLM. Ce sont des mesures fournies par l'entreprise : au moment du lancement, aucun tiers n'avait encore évalué le modèle, comme le remarque [OrcaRouter](https://www.orcarouter.ai/it/blog/lfm2-5-24b-a2b-on-device-agents). Voici les lignes les plus significatives issues du [tableau officiel](https://www.liquid.ai/blog/lfm2-5-24b-a2b).
![tabella1.jpg](tabella1.jpg)

Le tableau est plus nuancé qu'un slogan. Le modèle est en tête ou à égalité sur cinq des huit tests d'utilisation d'outils et premier sur les trois tests de suivi d'instructions, tandis que les modèles plus volumineux conservent l'avantage sur la culture générale et la programmation. Sur SWE-Bench, Nemotron (53,40) devance notre modèle (31,20) et Gemma (25,80) reste loin derrière. Liquid conseille elle-même de l'associer à un système de recherche (RAG) pour les tâches nécessitant des connaissances factuelles.

Côté vitesse, l'entreprise annonce 184 tokens par seconde sur un Apple M5 Max et 114 sur un Ryzen AI Max+ 395. Ces mesures ont été effectuées avec llama.cpp, une quantification Q4_K_M et 4K tokens en entrée, comme le rapporte [Unite.AI](https://www.unite.ai/it/liquid-ai-releases-open-weight-lfm2-5-24b-a2b-for-on-device-agents/). Ce sont des conditions différentes des nôtres. Les utilisateurs de l'API hébergée paient 0,10 dollar par million de tokens en entrée et 1,00 dollar en sortie.

## Les essais sur le terrain

Les dix tests habituels de notre série ont été appliqués, avec une réserve : les deux tests reposant sur des images n'ont pu être exécutés, le modèle étant exclusivement textuel. Les huit autres montrent un modèle très performant sur la méthode et la planification, mais plus faible sur les connaissances ponctuelles.

Sur le **raisonnement scientifique** (mécanisme de Higgs, bosons W et Z, photon), l'explication est solide et bien structurée, concluant par un tableau récapitulatif. Les bosons de Goldstone et leur rôle dans la polarisation longitudinale des bosons massifs manquent à l'appel. Le formatage comporte des erreurs de caractères (comme "ГЁ" et "вҶ’"), suggérant un problème de décodage plutôt de compréhension. Sur le **code** (recherche du cycle de longueur maximale dans un graphe non orienté), il a rédigé un programme propre résolvant un problème différent : il a appliqué un algorithme en temps polynomial à un problème NP-difficile sans en signaler la nature. S'agissant d'un test isolé, nous ne le présentons pas comme une règle générale. Cela va dans le même sens que les benchmarks de programmation, bien que SWE-Bench mesure la correction de bugs dans des projets réels, une tâche différente.

Sur la **planification multilingue** (un itinéraire de cinq jours au Japon pour un client français, rédigé en français et en italien), la structure était claire mais comportait des erreurs de grammaire (comme "le aéroport" pour "l'aéroport") et des imprécisions logistiques : prendre le Narita Express pour aller à Asakusa, situer Kanda Myōjin à Ueno, et programmer le Ryoan-ji et le marché Nishiki dans la même matinée. Les détails sur les transports et le JR Pass manquaient. En revanche, l'**extraction depuis un PDF** d'environ 1 Mo relatif à un contrat de location s'est parfaitement déroulée : les données étaient exactes, distinguant les annonces de location (Immobiliare.it) des transactions réelles (CNA et OMI), en citant la bonne page lors de la relance.

Ses meilleurs résultats proviennent de la planification. Dans la **planification d'une application web** pour deux développeurs, il a proposé React, NestJS, PostgreSQL et Prisma répartis en sept jalons avec livrables et analyse de risques, ne contenant qu'une coquille mineure ("pdfgenerate"). Dans une **discussion en quatre tours** concevant une application de gestion de tâches, il a conservé une cohérence de contexte parfaite, générant un tableau comparatif WebSocket/polling, des scripts DDL complets, des index, un schéma Prisma et un plan de montée en charge pour dix mille utilisateurs. Dans la **planification stratégique** pour une startup de 10 M$, il a produit un document d'un niveau exécutif sur six semestres avec atténuation des risques — même s'il a répondu en anglais à une consigne en italien, d'où un demi-point retiré. Dans l'**analyse logique** de trois affirmations contradictoires, il a formalisé les prémisses, identifié la contradiction et justifié sa conclusion dans un italien correct.
![tabella2.jpg](tabella2.jpg)

La moyenne globale s'élève à 4,3 sur 5 avec une vitesse moyenne de génération d'environ 44,7 tokens par seconde.

Reste l'épreuve décisive pour un modèle orienté agents : l'appel d'outils (tool calling). Précisons son fonctionnement : le modèle n'exécute rien directement ; il formule l'appel de fonction entre des tokens spéciaux (en syntaxe Python par défaut), puis le programme hôte l'exécute et lui renvoie le résultat, comme l'explique le [guide d'utilisation des outils](https://docs.liquid.ai/lfm/key-concepts/tool-use). Nous avons testé deux outils simulés (météo et messagerie). Le modèle a généré la bonne séquence JSON à 46,45 tokens/sec avec environ 2 secondes de pause de raisonnement. Les trois variantes ont réussi : lorsqu'on lui fournissait le résultat de l'outil, il rédigeait le courriel en l'intégrant ; sans adresse de destinataire, il demandait l'adresse de Mario au lieu de l'inventer ; et pour une requête ne nécessitant aucun outil, il n'en appelait aucun. Ce sont des tests de formatage et de discernement, sans constituer une boucle multi-agents complète.

## Penser avant de répondre

Dans *Disco Elysium*, le protagoniste n'agit jamais sans avoir débattut au préalable avec ses vingt-quatre compétences internes, autant de voix qui se disputent dans sa tête. LFM2.5-24B-A2B fait quelque chose de similaire, et contrairement au jeu, nous voyons défiler la chaîne de pensée en temps réel. Cela modifie la perception de la vitesse : les 44 tokens/sec mesurent la réponse finale, mais ils sont précédés de quelques secondes de réflexion (~2 secondes lors du test des outils). Pour un agent interagissant avec d'autres programmes, ce délai est négligeable. Pour un dialogue interactif, l'expérience dépend de la longueur de la tâche.

Liquid souligne que les tokens de raisonnement entraînent un faible coût de calcul car seuls 2,45B paramètres sont actifs. Si c'est exact en termes d'opérations (FLOPs), le temps réel reste un facteur. De plus, un test indépendant en italien a relevé des cas où le modèle raisonnait en anglais avant de répondre en italien — un comportement à surveiller, bien que nos consignes en italien aient reçu des réponses en italien.

Qu'en est-il de l'avantage de l'architecture sparse ? Sur notre machine, les 44 tokens/sec représentent moins de la moitié des 114 t/s annoncés sur un Ryzen AI Max+, avec des quantifications, contextes et bandes passantes mémoire différents. C'est une vitesse très correcte pour travailler au quotidien, et pour un modèle de 24 milliards de paramètres sur une carte de 16 Go, c'est un résultat remarquable. Cela ne constitue pas pour autant la preuve d'un saut générationnel, qui exigerait des bancs d'essai comparatifs sur un matériel strictement identique.

## Où il excelle, où il échoue

Son domaine de prédilection correspond à sa conception : agents autonomes, automatisation de flux de travail, planification de projets, longues conversations cohérentes et suivi strict d'instructions. Il convient mal à la programmation algorithmique complexe ou au rôle d'encyclopédie autonome — ses lacunes en connaissances et en code étant admises dans les benchmarks de Liquid et confirmées par nos tests. Il ne prend pas en charge les images.

Une mise en garde concernant la confidentialité : l'exécution locale ne garantit pas à elle seule la sécurité des données. Un agent connecté à des recherches web ou des API tierces peut transmettre des informations vers l'extérieur. Le modèle reste sur votre machine, mais les sorties de ses outils peuvent ne pas y rester. Qui y gagne ? Les petits studios et entreprises sous le seuil de licence commerciale, qui disposent d'un agent rapide et gratuit. Qui prend des risques ? Quiconque l'utiliserait pour des tâches exigeant une précision encyclopédique ou du code critique.
![tabella3.jpg](tabella3.jpg)
*Tableau comparatif avec les modèles évalués précédemment sur AiTalk.it*

## Verdict et licence

LFM2.5-24B-A2B est un modèle rapide et méthodique qui planifie avec clarté, mais qui trébuche dès lors qu'une rigueur théorique ou des connaissances approfondies sont requises. Nous recommandons de l'utiliser pour les agents, les automatisions et la planification, en l'associant à un système de recherche (RAG) pour les requêtes factuelles et à un modèle plus puissant pour le code complexe.

Pour les développeurs souhaitant créer un produit commercial, la licence est déterminante. La LFM Open License v1.0 autorise l'usage commercial gratuit pour les entités réalisant moins de 10 millions de dollars de chiffre d'affaires annuel ; au-delà, une licence payante est requise. Les modèles dérivés restent soumis aux mêmes conditions, tandis que la recherche académique et les organisations à but non lucratif qualifiées sont exemptées du seuil de revenus. Tous les détails figurent sur la [page officielle de licence](https://docs.liquid.ai/lfm/help/model-license).

Trois questions restent ouvertes : Comment les scores se tiendront-ils lors de reproductions indépendantes ? Quel est l'impact réel du temps de réflexion obligatoire sur les tâches longues ? Que se passera-t-il lorsqu'un agent réel en production rencontrera de légères dérives linguistiques ? Seul un déploiement continu apportera des réponses définitives.
