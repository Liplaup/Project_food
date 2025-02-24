import json
import requests

def load_food_data(filename=r"data/food_db.json"):
    """Charge la base de données des aliments."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_food_data(data, filename=r"data/food_db.json"):
    """Sauvegarde les aliments dans un fichier JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def get_food_info_from_api(food_name):
    """Recherche un aliment par son nom et récupère ses informations nutritionnelles."""
    search_url = f"https://world.openfoodfacts.org/api/v2/search"
    
    # Recherche d'aliment par nom (en anglais ou dans les autres langues)
    params = {
        'search_terms': food_name,  # Nom de l'aliment
        'page_size': 1,  # Limiter la recherche à un seul produit pour simplifier
        'fields': 'code,product_name,nutriments,nutrition_grades'  # Champs que nous souhaitons récupérer
    }
    
    response = requests.get(search_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # Si des produits sont trouvés, récupérons les données
        if data['count'] > 0:
            product = data['products'][0]
            nutriments = product.get('nutriments', {})
            
            return {
                "product_name": product['product_name'],
                "calories": nutriments.get("energy-kcal_100g", "Non disponible"),
                "protéines": nutriments.get("proteins_100g", "Non disponible"),
                "lipides": nutriments.get("fat_100g", "Non disponible"),
                "glucides": nutriments.get("carbohydrates_100g", "Non disponible"),
                "nutrition_grades": product.get('nutrition_grades', 'Non disponible')
            }
    return None

import myfitnesspal

def get_food_info_from_myfitnesspal(food_name):
    """Recherche un aliment par son nom et récupère ses informations nutritionnelles depuis MyFitnessPal."""
    client = myfitnesspal.Client('your_username', 'your_password')
    food = client.get_food_search_results(food_name)
    
    if food:
        food_item = food[0]  # Prenons le premier résultat pour simplifier
        return {
            "product_name": food_item.name,
            "calories": food_item.calories,
            "protéines": food_item.protein,
            "lipides": food_item.fat,
            "glucides": food_item.carbohydrates,
            "nutrition_grades": "Non disponible"  # MyFitnessPal ne fournit pas de Nutri-Score
        }
    return None