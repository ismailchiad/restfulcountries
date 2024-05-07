import random
import json
import tkinter as tk
from tkinter import messagebox

# Charger les données des pays depuis le fichier JSON
def charger_donnees_pays():
    with open('data/country_info.json', 'r') as file:
        return json.load(file)

# Sélectionner une question aléatoire et obtenir la réponse
def poser_question(donnees_pays):
    pays = random.choice(donnees_pays['data'])
    question = f"Quelle est la capitale de {pays['name']} ?"
    reponse_correcte = pays['capital']
    return question, reponse_correcte

# Fonction appelée lorsque l'utilisateur soumet sa réponse
def soumettre_reponse():
    reponse_utilisateur = entry_reponse.get()
    if reponse_utilisateur.lower() == reponse_correcte.lower():
        messagebox.showinfo("Résultat", "Correct !")
    else:
        messagebox.showinfo("Résultat", f"Faux. La réponse correcte est : {reponse_correcte}")

# Initialiser l'interface graphique
window = tk.Tk()
window.title("Quiz sur les capitales des pays")

# Charger les données des pays
donnees_pays = charger_donnees_pays()

# Poser une question
question, reponse_correcte = poser_question(donnees_pays)

# Créer les éléments de l'interface graphique
label_question = tk.Label(window, text=question)
label_question.pack()

entry_reponse = tk.Entry(window)
entry_reponse.pack()

button_soumettre = tk.Button(window, text="Soumettre", command=soumettre_reponse)
button_soumettre.pack()

# Lancer l'interface graphique
window.mainloop()
