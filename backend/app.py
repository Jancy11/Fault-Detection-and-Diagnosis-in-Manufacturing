from flask import Flask, request, jsonify
import pandas as pd
from app.anomaly_detection.detect_anomalies import detect_fault
from app.root_cause_analysis.analyze_faults import analyze_root_cause
from app.corrective_actions.take_corrective_actions import take_action

app = Flask(__name__)

@app.route("/detect_fault", methods=["POST"])
def detect_fault_api():
    data = request.get_json()
    sensor_data = pd.DataFrame(data)
    fault = detect_fault(sensor_data)
    return jsonify({"fault_detected": fault})

@app.route("/analyze_root_cause", methods=["POST"])
def analyze_root_cause_api():
    data = request.get_json()
    sensor_data = pd.DataFrame(data)
    root_cause = analyze_root_cause(sensor_data)
    return jsonify({"root_cause": root_cause})

@app.route("/take_corrective_action", methods=["POST"])
def take_corrective_action_api():
    data = request.get_json()
    corrective_action = take_action(data["root_cause"])
    return jsonify({"action_taken": corrective_action})

if __name__ == "__main__":
    app.run(debug=True)
