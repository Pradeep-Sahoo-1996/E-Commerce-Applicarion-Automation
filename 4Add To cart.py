#Add The product in Cart

import pytest
from selenium.webdriver.common.by import By

def test_add_to_cart(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.LINK_TEXT, "Next").click()
    driver.find_element(By.LINK_TEXT, "Next").click()  # Adjust as necessary to navigate to the last page

    products = driver.find_elements(By.CLASS_NAME, "card-block")
    last_product = products[-1]
    last_product.find_element(By.TAG_NAME, "a").click()
    driver.find_element(By.LINK_TEXT, "Add to cart").click()
    if test_add_to_cart in driver:
        print("Product added to cart")
    return False


