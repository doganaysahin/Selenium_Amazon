from Locators.locators import Locators

class EmailPage():
    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_id = Locators.email_textbox_id
        self.email_continue_id = Locators.email_continue_id

    def enter_email(self, email):
        self.driver.find_element_by_id(Locators.email_textbox_id).clear()
        self.driver.find_element_by_id(Locators.email_textbox_id).send_keys(email)

    def click_continue(self):
        self.driver.find_element_by_id(Locators.email_continue_id).click()