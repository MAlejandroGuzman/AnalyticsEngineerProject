#despues de haber instalado la API de Kaggle , ahora cargaremos el dataset en el proyecto , lo que hara que tengamos un archivo .csv y la conectaremos con snowflake

import pandas as pd
from sqlalchemy import create_engine

# Ruta del CSV, asumiendo que estás en el directorio "dataset_files"
csv_path = "best-selling-manga.csv"

# Leer el CSV con pandas
df = pd.read_csv(csv_path)

# Datos de conexión a Snowflake:
# Account: udrzygf-jt32451
# User: dbt
# Password: dbtPassword123
# Role: TRANSFORM
# Warehouse: COMPUTE_WH
# Database: MANGA
# Schema: RAW

# Construir la cadena de conexión para Snowflake:
connection_string = (
    "snowflake://dbt:dbtPassword123@udrzygf-jt32451/MANGA/RAW"
    "?warehouse=COMPUTE_WH&role=TRANSFORM"
)

# Crear el engine de SQLAlchemy
engine = create_engine(connection_string)

# Cargar el DataFrame en una tabla llamada "best_selling_manga"
df.to_sql("best_selling_manga", engine, if_exists="replace", index=False, method="multi")

print("Datos cargados en la tabla 'best_selling_manga' en Snowflake")
