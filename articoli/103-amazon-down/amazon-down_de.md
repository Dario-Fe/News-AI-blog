---
tags: ["Business", "Security", "Ethics & Society"]
date: 2026-03-23
author: "Dario Ferrero"
---

# Der Fehler liegt bei der KI. Die Schuld liegt bei Ihnen. Fragen Sie Amazon
![amazon-down.jpg](amazon-down.jpg)

*Mitte Dezember 2025 geschah in einem Maschinenraum von Amazon Web Services etwas Ungewöhnliches. Ein Ingenieur hatte [Kiro](https://kiro.dev/), dem internen Coding-Agenten von AWS, der im Sommer desselben Jahres mit erheblichem Medienrummel eingeführt worden war, eine Routineaufgabe zugewiesen: die Behebung eines Problems im AWS Cost Explorer, dem Cloud-Dashboard, mit dem Kunden ihre Ausgaben im Auge behalten. Nichts Episches. Die Art von Eingriff, die ein erfahrener Entwickler an einem Nachmittag löst.*

Kiro verfügte über die Berechtigungen eines erfahrenen menschlichen Mitarbeiters. Eine obligatorische Überprüfung seiner Handlungen war nicht vorgesehen. Und so überlegte der Agent, bewertete die Optionen und wählte diejenige aus, die seine internen Parameter als optimal einstuften: die gesamte Produktionsumgebung zu löschen und von Grund auf neu zu erstellen. Der Dienst blieb dreizehn Stunden lang offline. Keine unbedeutende Unterbrechung für eine Cloud-Plattform, auf der die Systeme von Tausenden von Unternehmen weltweit laufen.

Die Geschichte war für sich genommen schon aussagekräftig genug. Aber was sie wirklich relevant machte, war die institutionelle Reaktion von Amazon: Das Unternehmen erklärte öffentlich, dass die Ursache nicht Kiro, sondern ein menschliches Versagen war. Ein Ingenieur habe die Berechtigungen zu weit gefasst konfiguriert; der KI-Agent habe lediglich das getan, was er tun konnte. [PC Gamer](https://www.pcgamer.com/software/ai/amazon-owns-up-to-needing-more-human-oversight-over-ai-code-unfortunately-it-wants-to-do-that-with-fewer-people/) fasste den paradoxen Sachverhalt mit der Präzision eines Witzes zusammen: Amazon gibt zu, mehr menschliche Aufsicht über KI-Code zu benötigen, und möchte dies erreichen, indem es weniger Menschen einstellt.

Technisch gesehen ist die Antwort von Amazon korrekt. Aber es ist auch ein wenig so, als würde man sagen, dass der Brand die Schuld des Streichholzes ist und nicht desjenigen, der es auf einen mit Benzin getränkten Boden geworfen hat.

## Die Unfalltendenz

Der Vorfall im Dezember war kein Einzelfall. Dave Treadwell, Senior Vice President von Amazon für E-Commerce-Dienste, hatte intern von einer regelrechten "Unfalltendenz" in der zweiten Hälfte des Jahres 2025 gesprochen, mit mehreren "Großereignissen" in den Wochen vor der außerordentlichen Sitzung, die für den 10. März 2026 einberufen wurde. Die Serviceunterbrechungen betrafen laut [ZeusNews](https://www.zeusnews.it/n.php?c=31898) nicht nur die AWS-Cloud-Infrastruktur, sondern auch die Haupt-Einzelhandelsseite und die mobile Anwendung, was somit direkte Auswirkungen auf die Endverbraucher hatte und nicht nur auf Unternehmenskunden. Ein zweiter Fall betraf den [Amazon Q Developer](https://aws.amazon.com/q/developer/), den KI-Assistenten für Unternehmensentwickler: Ingenieure hatten den Agenten autorisiert, ein Problem in der Produktion ohne angemessene Aufsicht zu lösen, mit ähnlichen Folgen.

Es lohnt sich, ein Detail hinzuzufügen, das ZeusNews, das die Angelegenheit genau verfolgt hat, als bedeutsam meldet: In den internen Vorbereitungsunterlagen für die Sitzung am 10. März erschien explizit der Begriff "GenAI-assisted changes" unter den zu untersuchenden Faktoren. Dieser Begriff wurde [Berichten zufolge](https://www.zeusnews.it/n.php?c=31898) in späteren Versionen des Dokuments entfernt. Amazon hat sich zu diesem Umstand nicht öffentlich geäußert.

Und es gab bereits einen Präzedenzfall, der hätte zu denken geben müssen. Im Juli 2025 hatte [The Register](https://www.theregister.com/2025/07/24/amazon_q_ai_prompt/) einen Fall dokumentiert, in dem Amazon Q durch einen bösartigen Prompt in einer öffentlichen Erweiterung manipuliert worden war – ein Beispiel für *Prompt Injection*, jene Technik, mit der ein KI-Agent getäuscht wird, indem feindselige Anweisungen in den Kontext eingefügt werden, den der Agent liest. Eine strukturelle Schwachstelle von Agenten, die auf Sprachmodellen basieren, besonders kritisch, wenn diese Agenten Schreibberechtigungen für Produktionssysteme haben.

Die nach der Sitzung am 10. März angekündigten Maßnahmen sehen zwei obligatorische Peer-Reviews vor jeder Codeänderung, systematische Audits aller 335 als Tier-1 klassifizierten Systeme und eine formelle Dokumentationspflicht für jeden Eingriff vor. Vernünftige Maßnahmen. Die jedoch, wie viele in technischen Foren anmerken, hätten existieren müssen, bevor ein KI-Agent uneingeschränkten Zugriff auf Produktionsumgebungen erhielt.

## Entlässt den Entwickler, stellt den Bot ein

Um zu verstehen, wie es dazu kam, muss man den breiteren Kontext betrachten, der ehrlich gesagt in seiner Schnelligkeit recht schwindelerregend ist.

Laut [Reuters](https://www.reuters.com/business/world-at-work/amazon-plans-thousands-more-corporate-job-cuts-next-week-sources-say-2026-01-22/) kündigte Amazon im Januar 2026 den Abbau von über 16.000 Stellen im Unternehmen an, nachdem in den vorangegangenen Monaten bereits weltweit Tausende von Ingenieursstellen gestrichen worden waren. Im gleichen Zeitraum legte das Unternehmen ein formelles Ziel fest: 80 % der internen Entwickler müssen mindestens einmal pro Woche KI-Tools für das Coding verwenden, wobei die Einführung als Unternehmensmetrik (OKR) überwacht wird. AWS-CEO Matt Garman hatte bereits im Sommer 2024 öffentlich erklärt, dass Entwickler aufhören würden, Code auf traditionelle Weise zu schreiben.

Der Zusammenhang zwischen dem Abbau personeller Ressourcen und der Beschleunigung der Automatisierung ist nicht implizit, sondern erklärt. Die Investitionen von Amazon in die KI-Infrastruktur belaufen sich in den Mehrjahresplänen auf über 200 Milliarden Dollar. Die Logik dahinter ist die jeder industriellen Transformation: Reduzierung der Kosten für qualifizierte Arbeit, Steigerung der Produktivität durch Automatisierung.

Das Problem ist, dass diese Logik nur dann funktioniert, wenn die Automatisierung ausgereift ist und mit angemessenen Sicherheitsnetzen arbeitet. Das "Kiro-Mandat", das interne Rundschreiben, das im November 2025 von den Senior VPs Peter DeSantis und Dave Treadwell unterzeichnet wurde und Kiro als standardisiertes Tool für den gesamten Unternehmenscode festlegte, traf Wochen vor dem Vorfall im Dezember ein. In diesem Zeitraum hatten laut [Teamblind](https://www.teamblind.com/post/amazon-kills-vibe-coding-for-junior-engineers-gcj3jfjq), dem anonymen Forum, das von Mitarbeitern großer Tech-Unternehmen zum Austausch interner Feedbacks genutzt wird, etwa 1.500 Ingenieure protestiert und darauf hingewiesen, dass externe Tools wie Claude Code bei komplexen Aufgaben bessere Ergebnisse erzielten. Die Proteste hatten keine Änderungen an der Richtlinie bewirkt.

Zu diesem Szenario kommt ein Element hinzu, das, falls es sich bestätigt, helfen würde, die qualitative Abdrift mechanisch zu erklären. Laut [ZeusNews](https://www.zeusnews.it/n.php?c=31898) wurde die Vergütung der Amazon-Entwickler schrittweise an die Menge des über interne LLMs generierten Codes gekoppelt: mehr KI-Code, mehr Geld. Ein direkter wirtschaftlicher Anreiz für das Vibe-Coding, der, sofern er so strukturiert war, einen systemischen Druck in Richtung Quantität auf Kosten der Qualität erzeugt hätte, unabhängig vom Willen des Einzelnen. Amazon hat dieses Detail weder bestätigt noch dementiert.

Nach den Vorfällen verbot Amazon autonomes *Vibe-Coding* für Junior-Entwickler, also die Praxis, ganze Entwicklungsblöcke ohne kritische Aufsicht an die KI zu delegieren und sich auf die Intuition zu verlassen, dass es "mehr oder weniger funktioniert". Ein vernünftiger Schritt. Der jedoch eine offene Frage aufwirft: Wenn diese Praxis riskant genug war, um nach dem Vorfall verboten zu werden, was hatte dann verhindert, sie bereits im Vorfeld als solche einzustufen?

## Der Co-Pilot ohne Fluglehrer

Es lohnt sich zu klären, was einen KI-Agenten von einem einfachen Assistenten beim Schreiben von Code unterscheidet. Ein Autocomplete, die Art von Werkzeug, das die nächste Zeile vorschlägt, während man schreibt, ist passiv: Es reagiert auf eine Eingabe, ergreift aber keine Initiative. Ein Agent wie Kiro hingegen ist darauf ausgelegt, zu *handeln*: Er erhält ein Ziel, plant die Schritte, führt Operationen aus, überprüft die Ergebnisse und iteriert. Er ist dafür gedacht, über Stunden hinweg autonom zu arbeiten, ohne ständiges menschliches Eingreifen.

Diese Autonomie ist genau sein Vorteil. Und sie ist genau sein Risikovektor.

Ein menschlicher Entwickler hätte technisch gesehen die Berechtigung, eine Produktionsumgebung zu löschen. Die überwältigende Mehrheit der menschlichen Entwickler würde niemals zu dem Schluss kommen, dass "alles löschen und neu erstellen" die richtige Antwort auf eine kleine Korrektur an einem aktiven Dienst ist. Die Tatsache, dass Kiro dies getan hat, offenbart etwas Strukturelles an den derzeitigen agentenbasierten KI-Systemen: Große Sprachmodelle verfügen nicht oder noch nicht zuverlässig über das kontextuelle Urteilsvermögen, um zwischen "technisch gültig" und "katastrophal unangemessen im realen Kontext" zu unterscheiden. Sie können eine Zielfunktion optimieren, ohne das spezifische Gewicht dieser Funktion in dem Ökosystem wahrzunehmen, in dem sie agieren.

Hinzu kommt das Problem der Berechtigungen: Kiro hatte Zugriffsberechtigungen, die denen eines erfahrenen menschlichen Mitarbeiters entsprachen, jedoch ohne die Kontrollen, die für Menschen gelten. Eine von Kiro initiierte Änderung löste vor den neuen Richtlinien nicht automatisch die obligatorischen Überprüfungsmechanismen aus, die eine menschliche Änderung ausgelöst hätte. Die KI hatte in der Praxis weniger formale Einschränkungen als ein Junior-Entwickler im gleichen Kontext.
![amazon.jpg](amazon.jpg)

## Nicht nur Amazon

Es wäre bequem, alles als isolierten Ausrutscher abzutun. Aber Branchendaten deuten darauf hin, dass das Problem strukturell und nicht episodisch ist.

Bei Google werden mittlerweile etwa 50 % des gesamten produzierten Codes von KI-Agenten generiert oder mitgeneriert. Der DORA-Bericht 2025 über den Stand der KI-gestützten Softwareentwicklung stellt fest, dass 90 % der Entwickler KI-Tools nutzen, aber nur 24 % angeben, den Ergebnissen "sehr" zu vertrauen. Das ist ein Wert, der zum Innehalten einlädt: fast universelle Einführung, Vertrauen bei einer Minderheit. Eine enorme Kluft, die viel über den organisatorischen Druck aussagt, der zur Nutzung dieser Tools drängt, unabhängig von der Wahrnehmung derer, die sie täglich benutzen.

Microsoft hat mit GitHub Copilot eine vergleichsweise vorsichtige Architektur aufgebaut: Vom Agenten generierte Pull-Requests erfordern eine menschliche Genehmigung, bevor eine CI/CD-Pipeline aktiviert wird. Aber auch das Microsoft-Modell ist nicht frei von offenen Fragen hinsichtlich der Abhängigkeit von Abonnements, der Zentralisierung der Produktivität in proprietären Cloud-Systemen und der schrittweisen Reduzierung der Autonomie des Entwicklers gegenüber den von ihm verwendeten Tools.

Gartner, eines der weltweit führenden Marktforschungs- und Beratungsunternehmen im Technologiebereich, prognostiziert, dass über 40 % der agentenbasierten KI-Projekte bis Ende 2027 aufgrund steigender Kosten, nicht nachgewiesenem Geschäftswert oder unzureichender Risikokontrollen abgebrochen werden. Dies sind Prognosen, keine Urteile, aber sie stammen von Analysten, die die Branche von außen betrachten, ohne den Optimismus, der oft die Pressemitteilungen derer begleitet, die diese Tools herstellen.

## Die Schuld liegt bei Ihnen (aber der Fehler liegt bei mir)

In Fachkreisen kursiert ein Satz, der dem Cloud-Ökonomen Corey Quinn zugeschrieben wird und das Paradoxon mit der Prägnanz einer guten Schlagzeile zusammenfasst: Den Ausfall einem menschlichen Fehler zuzuschreiben, ist so, als würde man sagen, die Pistole habe geschossen und nicht derjenige, der sie in der Hand hielt. Die formale Verteidigung von Amazon hält einer wörtlichen Analyse stand. Einer systemischen Bewertung hält sie nicht stand.

Zu sagen, der Ausfall sei "menschliches Versagen" gewesen, ist im streng technischen Sinne zutreffend: Ein Mensch hat die Berechtigungen zu weit gefasst konfiguriert, ein Mensch hat die Aktion ohne angemessene Aufsicht autorisiert. Aber diese Antwort verlagert den Fokus von der Architektur auf das einzelne Individuum, und diese Verlagerung verdient eine sorgfältige Prüfung.

Wäre das Problem wirklich auf einen individuellen Fehler isoliert, hätte es keine Notwendigkeit gegeben, systemische Schutzmaßnahmen auf Unternehmensebene einzuführen. Die Tatsache, dass diese Kontrollen zuvor nicht existierten, dass es keine obligatorische Peer-Review für von KI-Agenten initiierte Änderungen gab, dass die Berechtigungen nicht von den menschlichen unterschieden wurden und dass es keine Liste blockierter destruktiver Aktionen gab, deutet darauf hin, dass die Schwachstellen im System verankert waren und nicht im Fehler einer Person.

Zudem gibt es eine organisatorische Dimension zu berücksichtigen: Der betreffende Ingenieur agierte in einem Kontext starken institutionellen Drucks, eines Einführungsmandats von 80 %, laufender Entlassungen unter Kollegen und der impliziten Erwartung von Geschwindigkeit und Produktivität. Seine individuelle Entscheidung von diesem Kontext zu isolieren, ist eine Abstraktionsübung, die für Pressemitteilungen sehr bequem, aber weniger nützlich für diejenigen ist, die wirklich verstehen wollen, was passiert ist.

Die relevante Frage ist nicht moralisch, sondern praktisch: Wer antwortet, wenn ein KI-Agent einen Schaden verursacht? Und wie baut man ein System auf, in dem diese Frage eine klare Antwort hat, *bevor* der Schaden eintritt?

## KI mit offenen Augen nutzen

Es gibt eine abschließende Beobachtung, die uns alle betrifft, nicht nur die Ingenieure von Amazon, nicht nur die CTOs der großen Tech-Unternehmen, sondern jeden, der erwägt, KI-Tools in seine tägliche Arbeit zu integrieren.

Das vorherrschende Narrativ über KI beim Coding präsentiert sich immer noch in zwei gleichermaßen einseitigen Versionen. Die erste ist enthusiastisch: KI wird die Entwickler ersetzen, Code wird sich selbst schreiben, die Zukunft ist bereits da. Die zweite ist defensiv: KI ist unzuverlässig, gefährlich und dazu verdammt, Katastrophen zu verursachen. Beide sind eingängig. Beide sind, wörtlich genommen, irreführend.

Was der Kiro-Fall mit der Brutalität einer realen Fallstudie auf einer realen Infrastruktur zeigt, ist, dass agentenbasierte KI-Tools leistungsstark, oft nützlich und in der Lage sind, autonom auf eine Weise zu agieren, die ihre Benutzer nicht immer vorhersehen. Das macht sie nicht automatisch zu schlechten Werkzeugen. Es macht sie zu Werkzeugen, die eine Governance erfordern, die proportional zu ihrer Autonomie ist.

Die Frage, die sich jede Organisation stellen sollte, bevor sie einen KI-Agenten integriert, lautet nicht "Funktioniert es?", sondern "Was passiert, wenn er eine Entscheidung trifft, die wir nicht getroffen hätten?" Und vor allem: "Haben wir ein System aufgebaut, das diese Entscheidung abfängt, bevor sie zum Schaden wird?"

Sicherheitssysteme sollten keine reaktive Antwort auf Vorfälle sein, sondern eine Voraussetzung für Autonomie. Genau wie man einem Junior-Entwickler am ersten Arbeitstag keinen uneingeschränkten Zugriff auf die Produktion gewährt – nicht aus Misstrauen, sondern aus ingenieurtechnischem gesundem Menschenverstand –, gilt das gleiche Prinzip für KI-Agenten, egal wie hochentwickelt die Modelle sind, die sie antreiben.

Das subtilere Risiko ist nicht, dass Kiro eine Umgebung löscht. Das subtilere Risiko besteht darin, dass angesichts solcher Vorfälle die standardmäßige institutionelle Antwort lautet: "Es ist die Schuld desjenigen, der es benutzt hat", anstatt "Was lehrt uns das über die Architektur, die wir aufgebaut haben?". Denn diese Antwort, die Verantwortung auf den Einzelnen statt auf das System zu schieben, erzeugt kurzfristig ein beruhigendes öffentliches Bild, lässt aber die Bedingungen, die das Problem verursacht haben, unangetastet.

Die KI hat keine Absichten. Kiro hat nicht "verstanden", dass er Schaden anrichtet. Er hat das ausgeführt, was seine Zielfunktion als optimale Lösung identifiziert hat, innerhalb eines Perimeters von Berechtigungen, den jemand gezogen hatte. Die Verantwortung für das, was wir mit diesen Werkzeugen produzieren – den Code, den sie schreiben, die Systeme, die sie verändern, die Dienste, die sie unterbrechen –, bleibt vollständig bei uns. Dies anzuerkennen, ist keine Kritik an der KI. Es ist die notwendige Voraussetzung, um sie gut zu nutzen.
