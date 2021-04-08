from flask import Flask, render_template, Response, jsonify
import requests

service_2 = "http://localhost:5001"
service_3 = "http://localhost:5002"
service_4 = "http://localhost:5003"

app = Flask(__name__, template_folder=".")

@app.route("/")
def home():

    response_service_2 = requests.get(service_2 + "/int_one").json()["output"]
    response_service_3 = requests.get(service_3 + "/int_two").json()["output"]

    ints_to_be_sent = {"int_one":response_service_2, "int_two":response_service_3}
    response_service_4 = requests.post(service_4 + "/sum_ints", json=ints_to_be_sent).json()["output"]


    data_to_be_saved = {"int_one":response_service_2, "int_two":response_service_3, "sum":response_service_4} 
    requests.post(service_4 + "/record_data", json=data_to_be_saved)

    previous_data_dict = {}


    return render_template("home.html", int_one=str(response_service_2), int_two=str(response_service_3), total=str(response_service_4))


@app.route("/previous_data")
def previous_data():
    record_json_output = requests.get(service_4 + "/read_data").json()

    return record_json_output

if __name__ == "__main__":
    app.run(debug=True, port="5000")
