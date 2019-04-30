# flask_app.py
from flask import Flask, jsonify
import requests
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api")
def json_data():
    data = pd.DataFrame(dict(words=[1, 2, 3]))
    return data.to_json(great='records')
