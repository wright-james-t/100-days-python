import requests
from datetime import datetime
import smtplib

MY_LAT = 30.060049 # Your latitude
MY_LONG = -95.445122 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# iss_latitude = 27.05323
# iss_longitude = -99.23422

MY_EMAIL = "$my-email"
MY_PASSWORD = "$my-password"
LOCAL_UTC_OFFSET = -6
# Your position is within +5 or -5 degrees of the ISS position.


def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Look up!"
        )


def iss_overhead_lat():
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5


def iss_overhead_long():
    return MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


def is_dark():
    return converted_sunset > time_now.hour < converted_sunrise


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

converted_sunrise = utc_to_local(sunrise)
converted_sunset = utc_to_local(sunset)

if iss_overhead_lat() and iss_overhead_long() and is_dark():
    send_email()
else:
    print("Not overhead")


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



