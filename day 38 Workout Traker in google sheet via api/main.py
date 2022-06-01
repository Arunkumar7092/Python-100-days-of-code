import requests
from datetime import datetime
import os

AP_ID = os.environ["APP_ID"]
AP_KEY = os.environ["APP_KEY"]


GENDER = "male"
WEIGHT_KG = 61.0
HEIGHT_CM = 164.5
AGE = 24

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": AP_ID,
    "x-app-key": AP_KEY,
}

parameters = {
    "query":exercise_text,
    "gender": GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}


url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

response = requests.post(url, json=parameters, headers=headers)
result = response.json()
response.raise_for_status()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
# print(sheet_response.text)



sheet_response = requests.post(sheet_endpoint, json=sheet_inputs ,auth=(os.environ.get("USERNAME") ,os.environ.get("PASSWORD")))

print(sheet_response.text)