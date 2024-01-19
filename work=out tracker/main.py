import requests
from datetime import datetime

sheety_url = "https://api.sheety.co/097f9edf6428bf0f8c5d7af6a7961dc1/workoutTracking/workouts"

GENDER = "MALE"
WEIGHT_KG = "50"
HEIGHT = "176"
AGE = '25'

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")
# print(today_time)
# print(today_date)

APP_ID_NUTRITIONIX = "51b176d9"

APP_KEY_NUTRITIONIX = "bb35ea348a5dda330ee9d2ee8402e205"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID_NUTRITIONIX,
    'x-app-key': APP_KEY_NUTRITIONIX,


}

sheet_header = {
    "Authorization": "123456789",
}

parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()


for values in result["exercises"]:
    param ={
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": values["user_input"],
            "duration": values["duration_min"],
            "calories": values["nf_calories"]
    }
 }

    response = requests.post(url=sheety_url, json=param)
    response.raise_for_status()
    print(response.text)




