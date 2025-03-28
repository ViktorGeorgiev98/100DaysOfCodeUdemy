from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self):
        self.base_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
            "Accept-Language": "en-US,en;q=0.9",
        }
        self.webpage = requests.get(self.base_url, headers=self.headers)
        self.soup = BeautifulSoup(self.webpage.content, "html.parser")

    def get_price_of_pot(self):
        price = self.soup.select_one(
            selector="span.a-price aok-align-center > span.a-offscreen"
        ).getText()
        price_without_currency = price.split("$")[1]
        self.pot_price = float(price_without_currency)
        return float(price_without_currency)
