from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Constants
WIKI_URL = 'https://en.wikipedia.org/wiki/Main_Page'
FORM_URL = 'https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/'

# Instantiating Selenium Stuff
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# WIKI PROJECT
# driver.get(WIKI_URL)

# # Getting article count link
# article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
#
# # Clicking on it
# article_count.click()
#
# # Finding a clickable link by using the text itself in the tag
# view_source = driver.find_element(By.LINK_TEXT, "View source")
#
# # Clicking on it
# view_source.click()

# Finding search bar
# search = driver.find_element(By.NAME, 'search')
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# FORM PROJECT
driver.get(FORM_URL)

# Get form info/fetch elements
first_name = driver.find_element(By.NAME, 'fName')
last_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')

# Input data for the form and hit 'Enter' to submit
first_name.send_keys("James")
last_name.send_keys("Wright")
email.send_keys("not-a-real-email@not-a-real-domain.com")
email.send_keys(Keys.ENTER)

# Quit selenium
# driver.quit()
