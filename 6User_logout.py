#Logout the User

import pytest
from selenium.webdriver.common.by import By

def test_logout(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "logout2").click()
    if test_logout in driver:
        print("Successfully Logout")
    return False
