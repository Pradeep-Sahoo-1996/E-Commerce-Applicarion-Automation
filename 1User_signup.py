#Signup with this E-commerce Application

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("username,password", [("pradeep1234@gmail.com", "pradeep1234@")])
def test_signup_valid(driver, username, password):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "signin2").click()
    driver.find_element(By.ID, "sign-username").send_keys("pradeep1234@gmail.com")
    driver.find_element(By.ID, "sign-password").send_keys("pradeep1234@")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign up')]").click()
    if test_signup_valid in driver:
        print("Test Passed")
    else:
        print("User already Exist")

@pytest.mark.parametrize("username,password", [("invalid_user", "invalid_password")])
def test_signup_invalid(driver, username, password):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "signin2").click()
    driver.find_element(By.ID, "sign-username").send_keys("invalid_user")
    driver.find_element(By.ID, "sign-password").send_keys("invalid_password")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign up')]").click()
    if test_signup_invalid in driver:
        print("Test Failed. Enter Valid User name and password")
    
