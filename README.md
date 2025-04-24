🗣️ Discord Redelisten-Bot
Ein einfacher, aber effektiver Discord-Bot zur Verwaltung von Redelisten – perfekt für strukturierte Online-Diskussionen, Besprechungen oder Unterricht in Discord-Sprachkanälen.

🚀 Features
✅ Redeliste beitreten mit !sprechen

👀 Nächste Person anzeigen mit !weristdran

📋 Aktuelle Redeliste anzeigen mit !redeliste

✅ Fertig sprechen & von Liste entfernen mit !fertig (nur wer dran ist)

🔐 Nutzt .env zur sicheren Token-Verwaltung

🛠️ Installation
1. Voraussetzungen
Python 3.8 oder neuer

Discord Bot-Token (erstellbar unter Discord Developer Portal)

2. Setup
bash
Kopieren
Bearbeiten
git clone https://github.com/dein-name/redelisten-bot.git
cd redelisten-bot
pip install -r requirements.txt
Falls keine requirements.txt vorhanden ist:

bash
Kopieren
Bearbeiten
pip install discord.py python-dotenv
3. .env Datei anlegen
Erstelle im Projektverzeichnis eine .env Datei mit folgendem Inhalt:

ini
Kopieren
Bearbeiten
DISCORD_TOKEN=DEIN_DISCORD_BOT_TOKEN_HIER
▶️ Starten
bash
Kopieren
Bearbeiten
python bot.py
💬 Befehle im Überblick

Befehl	Beschreibung
!sprechen	Fügt dich zur Redeliste hinzu
!weristdran	Zeigt die nächste Person auf der Liste an
!redeliste	Gibt die vollständige Redeliste zurück
!fertig	Entfernt dich von der Liste, wenn du gerade dran bist
📦 Beispielausgabe
txt
Kopieren
Bearbeiten
🗣️ Aktuelle Redeliste:
1. UserA
2. UserB
3. UserC

UserA: !fertig
Bot: Danke UserA, du wurdest von der Redeliste entfernt.
💡 Erweiterungsideen
📦 Speicherung der Redeliste in einer Datei oder Datenbank

⏱️ Timer für Sprechzeit pro Person

🔒 Rollenbasierte Berechtigungen

🌐 Web-Dashboard zur Verwaltung

📄 Lizenz
MIT License – frei nutzbar & anpassbar. ❤️
