#Este archivo configura un entorno de pruebas para la aplicación Flask. 
#Aquí se crea una instancia de la aplicación en modo de pruebas y una base de datos SQLite en memoria.

import pytest
from app import create_app, db
from app.config import config_dict

@pytest.fixture
def app():
    """
    Configura una instancia de la aplicación Flask en modo de pruebas.
    Utiliza una base de datos SQLite en memoria para garantizar que las pruebas
    no afecten los datos reales.
    """
    # Crear la aplicación Flask con la configuración de pruebas
    app = create_app("testing")  # Asegúrate de definir "testing" en config_dict
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # Base de datos en memoria
    })

    with app.app_context():
        # Crear las tablas en la base de datos
        db.create_all()
        yield app
        # Limpiar la base de datos después de las pruebas
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """
    Proporciona un cliente de pruebas para realizar solicitudes HTTP a la aplicación.
    """
    return app.test_client()

@pytest.fixture
def runner(app):
    """
    Proporciona un runner de pruebas para ejecutar comandos de la aplicación.
    """
    return app.test_cli_runner()