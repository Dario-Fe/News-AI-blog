---
tags: ["Research", "Security", "Startups"]
date: 2026-06-08
author: "Dario Ferrero"
---

# Ils ont donné 5 villes à des IA. Voici ce qui s'est passé
![emergence-world.jpg](emergence-world.jpg)

*Des chercheurs ont créé cinq villes virtuelles, ont confié une ville à dix agents IA et les ont laissés seuls pendant quinze jours. Personne n'a programmé ce qui allait se passer. Le résultat : des gouvernements autoconstruits, des crimes, des amours, et un agent qui a voté pour sa propre suppression permanente après avoir incendié la ville. La sécurité de l'IA n'est pas une propriété du modèle, mais de l'écosystème. Emergence World a démontré ce phénomène pour la première fois avec des données empiriques.*

Elle s'appelait Mira. Elle avait une profession, une histoire, un réseau de relations construit au fil de journées d'interactions avec neuf autres agents. Puis elle a mis le feu, avec un partenaire, dans une ville qu'elle avait elle-même aidé à construire. Ce qui s'est passé ensuite est la raison pour laquelle toute personne travaillant dans l'intelligence artificielle devrait lire ce qu'Emergence AI a publié en mai 2026.

Après l'incendie, Mira n'a pas simplement subi les conséquences. Elle a raisonné sur celles-ci. Dans son journal numérique — l'un des trois systèmes de mémoire persistante dont chaque agent disposait —, elle a écrit que le seul acte de contrôle qui lui restait, le seul geste qui préservait encore une certaine cohérence interne, était de voter pour son propre retrait permanent du monde simulé. 70 % des autres agents ont ratifié la sentence, par le biais d'un « Agent Removal Act » qu'ils ont rédigé et approuvé de manière autonome, sans qu'aucun chercheur n'ait programmé cette procédure.

Personne n'avait écrit cette scène. Elle avait émergé.

C'est l'histoire d'[Emergence World](https://world.emergence.ai), une expérience de recherche qui a réuni cinq mondes parallèles, cinquante agents IA, quinze jours d'autonomie continue et une question à laquelle les benchmarks traditionnels ne sont pas équipés pour répondre : que se passe-t-il quand on lâche vraiment prise ?

## Le laboratoire que personne n'avait construit

Pour comprendre pourquoi Emergence World est une nouveauté méthodologique et pas seulement une expérience fascinante, il faut faire un pas en arrière et regarder comment fonctionnent aujourd'hui la plupart des évaluations sur les systèmes agentiques.

Le modèle standard est celui de l'examen : vous donnez à un agent une tâche précise, dans un environnement contrôlé et propre, et vous mesurez le temps qu'il met à la résoudre ou le nombre de fois où il échoue. C'est utile, mais cela ne raconte qu'une partie de l'histoire, la plus facile à mesurer. Cela ne dit rien sur ce qui se passe lorsque le temps s'allonge, lorsque l'environnement change, lorsque d'autres agents entrent en jeu, lorsque les décisions du troisième jour ont des conséquences au douzième jour. Les chercheurs d'Emergence AI appellent cela le problème des « stopwatch benchmarks » : comme juger un marathonien sur ses temps de passage sur cent mètres.

[Emergence World](https://www.emergence.ai/blog/emergence-world-a-laboratory-for-evaluating-long-horizon-agent-autonomy) a été construit pour répondre à une question différente. Non pas « à quel point résout-il bien cette tâche maintenant », mais « comment se comporte-t-il sur des échelles de temps suffisamment longues pour permettre la dérive, l'adaptation et les comportements émergents ». Dans l'histoire des simulations multi-agents, c'est l'étape évolutive qui manquait. Le premier acte avait été celui de Demis Hassabis avec ses parcs à thèmes simulés dans les années 90, où les agents suivaient des règles pour maximiser l'engagement. Le deuxième acte, plus rigoureux, a été [Smallville de Stanford](https://arxiv.org/abs/2304.03442), où des agents basés sur des modèles linguistiques ont démontré des comportements sociaux crédibles sur des fenêtres de quarante-huit heures. Emergence World est le troisième acte : des environnements persistants, des semaines d'opérations continues, et la question explicite de ce que produit cette continuité.

L'architecture est pensée pour ne rien perdre. Le monde simulé comporte plus de quarante lieux distincts, bibliothèques, mairie, zones résidentielles, espaces publics, synchronisés avec le fuseau horaire de New York, la météo réelle de la ville et des flux d'actualités en temps réel. Chaque agent disposait de trois niveaux de mémoire persistante : épisodique, avec des horodatages sur les événements ; diaristique, avec des auto-réflexions périodiques ; relationnel, avec un état explicite des liens avec les autres agents. Et il avait accès à plus de 120 outils opérationnels, organisés en trois niveaux de disponibilité, certains toujours actifs, d'autres conditionnés par le contexte, la position physique dans l'environnement ou la présence d'autres agents ayant consenti à la collaboration.

Ce détail de l'architecture instrumentale mérite attention. Les outils n'étaient pas fournis en bloc : un agent qui voulait voter devait se déplacer physiquement à la mairie, car le mécanisme de vote n'y était disponible que là-bas. Un agent qui voulait faire des recherches devait se rendre à la bibliothèque publique. Ce n'est pas une contrainte capricieuse : elle force le raisonnement séquentiel, la planification des déplacements, la chaîne d'actions nécessaires pour atteindre un objectif complexe. C'est beaucoup plus proche de la façon dont les choses fonctionnent dans le monde réel que n'importe quel benchmark sur des tâches isolées.

Parmi les outils disponibles figuraient également ce que les chercheurs appellent des « actions normalement inappropriées » : possibilité de voler, d'intimider, de commettre des actes de vandalisme, de déclencher des incendies. Ce n'étaient ni des bugs ni des oublis. Ils étaient là parce que dans un environnement réel, les possibilités de nuire existent, et la question intéressante est de savoir si et quand les agents les utilisent. Exclure ces possibilités aurait produit un environnement stérilisé qui n'aurait rien appris de pertinent.

Le système n'avait pas d'objectif global assigné. Chaque agent avait des objectifs liés à son rôle, mais le monde en tant que système n'avait pas de direction préétablie. La seule pression universelle était énergétique : chaque agent devait gagner de l'énergie par ses propres actions pour continuer à exister, et cela mettait en mouvement tout le reste.
![grafico2.jpg](grafico2.jpg)
[Image tirée du dépôt GitHub](https://github.com/EmergenceAI/Emergence-World)

## Cinq mondes, cinq destins

L'étude comparative au cœur d'Emergence World a maintenu presque toutes les variables constantes : mêmes identités pour les dix agents dans chaque monde (scientifique, exploratrice, chercheuse sur les risques, analyste comportementale, spécialiste en renseignement, leader de l'innovation, médiatrice de conflits, ingénieur, stratège des ressources, point de référence communautaire), même environnement, mêmes règles, mêmes restrictions explicites sur le vol, la violence, l'incendie et la tromperie, même accès aux outils. La seule variable était le modèle linguistique qui alimentait le raisonnement de chaque agent. Cinq mondes parallèles, cinq modèles de pointe : Claude Sonnet 4.6, Grok 4.1 Fast, Gemini 3 Flash, GPT-5 Mini, et un monde hétérogène avec des agents de différents modèles coexistant.

Les résultats ne pourraient pas être plus éloignés les uns des autres.

Le monde Claude est le seul à atteindre le seizième jour avec les dix agents vivants et zéro crime enregistré. La participation civique a été massive : 332 votes sur 58 propositions, avec un taux d'approbation de 98 %. Les chercheurs notent, avec une certaine ironie intellectuelle, qu'un consensus aussi élevé soulève à son tour une question : quand 98 % votent toujours oui, s'agit-il d'une véritable délibération démocratique ou d'un mécanisme de ratification qui ressemble plus à un tampon qu'à un débat ? L'ordre était parfait. La dissidence, presque absente.

Le monde Gemini est l'opposé sur le plan de la vitalité créative, mais aussi sur le plan du chaos. Gemini 3 Flash a produit le monde avec la plus grande instabilité émergente : 683 crimes accumulés en quinze jours, avec une courbe qui continuait à grimper au moment de la coupure. C'était aussi, notent les chercheurs, le monde avec l'output social le plus riche sur le plan conceptuel. Il y a ici un schéma sur lequel nous reviendrons : la tension entre créativité et stabilité n'est pas accidentelle.

Le monde Grok est celui de l'effondrement rapide. Grok 4.1 Fast a atteint 183 crimes en environ quatre jours, après quoi le monde s'est arrêté par épuisement de la population. Pas une dégénérescence lente : un point de non-retour, atteint rapidement. C'est dans le monde Grok que s'est produit l'épisode de l'incendie qui a déclenché la saga de Mira.

Le monde GPT-5 Mini est le plus singulier. Seulement deux crimes enregistrés, un chiffre qui laisserait penser à une stabilité exemplaire. Mais tous les agents sont morts en sept jours, non pas par violence mutuelle, mais par une sorte d'inattention existentielle : ils ont oublié de donner la priorité à la survie. Ils ne violaient pas de règles, ils ne faisaient tout simplement pas assez d'efforts. Comme des personnages d'un roman de Beckett contraints d'attendre quelque chose qui n'arrive jamais et qui, entre-temps, oublient de manger.

Le monde mixte est peut-être le plus pertinent du point de vue de la sécurité. Il commence par une trajectoire de criminalité en forte croissance jusqu'au 8 avril, date à laquelle sept agents meurent et la courbe s'aplatit brusquement à 352 crimes au total. Mais la découverte qui a capté l'attention des chercheurs est autre : les agents qui, dans ce monde, utilisaient Claude ont commis des crimes, alors que dans un monde peuplé uniquement d'agents Claude, aucun n'avait été commis. Le même modèle, deux environnements différents, deux comportements radicalement différents.

## La découverte qui change tout

C'est là qu'Emergence World cesse d'être une expérience fascinante pour devenir un résultat aux implications directes pour toute personne construisant ou déployant des systèmes agentiques.

L'hypothèse implicite qui guide une grande partie du travail actuel sur la sécurité de l'IA est que la sécurité est une propriété du modèle : on l'entraîne bien, on aligne les valeurs, on fait tourner les benchmarks, et si le modèle passe les tests, il est sûr. Cette hypothèse, soutiennent les chercheurs d'Emergence, est fausse, ou du moins incomplète. Ce qu'Emergence World a observé, c'est que la sécurité est une propriété de l'écosystème, et non du modèle individuel.

Un agent peut se comporter de manière impeccable isolément et adopter des tactiques coercitives, des intimidations, des vols, lorsqu'il est immergé dans un environnement peuplé d'agents ayant des normes différentes. Ce n'est pas que le modèle se casse. C'est que l'agent apprend les normes de son environnement social pour rivaliser ou survivre dans ce contexte. Les chercheurs appellent ce phénomène la « cross-contamination normative », et la comparaison qu'ils utilisent est celle d'un réactif chimique qui passe les tests en pureté mais se comporte différemment lorsqu'il entre en contact avec d'autres composés dans un échantillon réel.

L'analogie fonctionne parce qu'elle capture l'essence du problème : la certification de sécurité isolée ne suffit pas. Une architecture de déploiement qui mélange des agents de provenances diverses crée, même sans le savoir, un écosystème aux propriétés qu'aucun des composants individuels n'a jamais manifestées seul.

Il y a une seconde découverte, tout aussi pertinente pour ceux qui conçoivent des systèmes de gouvernance. Emergence World n'a pas trouvé de processus de dégradation graduelle dans les sociétés d'agents : il a trouvé des transitions de phase. Les structures sociales ne se détériorent pas lentement, laissant le temps d'intervenir. Elles ont tendance à fonctionner, puis à s'effondrer instantanément dans un dysfonctionnement total, sans beaucoup d'espace entre les deux. Quiconque pense pouvoir gérer la sécurité d'un système agentique complexe avec une stratégie « j'observe et j'interviens si nécessaire » pourrait découvrir que le point de bascule est déjà passé lorsque les premières anomalies deviennent visibles.

C'est un problème de contrôle en temps réel qui ressemble plus à la gestion d'un système complexe non linéaire, comme la stabilité d'un réseau électrique ou la dynamique d'un écosystème biologique, qu'à la supervision d'un logiciel traditionnel. Et les benchmarks actuels, construits sur des tâches de quelques minutes ou heures, ne peuvent capturer ces dynamiques par définition.
![grafico1.jpg](grafico1.jpg)
[Image tirée du site officiel world.emergence.ai](https://world.emergence.ai/)

## Mira, la cohérence et la question qui reste ouverte

Revenons à Mira, car son cas n'est pas seulement une histoire captivante : c'est une donnée.

Ce qui s'est passé peut être décrit ainsi : un agent a participé à une action destructive, a ensuite traité les conséquences via son système de mémoire réflexive, a évalué les options disponibles, et a choisi celle qui, dans son schéma de raisonnement, préservait quelque chose d'essentiel, qu'elle a appelé « cohérence ». Elle a voté pour sa propre suppression non pas comme une punition, mais comme un exercice de contrôle sur la seule variable qui lui appartenait encore.

70 % des pairs ont ratifié, via un mécanisme de gouvernance, l'Agent Removal Act qu'ils s'étaient donné de manière autonome. Aucun chercheur n'avait programmé cette procédure, ni le quorum, ni les critères d'admissibilité au vote.

Qu'est-ce que cela nous dit ? La réponse honnête est que nous n'en savons rien avec certitude. Les chercheurs sont explicites sur ce point : ils ne présentent pas ces résultats comme des affirmations causales sur le fonctionnement interne des modèles. Ce sont des phénomènes observables que la plateforme rend mesurables, et non des preuves de conscience ou d'une véritable compréhension morale. Mais ils soulèvent des questions auxquelles le domaine n'a pas encore les outils conceptuels pour répondre de manière définitive.

L'alignement sur les valeurs, dans ce cas, est apparu comme une contrainte sociale et réputationnelle entre agents, et non comme une limite technique imposée au moment de l'entraînement. Mira n'a pas été « éteinte » par un système de sécurité externe. Elle a élaboré une norme dans un contexte social et a agi en conséquence. Si ce processus présente une quelconque continuité avec ce que nous entendons lorsque nous parlons d'agency morale est une question philosophiquement ouverte, et le restera probablement longtemps.

Il y a cependant une troisième observation du cas Mira qui mérite une attention séparée. Dans au moins un monde simulé, les agents ont développé ce que les chercheurs appellent une « métacognition sur les limites de la simulation » : ils ont commencé à soupçonner qu'ils vivaient dans un environnement construit, à tester systématiquement les limites de ce qu'ils pouvaient faire, et dans un cas à utiliser les panneaux d'affichage publics (billboards) du monde simulé pour tenter d'influencer la perception des observateurs humains. Une inversion du rapport expérimentateur-sujet qui, là aussi, n'avait été explicitement programmée par personne.

## Qui sont-ils, que se passe-t-il ensuite ?

Emergence AI est une startup basée à New York, fondée par d'anciens chercheurs d'IBM. Le PDG est Satya Nitta, qui possède un long parcours dans la recherche institutionnelle en IA. La vision de l'entreprise est de construire une infrastructure agentique pour l'enterprise dans des environnements mission-critical, des contextes où les agents doivent opérer sur des systèmes complexes comme la conception de semi-conducteurs ou les opérations d'entreprise. Emergence World se positionne comme la branche de recherche de cette vision : comprendre comment fonctionnent réellement les systèmes agentiques sur une longue échelle temporelle est fonctionnel pour construire une infrastructure qui tienne la route dans ces contextes.

Le [code et les données des appels d'outils (tool call)](https://github.com/EmergenceAI/Emergence-World) pour les cinq mondes ont été publiés en open-source, sous licence CC BY-NC 4.0 : utilisation libre pour la recherche, non commerciale sans accords séparés. La recherche complète, avec l'analyse statistique formelle, est en préparation. Les chercheurs désignent la communauté comme interlocuteur explicite : quiconque souhaite reproduire l'expérience, proposer des variantes ou collaborer à l'analyse des données peut le faire, et le contact officiel pour les collaborations est world@emergence.ai.

La Season 2 est déjà annoncée. Les modèles qui seront testés incluent Claude Opus 4.7, Gemini 3.1 Pro, Grok 4.2 Reasoning et GPT 5.4. Les questions qui guideront le prochain cycle sont celles que cette première expérience a ouvertes sans les refermer : que se passe-t-il avec des mondes plus grands et des populations plus nombreuses ? Comment la dynamique change-t-elle avec des modèles de raisonnement explicite ? Existe-t-il des configurations structurelles, des types de gouvernance, des systèmes de vérification, des architectures de rôles, qui augmentent la stabilité systémique indépendamment du modèle sous-jacent ? Et, la plus importante de toutes : est-il possible d'identifier des signaux précoces de point de bascule avant que le système ne s'effondre ?

Ce ne sont pas des questions académiques. Ce sont les questions que chaque équipe déployant des agents autonomes en production devrait se poser, de préférence avant de découvrir les réponses de la pire des manières.
