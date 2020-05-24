import requests
from bs4 import BeautifulSoup
import mechanicalsoup
import pymongo
browser = mechanicalsoup.StatefulBrowser()
req = requests.get("https://today.line.me/ID/pc")
soup = BeautifulSoup(req.text, "lxml")

popular = soup.find_all(class_="_side_popular_100270")[0].find_all("li")


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["linetoday"]
mycol = mydb["popular"]


def render_url(url):
    browser.open(url)
    news = browser.get_current_page()
    title = news.find("h1",class_="news-title").text
    publisher = news.find("dd", class_="publisher").text.rstrip().lstrip()
    date_published = news.find("dd", class_="date").text
    content = news.find("article", class_="news-content")
    text = content.text
    # description = soup.find("meta", property="og:description").text
    return {
        "title" : title,
        "publisher" : publisher,
        "date_published" : date_published,
        "content" : str(content),
        "text" : text,
        "url" : url
        # "description" : description
    }

data = []
for pop in popular:
    link = pop.find("a").get("href")
    data.append(render_url(link))
#
data = mycol.insert_many(data)
print("Berhasil menyimpan data")
