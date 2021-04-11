from flask import Flask, render_template, Response, jsonify
import requests
import os
from application import app

service_2 = "http://service_02:5001"
service_3 = "http://service_03:5002"
service_4 = "http://service_04:5003"

@app.route("/")
def home():

    # get responses
    name = requests.get(service_2 + "/name_gen").json()["output"]
    colour = requests.get(service_3 + "/colour_gen").json()["output"]

    data_to_be_sent = {"name":name, "colour":colour}
    statement = requests.post(service_4 + "/generate_statement", json=data_to_be_sent).json()["output"]

    data_to_be_saved = {"name":name, "colour":colour, "statement":statement} 
    previous_statements = requests.post(service_4 + "/record_statement", json=data_to_be_saved).data
    
    data_decoded = json.loads(previous_statements.decode('utf-8'))

    return render_template("index.html", name=str(name), colour=str(colour), statement=statement, previous_statements=data_decoded, version=os.getenv("VERSION"))
