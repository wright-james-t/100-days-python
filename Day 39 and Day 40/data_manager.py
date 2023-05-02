import os
from dotenv import load_dotenv
import requests
from flight_search import FlightSearch
import json

load_dotenv()
SHEETY_API = os.environ['SHEETY_API']

SHEETY_URL = 'https://api.sheety.co/ad1f4b08b09675ee998ed952dbf07a23/flightDeals/prices'
SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_API}"
}

flight_search = FlightSearch()

class DataManager:
    def __init__(self):
        # Pull all current sheet data
        self.get_sheet_data = requests.get(url=SHEETY_URL, headers=SHEETY_HEADERS).json()
        # Instantiate the City/URL dictionary, then populate it with key -> value = ${city} -> ${API-endpoint-url}
        # for use in functions later on
        self.city_url_dict = {}
        for row in self.get_sheet_data["prices"]:
            self.city_url_dict[row["city"]] = SHEETY_URL + "/" + str(row["id"])
        # make list of cities currently in the sheet
        self.city_list = self.make_list_of_cities()
        # get a city code for each city in sheet
        self.city_codes = flight_search.get_city_codes(self.make_list_of_cities())

    def make_list_of_cities(self):
        """Pull a list of cities from the google sheet and return it"""
        list_of_cities = []
        for city in self.get_sheet_data["prices"]:
            list_of_cities.append(city["city"])
        return list_of_cities

    def format_sheety_body(self):
        for city in self.city_list:
            sheety_body = {
                'price': {
                    'cuntFuckAss': 'cunt fuck ass' 
                    'IATA Code': '',
                    'Lowest Price': ''
                }
            }
        return sheety_body

    def write_to_sheet(self):
        """Takes JSON (?) data and writes it to the sheet"""
        # response = requests.put(url=url_with_id, json=sheety_body, headers=SHEETY_HEADERS)
        # response.raise_for_status()
        pass
