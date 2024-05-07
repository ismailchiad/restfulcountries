import random
import json

CATEGORY = ['capital', 'population']
# Charger les données des pays depuis le fichier JSON
def charger_donnees_pays():
    with open('data/country_info.json', 'r') as file:
        return json.load(file)

# Charger les données des pays depuis le fichier JSON
donnees_pays = charger_donnees_pays()

# Sélectionner une question aléatoire et obtenir la réponse
def poser_question(donnees_pays):
    pays = random.choice(donnees_pays['data'])  # Accéder à la liste des pays
    question = f"Quelle est la capitale de {pays['name']} ?"
    reponse_correcte = pays['capital']
    return question, reponse_correcte

# Poser une question sur la population d'un pays
def poser_question_population(donnees_pays):
    pays = random.choice(donnees_pays['data'])
    question = f"Quelle est la population de {pays['name']} ?"
    reponse_correcte = pays['population']
    return question, reponse_correcte

# Poser une question sur le continent d'un pays
def poser_question_continent(donnees_pays):
    pays = random.choice(donnees_pays['data'])
    question = f"À quel continent appartient {pays['name']} ?"
    reponse_correcte = pays['continent']
    return question, reponse_correcte

# Poser une question sur la langue officielle d'un pays
def nom_complet_pays(donnees_pays):
    pays = random.choice(donnees_pays['data'])
    question = f"Quelle est le nom complet du {pays['name']} ?"
    reponse_correcte = pays['full_name']
    return question, reponse_correcte

# Charger les données des pays depuis le fichier JSON
donnees_pays = charger_donnees_pays()

# Liste des fonctions de question disponibles
fonctions_questions = [
    poser_question,
    poser_question_population,
    poser_question_continent,
    nom_complet_pays
]

# Déroulement du quiz
for _ in range(5):  # 5 questions au total
    fonction_question = random.choice(fonctions_questions)  # Choisir une fonction de question aléatoire
    question, reponse_correcte = fonction_question(donnees_pays)  # Poser la question
    reponse_utilisateur = input(question + "\nRéponse : ")  # Demander à l'utilisateur sa réponse
    if reponse_utilisateur.lower() == reponse_correcte.lower():  # Vérifier la réponse
        print("Correct !")
    else:
        print(f"Faux. La réponse correcte est : {reponse_correcte}")