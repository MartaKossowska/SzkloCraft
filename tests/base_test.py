import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.spectrum_page import SpectrumGlassPage
from pages.cart_page import CartPage


class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):

        cService = webdriver.ChromeService(executable_path='/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=cService)
        self.driver.maximize_window()
        self.driver.get("https://www.szklocraft.pl/")
        self.driver.implicitly_wait(4)
        self.home_page = HomePage(self.driver)
        self.spectrum_page = SpectrumGlassPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def tearDown(self):
        self.driver.quit()
