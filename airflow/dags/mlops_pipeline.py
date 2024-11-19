from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

def acquire_data_historical():
    """Ejecuta el script de adquisición de datos históricos."""
    subprocess.run(["python", "src/data_acquisition.py", "--mode", "historical"])

def acquire_data_recent():
    """Ejecuta el script de adquisición de datos recientes."""
    subprocess.run(["python", "src/data_acquisition.py", "--mode", "recent"])

def preprocess_data():
    """Ejecuta el preprocesamiento de datos."""
    subprocess.run(["python", "src/data_preprocessing.py"])

def train_model():
    """Entrena el modelo."""
    subprocess.run(["python", "src/model_training.py"])

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2023, 1, 1),
}

dag = DAG(
    'mlops_pipeline',
    default_args=default_args,
    description='Un pipeline completo de MLOps para predicción de calidad del aire',
    schedule_interval='@daily',
)

t1 = PythonOperator(
    task_id='acquire_data_historical',
    python_callable=acquire_data_historical,
    dag=dag,
)

t2 = PythonOperator(
    task_id='acquire_data_recent',
    python_callable=acquire_data_recent,
    dag=dag,
)

t3 = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag,
)

t4 = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

t1 >> [t2, t3] >> t4
