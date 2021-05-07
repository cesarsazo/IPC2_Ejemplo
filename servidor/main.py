from flask import Flask, request, url_for, redirect, jsonify
from flask_cors import CORS
from findEmail import findEmail
from moduleXml import returnArray
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '<h1>IPC2</h1>'

@app.route('/suma', methods=['GET', 'POST'])
def suma():
    if request.method == 'GET':
        return 'Suma'
    else:
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        result = int(numero1) + int(numero2)
        return "suma realizada el resultado es: "+ str(result)

@app.route('/correos', methods=['GET', 'POST'])
def correos():
    if request.method == 'GET':
        return 'GET'
    else:
        entrada = request.form['texto']
        response = findEmail(entrada)
        return jsonify(response)

@app.route('/obtenerTodo', methods=['GET'])
def todo():
    for value in returnArray().values():
        print(value)
    return json.dumps(returnArray())

app.run(host='0.0.0.0', debug=True)