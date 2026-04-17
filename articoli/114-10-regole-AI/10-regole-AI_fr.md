---
tags: [" Generative AI", "Security", "Business"]
date: 2026-04-15
author: "Dario Ferrero"
---

# 10 règles pour utiliser l'IA en entreprise
![10-regole-AI.jpg](10-regole-AI.jpg)

*Partons d'une donnée qui sert de miroir. Selon le [rapport McKinsey State of AI de novembre 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai), 88 % des organisations utilisent déjà l'IA dans au moins une fonction métier. Pourtant, au cours de la même période, le Forum économique mondial et Accenture ont estimé que moins de 1 % d'entre elles ont pleinement opérationnalisé une approche d'IA responsable, tandis que 81 % en restent aux stades les plus embryonnaires de maturité en matière de gouvernance. Le paradoxe est là : presque tout le monde utilise l'IA, presque personne ne la gouverne vraiment.*

La confirmation la plus cinglante vient d'une [enquête d'EY de février 2026](https://www.ey.com/en_us/newsroom/2026/03/ey-survey-autonomous-ai-adoption-surges-at-tech-companies-as-oversight-falls-behind) menée auprès de 500 cadres technologiques : 45 % ont déclaré que leur organisation avait subi au cours des douze derniers mois une fuite de données sensibles, confirmée ou suspectée, causée par des employés utilisant des outils d'IA générative non autorisés (ChatGPT, Claude, Gemini), souvent avec des données d'entreprise sensibles collées dans un prompt, sans que le service informatique n'en sache rien. Le [PEX Report 2025/26](https://www.aidataanalytics.network/data-science-ai/news-trends/less-than-half-of-businesses-have-an-ai-governance-policy) complète le tableau : seulement 43 % des organisations disposent d'une politique formelle de gouvernance de l'IA, tandis que près d'un tiers, soit 29 %, n'en ont aucune.

Cet article ne se veut pas une leçon magistrale. Il ressemble davantage à cette conversation utile que l'on a avec un collègue avant un choix important : quelque chose qui aide à comprendre où l'on met les pieds, avec des exemples concrets et des références vérifiables. Dix règles, dix contrôles, dix erreurs à ne pas répéter.

## Avant tout : la sécurité de l'IA n'est pas la sécurité informatique avec un nouveau chapeau

Ceux qui travaillent dans l'informatique savent qu'il existe déjà un arsenal consolidé d'outils pour la protection des systèmes : pare-feu, gestion des identités, chiffrement, évaluation des vulnérabilités. Le problème est que l'IA introduit une surface de risque que ces outils ne voient pas.

Un modèle linguistique peut produire des réponses fausses avec la même assurance que s'il produisait des réponses correctes, un phénomène appelé hallucination dans le domaine et qui, dans des contextes professionnels, peut se traduire par de mauvaises décisions basées sur des informations inventées. Un système RAG (retrieval-augmented generation) qui accède aux documents internes peut être manipulé via une instruction cachée dans un fichier apparemment inoffensif : c'est ce que l'[OWASP LLM Top 10](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/) appelle l'*injection de prompt*, et qui a déjà été exploitée en 2025 dans des environnements réels. Les données que vous insérez dans le système peuvent être mémorisées, enregistrées ou envoyées à des infrastructures externes que vous ne contrôlez pas.

Le [NIST AI Risk Management Framework](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/), mis à jour et de plus en plus adopté comme référence mondiale, organise la réponse à ces risques en quatre fonctions : *Govern, Map, Measure, Manage* (Gouverner, Cartographier, Mesurer, Gérer). Ce ne sont pas des étapes séquentielles, mais des roues qui tournent en continu. Et c'est de là qu'il convient de partir.

## La gouvernance avant la technologie

Avant tout outil, il faut une réponse claire à trois questions : qui décide de ce que l'on peut faire avec l'IA dans l'entreprise ? Qui est responsable si quelque chose tourne mal ? À qui le problème est-il remonté ?

L'ISO/CEI 42001, la norme internationale pour les systèmes de gestion de l'IA publiée en décembre 2023 et déjà adoptée comme référence par [KPMG](https://kpmg.com/ch/en/insights/artificial-intelligence/iso-iec-42001.html) et d'autres grands acteurs du conseil, répond à ces questions avec un concept simple : il faut un *système de gestion de l'IA* avec des rôles nommés, des processus documentés et des cycles d'amélioration continue. Ce n'est pas de la bureaucratie gratuite : c'est le moyen de ne pas se retrouver à gérer un incident sans savoir qui a l'autorité pour éteindre le système.

L'ISO/CEI 42001:2023 reste la norme en vigueur et la référence certifiable pour les systèmes de gestion de l'IA. Il convient toutefois de noter qu'en avril 2025, l'ISO a publié l'[ISO/CEI 42005:2025](https://www.aarc-360.com/understanding-iso-iec-42005-2025/), une norme complémentaire dédiée spécifiquement aux évaluations d'impact des systèmes d'IA, un outil qui aide à mesurer les effets sociaux et individuels de l'IA tout au long de son cycle de vie, et pas seulement les risques techniques. Elle n'est pas obligatoire pour obtenir la certification 42001, mais dans la pratique, elle comble exactement le fossé entre « nous avons une gouvernance » et « nous savons ce que notre système produit concrètement sur les personnes ».

### Le problème invisible : le shadow AI

Avant même de parler de classification des risques, il y a un phénomène qu'il convient de nommer explicitement car il est le plus répandu et le moins encadré : le *shadow AI*. Il fonctionne exactement comme le shadow IT des années 2000, lorsque les employés ont commencé à utiliser Dropbox et leur compte Gmail personnel pour des fichiers de travail parce que les outils de l'entreprise étaient lents, sauf que les conséquences sont plus immédiates et moins réversibles.

Un employé du secteur financier qui colle un bilan non consolidé dans ChatGPT pour se faire aider à rédiger un commentaire, un recruteur qui télécharge les CV de candidats sur un outil externe pour faire une présélection, un avocat qui utilise un LLM grand public pour ébaucher une clause contractuelle : dans tous ces cas, les données sortent de l'infrastructure de l'entreprise, se retrouvent sur des serveurs tiers avec des politiques de conservation que l'entreprise n'a pas négociées, et contribuent potentiellement à l'entraînement de futurs modèles. Le chiffre d'EY cité en introduction, soit 45 % de fuites de données provenant d'outils non autorisés, n'est pas une exception : c'est la norme silencieuse.

La réponse n'est pas de tout interdire, car les interdictions non surveillées ne fonctionnent pas, comme l'enseigne l'histoire du shadow IT. La réponse est de construire des alternatives gouvernées qui soient suffisamment bonnes pour ne pas pousser les gens à chercher des solutions externes, accompagnées d'une politique claire sur ce qui est autorisé, avec quels outils et sous quelles conditions. C'est exactement le point de départ de la gouvernance de l'IA.
![grafico1.jpg](grafico1.jpg)
[Image tirée de blog.getpolicyguard.com](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/)

## Règle 1 — Classer les cas d'usage par niveau de risque, avant le déploiement

Tous les usages de l'IA ne se valent pas. Un chatbot interne pour répondre aux questions sur les congés est différent d'un système qui évalue les candidats RH ou qui attribue une note de crédit aux clients. Le [NIST AI RMF](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/) utilise la fonction *Map* exactement pour cela : créer un inventaire des systèmes d'IA utilisés et les classer par niveau d'impact potentiel.

L'[IA Act de l'UE](https://www.lw.com/en/insights/eu-ai-act-obligations-for-deployers-of-high-risk-ai-systems), avec une pleine applicabilité aux usages à haut risque d'ici août 2027, identifie comme systèmes à haut risque ceux utilisés pour la sélection et le suivi des employés, pour le crédit et pour le profilage des individus. Pour chacun de ces cas, les obligations augmentent de manière significative : évaluation d'impact, supervision humaine, enregistrement des journaux (logs), notification des incidents.

Un exemple concret : si votre entreprise utilise un LLM pour aider les recruteurs dans la présélection des CV, ce système est à haut risque selon l'IA Act de l'UE. Si le même modèle est utilisé uniquement pour générer des ébauches de descriptions de poste, le risque est beaucoup plus faible. La classification doit être faite au cas par cas, et non par catégorie générique d'outil.

## Règle 2 — Limiter les données qui entrent dans le système

Le principe est le même que pour un régime : tout ce que vous pouvez manger ne doit pas forcément être mangé. Dans le domaine de l'IA, cela s'appelle la *minimisation des données*, et c'est le premier rempart contre le risque de *fuite de données*.

Le guide publié par la [CISA, la NSA et le FBI en mai 2025](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) est explicite : les organisations doivent classer les données avant de les utiliser dans les systèmes d'IA, appliquer des contrôles d'accès rigoureux et ne jamais supposer que les jeux de données sont propres et exempts de contenus malveillants. Le même guide introduit le concept de *provenance des données* : savoir d'où proviennent les données avec lesquelles le modèle travaille n'est pas une formalité, c'est une exigence de sécurité.

En pratique : établissez par politique quelles catégories de données ne peuvent jamais entrer dans un système d'IA (secrets industriels, identifiants, données personnelles non strictement nécessaires, informations soumises à des contraintes réglementaires). Un exemple utile pour le secteur financier : les données de bilan non consolidées ne devraient jamais être utilisées comme contexte dans un chatbot d'entreprise générique accessible à toute l'organisation.

## Règle 3 — Gouverner les fournisseurs, les modèles et les intégrations

L'IA en entreprise est rarement un système monolithique que vous contrôlez entièrement. C'est généralement un assemblage : une plateforme SaaS, un modèle fondationnel tiers, des plugins, des outils externes connectés via API. Chacun de ces composants est un point d'entrée potentiel pour des risques que vous n'avez pas évalués directement.

Le [guide conjoint de la CISA de 2025](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) consacre une section entière aux risques de la *chaîne d'approvisionnement des données*, avec une attention particulière au *data poisoning* (empoisonnement des données) : la manipulation des données d'entraînement par des acteurs malveillants, qui peut se produire via des jeux de données collectés sur le web, des domaines expirés rachetés astucieusement, ou l'injection de faux exemples dans les corpus utilisés pour le fine-tuning (ajustement fin).

Le contrôle pratique est une évaluation structurée du fournisseur : pour chaque fournisseur de composants d'IA, vérifiez où sont enregistrés les journaux des interactions, si et comment vos données sont utilisées pour entraîner des modèles, quelles garanties contractuelles existent sur le traitement des données. L'ISO/CEI 42001 prévoit explicitement la *surveillance des fournisseurs tiers* comme une exigence du système de gestion.

## Règle 4 — Tester le système avant sa mise en service

Aucun système d'IA ne devrait être mis en production sans avoir subi un cycle de tests incluant des scénarios d'abus. L'IA Act de l'UE, pour les systèmes à haut risque, l'exige explicitement dans le cadre du *système de gestion de la qualité* : vérifications de la précision, de la robustesse, des biais et des comportements inattendus avant la mise en service.

Le *red teaming*, c'est-à-dire la simulation d'attaques et d'usages abusifs par une équipe interne ou externe, n'est pas une pratique réservée aux grandes entreprises technologiques. Des outils comme [Promptfoo](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/) permettent d'automatiser des tests basés sur l'OWASP LLM Top 10 même sans équipe de sécurité dédiée.

Un exemple concret pour le service client : avant de déployer un assistant conversationnel ayant accès aux données clients, vérifiez systématiquement s'il répond différemment à des utilisateurs ayant des noms de diverses origines culturelles (test de biais), s'il révèle des informations sur des utilisateurs autres que celui authentifié (test de fuite), s'il peut être amené à ignorer les instructions du système avec des prompts élaborés (test de jailbreak).

## Règle 5 — Se protéger des injections de prompt et des sorties dangereuses

C'est la règle la plus technique, mais elle mérite d'être comprise car elle est aussi la plus sous-estimée. L'*injection de prompt* fonctionne ainsi : un utilisateur, ou un contenu externe que le modèle lit, insère des instructions qui écrasent les instructions originales du système. Le modèle ne fait pas la distinction entre les instructions de son opérateur et celles injectées : il exécute les deux, et préfère souvent les plus récentes.

L'[OWASP LLM Top 10](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/), le document de référence pour la sécurité des modèles linguistiques, indique cela comme le risque numéro un. Les contre-mesures opérationnelles incluent : séparer architecturalement les instructions du système des entrées des utilisateurs, limiter les outils auxquels le modèle a accès (un assistant qui répond aux questions sur les produits n'a pas besoin de pouvoir envoyer des e-mails ou modifier des bases de données), appliquer des filtres sur les sorties pour intercepter les réponses contenant des données structurées sensibles.

L'ère agentique a déjà commencé et on est au-delà des chatbots et des copilotes ; les agents ne se contentent pas de répondre à une question mais exécutent des séquences d'actions, naviguent sur des sites, lisent et écrivent des fichiers, appellent des API, envoient des e-mails, avec une supervision humaine minimale ou nulle. Le [rapport Deloitte State of AI in the Enterprise de janvier 2026](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html) estime que seulement une entreprise sur cinq dispose aujourd'hui d'un modèle de gouvernance mature pour les agents IA autonomes, alors que leur utilisation est appelée à croître nettement au cours des deux prochaines années.

Dans ce contexte, le principe du moindre privilège cesse d'être une bonne pratique pour devenir une condition de survie : un agent avec un accès illimité aux outils, aux données et aux canaux de communication peut produire des dommages difficilement réversibles, rapidement et de manière automatique. Avant de déployer tout système agentique, la question à se poser est : si cet agent interprète mal l'instruction de la manière la plus raisonnablement erronée possible, que se passe-t-il ?
![grafico2.jpg](grafico2.jpg)
[Image tirée de mckinsey.com](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)

## Règle 6 — Maintenir un contrôle humain réel, pas seulement formel

Il existe une version vide de la *human oversight* (supervision humaine) : vous apposez une signature au bas d'un document attestant qu'un humain a supervisé la décision, alors qu'en réalité personne n'a vraiment rien contrôlé. L'IA Act de l'UE, dans les articles consacrés aux obligations des déployeurs de systèmes à haut risque, est précis sur ce point : la supervision humaine doit être substantielle, pas décorative. Les personnes chargées de la supervision doivent avoir la compétence nécessaire pour interpréter les sorties, la capacité d'interrompre le système et l'autorité pour le faire.

La distinction pratique à établir par écrit dans chaque processus critique est la suivante : l'IA suggère, l'humain décide. Pas « l'IA décide et l'humain peut s'y opposer », car le coût psychologique de l'opposition à un système automatique a déjà été documenté par la recherche : les gens ont tendance à accepter les suggestions des systèmes automatiques même lorsqu'ils ont des doutes, surtout sous la pression du temps. Dans les domaines des RH, de la finance, de la conformité et de la santé, cette dynamique n'est pas acceptable.

## Règle 7 — Surveiller le système après sa mise en service

Le lancement n'est pas l'arrivée : c'est le départ. Les systèmes d'IA se dégradent avec le temps pour des raisons qui ne sont pas toujours évidentes : le langage des utilisateurs change, les données d'entrée se décalent par rapport à la distribution originale (c'est ce que le [guide de la CISA](https://www.insidegovernmentcontracts.com/2025/06/cisa-releases-ai-data-security-guidance/) appelle le *data drift*), les schémas d'abus évoluent. Il faut un système de journalisation (logging) qui enregistre par échantillonnage les sorties, des alertes automatiques lorsque les mesures de qualité s'écartent de la référence (baseline), et un processus de réponse aux incidents qui réponde à la question : si le système fait une erreur ce soir, qui s'en aperçoit et en combien de temps ?

L'IA Act de l'UE exige la conservation des journaux pendant au moins six mois pour les systèmes à haut risque, et la notification aux autorités en cas d'incidents graves. L'ISO/CEI 42001 prévoit des révisions périodiques du système de gestion. Le NIST AI RMF, dans la fonction *Manage*, insiste sur une surveillance active qui alimente le cycle d'amélioration.

## Règle 8 — Tout documenter, vraiment

Si ce n'est pas documenté, ce n'est pas gouvernable. C'est une phrase qui semble évidente mais qui, dans l'activité quotidienne, est systématiquement ignorée. La documentation d'un système d'IA n'est pas le manuel d'utilisation : c'est l'ensemble des politiques approuvées, des évaluations des risques, des résultats des tests, des versions du modèle en production, des décisions prises et des justifications.

Cette documentation sert à trois choses concrètes : prouver la conformité réglementaire en cas d'audit, comprendre ce qui a changé quand quelque chose s'arrête de fonctionner, et améliorer le système au fil du temps en apprenant des erreurs. Le format n'est pas prescriptif, mais il doit être traçable et accessible à ceux qui en ont besoin. Un registre des versions du modèle en production, tenu sur un fichier Excel partagé et mis à jour manuellement, vaut déjà mieux que rien.

Pour ceux qui souhaitent structurer cette étape de manière rigoureuse, l'[ISO/CEI 42005:2025](https://www.aarc-360.com/understanding-iso-iec-42005-2025/) offre un cadre spécifique pour documenter l'impact des systèmes d'IA, y compris les usages sensibles, les abus prévisibles et les applications non intentionnelles, directement mis en correspondance avec les contrôles de l'ISO/CEI 42001.

## Règle 9 — Former les personnes qui utilisent le système

L'erreur humaine reste l'une des surfaces de risque les plus larges, et la formation est le rempart le plus économique contre elle. Mais il existe une donnée qui transforme ce principe de bon sens générique en levier stratégique mesurable : selon le [rapport de la CSA et de Google Cloud de décembre 2025](https://cloudsecurityalliance.org/blog/2025/12/18/ai-security-governance-your-maturity-multiplier), 65 % des organisations disposant d'une gouvernance complète de l'IA forment déjà leur personnel aux outils d'IA, contre seulement 27 % de celles ayant des politiques partielles et 14 % de celles encore en phase de développement. Ce n'est pas un détail : la formation est l'un des indicateurs les plus discriminants entre ceux qui gouvernent réellement l'IA et ceux qui se contentent d'écrire des politiques que personne ne lit.

La formation à l'IA n'est pas un cours obligatoire d'une heure sur lequel tout le monde clique sans regarder : elle doit être spécifique au rôle et doit aborder trois points distincts. Le premier est l'utilisation correcte des outils : comment utiliser le système, ce que l'on peut demander, ce que l'on ne doit jamais insérer. Le deuxième est la reconnaissance des limites : les employés doivent savoir que les modèles linguistiques peuvent se tromper avec une grande assurance, et ils doivent avoir l'autorité nécessaire pour ne pas faire confiance à la sortie lorsqu'ils ont des doutes fondés. Le troisième est la gestion des incidents : que faire quand quelque chose tourne mal, à qui le signaler, comment le documenter. L'IA Act de l'UE exige explicitement une *formation à la littératie en IA* (AI literacy training) pour tous les utilisateurs de systèmes à haut risque : ce n'est pas un détail réglementaire, c'est du bon sens opérationnel avec une échéance.

## Règle 10 — Mettre à jour les règles au fil du temps

L'IA est peut-être le seul domaine dans lequel les instructions opérationnelles vieillissent plus vite que les systèmes qu'elles régissent. Un cadre de gouvernance écrit au début de 2024 ne tient pas compte des capacités agentiques des modèles actuels, des nouveaux vecteurs d'attaque documentés en 2025, ou des échéances réglementaires de l'IA Act de l'UE qui approchent. Tant le [NIST AI RMF](https://blog.getpolicyguard.com/nist-ai-rmf-implementation-guide/) que l'[ISO/CEI 42001](https://kpmg.com/ch/en/insights/artificial-intelligence/iso-iec-42001.html) sont construits autour du principe de l'amélioration continue : les politiques doivent être revues au moins une fois par an, et tout incident significatif doit déclencher une révision immédiate des contrôles associés.

Le rythme minimum praticable est le suivant : révision annuelle du cadre global, révision semestrielle des politiques de données, révision immédiate après chaque incident ou changement majeur dans les modèles utilisés. Ce n'est pas un cycle lourd : c'est la différence entre une gouvernance vivante et un document que personne ne met à jour.

## Conclusion

En reprenant une métaphore de *Ghost in the Shell*, non pas le film d'Hollywood, mais le manga original de Masamune Shirow, le problème n'est jamais le système lui-même, mais celui qui l'a construit et avec quelle intention. L'IA en entreprise fonctionne lorsque celui qui l'a adoptée sait exactement ce qu'il veut obtenir, connaît les risques qu'elle comporte et a construit une structure capable de répondre lorsque les choses ne se passent pas comme prévu.

La question à se poser n'est pas « utilisons-nous l'IA ? ». Très certainement oui. La question est : « savons-nous avec quelles règles ? »
