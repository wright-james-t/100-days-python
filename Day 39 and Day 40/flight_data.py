import os
from dotenv import load_dotenv
import requests
from datetime import date
from dateutil.relativedelta import relativedelta

load_dotenv()
KIWI_API_KEY = os.environ['KIWI_API_KEY']
KIWI_URL = 'https://api.tequila.kiwi.com/locations/query'
HOME_LOC = 'HOU'
TODAY = date.today()
# Todays date + 6 months
TODAY_PLUS_6_MONTHS = date.today() + relativedelta(months=+6)
KIWI_HEADERS = {
    "apikey": KIWI_API_KEY,
    "Content-Type": 'application/json'
}

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.kiwi_parameters = {
            "term": '',
            "locale": 'en-US',
            "location_types": 'airport',
            "active_only": True
        }
        self.price = ''
        self.departure_airport_city = HOME_LOC
        self.departure_date_begin_range = TODAY
        self.departure_date_end_range = TODAY_PLUS_6_MONTHS

    def get_current_price_by_city(self, destination_city):
        """Returns (probably) a dict of prices from the city key -> value = city -> price"""
        self.kiwi_parameters["term"] = destination_city
        location_response = requests.get(url=KIWI_URL, headers=KIWI_HEADERS, params=self.kiwi_parameters)
