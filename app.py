from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)

# Charger les données des pays depuis le fichier JSON
def charger_donnees_pays():
    with open('data/country_info.json', 'r') as file:
        return json.load(file)

# Sélectionner une question aléatoire et obtenir la réponse
def poser_question(donnees_pays):
    pays = random.choice(donnees_pays['data'])
    question = random.choice([
        f"Quelle est la capitale de {pays['name']} ?",
        f"Quelle est la population de {pays['name']} ?",
        f"À quel continent appartient {pays['name']} ?"
    ])
    reponse_correcte = pays.get('capital', pays.get('population', pays.get('continent')))
    return question, reponse_correcte

# Charger les données des pays
donnees_pays = charger_donnees_pays()

@app.route('/')
def index():
    question, _ = poser_question(donnees_pays)
    return render_template('index.html', question=question)

@app.route('/submit', methods=['POST'])
def submit():
    reponse_utilisateur = request.form['reponse']
    _, reponse_correcte = poser_question(donnees_pays)
    if reponse_utilisateur.lower() == reponse_correcte.lower():
        resultat = "Correct !"
    else:
        resultat = f"Faux. La réponse correcte est : {reponse_correcte}"
    return render_template('resultat.html', resultat=resultat)

if __name__ == '__main__':
    app.run(debug=True)
