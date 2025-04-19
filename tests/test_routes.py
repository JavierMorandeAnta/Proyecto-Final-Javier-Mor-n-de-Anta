def test_insert_data(client):
    """
    Prueba para insertar datos correctamente.
    """
    response = client.post("/data", json={"name": "Test Data"})
    assert response.status_code == 200
    assert response.json["message"] == "Data inserted successfully"


def test_insert_duplicate_data(client):
    """
    Prueba para insertar datos duplicados.
    """
    client.post("/data", json={"name": "Duplicate Data"})
    response = client.post("/data", json={"name": "Duplicate Data"})
    assert response.status_code == 409
    assert response.json["message"] == "Data already exists"


def test_insert_empty_name(client):
    """
    Prueba para insertar datos con un nombre vacío.
    """
    response = client.post("/data", json={"name": ""})
    assert response.status_code == 400  # Asegúrate de manejar este caso en la app
    assert "Invalid data" in response.json["message"]


def test_get_all_data(client):
    """
    Prueba para obtener todos los datos.
    """
    client.post("/data", json={"name": "Test Data 1"})
    client.post("/data", json={"name": "Test Data 2"})
    response = client.get("/data")
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["name"] == "Test Data 1"
    assert response.json[1]["name"] == "Test Data 2"


def test_delete_data(client):
    """
    Prueba para eliminar un dato existente.
    """
    client.post("/data", json={"name": "Test Data"})
    response = client.delete("/data/1")
    assert response.status_code == 200
    assert response.json["message"] == "Data deleted successfully"


def test_delete_nonexistent_data(client):
    """
    Prueba para eliminar un dato que no existe.
    """
    response = client.delete("/data/999")
    assert response.status_code == 404
    assert response.json["message"] == "Data not found"