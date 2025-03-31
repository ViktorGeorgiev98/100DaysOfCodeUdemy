from selenium import webdriver
from selenium.webdriver.common.by import By

# constants
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
PAUSE = 2  # seconds


# utils
def pause(seconds):
    driver.implicitly_wait(seconds)


def open_url(url):
    driver.get(url)
    pause(PAUSE)


def login():
    try:
        driver.find_element(*username_field_by).clear()
        driver.find_element(*username_field_by).send_keys(USERNAME)
        driver.find_element(*password_field_by).clear()
        driver.find_element(*password_field_by).send_keys(PASSWORD)
        driver.find_element(*submit_login_button_by).click()
        pause(PAUSE)
    except:
        print("Login failed")
        raise Exception("Login failed")
    else:
        print("Logged in")


def clear_cart():
    try:
        driver.find_element(*cart_icon_by).click()
        pause(PAUSE)
        cart_items = len(driver.find_elements(*remove_cart_item_button_by))
        if cart_items > 0:
            for _ in range(cart_items):
                driver.find_element(*remove_cart_item_button_by).click()
                pause(PAUSE)
        else:
            print("Cart is already empty")
    except:
        print("Failed to clear cart")
        raise Exception("Failed to clear cart")
    else:
        print("Cart cleared successfully")


def go_to_all_items():
    try:
        driver.find_element(*nav_bar_by).click()
        pause(PAUSE)
        driver.find_element(*all_items_by).click()
    except:
        print("Failed to go to all items")
        raise Exception("Failed to go to all items")
    else:
        print("Navigated to all items successfully")


def put_first_item_to_cart():
    try:
        driver.find_element(*first_item_add_to_cart_by).click()
    except:
        print("Failed to put first item to cart")
        raise Exception("Failed to put first item to cart")
    else:
        print("First item added to cart successfully")


def check_that_item_was_added_to_cart():
    try:
        driver.find_element(*cart_icon_by).click()
        pause(PAUSE)
        cart_items = len(driver.find_elements(*remove_cart_item_button_by))
        if cart_items == 1:
            print("Item was added to cart successfully")
        else:
            print("Item was not added to cart")
    except:
        print("Failed to check if item was added to cart")
        raise Exception("Failed to check if item was added to cart")


# variables and selectors
username_field_by = (By.ID, "user-name")
password_field_by = (By.ID, "password")
submit_login_button_by = (By.ID, "login-button")
cart_icon_by = (By.XPATH, "//*[@class='shopping_cart_link']")
remove_cart_item_button_by = (
    By.XPATH,
    "//*[@class='btn btn_secondary btn_small cart_button']",
)
nav_bar_by = (By.ID, "react-burger-menu-btn")
all_items_by = (By.ID, "inventory_sidebar_link")
first_item_add_to_cart_by = (
    By.XPATH,
    "(//*[@class='btn btn_primary btn_small btn_inventory '])[1]",
)

# chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    "detach", True
)  # Keep the browser open after script execution

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1920, 1080)  # Set the window size to 1920x1080

# actual code
open_url(URL)
login()
clear_cart()
go_to_all_items()
put_first_item_to_cart()
check_that_item_was_added_to_cart()
driver.quit()  # Close the browser when done
