# flask_app.py
from flask import Flask, jsonify, request
import requests
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api", methods=['GET', 'POST'])
def json_data():
    if request.method == 'GET':
        return "HI I am API bye"
    if request.method == 'POST':
        payload = request.get_json()
        data = pd.DataFrame(payload)
        return data.to_json(orient='records')
    return "Not supporte"

