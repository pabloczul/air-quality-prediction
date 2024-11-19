# Predicción de Calidad del Aire con MLOps

## Descripción
Este proyecto implementa un pipeline de MLOps para predecir los niveles de PM2.5 en el aire usando modelos de machine learning. Incluye la adquisición de datos de la API de OpenAQ, el preprocesamiento, el entrenamiento y el despliegue de una API con FastAPI. También contiene un archivo Docker para su contenedorización.

## Estructura del Proyecto
air-quality-prediction/ │ ├── data/ │ └── dataset.csv # Datos de entrenamiento descargados de OpenAQ ├── models/ │ └── mlruns/ # Directorio para los registros de MLflow ├── src/ │ ├── data_acquisition.py # Adquisición de datos históricos y recientes │ ├── data_preprocessing.py # Preprocesamiento de datos │ ├── model_training.py # Entrenamiento del modelo y logging en MLflow │ └── model_service.py # Funciones de carga y predicción del modelo ├── api/ │ ├── main.py # API FastAPI para predicciones │ └── test_api.py # Pruebas unitarias para la API ├── Dockerfile # Dockerfile para contenedorización ├── requirements.txt # Dependencias del proyecto ├── .env # Variables de entorno para MLflow ├── .gitignore # Archivos y carpetas a ignorar por git └── README.md # Documentación del proyecto

markdown
Copiar código

## Instrucciones

### 1. Adquisición de Datos
Para obtener los datos, usa el archivo `data_acquisition.py` con el modo deseado:

- **Histórico**: Genera datos de todo el año 2023.
  ```bash
  python src/data_acquisition.py --mode historical
Reciente: Genera datos de la última semana.
bash
Copiar código
python src/data_acquisition.py --mode recent
2. Preprocesamiento de Datos
El archivo data_preprocessing.py carga y preprocesa los datos para ser usados en el modelo.

bash
Copiar código
python src/data_preprocessing.py
3. Entrenamiento del Modelo
Entrena un modelo usando model_training.py. Esto incluye el tracking de parámetros y métricas en MLflow.

bash
Copiar código
python src/model_training.py
4. Ejecutar la API de Predicción
El archivo main.py en la carpeta api contiene la implementación de una API con FastAPI. Para iniciar la API:

bash
Copiar código
uvicorn api.main:app --host 0.0.0.0 --port 8000
5. Pruebas de la API
Para verificar el funcionamiento de la API, ejecuta las pruebas con pytest.

bash
Copiar código
pytest api/test_api.py
6. Dockerización
El Dockerfile permite construir una imagen Docker para desplegar la API en un contenedor. Para construir la imagen y ejecutarla:

bash
Copiar código
docker build -t air-quality-api .
docker run -p 8000:8000 air-quality-api
Estructura de Archivos
data_acquisition.py - Descarga datos de OpenAQ. Admite modos historical y recent.
data_preprocessing.py - Realiza el preprocesamiento del conjunto de datos.
model_training.py - Entrena el modelo y guarda el experimento en MLflow.
model_service.py - Carga el modelo y realiza predicciones.
main.py - Implementa la API FastAPI para predicciones.
test_api.py - Pruebas unitarias para la API.
Dockerfile - Dockerización del proyecto.
requirements.txt - Dependencias del proyecto.
.env - Variables de entorno para MLflow.
Dependencias
Python 3.9
FastAPI
Scikit-learn
MLflow
Docker
Requests (para adquisición de datos)
Variables de Entorno
El archivo .env contiene las variables de configuración para MLflow:

env
Copiar código
MLFLOW_TRACKING_URI=http://127.0.0.1:5000
MLFLOW_EXPERIMENT_NAME="Air Quality Prediction"
Recursos Adicionales
MLflow: https://mlflow.org/
OpenAQ API: https://openaq.org/
FastAPI: https://fastapi.tiangolo.com/