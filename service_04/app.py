from flask import Flask, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///test-db"
app.config["SECRET_KEY"]="SECRET_KEY"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    int_one = db.Column(db.Integer, nullable=False)
    int_two = db.Column(db.Integer, nullable=False)
    sum = db.Column(db.Integer, nullable=False)


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


if __name__ == "__main__":
    app.run(debug=True, port="5003")
