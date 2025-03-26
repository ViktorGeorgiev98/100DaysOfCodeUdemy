from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self):
        self.url = "https://www.billboard.com/charts/hot-100/2000-08-12"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
        }
        self.webpage = requests.get(url=self.url, headers=self.header)
        self.soup = BeautifulSoup(self.webpage.text, "html.parser")

    def get_first_100_titles(self):
        song_names_spans = self.soup.select("li ul li h3")
        song_names = [song.getText().strip() for song in song_names_spans]
        return song_names
