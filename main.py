import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 183
AGE = 27

exercise_endpoint = os.getenv("exercise_endpoint")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

data = {

    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,

}

response = requests.post(exercise_endpoint, json=data, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# Date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = os.getenv("SHEET_ENDPOINT")

for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(f"Sheety Response: \n {sheet_response.text}")

