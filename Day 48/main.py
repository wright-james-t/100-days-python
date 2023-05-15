from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pprint import pprint as pp
from datetime import datetime, timedelta

# Constants
COOKIE_URL = 'http://orteil.dashnet.org/experiments/cookie/'

# Instantiating Selenium Stuff
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(COOKIE_URL)

# Timer
loop_end = datetime.now() + timedelta(seconds=300)
inner_loop_timer = datetime.now() + timedelta(seconds=1)

# # Instantiating upgrade dict
# upgrade_dict = {}
#
# # Finding all the elements
# store_elements = driver.find_elements(By.CSS_SELECTOR, '#store div')
#
# # Adding to dict for initial prices
# for index in range(len(store_elements) - 1):
#     upgrade_id = store_elements[index].get_attribute('id')
#     upgrade_cost_html = store_elements[index].text.split(' - ')
#     upgrade_cost = int(upgrade_cost_html[1].split('\n')[0].replace(',', ''))
#     upgrade_dict[upgrade_id] = upgrade_cost
#
# reversed_dict = dict(sorted(upgrade_dict.items(), key=lambda item: item[1], reverse=True))

# # Starting the loop for 5 minutes
# while datetime.now() < loop_end:
#     # Re-find and print CPS when the loop restarts, also reinstantiate big cookie
#     big_cookie = driver.find_element(By.ID, 'cookie')
#     cps = driver.find_element(By.ID, 'cps').text
#     print(cps)
#     # Click until the loop end timer is done
#     while inner_loop_timer > datetime.now():
#         big_cookie.click()
#
#     # Update our money amount
#     money = int(driver.find_element(By.ID, 'money').text)
#
#     # Loop through upgrades, stop after finding one we can buy
#     for upgrade_id, cost in reversed_dict.items():
#         if money > cost:
#             button = driver.find_element(By.ID, upgrade_id)
#             button.click()
#
#             # Re-find necessary elements after the page refresh
#             button = driver.find_element(By.ID, upgrade_id)
#             new_cost_html = button.text.split(' - ')
#             new_cost = int(new_cost_html[1].split('\n')[0].replace(',', ''))
#             reversed_dict[upgrade_id] = new_cost
#
#             # Break out back to the main loop now that we bought something
#             break
#
#     # Reset loop timer
#     inner_loop_timer = datetime.now() + timedelta(seconds=1)

# Starting the loop for 5 minutes
while datetime.now() < loop_end:
    # Re-find and print CPS when the loop restarts, also reinstantiate big cookie
    big_cookie = driver.find_element(By.ID, 'cookie')
    cps = driver.find_element(By.ID, 'cps').text
    print(cps)
    # Click until the loop end timer is done
    while inner_loop_timer > datetime.now():
        big_cookie.click()

    # Update our money amount
    money = int(driver.find_element(By.ID, 'money').text)

    # Finding all the elements
    store_elements = driver.find_elements(By.CSS_SELECTOR, '#store div')

    # Instantiating upgrade dict
    upgrade_dict = {}

    # Adding to dict for initial prices
    for index in range(len(store_elements) - 1):
        upgrade_id = store_elements[index].get_attribute('id')
        upgrade_cost_html = store_elements[index].text.split(' - ')
        if len(upgrade_cost_html) >= 2:
            upgrade_cost = int(upgrade_cost_html[1].split('\n')[0].replace(',', ''))
            upgrade_dict[upgrade_id] = upgrade_cost

    reversed_dict = dict(sorted(upgrade_dict.items(), key=lambda item: item[1], reverse=True))

    # Loop through upgrades, stop after finding one we can buy
    for upgrade_id, cost in reversed_dict.items():
        if money > cost:
            button = driver.find_element(By.ID, upgrade_id)
            button.click()

            # Re-find necessary elements after the page refresh
            try:
                button = driver.find_element(By.ID, upgrade_id)
                new_cost_html = button.text.split(' - ')
                if len(new_cost_html) >= 2:
                    new_cost = int(new_cost_html[1].split('\n')[0].replace(',', ''))
                    reversed_dict[upgrade_id] = new_cost
            except:
                pass

            # Break out back to the main loop now that we bought something
            break

    # Reset loop timer
    inner_loop_timer = datetime.now() + timedelta(seconds=1)







