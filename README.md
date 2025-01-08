# Fault Detection and Diagnosis in Manufacturing
# Submitted By: Nandhini K, Devishri N,Shiyamala G, Usharani S,Lavanya P College Name:Chenduran college of engineering and Technology.

This project implements a real-time fault detection and diagnosis system for manufacturing processes using data science and machine learning. It monitors sensor data from production machines to identify anomalies, analyze root causes, and suggest corrective actions.

## Folder Structure

```
fault_detection_manufacturing/
├── data/
│   └── sensor_data.csv
├── app/
│   ├── anomaly_detection/
│   ├── root_cause_analysis/
│   └── corrective_actions/
├── backend/
│   └── app.py
├── frontend/
│   └── src/
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your_username/fault_detection_manufacturing.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Start the backend:
   ```
   python backend/app.py
   ```

4. Run the frontend:
   ```
   cd frontend
   npm install
   npm start
   ```

## Usage

- Use the `/detect_fault` API to check if any faults are detected from the sensor data.
- Use `/analyze_root_cause` to find potential root causes of detected faults.
- `/take_corrective_action` provides suggestions for corrective actions based on the root cause.

## Real-Time Examples

1. **Automotive Manufacturing**: Detect faults in assembly lines.
2. **Pharmaceutical Manufacturing**: Monitor drug production processes.

---

Feel free to contribute or use this project in your own manufacturing environments.
