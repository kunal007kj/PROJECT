import json
from webbrowser import get
import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"TITLE": "Hello world"}) # HTTP request
print(get_response.headers)
print(get_response.text)
#print(get_response.status_code)


print(get_response.json())


