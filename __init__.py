from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    pyramide = ''
    for j in range(1, valeur + 1):
        # Espaces pour centrer la pyramide
        pyramide += '&nbsp;' * (valeur - j) * 2
        # Affichage des nombres
        for k in range(1, j + 1):
            pyramide += str(k) + ' '
        pyramide += '<br>'
    return pyramide


if __name__ == "__main__":
  app.run(debug=True)
