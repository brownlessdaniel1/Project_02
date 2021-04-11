from flask import request, jsonify
import os
from application import app, db
from application.models import Record

@app.route("/sum_ints", methods=["POST"])
def sum_data():

    input_data = request.get_json()
    int_one = input_data["int_one"]
    int_two = input_data["int_two"]

    sum = int_one + int_two

    return jsonify({"output": sum})

@app.route("/record_data", methods=["POST"])
def record_data():
    
    input_data = request.get_json()
    int_one = input_data["int_one"]
    int_two = input_data["int_two"]
    sum = input_data["sum"]

    new_row = Record(int_one=int_one, int_two=int_two, sum=sum)
    db.session.add(new_row)
    db.session.commit()

    output = {}
    for row in Record.query.all():
        
        output[row.id] = [str(row.int_one), str(row.int_two), str(row.sum)]


    return jsonify(output)
