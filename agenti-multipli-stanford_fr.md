---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-05-01
author: "Dario Ferrero"
---

# Plus d'agents, moins d'intelligence ? Stanford remet en question l'architecture multi-agents
![agenti-multipli-stanford.jpg](agenti-multipli-stanford.jpg)

*Il y a une scène culte dans "Primer", le film de science-fiction à petit budget de Shane Carruth, où deux ingénieurs construisent une machine à explorer le temps dans leur garage, convaincus que plus ils ajoutent de composants, mieux elle fonctionnera. Ils découvrent ensuite, de la manière la plus douloureuse qui soit, que la complexité n'est pas synonyme de puissance : c'est juste de la complexité. L'industrie de l'intelligence artificielle traverse actuellement une crise philosophique similaire, bien que nettement moins temporelle, concernant les systèmes multi-agents. Et un article, publié par deux chercheurs de Stanford en avril 2026, a le mérite de mettre le doigt exactement là où ça fait mal.*

Le titre de l'article : [*Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets*](https://arxiv.org/abs/2604.02460), est de ceux qui ne laissent aucune place à l'interprétation. Un agent unique, dans les bonnes conditions, bat un système multi-agents. Pas toujours, pas partout, pas pour des raisons triviales. Mais il le bat.

## Qu'est-ce qu'un agent, et pourquoi en faut-il soudainement de plus en plus ?

Avant de comprendre pourquoi l'article est pertinent, il convient de s'arrêter un instant sur ce que nous entendons par "agent" dans le contexte des grands modèles de langage. Un agent, dans ce contexte, est simplement une instance d'un modèle de langage à laquelle on confie une tâche : il reçoit un texte en entrée, une question, un problème, une instruction, "raisonne" dessus, et produit une réponse. C'est tout. Le modèle réfléchit, répond, fin de l'histoire.

Un système multi-agents est en revanche une pipeline dans laquelle plusieurs de ces agents travaillent ensemble, chacun ne voyant qu'une partie du problème ou une portion des informations disponibles, et communiquant par le biais de textes générés. En général, il y a un planificateur qui décompose le problème en sous-problèmes, un ensemble de travailleurs spécialisés qui traitent chacun leur partie, et un agrégateur qui synthétise les réponses partielles en une réponse finale.

L'idée intuitive est puissante : diviser pour mieux régner. Il semble presque évident que la distribution d'une tâche complexe entre des agents spécialisés doit produire de meilleurs résultats que ce qu'un seul esprit peut faire. C'est exactement la même logique qui nous amène à penser qu'un orchestre joue mieux qu'un soliste, qu'une équipe de chirurgiens opère mieux qu'un seul, qu'un collectif créatif produit plus qu'un individu isolé. Et dans de nombreux contextes, c'est vrai. Le problème est qu'avec les modèles de langage, la comparaison est presque toujours effectuée de manière incorrecte.

## L'astuce de l'addition cachée

Lorsqu'un système multi-agents semble battre un agent unique, il y a presque toujours une raison très simple derrière : il a utilisé plus de ressources informatiques. Ce n'est pas une meilleure architecture. C'est simplement qu'il a "réfléchi" davantage, au sens littéral du terme : il a généré plus de tokens de raisonnement intermédiaire.

Les modèles de langage modernes, en particulier ceux dits de "raisonnement" comme DeepSeek, Gemini ou Qwen, produisent un flux de pensée interne avant de répondre, ce qu'on appelle les *thinking tokens*, ou tokens de pensée. Ces tokens n'apparaissent pas dans la réponse finale, mais ils sont le moyen par lequel le modèle raisonne étape par étape avant de produire le résultat. Ils sont coûteux en termes de calcul, et le nombre de tokens qu'un modèle utilise en interne est directement proportionnel à la qualité des réponses sur des tâches complexes.

Or, le problème est que dans un système multi-agents, chaque agent dispose de son propre budget de tokens de raisonnement. Si vous avez cinq agents et que chacun réfléchit pendant mille tokens, le système a consommé cinq mille tokens de raisonnement au total. Si vous comparez ensuite ce système à un agent unique auquel vous n'en avez donné que mille, vous faites une comparaison inégale. C'est comme comparer un athlète qui s'entraîne cinq heures par jour à un autre qui s'entraîne une heure, puis s'étonner que le premier coure plus vite.

C'est exactement ce point que Dat Tran et Douwe Kiela de Stanford ont décidé d'aborder avec une rigueur méthodologique. Leur approche est simple : imposez un budget total de tokens de pensée égal pour tous les systèmes, puis mesurez qui s'en sort le mieux. Pas de tokens de prompt, pas de tokens de sortie, seulement des tokens de raisonnement intermédiaire. Et regardez ce qui se passe.

## Le terrain d'essai : questions en chaîne et réponses à étapes multiples

Les chercheurs ont choisi deux benchmarks spécifiques pour leurs expériences. Le premier est [FRAMES](https://arxiv.org/abs/2409.12941), un ensemble de données conçu pour tester la capacité à récupérer et synthétiser des informations provenant de sources multiples. Le second est [MuSiQue](https://arxiv.org/abs/2108.00573), filtré pour n'inclure que les questions à quatre sauts, c'est-à-dire celles qui nécessitent d'enchaîner quatre étapes de raisonnement distinctes pour arriver à la bonne réponse. Du type : "Dans quel pays se trouve la ville natale du réalisateur du film qui a remporté le prix X l'année où est né l'auteur du livre Y ?" Ce n'est pas un exemple réel, mais cela donne une idée de la complexité : chaque réponse est liée à la précédente, et se tromper sur un maillon signifie perdre toute la chaîne.

Les familles de modèles utilisées sont au nombre de trois : Qwen3-30B, DeepSeek-R1-Distill-Llama-70B, Gemini 2.5 Flash et Gemini 2.5 Pro. Les budgets de tokens de pensée testés vont de 100 à 10 000, à travers six niveaux. Et les architectures multi-agents comparées sont au nombre de cinq, toutes décrites en détail dans l'article : la Séquentielle (un planificateur qui divise le problème en étapes, des agents qui s'exécutent en série, un agrégateur final), la Parallèle pour Sous-tâches (même logique mais les travailleurs opèrent en parallèle), celle à Rôles Parallèles (un résolveur, un extracteur de faits, un sceptique et un second résolveur opérant en parallèle), le Débat (deux agents se confrontent puis se critiquent mutuellement) et enfin l'Ensemble (plusieurs agents répondent indépendamment et un juge choisit la meilleure réponse).

L'architecture la plus intéressante d'un point de vue théorique est la Séquentielle, car c'est la comparaison la plus pure avec l'agent unique : tous deux abordent le problème de manière sérielle, tous deux utilisent le même budget total, la seule différence étant que dans le système multi-agents, le raisonnement intermédiaire est externalisé dans des messages explicites entre agents, alors que dans l'agent unique, il reste latent au sein d'une chaîne de pensée continue.

## La mathématique qui nous dit pourquoi l'agent unique devrait gagner

Avant d'examiner les chiffres, les chercheurs construisent un argument théorique qui mérite d'être compris, car il a des implications qui vont bien au-delà de cet article spécifique.

L'argument repose sur l'"Inégalité de Traitement des Données", un résultat classique de la théorie de l'information. En termes très simples, elle dit ceci : quelle que soit la transformation que vous appliquez à une information, vous ne pouvez pas augmenter la quantité d'information qu'elle contient sur la réponse que vous cherchez. Vous ne pouvez que la conserver ou la perdre.

Dans le contexte des systèmes multi-agents, cela se traduit par une observation directe : les messages qu'un agent transmet à l'agent suivant sont une fonction du contexte original. Cette fonction ne peut pas créer d'information à partir de rien. Par conséquent, le contexte original, vu dans sa globalité par un agent unique, contient toujours au moins autant d'informations utiles que n'importe quel message qui en est extrait. Chaque fois qu'une information est "résumée" et transmise d'un agent à l'autre, quelque chose est inévitablement perdu. La communication est toujours un entonnoir.

Le corollaire pratique est immédiat : si un agent unique peut voir tout le contexte disponible et dispose du même budget informatique qu'un système multi-agents, il n'y a aucune raison théorique pour laquelle le système multi-agents ferait mieux. Il pourrait faire aussi bien. Pas mieux.

Mais il y a une exception, et c'est là que l'article devient vraiment intéressant.
![tabella1.jpg](tabella1.jpg)
[Image tirée de arxiv.org](https://arxiv.org/abs/2604.02460)

## Quand le contexte est dégradé : le seul cas où les multi-agents récupèrent

La garantie théorique de l'agent unique ne vaut que si celui-ci utilise le contexte de manière parfaite. Or, les modèles de langage modernes ne le font pas. Des phénomènes bien documentés dans la littérature, de la dilution de l'attention au phénomène dit "lost in the middle" (le fait que les modèles ont tendance à mieux se souvenir des informations situées au début et à la fin d'un long contexte plutôt qu'au milieu), montrent que la capacité à utiliser efficacement un contexte très long n'est pas acquise.

Les chercheurs formalisent cela sous le nom de "dégradation du contexte" et le modélisent expérimentalement à travers quatre modes : suppression de parties du texte pertinent, masquage d'informations clés, remplacement par un texte incorrect et insertion de distracteurs trompeurs. À mesure que le niveau de dégradation augmente, la garantie théorique de l'agent unique s'affaiblit, car celui-ci n'opère plus sur un contexte intact mais sur une version bruitée de celui-ci. Dans ce cas, un système multi-agents bien conçu peut compenser partiellement ce bruit grâce à la structuration du travail : différents agents voyant différentes parties, se vérifiant les uns les autres, filtrant le bruit à travers plusieurs étapes.

Le point crucial est "partiellement". Même dans des conditions de dégradation sévère, les systèmes multi-agents ne deviennent pas nettement dominants : ils deviennent *comparables* à l'agent unique. L'avantage de l'agent unique diminue, mais ne s'inverse pas de manière continue.

## Les chiffres, qui sont la partie dérangeante

Le Tableau 1 de l'article, qui couvre 192 combinaisons de modèle, de benchmark, de budget et d'architecture, est de ceux que l'on regarde avec une certaine lenteur. Non pas parce que les résultats sont ambigus, mais parce que la complexité est réelle et mérite le respect.

Le résultat principal est que, à budget de tokens de pensée égal, l'agent unique (SAS) est l'architecture la plus forte ou statistiquement indiscernable de la meilleure architecture dans pratiquement tous les cas au-dessus du budget minimum de 100 tokens. Avec 100 tokens, le modèle ne produit aucun raisonnement utile, que ce soit en tant qu'agent unique ou multi-agents, donc ce niveau ne dit rien d'intéressant.

En examinant les budgets intermédiaires et élevés, le schéma est stable. À 1 000 tokens de pensée, par exemple, la moyenne pour tous les modèles et datasets est de 0,418 pour SAS contre 0,379 pour la Séquentielle, 0,369 pour la Parallèle et 0,333 pour l'Ensemble. À 2 000 tokens, 0,421 pour SAS contre 0,389 pour la Séquentielle. À 5 000 tokens, 0,427 pour SAS contre 0,386 pour la Séquentielle. La distance a tendance à ne pas s'amplifier ni à disparaître avec l'augmentation du budget, mais reste cohérente.

Il existe des exceptions : avec Gemini 2.5 Pro à bas budgets, le système Séquentiel et le Débat ont des chiffres compétitifs, parfois légèrement supérieurs. Mais ces cas sont en partie expliqués par un artefact technique spécifique à Gemini qui mérite une mention à part.

## Le problème de Gemini et l'opacité de la comptabilité des tokens

L'une des sections de diagnostic les plus intéressantes de l'article concerne Gemini 2.5 et révèle quelque chose d'assez inconfortable sur la manière dont les API de ces modèles fonctionnent en pratique.

Lorsqu'on définit un budget de tokens de pensée pour Gemini via l'API, le nombre de tokens de pensée réellement "visibles", c'est-à-dire qui apparaissent dans le texte de réponse, a tendance à être beaucoup plus faible que le budget demandé dans le cas de l'agent unique. Les chercheurs montrent que Gemini semble "réfléchir en interne" de manière opaque, produisant moins de texte de raisonnement visible que ce que le budget permettrait, alors que dans un système multi-agents avec plusieurs appels API, la quantité totale de pensée visible est plus élevée, simplement parce qu'il y a plus d'appels qui extraient du texte de raisonnement.

Cela signifie que, pour Gemini, les comparaisons à budget nominal égal ne sont pas tout à fait fiables : l'agent unique pourrait en réalité utiliser *moins* de calcul effectif que demandé, tandis que le système multi-agents en utilise davantage via les appels multiples. C'est une irrégularité dans la manière dont Gemini gère les tokens de pensée en interne, et non un avantage architectural du multi-agents.

Pour compenser cela, les chercheurs ont développé la variante SAS-Lm "Longer Thinking", qui ajoute au prompt de l'agent unique une instruction structurée : avant de répondre, identifie les ambiguïtés, propose des interprétations, évalue-les, puis réponds. Cette petite modification pousse Gemini à produire plus de texte de raisonnement visible, rapprochant le calcul effectif du calcul nominal. Le résultat est que SAS-L s'améliore de manière significative sur Gemini 2.5 Flash et Pro, alors qu'il a des effets négligeables ou neutres sur Qwen3 et DeepSeek, où le problème de comptabilité opaque n'existe pas. Pour Gemini 2.5 Flash sur MuSiQue, SAS-L est l'architecture la plus forte dans toutes les tranches de budget. Une donnée significative.

## La fragilité des benchmarks : le test de la paraphrase

Une autre analyse de l'article mérite l'attention, car elle touche à une question méthodologique qui afflige toute la littérature sur les modèles de langage : à quel point les résultats dépendent-ils de la formulation exacte des questions ?

Les chercheurs ont mené une étude d'ablation par paraphrase : ils ont réécrit les questions des benchmarks avec des termes différents mais un sens équivalent, puis ont mesuré l'évolution des résultats. La réponse est : pas mal. L'exactitude des modèles change de manière non négligeable lorsque les questions sont paraphrasées, ce qui suggère qu'une partie des résultats dépend du fait que les modèles "reconnaissent" les questions des benchmarks, c'est-à-dire qu'ils ont vu des formulations similaires ou identiques pendant l'entraînement, et qu'ils y répondent en partie par mémoire plutôt que par pur raisonnement. Ce phénomène, connu sous le nom de *benchmark contamination* ou mémorisation, est un problème transversal à toute l'évaluation des modèles de langage, et l'article le signale honnêtement comme une limite.

La bonne nouvelle est que la contamination semble se répartir de manière relativement uniforme entre SAS et MAS : ce n'est pas que les systèmes multi-agents en bénéficient systématiquement plus que l'agent unique, ou inversement. Mais c'est un avertissement à ne pas prendre les chiffres absolus d'exactitude comme une vérité définitive.
![grafico1.jpg](grafico1.jpg)
[Image tirée de arxiv.org](https://arxiv.org/abs/2604.02460)

## La limite honnête : FRAMES et MuSiQue ne sont pas le monde réel

L'article est également rigoureux dans ses aveux. Les deux benchmarks choisis, FRAMES et MuSiQue, sont excellents pour isoler la capacité de raisonnement en chaîne sur des données structurées. Mais ils ne sont pas représentatifs de toutes les tâches pour lesquelles les systèmes multi-agents sont réellement utilisés. Ils sont relativement "propres" : les questions ont des réponses correctes bien définies, le contexte est fourni explicitement, il n'y a pas d'outils externes, pas d'incertitude sur les sources, pas d'ambiguïté du monde réel.

Un système multi-agents pour l'analyse de documents d'entreprise qui inclut de la recherche sur le web, de l'extraction de bases de données, de la vérification de sources et de la génération de rapports opère dans un environnement beaucoup plus chaotique que celui testé dans l'article. Les chercheurs reconnaissent explicitement cette limite dans la section dédiée et invitent à ne pas généraliser les résultats au-delà du domaine du raisonnement à sauts multiples sur contexte intact. C'est un avertissement à garder à l'esprit, et sur lequel nous reviendrons.

De même, la métrique d'évaluation utilisée, LLM-as-a-judge, c'est-à-dire l'utilisation d'un autre modèle de langage pour juger de l'exactitude des réponses, a ses propres limites. Le juge peut être influencé par le format des réponses, par la verbosité, par la "confiance" avec laquelle une architecture présente ses conclusions. Les systèmes multi-agents, qui agrègent les réponses de plusieurs agents, produisent souvent des réponses plus élaborées et structurées, qu'un juge pourrait évaluer positivement même lorsque le contenu factuel est similaire. Les chercheurs ont tenté de minimiser cet effet en utilisant une grille d'évaluation fixe, mais le risque d'un biais systématique du juge n'est pas totalement éliminable.

## Quand l'orchestration est une véritable architecture

Cela dit, nous en arrivons à la question qui compte vraiment pour ceux qui doivent décider comment construire des systèmes réels : quand est-ce qu'un système multi-agents a un sens véritable et quand s'agit-il au contraire de calcul masqué par de la complexité ?

La réponse de l'article, intégrée au contexte plus large, amène à distinguer deux scénarios très différents.

Le premier scénario où l'orchestration a un sens authentique est celui où la tâche nécessite des phases opérationnellement distinctes et non interchangeables : recherche dans des sources externes, récupération de données structurées, vérification factuelle, planification, exécution d'outils, contrôle qualité. Dans ces cas, la séparation en agents n'est pas un choix architectural pour améliorer le raisonnement, c'est une nécessité opérationnelle. L'agent qui cherche sur le web ne peut pas faire la même chose que l'agent qui génère du code exécutable. Il ne s'agit pas de diviser un problème de raisonnement, mais d'orchestrer des capacités différentes qui ne peuvent pas coexister dans un seul prompt.

Le second scénario où l'orchestration devient pertinente est exactement celui que l'article identifie théoriquement et vérifie expérimentalement : lorsque le contexte disponible pour l'agent unique est dégradé, fragmenté, bruité ou trop long pour être utilisé efficacement. Dans ces cas, la répartition du travail entre des agents qui voient chacun une portion plus petite et plus gérable du contexte peut compenser la perte de qualité du raisonnement que l'agent unique subit face à un contexte détérioré. Ce n'est pas une solution miracle, et l'article montre que même dans ces cas, l'avantage du multi-agents est souvent modeste, mais c'est une direction réelle et théoriquement fondée.

Il existe également un troisième scénario, non testé directement dans l'article mais cohérent avec son cadre théorique : les tâches où le nombre d'étapes nécessaires n'est pas déterminable à l'avance, et où l'orchestration sert à gérer une complexité opérationnelle qui change dynamiquement pendant l'exécution. Un système qui doit surveiller un processus en cours, s'adapter à des résultats intermédiaires imprévus et coordonner des actions sur plusieurs systèmes ne peut pas être réduit à un seul prompt avec un budget fixe. Ici, l'orchestration n'est pas un choix de performance mais une nécessité structurelle.

## Quand il s'agit seulement de calcul déguisé

Les situations où le caractère multi-agents ne sert à rien, ou peu, sont peut-être les plus importantes pour ceux qui doivent décider quoi construire et quoi ne pas construire.

Le schéma de pseudo-architecture le plus courant est le système qui fonctionne mieux que l'agent unique simplement parce qu'il utilise plus de calcul total, sans qu'il y ait d'avantage structurel réel. Si votre système multi-agents ne produit de meilleurs résultats que parce qu'il dispose de cinq fois plus de tokens de raisonnement répartis entre les agents, vous n'avez pas une architecture plus intelligente : vous avez un agent unique plus riche qui se cache derrière une interface plus complexe. Les données de l'article le montrent clairement : lorsque le budget total est contrôlé et égal, l'avantage diminue ou disparaît.

Une version spécifique de ce problème est l'Ensemble : plusieurs agents répondant indépendamment à la même question, puis un juge choisissant la meilleure réponse. L'intuition est celle de la "sagesse des foules", la loi des grands nombres appliquée à l'intelligence artificielle. Mais l'article montre que l'Ensemble est presque toujours la pire architecture parmi les multi-agents testés, avec des moyennes systématiquement inférieures à l'agent unique et souvent inférieures aux autres architectures multi-agents. La raison en est que l'échantillonnage de plusieurs réponses à partir du même modèle ne produit pas de véritable diversité si le modèle est déjà suffisamment performant : il produit de la variance, pas de la qualité. Vous achetez une marge statistique, pas un meilleur raisonnement.

Il en va de même pour l'architecture de Débat, deux agents qui se critiquent mutuellement, qui produit des résultats en moyenne similaires à la Séquentielle mais pas supérieurs à l'agent unique. L'idée que le débat entre agents conduit à un meilleur raisonnement est séduisante, mais elle ne fonctionne que lorsque les agents ont des informations ou des perspectives véritablement différentes. Si deux instances du même modèle s'attaquent au même problème avec le même contexte, la critique a tendance à être superficielle ou à converger rapidement vers la même réponse, sans que l'interaction n'apporte de réelle valeur ajoutée.

Le signal le plus facile à reconnaître pour savoir si l'on se trouve sur le terrain du "calcul masqué" est simple : supprimez les tokens supplémentaires et l'avantage disparaît. Si votre système multi-agents ne fonctionne bien que lorsque vous lui faites effectuer plus de tentatives, plus de discussions internes, plus d'itérations de vérification par rapport à un agent unique avec un budget équivalent, vous n'avez pas une meilleure architecture. Vous avez un agent unique avec un emballage décoratif autour.

## La question finale : qu'est-ce qui change, en pratique ?

Pour ceux qui construisent des systèmes réels, les implications pratiques de cet article sont concrètes et immédiates. La première est que les coûts d'un système multi-agents ne sont pas seulement monétaires. Il y a des coûts d'observabilité (un système avec cinq agents qui communiquent est beaucoup plus difficile à inspecter et à déboguer qu'un agent unique) et des coûts de maintenance, car chaque interface entre agents est un point de défaillance potentiel. Si les performances sont équivalentes, l'agent unique est presque toujours préférable pour la simplicité opérationnelle.

La deuxième implication est que le choix de l'architecture doit être guidé par la structure de la tâche, et non par les attentes ou le marketing. Une tâche de raisonnement complexe sur un contexte bien défini n'a pas besoin d'orchestration. Un workflow qui inclut la récupération à partir de sources externes, l'exécution de code et la vérification croisée en a probablement besoin.

La troisième, et peut-être la plus importante, est que chaque fois que l'on compare des architectures différentes, il faut regarder le calcul total consommé, et pas seulement le résultat. Un système multi-agents qui bat un agent unique en utilisant cinq fois plus de ressources n'est pas plus efficace : il est plus coûteux. La bonne question n'est pas "qui gagne ?", mais "qui gagne à ressources égales ?".

L'article de Stanford ne dit pas que les systèmes multi-agents sont inutiles. Il dit quelque chose de plus précis et de plus utile : ils ne sont pas universellement meilleurs, leur avantage présumé est souvent un artefact informatique et, pour les tâches où le raisonnement est le principal goulot d'étranglement, un agent unique avec un bon budget est difficile à battre. Comprendre quand cette règle s'applique et quand la complexité opérationnelle nécessite réellement une orchestration est la distinction qui sépare une architecture d'IA bien conçue d'une architecture qui est seulement, pour utiliser un mot qui a encore une aura de mythe dans le secteur, "agentique".
