import pandas as pd
import numpy as np

# normal logs
data = {
    "response_time": np.random.normal(200, 50, 1000),
    "error_rate": np.random.normal(0.1, 0.05, 1000),
}

df = pd.DataFrame(data)

# inject anomalies
df.iloc[::50] = [500, 0.9]

df.to_csv("logs.csv", index=False)

print("Logs generated!")