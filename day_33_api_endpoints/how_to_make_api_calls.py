import requests
import datetime as dt

url = "http://api.open-notify.org/iss-now.json"
MY_LAT = 51.507351
MY_LONG = -0.32322
# response = requests.get(url=url)
# # if response.status_code != 200:
# #     raise Exception("Bad response from ISS API")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorized to access this data")
# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)


#  we can provide parameters as well
# get sunrise and sunsets

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0])
time_now = dt.datetime.now()
