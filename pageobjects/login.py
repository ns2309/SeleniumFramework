import time

from selenium.webdriver.common.by import By

from pageobjects.ShopPage import ShopPage
from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password = (By.NAME, "password")
        self.signButton = (By.ID, "signInBtn")


    def login(self,userEmail, userPassword):
        self.driver.find_element(*self.username_input).send_keys(userEmail)
        self.driver.find_element(*self.password).send_keys(userPassword)
        self.driver.find_element(*self.signButton).click()
        time.sleep(7)
        Shop_Page = ShopPage(self.driver)
        return Shop_Page
