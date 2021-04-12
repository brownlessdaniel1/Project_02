from flask import request, jsonify
from application import app, db
from application.models import Colour_Statement

@app.route("/generate_statement", methods=["POST"])
def generate_statement():

    input_data = request.get_json()
    name = input_data["name"]
    colour = input_data["colour"]

    statement = f"{name} loves {colour}!"

    return jsonify({"output": statement})

@app.route("/record_statement", methods=["POST"])
def record_statement():
    
    input_data = request.get_json()
    name = input_data["name"]
    colour = input_data["colour"]
    statement = input_data["statement"]

    new_row = Colour_Statement(name=name, colour=colour, statement=statement)
    db.session.add(new_row)
    db.session.commit()

    output = {}
    for row in Colour_Statement.query.all():
        output[row.id] = [str(row.name), str(row.colour), str(row.statement)]

    return jsonify(output)
