import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

NUTRITION_API_KEY = os.environ['NUTRITION_API_KEY']
NUTRITION_APP_ID = os.environ['NUTRITION_APP_ID']
SHEETY_API_TOKEN = os.environ['SHEETY_API_TOKEN']

NATURAL_EXERCISE_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_URL = 'https://api.sheety.co/ad1f4b08b09675ee998ed952dbf07a23/myWorkouts/workouts'

AUTH_HEADER = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
    "Content-Type": 'application/json'
}

NATURAL_EXERCISE_PARAMS = {
    "query": f"{input('What exercises did you do today? ')}",
    "gender": 'male',
    "weight_kg": 140.614,
    "height_cm": 187,
    "age": 31
}


natural_exercise_response = requests.post(NATURAL_EXERCISE_URL, headers=AUTH_HEADER, json=NATURAL_EXERCISE_PARAMS)

date_today = str(datetime.today().strftime("%m-%d-%Y"))
time_now = str(datetime.now().strftime("%X"))
specified_exercise = natural_exercise_response.json()["exercises"][0]["name"]
total_duration = natural_exercise_response.json()["exercises"][0]["duration_min"]
total_calories = natural_exercise_response.json()["exercises"][0]["nf_calories"]

sheetyBody = {
    "workout": {
        "date": date_today,
        "time": time_now,
        "exercise": specified_exercise,
        "duration": total_duration,
        "calories": total_calories
    }
}

sheetyHeader = {
    "Authorization": f"Bearer {SHEETY_API_TOKEN}"
}

response = requests.post(url=SHEETY_URL, json=sheetyBody, headers=sheetyHeader)
print("response.status_code =", response.status_code)
print("response.text =", response.text)