from selenium.webdriver.common.by import By
from PageObject.LoginRagister import LoginReg


class CheckOutPage:

    product_list = (By.XPATH, "//table/tbody/tr/td[@class='product-name']")
    add_product = (By.XPATH, "//li[@class='post-169 ][normalize-space()='Add to basket']")
    delete_button = (By.XPATH, "//tbody/tr/td/a[@class='remove']")

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        pass
    def delete_product_from_cart(self):
        return self.driver.find_element(*CheckOutPage.delete_button).click()