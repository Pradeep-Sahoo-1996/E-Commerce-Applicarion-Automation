#Browsing The Product

import pytest
from selenium.webdriver.common.by import By

def test_browse_products(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.XPATH, "//a[@id = 'cat']").click() #Check if products are displayed
    for category in driver:
        category.click()
    print("Category Successfull Clicked")

    products = driver.find_elements_by_css_selector(".product-item")
    for product in products:
        product.click()
    print(products)


