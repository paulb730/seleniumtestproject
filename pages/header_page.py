from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import BasePage

class HeaderPage(BasePage):

    #locators
    header=(By.CLASS_NAME,"header")
    h1=(By.TAG_NAME,"h1")


    def __init__(self, driver,URL):
        super().__init__(driver)
        self.driver.get(URL)
        
    def checker(self,text):
        flag=0
        header=self.find_element_specific(*self.header)
        catched_child=header.find_element(*self.h1)
        print(catched_child)
        if str(catched_child.text)==text:
                flag=1
                return flag            
            


