from bs4 import BeautifulSoup
import requests

# get html of the website
response = requests.get("https://news.ycombinator.com/news")

# set the response text to a variable
yc_web_page = response.text

# parse the html with beautiful soup
soup = BeautifulSoup(yc_web_page, "html.parser")
# work with soup
article_tag = soup.find_all(name="a", class_="storylink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()
print(article_text, article_link, article_upvote)
