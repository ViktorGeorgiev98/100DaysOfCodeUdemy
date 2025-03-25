from bs4 import BeautifulSoup

# Open the HTML file in the same folder as this script
with open(
    "day_45_web_scraping_with_beautiful_soup\\bs4-start\\website.html",
    "r",
    encoding="utf-8",
) as html_file:
    content = html_file.read()

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(content, "html.parser")

# Print the parsed HTML content
# print(soup.title)
# print(soup.title.string)


# finding and selecting particular elements

# find all anchor tags
# all_anchor_tags = soup.find_all(name="a")
# find all paragraph tags
# all_paragraph_tags = soup.find_all(name="p")

# text in anchor tags
# for tag in all_anchor_tags:
#     print(tag.getText())

# get the links
# for tag in all_anchor_tags:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# when searching for a specific class we need to _ (underscore), because class is reserved in python
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.text)

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".heading")
print(headings)
