from flask import Flask
from flask import render_template
from flask import json
app = Flask(_name_)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(n) for n in liste_nombres]

    min_valeur = liste_nombres[0]
    for n in liste_nombres:
        if n < min_valeur:
            min_valeur = n

    return str(min_valeur)

if name == '_main_':
    app.run(debug=True)
