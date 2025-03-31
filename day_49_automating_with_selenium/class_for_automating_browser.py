from selenium import webdriver
from selenium.webdriver.common.by import By


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

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
PAUSE = 2  # seconds


class Automating_Browser:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)  # Keep the
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.set_window_size(1920, 1080)  # Set the window size to 1920x1080

    def pause(self, PAUSE) -> None:
        self.driver.implicitly_wait(PAUSE)

    def open_url(self):
        self.driver.get(URL)
        self.pause(PAUSE)
        return self

    def login(self):
        try:
            self.driver.find_element(*username_field_by).clear()
            self.driver.find_element(*username_field_by).send_keys(USERNAME)
            self.driver.find_element(*password_field_by).clear()
            self.driver.find_element(*password_field_by).send_keys(PASSWORD)
            self.driver.find_element(*submit_login_button_by).click()
            self.pause(PAUSE)
        except:
            print("Login failed")
            raise Exception("Login failed")
        else:
            print("Logged in")
            return self

    def clear_cart(self):
        try:
            self.driver.find_element(*cart_icon_by).click()
            self.pause(PAUSE)
            cart_items = len(self.driver.find_elements(*remove_cart_item_button_by))
            if cart_items > 0:
                for _ in range(cart_items):
                    self.driver.find_element(*remove_cart_item_button_by).click()
                    self.pause(PAUSE)
            else:
                print("Cart is already empty")
        except:
            print("Failed to clear cart")
            raise Exception("Failed to clear cart")
        else:
            print("Cart cleared successfully")
            return self

    def go_to_all_items(self):
        try:
            self.driver.find_element(*nav_bar_by).click()
            self.pause(PAUSE)
            self.driver.find_element(*all_items_by).click()
        except:
            print("Failed to go to all items")
            raise Exception("Failed to go to all items")
        else:
            print("Navigated to all items successfully")
            return self

    def put_first_item_to_cart(self):
        try:
            self.driver.find_element(*first_item_add_to_cart_by).click()
        except:
            print("Failed to put first item to cart")
            raise Exception("Failed to put first item to cart")
        else:
            print("First item added to cart successfully")
            return self

    def check_that_item_was_added_to_cart(self):
        try:
            self.driver.find_element(*cart_icon_by).click()
            self.pause(PAUSE)
            cart_items = len(self.driver.find_elements(*remove_cart_item_button_by))
            if cart_items == 1:
                print("Item was added to cart successfully")
            else:
                print("Item was not added to cart")
        except:
            print("Failed to check if item was added to cart")
            raise Exception("Failed to check if item was added to cart")
        else:
            print("Checked that item was added to cart successfully")
            return self

    def close_browser(self) -> None:
        self.driver.quit()
        print("Browser closed successfully")
