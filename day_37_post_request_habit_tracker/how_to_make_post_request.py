import requests
import datetime as dt

USERNAME = "test981"
TOKEN = "sadadsdsadasdasdasdasdsa"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# normal post request, above we have required params
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# advanced authentication with http headers
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# posting a pixel
today = dt.datetime.now()
# print(today.strftime("%Y%m%d"))
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# put request
update_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
)
new_pixel_data = {"quantity": "15"}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# delete request
delete_endpoint = update_endpoint
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
