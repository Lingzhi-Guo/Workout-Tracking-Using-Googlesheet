import requests
from datetime import datetime
import os

nutrition_calculation_id = "abb5c476"
nutrition_calculation_keys = "1bb0944feec4aa5d2b449d836ce8ab91"
natural_language_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/a7b7f405814d03ed1b7075e8487dd677/myWorkouts/workouts"
bearer_authentication_key = "Bearer vbdfik782ibsfa92brdb32"
# os.environ["nutrition_calculation_id"] = "abb5c476"
# os.environ["nutrition_calculation_keys"] = "1bb0944feec4aa5d2b449d836ce8ab91"
# os.environ["sheet_endpoint"] = "https://api.sheety.co/a7b7f405814d03ed1b7075e8487dd677/myWorkouts/workouts"
# os.environ["bearer_authentication_key"] = "Bearer vbdfik782ibsfa92brdb32"

natural_language_headers = {
    "x-app-id": nutrition_calculation_id,
    "x-app-key": nutrition_calculation_keys
}

natural_language_data = {
    "query": input("Tell me which exercises you did:\n")
}

response = requests.post(url=natural_language_endpoint, json=natural_language_data, headers=natural_language_headers)
data = response.json()
exercises = data["exercises"]
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for data in exercises:
    exercise = data["user_input"].title()
    duration = str(data["duration_min"])
    calories = str(data["nf_calories"])

    sheet_headers = {
        "Authorization": bearer_authentication_key
    }

    sheet_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    response = requests.post(url=sheet_endpoint, json=sheet_data, headers=sheet_headers)
    print(response.text)
