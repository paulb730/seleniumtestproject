import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from pages.header_page import HeaderPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService #use chrome service to automation
from webdriver_manager.chrome import ChromeDriverManager #manager the chrome driver


@pytest.fixture
def driver():
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_name_header(driver,URL="https://trytestingthis.netlify.app/"):
    header_page=HeaderPage(driver,URL)
    check_title=header_page.checker("Your Website to practice Automation Testing")
    time.sleep(1)
    assert check_title==1 


    

    


