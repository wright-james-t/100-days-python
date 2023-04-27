#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import os
from dotenv import load_dotenv
import requests
from datetime import date
from dateutil.relativedelta import relativedelta

load_dotenv()

KIWI_API_KEY = os.environ['KIWI_API_KEY']

SHEETY_URL = 'https://api.sheety.co/ad1f4b08b09675ee998ed952dbf07a23/flightDeals/prices'
KIWI_URL = 'https://api.tequila.kiwi.com/locations/query'
HOME_LOC = 'HOU'

kiwi_parameters = {
    "term": 'Tokyo',
    "locale": 'en-US',
    "location_types": 'airport',
    "active_only": True
}

kiwi_headers = {
    "apikey": KIWI_API_KEY,
    "Content-Type": 'application/json'
}

start_date = date.today()
# Todays date + 6 months
end_date = date.today() + relativedelta(months=+6)

# # TODO use the below format to pull all of the city codes for each city in the list
# kiwi_response = requests.get(url=KIWI_URL, headers=kiwi_headers, params=kiwi_parameters).json()
# print(kiwi_response["locations"][0]["city"]["code"])

# TODO use the below format to pull all of the city names (to use the above to get the city codes) probably throw them in a list then iterate the list? pseudo code tomorrow
sheety_get_city_names = requests.get(url=SHEETY_URL).json()
print(sheety_get_city_names["prices"][0]["city"])