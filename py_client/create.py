from dataclasses import dataclass
import requests



header =  {'Authorization': 'Bearer 9a3f6fc3edad1ee56c54cf51a34b2d13ac5edc09'}



endpoint = "http://localhost:8000/api/products/" 
# http://localhost:8000/admin/
# session > post data
# selenium


    


data = {
    "title": "This field is done"
}


get_response = requests.post(endpoint, json=data) 
print(get_response.json())