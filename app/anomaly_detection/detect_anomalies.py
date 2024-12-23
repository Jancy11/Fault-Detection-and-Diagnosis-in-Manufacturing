from sklearn.ensemble import IsolationForest

def detect_fault(sensor_data):
    model = IsolationForest(contamination=0.1)
    sensor_data['anomaly'] = model.fit_predict(sensor_data)
    anomalies = sensor_data[sensor_data['anomaly'] == -1]
    return len(anomalies) > 0
