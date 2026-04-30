import random
import string
from api_tests.services.petstore_api import PetStoreAPI

def generate_random_user():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    return {
        "id": random.randint(1, 1000),
        "username": f"user_{random_string}",
        "firstName": f"First{random_string}",
        "lastName": f"Last{random_string}",
        "email": f"{random_string}@test.com",
        "password": "password123",
        "phone": "999999999",
        "userStatus": 1
    }


def test_create_get_delete_user():
    api = PetStoreAPI()
    
    new_user = generate_random_user()
    create_response = api.create_user(new_user)
    assert create_response.status_code == 200

    get_response = api.get_user(new_user["username"])
    assert get_response.status_code == 200
    assert get_response.json()["username"] == new_user["username"]

    delete_response = api.delete_user(new_user["username"])
    assert delete_response.status_code == 200


def test_get_user_not_found():
    api = PetStoreAPI()
    response = api.get_user("usuario_que_nao_existe")
    assert response.status_code == 404
