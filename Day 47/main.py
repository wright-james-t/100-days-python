import requests
from bs4 import BeautifulSoup
import lxml

MY_URL = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
MY_BUY_PRICE = 100.00

MY_HEADERS = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    "Accept-Language": 'en-US,en;q=0.9'
}

response = requests.get(url=MY_URL, headers=MY_HEADERS)
soup = BeautifulSoup(response.text, features="lxml")

item_current_price = float(soup.find(class_='a-price-whole').text + soup.find(class_='a-price-fraction').text)

if item_current_price < MY_BUY_PRICE:
    print("BUY NOW")
else:
    print("NO BUY NOW")