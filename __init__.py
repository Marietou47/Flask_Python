from flask import Flask
from flask import rendertemplate
from flask import json

app = Flask(name)

@app.route('/<int:valeur>')
def exercice(valeur):
    a, b = 0, 1
    sequence = [a, b]
    for  in range(2, valeur):
        a, b = b, a + b
        sequence.append(b)

    fibonacci = '<pre>' + ', '.join(map(str, sequence)) + '</pre>'
    return fibonacci

if name == "main":
    app.run(debug=True)
