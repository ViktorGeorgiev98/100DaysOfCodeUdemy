import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in all_movies]
reversed_movies = movies[::-1]

# first way
# movies_text = "\n".join(reversed_movies)
# with open(
#     "day_45_web_scraping_with_beautiful_soup\\Starting Code - 100 movies to watch start\\movies.txt",
#     "a",
#     encoding="utf-8",
# ) as movies:
#     movies.write(movies_text)

# second way
with open(
    "day_45_web_scraping_with_beautiful_soup\\Starting Code - 100 movies to watch start\\movies.txt",
    "a",
    encoding="utf-8",
) as movies:
    for movie in reversed_movies:
        movies.write(f"{movie}\n")
