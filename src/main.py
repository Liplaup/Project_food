from calculator import calculate_nutrition
from database import load_food_data

def main():
    print("Bienvenue dans l'application de calcul des besoins nutritionnels !")
    
    poids = float(input("Entrez votre poids (kg) : "))
    taille = float(input("Entrez votre taille (cm) : "))
    age = int(input("Entrez votre âge : "))
    sexe = input("Entrez votre sexe (H/F) : ").strip().lower()
    activite = input("Niveau d'activité (faible, modéré, intense) : ").strip().lower()

    besoins = calculate_nutrition(poids, taille, age, sexe, activite)
    print("\nVoici vos besoins nutritionnels journaliers :")
    for key, value in besoins.items():
        if key in ["vitamines", "mineraux"]:
            print(f"\n{key.capitalize()} :")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key.capitalize()} : {sub_value} mg/µg")
        else:
            print(f"{key.capitalize()} : {value} g")

if __name__ == "__main__":
    main()