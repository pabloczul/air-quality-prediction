from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de predicción de calidad del aire"}

def test_predict():
    response = client.post("/predict", json={"pm10": 20.5, "temperature": 22.3, "humidity": 45.0, "wind_speed": 3.2})
    assert response.status_code == 200
    assert "pm2.5_prediction" in response.json()
