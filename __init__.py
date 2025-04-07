from flask import Flask
from flask import render_template
from flask import json


app = Flask(__name__)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    try:
        liste_nombres = [int(n) for n in valeurs.split('/')]
        min_valeur = min(liste_nombres)
        return render_template('resultat.html', minimum=min_valeur, valeurs=liste_nombres)
    except ValueError:
        return "Erreur : assure-toi de fournir uniquement des nombres séparés par des slashes ('/')."

if __name__ == '__main__':
    app.run(debug=True)
