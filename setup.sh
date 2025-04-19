#!/bin/bash

echo "Configurando el entorno de desarrollo local..."

# Crear entorno virtual
echo "Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Verificar si Docker está levantado
if ! systemctl is-active --quiet docker; then
    echo "Docker no está levantado. Iniciando Docker..."
    sudo systemctl start docker
    if [ $? -ne 0 ]; then
        echo "Error al iniciar Docker. Por favor, verifica la instalación de Docker."
        exit 1
    fi
fi

# Verificar si el contenedor ya está en ejecución
if ! docker ps --format '{{.Names}}' | grep -q '^flask-db$'; then
    echo "Iniciando contenedor Docker para PostgreSQL..."
    docker run --name flask-db -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres
    if [ $? -ne 0 ]; then
        echo "Error al iniciar el contenedor Docker. Por favor, verifica la configuración."
        exit 1
    fi
else
    echo "El contenedor Docker 'flask-db' ya está en ejecución."
fi

# Crear tablas en la base de datos
echo "Creando tablas en la base de datos..."
FLASK_ENV=development DATABASE_URI=postgresql://myuser:mypassword@127.0.0.1:5432/mydatabase python manage.py
if [ $? -ne 0 ]; then
    echo "Error al crear las tablas. Verificando si el contenedor está en ejecución..."
    if ! docker ps --format '{{.Names}}' | grep -q '^flask-db$'; then
        echo "El contenedor 'flask-db' no está en ejecución. Iniciándolo nuevamente..."
        docker start flask-db
        if [ $? -ne 0 ]; then
            echo "Error al iniciar el contenedor Docker. Por favor, verifica la configuración."
            exit 1
        fi
        echo "Reintentando crear las tablas..."
        FLASK_ENV=development DATABASE_URI=postgresql://myuser:mypassword@127.0.0.1:5432/mydatabase python manage.py
        if [ $? -ne 0 ]; then
            echo "Error persistente al crear las tablas. Por favor, verifica la configuración."
            exit 1
        fi
    else
        echo "El contenedor está en ejecución, pero ocurrió un error al crear las tablas. Por favor, verifica la configuración."
        exit 1
    fi
fi

echo "Entorno configurado correctamente. Usa 'source venv/bin/activate' para activar el entorno virtual."
