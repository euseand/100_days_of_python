import requests
from datetime import datetime

from constants import APP_ID, API_KEY, EXERCISE_URL, GOOGLE_SHEET_URL


headers_data = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

ex = input("enter exercise with duration or distance: ")
exercise_data = {
    "query": ex,
    "gender": "male",
    "weight_kg": 72,
    "height_cm": 175,
    "age": 23
}

response = requests.post(EXERCISE_URL, json=exercise_data, headers=headers_data).json()
exercise = response["exercises"][0]

curr_date = datetime.strftime(datetime.now(), "%d/%m/%Y")
curr_time = datetime.strftime(datetime.now(), "%H:%M:%S")
workout_data = {
    "workout": {
        "date": curr_date,
        "time": curr_time,
        "exercise": exercise["user_input"].capitalize(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }
}
response = requests.post(GOOGLE_SHEET_URL, json=workout_data).text
