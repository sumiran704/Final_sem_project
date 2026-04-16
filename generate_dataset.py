import pandas as pd
import numpy as np

rows = 50000  # LARGE dataset

data = {
    "pm2_5": np.random.uniform(10, 300, rows),
    "pm10": np.random.uniform(20, 400, rows),
    "no2": np.random.uniform(5, 200, rows),
    "co": np.random.uniform(0.1, 10, rows),
    "o3": np.random.uniform(10, 250, rows),
}

df = pd.DataFrame(data)

# AQI formula (simple logic)
df["aqi"] = (
    df["pm2_5"] * 0.4 +
    df["pm10"] * 0.2 +
    df["no2"] * 0.2 +
    df["co"] * 5 +
    df["o3"] * 0.2
)

df.to_csv("dataset.csv", index=False)
print("Large dataset generated!")