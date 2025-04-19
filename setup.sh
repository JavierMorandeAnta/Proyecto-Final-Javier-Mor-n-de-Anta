#!/bin/bash

echo "Configurando el entorno de desarrollo local..."

# Crear entorno virtual
echo "Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Iniciar contenedor Docker para PostgreSQL
echo "Iniciando contenedor Docker para PostgreSQL..."
docker run --name flask-db -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres

# Crear tablas en la base de datos
echo "Creando tablas en la base de datos..."
FLASK_ENV=development DATABASE_URI=postgresql://myuser:mypassword@127.0.0.1:5432/mydatabase python manage.py

echo "Entorno configurado correctamente. Usa 'source venv/bin/activate' para activar el entorno virtual."