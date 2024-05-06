import requests
import json
import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

API_BASE_URL = "https://restfulcountries.com/api/v1"
API_KEY = os.getenv("RESTFULCOUNTRIES_API_KEY")

# Exemple d'utilisation des fonctions
iso2 = "FR"

headers = {
  'Authorization': API_KEY
}

def get_country_info(iso2):
    url = f"{API_BASE_URL}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de la récupération des informations sur le pays.")
        return None

# Récupérer les informations sur le pays
country_info = get_country_info(iso2)
if country_info:
    # Créer un dossier 'data' s'il n'existe pas
    if not os.path.exists('data'):
        os.makedirs('data')

    # Chemin du fichier contenant le compteur
    fichier_compteur = 'data/compteur.txt'

    # Lire le compteur depuis le fichier s'il existe, sinon initialiser à 1
    if os.path.exists(fichier_compteur):
        with open(fichier_compteur, 'r') as f:
            compteur = int(f.read())
    else:
        compteur = 1

    # Nom du fichier JSON avec un numéro séquentiel
    nom_fichier = f"data/country_info_{compteur}.json"

    # Incrémenter le compteur pour la prochaine exécution
    compteur += 1

    # Écrire les informations dans un fichier JSON dans le dossier 'data'
    with open(nom_fichier, 'w') as file:
        json.dump(country_info, file, indent=4)

    # Enregistrer le compteur dans le fichier
    with open(fichier_compteur, 'w') as f:
        f.write(str(compteur))

    print(f"Les informations sur le pays ont été enregistrées dans {nom_fichier}")
