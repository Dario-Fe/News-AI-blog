---
tags: ["Research", "Generative AI", "Applications"]
date: 2026-01-19
author: "Dario Ferrero"
---

# Jenseits der Kontextmauer: Rekursive Sprachmodelle fordern die unsichtbare Grenze der KI heraus
![rlm-ai.jpg](rlm-ai.jpg)

*Es gibt ein Problem in der modernen künstlichen Intelligenz, über das wenig gesprochen wird, das aber jeder Entwickler und intensive Chatbot-Nutzer mindestens einmal erlebt hat: das Gefühl, dass das Modell nach einem längeren Gespräch zunehmend dümmer wird. Das ist kein subjektiver Eindruck und auch kein Mangel an Klarheit Ihrerseits bei den Anfragen. Es ist ein präzises technisches Phänomen, das Forscher als *Kontextfäulnis* bezeichnen, und es stellt eine der frustrierendsten Einschränkungen der aktuellen Architektur großer Sprachmodelle dar.*

Stellen Sie sich vor, Sie müssten einen Roman schreiben und hätten nur einen Post-it-Zettel zur Verfügung. Jedes Mal, wenn Sie einen neuen Satz hinzufügen, müssen Sie einen alten löschen. Das ist mehr oder weniger das, was passiert, wenn ein Sprachmodell die Grenze seines Kontextfensters erreicht, jenes Kurzzeitgedächtnisfensters, in dem es Informationen "sehen" und verarbeiten kann. GPT-5, das Flaggschiffmodell von OpenAI, verfügt über 400.000 Token per API (etwa 300.000 Wörter), was viel erscheint, bis Sie versuchen, eine ganze Codebasis oder eine Sammlung von Rechtsdokumenten zu analysieren. Aber das eigentliche Problem ist nicht nur die Größe: Die Leistung der Modelle nimmt mit zunehmender Eingabelänge ab, selbst bei trivialen Aufgaben.

Hier setzt die Arbeit von Alex Zhang, Tim Kraska und Omar Khattab vom MIT CSAIL an, die im Dezember 2025 auf [arXiv](https://arxiv.org/html/2512.24601v1) veröffentlicht wurde. Ihr Papier schlägt rekursive Sprachmodelle vor, ein Framework, das den Ansatz des Problems komplett auf den Kopf stellt: Anstatt zu versuchen, den Speicher des Modells unendlich zu erweitern, lehren sie es, *über* den Speicher selbst nachzudenken und ihn als eine externe Umgebung zu behandeln, die programmatisch erkundet werden muss.

## Wenn Lesen zum Erinnern wird

Um die Intuition hinter den RLMs zu verstehen, sollte man beim Problem ansetzen. Die Transformer-Architektur, auf der moderne LLMs basieren, vergleicht jedes neue Token mit allen vorherigen Token im Kontextfenster und erzeugt n²-Beziehungen, die mit wachsendem Kontext immer aufwendiger werden. Es ist, als ob Ihr Gehirn jedes Mal, wenn Sie ein Wort aussprechen, alle Gespräche Ihres Lebens geistig durchgehen müsste. Unpraktikabel.

Die Forschung von Chroma [hat gezeigt](https://research.trychroma.com/context-rot), dass selbst die fortschrittlichsten Modelle unter einem Positionierungsbias leiden: Eine an erster Stelle platzierte Information erreicht eine Genauigkeit von 75 %, dieselbe Information an zehnter Stelle sinkt auf 55 %. Es geht nicht darum, wie viele Token man in das Fenster stecken kann, sondern darum, wie das Modell sie tatsächlich nutzen kann.

Zhang und Kollegen verfolgten einen anderen Weg. Anstatt das Modell zu zwingen, den gesamten Prompt in einem einzigen Durchgang aufzunehmen, behandeln RLMs den Prompt als Teil einer externen Umgebung, mit der das Modell symbolisch interagieren kann. In der Praxis wird der Kontext als Python-Variable in einer REPL-Umgebung (Read-Eval-Print Loop) geladen, und das Modell kann Code schreiben, um ihn zu inspizieren, zu zerlegen, nach Mustern zu suchen und, was entscheidend ist, sich selbst oder andere LLMs rekursiv auf bestimmte Teile des Inhalts aufzurufen.

Denken Sie an den Unterschied zwischen dem Lesen eines Buches von vorne bis hinten und dem Nachschlagen wie in einer Enzyklopädie: direkt zum Inhaltsverzeichnis springen, die relevanten Abschnitte identifizieren, vielleicht Notizen zu dem machen, was Sie finden. RLMs replizieren diesen zweiten, metakognitiven und strategischen Ansatz.

## REPL: der interne Dialog

Die technische Umsetzung ist in ihrer Einfachheit raffiniert. Wenn ein Benutzer einen Prompt an ein RLM sendet, wird dieser als String-Variable in einer Python-REPL-Umgebung gespeichert. Das Wurzelmodell (nennen wir es LM₀) erhält diesen String niemals direkt in seinem Kontextfenster. Stattdessen erhält es einen System-Prompt, der ihm erklärt, wie es mit der Variablen interagieren kann: Es kann bestimmte Slices davon lesen, es kann Hilfsfunktionen schreiben, um sie zu verarbeiten, es kann rekursive Sub-LM-Aufrufe (LM₁, LM₂...) auf ausgewählte Teile starten und es kann die Ergebnisse kombinieren.

Im Wesentlichen arbeitet das Modell in drei verschiedenen Modi. Zuerst erkundet es den Kontext durch programmatische Lese- und Suchoperationen, ähnlich wie bei der Verwendung von grep oder regex in einer Textdatei. Dann zerlegt es das Problem in überschaubarere Teilaufgaben und entscheidet autonom, welche Teile des Kontexts eine eingehende Analyse verdienen. Schließlich delegiert es diese Teilaufgaben an rekursive Instanzen von sich selbst oder anderen Modellen und fasst die Ergebnisse dann zu einer endgültigen Antwort zusammen.

[Das offizielle GitHub-Repository](https://github.com/alexzhang13/rlm) bietet eine Plug-and-Play-Implementierung, die einfach den Standardaufruf `llm.completion(prompt, model)` durch `rlm.completion(prompt, model)` ersetzt. Die externe Schnittstelle bleibt für den Benutzer identisch, aber unter der Haube findet dieser rekursive Tanz aus Erkundung und Berechnung statt.

Zhang selbst verwendet [in seinem Blog](https://alexzhang13.github.io/blog/2025/rlm/) eine aufschlussreiche Analogie: Es ist, als ob der Verlauf von Claude Code anschwillt oder Sie lange mit ChatGPT chatten und das Modell zunehmend dümmer zu werden scheint. Die intuitive Lösung wäre, den Kontext in zwei separate Aufrufe aufzuteilen und die Ergebnisse dann in einem dritten zu kombinieren: genau das, was RLMs systematisch und rekursiv tun.
![rlm-schema1.jpg](rlm-schema1.jpg)
[Bild von arxiv.org](https://arxiv.org/html/2512.24601v1)

## Benchmarks gegen Realität

Die Zahlen im Papier sind beeindruckend, müssen aber mit der gebotenen Vorsicht gelesen werden. Auf OOLONG, einem Benchmark zum Verständnis langer Kontexte, übertraf ein RLM auf Basis von GPT-5-mini GPT-5 base um mehr als das Doppelte an korrekten Antworten und verarbeitete Prompts mit 132.000 Token. Bei der S-NIAH-Aufgabe (einer komplexeren Variante der klassischen Nadel-im-Heuhaufen-Suche) verarbeiten RLMs Eingaben, die bis zu zwei Größenordnungen über den nativen Kontextfenstergrößen liegen.

Aber es gibt einen wichtigen Kompromiss: die Kosten. Das Papier berichtet von signifikanten Abweichungen von der Baseline, in einigen Fällen bis zu dreimal höher, je nachdem, wie viele rekursive Aufrufe das Modell durchführt. Es ist kein Zauberstab, der alles billiger macht: Es ist eine Architektur, die Rechenzeit gegen erweiterte Denkfähigkeiten eintauscht.

Auf dem BrowseComp-Plus-Datensatz, der für Such- und Syntheseaufgaben auf riesigen Dokumentenmengen entwickelt wurde, zeigten RLMs, dass sie über 10 Millionen Token effektiv verarbeiten können. Hier kommt jedoch eine weitere Überlegung ins Spiel: In einigen Fällen erwies sich die Antwortüberprüfung als überflüssig und erhöhte die Kosten pro Aufgabe erheblich. Das Modell konnte versuchen, seine korrekte Antwort mehr als fünfmal zu reproduzieren, bevor es sich am Ende für die falsche entschied.

Dies ist eine wichtige Erinnerung: RLMs sind nicht automatisch auf Effizienz optimiert. Die Zerlegungs- und Rekursionsstrategie wird vom Modell selbst entschieden, das bei der Beurteilung, wann weitere Unterabfragen sinnvoll sind, Fehler machen kann.

## Der Preis der Unendlichkeit

Prime Intellect, eine Organisation, die sich auf offene KI-Forschung konzentriert, [hat RLMs als zentrales Element](https://www.primeintellect.ai/blog/rlm) ihrer Strategie für Agenten mit langem Horizont übernommen. Sie glauben, dass das Lehren von Modellen, ihren eigenen Kontext von Anfang bis Ende durch Reinforcement Learning zu verwalten, der nächste Durchbruch sein wird, der es Agenten ermöglicht, Aufgaben zu lösen, die sich über Wochen oder Monate erstrecken.

Sie haben RLMEnv veröffentlicht, eine Trainingsumgebung, die speziell für das Training von Modellen mit integriertem RLM-Scaffolding entwickelt wurde. Die Idee ist faszinierend: Anstatt effizientere Aufmerksamkeitsarchitekturen zu lernen (was ein Problem der Sprachmodellierung ist), kann man lernen, wie man den Kontext durch das Ergebnis der gelösten Aufgaben verwaltet. Ein komplementärer Ansatz: Effiziente Aufmerksamkeit verzögert die Kontextfäulnis, Kontextfaltung (ein Begriff, den einige zur Beschreibung von Strategien wie RLMs verwenden) ermöglicht es dem Modell, sie aktiv zu verwalten.

Dies wirft jedoch ethische und Governance-Fragen auf. Ein Modell, das in der Lage ist, seinen eigenen Kontext über so lange Zeiträume autonom zu verwalten, könnte für sensible Aufgaben eingesetzt werden, bei denen die Nachvollziehbarkeit von Entscheidungen entscheidend wird. Denken Sie an Finanzentscheidungen, medizinische Diagnosen oder rechtliche Bewertungen: Die rekursive und programmatische Natur von RLMs macht die Interpretierbarkeit des Entscheidungsprozesses komplexer als bei einem einzelnen LLM-Aufruf.

Der EU AI Act klassifiziert KI-Systeme nach ihrem Risikoniveau, und Systeme, die in der Lage sind, Zustand und Argumentation über lange Zeiträume aufrechtzuerhalten, könnten in Hochrisikokategorien fallen, die strenge Audits erfordern. Dies ist natürlich kein Problem nur für RLMs, aber ihre Fähigkeit, autonom mit riesigen Datenmengen zu arbeiten, verstärkt die Notwendigkeit robuster Protokollierungs- und Erklärbarkeitsmechanismen.

## Alternativen auf dem Tisch

RLMs sind nicht die einzige Antwort auf das Problem des langen Kontexts. Es gibt mindestens drei Hauptansätze, die es wert sind, verglichen zu werden.

Der erste ist die direkte architektonische Modifikation: Modelle wie Llama 4 mit seinen Variationen von RoPE (Rotary Position Embeddings) oder Gemini 2.5 Pro mit Fensteraufmerksamkeit sind nativ für die Verarbeitung größerer Kontextfenster konzipiert. Sie funktionieren, aber selbst unter minimalen und kontrollierten Bedingungen nimmt die Leistung mit zunehmender Eingabelänge auf überraschende und uneinheitliche Weise ab.

Der zweite ist RAG (Retrieval-Augmented Generation), bei dem ein externes Abrufsystem dem Modell nur die relevanten Teile einer größeren Datenbank zur Verfügung stellt. Es ist effektiv für strukturierte Wissensdatenbanken, erfordert aber eine dedizierte Infrastruktur (Einbettungsmodelle, Vektordatenbanken, Chunking-Strategien) und schafft eine Abhängigkeit von externen Komponenten, die zum Engpass werden können.

Der dritte sind Frameworks wie MemGPT oder Multi-Agenten-Systeme wie das ebenfalls am MIT entwickelte DisCIPL. [Letzteres](https://news.mit.edu/2025/enabling-small-language-models-solve-complex-reasoning-tasks-1212) verwendet ein LLM als "Führer", das die Strategie plant und die Arbeit an kleinere Modelle verteilt. Es funktioniert gut für Aufgaben mit überprüfbaren Einschränkungen (wie Terminplanung oder Planung), weniger für offene Analysen, bei denen die Überprüfung der Korrektheit nuanciert ist.

RLMs positionieren sich in einem Zwischenraum: flexibler als RAG (keine Vorindizierung erforderlich), allgemeiner als Multi-Agenten-Systeme (keine aufgabenspezifische Orchestrierung erforderlich), aber potenziell teurer als native architektonische Ansätze, wenn diese gut funktionieren.
![rlm-schema2.jpg](rlm-schema2.jpg)
[Bild von arxiv.org](https://arxiv.org/html/2512.24601v1)

## Implementierungen von unten

Die Open-Source-Community hat schnell reagiert. [Eine TypeScript-Implementierung](https://www.reddit.com/r/opensource/comments/1q5f1sb/i_built_a_typescript_implementation_of_recursive/) erschien wenige Wochen nach der Veröffentlichung des Papiers auf Reddit, ein Zeichen dafür, dass die Idee bei Entwicklern Anklang findet, die mit konkreten Problemen konfrontiert sind. [Python-Implementierungen](https://github.com/ysz/recursive-llm) verbreiten sich, einige mit einem Fokus auf bestimmte Sandboxes (Docker, WebAssembly), um eine sichere Ausführung des vom Modell generierten Codes zu gewährleisten.

Es ist interessant festzustellen, wie verschiedene Community-Implementierungen mit alternativen Umgebungen zum Python-REPL experimentieren. Einige verwenden Clojure-REPLs, um die Unveränderlichkeit von Daten zu nutzen, andere erkunden SQL-Umgebungen für Abfragen auf strukturierten Datenbanken und wieder andere Bash für Systemadministrationsaufgaben.

Dies wirft eine allgemeinere Frage auf: Inwieweit beeinflusst die Wahl der Umgebung die Wirksamkeit von RLMs? Das MIT-Papier verwendet Python, weil es die den meisten LLMs vertrauteste Sprache ist (es ist in Trainingsdaten allgegenwärtig), aber nichts hindert daran, DSLs (Domain-Specific Languages) zu verwenden, die für bestimmte Anwendungsdomänen optimiert sind.

## Offene Fragen

Trotz der vielversprechenden Ergebnisse bleiben grundlegende Fragen offen. Die erste betrifft das Training. Zhang und Khattab sind besonders begeistert von der Möglichkeit, Modellen explizit beizubringen, wie RLMs zu denken, was eine weitere Skalierungsachse für die nächste Generation von Sprachsystemen darstellen könnte. Aber wie trainiert man ein Modell genau, um den Kontext optimal zu zerlegen? Man könnte Reinforcement-Learning-Techniken auf REPL-Trajektorien anwenden und Zerlegungen belohnen, die die Gesamtkosten minimieren und gleichzeitig eine hohe Genauigkeit beibehalten.

Modelle wie o1 von OpenAI beinhalten bereits während der Inferenz erweitertes Denken, tun dies aber auf undurchsichtige und nicht programmatische Weise. RLMs könnten von einem hybriden Ansatz profitieren: internes Denken zur Planung der Zerlegungsstrategie, programmatische Ausführung zur Umsetzung.

Die zweite Frage betrifft die Reproduzierbarkeit. RLM-Trajektorien sind nicht-deterministisch: derselbe Prompt kann in aufeinanderfolgenden Durchläufen unterschiedliche Zerlegungsstrategien erzeugen. Dies ist problematisch für Anwendungen, bei denen Konsistenz entscheidend ist (Compliance, Audit, reproduzierbare Forschung). Es werden Techniken benötigt, um den Explorationsraum des Modells einzuschränken oder um immer das gleiche Ergebnis der Operationen zu gewährleisten.

Die dritte betrifft die extreme Skalierbarkeit. Das Papier testet bis zu 10M+ Token, aber was passiert bei 100M? Bei 1B? Irgendwann wird auch die programmatische Verwaltung des Kontexts zu einem Problem der Rechenkomplexität. Möglicherweise ist ein "Meta-RLM" erforderlich, das andere RLMs in einer mehrstufigen Hierarchie verwaltet, ähnlich wie bei Betriebssystemen mit mehreren Cache-Ebenen.

Schließlich gibt es die Frage der offenen versus geschlossenen Modelle. Die Tests des Papiers verwenden hauptsächlich GPT-5, aber wie verhalten sich offene Modelle wie Qwen3 oder Llama 4? Die Fähigkeit, komplexe REPL-Anweisungen zu befolgen und korrekten Code zu schreiben, variiert erheblich zwischen den Modellen. Ein RLM ist nur so effektiv wie das Wurzelmodell, das es leitet.

Der Ansatz von Zhang und Kollegen löst das Problem der Kontextfäulnis nicht auf magische Weise, sondern verwandelt es von einer architektonischen Grenze in eine Herausforderung des Systemdesigns. Und vielleicht stellen rekursive Sprachmodelle, genau wie Betriebssysteme, die virtuellen Speicher einführten, um die Grenzen des physischen RAM zu überwinden, einen Paradigmenwechsel dar: nicht mehr Modelle, die Speicher *haben*, sondern Modelle, die Speicher *verwalten*.

Es ist zu früh, um zu sagen, ob sie zum De-facto-Standard werden, aber eines ist sicher: Die Debatte darüber, wie man KI dazu bringt, über beliebig lange Kontexte nachzudenken, hat gerade erst begonnen, und die nächsten Generationen von Modellen werden sich ernsthaft mit dieser Forschungsrichtung auseinandersetzen müssen.
