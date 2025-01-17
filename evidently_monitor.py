import pandas as pd
import numpy as np
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metrics import DataDriftTable

# Paths
TRAINING_DATA_PATH = "data/cleaned_california_housing.csv"
LIVE_DATA_PATH = "data/live_data.csv"
REPORT_PATH = "reports/data_drift_report.html"

def simulate_production_data(df, num_samples=500):
    """Generate synthetic production data with slight perturbations."""
    live_data = df.sample(n=num_samples, replace=True).copy()
    live_data["MedInc"] = live_data["MedInc"] * np.random.uniform(0.9, 1.1, size=num_samples)
    live_data["HouseAge"] = live_data["HouseAge"] + np.random.randint(-2, 3, size=num_samples)
    live_data["AveRooms"] = live_data["AveRooms"] * np.random.uniform(0.9, 1.2, size=num_samples)
    live_data["Latitude"] = live_data["Latitude"] + np.random.uniform(-0.02, 0.02, size=num_samples)
    live_data["Longitude"] = live_data["Longitude"] + np.random.uniform(-0.02, 0.02, size=num_samples)
    return live_data

def generate_drift_report(training_data, live_data, output_path):
    """Generate a data drift report using Evidently."""
    column_mapping = ColumnMapping(
        target=None,
        prediction=None,
        numerical_features=["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
    )
    report = Report(metrics=[DataDriftTable()])
    report.run(reference_data=training_data, current_data=live_data, column_mapping=column_mapping)
    report.save_html(output_path)
    print(f"Data drift report saved to {output_path}")

def main():
    # Load training data
    df = pd.read_csv(TRAINING_DATA_PATH)
    X = df.drop(columns=["MedHouseVal"])

    # Simulate live production data
    live_data = simulate_production_data(X)
    live_data.to_csv(LIVE_DATA_PATH, index=False)
    print(f"Live production data saved to {LIVE_DATA_PATH}")

    # Generate drift report
    generate_drift_report(X, live_data, REPORT_PATH)

if __name__ == "__main__":
    import os
    os.makedirs("reports", exist_ok=True)
    main()
