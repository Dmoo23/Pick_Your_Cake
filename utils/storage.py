import os
import json


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATEI = os.path.join(BASE_DIR, "Rezepte.json")
def load_rezepte():
    if os.path.exists(DATEI):
        with open(DATEI, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    # falls nicht vorhanden, initial leere Datei erzeugen
    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)
    return []

def save_rezepte(rezepte):
    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(rezepte, f, indent=4, ensure_ascii=False)
