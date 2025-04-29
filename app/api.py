from flask import Flask, request, jsonify
from predict import predict_consumption

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    input_data = request.get_json()
    prediction = predict_consumption(input_data)
    return jsonify({"prediction": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)