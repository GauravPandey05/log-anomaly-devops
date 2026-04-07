from fastapi import FastAPI
import joblib
import csv
import os
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load model
model = joblib.load("model.pkl")

LOG_FILE = "predictions_log.csv"
ALERT_FILE = "alerts.txt"

# create CSV if not exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "response_time", "error_rate", "anomaly"])


@app.get("/")
def home():
    return {"message": "Log Anomaly Detection API Running"}


@app.post("/predict")
def predict(log: dict):
    response_time = log["response_time"]
    error_rate = log["error_rate"]

    # model prediction
    data = [[response_time, error_rate]]
    result = model.predict(data)

    anomaly = True if result[0] == -1 else False

    # save to CSV
    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(),
            response_time,
            error_rate,
            anomaly
        ])

    # 🚨 ALERT SYSTEM
    if anomaly:
        alert_msg = f"ALERT at {datetime.now()} | Response: {response_time}, Error: {error_rate}\n"
        
        print("🚨", alert_msg)

        with open(ALERT_FILE, "a") as f:
            f.write(alert_msg)

    return {"anomaly": anomaly}


# 📊 OPTIONAL: STATS ENDPOINT (VERY USEFUL FOR DEMO)
@app.get("/stats")
def stats():
    if not os.path.exists(LOG_FILE):
        return {"message": "No data yet"}

    df = pd.read_csv(LOG_FILE)

    counts = df["anomaly"].value_counts().to_dict()

    return {
        "total_logs": len(df),
        "anomalies": counts.get(True, 0),
        "normal": counts.get(False, 0)
    }