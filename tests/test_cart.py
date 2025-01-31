# Execute the test case 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from pages.cart_page import CartPage
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


def test_cart(driver, URL="https://www.flipkart.com"):
    #create object 
    testcard=CartPage(driver,URL)
    testcard.search_smartphone("iphone")
    assert "iphone" in driver.current_url




