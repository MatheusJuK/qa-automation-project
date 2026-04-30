import requests

class PetStoreAPI:
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
    
    def get_user(self, username):
        url = f"{self.BASE_URL}/user/{username}"
        response = self.session.get(url)
        return response
    
    def update_user(self, username, payload):
        url = f"{self.BASE_URL}/user/{username}"
        response = self.session.put(url, json=payload)
        return response
    
    def delete_user(self, username):
        url = f"{self.BASE_URL}/user/{username}"
        response = self.session.delete(url)
        return response
    
    def create_user(self, payload):
        url = f"{self.BASE_URL}/user"
        response = self.session.post(url, json=payload)
        return response
    
    def login_user(self, username, password):
        url = f"{self.BASE_URL}/user/login"
        params = {"username": username, "password": password}
        response = self.session.get(url, params=params)
        return response
    
    def logout_user(self):
        url = f"{self.BASE_URL}/user/logout"
        response = self.session.get(url)
        return response
    
    def create_users_with_array(self, payload):
        url = f"{self.BASE_URL}/user/createWithArray"
        response = self.session.post(url, json=payload)
        return response
    
    def create_users_with_list(self, payload):
        url = f"{self.BASE_URL}/user/createWithList"
        response = self.session.post(url, json=payload)
        return response
    
    
    def find_purchase_order_by_id(self, order_id):
        url = f"{self.BASE_URL}/store/order/{order_id}"
        response = self.session.get(url)
        return response
    
    def delete_order(self, order_id):
        url = f"{self.BASE_URL}/store/order/{order_id}"
        response = self.session.delete(url)
        return response
    
    def get_inventory(self):
        url = f"{self.BASE_URL}/store/inventory"
        response = self.session.get(url)
        return response
    
    def place_order(self, payload):
        url = f"{self.BASE_URL}/store/order"
        response = self.session.post(url, json=payload)
        return response
    
    def get_pet_by_id(self, pet_id):
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = self.session.get(url)
        return response
    
    def update_pet_with_formData(self, pet_id, name=None, status=None):
        url = f"{self.BASE_URL}/pet/{pet_id}"
        data = {}
        if name:
            data['name'] = name
        if status:
            data['status'] = status
        response = self.session.post(url, data=data)
        return response
    
    def delete_pet(self, pet_id):
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = self.session.delete(url)
        return response
    
    def upload_file(self, pet_id, file_path):
        url = f"{self.BASE_URL}/pet/{pet_id}/uploadImage"
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = self.session.post(url, files=files)
        return response
    
    def create_pet(self, payload):
        url = f"{self.BASE_URL}/pet"
        response = self.session.post(url, json=payload)
        return response
    
    def update_pet(self, payload):
        url = f"{self.BASE_URL}/pet"
        response = self.session.put(url, json=payload)
        return response
    
    def find_pets_by_status(self, status):
        url = f"{self.BASE_URL}/pet/findByStatus"
        params = {"status": status}
        response = self.session.get(url, params=params)
        return response