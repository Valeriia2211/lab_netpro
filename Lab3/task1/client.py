import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:5000"
auth = HTTPBasicAuth("admin", "1234")

print("=== GET ALL ITEMS ===")
print(requests.get(f"{BASE_URL}/items", auth=auth).json())

print("\n=== UPDATE PHONE (id=2) ===")
update_data = {
    "price": 17000,
    "color": "blue"
}
print(requests.put(f"{BASE_URL}/items/2", json=update_data, auth=auth).json())

print("\n=== DELETE TABLET (id=3) ===")
print(requests.delete(f"{BASE_URL}/items/3", auth=auth).json())

print("\n=== ADD NEW ITEM ===")
new_item = {
    "name": "Camera",
    "price": 12000,
    "color": "black"
}
print(requests.post(f"{BASE_URL}/items", json=new_item, auth=auth).json())
