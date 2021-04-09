from flask import Flask, render_template, Response, jsonify
import requests

service_2 = "http://service_02:5001"         # Was: localhost
service_3 = "http://service_03:5002"
service_4 = "http://service_04:5003"

app = Flask(__name__, template_folder=".")

@app.route("/")
def home():

    response_service_2 = requests.get(service_2 + "/int_one").json()["output"]
    response_service_3 = requests.get(service_3 + "/int_two").json()["output"]

    ints_to_be_sent = {"int_one":response_service_2, "int_two":response_service_3}
    response_service_4 = requests.post(service_4 + "/sum_ints", json=ints_to_be_sent).json()["output"]


    data_to_be_saved = {"int_one":response_service_2, "int_two":response_service_3, "sum":response_service_4} 
    
    
    previous_records = requests.post(service_4 + "/record_data", json=data_to_be_saved).json()


    return render_template("home.html", int_one=str(response_service_2), int_two=str(response_service_3), total=previous_records)



if __name__ == "__main__":
    app.run(debug=True, port="5000", host="0.0.0.0")
