import requests
from datetime import datetime

API_KEY = "4c079c06cdce18c0f6808bd0afcfa134"
APP_ID = "47a0643d"

GENDER = "male"
WEIGHT_KG = 94
HEIGHT_CM = 175
AGE = 21

SHEETY_USERNAME = "Tanmay"
SHEETY_PASSWORD = "tanmay123"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
#print(result)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_endpoint = "https://api.sheety.co/d4567ca7da48af7aef6a606a8b062da7/myWorkouts/workouts"
for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    #sheety_response = requests.post(sheety_endpoint, json=sheety_parameters)
    sheety_response = requests.post(
        sheety_endpoint, 
        json=sheety_parameters, 
        auth=(
            SHEETY_USERNAME, 
            SHEETY_PASSWORD,
            )
        )
    print(sheety_response.text)
    
