from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
class CartPage(BasePage):

    #locators 

    input=(By.NAME,"q")
    search_button=(By.XPATH, "//button[@type='submit']")
    ram_selected=(By.XPATH, "//div[@title='1GB and Below']//div[@class='XqNaEv']")
    image_product=(By.XPATH,"//img[@alt='Apple iPhone 16 (Black, 128 GB)']")
   

    def __init__(self, driver,getURL):
        super().__init__(driver)
        self.driver.get(getURL)

    def search_smartphone(self,text):
        self.enter_text(*self.input,text)
        time.sleep(3)
        #self.enter_text(*self.input,Keys.ENTER)
        self.click(*self.search_button)
        time.sleep(1)
        self.click(*self.ram_selected)
        time.sleep(1)
        self.click(*self.image_product)
        time.sleep(1)


    def get_cardbutton(self,text):
        
        self.driver.switch_to.window(self.driver.window_handles[1])
        print("Current URL", str(self.getcurrentURL()))
        time.sleep(1)
        add_card_button=(By.TAG_NAME,"button")
        flag=0
        element=self.find_element(*add_card_button)
        time.sleep(1)
        for i in element:
            if i.text==text:
                flag=1
                return flag
                 

        
         

       
            
