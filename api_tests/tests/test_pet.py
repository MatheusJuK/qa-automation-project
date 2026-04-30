from api_tests.services.petstore_api import PetStoreAPI
import random

def generate_random_pet():
    pet_id = random.randint(1, 1000000)
    pet_name = f"Pet{pet_id}"
    return {
        "id": pet_id,
        "name": pet_name,
        "status": "available",
        "photoUrls": ["string"],
    }

def test_pet_crud():
    api = PetStoreAPI()
    
    pet = generate_random_pet()
    create_response = api.create_pet(pet)
    assert create_response.status_code == 200
    
    get_response = api.get_pet_by_id(pet['id'])
    assert get_response.status_code == 200
    
    data = get_response.json()
    assert data['id'] == pet['id']
    assert data['name'] == pet['name']
    
    pet['status'] = 'sold'
    update_response = api.update_pet(pet)
    assert update_response.status_code == 200
    
    get_updated_pet = api.get_pet_by_id(pet['id'])
    assert get_updated_pet.json()["status"] == 'sold'
    
    delete_response = api.delete_pet(pet['id'])
    assert delete_response.status_code == 200
    
    get_deleted_pet = api.get_pet_by_id(pet['id'])
    assert get_deleted_pet.status_code == 404