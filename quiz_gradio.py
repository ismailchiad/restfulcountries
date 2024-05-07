import random
import json
import gradio as gr

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

# Fonction pour poser une question et obtenir la réponse
def poser_et_repondre():
    reponse_utilisateur = gr.Textbox(label="Votre réponse")
    resultat = gr.Textbox(label="Résultat")
    
    question, reponse_correcte = poser_question(donnees_pays)
    return gr.Interface(fn=lambda reponse: "Correct !" if reponse.lower() == reponse_correcte.lower() else f"Faux. La réponse correcte est : {reponse_correcte}", 
                         inputs=reponse_utilisateur, 
                         outputs=resultat, 
                         title="Quiz sur les pays",
                         description=question)

# Lancer l'interface utilisateur
if __name__ == "__main__":
    poser_et_repondre().launch()
