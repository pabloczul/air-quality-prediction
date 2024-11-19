import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    
    # Selección de características relevantes
    features = df[['pm10', 'temperature', 'humidity', 'wind_speed']]
    target = df['pm2.5']

    # Preprocesamiento
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    # División de datos
    X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test
