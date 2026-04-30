from api_tests.services.petstore_api import PetStoreAPI

def test_get_user_not_found():
    api = PetStoreAPI()
    response = api.get_user("usuario_que_nao_existe")
    assert response.status_code == 404

test_get_user_not_found()