from flask import jsonify
from random import choice
from application import app

@app.route("/name_gen", methods=["GET"])
def name_gen():

    # return a randomly selected name

    names = ["Sophie", "Olivia", "Riley", "Emma", "Ava", "Isabella", "Aria", "Aaliya", "Liam", "Noah", "Jackson", "Aiden", "Elijah", "Grayson", "Lucas", "Oliver"]
    output = choice(names)

    return jsonify({"output": output})
    