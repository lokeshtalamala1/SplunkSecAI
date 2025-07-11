import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("../sample_logs/synthetic_login_data.csv")
X = df[["login_hour", "login_day", "geo_distance"]]
model = IsolationForest(n_estimators=100, contamination=0.05)
model.fit(X)
df["anomaly_score"] = model.decision_function(X)
df["is_anomaly"] = model.predict(X)
df.to_csv("../sample_logs/anomaly_results.csv", index=False)
print("Anomaly detection completed.")