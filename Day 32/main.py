##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL = "$my-email"
MY_PASSWORD = "$my-password"

this_month = dt.datetime.now().month
this_day = dt.datetime.now().day
birthdays_csv = pd.read_csv("birthdays.csv")
birthday_letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

for birthday_month in birthdays_csv[birthdays_csv.month == this_month].iterrows():
    if birthday_month[1]['day'] == this_day:
        birthday_name = birthday_month[1]['name']
        birthday_email = birthday_month[1]['email']
        random_letter = random.choice(birthday_letters)
        with open(f"letter_templates/{random_letter}") as letter:
            base_letter = letter.read()
            named_letter = base_letter.replace("[NAME]", birthday_name)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_email,
                msg=f"{named_letter}"
            )