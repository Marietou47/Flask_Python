from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    try:
        liste_nombres = [int(n) for n in valeurs.split('/')]
        max_valeur = max(liste_nombres)
        return f"Le nombre maximum est : {max_valeur}"
    except ValueError:
        return "Erreur : assure-toi de fournir uniquement des nombres séparés par des slashes ('/')."

if __name__ == '__main__':
    app.run(debug=True)

