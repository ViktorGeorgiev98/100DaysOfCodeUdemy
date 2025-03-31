from class_for_automating_browser import Automating_Browser

automated_browser = Automating_Browser()
(
    automated_browser.open_url()
    .login()
    .clear_cart()
    .go_to_all_items()
    .put_first_item_to_cart()
    .close_browser()
)
