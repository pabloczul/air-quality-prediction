import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import openaq
import datetime

API_KEY = "457efac3c78d4e9658f571eac6fcfedb65a6a288587783e3be982768cbf1c3fa"
# Obtener datos de OpenAQ
def get_openaq_data(city='Madrid', parameter='pm25', limit=1000):
    api = openaq.OpenAQ(api_key=API_KEY)
    print(api.countries.list())
    response = api.measurements.list()

    # Convertir respuesta en DataFrame
    data = pd.DataFrame([{
        'date': x['date']['utc'],
        'location': x['location'],
        'value': x['value'],
        'unit': x['unit']
    } for x in response['results']])
    
    # Convertir fecha a datetime y extraer características adicionales
    data['date'] = pd.to_datetime(data['date'])
    data['hour'] = data['date'].dt.hour
    data['day_of_week'] = data['date'].dt.dayofweek
    data['month'] = data['date'].dt.month
    
    # Filtrar y limpiar datos
    data = data.drop(columns=['date', 'location', 'unit']).dropna()
    return data

# Obtener datos
data = get_openaq_data(city='Madrid', parameter='pm25', limit=1000)
print(data.head())
