from selenium import webdriver
import unittest
from Pages.homePage import HomePage
from Pages.emailPage import EmailPage
from Pages.passwordPage import PasswordPage
from Pages.search import SearchPage
from Pages.pageNumberClick import PageNumberClick
from Pages.addWishList import AddWishList

class amazonTest(unittest.TestCase):



    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/Selenium/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_amazon_case(self):
        driver = self.driver

        mailaddress = 'gulsan.celep@useinsider.com'
        loginpassword = 'wsxzaq1'

        driver.get("https://www.amazon.com/")

        home = HomePage(driver)
        self.driver.implicitly_wait(5)
        home.click_sign_in()

        email = EmailPage(driver)
        email.enter_email(mailaddress)
        email.click_continue()

        password = PasswordPage(driver)
        password.enter_password(loginpassword)
        password.click_sign_in()

        search = SearchPage(driver)
        search.enter_search_keyword("Samsung")
        search.click_search()

        page2 = PageNumberClick(driver)
        page2.click_page_2()
        page2.click_third_product()

        addwishlist = AddWishList(driver)
        addwishlist.click_add_to_list()
        addwishlist.click_wish_list()
        addwishlist.click_create_list()
        addwishlist.click_wiew_list()
        self.driver.implicitly_wait(5)
        addwishlist.delete_from_wish_list()

        self.driver.implicitly_wait(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
