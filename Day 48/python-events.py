from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

# Constants
MY_URL = 'https://www.python.org/'

# Instantiating Selenium Stuff
driver = webdriver.Chrome()
driver.get(MY_URL)

# Getting the HTML for the events
upcoming_event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu time')
upcoming_event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu a')

# Creating event dict, then looping through the above events/times to make a nested dict with the info
event_dict = {}
for index in range(len(upcoming_event_names)):
    time = upcoming_event_times[index].text
    name = upcoming_event_names[index].text
    event_dict[f"event_{index}"] = {
            "name": name,
            "time": time
    }

pprint(event_dict)
driver.quit()
