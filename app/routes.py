from flask import Blueprint, request, jsonify
from app.models import Data
from app import db

data_routes = Blueprint("data_routes", __name__)


@data_routes.route("/data", methods=["POST"])
def insert_data():
    """
    Inserta un nuevo dato en la base de datos.
    Valida que el nombre no sea vacío o nulo.
    """
    data = request.json

    # Validar que el nombre esté presente y no sea vacío
    if not data or not data.get("name") or data.get("name").strip() == "":
        return {"message": "Invalid data: 'name' is required and cannot be empty"}, 400

    # Verificar si el dato ya existe
    current_data = Data.query.filter_by(name=data.get("name")).first()
    if current_data:
        return {"message": "Data already exists"}, 409

    # Insertar el nuevo dato
    new_data = Data(name=data.get("name").strip())
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"message": "Data inserted successfully"})


@data_routes.route("/data", methods=["GET"])
def get_all_data():
    """
    Devuelve todos los datos almacenados en la base de datos.
    """
    data_list = [{"id": data.id, "name": data.name} for data in Data.query.all()]
    return jsonify(data_list)


@data_routes.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    """
    Elimina un dato de la base de datos por su ID.
    """
    element_to_delete = Data.query.get(id)
    if not element_to_delete:
        return {"message": "Data not found"}, 404

    db.session.delete(element_to_delete)
    db.session.commit()
    return {"message": "Data deleted successfully"}
