from Locators.locators import Locators

class SearchPage():
    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_id = Locators.search_textbox_id
        self.search_button_xpath = Locators.search_button_xpath

    def enter_search_keyword(self, keyword):
        self.driver.find_element_by_id(Locators.search_textbox_id).clear()
        self.driver.find_element_by_id(Locators.search_textbox_id).send_keys(keyword)

    def click_search(self):
        self.driver.find_element_by_xpath(Locators.search_button_xpath).click()
