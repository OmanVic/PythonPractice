import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

FLIGHT_KEY = "XrfaX5eNS74DWUGrlICtlSBaUnpqzvQK"

FLIGHT_SEARCH_URL = "https://api.tequila.kiwi.com/v2/search"

MY_LOCATION = 'LGA'

today = datetime.now()
today = today.strftime("%d/%m/%Y")
print(today)

six_months = datetime.now() + relativedelta(months=6)
six_months = six_months.strftime("%d/%m/%Y")

headers = {
    "apikey": FLIGHT_KEY
}

available_flight = {
    "fly_from": "LGA",
    "fly_to": 'MIA',
    "date_from": today,
    "date_to": six_months

}

response = requests.get(url=FLIGHT_SEARCH_URL, json=available_flight, headers=headers)
print(response)
response.raise_for_status()
print(response.json())