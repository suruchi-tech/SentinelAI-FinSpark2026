import pandas as pd
from sklearn.ensemble import IsolationForest

# Load security telemetry data
data = pd.read_csv("sample_logs.csv")

# Features used for anomaly detection
features = data[
    ["failed_attempts",
     "files_accessed",
     "privilege_change"]
]

# AI anomaly detection model
model = IsolationForest(
    contamination=0.3,
    random_state=42
)

data["prediction"] = model.fit_predict(features)

# Convert output
data["threat_status"] = data["prediction"].apply(
    lambda x: "HIGH RISK" if x == -1 else "NORMAL"
)

print("Insider Threat Analysis Result:")
print(data[[
    "user",
    "location",
    "threat_status"
]])
