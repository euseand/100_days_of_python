import bs4
import requests


site = requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text
soup = bs4.BeautifulSoup(site, "html.parser")

titles = soup.findAll("img")
titles = [title.get("alt") for title in titles]
titles = list(filter(lambda x: x, titles))

print(titles)
