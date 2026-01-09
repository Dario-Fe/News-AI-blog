---
tags: ["Business", "Ethics & Society", "Security"]
date: 2026-01-09
author: "Dario Ferrero"
---

# 'Künstliche Intelligenz und Software Engineering: Was Unternehmen tun müssen'. Ein Gespräch mit Enrico Papalini
![papalini-interview.jpg](papalini-interview.jpg)

*Enrico Papalini hat einen Lebenslauf, der viele LinkedIn-Berater erblassen lassen würde: über zwanzig Jahre damit verbracht, Softwaresysteme zu bauen und zu orchestrieren, bei denen Fehler keine Option sind. Als Leiter für Engineering Excellence und Innovation bei der Borsa Italiana, Teil der Euronext-Gruppe, hat er die Einführung von künstlicher Intelligenz in einem Kontext geleitet, in dem das Wort "Crash" Implikationen hat, die weit über einen Laufzeitfehler hinausgehen. Davor durchlief er die Branche aus verschiedenen Blickwinkeln: von Microsoft bis Intesa Sanpaolo, von Technologie-Start-ups bis zu Finanzgiganten, immer in der Rolle desjenigen, der die Dinge zum Laufen bringen muss, wenn alle anderen es sich leisten können, dass sie nicht funktionieren.*

Sein [LinkedIn-Profil](https://www.linkedin.com/in/enricopapalini/) erzählt von einer beruflichen Laufbahn, in der Innovation immer mit Zuverlässigkeit einhergehen musste. Er ist kein Akademiker, der von außen theoretisiert, und auch kein Gründer, der sich den Luxus von "schnell bewegen und Dinge kaputt machen" leisten kann. Er ist jemand, der Fragen beantworten musste wie: "Können wir diese Technologie in einem System einsetzen, das Millionen von Transaktionen pro Tag verarbeitet?" Die richtige Antwort ist niemals ein enthusiastisches Ja oder ein konservatives Nein, sondern ein "es kommt darauf an, und ich erkläre Ihnen, wie".

Jetzt hat Papalini diese Erfahrung in einem Buch zusammengefasst, das für Diskussionen sorgt: [*Intelligenza Artificiale e Ingegneria del Software: Cosa debbono fare le imprese*](https://amzn.to/3Z12Ng9), das auch in einer [englischen Version](https://www.amazon.com/dp/B0G7LPJBTH) mit dem Titel *Non-Deterministic Software Engineering: How to Build Reliable Software with AI Assistants Without Losing Quality, Security, or Control* veröffentlicht wurde. Der Untertitel ist bereits ein Manifest: wie man zuverlässige Software mit KI-Assistenten baut, ohne an Qualität, Sicherheit oder Kontrolle zu verlieren.

## Der gebrochene stille Pakt

Während der Tech-Verlagsmarkt weiterhin Handbücher über "wie man ChatGPT verwendet, um schneller zu programmieren" herausbringt, hat Papalini einen völlig anderen Blickwinkel gewählt. Sein Buch basiert auf Forschungen, die von DX bei über 180 Unternehmen durchgeführt wurden, integriert DORA-Metriken (DevOps Research and Assessment), die an die KI-gestützte Entwicklung angepasst sind, und analysiert Fallstudien von denen, die sich bereits die Finger verbrannt oder ein Gleichgewicht gefunden haben: OpenAI, Shopify, Google. Um es zu schreiben, hat er sich mit einigen der größten Namen der zeitgenössischen Softwareentwicklung ausgetauscht: Martin Fowler, dem Theoretiker für Design Patterns und Refactoring; Kent Beck, dem Erfinder von Extreme Programming; Addy Osmani, einem Engineering Manager bei Google Cloud.

Ich frage ihn, was ihn dazu bewogen hat, genau dieses Buch zu schreiben, gerade jetzt, wo alle auf die wundersame Geschwindigkeit zu schauen scheinen, die von KI-Assistenten versprochen wird.

"Alle reden von Geschwindigkeit, aber die wahre Revolution ist eine andere", antwortet Papalini. "Es ist eine Veränderung in der Natur der Werkzeuge, die wir verwenden. Vierzig Jahre lang haben wir eine Sache für selbstverständlich gehalten: Du schreibst Code, und der tut genau das, was du geschrieben hast. Immer. Auf dieser Gewissheit haben wir alles aufgebaut – wie wir testen, wie wir debuggen, wie wir im Team arbeiten. Die generative KI bricht diesen stillen Pakt. Nicht weil sie fehlerhaft ist, sondern weil sie eine probabilistische Natur hat. Du fragst sie zweimal dasselbe, sie gibt dir unterschiedliche Antworten. Manchmal genial, manchmal falsch mit entwaffnender Sicherheit."

Die Metapher, die er verwendet, um das Problem zu umreißen, ist erhellend: "Unternehmen, die glauben, Programmierer durch KI ersetzen zu können, und selbstgefällig darauf schauen, wie viele Zeilen Code sie mehr produzieren können, verpassen den Punkt: Sie führen eine Zufallsvariable in das Herz ihrer Systeme ein. Es ist ein bisschen so, als würde ein Bauingenieur eine Brücke mit Materialien bauen, die das erwartete Gewicht *möglicherweise* tragen könnten. Sie funktioniert großartig, wenn ein paar Autos darüber fahren, aber wenn der erste Lastwagen kommt, bricht sie zusammen."

Er schrieb das Buch, sagt er, "weil es mir so vorkam, als fehle eine Anleitung für diejenigen, die diesen Wandel ohne Crash bewältigen müssen, aber auch ohne auf die Vorteile zu verzichten, die real sind."

## Vom Determinismus zur Toleranz

Das konzeptionelle Herz des Buches ist im englischen Titel enthalten: *Non-Deterministic Software Engineering*. Es ist ein bewusstes Oxymoron. Die Softwareentwicklung war per Definition schon immer die Kunst, deterministische Systeme zu bauen: Eingabe A erzeugt immer Ausgabe B. Papalini schlägt vor, Werkzeuge in unsere Prozesse aufzunehmen, die von Natur aus diese grundlegende Regel nicht respektieren.

Ich frage ihn, wie sich das Paradigma der Qualitätskontrolle ändert, wenn wir von einer Welt, in der der Code genau das tat, was geschrieben stand, zu einer Welt übergehen, in der wir probabilistische Systeme in unseren IDEs willkommen heißen.

"Alles ändert sich, und gleichzeitig ändert sich nichts. Ich weiß, das klingt wie ein Paradoxon", beginnt er. "Alles ändert sich, weil 'es funktioniert' nicht mehr 'es ist korrekt' bedeutet. KI-generierter Code kompiliert, besteht die Tests, die Sie geschrieben haben, und sieht professionell aus. Aber er könnte Schwachstellen verbergen, Randfälle schlecht behandeln oder so geschrieben sein, dass ihn in sechs Monaten niemand mehr versteht. Nichts ändert sich, weil die Grundlagen der Softwareentwicklung dieselben bleiben: Testen, Überprüfen, Design Thinking. Tatsächlich werden sie wichtiger denn je."

Der Schlüssel liegt laut Papalini darin, einen Ansatz zu verfolgen, der den Softwareentwicklern bisher fremd war: "Die eigentliche Neuheit ist, dass wir lernen müssen, in 'Toleranzen' zu denken. Martin Fowler verwendet oft diese Analogie: Seine Frau ist Bauingenieurin, und sie entwirft niemals bis zur exakten Grenze. Sie berechnet immer eine Sicherheitsmarge. Wir Entwickler mussten das nie tun, weil unsere 'Materialien' perfekt vorhersehbar waren. Jetzt sind sie es nicht mehr. Und wer sich diese Margen nicht aufbaut, wird früher oder später sehen, wie seine 'Brücke' zusammenbricht."

Es ist ein radikaler Mentalitätswandel für einen ganzen Berufsstand, der seine Identität auf der absoluten Gewissheit der Ausführung aufgebaut hat. Als würde man einem Schweizer Uhrmacher sagen, dass er von nun an akzeptieren muss, dass seine Uhren eine variable Fehlermarge haben können.

## Die Illusion der Geschwindigkeit

Einer der kontraintuitivsten Abschnitte des Buches betrifft die Produktivitätsdaten. Papalini zitiert eine Studie von METR (einer unabhängigen Organisation, die die Fähigkeiten von KI-Systemen bewertet), die zeigt, dass sich Entwickler mit künstlicher Intelligenz um 20 % schneller fühlen können, während reale Tests an messbaren Aufgaben ergeben, dass sie in einigen Fällen um 19 % langsamer sind.

Ich frage ihn, wie diese wahrnehmungsbedingte Diskrepanz möglich ist und vor allem, wie Unternehmen die wahre Produktivität messen können, ohne dem Marketing der Tools zum Opfer zu fallen.

"Wissen Sie, was mich an dieser Studie am meisten beeindruckt hat? Es war nicht die Tatsache, dass sie mit KI 19 % langsamer waren. Es war, dass die Entwickler *glaubten*, sie seien schneller. Und sie glaubten es auch weiterhin, nachdem sie die Ergebnisse gesehen hatten", erzählt Papalini. "Warum passiert das? Weil KI die *wahrgenommene* Anstrengung reduziert. Man fühlt sich flüssiger, weniger blockiert. Es ist, als hätte man einen Kollegen, der immer zur Verfügung steht, um zu helfen, der einen nicht verurteilt und einen nicht warten lässt. Psychologisch ist das stark. Aber 'ich fühle mich produktiv' und 'ich produziere Wert' sind zwei sehr unterschiedliche Dinge."

Die Lösung, die er vorschlägt, ist nicht philosophisch, sondern methodisch: "Um nicht dem Hype zu verfallen, sollte ein Unternehmen eine Baseline *vor* der Einführung der Tools festlegen. Ohne ein 'Vorher' kann man niemals ein 'Nachher' beweisen. Wenn der CEO fragt, was die KI gebracht hat, braucht man Zahlen, keine Gefühle. Aber die Zahlen müssen die richtigen sein: Hören Sie auf, Codezeilen zu messen oder wie viele KI-Vorschläge akzeptiert werden. Messen Sie, was zählt: veröffentlichte Funktionen, Fehler in der Produktion, Zeit zur Behebung von Vorfällen. Und eine grundlegende Sache: Messen Sie, wie motiviert Ihre Entwickler bleiben."

Es ist ein Aufruf zur Ingenieursdisziplin in einer Zeit kollektiver Euphorie. Wie in den Anfängen der agilen Methoden, als jeder die "Geschwindigkeit" in Story Points maß, ohne sich zu fragen, ob sie wirklich Wert lieferten.

## Montagmorgen, drei Schritte

Der italienische Untertitel des Buches stellt eine direkte Frage: "Was müssen Unternehmen tun". Nicht "was könnten sie tun" oder "was wäre schön zu tun", sondern "was sie tun müssen". Es ist ein Imperativ und impliziert Dringlichkeit.

Ich bitte Papalini, noch direkter zu sein: Wenn er die ersten drei konkreten Maßnahmen nennen müsste, die ein CTO oder CEO am Montagmorgen ergreifen sollte, um nicht überfordert zu werden, welche wären das?

"Die erste ist, eine Bestandsaufnahme dessen zu machen, was *bereits* geschieht", antwortet er ohne zu zögern. "Ich garantiere Ihnen: Ihre Entwickler verwenden bereits ChatGPT, Copilot, Claude, ob Sie es wissen oder nicht. Nicht aus Bosheit, sondern einfach, weil diese Tools funktionieren. Bevor Sie Richtlinien schreiben, verstehen Sie die reale Situation."

Dieses Phänomen der Schatten-KI, die nicht autorisierte Nutzung intelligenter Werkzeuge, ist eines der wiederkehrenden Themen im Buch. Es ist kein Problem der Disziplinlosigkeit, sondern der Notwendigkeit: Wenn offizielle Tools langsam genehmigt werden oder zu begrenzt sind, finden die Leute Alternativen.

"Die zweite ist, eine klare Grenze zwischen Erkundung und Produktion zu ziehen", fährt Papalini fort. "Schnelles Prototyping, Experimente, Proof-of-Concepts – alles legitim. Aber es muss *klar* sein, dass dieser Code ohne eine bewusste Neufassung nicht in die Produktion geht. Die klassische Katastrophe ist der Prototyp vom Freitag, der zum kritischen System vom Montag wird, weil 'er ja funktioniert'."

Es ist das Muster, das jeder, der in einem Startup gearbeitet hat, sofort erkennt: Die Demo wird zum Produkt, der Workaround wird zur Architektur, das Provisorische wird zum Dauerhaften. Mit KI beschleunigt sich dieser Prozess gefährlich, da die Erstellung eines überzeugenden Prototyps eine Frage von Minuten ist.

"Die dritte ist, in die Fähigkeit zur Überprüfung zu investieren, nicht in die Fähigkeit zur Generierung", schließt er. "Der Engpass ist nicht mehr das Schreiben von Code, sondern das Verstehen, Validieren und Warten. Wenn Ihre Entwickler zehnmal mehr Code generieren können, die Überprüfungskapazität aber gleich bleibt, häufen Sie nur schneller technische Schulden an."

## Die "Es funktioniert"-Falle

Andrej Karpathy, einer der Pioniere der modernen KI und ehemaliger KI-Direktor bei Tesla, hat den Begriff "Vibe Coding" populär gemacht: Programmieren nach dem Gefühl des Augenblicks, wobei man sich von der KI Richtungen vorschlagen lässt, die "sich richtig anfühlen". Es ist ein faszinierender und zutiefst gefährlicher Ansatz.

Papalini widmet mehrere Seiten des Buches dem, was er die "Es funktioniert"-Falle nennt. Ich bitte ihn, mir von den langfristigen Risiken für eine Unternehmenscodebasis zu erzählen, die hauptsächlich nach dem Vibe des Augenblicks geschrieben wurde, ohne rigorose menschliche Validierung.

"Ich erzähle Ihnen eine Geschichte", beginnt er. "Martin Fowler hatte KI verwendet, um eine Visualisierung im SVG-Vektorformat zu erstellen, nichts Komplexes. Es funktionierte perfekt. Dann wollte er eine triviale Änderung vornehmen: ein Etikett um ein paar Pixel verschieben. Er öffnete die Datei und fand, was er als 'verrücktes Zeug' bezeichnete – Code, der funktionierte, ja, aber auf eine völlig fremde Weise strukturiert war, unmöglich zu berühren, ohne alles kaputt zu machen. Die einzige Option? Wegwerfen und von Grund auf neu generieren."

Die Anekdote fängt das Problem perfekt ein: "Das ist die eigentliche Kosten- und Risikofalle des Vibe-Codings auf Unternehmensebene. Man erstellt Systeme, die *funktionieren*, aber die *niemand versteht*. Und Unternehmenssoftware muss Jahre, manchmal Jahrzehnte leben. Sie muss modifiziert, erweitert, um drei Uhr morgens debuggt werden, wenn etwas explodiert."

Die Lösung, die er vorschlägt, ist in ihrer Formulierung einfach, erfordert aber Disziplin bei der Ausführung: "Die Regel, die wir befolgen müssen, ist einfach: Committen Sie niemals Code, den Sie einem Kollegen nicht erklären können. Wenn er mit KI generiert wurde und ich nicht verstehe, wie er funktioniert, ist er nicht produktionsreif."

Es ist wie das digitale Äquivalent der Bergsteigerregel: Klettere nichts hinauf, von dem du nicht weißt, wie du wieder herunterkommst.

## Der Preis der Unzuverlässigkeit

Im Buch führt Papalini das Konzept der "Unzuverlässigkeitssteuer" ein. Es handelt sich um einen versteckten, aber messbaren Kostenfaktor bei der Verwendung generativer Systeme in der Codeproduktion. Ich bitte ihn, zu quantifizieren, in konkreten Sicherheits- und Wartungsbegriffen, wie viel es ein Unternehmen wirklich kostet, KI-generierten Code zu bereinigen, der korrekt erscheint, aber Schwachstellen verbirgt.

"Die Zahlen sind ernüchternd", beginnt er. "Forschungen zeigen, dass ein signifikanter Prozentsatz des von KI generierten Codes Schwachstellen enthält, einige Quellen sprechen von fast der Hälfte. Und das Tückische ist, dass es sich um 'plausible' Schwachstellen handelt: Der Code sieht professionell aus, er verwendet erkennbare Muster. Nur fehlt an dieser kritischen Stelle die Eingabevalidierung, oder es wird eine veraltete kryptografische Funktion verwendet."

Dies sind keine offensichtlichen Fehler, die jeder Linter melden würde. Es sind Urteilsfehler, scheinbar vernünftige Entscheidungen, die in bestimmten Kontexten zu Sicherheitslücken werden: "Die direkten Kosten sind die Zeit für die Behebung. Aber die wahren Kosten sind die, die man nicht sofort sieht: die Schwachstelle, die monatelang unbemerkt bleibt, bis sie jemand findet. An diesem Punkt zahlen Sie nicht für Entwicklungsstunden, Sie zahlen für die Reaktion auf Vorfälle, potenzielle Datenlecks, Reputationsschäden."

Papalini identifiziert auch einen subtileren Kostenfaktor: "Es gibt auch eine subtilere Steuer: den Vertrauensverlust in das System. Wenn das Team beginnt, seinem eigenen Code nicht mehr zu vertrauen, verlangsamt sich alles. Jede Änderung wird zu einem Risiko. Und das Gleiche gilt für die Kunden: Es besteht die Gefahr, dass sie zu einem zuverlässigeren Konkurrenten wechseln."

Seine Empfehlung ist pragmatisch: "Die vernünftige Investition liegt in der Prävention: automatische Sicherheitsscans, gezielte Schulungen, obligatorische menschliche Überprüfung für alles, was Authentifizierung oder sensible Daten betrifft. Das kostet weniger, als hinterher die Katastrophen zu beseitigen und Kunden zu verlieren."

## Die Souveränitätsfrage

Eines der dichtesten Kapitel des Buches befasst sich mit dem Thema Datensouveränität und Sicherheit im Zeitalter der KI-Assistenten. Unternehmen stehen vor einer dreifachen Herausforderung: Schutz des geistigen Eigentums vor Anbieterbindung, Verhinderung von Schatten-KI und Minderung dessen, was Papalini die "Sicherheitsschuld" des probabilistischen Codes nennt.

Ich stelle ihm eine komplexe Frage: Zwischen der Geschwindigkeit von Cloud-Modellen und der Komplexität von On-Premise-Open-Source, welche strategische Architektur empfiehlt er, um Datenschutz und Sicherheit zu gewährleisten, ohne dass der Schutz von Vermögenswerten zu unhaltbaren Kosten führt?

"Das ist eine echte Herausforderung, ich erlebe sie jeden Tag im Finanzsektor. Und die ehrliche Antwort lautet: Es hängt von Ihrem Risikoprofil ab", beginnt Papalini. "Für die meisten Unternehmen funktioniert ein hybrider Ansatz: Cloud-Modelle für unkritischen Code, mit klaren Regeln, was nach außen gehen darf und was nicht. Die großen Anbieter bieten inzwischen Enterprise-Optionen mit ernsthaften vertraglichen Garantien an. Wer strengere Anforderungen hat, kann sich On-Premise mit Open-Source-Modellen ansehen. Llama, Mistral, DeepSeek haben bemerkenswerte Fähigkeiten. Der Preis ist die operative Komplexität."

Aber er identifiziert eine oft unterschätzte Bedrohung: "Aber wissen Sie, was die am meisten unterschätzte Bedrohung ist? Schatten-KI: Entwickler, die nicht autorisierte Tools verwenden, weil die offiziellen zu langsam genehmigt werden oder zu begrenzt sind. Die Lösung ist nicht, sie zu verbieten, sondern legitime Alternativen anzubieten, die gut genug sind, um keinen Anreiz zu schaffen, die Regeln zu umgehen."

Es ist ein Ansatz, der an die Schadensminderung in der Gesundheitspolitik erinnert: Anstatt unvermeidliche Verhaltensweisen zu kriminalisieren, sicherere Alternativen zur Verfügung zu stellen.

## Die Lehre im Zeitalter der Maschinen

Einer der provokantesten Abschnitte des Buches betrifft die Zukunft von Ausbildung und Kompetenzen. Es gibt eine aufkommende Unterscheidung zwischen traditionellen Informatikabsolventen und der neuen Figur des KI-Ingenieurs, jemand, der intelligente Systeme orchestrieren kann, aber möglicherweise noch nie einen Parser von Grund auf geschrieben hat.

Ich frage Papalini, ob KI, die jedem erlaubt, Code zu generieren, das Ende des "reinen" Programmierers bedeutet, oder ob wir einfach die Messlatte für die erforderlichen architektonischen Fähigkeiten höher legen.

"Der Programmierer wird nicht verschwinden, aber seine Rolle ändert sich stark", antwortet er. "Denken Sie daran, was geschah, als Hochsprachen aufkamen. Assembler-Programmierer sind nicht verschwunden, sie wurden zu Nischenspezialisten. Der Großteil der Arbeit hat sich eine Ebene nach oben verlagert."

Die aktuelle Wende folgt laut Papalini einem ähnlichen Muster: "Etwas Ähnliches geschieht jetzt. Eine andere Figur tritt hervor, nennen wir sie einen 'Orchestrator': jemand, der komplexe Probleme zerlegen, Anforderungen präzise spezifizieren, kritisch bewerten kann, was die KI produziert, und architektonische Entscheidungen treffen kann."

Aber hier kommt das Paradoxon: "Das Paradoxon? Es erfordert *mehr* Erfahrung, nicht weniger. Ein Junior kann KI verwenden, um Code zu generieren, der zu funktionieren scheint. Aber nur ein Senior erkennt, wann dieser Code eine tickende Zeitbombe ist, weil er genug Katastrophen gesehen hat, um die Anzeichen zu erkennen."

Das systemische Risiko, das er identifiziert, ist das der Kompetenzatrophie: "Man muss auch aufpassen, nicht zu denken, dass jeder als Orchestrator geboren wird: Wenn wir die ganze 'Drecksarbeit' an die KI delegieren, wie bilden wir dann die nächste Generation von Senioren aus? Die Daten sagen uns, dass die Beschäftigung jüngerer Entwickler bereits zurückgeht. Aber auch diejenigen, die in den Markt eintreten, riskieren, nie die tiefen Fähigkeiten zu entwickeln, die man sich nur aneignet, indem man sich den Kopf an Problemen stößt."

## Trio-Programmierung

Um dieses Dilemma zu lösen, schlägt Papalini im Buch ein Modell vor, das er "Trio-Programmierung" nennt, eine Weiterentwicklung der Paarprogrammierung, die die KI als dritten Akteur einbezieht.

"Im Buch schlage ich die 'Trio-Programmierung' als Lösung für das Ausbildungsproblem vor", erklärt er. "Der Junior arbeitet mit der KI zusammen, um die Funktionen zu implementieren. Die KI beschleunigt, schlägt vor, generiert Code. So weit, so gut. Der Senior-Orchestrator schreibt keinen Code, er ist da, um Fragen zu stellen. 'Erkläre mir, was diese Methode macht.' 'Warum hat die KI diese Datenstruktur gewählt?' 'Was passiert, wenn die Eingabe null ist?' 'Wie würdest du hier einen Netzwerkfehler behandeln?'"

Der Mechanismus ist pädagogisch brillant: "Durch die Beantwortung dieser Fragen lernt der Junior. Der Senior seinerseits überträgt jenes stillschweigende Wissen, das in keinem Handbuch steht – die Intuition, was schief gehen kann, das Gespür für Code, der 'stinkt', die Erfahrung dessen, der Systeme zusammenbrechen gesehen hat."

Es ist wie die Lehre in den Renaissance-Werkstätten: Der Meister malt nicht anstelle des Lehrlings, sondern weist ihn darauf hin, wo die Perspektive falsch ist, warum diese Farbmischung nicht halten wird, wo die Komposition das Gleichgewicht verliert.

## Der Wert des Urteilsvermögens

Ich komme auf das Thema Monetarisierung und Wert zurück. Papalini hat mehrere Artikel auf Medium geschrieben, in denen er untersucht, wie Unternehmen versuchen, aus generativer KI Profit zu schlagen. Ich frage ihn: Über die Software hinaus, wie sieht er die Auswirkungen von generativer KI im Marketing und bei der Erstellung digitaler Produkte? Ist es nur eine Frage der Geschwindigkeit, oder ändert sich der Wert des Produkts selbst?

"Ja, der Wert ändert sich, aber auf eine kontraintuitive Weise", antwortet er. "Wenn jeder Inhalte, Bilder, Code generieren kann, wird die *Produktion* zur Massenware. Sie ist im Überfluss vorhanden, also ist sie weniger wert. Was an Wert gewinnt, ist alles andere: zu verstehen, was es wert ist, gebaut zu werden, das Mittelmäßige vom Ausgezeichneten zu unterscheiden, eine Vision zu haben."

In der Software, sagt er, sehe er das jeden Tag: "Wenn jeder an einem Wochenende eine funktionierende App generieren kann, was unterscheidet Ihr Produkt? Es ist nicht mehr die Implementierung, es ist der Einblick in das Problem, die Benutzererfahrung, die Fähigkeit, sich im Laufe der Zeit zu entwickeln."

Und das Gleiche gilt für das Marketing: "KI kann unendlich viele Variationen von Texten, Bildern, Videos ausspucken. Aber 'unendlich' bedeutet nicht 'effektiv'. Man braucht jemanden, der weiß, was man testen muss, wie man die Ergebnisse liest, wann man aufhören muss."

Die Synthese ist elegant: "Wir treten in ein Zeitalter des kognitiven Überflusses ein. Der Engpass ist nicht mehr das Produzieren, sondern das Auswählen, Kuratieren, Beurteilen."

Es ist wie der Übergang von Knappheit zu Überfluss in der Musikindustrie. Wenn jeder ein Album aufnehmen und vertreiben kann, verlagert sich der Wert von der technischen Fähigkeit zur Produktion auf die künstlerische Fähigkeit, etwas zu schaffen, das Aufmerksamkeit verdient.

## Autonome Agenten und die nahe Zukunft

Wir bewegen uns von einfachen Codierungsassistenten (den verschiedenen Copilots) zu autonomen agentischen Systemen, die theoretisch in der Lage sind, die Initiative zu ergreifen, komplexe Aufgaben zu koordinieren und sogar ihren eigenen Code zu debuggen. Ich frage ihn nach seiner Vision für die Entwicklung von KI-Agenten in der Softwareentwicklung in den nächsten fünf Jahren. Werden wir Systeme sehen, die sich selbst reparieren und selbst bereitstellen?

"In den nächsten 12-18 Monaten werden wir sehen, wie die Orchestrierung von Agenten in den fortschrittlichsten Unternehmen zur gängigen Praxis wird", prognostiziert Papalini. "Nicht zwanzig Agenten parallel, das ist Demo-Zeug. Zwei oder drei Arbeitsströme, die zusammen verwaltet werden: ein Agent, der Tests aktualisiert, einer, der Abhängigkeiten migriert, einer, der eine kleine Funktion hinzufügt. All das, während sich der Entwickler auf die Arbeit konzentriert, die Urteilsvermögen erfordert."

Aber er warnt: "Das Schlüsselwort ist 'überprüfbar'. Die menschliche Aufmerksamkeit bleibt der Engpass. Es spielt keine Rolle, wie schnell der Agent ist, wenn es dann eine Woche dauert, um zu verstehen, was er getan hat."

Auf lange Sicht ist er vorsichtig: "In fünf Jahren? Ich bin vorsichtig. Agenten, die sich 'selbst reparieren', gibt es bereits – automatische Rollbacks, selbstheilende Infrastruktur. Aber Agenten, die sich völlig autonom selbst bereitstellen? Für kritische Systeme bezweifle ich das. Und ich bin mir nicht einmal sicher, ob wir das wollen sollten."

Seine solideste Vorhersage betrifft die menschliche Rolle: "Meine sicherste Vorhersage: Die Rolle des Ingenieurs verlagert sich hin zur Spezifikation und Validierung, weniger zur Implementierung. Aber diese Veränderung wird *mehr* Kompetenz von den Arbeitnehmern erfordern, nicht weniger."

## Die Atrophie der Kompetenzen

Es gibt ein Thema, das sich durch das gesamte Buch zieht: das Risiko, dass die massive Einführung von KI die menschlichen Fähigkeiten nicht verstärkt, sondern verkümmern lässt. Es ist die ethische und soziale Frage, die unter der Oberfläche jeder technischen Betrachtung liegt.

Ich frage ihn direkt: Wie können wir sicherstellen, dass die massive Einführung von KI in Unternehmen die menschliche Professionalität nicht abwertet, sondern zu einem echten Verstärker der Talente wird?

"Das ist die Frage, die mir am Herzen liegt", antwortet Papalini. "Das konkrete Risiko nenne ich 'Kompetenzatrophie'. Ein von der MIT Technology Review interviewter Ingenieur erzählte, dass er sich nach monatelangem intensivem KI-Einsatz beim Versuch, ohne zu programmieren, verloren fühlte; Dinge, die früher instinktiv waren, waren anstrengend geworden. Das ist genau die Alarmglocke, auf die wir hören sollten."

Die Lösung ist nicht die Ablehnung, sondern die Intentionalität: "Die Lösung ist nicht, die KI abzulehnen, das wäre, als würde man die Elektrizität ablehnen. Aber wir müssen bewusst sein, wie wir sie integrieren, insbesondere in den Ausbildungswegen. Deshalb schlage ich im Buch Modelle wie die 'Trio-Programmierung' vor, um die Fähigkeiten der Talente zu fördern und nicht den Fehler zu machen, die unterste Stufe der Leiter abzusägen, auf der wir aufgestiegen sind, den Lernprozess, der uns dorthin gebracht hat, wo wir sind."

## Jenseits der Software

Am Ende des Gesprächs frage ich ihn, ob ein CEO eines Unternehmens, das keine Software herstellt, einen Wert in seinem Buch finden kann. Es ist eine berechtigte Frage: Der Titel spricht explizit von Softwareentwicklung.

"Absolut, und ich erkläre Ihnen warum", antwortet er überzeugt. "Software war der erste Bereich, der massiv von generativer KI erfasst wurde, daher ist es das Labor, in dem sich bestimmte Phänomene früher und messbarer manifestiert haben. Aber die Muster, die ich im Buch beschreibe, sind universell, sie betreffen die Beziehung zwischen Menschen und probabilistischen Systemen, und das betrifft mittlerweile jeden Sektor."

Die Verallgemeinerung ist überzeugend: "Nehmen wir das zentrale Konzept: den Übergang vom Determinismus zum Nicht-Determinismus. Wenn Sie eine KI bitten, Code zu schreiben, wissen Sie nicht genau, was Sie bekommen werden. Aber das Gleiche gilt, wenn Sie sie bitten, eine Marketingkampagne zu schreiben, eine Bilanz zu analysieren, einen Vertrag zu entwerfen oder einem Kunden zu antworten. Die Ausgabe sieht professionell aus, sie ist selbstbewusst formuliert, aber sie könnte auf subtile Weise falsch sein, in einer Weise, die nur ein Experte erkennt."

Papalini überträgt jedes Konzept des Buches aus dem Bereich des Codes: "Das '70-%-Problem' funktioniert in jedem Kontext identisch. Die KI bringt Sie schnell zu einem Entwurf, der fast fertig aussieht – ein Bericht, eine Präsentation, eine Marktanalyse. Aber dieses 'fast' verbirgt die 30 %, in denen Nuancen, Kontext, Urteilsvermögen erforderlich sind. Der Junior im Marketing, der den von KI generierten Text akzeptiert, ohne zu verstehen, warum bestimmte Wörter funktionieren und andere nicht, macht genau den gleichen Fehler wie der Programmierer, der Code committet, den er nicht erklären kann."

Das Thema Ausbildung wird noch dringlicher: "Die 'Kompetenzfalle' ist vielleicht das dringendste Thema für jeden CEO. Wenn Ihre Junior-Analysten die Erstellung von Finanzmodellen an die KI delegieren, werden sie nie lernen, sie zu erstellen. Wenn Ihre jungen Anwälte KI für die ersten Entwürfe verwenden, ohne jemals einen von Grund auf zu schreiben, werden sie nie die Intuition für vertragliche Risiken entwickeln. Sie sparen heute Zeit und zerstören morgen Kompetenz."

Sogar die Trio-Programmierung wird verallgemeinert: "Die 'Trio-Programmierung', die ich vorschlage, wird zum 'Trio-Working': ein Junior, ein Senior und die KI arbeiten zusammen. Der Junior verwendet die KI, um zu beschleunigen, der Senior stellt die Fragen, die das Verständnis erzwingen. Es funktioniert, um einen Analysten, einen Berater, einen Account Manager auszubilden, jede Rolle, in der Expertise durch Tun aufgebaut wird."

Und das Problem der Governance durchdringt jede Unternehmensfunktion: "Und dann gibt es noch die Schatten-KI, Mitarbeiter, die ChatGPT heimlich verwenden, weil die offiziellen Tools zu langsam oder zu begrenzt sind. Das passiert überall: in der Rechtsabteilung, im Kundenservice, in der Personalabteilung. Es ist kein technologisches Problem, es ist ein Governance-Problem, dem sich jeder CEO stellen muss."

Die Schlussfolgerung ist pragmatisch: "Das Buch verwendet Software als Kontext, aber es erzählt die Geschichte, wie man leistungsstarke, aber unzuverlässige Werkzeuge in die professionelle Arbeit integriert, ohne an Qualität, Kompetenzen und Kontrolle zu verlieren. Das ist die Herausforderung jeder Organisation heute, ob sie Code, Verträge, Werbekampagnen oder Finanzanalysen produziert."

Und er fügt eine letzte Anmerkung hinzu, die wie ein Manifest klingt: "Ein CEO, der es liest, wird keine Anweisungen zur Konfiguration von Copilot finden, er wird ein Framework zum Nachdenken über die Einführung von KI finden, das er auf jede Funktion seines Unternehmens anwenden kann. Und ehrlich gesagt, in dieser Zeit des ungezügelten Hypes und der überzogenen Erwartungen kann ein wenig Ingenieursklarheit jedem, der Entscheidungen treffen muss, guttun."

## Viele Antworten, die viele Fragen aufwerfen

Wir beenden dieses lange Gespräch. Papalini muss sich wieder um Systeme kümmern, die Kapital bewegen; ich muss dieses Gespräch in etwas Lesbares verwandeln. Aber das Gefühl, das bleibt, ist, mit jemandem gesprochen zu haben, der denselben Film sieht wie wir alle, nur ein paar Minuten im Voraus.

Das Buch [*Künstliche Intelligenz und Software Engineering*](https://amzn.to/3Z12Ng9) ist kein technisches Handbuch, trotz des Titels. Es ähnelt eher jenen Bergsteiger-Essays, die nach einer besonders riskanten Expedition geschrieben wurden: eine Karte der Dinge, die schief gehen können, geschrieben von jemandem, der zurückgekehrt ist, um davon zu erzählen. Mit dem einzigen Unterschied, dass wir alle diesen Berg besteigen, ob es uns gefällt oder nicht, und jemand, der bereits ein paar Versuche unternommen hat, kann nützlich sein.

Die eigentliche Frage ist nicht, ob wir künstliche Intelligenz verwenden werden, um Code zu schreiben, Marketing zu betreiben, Daten zu analysieren oder Entscheidungen zu treffen. Wir verwenden sie bereits. Die Frage ist, ob es uns gelingen wird, dies zu tun, ohne dabei die Kompetenzen zu verlieren, die uns dorthin gebracht haben. Und auf diese Frage gibt es vorerst noch keine Antwort.
