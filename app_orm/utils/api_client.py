import requests
from config import API_BASE_URL

def get_users():
    return requests.get(f"{API_BASE_URL}/users").json()

def get_user(user_id):
    return requests.get(f"{API_BASE_URL}/users/{user_id}").json()

def create_user(data):
    return requests.post(f"{API_BASE_URL}/users", json=data).json()

def update_user(user_id, data):
    return requests.put(f"{API_BASE_URL}/users/{user_id}", json=data).json()

def delete_user(user_id):
    return requests.delete(f"{API_BASE_URL}/users/{user_id}").json()

# Similar para categorías y productos...
def get_categories():
    return requests.get(f"{API_BASE_URL}/categories").json()

def create_category(data):
    return requests.post(f"{API_BASE_URL}/categories", json=data).json()

def update_category(category_id, data):
    return requests.put(f"{API_BASE_URL}/categories/{category_id}", json=data).json()

def delete_category(category_id):
    return requests.delete(f"{API_BASE_URL}/categories/{category_id}").json()

# Puedes continuar para productos...
def get_products():
    return requests.get(f"{API_BASE_URL}/products").json()

def create_product(data):
    return requests.post(f"{API_BASE_URL}/products", json=data).json()

def update_product(product_id, data):
    return requests.put(f"{API_BASE_URL}/products/{product_id}", json=data).json()

def delete_product(product_id):
    return requests.delete(f"{API_BASE_URL}/products/{product_id}").json()
