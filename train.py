from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib

df = pd.read_csv("logs.csv")

model = IsolationForest(contamination=0.05)
model.fit(df)

joblib.dump(model, "model.pkl")

print("Model trained!")