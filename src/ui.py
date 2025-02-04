import streamlit as st
from calculator import calculate_nutrition
from database import load_food_data, get_food_info_from_api

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

        st.subheader("Vitamines")
        for vitamine, valeur in besoins["vitamines"].items():
            st.write(f"**{vitamine.capitalize()}**: {valeur} mg/µg")

        st.subheader("Minéraux")
        for mineral, valeur in besoins["mineraux"].items():
            st.write(f"**{mineral.capitalize()}**: {valeur} mg/µg")

    st.sidebar.header("Rechercher un aliment")
    food_name = st.sidebar.text_input("Nom de l'aliment", "")

    if food_name:
        food_info = get_food_info_from_api(food_name)
        if food_info:
            st.subheader(f"Informations nutritionnelles pour {food_info['product_name']}")
            st.write(f"**Calories**: {food_info['calories']} kcal")
            st.write(f"**Protéines**: {food_info['protéines']} g")
            st.write(f"**Lipides**: {food_info['lipides']} g")
            st.write(f"**Glucides**: {food_info['glucides']} g")
            st.write(f"**Nutri-Score**: {food_info['nutrition_grades']}")
        else:
            st.write("Aucune information disponible pour cet aliment.")

if __name__ == "__main__":
    display_app()