from utils.storage import load_rezepte, save_rezepte

rezepte = load_rezepte()

print("Rezepte geladen:")
neues_rezept = {
    "name": "Vanillecreme",
    "kategorie": "Creme",
    "groesse": 20,
    "zutaten": {"Milch (ml)": 500, "Zucker (g)": 100, "Vanillepuddingpulver (g)": 40}
}

import streamlit as st
from utils.storage import load_rezepte, save_rezepte
from utils.converter import umrechnen
from utils.converter import kombiniere_rezepte


st.title("🎂 Pick Your Cake – Rezepte kombinieren")

# --------------------------
# Neues Rezept hinzufügen
# --------------------------
st.subheader("🆕 Neues Rezept hinzufügen")

name = st.text_input("Rezeptname (z. B. Schokokuchen und Erdbeercreme)")
kategorie = st.text_input("Kategorie (z. B. 'Boden' oder 'Creme')")
groesse = st.number_input("Rezeptgröße (cm)", min_value=1, step=1)

# Zutaten-Felder dynamisch verwalten
if "zutaten" not in st.session_state:
    st.session_state.zutaten = [{"name": "", "einheit": "g", "menge": 0.0}]

st.markdown("### Zutaten eingeben")

# Zutatenzeilen anzeigen
for i, zutat in enumerate(st.session_state.zutaten):
    cols = st.columns([2, 1, 1, 0.3])
    with cols[0]:
        zutat["name"] = st.text_input(f"Zutat {i+1}", value=zutat["name"], key=f"zutat_name_{i}")
    with cols[1]:
        zutat["einheit"] = st.selectbox(
            "Einheit", ["g", "ml", "Stk","EL","TL"], index=["g", "ml", "Stk","EL","TL"].index(zutat["einheit"]), key=f"zutat_einheit_{i}"
        )
    with cols[2]:
        zutat["menge"] = st.number_input("Menge", min_value=0.0, value=float(zutat["menge"]), step=1.0, key=f"zutat_menge_{i}")
    with cols[3]:
        if st.button("❌", key=f"delete_{i}"):
            st.session_state.zutaten.pop(i)
            st.rerun()

# Zutat hinzufügen
if st.button("+ Zutat hinzufügen"):
    st.session_state.zutaten.append({"name": "", "einheit": "g", "menge": 0.0})
    st.rerun()

# Rezept speichern
if st.button("💾 Rezept speichern"):
    if not name:
        st.warning("Bitte einen Rezeptnamen eingeben!")
    else:
        zutaten_dict = {}
        for z in st.session_state.zutaten:
            if z["name"]:
                # Zutat als Kombination von Einheit und Menge speichern
                zutaten_dict[z["name"]] = f"{z['menge']} {z['einheit']}"

        neues_rezept = {
            "name": name.strip(),
            "kategorie": kategorie.strip(),
            "groesse": groesse,
            "zutaten": zutaten_dict
        }

        if not any(r["name"].lower() == neues_rezept["name"].lower() for r in rezepte):
            rezepte.append(neues_rezept)
            save_rezepte(rezepte)
            st.success(f"Rezept '{name}' wurde hinzugefügt!")
            st.session_state.zutaten = [{"name": "", "einheit": "g", "menge": 0.0}]  # reset
        else:
            st.warning(f"Rezept '{name}' existiert bereits!")

# --------------------------
# Rezepte kombinieren & umrechnen
# --------------------------
st.subheader("🧮 Rezepte kombinieren & umrechnen")

if rezepte:
    auswahl = st.multiselect(
        "Wähle Rezepte zum Kombinieren:",
        options=[r["name"] for r in rezepte],
    )

    ziel_groesse = st.number_input("Zielgröße (cm)", min_value=1, step=1, value=26)

    if st.button("Rezepte berechnen"):
        if not auswahl:
            st.warning("Bitte wähle mindestens ein Rezept aus.")
        else:
            st.markdown("## 🍰 Kombinierte Rezepte")
            for rezept_name in auswahl:
                r = next(r for r in rezepte if r["name"] == rezept_name)
                faktor = (ziel_groesse / r["groesse"]) ** 2
                st.markdown(f"### {r['name']} ({ziel_groesse} cm)")
                st.write(f"**Kategorie:** {r['kategorie']}")
                st.write("**Zutaten:**")

                for zutat, menge in r["zutaten"].items():
                    # Extrahiere Zahl und Einheit
                    try:
                        menge_wert, einheit = menge.split(" ")
                        menge_wert = float(menge_wert)
                        umgerechnet = round(menge_wert * faktor, 1)
                        st.write(f"- {umgerechnet} {einheit} {zutat}")
                    except Exception:
                        st.write(f"- {menge} {zutat}")
                st.divider()
else:
    st.info("Noch keine Rezepte vorhanden. Füge zuerst welche hinzu.")
