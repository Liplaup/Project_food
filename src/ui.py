import streamlit as st
from calculator import calculate_nutrition
from database import load_food_data

def display_app():
    st.title("Calcul des besoins nutritionnels")

    st.sidebar.header("Informations personnelles")
    poids = st.sidebar.number_input("Poids (kg)", min_value=20, max_value=200, value=70)
    taille = st.sidebar.number_input("Taille (cm)", min_value=100, max_value=250, value=175)
    age = st.sidebar.number_input("Âge", min_value=18, max_value=120, value=25)
    sexe = st.sidebar.selectbox("Sexe", ["Homme", "Femme"])
    activite = st.sidebar.selectbox("Niveau d'activité", ["Faible", "Modéré", "Intense"])

    if st.sidebar.button("Calculer"):
        sexe = "h" if sexe == "Homme" else "f"
        activite = activite.lower()

        besoins = calculate_nutrition(poids, taille, age, sexe, activite)

        st.subheader("Résultats")
        st.write(f"**Calories journalières**: {besoins['calories']} kcal")
        st.write(f"**Protéines**: {besoins['protéines']} g")
        st.write(f"**Lipides**: {besoins['lipides']} g")
        st.write(f"**Glucides**: {besoins['glucides']} g")

    # Charger les aliments à partir de la base de données
    food_data = load_food_data()

    st.sidebar.header("Sélectionner un aliment")
    food_list = list(food_data.keys())
    selected_food = st.sidebar.selectbox("Choisissez un aliment", food_list)

    if selected_food:
        food_info = food_data[selected_food]
        st.subheader(f"Informations nutritionnelles pour {selected_food}")
        st.write(f"**Calories**: {food_info['calories']} kcal")
        st.write(f"**Protéines**: {food_info['protéines']} g")
        st.write(f"**Lipides**: {food_info['lipides']} g")
        st.write(f"**Glucides**: {food_info['glucides']} g")

if __name__ == "__main__":
    display_app()
