import requests
from bs4 import BeautifulSoup

highest_upvote_id = 0
highest_upvotes = 0

site = requests.get("https://news.ycombinator.com/")

yc_web_page = site.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_='titleline', selector="a")
base_ids = soup.find_all(name="tr", class_="athing")
article_ids = []

for tag in base_ids:
    article_ids.append(tag.get('id'))

for article_id in article_ids:
    article = soup.find(name="tr", class_="athing", id=article_id)
    article_link = article.select_one(selector="span a").get("href")
    article_text = article.find(class_="titleline").getText()
    try:
        article_upvote = soup.find(name="span", id=f"score_{article_id}").getText()
        article_upvote = int(article_upvote.split()[0])
        if article_upvote > highest_upvotes:
            highest_upvotes = article_upvote
            highest_upvote_id = article_id
    except AttributeError:
        print(f"No upvotes found for {article_id}\n\n")

highest_article = soup.find(name="tr", class_="athing", id=highest_upvote_id)
highest_article_link = highest_article.select_one(selector="span a").get("href")
highest_article_text = highest_article.find(class_="titleline").getText()

print(f"{highest_article_text}\n{highest_article_link}\n{highest_upvotes}\n\n")
