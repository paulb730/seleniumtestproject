from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    
    def __init__(self,driver):
        self.driver=driver
        self.timeout=10

    def getcurrentURL(self):
        try:
            return self.driver.current_url
        except Exception as e: print (str(e))  

    def find_element(self,by,locator):
        return WebDriverWait(self.driver,self.timeout).until(
            EC.presence_of_all_elements_located((by,locator))
        )
    
    def find_element_specific(self,by,locator):
        try:
            return self.driver.find_element(by,locator)
        except Exception as e: print( str (e))     


    def switchwindowhandle(self):
        #store ID of the original window
        original_window=self.driver.current_window_handle

    

    def click(self,by,locator):
        element=self.find_element(by,locator)
        for i in element:
            i.click()
        

    


    def enter_text(self,by,locator,text):
        element=self.find_element(by,locator)
        for i in element:
            i.send_keys(text)
        
     




