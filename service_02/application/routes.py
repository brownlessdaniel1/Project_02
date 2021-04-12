from flask import jsonify
from random import choice
from application import app

@app.route("/name_gen", methods=["GET"])
def name_gen():

    # return a randomly selected name

    names = ["Dan", "Soso", "Titi", "Minty", "Gamora", "Zac", "Sabrina"]
    output = choice(names)

    return jsonify({"output": output})
    