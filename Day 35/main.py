import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

LAT = '30.079941'
LONG = '-95.417160'
BASE_URL = 'https://api.openweathermap.org/data/2.8/onecall?'
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
MY_NUMBER = os.environ['MY_NUMBER']
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']


parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": WEATHER_API_KEY,
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
    print(condition_code)
    if condition_code < 700:
        will_rain = True

if will_rain:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's going to rain, bring an umbrella ☔",
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
    )

    print(message.status)