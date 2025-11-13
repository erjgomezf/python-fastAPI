from fastapi import status

def test_create_customer(client):
    '''
    Test para crear un cliente.
    '''
    customer_data = {
        "name": "John Doe",
        "description": "This is a test customer",
        "email": "prueba@prueba.com",
        "age": 30
    }
    response = client.post("/customers/", json=customer_data)
    assert response.status_code == status.HTTP_201_CREATED
    
    response_data = response.json()
    assert response_data["name"] == customer_data["name"]
    assert response_data["description"] == customer_data["description"]
    assert response_data["email"] == customer_data["email"]
    assert response_data["age"] == customer_data["age"]
    assert "id" in response_data
    assert response_data["id"] is not None
    
def test_read_customer(client):
    '''
    Test para leer un cliente por su ID.
    '''
    customer_data = {
        "name": "John Doe",
        "description": "This is a test customer",
        "email": "prueba@prueba.com",
        "age": 30
    }
    response = client.post("/customers/", json=customer_data)
    assert response.status_code == status.HTTP_201_CREATED

    customer_id: int  = response.json()["id"]
    response_read = client.get(f"/read_customers/{customer_id}")
    assert response_read.status_code == status.HTTP_200_OK
    assert response_read.json()["name"] == customer_data["name"]
    assert response_read.json()["description"] == customer_data["description"]
    assert response_read.json()["email"] == customer_data["email"]
    assert response_read.json()["age"] == customer_data["age"]
    assert response_read.json()["id"] == customer_id
    

    
