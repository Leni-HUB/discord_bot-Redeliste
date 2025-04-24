🗣️ Discord Redelisten-Bot
Ein einfacher Discord-Bot zur Verwaltung einer Redeliste bei Besprechungen oder Diskussionen im Discord-Channel. Ideal für organisierte Gespräche, z. B. in Orga-Teams, Arbeitsgruppen oder Online-Meetings.

🔧 Features
!sprechen: Fügt dich zur Redeliste hinzu.

!weristdran: Zeigt die nächste Person auf der Redeliste an.

!redeliste: Gibt die komplette aktuelle Redeliste aus.

!fertig: Entfernt dich von der Redeliste, wenn du an der Reihe warst.

🛠️ Installation
Python installieren (mind. Version 3.8).

Projekt clonen oder Dateien speichern.

Abhängigkeiten installieren:

bash
Kopieren
Bearbeiten
pip install discord.py python-dotenv
.env Datei erstellen im selben Verzeichnis mit folgendem Inhalt:

ini
Kopieren
Bearbeiten
DISCORD_TOKEN=dein_discord_bot_token
Bot starten:

bash
Kopieren
Bearbeiten
python bot.py
⚙️ Verwendung
Der Bot reagiert auf Befehle mit dem Präfix !

Nur der erste Platz auf der Redeliste kann sich selbst mit !fertig entfernen.

Die Redeliste ist sitzungsbasiert (wird bei Neustart zurückgesetzt).

🧠 Beispiel
text
Kopieren
Bearbeiten
UserA: !sprechen
Bot: UserA wurde zur Redeliste hinzugefügt.

UserB: !sprechen
Bot: UserB wurde zur Redeliste hinzugefügt.

UserC: !weristdran
Bot: Die nächste Person auf der Redeliste ist: UserA

UserA: !fertig
Bot: Danke UserA, du wurdest von der Redeliste entfernt.
📄 Lizenz
Dieses Projekt ist unter der MIT-Lizenz veröffentlicht.