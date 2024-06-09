import re
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import random


class CartPageLocators:
    NO_OF_ITEMS_IN_CART = (By.XPATH, "//*[@class='cart_quantity_input form-control grey']")
    PLUS_ICON = (By.ID, "cart_quantity_up_126_0_0_0")
    MINUS_ICON = (By.XPATH, "//*[@class='icon-minus']")
    TRASH_ICON = (By.ID, "126_0_0_0")
    ITEM_PRICE = (By.ID, "product_price_126_0_0")
    TOTAL_PRICE = (By.ID, "total_product_price_126_0_0")
    TOTAL_NO_OF_ITEMS_IN_CART_UPPER_MSG = (By.ID, "summary_products_quantity")
    EMPTY_CART_MESSAGE = (By.XPATH, "//*[@class='alert alert-warning']")


class CartPage(BasePage):
    """
    Cart Page object
    """

    def get_no_of_items_upper_message(self):
        # gets from Cart Page message that informs user of total number of items in cart
        element = self.driver.find_element(*CartPageLocators.TOTAL_NO_OF_ITEMS_IN_CART_UPPER_MSG)
        text_content = element.text
        return text_content

    def get_item_price(self):
        # gets from table on Cart Page unit price of item in cart and extracts numerical value
        element = self.driver.find_element(*CartPageLocators.ITEM_PRICE)
        text_content = element.text
        initial_item_price = float(text_content.replace(' zł', '').replace(',', '.'))
        return initial_item_price

    def get_total_price(self):
        # gets from table on Cart Page total price of item/s in cart and extracts numerical value
        element = self.driver.find_element(*CartPageLocators.TOTAL_PRICE)
        text_content = element.text
        final_item_price = float(text_content.replace(' zł', '').replace(',', '.'))
        return final_item_price

    def click_plus_icon_randomly(self):
        # finds "plus icon" on Cart Page (table) and clicks on it randomly (1 to 3 times)
        # also prints number drawn and returns number of clicks
        plus_button = self.driver.find_element(*CartPageLocators.PLUS_ICON)
        click_times = random.randint(1, 3)
        print(f"Number of clicks on plus icon: {click_times}")
        for element in range(click_times):
            plus_button.click()
        return click_times

    def click_minus_icon_randomly(self):
        # finds minus icon on Cart Page (table) and gets current number of items in cart
        # then clicks randomly (1 to 3 times) on minus icon, but makes sure that at lest one item will remain in cart
        # prints number of items in cart before cliks and number of cliks
        # returns number of minus cliks
        minus_button = self.driver.find_element(*CartPageLocators.MINUS_ICON)
        current_items_count = self.get_number_of_items_in_cart_from_table()
        print(f'Before clicking on minus icon there are: {current_items_count} items in cart.')
        if current_items_count > 1:
            minus_clicks = random.randint(1, min(3, current_items_count - 1))
            print(f"Number of cliks on minus icon: {minus_clicks}")
            for _ in range(minus_clicks):
                minus_button.click()
            return minus_clicks
        else:
            print("There is only one item i cart, so clicking on minus icon was not possible.")
            return 0

    def compare_total_price_after_plus_click(self, click_times):
        # checks if total price after plus clicks is correspondingly higher
        initial_item_price = self.get_item_price()
        print(f"Unit price for an item: {initial_item_price:.2f} zl")

        new_total_price = self.get_total_price()
        print(f"Final price for items: {new_total_price:.2f} zl")

        if new_total_price == initial_item_price + (initial_item_price * click_times):
            print("Final price is correspondingly higher.")
        else:
            print("Final price is NOT correspondingly higher.")

    def compare_total_price_after_minus_click(self):
        # checks if total price after minus clicks is correspondingly lower.
        initial_item_price = self.get_item_price()
        print(f"Unit price for an item: {initial_item_price:.2f} zl")

        new_total_price = self.get_total_price()
        print(f"Final price for items: {new_total_price:.2f} zl")

        numbers_of_items_in_cart = self.get_number_of_items_in_cart_from_table()

        if new_total_price == initial_item_price * numbers_of_items_in_cart:
            print("Final price is correspondingly lower.")
        else:
            print("Final price is NOT correspondingly lower.")

    def get_total_number_of_items_in_cart_from_upper_corner(self):
        # extracts numerical value from message informing costumer about number of items in cart
        # message is located in upper right side of site
        message = self.driver.find_element(*CartPageLocators.TOTAL_NO_OF_ITEMS_IN_CART_UPPER_MSG).text
        number = int(re.search(r'\d+', message).group())
        return number

    def get_number_of_items_in_cart_from_table(self):
        # gets number of items in cart from the table and returns it in form of an integer
        element = self.driver.find_element(*CartPageLocators.NO_OF_ITEMS_IN_CART)
        value = element.get_attribute("value")
        if value is not None:
            number = int(value)
            return number
        else:
            return None

    def click_trash_icon(self):
        # finds and clicks on trashcan icon - removes all items from cart
        element = self.driver.find_element(*CartPageLocators.TRASH_ICON)
        element.click()

    def get_empty_cart_message(self):
        # gets text message about empty cart from alert banner
        element = self.driver.find_element(*CartPageLocators.EMPTY_CART_MESSAGE)
        text_content = element.text
        return text_content
