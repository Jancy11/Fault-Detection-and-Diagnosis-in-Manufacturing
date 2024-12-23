import pandas as pd

def analyze_root_cause(sensor_data):
    correlation = sensor_data.corr()
    return correlation.to_dict()
