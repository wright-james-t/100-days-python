import os
from dotenv import load_dotenv
import requests

SHEETY_API = os.environ['SHEETY_API']

load_dotenv()

SHEETY_URL = 'https://api.sheety.co/ad1f4b08b09675ee998ed952dbf07a23/flightDeals/prices'
SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_API}"
}

class DataManager:
    def __init__(self):
        self.get_sheet_data = requests.get(url=SHEETY_URL, headers=SHEETY_HEADERS).json()

    def make_list_of_cities(self):
        list_of_cities = []
        for city in self.get_sheet_data["prices"]:
            list_of_cities.append(city["city"])
        return list_of_cities


    def write_to_sheet(self):
        """Takes JSON (?) data and writes it to the sheet"""
        pass

    def get_current_price_by_city(self):
        """Returns (probably) a dict of prices from the city key -> value = city -> price"""
        pass
