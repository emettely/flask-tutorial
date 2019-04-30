# flask_app.py
from flask import Flask, jsonify
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api")
def json_data():
    return jsonify(something="somethingelse")
