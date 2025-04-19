# Proyecto Flask API - Entorno de Desarrollo Local

Este repositorio contiene una aplicación Flask que implementa una API REST para la gestión de datos. Este documento describe cómo configurar un entorno de desarrollo local, ejecutar pruebas y colaborar en el proyecto.

---

## **Arquitectura del Software**

La aplicación sigue una arquitectura modular basada en Flask. Los componentes principales son:
- **API Backend**: Implementado con Flask y Flask-SQLAlchemy.
- **Base de Datos**: PostgreSQL.
- **Gestión de Configuración**: Configuración separada para entornos de desarrollo y producción.

Para más detalles, consulta el archivo [ArquitecturaSolución.md](ArquitecturaSolución.md).

---

## **Requisitos Previos**

1. **Instalar Docker y Docker Compose**: La base de datos se ejecutará en un contenedor Docker.
2. **Python 3.8+**: Para ejecutar la aplicación localmente.

---

## **Configuración del Entorno Local**

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JavierMorandeAnta/Proyecto-Final-Javier-Moran-de-Anta.git
   cd Proyecto-Final-Javier-Moran-de-Anta
   
2. Ejecuta el script de configuración:
Asegúrate de que el archivo `setup.sh` tenga permisos de ejecución:
   ```bash
   chmod +x setup.sh
   ```

Levanta Docker:

`sudo systemctl start docker`

Si no tienes permisos para ejecutar docker como usuario normal, puede añadir tu usuario al grupo docker:

`sudo usermod -aG docker $USER`

Y ejecútalo de la siguiente manera:

`./setup.sh`

Este script:

 - Configura un entorno virtual.
 - Instala las dependencias.
 - Inicia un contenedor Docker con PostgreSQL.
 - Crea las tablas necesarias en la base de datos.

3. Inicia la aplicación:
Asegurate de tener el entorno virtual activado, si no lo tienes activado, actívalo con el siguiente comando:
`source venv/bin/activate`

Finalmente inicia la aplicación:
`FLASK_ENV=development python run.py`

La API estará disponible en http://127.0.0.1:5000.

4. Ejecución de test:
Ejecución de las pruebas unitarias declaradas en la carpeta /tests para su ejecución asegurate de que el entorno vitual
este activado.

Para ejecutar las pruebas ejecuta el siguiente comando:
`pytest --cov=app tests/`
