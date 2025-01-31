from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    #locators
    USERNAME_INPUT=(By.ID,"uname")
    PASSWORD_INPUT=(By.ID,"pwd")
    LOGIN_BUTTON=(By.XPATH,"//input[@value='Login']")

    def __init__(self, driver,URL):
        super().__init__(driver)
        self.driver.get(URL)
    def enter_username(self,username):
        self.enter_text(*self.USERNAME_INPUT,username)
    def enter_password(self,password):
        self.enter_text(*self.PASSWORD_INPUT,password)
    def click_login(self):
        self.click(*self.LOGIN_BUTTON)





