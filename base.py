import requests
import json

# à faire : 
# .env 
# .gitignore 
# test 


url = "https://restfulcountries.com/api/v1"

payload = {}
headers = {
  'Authorization': 'Bearer 665|4J4DpCZIAIqnYlAGapManfGf2uOEuBRGc94yEs58'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Vérifiez si la requête a réussi (code 200)
if response.status_code == 200:
    # Convertissez la réponse en format JSON
    json_response = response.json()
    # Enregistrez la réponse JSON dans un fichier avec une meilleure mise en forme
    with open('response.json', 'w') as file:
        json.dump(json_response, file, indent=4)
    print("La réponse a été enregistrée dans response.json")
else:
    print("Erreur lors de la requête : ", response.status_code)
