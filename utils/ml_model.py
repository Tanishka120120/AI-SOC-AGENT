from sklearn.ensemble import IsolationForest


def detect_anomalies(logs):

    features = logs[
        ["failed_logins", "data_transfer"]
    ]

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    logs["anomaly"] = model.fit_predict(features)

    return logs