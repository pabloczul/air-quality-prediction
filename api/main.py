from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from src.model_service import predict

app = FastAPI()

class PredictionRequest(BaseModel):
    pm10: float
    temperature: float
    humidity: float
    wind_speed: float

@app.get("/")
async def root():
    return {"message": "API de predicción de calidad del aire"}

@app.post("/predict")
async def make_prediction(request: PredictionRequest):
    input_data = request.dict()
    prediction = predict(input_data)
    return {"pm2.5_prediction": prediction}
