import json

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
