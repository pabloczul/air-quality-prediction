import mlflow
import pandas as pd

def load_model():
    model_uri = "models:/AirQualityPredictionModel/Production"
    model = mlflow.pyfunc.load_model(model_uri)
    return model

def predict(input_data):
    model = load_model()
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    return prediction[0]
