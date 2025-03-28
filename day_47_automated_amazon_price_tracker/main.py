from scraper import Scraper
from email_sender import Mail_Sender

scraper = Scraper()
email_sender = Mail_Sender()
pot_price = scraper.get_price_of_pot()
if pot_price < 100:
    email_sender.send_email(price=pot_price, url=scraper.base_url)
