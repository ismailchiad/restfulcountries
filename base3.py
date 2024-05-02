import requests
import json

API_BASE_URL = "https://restfulcountries.com/api/v1"
API_KEY = 'Bearer 665|4J4DpCZIAIqnYlAGapManfGf2uOEuBRGc94yEs58'

payload = {}
headers = {
  'Authorization': API_KEY
}

def get_country_info(iso2):
    url = f"{API_BASE_URL/{iso2}}"
    response = requests.get(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de la récupération des informations sur le pays.")
        return None

# Exemple d'utilisation des fonctions
iso2 = "FR"

# Récupérer les informations sur le pays
country_info = get_country_info(iso2)
if country_info:
    with open('country_info.json', 'w') as file:
        json.dump(country_info, file, indent=4)
    print("Les informations sur le pays ont été enregistrées dans country_info.json")