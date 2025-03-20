import requests
from datetime import datetime
import os
# constants
GENDER = "male"
WEIGHT_KG = 68
HEIGHT_CM = 170
AGE = 26
APP_ID = "1"
API_KEY = "1"
SECRET_KEY = "1"

exercise_endpoint = "1"
exercise_text = input("Tell me which exercises you did: ")
sheety_endpoint = (
    f"1"
)

headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


def get_exercises_from_nutrio() -> list:
    response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
    response.raise_for_status()
    result = response.json()
    return result["exercises"]


def get_date_now() -> list:
    now = datetime.now()
    formatted_date = now.strftime("%d/%m/%Y")
    formatted_hour = now.strftime("%H:%M:%S")
    date_time_array = [formatted_date, formatted_hour]
    return date_time_array


def put_exercises_to_google_sheets(exercises: list) -> None:
    for exercise in exercises:
        time_now = get_date_now()
        bearer_headers = {"Authorization": f"Bearer {SECRET_KEY}}"
        params = {
            "workout": {
                "date": time_now[0],
                "time": time_now[1],
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }
        response = requests.post(
            url=sheety_endpoint, json=params, headers=bearer_headers
        )
        response.raise_for_status()
        print(response.text)


exercises = get_exercises_from_nutrio()
put_exercises_to_google_sheets(exercises=exercises)
