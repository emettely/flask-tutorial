# flask_app.py
from flask import Flask, jsonify, request
import requests
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

# Set debug status
if config.ENVIRONMENT == 'development':
    app.config["DEBUG"] = True
else:
    app.config["DEBUG"] = False

for key, value in config.DB[config.ENVIRONMENT].items():
    app.config[key] = value
db = SQLAlchemy(app)

class ApiRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), unique=True, nullable=False)
    value = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f'<{self.key}: {self.value}>'


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

