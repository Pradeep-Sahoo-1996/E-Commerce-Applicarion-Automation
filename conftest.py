#Get the Url throug browser
from selenium import webdriver
import pytest

@pytest.fixture(scope= "module")
def driver():
    driver = webdriver.Chrome(executable_path='C:/Assignment/chromedriver')
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.demoblaze.com/")
    driver.quit()
    