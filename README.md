# Pick_Your_Cake 🍰

**Pick_Your_Cake** ist eine interaktive Web-App, mit der du Kuchenrezepte verwalten, kombinieren und skalieren kannst.  
Die App ist in Python mit [Streamlit](https://streamlit.io/) entwickelt und ermöglicht es, Rezepte einfach zu erstellen, anzupassen und direkt online zu nutzen – auch auf dem Handy.

---

## 🚀 Funktionen der App

### 1. Rezepte hinzufügen
- Neue Rezepte können über ein Eingabeformular erstellt werden.
- Jede Zutat wird mit **Name**, **Menge** und **Einheit (g, ml, Stk)** eingegeben.
- Zusätzliche Zutaten können über ein **“+”**-Feld hinzugefügt werden.
- Rezepte werden automatisch in `rezepte.json` gespeichert.

### 2. Rezepte kombinieren
- Mehrere Rezepte (z. B. Boden + Creme) können kombiniert werden.
- Die Zutatenmengen werden automatisch **auf die gewünschte Torten-Größe skaliert**.
- Ausgabe erfolgt **untereinander pro Rezept**, nicht als Gesamtliste.
- Perfekt, um z. B. komplette Torten zusammenzustellen.

### 3. Rezepte anzeigen
- Alle gespeicherten Rezepte werden übersichtlich angezeigt.
- Zutaten und Mengen werden klar dargestellt (Menge zuerst, dann Zutat).
- Rezepte werden **mit Namen** hervorgehoben.

### 4. Rezepte löschen
- Einzelne Rezepte können über ein Dropdown-Menü ausgewählt und gelöscht werden.
- Änderungen werden automatisch in `rezepte.json` gespeichert.
- Die UI aktualisiert sich sofort nach dem Löschen.

### 5. Skalierung der Rezepte
- Für kombinierte Rezepte kann die **Tortengröße angepasst** werden.
- Zutaten werden proportional zur Zielgröße umgerechnet.

### Link zur Nutzung:
https://pickyourcake.streamlit.app/

