from selenium.webdriver.common.by import By


class UserProfile:
    sign_out = (By.XPATH, "//a[normalize-space()='Sign out']")
    cart_box = (By.CLASS_NAME, "cartcontents")
    shop_button = (By.XPATH, "//a[normalize-space()='Shop']")

    def __init__(self, driver):
        self.driver = driver

    def sign_out_user(self):
        self.driver.find_element(*UserProfile.sign_out).click()

    def check_cart_box(self):
        self.driver.find_element(*UserProfile.cart_box).click()

    def shop_button_fun(self):
        self.driver.find_element(*UserProfile.shop_button).click()
