from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage


class SpectrumPageLocators:
    SELECT_IN_STOCK = (By.XPATH, '//*[@id="selectProductSort"]')
    FIRST_PRODUCT = (By.XPATH, "//*[@id='product_list']/li[1]")
    ADD_TO_BASKET = (By.XPATH, '//*[@id="product_list"]/li[1]/div/div[2]/div[2]/a[1]/span')
    GO_TO_CART = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[5]/a/span')


class SpectrumGlassPage(BasePage):
    """
    Spectrum Glass Page object
    """
    def select_on_stock(self):
        # selects from menu option "w magazynie"
        select_element = self.driver.find_element(*SpectrumPageLocators.SELECT_IN_STOCK)
        select = Select(select_element)
        select.select_by_value("quantity:desc")

    def choose_first_item_and_add_to_cart(self):
        # finds first item for sale on page, then hover over it until additional menu appears
        # next finds and clicks on "dodaj do koszyka" button
        first_item = self.driver.find_element(*SpectrumPageLocators.FIRST_PRODUCT)
        hover = ActionChains(self.driver).move_to_element(first_item)
        hover.perform()
        wait = WebDriverWait(self.driver, 5)
        menu_element = wait.until(EC.visibility_of_element_located(SpectrumPageLocators.ADD_TO_BASKET))
        dodaj_do_koszyka = menu_element.find_element(*SpectrumPageLocators.ADD_TO_BASKET)
        dodaj_do_koszyka.click()

    def go_to_cart(self):
        # finds and clicks on "go to cart" button and returns Cart Page
        go_to_cart = self.driver.find_element(*SpectrumPageLocators.GO_TO_CART)
        go_to_cart.click()
        return CartPage(self.driver)
