from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
       pyramide = ''
    for i in range(1, valeur + 1):
           pyramide += '' * (valeur - i )
           pyramide += ''.join(str(j) for j in range(1, i + 1))
           pyramide += ''.join(str(j) for j in range (i - 1,0, -1))
           pyramide += '<br>'
       return etoiles

if __name__ == "__main__":
  app.run(debug=True)
