#!/bin/bash

# Clona el repositorio en PythonAnywhere
git clone https://github.com/josemucv2/ApiWithPython.git

# Crea un entorno virtual y activa el entorno
python3 -m venv env
source env/Scripts/activate

# Instala las dependencias
pip install -r requirements.txt

# Crea una variable de entorno para el archivo .env
export $(cat .env | xargs)

# Ejecuta la aplicación con Uvicorn
uvicorn main:app
