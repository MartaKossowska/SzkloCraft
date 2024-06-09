from pages.base_page import BasePage
from pages.spectrum_page import SpectrumGlassPage
from selenium.webdriver.common.by import By


class HomePageLocators:
    COOKIE_BUTTON = (By.ID, "x13pmcookiebar-acceptation")
    EMAIL_INPUT = (By.ID, 'newsletter-input')
    USER_ERROR_MESSAGE_BANNER = (By.XPATH, "//*[@class='alert alert-danger']")
    EMAIL_SUBMIT_BTN = (By.NAME, 'submitNewsletter')
    SZKLO_MENU_PLUS = (By.XPATH, "//*[@class='grower CLOSE']")
    SPECTUM_LINK = (By.XPATH, '//*[@id="categories_block_left"]/div/ul/li[1]/ul/li[1]/a')


class HomePage(BasePage):
    """
    Landing Page object
    """

    def cookie_button_click(self):
        # accepts cookie message
        cookie_button = self.driver.find_element(*HomePageLocators.COOKIE_BUTTON)
        cookie_button.click()

    def enter_email(self, bad_email):
        # enters modified email into subscription box
        el = self.driver.find_element(*HomePageLocators.EMAIL_INPUT)
        el.send_keys(bad_email)

    def click_submit_email_btn(self):
        # submits modified email
        el = self.driver.find_element(*HomePageLocators.EMAIL_SUBMIT_BTN)
        el.click()

    def get_user_error_message(self):
        # finds email-error banner and extracts error message from it
        element = self.driver.find_element(*HomePageLocators.USER_ERROR_MESSAGE_BANNER)
        text_content = element.text
        return text_content

    def open_side_menu(self):
        # opens side menu
        el = self.driver.find_element(*HomePageLocators.SZKLO_MENU_PLUS)
        el.click()

    def open_spectrum_page(self):
        # finds and clicks on Spectrum Glass link from opened side menu and returns Spectrum Page
        link = self.driver.find_element(*HomePageLocators.SPECTUM_LINK)
        link.click()
        return SpectrumGlassPage
