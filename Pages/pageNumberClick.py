from Locators.locators import Locators

class PageNumberClick():
    def __init__(self, driver):
        self.driver = driver

        self.page_number_link_text = Locators.page_number_link_text
        self.click_third_product_xpath = Locators.click_third_product_xpath

    def click_page_2(self):
        self.driver.find_element_by_link_text(Locators.page_number_link_text).click()

    def click_third_product(self):
        self.driver.find_element_by_xpath(Locators.click_third_product_xpath).click()
