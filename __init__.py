from flask import Flask
from flask import rendertemplate
from flask import json

app = Flask(name)

@app.route('/<int:valeur>')
def suite_fibonacci(n):
    a, b = 0, 1
    sequence = []
    for_in range(n):
       suite.append(a)
        a, b = b, a + b
       return suite

# Exemple avec la valeur 7
valeur = 7
resultat = suite_fibonacci(valeur)
print(",".join(str(x) for x in resultat))    
if name == "main":
    app.run(debug=True)
