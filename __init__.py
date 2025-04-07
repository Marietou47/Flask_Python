from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)

@app.route('/<int:valeur>')
def calcul_somme(n):
     somme = 0
    for i in rangel(1, n + 1):
        if i % 11 == 0:
            continue
         if i % 5 == 0 or i % 7 == 0:
             somme += i
         if somme > 5000:
             return f"La somme a dépassé 5000.Arrêt du programme.<br>Somme finale : {somme}"
        return f"Somme finale : {somme}"

if __name__ == "__main__":
    app.run(debug=True)
