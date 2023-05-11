from bs4 import BeautifulSoup

with open("website.html", 'r', encoding='utf-8') as file:
    file_contents = file.read()

soup = BeautifulSoup(file_contents, "html.parser")

# print(soup.prettify())

# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

heading = soup.find_all(name="h1", id="name")
# print(heading[0].getText())

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)
# print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
# print(company_url)

name = soup.select_one(selector="#name")
# print(name)

headings = soup.select(".heading")
print(headings)