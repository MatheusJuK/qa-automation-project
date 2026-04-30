from api_tests.services.petstore_api import PetStoreAPI
from datetime import datetime
import random


def generate_order():
    order_id = random.randint(1000, 9999)

    return {
        "id": order_id,
        "petId": 1,
        "quantity": 1,
        "shipDate": datetime.now().isoformat(),
        "status": "placed",
        "complete": True
    }


def test_store_order_flow():
    api = PetStoreAPI()

    order = generate_order()
    
    create_response = api.create_order(order)
    assert create_response.status_code == 200
    
    get_response = api.get_order_by_id(order["id"])
    assert get_response.status_code == 200
    
    data = get_response.json()
    assert data["id"] == order["id"]
    assert data["status"] == "placed"
    
    delete_response = api.delete_order(order["id"])
    assert delete_response.status_code == 200

    get_after_delete = api.get_order_by_id(order["id"])
    assert get_after_delete.status_code == 404

def test_get_inventory():
    api = PetStoreAPI()
    
    response = api.get_inventory()
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, dict)