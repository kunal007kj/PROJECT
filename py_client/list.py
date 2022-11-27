from wsgiref import headers
import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/" 
username = input("what is your Username?\n")
password = getpass("what is your Password?\n")
auth_response = requests.post(endpoint, json={"username": username, "password": password }) 
print(auth_response.json())

if auth_response.status_code == 200:
    token= auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer{token}"
    }
endpoint = "http://localhost:8000/api/products/" 

get_response = requests.get(endpoint) 
print(get_response.json())