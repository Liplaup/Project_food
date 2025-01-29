def calculate_nutrition(poids, taille, age, sexe, activite):
    """
    Calcule les besoins en macronutriments en fonction des paramètres de l'utilisateur.
    """
    # Estimation du métabolisme basal (Harris-Benedict)
    if sexe == "h":
        bmr = 88.36 + (13.4 * poids) + (4.8 * taille) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * poids) + (3.1 * taille) - (4.3 * age)
    
    # Facteur d'activité
    facteurs = {"faible": 1.2, "modéré": 1.55, "intense": 1.9}
    bmr *= facteurs.get(activite, 1.2)

    # Répartition des macronutriments (exemple)
    protéines = poids * 1.5  # 1.5g par kg de poids
    lipides = poids * 0.8  # 0.8g par kg
    glucides = (bmr - (protéines * 4 + lipides * 9)) / 4  # Le reste en glucides

    return {"calories": round(bmr, 2), "protéines": round(protéines, 2), "lipides": round(lipides, 2), "glucides": round(glucides, 2)}
