from Locators.locators import Locators

class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.sign_in_button_xpath = Locators.sign_in_button_xpath

    def click_sign_in(self):
        if "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more" in self.driver.title:
            self.driver.find_element_by_xpath(Locators.sign_in_button_xpath).click()
