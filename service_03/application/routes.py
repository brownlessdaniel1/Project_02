from flask import Flask, jsonify
from random import randint
from application import app


@app.route("/int_two", methods=["GET"])         # App1 comes here and gets this random number.
def int_two():

    output = randint(1, 100)

    return jsonify({"output": output})
