import requests
API_KEY = "dcefdc0cb5e1e5a8164e67fef58d4a5b"
lat = 4.815554
lon = 7.049844
weather_parameter = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=weather_parameter)
response.raise_for_status()
weather_data = response.json()
weather_condition = weather_data["weather"][0]["id"]


