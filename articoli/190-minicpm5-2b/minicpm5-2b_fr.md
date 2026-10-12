---
tags: ["Generative AI", "Training", "Applications"]
date: 2026-10-12
author: "Dario Ferrero"
---

# MiniCPM5-2B : ultrarapide, excellent en code, moins sur le reste
![minicpm5-2b.jpg](minicpm5-2b.jpg)

*Ces dernières semaines, le nom de MiniCPM5-2B a traversé les fils d'actualité, les bulletins d'information et les canaux Discord consacrés à l'IA locale avec une fréquence suspecte pour un modèle d'à peine 2,5 milliards de paramètres. Selon la fiche officielle disponible sur [Hugging Face](https://huggingface.co/openbmb/MiniCPM5-2B), le modèle affiche un score de 97,1 sur τ²-Bench Telecom, 69,1 sur LiveCodeBench v6 et 86,5 sur AIME—des chiffres qui, dans le comparatif publié par les auteurs eux-mêmes, dépassent ceux de modèles 4B comme Qwen3.5-4B. [Artificial Analysis](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b), qui a réexécuté une partie des tests de manière indépendante, confirme qu'il s'agit du score le plus élevé sur son Intelligence Index parmi tous les modèles open-weight sous la barre des 4 milliards de paramètres. La question qui mérite d'être posée, avant de répéter la formule « rivalise avec des modèles quatre fois plus grands », est simple : rivalise-t-il vraiment, et sur quoi ?*

## Le laboratoire, en bref

La configuration matérielle est identique à celle décrite lors de la première [analyse de Qwen 3.5](https://aitalk.it/it/qwen3.5-locale-puntata1) : processeur AMD Ryzen 7700, 32 Go de RAM DDR5, carte graphique AMD Radeon RX 9060 XT avec 16 Go de VRAM, et LM Studio comme framework d'exécution. Pour les détails concernant l'installation et la configuration globale, je vous renvoie à cet article.

Une remarque méthodologique essentielle : pour ce test, j'ai délibérément utilisé la version quantifiée Q8_0 de 2,7 Go plutôt que la version Q4_K_M de 1,56 Go, afin de déterminer si les éventuelles limites constatées provenaient de la quantification ou du modèle lui-même. La réponse, comme nous le verrons, est que ces limites sont structurelles : même à la qualité maximale disponible en local, le modèle peine sur le raisonnement abstrait, la planification multi-étapes et les consignes comportant des contraintes multiples. En revanche, la vitesse demeure exceptionnelle en toutes circonstances, confirmant que l'efficience de l'architecture ne relève pas du simple argument marketing.

## Qu'est-ce que MiniCPM5-2B ?

Derrière ce modèle se trouve OpenBMB, une communauté de recherche open source liée à l'Université Tsinghua et à ModelBest, dont la famille MiniCPM a dépassé les 50 millions de téléchargements cumulés selon Tencent News. Il ne s'agit pas d'un projet d'amateurs : le dépôt [OpenBMB/MiniCPM sur GitHub](https://github.com/openbmb/minicpm) rassemble plus de 11 000 étoiles, et l'écosystème pris en charge dès le premier jour—de vLLM à SGLang en passant par neuf architectures de puces différentes via FlagOS—témoigne d'une opération industrielle d'envergure.

L'architecture s'appuie sur une variante dense standard de `LlamaForCausalLM`, comptant 2,52 milliards de paramètres au total (1,98 milliard hors embeddings), 42 couches et une attention GQA dotée de 16 têtes de requête et 2 têtes clé-valeur. La fenêtre de contexte native annoncée s'élève à 131 072 jetons sous licence Apache 2.0, autorisant un usage commercial libre. Il s'agit d'un modèle exclusivement textuel (sans capacités de vision), avec un mode de réflexion (*thinking mode*) activable via un paramètre du modèle de chat et un appel d'outils (*tool calling*) natif au format XML.

Toutefois, la véritable valeur ajoutée ne réside pas uniquement dans les poids : OpenBMB a également publié la recette complète d'entraînement, les jeux de données UltraData, le framework d'apprentissage par renforcement et la chaîne de post-entraînement reposant sur l'On-Policy Distillation. Cette dernière fusionne les capacités de seize modèles experts (dont cinq spécialisés dans les tâches agentiques) au sein d'un point de contrôle final unique. C'est la même approche, à échelle réduite, qui a fait le succès d'autres projets open-weight chinois ces deux dernières années.

Il convient néanmoins de soulever d'emblée un détail révélateur sur l'emballement médiatique : lors de la [World Artificial Intelligence Conference de Shanghai](https://www.orcarouter.ai/blog/minicpm5-2b-open-weights-release) du 19 juillet 2026, ModelBest avait présenté le modèle avec une fenêtre de contexte annoncée de 512 000 jetons et une liste de partenaires matériels incluant AMD, Intel, MediaTek et Qualcomm. Or, les poids effectivement publiés en septembre configurent une fenêtre de 131 072 jetons. Ce n'est pas un détail négligeable lors de la conception d'un flux de travail sur des documents longs : il vaut mieux planifier sur la base des 128K (qui restent suffisants pour un ouvrage d'environ 250 pages) plutôt que sur les 512K annoncés lors de la conférence.

## Les promesses du concepteur

Le tableau comparatif publié par OpenBMB confronte MiniCPM5-2B à des modèles de même catégorie (LFM2.5-2.6B, Qwen3.5-2B, Gemma-4-E2B-it) ainsi qu'à des modèles 4B plus volumineux (Qwen3.5-4B, granite-4.2-3B, Nemotron-3-Nano-4B). Le modèle revendique une moyenne générale de 53,9 contre 51,1 pour le meilleur modèle 4B du tableau. Les points forts mis en avant concernent le code, le tool calling, les capacités agentiques et les mathématiques : sur SWE-bench Verified, le modèle affiche 46,4 contre 33,6 pour Qwen3.5-4B, et sur τ²-Bench Telecom, 97,1 contre 92,1.

Les faiblesses, admises par les auteurs eux-mêmes dans le tableau, sont tout aussi nettes : sur la culture générale (MMLU-Pro), le modèle plafonne à 70,8 contre 78,0 pour Qwen3.5-4B ; sur GPQA-Diamond, il descend à 70,2 contre 77,1 ; et sur des benchmarks de codage agentique plus complexes tels que SWE-bench Pro (14,4 contre 28,2) et Terminal-Bench v2.1 (8,6 contre 25,8), l'écart avec les modèles 4B s'élargit considérablement.

On observe également une évolution intéressante concernant le chiffre le plus abondamment cité : l'Intelligence Index d'Artificial Analysis. Lors de la présentation de juillet, OpenBMB communiquait un score de 17. Avec la révision méthodologique v4.2 de septembre—qui accorde un poids supérieur aux examens réservés et intègre de nouveaux composants agentiques—, le score officiel a été réévalué à 15, ce qui demeure le score le plus élevé parmi les modèles open-weight sous la barre des 4B, comme le rappelle [Artificial Analysis](https://artificialanalysis.ai/articles/openbmb-releases-minicpm5-2b). L'analyse effectuée par [eesel AI](https://www.eesel.ai/blog/minicpm5-2b-review) souligne par ailleurs un écart entre cette évaluation indépendante et une publication sur les réseaux sociaux d'OpenBMB mentionnant 23 points. Ces chiffres traduisent l'évolution des méthodologies de test, une nuance importante à garder à l'esprit avant d'accepter aveuglément les données promotionnelles.

Concernant la vitesse d'exécution annoncée, la documentation officielle ne fournit pas de chiffres homologués pour smartphones ou Apple Silicon : les estimations circulant en ligne (10 à 12 jetons par seconde sur smartphone, 70 à 90 sur Apple M4 Max) proviennent de conversions communautaires non officielles, à l'image d'un portage MLX mesurant environ 96 jetons par seconde en décodage sur un M4 Max doté de 128 Go de mémoire unifiée. Elles doivent donc être considérées comme de simples ordres de grandeur et non comme des mesures certifiées par le concepteur.
![grafico1.jpg](grafico1.jpg)
[Illustration issue du dépôt officiel GitHub](https://github.com/openbmb/minicpm)

## Les tests sur le terrain

Voici la partie centrale de cette analyse : l'évaluation pratique réalisée avec la version quantifiée Q8_0 de 2,7 Go, représentant la qualité maximale exploitable en local sans passer par le format BF16 complet.

**Raisonnement mathématique**, note 3/5, 105,66 jetons/s. Le problème classique des deux trains partant de Milan et Rome a été résolu correctement (croisement à 10h40), mais la démarche logique s'est avérée inutilement alambiquée : le modèle a calculé des temps de trajet globaux sans lien avec la solution avant de poser l'équation adéquate, tout en introduisant des caractères parasites issus de jetons mal gérés. Le résultat est exact, mais l'explication manque de clarté : utile pour un calcul rapide, moins pour appréhender une méthode.

**Génération de code**, note 4,5/5, 106,42 jetons/s. Soumis à une demande de fonction Python calculant la plus longue sous-séquence croissante en O(n log n), le modèle a produit un algorithme optimal s'appuyant sur un tableau `tails` et une recherche dichotomique, accompagné d'un code propre, de docstrings et d'un exemple fonctionnel. Une coquille mineure dans la rédaction n'altère pas un bilan très positif, en phase avec ses excellents résultats sur SWE-bench Verified.

**Tool calling**, note 4/5, 103,56 jetons/s. Dans le scénario simulant un assistant doté des fonctions `get_weather` et `send_email`, la structure des appels JSON s'est révélée exacte. Néanmoins, le modèle n'a pas géré la dépendance logique entre les deux appels : le corps du courriel contenait du texte statique au lieu de réutiliser les données météo obtenues à l'étape précédente. Adapté pour des automations simples, mais plus limité sur des orchestrations complexes à étapes liées.

**Raisonnement logique abstrait**, note 3,5/5, 106,21 jetons/s. Face à un problème de logique syllogistique comportant trois propositions contradictoires, le modèle a identifié la solution exacte. Toutefois, la démonstration manquait de structure, comportait des fautes d'orthographe et n'utilisait pas la notation en ensembles qui aurait apporté au raisonnement la rigueur attendue. Il saisit la logique sous-jacente mais peine à l'exposer clairement.
![immagine1.jpg](immagine1.jpg)
*Capture d'écran réalisée pendant les tests de MiniCPM5-2B sur LM Studio*

**Culture générale**, note 2/5, 103,74 jetons/s. Invité à rédiger une synthèse sur la Renaissance italienne et nordique en citant deux artistes par région, le modèle n'a mentionné qu'un seul artiste par côté et a attribué à Hans Holbein une spécialisation dans le paysage historiquement erronée—Holbein étant renommé pour ses portraits, tandis que le paysage s'est affirmé comme genre autonome au XVIIe siècle en Hollande. C'est le domaine où l'écart avec les modèles 4B s'exprime le plus nettement.

**Traitement de contextes longs**, note 4/5, 96,11 jetons/s. Sur un document technique en allemand portant sur la propagation de l'autorité dans les systèmes multi-agents, le modèle a généré une synthèse en cinq points exacte et bien structurée. Il a restitué des notions complexes comme le problème du « confused deputy » et ses conséquences pour les développeurs, démontrant une capacité remarquable de synthèse multilingue sur des textes longs.

**Planification multi-étapes**, note 3/5, 105,63 jetons/s. Dans un test mettant à disposition trois outils (`read_file`, `write_file`, `run_command`) pour modifier une clé d'API dans un fichier de configuration, le modèle a contourné les outils prescrits. Il a exécuté la commande `sed` au sein de `run_command` au lieu de passer par `write_file`, générant une séquence redondante sans exploiter les données de l'étape `read_file` initiale. Ce test confirme que la qualification « agentique » doit être évaluée avec précaution lors de flux de travail complexes.

**Respect de consignes à contraintes multiples**, note 2,5/5, 106,42 jetons/s. Lors de la rédaction d'un courriel d'excuses soumis à cinq contraintes simultanées (longueur, date, pourcentage de remise, ton et mots interdits), le modèle a respecté quatre contraintes sur cinq. Cependant, il a laissé passer des fautes de grammaire, une phrase de conclusion confuse et a omis les formules de politesse usuelles.

## Tableau récapitulatif
![tabella1.jpg](tabella1.jpg)

Moyenne globale : 3,3/5. Vitesse moyenne de génération : environ 104,2 jetons par seconde—un débit d'inférence inégalé par les modèles de cette taille évalués sur cette configuration.

## Domaines de pertinence et limites

MiniCPM5-2B se montre convaincant sur des tâches de développement de complexité moyenne, où il produit un code propre et fonctionnel proche de celui de modèles quatre fois plus volumineux. Il gère avec efficacité le tool calling simple et s'avère étonnamment compétent pour résumer des documents techniques dans différentes langues. Avec une empreinte mémoire de 2,7 Go en Q8 ou 1,56 Go en Q4, il s'exécute sur des configurations très accessibles (du Raspberry Pi au smartphone milieu de gamme), en conservant des débits proches de 105 jetons par seconde sur une carte graphique grand public.

En revanche, il ne doit pas être utilisé pour des recherches d'informations encyclopédiques, où les risques d'erreurs factuelles sont avérés. Il rencontre des difficultés sur le raisonnement abstrait complexe—parvenant parfois au résultat via des explications confuses—et ne parvient pas à orchestrer de manière autonome des outils dans des séquences multi-étapes présentant de réelles dépendances. Le respect de consignes comportant des contraintes multiples constitue également une limite marquée.

## Bilan : mesurer la portée réelle

Ce qui est avéré : au regard de son volume de paramètres, MiniCPM5-2B constitue une réussite technique notable. Sa vitesse d'exécution est réelle, ses performances en génération de code sont élevées, le tool calling basique fonctionne correctement, et la démarche d'OpenBMB consistant à publier les jeux de données et la méthode d'entraînement bénéficie à l'ensemble de la communauté open source. Ce qui relève de la surévaluation : l'affirmation selon laquelle il « rivalise avec des modèles quatre fois plus grands » n'est exacte que sur un ensemble restreint de benchmarks (essentiellement le code et les tâches agentiques simples), mais s'avère inexacte en culture générale et en raisonnement abstrait. Ce qu'il n'est pas : il ne s'agit pas d'un modèle généraliste ni d'un assistant polyvalent.

On peut penser à une scène de *Chungking Express*, le film de Wong Kar-wai où les événements s'enchaînent à un rythme rapide mais où les détails restent parfois flous : MiniCPM5-2B adopte cette même dynamique, rapide et incisive ; mais lorsqu'on lui demande de poser son raisonnement sur une question complexe, la précision s'estompe. Ou pour employer une image plus concrète : il s'apparente à une petite voiture de sport agile, idéale pour les trajets urbains, mais inadaptée pour entreprendre un long voyage chargé de bagages.

L'évaluation menée en Q8_0, à la qualité maximale exploitable sans passer au format BF16 complet, confirme ces observations : les limites constatées sont liées à la taille même de son architecture (2,5B) et ne résultent pas de la quantification des poids.

## Cas d'usage recommandés

Les utilisateurs cibles sont les développeurs et les équipes à la recherche d'un moteur d'exécution rapide pour la complétion de code, la vérification syntaxique ou des automations simples sur du matériel limité—éventuellement couplé à un modèle plus volumineux pour les tâches nécessitant une analyse approfondie. Il est en revanche déconseillé aux utilisateurs recherchant un assistant généraliste, des connaissances factuelles garanties ou l'orchestration autonome d'outils complexes. Pour ces derniers usages, les modèles des gammes 4B ou 7B demeurent le choix le plus adapté.

En conclusion, la règle habituelle prévaut : exploitez-le pour ce qu'il est—un outil rapide et spécialisé pour des tâches locales ciblées—plutôt que pour l'image simplifiée véhiculée par les annonces promotionnelles.
