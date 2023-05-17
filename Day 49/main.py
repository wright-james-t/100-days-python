import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Loading .env
load_dotenv()

# Constants
COOKIE_URL = 'https://www.linkedin.com/jobs/search/?alertAction=viewjobs&currentJobId=3601160460&f_AL=true&f_F=it&f_SB2=2&f_T=25169&f_TPR=r604800&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States&refresh=true&sortBy=R'
# Import user/pass from .env
LI_USER = os.environ['LI_USER']
LI_PASS = os.environ['LI_PASS']

# Instantiating Selenium Stuff
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(COOKIE_URL)

# Fetching element for log in button
sign_in_button = driver.find_element(By.CSS_SELECTOR, 'div header nav div .nav__button-secondary')
sign_in_button.click()

# Inputting login information
username_input_box = driver.find_element(By.ID, 'username')
password_input_box = driver.find_element(By.ID, 'password')
username_input_box.send_keys(LI_USER)
password_input_box.send_keys(LI_PASS)
password_input_box.send_keys(Keys.ENTER)

# Sleep for a bit while we wait for page to load and jobs to be listed
time.sleep(5)

# Save jobs
listings_list = driver.find_elements(By.CSS_SELECTOR, '.scaffold-layout__list-container .ember-view .job-card-container--clickable')
for listing in listings_list:
    listing.click()
    time.sleep(3)
    save_button = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
    save_button.click()
