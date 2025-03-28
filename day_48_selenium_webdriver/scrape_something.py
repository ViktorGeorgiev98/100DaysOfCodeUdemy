from selenium import webdriver
from selenium.webdriver.common.by import By

english_articles_by = (By.XPATH, "//a[@id='js-link-box-en']//small")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)  # initialize the driver

driver.get("https://www.wikipedia.org/")
driver.implicitly_wait(10)
english_articles = driver.find_element(*english_articles_by).text
print(english_articles)
driver.quit()
