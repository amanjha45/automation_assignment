from selenium.webdriver.common.by import By


class LoginReg:
    reg_email = (By.XPATH, "//input[@id='reg_email']")
    reg_password = (By.XPATH, "//input[@id='reg_password']")
    login_email = (By.XPATH, "//input[@id='username']")
    login_password = (By.XPATH, "//input[@id='password']")
    reg_button = (By.XPATH, "//input[@name='register']")
    login_button = (By.XPATH, "//input[@name='login']")
    password_check = "//div[@class='woocommerce-password-strength strong']"
    hello_message = "//p[contains(text(),'Hello')]"


    def __init__(self, driver):
        self.driver = driver

    def reg_email_fun(self, key: str):
        self.driver.find_element(*LoginReg.reg_email).send_keys(key)

    def reg_pass_fun(self, key: str):
        self.driver.find_element(*LoginReg.reg_password).send_keys(key)

    def login_email_fun(self, key: str):
        self.driver.find_element(*LoginReg.login_email).send_keys(key)

    def login_pass_fun(self, key: str):
        self.driver.find_element(*LoginReg.login_password).send_keys(key)

    def reg_button_fun(self):
        self.driver.find_element(*LoginReg.reg_button).click()

    def login_button_fun(self):
        self.driver.find_element(*LoginReg.login_button).click()

    def pasword_strenght_fun(self):
        return self.driver.find_element(*LoginReg.password_check)



