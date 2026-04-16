import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("dataset.csv")

X = df[["pm2_5", "pm10", "no2", "co", "o3"]]
y = df["aqi"]

# Train model
model = RandomForestRegressor(n_estimators=50)
model.fit(X, y)

def predict_aqi(pm2_5, pm10, no2, co, o3):
    data = [[pm2_5, pm10, no2, co, o3]]
    prediction = model.predict(data)[0]
    return round(prediction, 2)