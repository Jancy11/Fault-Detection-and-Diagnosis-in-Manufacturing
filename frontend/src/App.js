import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [sensorData, setSensorData] = useState([]);
  const [faultDetected, setFaultDetected] = useState(false);
  const [rootCause, setRootCause] = useState("");

  const fetchData = async () => {
    const response = await axios.post("http://localhost:5000/detect_fault", { data: sensorData });
    setFaultDetected(response.data.fault_detected);
  };

  const analyzeRootCause = async () => {
    const response = await axios.post("http://localhost:5000/analyze_root_cause", { data: sensorData });
    setRootCause(response.data.root_cause);
  };

  return (
    <div className="App">
      <h1>Fault Detection in Manufacturing</h1>
      <button onClick={fetchData}>Detect Fault</button>
      {faultDetected && <p>Fault Detected!</p>}
      <button onClick={analyzeRootCause}>Analyze Root Cause</button>
      {rootCause && <pre>{JSON.stringify(rootCause, null, 2)}</pre>}
    </div>
  );
}

export default App;
