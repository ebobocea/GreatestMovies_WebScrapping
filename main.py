from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="h3", class_="title")
article_texts = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
article_texts.reverse()

with open('FilmsToWatch.txt', 'w', encoding="utf-8") as f:
    for article in article_texts:
        f.write(f"{article}\n")


