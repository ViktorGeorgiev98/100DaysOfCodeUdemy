from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule
import time

GAME_IS_ON = True
five_min = time.time() + 60 * 5  # 5 minutes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1920, 1080)  # Set the window size to full screen


driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//p[@class='fc-button-label'][text()='Consent']").click()
driver.implicitly_wait(2)
driver.find_element(
    By.XPATH, "//div[@class='langSelectButton title'][text()='English']"
).click()
driver.implicitly_wait(2)


def my_task():
    # Get all upgrade <b> tags
    all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
    item_prices = []

    # Convert <b> text into an integer price.
    for price in all_prices:
        element_text = price.text
        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)

    # Create dictionary of store items and prices
    cookie_upgrades = {}
    for n in range(len(item_prices)):
        cookie_upgrades[item_prices[n]] = item_ids[n]

    # Get current cookie count
    money_element = driver.find_element(by=By.ID, value="cookies").text.split(" ")[0]
    if "," in money_element:
        money_element = money_element.replace(",", "")
    cookie_count = int(money_element)

    # Find upgrades that we can currently afford
    affordable_upgrades = {}
    for cost, id in cookie_upgrades.items():
        if cookie_count > cost:
            affordable_upgrades[cost] = id

    # Purchase the most expensive affordable upgrade
    highest_price_affordable_upgrade = max(affordable_upgrades)
    print(highest_price_affordable_upgrade)
    to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

    driver.find_element(by=By.ID, value=to_purchase_id).click()


def stop_game():
    global GAME_IS_ON
    GAME_IS_ON = False
    cookie_per_s = driver.find_element(by=By.ID, value="cps").text
    print(cookie_per_s)


schedule.every(5).seconds.do(my_task)
schedule.every(300).seconds.do(stop_game)

while GAME_IS_ON:
    schedule.run_pending()
    driver.find_element(By.ID, "bigCookie").click()

driver.quit()
