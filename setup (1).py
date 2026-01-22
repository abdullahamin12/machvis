import pandas as pd
import os

# Your Raw Text
raw_text = """
"Öffnen Sie das Ventil zum Vorratsbehälter."
"Verbinden Sie die Schläuche des Klimagerätes mit den hochdruck- und niederdruckseitigen Anschlüssen des Fahrzeugs."
"Schalten Sie das Klimagerät ein. In dieser Phase fließt das Kühlmittel aus dem Auto in das Servicegerät, um es zurückzugewinnen und eventuell wiederzuverwerten."
"Achten Sie am Ende des Rückgewinnungsprozesses darauf, dass das Manometer einen Wert unter Null (Unterdruck) anzeigt – das ist der Hinweis, dass das gesamte Kühlmittel aus dem System entfernt ist."
"Trennen Sie mit zwei Schraubenschlüsseln die Kühlschläuche, um Zugang zum Stutzen zu bekommen. Entfernen Sie ihn."
"Installieren Sie einen neuen Gewindeanschluss."
"Stellen Sie den Timer am Klimagerät zum Evakuieren auf mindestens 30 min ein. Durch die Evakuierung wird dem System jegliche Feuchtigkeit entzogen."
"Während der Evakuierung sollte ein vorgeschriebener Wert an Unterdruck am Manometer vorhanden sein."
"Während der Entnahmephase sollte die Menge des „alten"" Kühlmittels gemessen werden. Dieselbe Menge an „frischem"" Kühlmittel sollte wieder zugeführt werden."
"Stellen Sie am Gerät die Menge Kühlmittel ein, die nachgefüllt werden soll."
"Kontrollieren Sie nach dem Wiederbefüllen die Ausströmtemperatur der Luft (an den Düsen im Innenraum). Sie sollte zwischen 2° und 7°C liegen."
"Um geringfügige Schäden aus einer Aluminiumhaube zu entfernen, richten Sie sich nach den folgenden Anweisungen:"
"Untersuchen Sie die Oberfläche der Haube auf Dellen und Beulen."
"Entfernen bzw. befestigen Sie die Dämmwolle, die Scheibenreinigungsschläuche, Lampen und anderen Teile, um den Zugang zu ermöglichen oder weitere Schäden zu verhindern."
"Entfernen Sie die Haube und stellen Sie sie auf eine Ablage, wenn dies die Reparatur erleichtert."
"Reparieren Sie die Dellen und verbeulten Bereiche mit Hilfe von Aluminiumreparaturwerkzeugen und Wärmebehandlungsverfahren."
"Ersetzen Sie die Muttern der Haubenbefestigung oder bohren Sie erforderlichenfalls Löcher."
"Verwenden Sie Füllerspachtel, wenn erforderlich. Für die meisten Spachtelanwendungen muss der auszubessernde Bereich innerhalb von 3 mm seiner Originalkontur liegen. Folgen Sie den Empfehlungen des Spachtelherstellers. Stellen Sie sicher, dass die verwendete Spachtelmasse mit Aluminium kompatibel ist. Einige Fahrzeug- und Produkthersteller empfehlen die Verwendung einer 2-Komponenten-Epoxid-Grundierung vor dem Anwenden der Spachtelmasse auf Aluminium."
"Verwenden Sie eine Anti-Rost-Grundierung für alle innen- und außenliegenden Oberflächen sowie alle anderen Bereiche, die durch Unfall oder Reparatur beschädigt wurden."
"Ersetzen Sie jedes Teil Dämmstoff zwischen dem Rahmen und der Außenhaut, wenn es während der Reparatur beschädigt oder entfernt wurde."
"Führen Sie den Korrosionsschutz an innenliegenden Oberflächen durch."
"Arbeiten Sie Bereiche nach, die vom Zusammenstoß, den Reparatur oder dem Verankern beschädigt wurden, um das Erscheinungsbild wieder herzustellen."
"Setzen Sie den Wiederzusammenbau fort."
"Führen Sie eine kosmetische Oberflächen-Nacharbeitung durch, nachdem alle Karosseriearbeiten erledigt sind."
"Entfernen Sie den Zündkerzenstecker."
"Stecken Sie den Zündkerzenschlüssel über die Zündkerze."
"Drehen Sie die Kerze gegen den Uhrzeigersinn heraus, bis sie lose ist."
"Nehmen Sie die Kerze aus der Stecknuss."
"Untersuchen Sie den Spalt (Elektrodenabstand) und vergewissern Sie sich, dass er sauber ist."
"Führen Sie die Fühlerlehre in den Spalt (Elektrodenabstand)."
"Kontrollieren Sie, ob der Spalt (Elektrodenabstand) zwischen 0,65 und 1,00 mm liegt."
"Stecken Sie die Kerze in die Stecknuss."
"Drehen Sie die Kerze im Uhrzeigersinn herein, bis sie handfest ist."
"Stecken Sie den Zündkerzenschlüssel über die Zündkerze und ziehen Sie die Kerze mit einer Viertel-Drehung im Uhrzeigersinn an."
"ACHTUNG: Die Kerze nicht überdrehen."
"Den Kerzenstecker wieder aufstecken."
"Reinigen Sie ihre Hände, bevor Sie eine Kupplungsscheibe einbauen. Halten Sie die Scheibe so an den Kanten, wie Sie auch ein Foto halten. Kupplungsscheiben haben häufig Fettspuren durch achtlose Handhabung."
"Es wird ein dünner Fettfilm bzw. Antihaftmittel auf die Verzahnung der Eingangswelle aufgetragen. Wird zu viel Fett aufgetragen, so kann es herausdrücken und auf die Reibbeläge tropfen. Selbst die geringste Menge Fett auf den Reibbelägen verursacht ein Klappern der Kupplung."
"Beachten Sie die richtige Einbaurichtung. Auf der Scheibe sollte eine Markierung / Aufschrift „Schwungscheibenseite"" sein. Im Zweifel lesen Sie bitte im Reparaturleitfaden nach."
"Befestigen Sie die Scheibe und den Kupplungsdeckel an der Schwungscheibe."
"Richten Sie Schwungscheibe und Kupplungsdeckel nach den Kerbmarkierungen aus, wenn Sie die Teile wiederverwenden."
"Verwenden Sie einen speziellen Kupplungszentrierdorn, oder eine alte Getriebeeingangswelle, um die Kupplungsscheibe zu zentrieren."
"Es gibt verschiedene Größen von Verzahnungen und Führungen. Universelle Zentrierwerkzeuge werden ebenfalls angeboten."
"Ziehen Sie, mit dem Zentrierdorn in der Scheibe, alle Deckelschrauben handfest an."
"Um jegliches Verdrehen der Druckplatte zu vermeiden, ziehen Sie die Schrauben nach der Kreuz-und-Quer-Methode an."
"Drehen Sie jede Schraube bei jedem Mal nur eine halbe Umdrehung. Sind alle Schrauben fest, dann ziehen sie kreuzweise mit dem entsprechenden Drehmoment an."
"Unterlagen für Hebebühnen werden häufig für Pickups, Großraumfahrzeuge und Geländewagen benötigt."
"Ein Gewindeschneider (Windeisen) wird verwendet, um ein Gewinde auf einer Stange zu schneiden."
"Metallsäge: Die Zähne des Sägeblattes sollten vom Griff weg zeigen."
"Innengewindeschneider werden im Allgemeinen zum „Nachschneiden"" und Reinigen von bestehenden Gewinden verwendet."
"Halten Sie alle Handwerkzeuge sauber, damit diese nicht rosten und man damit einen guten, festen Griff hat."
"Werkzeuge niemals größer Wärme aussetzen."
"Werkzeuge, die beschädigt oder schadhaft sind, sind zu ersetzen."
"Niemals mit einem Hammer auf den Griff von Schraubenschlüsseln oder „Ratschen"" schlagen."
"Bremstrommel: Nicht ausblasen."
"Brennbar – kein offenes Feuer. Von offenem Feuer fernhalten."
"Schließen Sie immer einen Abgasschlauch an das Auspuffrohr an, wenn Sie den Motor eines Fahrzeugs im Gebäude laufen lassen."
"Vorsicht ist geboten."
"Vermeiden Sie den Hautkontakt mit Bremsflüssigkeit."
"Tragen Sie immer eine Schutzbrille."
"Das Fahrzeug auf den Boden herunterlassen."
"Das Fahrzeug anheben (Hebebühne)."
"Die Schrauben lösen."
"Den Motor abstellen."
"Den Motor anlassen."
"Lösen Sie den Luftfilterdeckel und nehmen Sie den Luftfiltereinsatz heraus."
"Alle verschlissenen und defekten Teile erneuern."
"Den Motor auf Betriebstemperatur bringen. Den Vorgang wiederholen."
"Die Schrauben handfest anziehen."
"Den Vorratsbehälter für die Bremsflüssigkeit nicht überfüllen."
"Beachten Sie den empfohlenen Reifenluftdruck auf dem Aufkleber."
"Ziehen Sie die Handbremse an."
"Falls vorhanden: Nehmen Sie die Radkappen ab. Entfernen Sie die Radkappe mit dem Schraubendreher."
"Lösen Sie die Radschrauben/Radmuttern, aber schrauben Sie sie nicht komplett heraus."
"Finden Sie den korrekten Hebepunkt."
"Heben Sie das Fahrzeug an."
"Schrauben Sie die Radschrauben/Radmuttern heraus und nehmen Sie das Rad vom Fahrzeug."
"Setzen Sie das neue Rad auf. Häufig findet man das Reserverad unter der Abdeckung auf dem Boden des Kofferraums."
"Setzen Sie die Radschrauben/Radmuttern an/auf, aber ziehen Sie sie nur handfest an."
"Lassen Sie das Auto herunter und schrauben Sie, mit den Schrauben auf dem Boden, die Radschrauben/Radmuttern mit dem Radkreuz/Drehmomentschlüssel fest."
"Entfernen Sie den Wagenheber."
"Montieren Sie die Radkappe wieder so, dass das Luftventil zugänglich ist."
"Kontrollieren Sie abschließend den Luftdruck und pumpen/lassen Sie den Reifen auf den empfohlenen Druck auf/ab."
"Entfernen Sie nach vorsichtigem Anheben des Fahrzeugs die Räder. Um das Lösen des Entlüftungsventils zu erleichtern, klopfen Sie an der Stelle des Ventils leicht auf den Bremssattel."
"Häufig ist auch ein leichter Schlag auf den Kopf des Ventils nötig, um den „Konus am Sitz des Ventils zu knacken."
"Versuchen Sie vor dem Lösen des Entlüftungsventils zuerst das Ventil etwas festzuziehen. Wiederholen Sie es: Das hilft, das Ventil zu lösen."
"Das Entlüftungsventil sollte sich nun lösen lassen, ohne abzubrechen."
"Bei geöffnetem Ventil drücken Sie ein Stemeisen oder einen Schraubenzieher gegen die Belaginnenseite, um den Bremskolben im Bremszylinder zurückzudrängen, damit Freiraum entsteht, den Bremssattel zu entfernen."
"Ein Spannbügel kann ebenfalls zum Zurückdrücken des Kolbens verwendet werden. Stellen Sie sicher, dass das Entlüftungsventil offen ist, um zu verhindern, dass alte Bremsflüssigkeit in die ABS-Hydraulikeinheit und/oder den Hauptbremszylinder zurückgepresst wird."
"Nachdem der Radbremskolben zurück in seine Ausgangsstellung gedrückt worden ist, können die Bremssattel-Führungsstifte entfernt werden."
"Es kann notwendig sein, einen Schraubenzieher oder ähnliches Hebelwerkzeug zu verwenden, um den Bremssattel aus seiner Halterung zu nehmen."
"Drehen Sie nun den kompletten Bremssattel vor die Bremsscheibe."
"Hängen Sie den Bremssattel an einen Draht auf. Diese Unterstützung/Maßnahme ist notwendig, um Schäden an den flexiblen Bremsleitungen zu verhindern, die auftreten könnten, wenn der Bremssattel an den Schläuchen hängen würde."
"Verwenden Sie eine Bügel-Messschraube und messen Sie die Belagstärke. Bearbeiten Sie den Bremsscheibenbelag oder ersetzen Sie die Bremsscheibe, wenn nötig."
"Entfernen Sie die Scheibenbremsbeläge."
"Wenn notwendig, öffnen Sie das Entlüftungsventil und verwenden Sie die C-Spannvorrichtung, um den Bremskolben ganz in den Radbremszylinder zu drücken."
"Verwenden Sie während des Wiederzusammenbaus Silikon-Bremsfett, um alle Teile zu schmieren, die sowohl Gummi als auch Metall enthalten, genau wie der Führungsstift (des Bremssattels)."
"Reinigen Sie die Gleitflächen/Führungsschienen des Bremssattels gründlich."
"Verwenden Sie eine Dämpfungspaste auf der Rückseite der Beläge, insbesondere, wenn sie nicht mit geräuschdämpfenden Zwischenplatten/Unterlegblechen ausgerüstet sind."
"Bauen Sie die Beläge wieder ein. Achten Sie darauf, dass Sie alle Federklammern und Geräuschdämmplatten wieder einbauen, und arbeiten Sie gewissenhaft."
"Installieren Sie den Bremssattel und schrauben Sie die Führungsstifte nach Herstellervorschriften an. Achten Sie darauf, das Bremspedal mehrmals niederzudrücken, bevor Sie die Testfahrt durchführen."
"Der Fahrer stellte fest, dass die Warnanzeige im Armaturenfeld einen ständigen Fehler am Rücklicht anzeigte."
"Die Sichtkontrolle am Fahrzeug ergibt, dass ein Rücklicht nicht leuchtet. Entfernen Sie die Plastikabdeckung: Die (Rück-) Lichteinheit ist nun zugänglich."
"Die Lampenfassung wird durch sachtes Drehen gegen den Uhrzeigersinn aus der Halterung herausgenommen."
"Die neue Ersatzlampe wird vor dem Einbau in das Fahrzeug mit einem Ohmmeter geprüft, um sicherzugehen, dass sie funktioniert."
"Die Ersatzlampe wird wieder in die Fassung eingesetzt und das Licht wird eingeschaltet, um die einwandfreie Funktion zu prüfen, bevor man alle Komponenten wieder zusammenbaut."
"Überprüfen Sie am Ende die Kontrolllampe in der Armaturentafel. Sie sollte nach dem Einbau erloschen sein."
"""

# 1. Process the text
lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
cleaned_lines = []
for line in lines:
    # Remove outer quotes if present
    if line.startswith('"') and line.endswith('"'):
        line = line[1:-1]
    cleaned_lines.append(line)

# 2. Create the Clean DataFrame
df = pd.DataFrame({
    'ID': range(1, len(cleaned_lines) + 1),
    'German_Text': cleaned_lines
})

# 3. Save to the correct location
output_path = "data/input_german.csv"
if not os.path.exists("data"):
    os.makedirs("data")
    
df.to_csv(output_path, index=False)
print(f"[SUCCESS] Prepared {len(df)} rows of data.")
print(f"Saved to: {output_path}")

# 4. Cleanup old results (to start fresh)
if os.path.exists("data/output_results.csv"):
    os.remove("data/output_results.csv")
    print("[RESET] Cleared previous results file.")