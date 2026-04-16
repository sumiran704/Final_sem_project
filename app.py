from flask import Flask, render_template, request, jsonify
from predict import predict_aqi
import pandas as pd
import requests

app = Flask(__name__)

API_KEY = "c45a626038b4c2115e0d7678180219ef"

df = pd.read_csv("dataset.csv")

@app.route("/")
def home():
    return render_template("index.html")

# 🔥 ML Prediction
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    aqi = predict_aqi(
        float(data["pm2_5"]),
        float(data["pm10"]),
        float(data["no2"]),
        float(data["co"]),
        float(data["o3"])
    )

    return jsonify({"aqi": aqi})

# 🌍 LIVE AQI API
@app.route("/live_aqi/<city>")
def live_aqi(city):
    url = f"https://api.waqi.info/feed/{city}/?token={API_KEY}"
    res = requests.get(url).json()

    if res["status"] == "ok":
        return jsonify({
            "aqi": res["data"]["aqi"],
            "city": res["data"]["city"]["name"]
        })
    else:
        return jsonify({"error": "City not found"})

# 📊 Chart Data
@app.route("/data")
def data():
    sample = df.sample(100)

    return jsonify({
        "pm2_5": sample["pm2_5"].tolist(),
        "aqi": sample["aqi"].tolist()
    })

if __name__ == "__main__":
    app.run(debug=True)