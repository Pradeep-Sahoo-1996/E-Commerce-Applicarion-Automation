#Check out the Product

import pytest
from selenium.webdriver.common.by import By

def test_checkout_with_product(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "cartur").click()
    driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()
    driver.find_element(By.ID, "name").send_keys("Pradeep Kumar")
    driver.find_element(By.ID, "country").send_keys("India")
    driver.find_element(By.ID, "city").send_keys("Delhi")
    driver.find_element(By.ID, "card").send_keys("123450089235000")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2024")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Purchase')]").click()
    if test_checkout_with_product in driver:
        print("The Product is add to cart")
    else:
        print("The Product is not add to cart")

def test_checkout_without_product(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "cartur").click()
    if test_checkout_without_product in driver:
        print("your cart is empty")

