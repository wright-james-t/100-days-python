import requests

API_KEY = "$my api key"
LAT = '30.079729'
LONG = '-95.417686'
BASE_URL = 'https://api.openweathermap.org/data/2.8/onecall?'

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": 'current,minutely,daily'
}

response = requests.get(url=f"{BASE_URL}", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_data_hourly = weather_data["hourly"]

sliced_list = weather_data_hourly[0:12]
sliced_list = [sliced_list[num]["weather"][0]["id"] for num in range(12)]

will_rain = False

for condition_code in sliced_list:
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")