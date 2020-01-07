from Locators.locators import Locators

class AddWishList():
    def __init__(self, driver):
        self.driver = driver

        self.get_text_id = Locators.get_text_id
        self.add_to_list_button_id = Locators.add_to_list_button_id
        self.wish_list_xpath = Locators.wish_list_xpath
        self.create_list_button_xpath = Locators.create_list_button_xpath
        self.view_list_button_link_text = Locators.view_list_button_link_text
        self.delete_from_wish_list_xpath = Locators.delete_from_wish_list_xpath

    def click_add_to_list(self):
        self.driver.find_element_by_id(Locators.add_to_list_button_id).click()

    def click_wish_list(self):
        self.driver.find_element_by_xpath(Locators.wish_list_xpath).click()

    def click_create_list(self):
        self.driver.find_element_by_xpath(Locators.create_list_button_xpath).click()

    def click_wiew_list(self):
        self.driver.find_element_by_link_text(Locators.view_list_button_link_text).click()

    def delete_from_wish_list(self):
        self.driver.find_element_by_xpath(Locators.delete_from_wish_list_xpath).click()