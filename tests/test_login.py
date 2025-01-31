import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from pages.login_page import LoginPage
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

def test_valid_login(driver,URL="https://trytestingthis.netlify.app/"):
    login_page=LoginPage(driver,URL)
    login_page.enter_username("test")
    login_page.enter_password("test")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)
    assert "Successful" in  driver.page_source

        
