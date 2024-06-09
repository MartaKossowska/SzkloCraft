

class BasePage:
    """
    Base class for each Page
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(4)
