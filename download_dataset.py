# Descargar datasets de Kaggle
#Solicitar en Kaggle el archivo JSON siguiento esta ruta: Settings > API > Create new token

#Despues guardar el archivo JSON dentro de una nueva carpeta generada llamada .JSON dentro de la siguiente ruta C:\Users\<User_name>\
#hacer un mkdir con una carpeta llamada .kaggle

import os
import zipfile
import kaggle

# Define la ruta donde descargarás el dataset
download_path = "./dataset"
os.makedirs(download_path, exist_ok=True)

# Descarga el dataset (esto creará un archivo ZIP)
os.system(f'kaggle datasets download -d drahulsingh/best-selling-manga -p {download_path}')

# Opcional: descomprimir el archivo descargado
zip_file = os.path.join(download_path, "best-selling-manga.zip")
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(download_path)

print("Dataset descargado y descomprimido en:", download_path)
