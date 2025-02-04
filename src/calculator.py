def calculate_nutrition(poids, taille, age, sexe, activite):
    """
    Calcule les besoins en macronutriments et micronutriments en fonction des paramètres de l'utilisateur.
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

    # Ajout des besoins en vitamines et minéraux (exemple)
    vitamines = {
        "vitamine A": 900,  # µg
        "vitamine C": 90,  # mg
        "vitamine D": 20,  # µg
        "vitamine E": 15,  # mg
        "vitamine K": 120,  # µg
        "vitamine B1": 1.2,  # mg
        "vitamine B2": 1.3,  # mg
        "vitamine B3": 16,  # mg
        "vitamine B5": 5,  # mg
        "vitamine B6": 1.3,  # mg
        "vitamine B7": 30,  # µg
        "vitamine B9": 400,  # µg
        "vitamine B12": 2.4  # µg
    }

    mineraux = {
        "calcium": 1000,  # mg
        "fer": 8,  # mg
        "magnésium": 400,  # mg
        "phosphore": 700,  # mg
        "potassium": 4700,  # mg
        "sodium": 1500,  # mg
        "zinc": 11  # mg
    }

    return {
        "calories": round(bmr, 2),
        "protéines": round(protéines, 2),
        "lipides": round(lipides, 2),
        "glucides": round(glucides, 2),
        "vitamines": vitamines,
        "mineraux": mineraux
    }