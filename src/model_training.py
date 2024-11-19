import logging
from sklearn.ensemble import RandomForestRegressor
import mlflow
from joblib import dump
from src.data_preprocessing import preprocess_data

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def train_model(X_train, y_train):
    """Entrenamiento del modelo y logging en MLflow"""
    logger.info("Iniciando el entrenamiento del modelo")

    with mlflow.start_run():
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        
        # Logging de parámetros y métricas
        mlflow.log_param("model", "RandomForest")
        mlflow.log_metric("score", model.score(X_train, y_train))
        
        dump(model, 'models/random_forest.pkl')
        logger.info("Modelo entrenado y guardado como 'random_forest.pkl'")

    logger.info("Entrenamiento completado")
    return model
