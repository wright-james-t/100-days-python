import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
MOVIE_BASE = requests.get(URL)
# Write your code below this line 👇
movie_page_text = MOVIE_BASE.text
soup = BeautifulSoup(movie_page_text, "html.parser")

movie_name_ranking = {}

movies_list = soup.find_all(name="h3", class_="title")

for movie in movies_list:
    try:
        name_rank = movie.getText().split(')')
        movie_name_ranking[int(name_rank[0])] = name_rank[1]
    except:
        name_rank = movie.getText().split(':')
        movie_name_ranking[int(name_rank[0])] = name_rank[1]

# for num in range(1, 101):
#     print(f"{num + 1} - {movie_name_ranking[num]}")

movie_name_ranking_reversed = OrderedDict(reversed(list(movie_name_ranking.items())))

