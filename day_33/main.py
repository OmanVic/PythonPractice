import requests
from datetime import datetime
# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# iss_position = (latitude, longitude)
# print(iss_position)

MY_LAT = 4.815554
MY_LONG = 7.049844
parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameter)
response.raise_for_status()
print(response)
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)
