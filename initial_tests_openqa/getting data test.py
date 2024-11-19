from datetime import datetime
import requests
import pandas as pd

API_KEY = "457efac3c78d4e9658f571eac6fcfedb65a6a288587783e3be982768cbf1c3fa"
HEADERS = {"X-API-Key": API_KEY}

# Función para descargar datos históricos de PM2.5
def get_historical_data(city='Delhi', parameter='pm25', limit=1000):
    url = "https://api.openaq.org/v3/measurements"
    params = {
        "city": city,
        "parameter": parameter,
        "limit": limit,
        "date_from": "2023-01-01",
        "date_to": datetime.now().strftime("%Y-%m-%d"),
        "sort": "asc",
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        data = response.json()['results']
        if data:  # Verificar que haya datos
            df = pd.DataFrame(data)
            df['datetime'] = pd.to_datetime(df['date']['utc'])
            df = df[['datetime', 'value']].rename(columns={'value': 'pm25'})
            return df
        else:
            print("No se encontraron datos para esta consulta.")
            return None
    else:
        print(f"Error al obtener datos (status code {response.status_code}):", response.json())
        return None

# Descargar datos de PM2.5 para Delhi
city_data = get_historical_data(city='Delhi')
if city_data is not None:
    city_data.to_csv('pm25_data_delhi.csv', index=False)
    print(city_data.head())
