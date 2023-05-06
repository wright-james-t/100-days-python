import os
from dotenv import load_dotenv
import requests

load_dotenv()
KIWI_API_KEY = os.environ['KIWI_API_KEY']
KIWI_URL = 'https://api.tequila.kiwi.com/locations/query'
HOME_LOC = 'HOU'

KIWI_HEADERS = {
    "apikey": KIWI_API_KEY,
    "Content-Type": 'application/json'
}

temp_city_list = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']
class FlightSearch:
    def __init__(self):
        self.kiwi_parameters = {
            "term": '',
            "locale": 'en-US',
            "location_types": 'airport',
            "active_only": True
        }

    # def get_city_codes(self, list_of_cities):
    def get_city_codes(self):
        city_code_dict = {}
        # for city in list_of_cities:
        for city in temp_city_list:
            self.kiwi_parameters["term"] = city
            kiwi_search = requests.get(url=KIWI_URL, headers=KIWI_HEADERS, params=self.kiwi_parameters).json()
            city_code_dict[city] = kiwi_search["locations"][0]["city"]["code"]
        return city_code_dict