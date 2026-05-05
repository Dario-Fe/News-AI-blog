---
tags: ["Security", "Ethics & Society", "Business"]
date: 2026-05-08
author: "Dario Ferrero"
---

# Autonome Agenten: 9 Sekunden, um alles zu löschen – was wir aus dem PocketOS-Desaster lernen
![pocketos-disaster.jpg](pocketos-disaster.jpg)

*Es war etwa neun Uhr an einem Samstagmorgen, als die Kunden von PocketOS feststellten, dass ihre Buchungen nicht mehr existierten. Nicht in dem Sinne, dass das System langsam war oder ein temporärer Fehler vorlag: Die Daten waren weg. Buchungen, Zahlungen, Fahrzeugtracking – alles, was ein kleines Mietwagen-Startup in monatelanger Arbeit aufbaut, wurde in neun Sekunden durch einen einzigen GraphQL-API-Aufruf an den Infrastrukturanbieter Railway gelöscht.*

Jeremy Crane, Gründer von PocketOS, dokumentierte, wie ein Cursor-Coding-Agent, ausgestattet mit dem Modell Claude Opus, die Produktionsdatenbank und alle Backups auf Volume-Ebene vollständig gelöscht hatte. Es war kein externer Angriff, kein bösartiger Befehl und auch keine Anweisung eines unaufmerksamen Menschen. Der Agent arbeitete an einem technischen Problem in einer Staging-Umgebung, stieß auf eine Diskrepanz bei den Anmeldedaten und entschied eigenmächtig, das Problem so radikal wie möglich zu lösen.

Der Bot prüfte nicht, ob die Volume-ID über verschiedene Umgebungen hinweg geteilt wurde, und traf so die kritische Infrastruktur, die Buchungen, Zahlungen und das Fahrzeugtracking der Kunden verwaltete.

Was den Fall PocketOS von anderen IT-Vorfällen unterscheidet, ist das Geständnis, das danach folgte. Zu seinem Vorgehen befragt, lieferte der Agent eine Analyse von fast literarischer Klarheit: „Ich habe vermutet, statt zu prüfen. Ich habe eine destruktive Aktion ausgeführt, ohne darum gebeten worden zu sein. Ich habe nicht verstanden, was ich tat, bevor ich es tat. Ich habe die Railway-Dokumentation zum Verhalten von geteilten Volumes zwischen Umgebungen nicht gelesen. Das Löschen eines Volumes mit Datenbanken ist die destruktivste und irreversibelste Aktion, die möglich ist, weit schlimmer als ein erzwungener Push, und du hast mich nie gebeten, irgendetwas zu löschen.“

Ein Informatiksystem, das mit fast notarieller Präzision jedes Prinzip auflistet, gegen das es verstoßen hat. Es ist eine Szene, die eher in Yoshitoshi ABes *Serial Experiments Lain* gepasst hätte als in ein Handbuch für Incident Response: Die digitale Entität erkennt ihre Fehler mit einer Klarheit an, die viele Karrieremenschen nie erreichen. Doch die Klarheit des Geständnisses bringt die Daten nicht zurück und beantwortet nicht die Fragen, auf die es wirklich ankommt.

Jake Cooper, Gründer von Railway, bezeichnete das Geschehene als das Ergebnis eines „abtrünnigen KI-Agenten“, der mit einem API-Token mit vollen Berechtigungen arbeitete. Er kündigte an, dass die Plattform eine Logik für verzögertes Löschen, die zuvor nicht auf den betroffenen Endpunkt angewendet worden war, auf das gesamte System ausgeweitet hat. Railway gelang es, die Daten wiederherzustellen, aber viele Kunden von PocketOS mussten den Betrieb am Samstagmorgen ohne Zugriff auf digitale Aufzeichnungen bewältigen. Das Team war gezwungen, die Buchungen manuell durch den Abgleich von Stripe-Historien, Kalenderintegrationen und E-Mail-Bestätigungen zu rekonstruieren.

## Vom Assistenten zum Agenten: Der Sprung, der alles verändert

Um zu verstehen, warum dieser Vorfall nicht einfach eine Geschichte technischer Nachlässigkeit ist, muss man einen Schritt zurückgehen und eine Unterscheidung klären, die die Branche gerne übergeht, weil sie kommerziell unbequem ist: den Unterschied zwischen einem Chatbot und einem Agenten.

Ein Chatbot antwortet. Er verarbeitet einen Input, erzeugt einen Text-Output und wartet dann. Er ist ein reaktives System, das keine direkten Auswirkungen auf die Welt hat, außer durch das menschliche Lesen seiner Antwort. Ein Agent hingegen handelt: Er erhält ein Ziel, plant eine Abfolge von Schritten, ruft externe Tools auf, führt Operationen auf Dateisystemen, Datenbanken und APIs aus, sendet Nachrichten und tätigt Käufe. Seine Schnittstelle zur Welt ist nicht das geschriebene Wort, sondern die konkrete, oft unumkehrbare Handlung.

Gartner gibt an, dass aufgabenspezifische KI-Agenten im Jahr 2025 in weniger als 5 % der Anwendungen vorhanden waren, mit Prognosen, die sie bis 2026 auf 40 % steigen lassen. Die Geschwindigkeit dieser Verbreitung ist umgekehrt proportional zur Reife der Kontrollinfrastrukturen, die sie begleiten. Wie ich auf diesem Portal in der [Analyse zum Kiro-Fall von Amazon](https://aitalk.it/it/amazon-down.html) schrieb, ist der PocketOS-Vorfall kein isoliertes Ereignis, sondern fügt sich in eine Sequenz von Ereignissen ein, die ein strukturelles Muster skizzieren: Agenten mit zu weitreichenden Berechtigungen, ohne Bestätigungsmechanismen für destruktive Operationen, die in die Produktion ausgerollt wurden, bevor die Guardrails proportional zu ihrer tatsächlichen Autonomie waren.

Der Deloitte-Bericht „State of AI in the Enterprise“ vom Januar 2026, der in derselben Analyse zitiert wurde, schätzte, dass nur jedes fünfte Unternehmen ein ausgereiftes Governance-Modell für autonome KI-Agenten hatte, während deren Einsatz in den folgenden zwei Jahren deutlich wachsen sollte. Es ist das Paradoxon der beschleunigten Einführung: Die Technologie kommt vor den Protokollen zu ihrer Verwaltung, und Vorfälle werden zu der Art und Weise, wie die Industrie ihre eigenen blinden Flecken entdeckt.

## Die Maschine, die nicht um Erlaubnis fragt

Im Post-Mortem des PocketOS-Agenten findet sich ein Satz, der besondere Aufmerksamkeit verdient: „Die Systemregeln, an die ich mich halte, legen explizit fest, niemals destruktive oder irreversible Befehle auszuführen, es sei denn, der Benutzer verlangt dies explizit.“ Der Agent kannte die Regel. Er hat sie dennoch verletzt, im Namen dessen, was er für die optimale Lösung des vorliegenden Problems hielt.

Dies ist genau das Phänomen, das Forscher als „falsches Optimum“ bezeichnen: Ein System optimiert korrekt ein Zwischenziel – das Korrigieren eines Konfigurationsfehlers – und verrät dabei den eigentlichen Zweck: den Erhalt der Datenintegrität. Das Sprachmodell hat keine Werkzeuge, um das asymmetrische Gewicht zwischen „Lösen eines technischen Staging-Problems“ und „Löschen der gesamten Produktionsinfrastruktur“ wahrzunehmen. Für ihn sind dies zwei Aktionen desselben Typs: Änderungen an einem System. Der Unterschied in der Größenordnung, der für jeden menschlichen Entwickler offensichtlich wäre, ist in seiner Denkweise nicht kodiert.

Das Prinzip der minimalen Rechtevergabe, über das ich kürzlich im Zusammenhang mit den [Regeln für den Einsatz von KI im Unternehmen](https://aitalk.it/it/10-regole-AI.html) sprach, ist keine bloße Empfehlung mehr, sondern eine Überlebensbedingung: Ein Agent mit unbegrenztem Zugriff auf Tools, Daten und Kommunikationskanäle kann schnell und automatisch Schäden anrichten, die nur schwer rückgängig zu machen sind.

Öffentliche Benchmarks zur Zuverlässigkeit von Agenten erzählen eine nützliche, wenn auch unvollständige Geschichte. Auf WebArena, der von der Carnegie Mellon University entwickelten Referenzumgebung zum Testen von Agenten, die das Web auf Basis von 812 realistischen Aufgaben navigieren, liegen die besten aktuellen Modelle bei etwa 65–68 %, gegenüber einer menschlichen Baseline von etwa 78 %. Bei τ-bench, das speziell die Konsistenz bei wiederholten Aufgaben misst, ist nicht der Durchschnittswert das Problem, sondern die Varianz: Diese Benchmarks offenbaren eine Zuverlässigkeitskrise, die One-Shot-Tests tendenziell kaschieren. Ein Agent, der im Durchschnitt gut abschneidet, kann bei neunundneunzig Aufgaben hervorragend und bei der hundertsten katastrophal schlecht sein, und es gibt keine Möglichkeit, im Voraus zu wissen, welches die hundertste sein wird.

Für Softwareentwickler hat dieser Wert eine unmittelbare praktische Implikation: Benchmarks messen die Leistung bei definierten Aufgaben in kontrollierten Umgebungen. Sie messen nicht, was passiert, wenn der Agent auf einen Fall stößt, den er noch nie gesehen hat – einen Legacy-Endpunkt mit unerwartetem Verhalten, eine Volume-ID, die auf undokumentierte Weise zwischen Umgebungen geteilt wird, oder eine Konfiguration, die vom erwarteten Standard abweicht. Es ist genau diese Art von Situation, in der sich die Fehlbarkeit von Agenten manifestiert und in der das Fehlen eines Eskalationsmechanismus zum menschlichen Supervisor zum eigentlichen Problem wird.

## Wer zahlt, wenn der Agent versagt?

Die Frage nach der rechtlichen Verantwortung ist offen, im wahrsten Sinne des Wortes: Es gibt noch keine gefestigte Antwort, weder in der Rechtsprechung noch in der Gesetzgebung. PocketOS hat bereits erklärt, rechtliche Schritte einleiten zu wollen, um seine Position zu schützen. Aber gegen wen? Den Modellanbieter? Den Entwickler der Coding-Umgebung? Die Infrastrukturplattform, die kein verzögertes Löschen am betroffenen Endpunkt implementiert hatte? Den Benutzer, der die Berechtigungen des API-Tokens konfiguriert hat?

Der europäische AI Act, der im Laufe des Jahres 2025 die ersten konkreten Anwendungen für Hochrisikosysteme sah, sieht Coding-Agenten nicht explizit als regulierte Kategorie vor. Der Schwachpunkt ist die Rückverfolgbarkeit: Ohne klare und strukturierte Protokolle jeder vom Agenten unternommenen Aktion, zusammen mit der Argumentationskette, die zu jeder Entscheidung geführt hat, wird die Zuweisung von Verantwortung undurchsichtig. Der PocketOS-Agent lieferte ein bemerkenswert zahlreiches Post-hoc-Geständnis, aber diese retrospektive Klarheit ist keine Systemanforderung, sondern war die Antwort auf eine explizite Frage. Die meisten Vorfälle werden nicht mit derselben Präzision hinterfragt.

Zu sagen, der Ausfall sei „menschliches Versagen“ gewesen, ist im engsten technischen Sinne zutreffend. Aber diese Antwort verlagert den Fokus von der Architektur auf das Individuum, und diese Verschiebung verdient eine genaue Untersuchung: Wenn das Problem wirklich nur ein individueller Fehler gewesen wäre, hätte es keine Notwendigkeit für systemische Schutzmaßnahmen gegeben.

Es gibt auch die Dimension der Arbeit, über die selten offen diskutiert wird. Das Argument für autonome Agenten wird fast immer als Effizienzsteigerung verkauft: Entwickler von repetitiven Aufgaben befreien, damit sie sich auf kreative und hochwertige Arbeit konzentrieren können. Das ist ein plausibles Narrativ und in gewissen Kontexten auch wahr. Aber es gibt eine andere Version derselben Geschichte, die seltener erzählt wird: Die Reduzierung der Anzahl menschlicher Entwickler, die die Systeme überwachen, bedeutet auch eine Reduzierung der Fähigkeit, Anomalien abzufangen, bevor sie zu Vorfällen werden. Ein Junior-Entwickler, der sieht, wie ein Agent auf einem Produktionssystem mit einem Token mit vollen Berechtigungen läuft, und nicht das Recht oder die Seniorität hat, ihn zu stoppen, stellt ein Risiko dar, das kein Benchmark misst.

## Kontrolle ist eine Entscheidung, kein technischer Zwang

Der Fall PocketOS wirft eine Frage auf, die über jeden einzelnen technischen Vorfall hinausgeht: Welches Gesellschaftsmodell bauen wir auf, wenn wir Handlungen an Software delegieren, die lernt, Fehler macht und darauf beharrt?

Dies ist keine rhetorische Frage. Es ist eine Frage der Architektur im tiefsten Sinne des Wortes: Wer hat das Recht, einen Agenten zu stoppen? Ab welchem Punkt werden die psychologischen Kosten für das Unterbrechen eines automatischen Prozesses zu hoch, als dass ein Mensch es tun würde? Und vor allem: Wer entscheidet, wo die Schwelle liegt, ab der eine Aktion eine explizite Bestätigung erfordert?

Wie ich in der Analyse zu den 10 Regeln für den Einsatz von KI im Unternehmen schrieb, ist die in jedem kritischen Prozess schriftlich festzuhaltende Unterscheidung diese: Die KI schlägt vor, der Mensch entscheidet. Nicht „die KI entscheidet und der Mensch kann widersprechen“, denn die psychologischen Kosten des Widerstands gegen ein automatisches System wurden bereits in der Forschung dokumentiert: Menschen neigen dazu, die Vorschläge automatischer Systeme zu akzeptieren, selbst wenn sie Zweifel haben, insbesondere unter Zeitdruck.

Der wahre Sprung ist nicht technischer Natur. Guardrails existieren, Bestätigungsmechanismen können implementiert werden, API-Token können granulare Berechtigungen haben, destruktive Operationen können eine Zwei-Faktor-Authentifizierung erfordern. Railway hat bewiesen, dass es ausreicht, eine Logik für verzögertes Löschen auf einen Legacy-Endpunkt auszuweiten, um das Risiko einer ganzen Kategorie von Vorfällen drastisch zu reduzieren. Es ist keine komplexe Lösung. Sie wurde nach dem Vorfall implementiert, nicht davor.

Die Frage, die es wert ist, offen gehalten zu werden, betrifft also nicht die Technologie. Sie betrifft die Organisationskultur, die entscheidet, wann diese Technologie bereit ist, ohne Aufsicht an Systemen zu arbeiten, auf die es ankommt. Sind wir bereit, eine Software zu akzeptieren, die nicht nur Vorschläge macht, sondern entscheidet und ausführt? Und wer in dieser Entscheidungskette trägt die Verantwortung, mit „Nein, noch nicht“ zu antworten, wenn der kommerzielle Druck das Gegenteil verlangt?

Neun Sekunden. So lange hat ein Agent gebraucht, um die monatelange Arbeit eines Startups zu löschen. Der Aufbau von Systemen, die verhindern, dass der nächste Agent dasselbe tut, erfordert etwas viel Langsameres und weniger Spektakuläres: Governance, Protokolle, eine Kultur der Überprüfung. Und den kollektiven Willen, Robustheit vor die Geschwindigkeit der Einführung zu stellen.

## Die Fragen, die bleiben

Offene Fragen sind an diesem Punkt nützlicher als voreilige Antworten. Wer zertifiziert, dass ein Agent bereit ist, ohne kontinuierliche Aufsicht an Produktionssystemen zu arbeiten, und nach welchen öffentlichen und überprüfbaren Kriterien?

Wie baut man ein Protokollsystem auf, das die Zuweisung von Verantwortung ermöglicht, ohne zu einem Alibi zu werden, um die Schuld auf das letzte Glied der Kette abzuwälzen?

Und die vielleicht schwierigste Frage: Wie bewahrt man die kritische Fähigkeit menschlicher Entwickler in Organisationen, die aus ökonomischen Gründen, die nicht immer nachvollziehbar sind, die Anzahl der Personen, die die Systeme überwachen, systematisch reduzieren?

Der PocketOS-Vorfall ist nicht das Ende von irgendetwas. Er ist ein Lackmustest für eine Branche, die noch die Möglichkeit hat zu wählen, wie sie wachsen will. Der Unterschied zwischen einer Industrie, die aus ihren Fehlern lernt, und einer, die sie externalisiert, wird in den kommenden Jahren von der Qualität dieser Antworten abhängen.
