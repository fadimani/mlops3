from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd


try:
    # Load the model
    model = mlflow.pyfunc.load_model("mlruns/894923872765895610/8199cd163eac4904ad5a8de910f54733/artifacts/BestModel")
except Exception as e:
    raise RuntimeError(f"Failed to load model from MLflow: {e}")


# Define the input data schema using Pydantic
class ModelInput(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

# Create the FastAPI app
app = FastAPI(title="California Housing Value Prediction API")

@app.get("/")
def root():
    return {"message": "Welcome to the California Housing Value Prediction API!"}

@app.post("/predict")
def predict(input_data: ModelInput):
    try:
        # Convert input data to DataFrame format expected by the model
        input_df = pd.DataFrame([input_data.dict()])

        # Perform prediction
        prediction = model.predict(input_df)

        # Return the prediction as a response
        return {"median_house_value": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")

# Example of adding another endpoint for health checks
@app.get("/health")
def health_check():
    return {"status": "ok"}

# run with uvicorn
#uvicorn mission_4:app --host 0.0.0.0 --port 8000
#http://127.0.0.1:8000/docs


