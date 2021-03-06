from flask import jsonify
from random import choice
from application import app

@app.route("/colour_gen", methods=["GET"])
def colour_gen():

    # return a randomly selected colour

    colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple", "pink", "silver", "gold", "beige", "brown", "grey", "black", "white"]
    output = choice(colours)

    return jsonify({"output": output})
