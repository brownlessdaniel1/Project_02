from flask import jsonify
from random import choice
from application import app

@app.route("/colour_gen", methods=["GET"])
def colour_gen():

    # return a randomly selected colour

    colours = ["Green", "Yellow", "Dan", "Soso", "Titi", "Minty", "Gamora", "Zac", "Sabrina"]
    output = choice(colours)

    return jsonify({"output": output})
