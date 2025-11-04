from fastapi.testclient import TestClient


def test_client(client):
    assert type(client) == TestClient
    

#test para crear un customer
def test_create_customer(client):
    customer_data = {
        "name": "John Doe",
        "description": "This is a test customer",
        "email": "prueba@prueba.com",
        "age": 30
    }
    response = client.post("/customers/", json=customer_data)
    assert response.status_code == 200
    
    response_data = response.json()
    assert response_data["name"] == customer_data["name"]
    assert response_data["description"] == customer_data["description"]
    assert response_data["email"] == customer_data["email"]
    assert response_data["age"] == customer_data["age"]
    assert "id" in response_data
    assert response_data["id"] is not None