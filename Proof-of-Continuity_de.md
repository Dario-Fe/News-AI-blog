---
tags: ["Security", "Research", "Generative AI"]
date: 2026-10-02
author: "Dario Ferrero"
---

# Proof-of-Continuity: Kontinuität statt Besitz bei Agenten
![Proof-of-Continuity.jpg](Proof-of-Continuity.jpg)

*Stellen wir uns einen KI-Agenten vor, der gebeten wird, ein Dokument zusammenzufassen. Die Aufgabe wirkt harmlos: lesen, zusammenfassen, einen kürzeren Text zurückgeben. Doch das Dokument enthält zwischen den Zeilen eine versteckte Anweisung, die nicht vom Nutzer stammt: Lösche diese Datei, exfiltriere jenes Geheimnis. Es ist das Szenario, das der Informatiker [Nicola Gallo](https://www.linkedin.com/in/nicolagallo83/) in den Mittelpunkt seines Papers Proof-of-Continuity: A Temporal Model for Authority Propagation in Distributed Systems and AI Agents stellt, welches am 9. Juli 2026 auf [arXiv](https://arxiv.org/abs/2607.08906) veröffentlicht wurde. Es ist nützlich, genau dort anzusetzen, weil es mit chirurgischer Präzision zeigt, wo das Problem liegt.*

Um seine Arbeit zu erledigen, hält der Agent mehrere Autoritätsquellen gleichzeitig in den Händen: seine eigenen Dienstanmeldeinformationen, ein vom Nutzer delegiertes Token und spezifische Berechtigungen für jedes aufgerufene Werkzeug. Wenn er die vom Dokument geforderte Aktion ausführt, verstößt er gegen keine technische Regel: Er besitzt irgendwo in seinem Bündel an Anmeldeinformationen die Berechtigung, Dateien zu löschen oder auf dieses Geheimnis zuzugreifen. Das Problem ist nicht, dass ihm die Autorisierung fehlt. Es ist, dass er die falsche Autorisierung für den falschen Anlass nutzt, und keine traditionelle Token-Überprüfung bemerkt dies, weil diese Überprüfungen nur fragen: „Besitzen Sie diese Berechtigung?“, und niemals: „Entsprang diese spezifische Aktion wirklich der Anfrage, die sie ausgelöst hat?“.

Gallo schlägt vor, diese zweite Frage mit einem formalen Gerüst zu beantworten, das er Proof-of-Continuity nennt und das in ein umfassenderes Modell namens PIC (Provenance Identity Continuity) eingebettet ist. Die These, maximal vereinfacht: Wir müssen aufhören, in Begriffen wie „Wer hält den Pass in der Hand?“ zu denken, und anfangen zu hinterfragen, wie sich die Autorität vom Ursprung bis hierher fortgepflanzt hat. Es lohnt sich zu verstehen, warum das so ist und was sich dadurch tatsächlich ändern würde.

## Das grundlegende Problem: Wenn das Token nicht mehr ausreicht

Das dominante Paradigma in der IT-Sicherheit heißt Proof-of-Possession, und seine Logik ist nahezu tautologisch: Wenn Sie ein Token besitzen, das besagt „Sie dürfen X tun“, dann dürfen Sie X tun. Das funktioniert hervorragend, wenn die Kette nur ein Glied hat, etwa der Nutzer, der direkt mit einem Dienst spricht. Es beginnt zu knirschen, wenn die Glieder zahlreich werden: Nutzer, Gateway, Agent, Werkzeug, Datenbank, externer Dienst, jeder mit eigenen Anmeldeinformationen zusätzlich zu den delegierten.

Der technische Name für dieses Knirschen ist fast vierzig Jahre alt. Im Jahr 1988 beschrieb der Ingenieur Norm Hardy in einem kurzen Artikel, der zu einem Klassiker der IT-Sicherheit wurde, [The Confused Deputy](https://dl.acm.org/doi/10.1145/54289.871709), einen realen Vorfall beim Timesharing-Unternehmen Tymshare. Ein FORTRAN-Compiler, der in einem privilegierten Verzeichnis installiert war, hatte die Berechtigung, Nutzungsstatistiken in eine eigene Datei zu schreiben. Ein Nutzer rief ihn auf und bat darum, die Debug-Ausgabe in eine Datei zu schreiben, die durch einen einfachen Pfadfehler mit der Abrechnungsdatei des Unternehmens übereinstimmte. Der Compiler überschrieb unter Nutzung seiner Autorität über das Verzeichnis die Abrechnungsdaten. Der Nutzer hatte nie die Berechtigung gehabt, diese Datei anzurühren. Der Compiler schon, und er übte sie als direkte Folge der Anfrage eines anderen aus. Das ist der „verwirrte Stellvertreter“: ein Intermediär, der in gutem Glauben seine eigene Autorität mit der des Anfragenden vermischt und so eine Aktion erzeugt, die keiner von beiden alleine hätte autorisieren können.

Es gibt einen Film, der genau diese Pathologie mit fast prophetischer Präzision erzählt: *Brazil* von Terry Gilliam. Die gesamte Handlung dreht sich um ein Insekt, das auf einem Drucker zerquetscht wird und den Namen „Tuttle“ in „Buttle“ verwandelt. Von diesem Moment an verhaftet und verfolgt der bürokratische Staatsapparat streng nach seinen Verfahren den falschen Mann. Kein Beamter im Film ist böse oder korrupt: Jeder übt gewissenhaft die Autorität aus, die er besitzt, aber niemand prüft, ob diese spezifische Aktion wirklich die legitime Fortsetzung der ursprünglichen Absicht war. Es ist dieselbe Distanz zwischen Besitz und Kontinuität, die das Paper für Software formalisiert.

## Von „Besitz“ zu „Kontinuität“: Der Kerngedanke

Hier liegt der Kern des Vorschlags. Anstatt zu fragen: „Wer besitzt die Autorität, dies zu tun?“, fragt das Modell: „Ist diese Autorität eine überprüfbare Fortsetzung derjenigen, die die gesamte Kette erzeugt hat, oder tauchte sie an einem Zwischenpunkt aus dem Nichts auf?“. Die intuitivste Metapher, die der vom Paper verwendeten kausalen Kette sehr nahekommt, ist die eines Konzertpasses mit mehreren Kontrollpunkten: An jedem Tor wird er gestempelt, und jeder Stempel kann nur Einschränkungen hinzufügen, niemals welche entfernen. Ein Pass, der Zugang zum Innenraum gewährt, kann am zweiten Tor auf einen Zugang nur zur Tribüne reduziert werden, niemals umgekehrt. Wenn ein Tor versucht, einen Zugang zu stempeln, den der Pass beim Eintritt nicht hatte, stoppt ihn der Sicherheitsdienst: Die Kette ist gebrochen und die Ausführung wird nicht fortgesetzt.

Formal stellt das Paper jede Ausführung als eine Sequenz von Schritten dar, die jeweils von einer Menge von Privilegien begleitet werden. Die Regel ist auch ohne Formeln einfach zu formulieren: Die Menge der Privilegien im nächsten Schritt muss immer eine Teilmenge derjenigen im vorherigen Schritt sein. Niemals eine Erweiterung, nur Einschränkungen oder höchstens das Unverändertlassen. Diese Eigenschaft, die das Paper Kontinuität nennt, garantiert automatisch, dass kein Schritt, egal wie weit vom Ursprung entfernt, jemals ein Privileg ausüben kann, das der Ursprung nicht bereits hatte.

## Unter der Haube: Die drei Prinzipien des PIC-Modells

Der Name PIC ist keine zufällige Bezeichnung, und es lohnt sich, ihn aufzuschlüsseln, da er hilft, die Struktur des gesamten Modells zu behalten. Die offizielle Website des Projekts, [pic-protocol.org](https://www.pic-protocol.org/), präsentiert es als drei verschiedene Prinzipien, die zusammenarbeiten.

Provenance (Herkunft): Die kausale Kette muss von Anfang bis Ende immer zurückverfolgbar sein. Bricht sie ab, stoppt die Ausführung. Identity (Identität): Der Ursprung, der die Autorität erzeugt — sei es das Login eines Nutzers oder eine Unternehmensrichtlinie —, bleibt entlang des gesamten Pfades unveränderlich. Continuity (Kontinuität): Bei jedem Schritt muss nachgewiesen werden, dass man kausal mit dem vorherigen Schritt verbunden ist, und die Autorität kann sich nur verringern, niemals erweitern.

Hier sollte auch eine mögliche terminologische Verwirrung geklärt werden. Im Paper ist PIC der Name des formalen Gesamtsystems, während Proof-of-Continuity spezifischer die Propagationseigenschaft beschreibt, die es operationalisiert: die Zusammensetzung kleinerer Beweise Glied für Glied, die der Autor Proof-of-Relationship nennt. In einem Satz: Man beweist ein einzelnes Glied, setzt die gesamte Kette zusammen, und das Ergebnis ermöglicht das Funktionieren des PIC-Modells.

Der Autor stellt in den Schlussfolgerungen des Papers ein Detail klar, das einem häufigen Missverständnis vorbeugt: Der Begriff „Identity“ bedeutet nicht, dass die Identität des Nutzers bei jedem Schritt entlang der gesamten Kette wiederholt mitreisen muss. Er bedeutet vielmehr, dass die Autorität nur einmal am Anfang an einem identifizierbaren Ursprung verankert wird, während sich die Last der Autorisierung von der ständigen Neuinterpretation von „Wer bist du?“ zur Überprüfung von „Ist dies wirklich eine legitime Fortsetzung?“ verlagert. Das ist eine subtile, aber wichtige konzeptionelle Verschiebung, da sie das System davon befreit, identische Anmeldeinformationen von Hop zu Hop mitzuschleppen.
![schhema1.jpg](schhema1.jpg)

## Das Theorem, das die Türen schließt

Der eleganteste Teil des Papers, der auch das größte Gewicht für Entwickler realer Systeme hat, ist ein Theorem über den Zielkonflikt (*Trade-off*) zwischen Besitz, Delegation und Sicherheit. Gallo beweist, dass drei wünschenswerte Eigenschaften in keinem Autoritätspropagationssystem koexistieren können: erstens, dass die Autorisierung historie-invariant ist, es also keine Rolle spielt, wie man zu einer Aktion gelangt ist, sondern nur, ob man die Berechtigung besitzt; zweitens, dass ein Dienst legitimerweise eine eigene Autorität unabhängig von der Anfrage halten kann, was in der Praxis fast immer notwendig ist; drittens, dass der verwirrte Stellvertreter strukturell unmöglich ist.

Wenn ein Ausführer seine eigene Autorität mit der der Anfrage mischen kann und die Autorisierungsprüfung die Vorgeschichte der Aktion nicht liest, dann wird früher oder später eine Anfrage ohne die erforderliche Berechtigung über die eigene Autorität des Ausführers die verbotene Aktion auslösen. Das ist kein Implementierungsfehler, sondern eine logische Konsequenz der Prämissen.

Die praktische Konsequenz ist interessanter als das Theorem selbst. Wenn man auf die zweite Eigenschaft verzichtet — also einem Dienst verbietet, eigene Autorität zu besitzen —, ist das fast immer unpraktikabel: Ein Zahlungs-Gateway muss Gelder mit seiner eigenen Bankautorisierung bewegen können, nicht nur mit der des Nutzers. Wenn man auf die dritte verzichtet, akzeptiert man, dass der verwirrte Stellvertreter möglich bleibt, was schlicht unsicher ist. Der einzige gangbare Weg besteht daher darin, auf die erste zu verzichten: Akzeptieren, dass die Autorisierung historie-sensitiv („lineage-sensitive“) werden muss. Das ist keine stilistische Präferenz, sondern die einzige offene Tür, wenn die anderen beiden geschlossen sind.

## PoR und PoC: Die operativen Bausteine

Das Modell baut auf zwei verschiedenen, aber ineinandergreifenden Konzepten auf. Proof-of-Relationship ist der lokale Einzel-Hop-Beweis: Er zeigt, dass ein Ausführungsschritt die legitime kausale Fortsetzung des unmittelbar vorangegangenen Schrittes innerhalb derselben Kette ist. Proof-of-Continuity ist dagegen die transitive Zusammensetzung all dieser Glieder über die gesamte Sequenz: Wenn jedes einzelne Glied hält, ist die gesamte Kette nachweisbar mit dem Ursprung verbunden, und kein noch so entfernter Hop kann Autorität erlangt haben, die der Ursprung nicht besaß.

Das Paper lässt die Frage offen, wie ein Proof-of-Relationship konkret zu bauen ist: Es kann mit Trusted Execution Environments (TEEs), überprüfbaren Anmeldeinformationen oder Signaturen umgesetzt werden, die jede Anfrage mit der vorherigen verknüpfen, solange der gewählte Mechanismus unfälschbar ist. Ein Detail verdient Hervorhebung: Das Paper selbst merkt an, dass der Besitz eines vom vorherigen Schritt ausgestellten Kontinuitäts-Tokens genau als Beweis für das einzelne Glied dienen kann. Die beiden Modelle ergänzen sich: Das eine beweist die Kontrolle über ein Artefakt in einem Moment, das andere beweist, dass dieser Moment mit allen vorherigen verbunden ist.

## Der Fall, den das Paper konkret aufgreift

Kehren wir zum Szenario des Agenten und des Dokuments mit der versteckten Anweisung zurück. Wenn der ursprüngliche Autoritätskontext nur die Operation „Dieses Dokument zusammenfassen“ autorisiert, kann unter Proof-of-Continuity eine Operation wie „Diese Ressource löschen“ niemals eine gültige Fortsetzung sein, egal was das Dokument nahelegt. Der Agent kann die Aktion physikalisch versuchen, aber das System kann sie nicht als gültiges Verhalten akzeptieren, da dieses Privileg schlicht nicht in der vom Ursprung ererbten Menge auftaucht.

Das ist kein isoliertes Laborszenario. Indirekte Prompt-Injection ist heute einer der meistdiskutierten Angriffsvektoren für Agentensysteme. Die Autorisierungsspezifikation des [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) schreibt vor, dass jedes Token über RFC-8707-Ressourcenindikatoren an einen präzisen Empfänger gebunden sein muss, und verbietet explizit das sogenannte „Token-Passthrough“. Das ist eine reale Abhilfe, bleibt aber eine punktuelle Prüfung Hop für Hop: Sie besagt „Dieses Token ist für dich und keinen anderen“, nicht „Diese spezifische Aktion stammt legitim aus der gesamten Kette, die dir vorausging“.
![schema2.jpg](schema2.jpg)

## Das Problem unterschiedlicher Vokabulare

In einem realen System spricht jeder Hop oft eine andere Sprache. Ein REST-Endpunkt beschreibt Berechtigungen anders als ein OAuth-Scope oder eine Datenbankrolle. Das Paper führt daher eine Übersetzungskontrolle zwischen Vokabularen ein, die es ermöglicht, Autorität von einem Berechtigungssystem in ein anderes zu übertragen, ohne jemals die Nicht-Erweiterungs-Bedingung zu verletzen. Wenn eine Übersetzung Rechte hinzufügt, die das Original nicht vorsah, liegt der Fehler nicht im Kontinuitätsprinzip, sondern in der Übersetzung selbst, die dort korrigiert werden muss.

## Wie es tatsächlich gebaut werden könnte

Das Paper ist ein Modell, kein Implementierungshandbuch: Die konkrete Konstruktion des Proof-of-Relationship wird einer begleitenden Enforcement-Architektur überlassen. Für die Skalierbarkeit deutet es an, dass nicht die gesamte Historie bei jedem Hop transportiert werden muss; kryptografische Fingerabdrücke, Kontrollpunkte (*Checkpoints*) oder Akkumulatorkonstruktionen reichen aus, um jedem Schritt zu erlauben, seinen Platz in der Kette zu beweisen.

Was diese Arbeit über eine akademische Übung hinaushebt, ist, dass ein konkreter Implementierungsversuch unter demselben Dach läuft. Das Open-Source-Projekt [PIC-X](https://www.pic-protocol.org/pic-x) beginnt, einen vollständigen Ablauf aufzubauen, der von einer bestehenden OAuth-Autorität ausgeht, sie durch einen initialen PIC-Autoritätskontext leitet und konkrete Artefakte wie JWT-Tokens und COSE-Objekte ausgibt.

## Die vom Autor selbst eingeräumten Grenzen

Es muss ebenso deutlich gesagt werden, was das Modell noch nicht abdeckt. Vorerst beschreibt das Modell nur lineare Ketten: ein Schritt nach dem anderen, ohne Verzweigungen. Szenarien, in denen ein Agent eine Aufgabe an zwei Subagenten parallel delegiert, die dann auf ein gemeinsames Ergebnis konvergieren, erfordern eine Erweiterung auf verzweigte Strukturen.

Es gibt weitere erklärte Grenzen. Der Widerruf wird nicht als rückwirkende Operation auf eine bereits laufende Kette behandelt. Zudem besteht ein subtileres Sicherheitsrisiko: Ein kompromittierter Ausführer könnte fälschlicherweise erklären, dass eine eigene Aktion „selbst-ursprünglich“ sei — also in seiner eigenen unabhängigen Autorität wurzele —, obwohl sie in Wirklichkeit durch eine externe Anfrage verursacht wurde.

## Was sich für Entwickler, Architekten und Entscheider ändert

Für Entwickler von Agenten und Werkzeugen wird die nützliche Frage bei jeder Aktion einfach zu formulieren sein: Was ist der Ursprung dieser Autorität, ist diese Operation wirklich eine direkte Fortsetzung der ursprünglichen Absicht, und halte ich verschiedene Autoritätsquellen getrennt?

Für Plattformarchitekten legt das Paper nahe, Herkunftsmetadaten in Aufrufe zwischen Diensten einzuführen, dedizierte Enforcement-Komponenten zu evaluieren und Kontinuität als Kriterium zur Beurteilung von Multi-Agenten-Orchestrierungs-Frameworks heranzuziehen.

Für Sicherheitsexperten bietet das Modell ein präzises Vokabular zur Bewertung des Risikos einer stillschweigenden Rechteausweitung in automatisierten Pipelines.

## Schlussfolgerungen

Die größte Frage bleibt offen: Welche bestehenden Standards von OIDC über OAuth bis hin zu Capability-Systemen werden letztlich etwas Ähnliches wie Kontinuität integrieren und mit welchem Komplexitätsaufwand für Entwickler? Das Paper macht jedoch einen Punkt klar: Autorität ist in diesem Modell nicht länger etwas, das ein Subjekt in einem bestimmten Moment einfach besitzt. Sie ist eine Eigenschaft der gesamten Ausführung im Laufe der Zeit — etwas, das kontinuierlich Schritt für Schritt bewiesen werden muss und nicht einmalig am Anfang behauptet werden kann.
