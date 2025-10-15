def umrechnen(zutaten: dict, original: int, neu: int) -> dict:
    """
    Rechnet die Zutatenmengen anhand der Tortengröße um.
    
    :param zutaten: Dictionary mit Zutaten und Mengen
    :param original: Originalgröße laut Rezept (z. B. 20)
    :param neu: gewünschte Tortengröße (z. B. 26)
    :return: neues Dictionary mit angepassten Mengen
    """

    # Umrechnungsfaktoren aus der Tabelle (gerundet)
    faktoren = {
        12: {12:1, 14:1.36, 16:1.77, 18:2.25, 20:2.77, 22:3.36, 24:4.00, 26:4.69, 28:5.44, 30:6.25, 32:7.11},
        14: {12:0.73, 14:1, 16:1.31, 18:1.65, 20:2.04, 22:2.47, 24:2.94, 26:3.54, 28:4.00, 30:4.59, 32:5.22},
        16: {12:0.56, 14:0.77, 16:1, 18:1.27, 20:1.56, 22:1.89, 24:2.25, 26:2.64, 28:3.06, 30:3.52, 32:4.00},
        18: {12:0.44, 14:0.60, 16:0.79, 18:1, 20:1.23, 22:1.49, 24:1.78, 26:2.09, 28:2.42, 30:2.78, 32:3.16},
        20: {12:0.35, 14:0.49, 16:0.64, 18:0.81, 20:1, 22:1.21, 24:1.44, 26:1.69, 28:1.96, 30:2.25, 32:2.56},
        22: {12:0.29, 14:0.40, 16:0.53, 18:0.67, 20:0.83, 22:1, 24:1.19, 26:1.40, 28:1.62, 30:1.86, 32:2.12},
        24: {12:0.24, 14:0.34, 16:0.44, 18:0.56, 20:0.69, 22:0.84, 24:1, 26:1.17, 28:1.36, 30:1.56, 32:1.78},
        26: {12:0.21, 14:0.29, 16:0.38, 18:0.48, 20:0.59, 22:0.72, 24:0.85, 26:1, 28:1.16, 30:1.33, 32:1.51},
        28: {12:0.18, 14:0.25, 16:0.33, 18:0.41, 20:0.51, 22:0.62, 24:0.73, 26:0.86, 28:1, 30:1.15, 32:1.31},
        30: {12:0.15, 14:0.22, 16:0.28, 18:0.36, 20:0.44, 22:0.54, 24:0.64, 26:0.75, 28:0.87, 30:1, 32:1.14},
        32: {12:0.14, 14:0.19, 16:0.25, 18:0.32, 20:0.39, 22:0.47, 24:0.56, 26:0.66, 28:0.77, 30:0.88, 32:1}
    }

    if original not in faktoren or neu not in faktoren[original]:
        raise ValueError("Ungültige Tortengröße! Verfügbare Größen: 12,14,16,18,20,22,24,26,28,30,32")

    faktor = faktoren[original][neu]

    # Neue Zutaten berechnen
    neue_zutaten = {zutat: round(menge * faktor, 2) for zutat, menge in zutaten.items()}

    print(f"Umrechnungsfaktor von {original} cm auf {neu} cm = {faktor}")
    return neue_zutaten

def kombiniere_rezepte(rezept_liste, neue_groesse):
    kombi = {}
    for rezept in rezept_liste:
        umgerechnet = umrechnen(rezept["zutaten"], rezept["groesse"], neue_groesse)
        for zutat, menge in umgerechnet.items():
            kombi[zutat] = kombi.get(zutat, 0) + menge
    return kombi

def loesche_rezept(rezepte, name):
    """
    Löscht ein Rezept mit dem angegebenen Namen aus der Rezepte-Liste.
    Gibt True zurück, wenn ein Rezept gelöscht wurde, sonst False.
    """
    for i, r in enumerate(rezepte):
        if r["name"].lower() == name.lower():  # Name nicht case-sensitive
            del rezepte[i]
            return True
    return False