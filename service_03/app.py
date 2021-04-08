from flask import Flask, Response, jsonify
from random import randint

app = Flask(__name__)

@app.route("/int_two", methods=["GET"])         # App1 comes here and gets this random number.
def int_two():

    output = randint(1, 100)

    return jsonify({"output": output})




if __name__ == "__main__":
    app.run(debug=True, port="5002")
