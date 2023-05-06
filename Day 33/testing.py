import requests
import datetime as dt

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# iss_position = (data["iss_position"]["longitude"], data["iss_position"]["latitude"])
#
# print(iss_position)

MY_LAT = 30.060049
MY_LNG = -95.445122
time_now = dt.datetime.now()

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunset, sunrise)
print(time_now)