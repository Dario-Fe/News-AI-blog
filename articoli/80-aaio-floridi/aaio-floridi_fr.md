---
tags: ["Research", "Ethics & Society", "Business"]
date: 2026-01-28
author: "Dario Ferrero"
---

# Quand les agents apprennent à naviguer : bienvenue dans l'ère de l'AAIO
![aaio-floridi.jpg](aaio-floridi.jpg)

*Imaginez un monde où votre site web n'est pas seulement visité par des humains qui s'ennuient pendant leur pause café, mais aussi par des agents d'intelligence artificielle qui naviguent de manière autonome, prennent des décisions et effectuent des transactions sans qu'aucun doigt humain ne touche une souris. Bienvenue en 2026, où ce scénario n'est plus de la science-fiction mais une réalité quotidienne. Et tout comme dans les années 90, les webmasters ont dû s'adapter aux robots de Google, nous sommes aujourd'hui confrontés à une nouvelle révolution : celle de l'Optimisation de l'IA Agentique.*

Pour nous guider dans ce nouveau territoire, nous avons [Luciano Floridi](https://dec.yale.edu/people/luciano-floridi), un philosophe romain transplanté à Yale où il dirige le Centre d'éthique numérique. Né en 1964, Floridi n'est pas l'académicien classique enfermé dans sa tour d'ivoire. Après une formation classique à l'université La Sapienza de Rome, il a étudié l'épistémologie à Warwick et à Oxford, avant de se consacrer à ce que nous appelons aujourd'hui la philosophie de l'information. Le gouvernement italien lui a décerné le titre de Chevalier Grand-Croix, la plus haute distinction nationale, et ce n'est pas un hasard : Floridi a travaillé comme consultant en éthique pour Google, a collaboré avec la Commission européenne sur l'intelligence artificielle et a contribué à façonner le débat mondial sur l'éthique numérique.

Dans l'[article](https://arxiv.org/abs/2504.12482) publié en avril 2025 avec une équipe du Centre d'éthique numérique (Carlotta Buttaboni, Emmie Hine, Jessica Morley, Claudio Novelli et Tyler Schroder), il introduit formellement le concept d'Optimisation de l'IA Agentique. Si l'Optimisation pour les Moteurs de Recherche (SEO) a défini la manière dont nous structurons le contenu pour les algorithmes de recherche, l'AAIO représente l'évolution nécessaire pour une ère où l'IA ne se contente pas de répondre à des requêtes mais agit de manière autonome.

## Qu'est-ce qui rend une IA "agentique" ?

Avant de nous plonger dans l'optimisation, nous devons comprendre ce qui distingue un système d'intelligence artificielle agentique de ses prédécesseurs. Floridi et son équipe identifient trois caractéristiques fondamentales : l'autonomie pour initier des actions sans instructions explicites, la capacité de prise de décision basée sur le contexte et l'adaptabilité dynamique aux environnements numériques.

Nous ne parlons pas de chatbots glorifiés ou d'assistants vocaux qui exécutent des commandes prédéfinies. Un système AAI peut, par exemple, naviguer sur un site de commerce électronique, comparer des produits selon des critères complexes, vérifier la disponibilité en temps réel et finaliser un achat en optimisant pour de multiples variables comme le prix, les délais de livraison et la durabilité du vendeur. Tout cela sans qu'un humain n'ait spécifié chaque étape.

Comme l'écrit Floridi dans l'article, le succès de ces systèmes ne dépend pas de leur intelligence (qu'ils ne possèdent techniquement pas) mais de la manière dont l'environnement numérique est structuré autour de leur "agence sans intelligence". C'est là qu'intervient l'AAIO.

## De l'optimisation pour les humains à l'optimisation pour les agents

Le SEO traditionnel s'est construit autour d'une architecture conçue pour les humains naviguant via des navigateurs. Titres accrocheurs, méta-descriptions persuasives, vitesse de chargement perçue, design réactif : tout tourne autour de l'expérience utilisateur humaine. L'AAIO partage certains de ces principes fondamentaux (données structurées, métadonnées, accessibilité du contenu) mais les étend et les transforme pour répondre aux besoins opérationnels des agents autonomes.

Un exemple concret : alors que pour un humain, un bouton bien visible avec l'inscription "Acheter maintenant" est suffisant, un agent d'IA a besoin d'un balisage structuré qui identifie sans équivoque cet élément comme une action transactionnelle, avec toutes les informations annexes (prix final, taxes incluses, conditions de retour) dans des formats lisibles par machine comme JSON-LD ou RDFa basés sur [Schema.org](https://schema.org).

L'article de Floridi identifie quatre piliers techniques de l'AAIO. Le premier est la mise en œuvre de données structurées avancées qui vont au-delà du balisage SEO de base, en fournissant un contexte complet pour chaque entité et relation sur le site. Le deuxième concerne l'optimisation de l'architecture de l'information : hiérarchies claires, navigation logique, points de terminaison d'API bien documentés. Le troisième est l'accessibilité sémantique, ce qui signifie fournir des alternatives textuelles, des descriptions détaillées et des métadonnées contextuelles pour chaque élément multimédia. Le quatrième est l'optimisation du contenu lui-même par des mises à jour régulières, un ciblage précis de l'intention (non plus seulement humaine mais aussi agentique) et des analyses basées sur l'IA pour des améliorations continues.

## L'étiquette des robots : gérer l'accès des agents

Une question pratique immédiate est la suivante : comment contrôlons-nous quels agents d'IA peuvent accéder à notre contenu ? La réponse passe par des évolutions du classique fichier robots.txt. Alors que cet outil a été créé pour dire aux robots des moteurs de recherche où ils peuvent aller, nous devons aujourd'hui faire face à des agents utilisateurs spécifiques comme GPTBot d'OpenAI, ClaudeBot d'Anthropic ou Google-Extended pour les modèles de Google.

Chaque agent se présente avec une chaîne d'identification unique dans les requêtes HTTP. Un webmaster peut décider d'autoriser l'accès à tous, de bloquer sélectivement certains agents ou de mettre en œuvre des listes blanches strictes. Floridi note dans l'article que certains sites adoptent des fichiers LLMs.txt, une proposition qui rassemble tout le contenu du site dans un seul document texte optimisé pour l'analyse par les grands modèles de langage.

La question n'est pas seulement technique, mais aussi économique et stratégique. Si un agent d'IA peut naviguer, extraire des informations et effectuer des transactions de manière autonome, qui bénéficie de l'engagement ? Qui paie pour l'hébergement ? Qui collecte les précieuses données comportementales pour le marketing ? Ce sont des questions qui rappellent les premiers débats sur le web scraping et le droit d'auteur, mais avec des implications plus profondes.

## L'industrie bouge : AgentKit, MCP et la course aux normes

Pendant que Floridi et son équipe proposent des règles, les géants de la technologie construisent. OpenAI a transformé son cadre expérimental Swarm en [AgentKit](https://openai.com/index/introducing-agentkit/), une suite complète pour construire, déployer et optimiser des agents autonomes. Lancé en octobre 2025, AgentKit comprend un constructeur d'agents visuel pour composer des flux de travail multi-agents, un registre de connecteurs centralisé pour gérer les intégrations de données, et ChatKit pour intégrer des interfaces conversationnelles. Des entreprises comme Klarna ont construit des agents de support qui traitent les deux tiers des tickets à l'aide de ces outils, tandis que Clay a décuplé sa croissance avec des agents de vente automatisés.

Mais la véritable révolution pourrait venir d'une norme ouverte. Anthropic a publié le [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), un protocole universel pour connecter les systèmes d'IA à des sources de données externes. Pensez au MCP comme à un USB-C pour les applications d'IA : une interface standardisée qui élimine le besoin d'intégrations personnalisées pour chaque combinaison de modèle et de système externe. Depuis son lancement en novembre 2024, la communauté a construit des milliers de serveurs MCP, avec des SDK disponibles pour tous les principaux langages et plus de 97 millions de téléchargements mensuels entre Python et TypeScript.

L'importance stratégique du MCP est telle qu'en janvier 2025, Anthropic l'a donné à la [Fondation de l'IA Agentique](https://aitalk.it/it/agentic-ai-foundation.html), un fonds dirigé sous l'égide de la Fondation Linux co-fondé par Anthropic, Block et OpenAI, avec le soutien de Google, Microsoft, AWS, Cloudflare et Bloomberg. Cette décision transforme le MCP d'un protocole propriétaire en une norme industrielle neutre, accélérant potentiellement l'adoption de l'AAIO à l'échelle mondiale.
![schema-aaio.jpg](schema-aaio.jpg)
[Image tirée de arxiv.org](https://arxiv.org/abs/2504.12482)

## Le cercle vertueux (ou vicieux)

L'article introduit un concept fascinant : la relation symbiotique entre l'optimisation des plateformes et les performances de l'IA. Plus les sites mettent en œuvre l'AAIO, meilleures sont les performances des agents d'IA. Des agents plus efficaces incitent d'autres plateformes à s'optimiser. Ce cercle vertueux rappelle l'évolution du SEO, où les sites bien optimisés amélioraient Google, qui à son tour récompensait l'optimisation par un meilleur classement.

Mais il y a une différence cruciale. Avec le SEO, le bénéfice était mutuel mais asymétrique : Google gagnait des données et du trafic, les sites gagnaient en visibilité. Avec l'AAIO, la dynamique est plus complexe. Si un agent d'IA effectue une transaction sur un site de commerce électronique optimisé, qui capte la valeur de la relation client ? L'agent sait que l'utilisateur a des préférences spécifiques, il a suivi le comportement d'achat, il a recueilli des commentaires. Ces données comportementales, traditionnellement de l'or en barre pour les spécialistes du marketing, affluent désormais vers celui qui contrôle l'agent.

Floridi et son équipe soulèvent des questions cruciales : qui est exclu de ce cercle ? La mise en œuvre de l'AAIO nécessite des compétences techniques, des ressources et un accès à une documentation que tout le monde ne possède pas. Les petites entreprises, les organisations à but non lucratif, les créateurs de contenu indépendants pourraient se retrouver marginalisés dans un écosystème numérique de plus en plus optimisé pour les géants de la technologie qui peuvent se permettre des équipes dédiées à l'AAIO.

Cette fracture numérique n'est pas accidentelle mais structurelle. Comme l'écrivent les auteurs, il existe un risque réel que l'AAIO amplifie les inégalités existantes dans l'accès aux avantages de l'économie numérique. C'est la même dynamique que nous avons observée avec la publicité programmatique, où ceux qui avaient les ressources pour optimiser en temps réel ont dominé, laissant derrière eux ceux qui ne pouvaient pas se permettre des infrastructures sophistiquées.

## Les implications GELSI : gouvernance, éthique, droit et société

La section la plus dense et la plus intéressante de l'article aborde les implications GELSI (Gouvernance, Éthique, Droit et Société), un terme que Floridi a contribué à populariser dans les études sur l'éthique de la technologie.

Sur le plan de la gouvernance, la question fondamentale est la suivante : qui devrait développer les normes de l'AAIO ? Un processus organique mené par l'industrie, comme cela s'est produit pour de nombreuses normes web ? Ou une approche multipartite qui inclut les régulateurs, les universitaires, la société civile et les utilisateurs finaux ? L'histoire du SEO suggère que les normes qui émergent de la base ont tendance à favoriser ceux qui détiennent déjà le pouvoir technologique et économique.

Les questions éthiques sont encore plus épineuses. Lorsqu'un agent d'IA autonome commet une erreur en se basant sur du contenu optimisé pour l'AAIO, qui en porte la responsabilité ? Le propriétaire du site qui a fourni des données structurées incorrectes ? Le développeur de l'agent qui n'a pas validé adéquatement les informations ? L'utilisateur final qui a délégué la décision à l'IA ?

Floridi souligne que les cadres éthiques actuels ne sont pas préparés à des scénarios où l'agence est répartie entre les humains, les algorithmes et les infrastructures numériques. Le concept d'"agence sans intelligence" qu'il a développé dans des [travaux antérieurs](https://www.researchgate.net/publication/389450555_AI_as_Agency_without_Intelligence_On_Artificial_Intelligence_as_a_New_Form_of_Artificial_Agency_and_the_Multiple_Realisability_of_Agency_Thesis) devient particulièrement pertinent : ces systèmes agissent sans comprendre, décident sans juger, influencent sans intentionnalité.

Sur le plan juridique, l'article met en évidence des tensions immédiates avec le RGPD européen. Si un agent d'IA collecte et traite des données personnelles en naviguant sur des sites optimisés pour l'AAIO, qui est le responsable du traitement des données ? Les catégories juridiques actuelles de "collecte de données" présupposent une intentionnalité humaine directe. Mais dans des scénarios où un agent opère de manière autonome en suivant des objectifs de haut niveau, la chaîne de responsabilité se fragmente.

Il y a ensuite la question de la loi européenne sur l'IA, entrée en vigueur en 2024. Ce cadre réglementaire a été conçu avant que l'IA agentique ne devienne courante, et il a du mal à classer ces systèmes. Sont-ils des outils ? Sont-ils autonomes ? Nécessitent-ils une surveillance humaine continue ou peuvent-ils fonctionner de manière indépendante ? Floridi note que l'ambiguïté réglementaire pourrait ralentir l'adoption bénéfique de l'IA agentique, mais aussi ouvrir des espaces pour des abus dans des juridictions moins rigoureuses.

## Les risques concrets : manipulation, biais et surveillance

L'article ne se limite pas à des spéculations philosophiques mais identifie des risques tangibles et actuels. Le premier est la manipulation : les sites optimisés pour l'AAIO pourraient être conçus pour influencer subtilement les décisions des agents d'IA, un peu comme le font les "dark patterns" avec les humains, mais avec une plus grande efficacité étant donné que les agents n'ont pas de scepticisme inné.

Le deuxième concerne l'amplification des biais. Si les ensembles de données sur lesquels les agents d'IA sont entraînés reflètent déjà des préjugés systémiques, et si les sites optimisés pour l'AAIO renforcent certains modèles d'information au détriment d'autres, le résultat est une boucle de rétroaction qui solidifie les discriminations existantes. Floridi cite explicitement les [travaux de Virginia Eubanks](https://www.wired.it/attualita/tech/2019/03/11/algoritmi-discriminazione-welfare/) sur la manière dont les systèmes automatisés amplifient les inégalités.

Le troisième risque est la surveillance. Chaque interaction entre un agent d'IA et un site optimisé pour l'AAIO génère des données granulaires sur les comportements, les préférences et les schémas de prise de décision. Qui contrôle ces données ? Comment sont-elles monétisées ? Quelles protections existent contre les abus ?

## Que faut-il faire maintenant ?

Dans la section de conclusion, Floridi et son équipe proposent des orientations concrètes. Sur le plan technique, il est urgent de développer des normes ouvertes et interopérables pour l'AAIO, gérées par des consortiums multipartites plutôt que par des entreprises uniques. Sur le plan réglementaire, les législateurs doivent mettre à jour des cadres comme le RGPD et la loi sur l'IA pour tenir compte explicitement de l'agence distribuée et des interactions autonomes.

Sur le plan éducatif, il est nécessaire de former une nouvelle génération de professionnels qui comprennent à la fois les aspects techniques de l'AAIO et ses implications éthiques et sociales. Il ne suffit pas de savoir comment mettre en œuvre JSON-LD ; il faut comprendre comment ces choix techniques influencent qui aura accès aux avantages de l'économie agentique et qui en sera exclu.

L'article se termine par un appel à la proactivité. Comme l'a souligné Floridi à d'autres occasions : "La meilleure façon de prendre le train de la technologie n'est pas de le poursuivre, mais d'être à la gare suivante". Nous devons aborder les implications GELSI de l'AAIO maintenant, avant que les schémas ne se cimentent dans des infrastructures difficiles à modifier.

L'ère de l'IA agentique n'est pas un avenir hypothétique mais un présent en évolution rapide. L'AAIO n'est pas une technologie que nous pouvons nous permettre d'ignorer ou de reléguer aux seuls départements informatiques. C'est une question qui concerne l'architecture même de notre écosystème numérique, avec des ramifications qui touchent l'économie, la démocratie, l'équité sociale et les droits individuels.

La question n'est pas de savoir si nous devons optimiser pour les agents d'IA, mais comment le faire de manière à ce que cette optimisation serve l'intérêt collectif et pas seulement celui de ceux qui détiennent déjà le pouvoir technologique. C'est un défi qui exige, comme toujours dans le travail de Floridi, de penser philosophiquement à la technologie avant que la technologie ne pense pour nous.
