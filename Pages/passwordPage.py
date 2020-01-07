from Locators.locators import Locators

class PasswordPage():
    def __init__(self, driver):
        self.driver = driver

        self.password_textbox_id = Locators.password_textbox_id
        self.password_sign_in_button_id = Locators.password_sign_in_button_id

    def enter_password(self, password):
        self.driver.find_element_by_id(Locators.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element_by_id(Locators.password_sign_in_button_id).click()