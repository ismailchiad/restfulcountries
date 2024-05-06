import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Accéder à la clé API
api_key = os.getenv("RESTFULCOUNTRIES_API_KEY")

# Utiliser la clé API dans votre application
print("Clé API RESTFULCOUNTRIES:", api_key)
