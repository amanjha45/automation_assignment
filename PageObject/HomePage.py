from selenium.webdriver.common.by import By
from PageObject.LoginRagister import LoginReg


class HomePage:

    my_account = (By.XPATH, "//a[normalize-space()='My Account']")

    def __init__(self, driver):
        self.driver = driver

    def my_account_fun(self):
        self.driver.find_element(*HomePage.my_account).click()
        login_page = LoginReg(self.driver)
        return login_page
