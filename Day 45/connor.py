from bs4 import BeautifulSoup
import requests
import re

url = "https://www.empireonline.com/movies/features/best-movies-2/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

movie = soup.find_all("h3")

print(movie)