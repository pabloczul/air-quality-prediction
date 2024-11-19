from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Funciones de entrenamiento y evaluación
def fetch_data():
    return get_openaq_data()

def train_model():
    rf_model.fit(X_train, y_train)
    mlflow.sklearn.log_model(rf_model.model, "random_forest_model")

# Definición del DAG
dag = DAG('air_quality_prediction_pipeline', start_date=datetime(2024, 11, 1), schedule_interval='@daily')

fetch_task = PythonOperator(task_id='fetch_data', python_callable=fetch_data, dag=dag)
train_task = PythonOperator(task_id='train_model', python_callable=train_model, dag=dag)

fetch_task >> train_task
