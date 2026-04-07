import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("predictions_log.csv")

# convert properly
df["anomaly"] = df["anomaly"].astype(str).str.strip().str.lower()

# map values
df["anomaly"] = df["anomaly"].map({
    "true": "Anomaly",
    "false": "Normal"
})

# count BOTH explicitly (important)
counts = df["anomaly"].value_counts().reindex(["Normal", "Anomaly"], fill_value=0)

print(counts)  # debug

# plot
plt.figure()
counts.plot(kind="bar")

plt.title("Anomaly Detection Summary")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()