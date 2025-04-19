from app.models import Data
from app import db
import pytest


def test_create_data(app):
    """
    Prueba la creación de un objeto Data y su inserción en la base de datos.
    """
    with app.app_context():
        new_data = Data(name="Test Model")
        db.session.add(new_data)
        db.session.commit()

        # Verificar que se guardó correctamente
        saved_data = Data.query.first()
        assert saved_data is not None
        assert saved_data.name == "Test Model"


def test_duplicate_data(app):
    """
    Prueba que no se puedan insertar datos duplicados en la base de datos.
    """
    with app.app_context():
        data1 = Data(name="Duplicate Test")
        data2 = Data(name="Duplicate Test")

        db.session.add(data1)
        db.session.commit()

        # Intentar agregar un duplicado
        db.session.add(data2)
        with pytest.raises(Exception):
            db.session.commit()


def test_delete_data(app):
    """
    Prueba la eliminación de un objeto Data de la base de datos.
    """
    with app.app_context():
        new_data = Data(name="Delete Test")
        db.session.add(new_data)
        db.session.commit()

        # Verificar que el dato existe
        saved_data = Data.query.first()
        assert saved_data is not None

        # Eliminar el dato
        db.session.delete(saved_data)
        db.session.commit()

        # Verificar que se eliminó correctamente
        deleted_data = Data.query.first()
        assert deleted_data is None


def test_empty_name(app):
    """
    Prueba que no se puedan insertar datos con un nombre vacío.
    """
    with app.app_context():
        new_data = Data(name=None)

        db.session.add(new_data)
        with pytest.raises(Exception):
            db.session.commit()


def test_repr_method(app):
    """
    Prueba el método __repr__ del modelo Data.
    """
    with app.app_context():
        new_data = Data(name="Repr Test")
        db.session.add(new_data)
        db.session.commit()

        saved_data = Data.query.first()
        assert repr(saved_data) == f"<Data id={saved_data.id} name={saved_data.name}>"