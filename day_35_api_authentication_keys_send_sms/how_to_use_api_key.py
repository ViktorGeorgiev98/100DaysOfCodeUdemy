import requests

api_key = "69f04e4613056b159c2761a9d9e664d2"
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}"
)
print(response.json())
