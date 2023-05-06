import requests
from datetime import date
from datetime import timedelta
from dotenv import load_dotenv
from twilio.rest import Client
import os

# Loading .env file using dotenv module
load_dotenv()

# Stock API stuff here
STOCK_API = os.environ['ALPHA_API']
STOCK_URL = 'https://www.alphavantage.co/query?'
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_THRESHOLD = 1

# News API stuff here
NEWS_API = os.environ['NEWS_API']
NEWS_URL = 'https://newsapi.org/v2/everything?'

# Message API stuff here
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
MY_NUMBER = os.environ['MY_NUMBER']

# Getting the date for yesterday and the day before that in YYYY-MM-DD format and then turning it into a string
yesterday = str(date.today() - timedelta(days=1))
two_days_ago = str(date.today() - timedelta(days=2))


def check_percentage_difference(yesterday_value, two_days_ago_value):
    """Calculates the percentage difference of a given stock (params) over the last 2 days"""
    pdiff_updated = ((yesterday_value - two_days_ago_value) * 100) / yesterday_value
    return pdiff_updated


def get_news():
    """Obtains the top 3 news stories from the last 2 days for a given search term as defined by params"""
    # Use the requests module to make an API call
    news_response = requests.get(NEWS_URL, params=news_api_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    # List comprehension to add the headline and description to a list (3 total articles)
    formatted_messages = [f"Headline: {article['title']}\nBrief: {article['description']}\n\n"
                          for article in news_data['articles'][:3]]
    # Join and return the list of headlines/descriptions
    return ''.join(formatted_messages)


def send_message(pdiff):
    """Send text message to a person with 3 most popular news story for a stock over the last 2 days if change > 5%"""
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    if pdiff >= STOCK_THRESHOLD:
        title_line = f"{STOCK}: 🔺📈{pdiff}%"
    elif pdiff <= -STOCK_THRESHOLD:
        title_line = f"{STOCK}: 🔻📉{pdiff}%"
    news_articles = get_news()
    formatted_text = f"{title_line}\n\n{news_articles}"
    message = client.messages \
        .create(
            body=f"{formatted_text}",
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )


# Defining parameters for stock and sms
stock_api_parameters = {
    "function": 'TIME_SERIES_DAILY_ADJUSTED',
    "symbol": STOCK,
    "apikey": STOCK_API
}

news_api_parameters = {
    "q": COMPANY_NAME,
    "from": two_days_ago,
    "sortBy": 'popularity',
    "apiKey": NEWS_API,
    "pageSize": 3,
    "searchIn": 'title'
}

# Using requests module to send the API request to alphavantage
stock_response = requests.get(STOCK_URL, params=stock_api_parameters)
# Making sure the API request has no exceptions
stock_response.raise_for_status()
# Converting response to json
stock_data = stock_response.json()

# Pulling the closing stock price for each of the above vars
yesterday_close = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])
two_days_ago_close = float(stock_data['Time Series (Daily)'][two_days_ago]['4. close'])

# Set the percentage difference between 2 days ago and yesterday (closing)
pdiff = check_percentage_difference(yesterday_close, two_days_ago_close)

# If % difference is more than 5 (up or down), send a text with the news
if pdiff >= STOCK_THRESHOLD or pdiff <= -STOCK_THRESHOLD:
    send_message(pdiff)
else:
    print(check_percentage_difference(yesterday_close, two_days_ago_close))
    print(yesterday_close)
    print(two_days_ago_close)