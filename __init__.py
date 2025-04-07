from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(n) for n in liste_nombres]

    min_valeur = liste_nombres[0]
    for n in liste_nombres:
        if n < min_valeur:
            min_valeur = n

    return str(min_valeur)

if __name__ == '__main__':
    app.run(debug=True)
