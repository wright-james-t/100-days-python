import os
from dotenv import load_dotenv
import requests
from datetime import date
from dateutil.relativedelta import relativedelta

KIWI_API_KEY = os.environ['KIWI_API_KEY']
load_dotenv()

KIWI_URL = 'https://api.tequila.kiwi.com/locations/query'
HOME_LOC = 'HOU'

start_date = date.today()
# Todays date + 6 months
end_date = date.today() + relativedelta(months=+6)

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

kiwi_response = requests.get(url=KIWI_URL, headers=kiwi_headers, params=kiwi_parameters).json()
print(kiwi_response["locations"][0]["city"]["code"])

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass