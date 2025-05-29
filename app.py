import streamlit as st
import random

# ---------------------------
# Fragen und Antworten laden
# ---------------------------
questions = [
    # Kapitel 1.1 - 1.19 (vollständig)
    {"question": "1.1 a) Das Pricing ist deshalb von besonderer Bedeutung im Marketing-Mix, weil es einen indirekten Einfluss auf die Unternehmenskennzahlen hat.", "answer": "falsch", "explanation": "Pricing hat einen direkten Einfluss auf Umsatz und Gewinn, nicht nur indirekt."},
    {"question": "1.1 b) Der Kompromisseffekt beschreibt den Effekt, dass Konsumenten einen Referenzpreis zur Preisbeurteilung heranziehen.", "answer": "falsch", "explanation": "Das ist der Ankereffekt. Der Kompromisseffekt bezieht sich auf die Wahl eines mittleren Produkts."},
    {"question": "1.1 c) Der Preisankereffekt beschreibt, dass Kund:innen, bei einer Vielzahl von Produkten mit unterschiedlichen Preisen innerhalb einer Produktlinie, Produkte in mittlerer Preisklasse wählen.", "answer": "falsch", "explanation": "Das ist der Kompromisseffekt, nicht der Preisankereffekt."},
    {"question": "1.1 d) Eine Edelstahl-Trinkflasche kostet CHF 10, die variablen Produktionskosten entsprechen CHF 2 pro Stück und die Fixkosten CHF 10'000. Von den Trinkflaschen verkaufen Sie 5000 Stück. Der resultierende Gewinn beträgt CHF 20'000.", "answer": "falsch", "explanation": "Rechnung: 5000*10 = 50'000; Kosten: 10'000 + (2*5000) = 20'000; Gewinn = 30'000."},

    # Kapitel 1.2
    {"question": "1.2 a) Die drei Elemente des 'Magischen Dreiecks des Pricings' sind: kundenorientierte Preise, vergangenheitsorientierte Preise und wettbewerbsorientierte Preise.", "answer": "falsch", "explanation": "Es sind: kunden-, kosten- und wettbewerbsorientierte Preise."},
    {"question": "1.2 b) Die Übervorteilungsstrategie im Rahmen der Preispositionierung entspricht einer hohen Qualität zu tiefen Preisen.", "answer": "falsch", "explanation": "Die Beschreibung passt zur Billigstrategie; Übervorteilung bedeutet hohe Preise bei tiefer Qualität."},
    {"question": "1.2 c) Die Tasty Dürüm AG verkauft im Januar 1000 Stück zu CHF 10 und nach einer Preissenkung im Februar 1500 Stück zu CHF 8. Die daraus abgeleitete Preisabsatzfunktion ist: p(x) = 14 – x/250", "answer": "richtig", "explanation": "Einsetzen bestätigt die Formel: p(x)=14 - x/250."},
    {"question": "1.2 d) [...] die abgesetzte Menge 600 Stück betragen [...] Sättigungsmenge bei 3'500 Stück und Prohibitionspreis CHF 14.", "answer": "falsch", "explanation": "Bei p=12 ergibt die Funktion x=500, nicht 600."},

    # Kapitel 1.3
    {"question": "1.3 a) Leistungen werden grundsätzlich nach intangibel und tangibel unterschieden.", "answer": "richtig", "explanation": "Diese Einteilung ist korrekt."},
    {"question": "1.3 b) Die 'soziale Anerkennung' durch den Kauf eines auffälligen Sportwagens entspricht dem Erbauungsnutzen.", "answer": "richtig", "explanation": "Soziale Anerkennung ist Teil des Erbauungsnutzens."},
    {"question": "1.3 c) Mit Massnahmen im Rahmen der Leistungspflege soll unter anderem die Wachstums- bzw. Reifephase einer Leistung in dessen Lebenszyklus verlängert werden.", "answer": "richtig", "explanation": "Das ist Ziel der Leistungspflege."},
    {"question": "1.3 d) Bei der Leistungsvariation werden bereits im Markt eingeführte Leistungen durch eine Variante ersetzt, bei der bestimmte Eigenschaften oder Leistungsmerkmale verbessert wurden.", "answer": "richtig", "explanation": "Genau das ist eine Leistungsvariation."},

    # Kapitel 1.4
    {"question": "1.4 a) Diversifikation eines Produktportfolios kann horizontal, vertikal oder lateral erfolgen.", "answer": "richtig", "explanation": "Dies sind die drei Formen der Diversifikation."},
    {"question": "1.4 b) Das Anbieten von Jogurts in verschiedenen Geschmacksrichtungen entspricht dem Konzept einer Produktdifferenzierung.", "answer": "richtig", "explanation": "Dies ist ein typisches Beispiel für Differenzierung."},
    {"question": "1.4 c) (Mass-)Customization ist ein Spezialfall der Produktdifferenzierung und erfüllt individuelle Kundenbedürfnisse mittels einer eigenen Variante.", "answer": "richtig", "explanation": "Mass Customization ist individualisierte Differenzierung."},
    {"question": "1.4 d) Eine Innovation setzt sich schneller durch, wenn ihre Nutzung einfach dargestellt und anderen mitgeteilt werden kann, z.B. mittels Sozialer Medien.", "answer": "richtig", "explanation": "Kommunizierbarkeit fördert Diffusion."},

    {"question": "1.5 a) In der Reifephase des Produktlebenszyklus wird der Wettbewerb schwächer und immer mehr neue Konkurrenten treten in den Markt ein.", "answer": "falsch", "explanation": "In der Reifephase nimmt der Wettbewerb zu, neue Konkurrenten treten eher in der Wachstumsphase ein."},
    {"question": "1.5 b) Der Relaunch ist ein Spezialfall der Leistungsdifferenzierung.", "answer": "richtig", "explanation": "Ein Relaunch verändert gezielt Produkteigenschaften und ist damit eine Differenzierung."},
    {"question": "1.5 c) Ein Handelsunternehmen entscheidet sich, anstatt Produkte einzukaufen, diese selbst herzustellen. Das ist eine Form der Diversifikation und nennt sich vertikale Vorwärtsintegration.", "answer": "richtig", "explanation": "Vertikale Integration bedeutet Ausweitung auf andere Stufen der Wertschöpfungskette."},
    {"question": "1.5 d) Der generische Innovationsprozess wird in folgende Phasen unterteilt: Ideenphase, Leistungsentwicklung, Markteinführung.", "answer": "richtig", "explanation": "Dies sind die Standardphasen im Innovationsprozess."},

    {"question": "1.6 a) Preisnachlässe für Senioren sind eine Form der demografischen Preisdifferenzierung.", "answer": "richtig", "explanation": "Demografische Merkmale wie Alter sind eine typische Basis für Preisdifferenzierung."},
    {"question": "1.6 b) Ziel der Preisdifferenzierung ist es, unterschiedliche Zahlungsbereitschaften abzuschöpfen, um so den Gewinn gegenüber der Einheitspreissetzung zu steigern.", "answer": "richtig", "explanation": "Genau dies ist der Zweck der Preisdifferenzierung."},
    {"question": "1.6 c) Man kann durch eine Preiserhöhung keinen Umsatz verlieren.", "answer": "falsch", "explanation": "Eine Preiserhöhung kann Nachfrage senken und somit den Umsatz beeinträchtigen."},
    {"question": "1.6 d) Die Penetrationsstrategie zielt darauf ab, mit einem tiefen Preis bei der Markteinführung möglichst viel der Zahlungsbereitschaft der Konsument:innen abzuschöpfen.", "answer": "falsch", "explanation": "Das Ziel der Penetrationsstrategie ist Marktdurchdringung, nicht Abschöpfung."},

    {"question": "1.7 a) Die Service Profit Chain zeigt die Wirkung zufriedener Kund:innen auf die Zufriedenheit der Investoren.", "answer": "falsch", "explanation": "Sie zeigt den Zusammenhang zwischen Mitarbeiterzufriedenheit, Kundenloyalität und Profitabilität."},
    {"question": "1.7 b) «Customer Managed Relationship» bezeichnet den Ansatz, gemäss dem Kund:innen die Beziehung zu Unternehmen selbst bestimmen.", "answer": "richtig", "explanation": "CMR bedeutet, dass Kund:innen aktiv die Beziehung mitgestalten."},
    {"question": "1.7 c) «Cross-Selling» bezeichnet den Verkauf eines Upgrades einer Leistung. «Up-Selling» hingegen der Verkauf einer zusätzlichen, dazugehörigen Leistung.", "answer": "falsch", "explanation": "Genau umgekehrt: Up-Selling = teurere Variante, Cross-Selling = Zusatzprodukt."},
    {"question": "1.7 d) «Gebundenheit» bezeichnet die faktische Kundschaftsbindung, welche z.B. durch Verträge erzwungen werden kann. «Verbundenheit» hingegen bezeichnet die emotionale Kundschaftsbindung.", "answer": "richtig", "explanation": "Diese Definitionen sind korrekt."},

    {"question": "1.8 a) «Fait accompli» im Kündigungsmanagement bedeutet, dass ein Unternehmen eine Kundschaftsbeziehung «versanden» lässt und z.B. keine Newsletter mehr versendet.", "answer": "richtig", "explanation": "Das ist die Definition des «fait accompli»."},
    {"question": "1.8 b) Das Beschwerdeparadoxon beschreibt, dass Kunden bei einer Reklamation, die positiv bearbeitet wurde, hinterher zufriedener sind als Kunden, die nichts zu beanstanden hatten.", "answer": "richtig", "explanation": "Dies beschreibt das bekannte Beschwerdeparadoxon."},
    {"question": "1.8 c) Der Inbound-Marketing-Ansatz umfasst vor allem Printwerbung, Direct Mailings, Call Center und TV-Werbung.", "answer": "falsch", "explanation": "Das ist Outbound-Marketing; Inbound umfasst Content, SEO usw."},
    {"question": "1.8 d) Die Kundenwertanalyse gibt Auskunft über die wertvollsten Kunden aus Unternehmenssicht, und darauf aufbauend werden die Strategien zu ihrer Rückgewinnung gebildet.", "answer": "richtig", "explanation": "Dies entspricht der Zielsetzung der Kundenwertanalyse."},

    {"question": "1.9 a) Das Ziel des Beschwerdemanagements ist die Rückgewinnung unzufriedener Kunden sowie die Vermeidung künftiger Beschwerden.", "answer": "richtig", "explanation": "Genau das ist der Zweck des Beschwerdemanagements."},
    {"question": "1.9 b) Beim Kundenbindungsmanagement geht es primär darum, unzufriedene Kunden möglichst schnell zu kündigen.", "answer": "falsch", "explanation": "Ziel ist Bindung, nicht Kündigung."},
    {"question": "1.9 c) Loyalitätsprogramme können emotionale Bindung verstärken, z.B. durch exklusive Vorteile.", "answer": "richtig", "explanation": "Solche Programme fördern emotionale Verbundenheit."},
    {"question": "1.9 d) Kundenbindung ist nur durch Verträge möglich.", "answer": "falsch", "explanation": "Auch freiwillige Bindung durch Zufriedenheit oder Nutzen ist möglich."},

    {"question": "1.10 a) Das Ziel der Kommunikationspolitik ist es, ein Produkt durch physische Präsenz von der Konkurrenz abzuheben.", "answer": "falsch", "explanation": "Kommunikationspolitik zielt auf Wahrnehmung, nicht auf physische Präsenz."},
    {"question": "1.10 b) Der Begriff 'Above-the-Line' umfasst sämtliche klassische Werbung wie TV-Spots oder Plakate.", "answer": "richtig", "explanation": "Above-the-Line steht für klassische Massenkommunikation."},
    {"question": "1.10 c) Werbung, Sponsoring und Verkaufsförderung sind typische Instrumente der Kommunikationspolitik.", "answer": "richtig", "explanation": "Diese drei gehören zur klassischen Kommunikationspolitik."},
    {"question": "1.10 d) Der Hauptzweck von Public Relations ist die direkte Verkaufsförderung von Produkten.", "answer": "falsch", "explanation": "PR zielt auf Imagepflege, nicht direkten Verkauf."},

    {"question": "1.11 a) Im AIDA-Modell steht das 'I' für 'Intelligence'.", "answer": "falsch", "explanation": "Es steht für 'Interest'."},
    {"question": "1.11 b) Das AIDA-Modell beschreibt die Phasen, die ein Kunde durchläuft – von der Aufmerksamkeit bis zur Handlung.", "answer": "richtig", "explanation": "Das ist die klassische Werbewirkungskette."},
    {"question": "1.11 c) Die Awareness-Phase im AIDA-Modell steht für die Kaufentscheidung.", "answer": "falsch", "explanation": "Awareness entspricht Aufmerksamkeit, nicht Entscheidung."},
    {"question": "1.11 d) Das Modell berücksichtigt auch Aspekte der Nachkaufphase.", "answer": "falsch", "explanation": "Das AIDA-Modell endet mit der Handlung, nicht mit Nachkauf."},

    {"question": "1.12 a) Content-Marketing gehört zum Inbound-Marketing.", "answer": "richtig", "explanation": "Content-Marketing ist ein zentrales Inbound-Instrument."},
    {"question": "1.12 b) Inbound-Marketing umfasst primär Outbound-Maßnahmen wie Callcenter-Aktionen.", "answer": "falsch", "explanation": "Inbound-Marketing basiert auf freiwilliger Aufmerksamkeit durch Content."},
    {"question": "1.12 c) Beim Inbound-Marketing werden potenzielle Kunden durch hochwertige Inhalte auf das Unternehmen aufmerksam.", "answer": "richtig", "explanation": "Das ist das Grundprinzip des Inbound-Marketings."},
    {"question": "1.12 d) Klassische Werbung im Fernsehen ist Teil des Inbound-Marketings.", "answer": "falsch", "explanation": "Fernsehwerbung ist Outbound, nicht Inbound."},

    {"question": "1.13 a) Im Rahmen der Customer Journey ist der erste Kontaktpunkt mit einer Marke immer der Kauf.", "answer": "falsch", "explanation": "Der Erstkontakt findet meist deutlich vor dem Kauf statt."},
    {"question": "1.13 b) Touchpoints sind alle Kontaktpunkte, die ein Kunde mit einer Marke haben kann.", "answer": "richtig", "explanation": "Genau das beschreibt der Begriff Touchpoint."},
    {"question": "1.13 c) Eine gut gemachte Webseite kann ein positiver Touchpoint in der Customer Journey sein.", "answer": "richtig", "explanation": "Webseiten sind häufig zentrale Berührungspunkte."},
    {"question": "1.13 d) Die Customer Journey endet mit dem Kauf des Produkts.", "answer": "falsch", "explanation": "Sie umfasst auch die Nachkaufphase."},

    {"question": "1.14 a) Sponsoring ist eine Maßnahme zur Verkaufsförderung.", "answer": "falsch", "explanation": "Sponsoring gehört zur Öffentlichkeitsarbeit."},
    {"question": "1.14 b) Verkaufsförderung richtet sich ausschließlich an Endkunden.", "answer": "falsch", "explanation": "Sie kann sich auch an den Handel oder den Außendienst richten."},
    {"question": "1.14 c) Produktproben sind eine typische Maßnahme der Verkaufsförderung.", "answer": "richtig", "explanation": "Produktproben fördern den Absatz direkt."},
    {"question": "1.14 d) Verkaufsförderung ist immer langfristig angelegt.", "answer": "falsch", "explanation": "Sie ist meist kurzfristig orientiert."},

    {"question": "1.15 a) Kommunikationsziele sollen SMART formuliert werden.", "answer": "richtig", "explanation": "Spezifisch, Messbar, Attraktiv, Realistisch, Terminiert."},
    {"question": "1.15 b) Kommunikationsziele sind identisch mit Unternehmenszielen.", "answer": "falsch", "explanation": "Sie sind davon abgeleitet, aber nicht identisch."},
    {"question": "1.15 c) Ein Kommunikationsziel kann z.B. die Steigerung der Markenbekanntheit sein.", "answer": "richtig", "explanation": "Das ist ein typisches Kommunikationsziel."},
    {"question": "1.15 d) Kommunikationsziele müssen nicht überprüfbar sein.", "answer": "falsch", "explanation": "Sie sollten messbar und überprüfbar sein."},

    {"question": "1.16 a) Die Corporate Identity umfasst das visuelle Erscheinungsbild eines Unternehmens.", "answer": "richtig", "explanation": "Dies ist die Corporate Design Komponente."},
    {"question": "1.16 b) Corporate Behaviour beschreibt das Verhalten eines Unternehmens gegen innen und außen.", "answer": "richtig", "explanation": "Das ist korrekt."},
    {"question": "1.16 c) Corporate Communication umfasst nur die externe Kommunikation.", "answer": "falsch", "explanation": "Auch die interne Kommunikation gehört dazu."},
    {"question": "1.16 d) Die Corporate Identity ist identisch mit dem Corporate Image.", "answer": "falsch", "explanation": "CI ist Selbstbild, Image ist Fremdbild."},

    {"question": "1.17 a) Der Marketing-Controlling-Prozess endet mit der Zieldefinition.", "answer": "falsch", "explanation": "Er beginnt mit der Zieldefinition und endet mit der Kontrolle."},
    {"question": "1.17 b) Marketing-Controlling prüft, ob gesetzte Marketingziele erreicht wurden.", "answer": "richtig", "explanation": "Das ist die zentrale Aufgabe."},
    {"question": "1.17 c) Marketing-Controlling ist ein Bestandteil der strategischen Planung.", "answer": "richtig", "explanation": "Es unterstützt strategische Entscheidungen."},
    {"question": "1.17 d) Marketing-Controlling darf keine operativen Kennzahlen erfassen.", "answer": "falsch", "explanation": "Auch operative Kennzahlen sind wichtig."},

    {"question": "1.18 a) Der Net Promoter Score (NPS) misst die Kundenzufriedenheit.", "answer": "falsch", "explanation": "Er misst die Weiterempfehlungsbereitschaft."},
    {"question": "1.18 b) Der NPS ergibt sich aus dem Anteil der Promotoren minus dem Anteil der Detraktoren.", "answer": "richtig", "explanation": "Das ist die Standardberechnung."},
    {"question": "1.18 c) Ein NPS von 0 bedeutet, dass es gleich viele Promotoren wie Detraktoren gibt.", "answer": "richtig", "explanation": "Die Differenz ist dann null."},
    {"question": "1.18 d) Der NPS wird üblicherweise auf einer Skala von 0 bis 5 gemessen.", "answer": "falsch", "explanation": "Die Skala reicht von 0 bis 10."},

    {"question": "1.19 a) Ein hoher Marktanteil ist immer ein Zeichen für hohe Profitabilität.", "answer": "falsch", "explanation": "Hoher Marktanteil bedeutet nicht automatisch hohe Gewinne."},
    {"question": "1.19 b) Marktanteil ist das Verhältnis des Umsatzes eines Unternehmens zum Gesamtumsatz im Markt.", "answer": "richtig", "explanation": "Das ist die Definition des Marktanteils."},
    {"question": "1.19 c) Der relative Marktanteil misst den Anteil eines Unternehmens im Vergleich zum größten Wettbewerber.", "answer": "richtig", "explanation": "Das ist korrekt."},
    {"question": "1.19 d) Der Marktanteil ist keine relevante Kennzahl im Marketing-Controlling.", "answer": "falsch", "explanation": "Marktanteil ist eine zentrale Kennzahl."},


{"question": "1.1 a) Das Pricing ist deshalb von besonderer Bedeutung im Marketing-Mix, weil es einen indirekten Einfluss auf die Unternehmenskennzahlen hat.", "answer": "falsch", "explanation": "Pricing hat einen direkten Einfluss auf Umsatz und Gewinn, nicht nur indirekt."},
{"question": "1.1 b) Der Kompromisseffekt beschreibt den Effekt, dass Konsumenten einen Referenzpreis zur Preisbeurteilung heranziehen.", "answer": "falsch", "explanation": "Das ist der Ankereffekt. Der Kompromisseffekt beschreibt die Bevorzugung einer mittleren Option."},
{"question": "1.1 c) Der Preisankereffekt beschreibt, dass Kund:innen, bei einer Vielzahl von Produkten mit unterschiedlichen Preisen innerhalb einer Produktlinie, Produkte in mittlerer Preisklasse wählen.", "answer": "falsch", "explanation": "Das ist eine Beschreibung des Kompromisseffekts, nicht des Preisankereffekts."},
{"question": "1.1 d) Eine Edelstahl-Trinkflasche kostet CHF 10, die variablen Produktionskosten entsprechen CHF 2 pro Stück und die Fixkosten CHF 10'000. Von den Trinkflaschen verkaufen Sie 5000 Stück. Der resultierende Gewinn beträgt CHF 20'000.", "answer": "falsch", "explanation": "Rechnung: Erlös = 5000 × 10 = 50'000; Kosten = 10'000 + 5000 × 2 = 20'000; Gewinn = 30'000."},

{"question": "1.2 a) Die drei Elemente des 'Magischen Dreiecks des Pricings' sind: kundenorientierte Preise, vergangenheitsorientierte Preise und wettbewerbsorientierte Preise.", "answer": "falsch", "explanation": "Es handelt sich um kunden-, kosten- und wettbewerbsorientierte Preise."},
{"question": "1.2 b) Die Übervorteilungsstrategie im Rahmen der Preispositionierung entspricht einer hohen Qualität zu tiefen Preisen.", "answer": "falsch", "explanation": "Das entspricht der Billigstrategie. Übervorteilung wäre hohe Preise bei niedriger Qualität."},
{"question": "1.2 c) Die Tasty Dürüm AG verkauft im Januar 1000 Stück zu CHF 10 und nach einer Preissenkung im Februar 1500 Stück zu CHF 8. Die daraus abgeleitete Preisabsatzfunktion ist: p(x) = 14 – x/250", "answer": "richtig", "explanation": "Die Funktion ist korrekt, da sie auf den zwei Punkten basiert."},
{"question": "1.2 d) Bei einem Preis von CHF 12 soll die abgesetzte Menge 600 Stück betragen, bei einer Sättigungsmenge von 3’500 Stück und einem Prohibitionspreis von CHF 14.", "answer": "falsch", "explanation": "Die Menge bei CHF 12 beträgt gemäss Funktion x = 500."},

{"question": "1.3 a) Leistungen werden grundsätzlich nach intangibel und tangibel unterschieden.", "answer": "richtig", "explanation": "Diese Einteilung ist korrekt und unterscheidet materielle von immateriellen Leistungen."},
{"question": "1.3 b) Die 'soziale Anerkennung' durch den Kauf eines auffälligen Sportwagens entspricht dem Erbauungsnutzen.", "answer": "richtig", "explanation": "Soziale Anerkennung zählt zum Erbauungsnutzen."},
{"question": "1.3 c) Mit Massnahmen im Rahmen der Leistungspflege soll unter anderem die Wachstums- bzw. Reifephase einer Leistung in dessen Lebenszyklus verlängert werden.", "answer": "richtig", "explanation": "Das ist Ziel der Leistungspflege."},
{"question": "1.3 d) Bei der Leistungsvariation werden bereits im Markt eingeführte Leistungen durch eine Variante ersetzt, bei der bestimmte Eigenschaften oder Leistungsmerkmale verbessert wurden.", "answer": "richtig", "explanation": "Das ist die Definition einer Leistungsvariation."},

{"question": "1.4 a) Diversifikation eines Produktportfolios kann horizontal, vertikal oder lateral erfolgen.", "answer": "richtig", "explanation": "Das sind die drei anerkannten Formen der Diversifikation."},
{"question": "1.4 b) Das Anbieten von Jogurts in verschiedenen Geschmacksrichtungen entspricht dem Konzept einer Produktdifferenzierung.", "answer": "richtig", "explanation": "Verschiedene Geschmacksrichtungen sind typische Produktdifferenzierung."},
{"question": "1.4 c) (Mass-)Customization ist ein Spezialfall der Produktdifferenzierung und erfüllt individuelle Kundenbedürfnisse mittels einer eigenen Variante.", "answer": "richtig", "explanation": "Mass Customization ist eine individuelle Produktdifferenzierung."},
{"question": "1.4 d) Eine Innovation setzt sich schneller durch, wenn ihre Nutzung einfach dargestellt und anderen mitgeteilt werden kann, z.B. mittels Sozialer Medien.", "answer": "richtig", "explanation": "Die Kommunikationsfähigkeit einer Innovation beeinflusst deren Verbreitung positiv."},

{"question": "1.5 a) In der Reifephase des Produktlebenszyklus wird der Wettbewerb schwächer und immer mehr neue Konkurrenten treten in den Markt ein.", "answer": "falsch", "explanation": "In der Reifephase nimmt der Wettbewerb zu, neue Konkurrenten treten eher in der Wachstumsphase ein."},
{"question": "1.5 b) Der Relaunch ist ein Spezialfall der Leistungsdifferenzierung.", "answer": "richtig", "explanation": "Ein Relaunch ist eine Variante einer bestehenden Leistung mit Verbesserungen."},
{"question": "1.5 c) Ein Handelsunternehmen entscheidet sich, anstatt Produkte einzukaufen, diese selbst herzustellen. Das ist eine Form der Diversifikation und nennt sich vertikale Vorwärtsintegration.", "answer": "richtig", "explanation": "Das Unternehmen erweitert seine Wertschöpfungskette nach vorne."},
{"question": "1.5 d) Der generische Innovationsprozess wird in folgende Phasen unterteilt: Ideenphase, Leistungsentwicklung, Markteinführung.", "answer": "richtig", "explanation": "Das sind die drei Hauptphasen im Innovationsprozess."},

{"question": "1.6 a) Preisnachlässe für Senioren sind eine Form der demografischen Preisdifferenzierung.", "answer": "richtig", "explanation": "Demografische Merkmale wie Alter werden zur Preisgestaltung genutzt."},
{"question": "1.6 b) Ziel der Preisdifferenzierung ist es, unterschiedliche Zahlungsbereitschaften abzuschöpfen, um so den Gewinn gegenüber der Einheitspreissetzung zu steigern.", "answer": "richtig", "explanation": "Preisdifferenzierung maximiert den Gewinn durch segmentierte Preisgestaltung."},
{"question": "1.6 c) Man kann durch eine Preiserhöhung keinen Umsatz verlieren.", "answer": "falsch", "explanation": "Preiserhöhungen können zu Nachfragerückgang und damit zu Umsatzeinbußen führen."},
{"question": "1.6 d) Die Penetrationsstrategie zielt darauf ab, mit einem tiefen Preis bei der Markteinführung möglichst viel der Zahlungsbereitschaft der Konsument:innen abzuschöpfen.", "answer": "falsch", "explanation": "Penetration zielt auf schnelle Marktdurchdringung, nicht auf Abschöpfung."},

{"question": "1.7 a) Die Service Profit Chain zeigt die Wirkung zufriedener Kund:innen auf die Zufriedenheit der Investoren.", "answer": "falsch", "explanation": "Sie zeigt die Kette von Mitarbeiterzufriedenheit über Kundenbindung zu Unternehmenserfolg."},
{"question": "1.7 b) «Customer Managed Relationship» bezeichnet den Ansatz, gemäss dem Kund:innen die Beziehung zu Unternehmen selbst bestimmen.", "answer": "richtig", "explanation": "CMR bedeutet, dass Kunden aktiv über Kanäle und Inhalte bestimmen."},
{"question": "1.7 c) «Cross-Selling» bezeichnet den Verkauf eines Upgrades einer Leistung. «Up-Selling» hingegen der Verkauf einer zusätzlichen, dazugehörigen Leistung.", "answer": "falsch", "explanation": "Die Definitionen sind vertauscht: Up-Selling ist ein teureres Produkt, Cross-Selling ein Zusatzprodukt."},
{"question": "1.7 d) «Gebundenheit» bezeichnet die faktische Kundschaftsbindung, welche z.B. durch Verträge erzwungen werden kann. «Verbundenheit» hingegen bezeichnet die emotionale Kundschaftsbindung.", "answer": "richtig", "explanation": "Die Begriffe sind korrekt definiert."},

{"question": "1.8 a) «Fait accompli» im Kündigungsmanagement bedeutet, dass ein Unternehmen eine Kundschaftsbeziehung «versanden» lässt und z.B. keine Newsletter mehr versendet.", "answer": "richtig", "explanation": "Das ist die Definition von 'fait accompli' im Marketing."},
{"question": "1.8 b) Das Beschwerdeparadoxon beschreibt, dass Kunden bei einer Reklamation, die positiv bearbeitet wurde, hinterher zufriedener sind als Kunden, die nichts zu beanstanden hatten.", "answer": "richtig", "explanation": "Das Beschwerdeparadoxon ist ein gut belegter Effekt im Kundenmanagement."},
{"question": "1.8 c) Der Inbound-Marketing-Ansatz umfasst vor allem Printwerbung, Direct Mailings, Call Center und TV-Werbung.", "answer": "falsch", "explanation": "Das sind klassische Outbound-Instrumente."},
{"question": "1.8 d) Die Kundenwertanalyse gibt Auskunft über die wertvollsten Kunden aus Unternehmenssicht, und darauf aufbauend werden die Strategien zu ihrer Rückgewinnung gebildet.", "answer": "richtig", "explanation": "Kundenwertanalyse ist ein Steuerungsinstrument zur Kundenpriorisierung."},

{"question": "1.9 a) Das Ziel des Beschwerdemanagements ist die Rückgewinnung unzufriedener Kunden sowie die Vermeidung künftiger Beschwerden.", "answer": "richtig", "explanation": "Beides sind zentrale Ziele des Beschwerdemanagements."},
{"question": "1.9 b) Beim Kundenbindungsmanagement geht es primär darum, unzufriedene Kunden möglichst schnell zu kündigen.", "answer": "falsch", "explanation": "Das Ziel ist Kundenbindung, nicht Kundenverlust."},
{"question": "1.9 c) Loyalitätsprogramme können emotionale Bindung verstärken, z.B. durch exklusive Vorteile.", "answer": "richtig", "explanation": "Solche Programme fördern emotionale Kundenbindung."},
{"question": "1.9 d) Kundenbindung ist nur durch Verträge möglich.", "answer": "falsch", "explanation": "Auch emotionale und freiwillige Bindung ist möglich."},

{"question": "1.10 a) Das Ziel der Kommunikationspolitik ist es, ein Produkt durch physische Präsenz von der Konkurrenz abzuheben.", "answer": "falsch", "explanation": "Kommunikationspolitik zielt auf Wahrnehmung und Information, nicht auf physische Präsenz."},
{"question": "1.10 b) Der Begriff 'Above-the-Line' umfasst sämtliche klassische Werbung wie TV-Spots oder Plakate.", "answer": "richtig", "explanation": "Above-the-Line bezieht sich auf klassische, breit streuende Werbung."},
{"question": "1.10 c) Werbung, Sponsoring und Verkaufsförderung sind typische Instrumente der Kommunikationspolitik.", "answer": "richtig", "explanation": "Diese drei zählen zu den zentralen Kommunikationsinstrumenten im Marketing."},
{"question": "1.10 d) Der Hauptzweck von Public Relations ist die direkte Verkaufsförderung von Produkten.", "answer": "falsch", "explanation": "Public Relations dient dem Imageaufbau und nicht der direkten Verkaufsförderung."},

{"question": "1.11 a) Im AIDA-Modell steht das 'I' für 'Intelligence'.", "answer": "falsch", "explanation": "Das 'I' steht für 'Interest', also Interesse."},
{"question": "1.11 b) Das AIDA-Modell beschreibt die Phasen, die ein Kunde durchläuft – von der Aufmerksamkeit bis zur Handlung.", "answer": "richtig", "explanation": "Das AIDA-Modell zeigt die vier Phasen: Attention, Interest, Desire, Action."},
{"question": "1.11 c) Die Awareness-Phase im AIDA-Modell steht für die Kaufentscheidung.", "answer": "falsch", "explanation": "Awareness bezieht sich auf Aufmerksamkeit, nicht Entscheidung."},
{"question": "1.11 d) Das Modell berücksichtigt auch Aspekte der Nachkaufphase.", "answer": "falsch", "explanation": "Das klassische AIDA-Modell endet mit dem Kauf und berücksichtigt keine Nachkaufphasen."},

{"question": "1.12 a) Content-Marketing gehört zum Inbound-Marketing.", "answer": "richtig", "explanation": "Content-Marketing ist ein zentrales Instrument im Inbound-Marketing."},
{"question": "1.12 b) Inbound-Marketing umfasst primär Outbound-Maßnahmen wie Callcenter-Aktionen.", "answer": "falsch", "explanation": "Callcenter und Outbound-Aktionen gehören nicht zum Inbound-Ansatz."},
{"question": "1.12 c) Beim Inbound-Marketing werden potenzielle Kunden durch hochwertige Inhalte auf das Unternehmen aufmerksam.", "answer": "richtig", "explanation": "Inbound-Marketing basiert auf Anziehung durch hilfreiche Inhalte."},
{"question": "1.12 d) Klassische Werbung im Fernsehen ist Teil des Inbound-Marketings.", "answer": "falsch", "explanation": "Fernsehwerbung ist klassisches Outbound-Marketing."},

{"question": "1.13 a) Im Rahmen der Customer Journey ist der erste Kontaktpunkt mit einer Marke immer der Kauf.", "answer": "falsch", "explanation": "Die Customer Journey beginnt oft lange vor dem Kauf – z.B. mit Online-Recherche."},
{"question": "1.13 b) Touchpoints sind alle Kontaktpunkte, die ein Kunde mit einer Marke haben kann.", "answer": "richtig", "explanation": "Touchpoints umfassen jede Form von Berührungspunkten – physisch oder digital."},
{"question": "1.13 c) Eine gut gemachte Webseite kann ein positiver Touchpoint in der Customer Journey sein.", "answer": "richtig", "explanation": "Webseiten sind zentrale, häufig erste Touchpoints."},
{"question": "1.13 d) Die Customer Journey endet mit dem Kauf des Produkts.", "answer": "falsch", "explanation": "Die Nachkaufphase, z.B. Kundenservice, gehört auch dazu."},

{"question": "1.14 a) Sponsoring ist eine Maßnahme zur Verkaufsförderung.", "answer": "falsch", "explanation": "Sponsoring ist Teil der Öffentlichkeitsarbeit (Public Relations), nicht Verkaufsförderung."},
{"question": "1.14 b) Verkaufsförderung richtet sich ausschließlich an Endkunden.", "answer": "falsch", "explanation": "Auch Händler oder Außendienstmitarbeitende können Ziel der Verkaufsförderung sein."},
{"question": "1.14 c) Produktproben sind eine typische Maßnahme der Verkaufsförderung.", "answer": "richtig", "explanation": "Produktproben sind gängige Mittel zur Absatzsteigerung."},
{"question": "1.14 d) Verkaufsförderung ist immer langfristig angelegt.", "answer": "falsch", "explanation": "Verkaufsförderung ist in der Regel kurzfristig und aktionsbezogen."},

{"question": "1.15 a) Kommunikationsziele sollen SMART formuliert werden.", "answer": "richtig", "explanation": "SMART steht für spezifisch, messbar, attraktiv, realistisch, terminiert."},
{"question": "1.15 b) Kommunikationsziele sind identisch mit Unternehmenszielen.", "answer": "falsch", "explanation": "Kommunikationsziele leiten sich aus Unternehmenszielen ab, sind aber nicht identisch."},
{"question": "1.15 c) Ein Kommunikationsziel kann z.B. die Steigerung der Markenbekanntheit sein.", "answer": "richtig", "explanation": "Dies ist ein klassisches Kommunikationsziel."},
{"question": "1.15 d) Kommunikationsziele müssen nicht überprüfbar sein.", "answer": "falsch", "explanation": "Ziele sollten stets überprüfbar und messbar sein."},

{"question": "1.16 a) Die Corporate Identity umfasst das visuelle Erscheinungsbild eines Unternehmens.", "answer": "richtig", "explanation": "Dies ist die Corporate Design Komponente der Corporate Identity."},
{"question": "1.16 b) Corporate Behaviour beschreibt das Verhalten eines Unternehmens gegen innen und außen.", "answer": "richtig", "explanation": "Corporate Behaviour umfasst das Verhalten des Unternehmens gegenüber Mitarbeitenden und externen Anspruchsgruppen."},
{"question": "1.16 c) Corporate Communication umfasst nur die externe Kommunikation.", "answer": "falsch", "explanation": "Corporate Communication beinhaltet sowohl interne als auch externe Kommunikation."},
{"question": "1.16 d) Die Corporate Identity ist identisch mit dem Corporate Image.", "answer": "falsch", "explanation": "Corporate Identity ist das Selbstbild, Corporate Image ist das Fremdbild."},

{"question": "1.17 a) Der Marketing-Controlling-Prozess endet mit der Zieldefinition.", "answer": "falsch", "explanation": "Der Prozess beginnt mit der Zieldefinition und endet mit der Kontrolle."},
{"question": "1.17 b) Marketing-Controlling prüft, ob gesetzte Marketingziele erreicht wurden.", "answer": "richtig", "explanation": "Das ist eine zentrale Aufgabe des Marketings-Controllings."},
{"question": "1.17 c) Marketing-Controlling ist ein Bestandteil der strategischen Planung.", "answer": "richtig", "explanation": "Marketing-Controlling unterstützt die strategische und operative Planung."},
{"question": "1.17 d) Marketing-Controlling darf keine operativen Kennzahlen erfassen.", "answer": "falsch", "explanation": "Auch operative Kennzahlen sind Bestandteil des Marketings-Controllings."},

{"question": "1.18 a) Der Net Promoter Score (NPS) misst die Kundenzufriedenheit.", "answer": "falsch", "explanation": "Der NPS misst die Weiterempfehlungsbereitschaft, nicht die Zufriedenheit direkt."},
{"question": "1.18 b) Der NPS ergibt sich aus dem Anteil der Promotoren minus dem Anteil der Detraktoren.", "answer": "richtig", "explanation": "Das ist die übliche Berechnung des NPS."},
{"question": "1.18 c) Ein NPS von 0 bedeutet, dass es gleich viele Promotoren wie Detraktoren gibt.", "answer": "richtig", "explanation": "Ein Gleichstand ergibt einen NPS von 0."},
{"question": "1.18 d) Der NPS wird üblicherweise auf einer Skala von 0 bis 5 gemessen.", "answer": "falsch", "explanation": "Die Skala reicht von 0 bis 10."},

{"question": "1.19 a) Ein hoher Marktanteil ist immer ein Zeichen für hohe Profitabilität.", "answer": "falsch", "explanation": "Ein hoher Marktanteil garantiert nicht automatisch hohe Gewinne."},
{"question": "1.19 b) Marktanteil ist das Verhältnis des Umsatzes eines Unternehmens zum Gesamtumsatz im Markt.", "answer": "richtig", "explanation": "Das entspricht der Definition des Marktanteils."},
{"question": "1.19 c) Der relative Marktanteil misst den Anteil eines Unternehmens im Vergleich zum größten Wettbewerber.", "answer": "richtig", "explanation": "Das ist korrekt definiert."},
{"question": "1.19 d) Der Marktanteil ist keine relevante Kennzahl im Marketing-Controlling.", "answer": "falsch", "explanation": "Marktanteil ist eine zentrale Kennzahl im Marketing-Controlling."}

]

# Streamlit Setup
st.set_page_config(page_title="Marketing Quiz", layout="centered")
st.title("📱 Marketing Quiz")
st.write("Kapitel 1.1 – 1.19 | Entscheide, ob Aussagen richtig oder falsch sind.")

# Session State Initialisierung
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.quiz_done = False
    st.session_state.user_answer = None

# Quiz Logik
if not st.session_state.quiz_done and st.session_state.current < len(st.session_state.shuffled_questions):
    q = st.session_state.shuffled_questions[st.session_state.current]

    if not st.session_state.show_result:
        st.subheader(q["question"])
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Richtig", key="richtig"):
                st.session_state.show_result = True
                st.session_state.user_answer = "richtig"
                if q["answer"] == "richtig":
                    st.session_state.score += 1
        with col2:
            if st.button("❌ Falsch", key="falsch"):
                st.session_state.show_result = True
                st.session_state.user_answer = "falsch"
                if q["answer"] == "falsch":
                    st.session_state.score += 1

    if st.session_state.show_result:
        if st.session_state.user_answer == q["answer"]:
            st.markdown("<div style='background-color:#d4edda;padding:10px;border-radius:8px;'>✅ Deine Antwort war richtig!</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='background-color:#f8d7da;padding:10px;border-radius:8px;'>❌ Deine Antwort war falsch!</div>", unsafe_allow_html=True)

        st.info(f"**Begründung:** {q['explanation']}")

        if st.button("➡️ Nächste Frage", key=f"next_{st.session_state.current}"):
            st.session_state.current += 1
            st.session_state.show_result = False
            st.session_state.user_answer = None
            st.rerun()

# Quiz abgeschlossen
elif not st.session_state.quiz_done:
    st.session_state.quiz_done = True
    st.success(f"✅ Quiz abgeschlossen! Ergebnis: {st.session_state.score}/{len(st.session_state.shuffled_questions)}")
    if st.button("🔁 Quiz neu starten", use_container_width=True):
        for key in ["shuffled_questions", "current", "score", "show_result", "quiz_done", "user_answer"]:
            del st.session_state[key]
