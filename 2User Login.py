#login With this Application

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("username, password", [("pradeep1234@gmail.com", "pradeep1234@"), ("invalid_user", "invalid_password")])
def test_login(driver, username, password):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "login2").click()
    driver.find_element(By.ID, "loginusername").send_keys(username)
    driver.find_element(By.ID, "loginpassword").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()
    
    if test_login == driver:
        print("Login Successfully")
    else:
        print("Enter Valid data")