import requests
import pandas as pd
from datetime import datetime, timedelta
import os

API_BASE_URL = "https://api.openaq.org/v2/measurements"

def fetch_data(params):
    """Realiza una solicitud a la API de OpenAQ con los parámetros especificados."""
    response = requests.get(API_BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

def acquire_historical_data(city, parameter, start_date, end_date):
    """Descarga datos históricos desde start_date hasta end_date."""
    data = []
    current_date = start_date

    while current_date <= end_date:
        params = {
            "city": city,
            "parameter": parameter,
            "date_from": current_date.strftime("%Y-%m-%d"),
            "date_to": (current_date + timedelta(days=6)).strftime("%Y-%m-%d"),
            "limit": 10000,
            "format": "json"
        }
        
        response = fetch_data(params)
        data.extend(response["results"])
        current_date += timedelta(days=7)

    return pd.DataFrame(data)

def acquire_recent_data(city, parameter):
    """Descarga datos de la última semana."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    params = {
        "city": city,
        "parameter": parameter,
        "date_from": start_date.strftime("%Y-%m-%d"),
        "date_to": end_date.strftime("%Y-%m-%d"),
        "limit": 10000,
        "format": "json"
    }
    
    response = fetch_data(params)
    return pd.DataFrame(response["results"])

def save_data(data, filepath="data/dataset.csv"):
    """Guarda el DataFrame de datos en un archivo CSV."""
    os.makedirs("data", exist_ok=True)
    data.to_csv(filepath, index=False)

def main(mode="historical", city="Delhi", parameter="pm25"):
    """Función principal para adquisición de datos en modo 'historical' o 'recent'."""
    if mode == "historical":
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 12, 31)
        data = acquire_historical_data(city, parameter, start_date, end_date)
    elif mode == "recent":
        data = acquire_recent_data(city, parameter)
    else:
        raise ValueError("Modo no válido. Usa 'historical' o 'recent'.")

    save_data(data)

if __name__ == "__main__":
    main(mode="historical")
