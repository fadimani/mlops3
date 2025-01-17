import pytest
from fastapi.testclient import TestClient
from mission_4 import app, ModelInput

# Create a test client
client = TestClient(app)

# Test the root endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the California Housing Value Prediction API!"}

# Test the health endpoint
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# Test the predict endpoint with valid input
def test_predict_valid_input():
    valid_data = {
        "MedInc": 8.0,
        "HouseAge": 20.0,
        "AveRooms": 5.5,
        "AveBedrms": 1.1,
        "Population": 1500.0,
        "AveOccup": 3.0,
        "Latitude": 35.0,
        "Longitude": -120.0
    }
    response = client.post("/predict", json=valid_data)
    assert response.status_code == 200
    assert "median_house_value" in response.json()

# Test the predict endpoint with invalid input
def test_predict_invalid_input():
    invalid_data = {
        "MedInc": "invalid",  # Non-numeric value
        "HouseAge": 20.0,
        "AveRooms": 5.5,
        "AveBedrms": 1.1,
        "Population": 1500.0,
        "AveOccup": 3.0,
        "Latitude": 35.0,
        "Longitude": -120.0
    }
    response = client.post("/predict", json=invalid_data)
    assert response.status_code == 422  # Unprocessable Entity

# Test the predict endpoint with missing fields
def test_predict_missing_fields():
    incomplete_data = {
        "MedInc": 8.0,
        "HouseAge": 20.0,
        "AveRooms": 5.5
        # Missing other required fields
    }
    response = client.post("/predict", json=incomplete_data)
    assert response.status_code == 422  # Unprocessable Entity
