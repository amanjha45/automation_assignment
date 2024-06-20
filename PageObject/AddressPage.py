from selenium.webdriver.common.by import By


class AddAddressPage:
    """

    """

    address_link = (By.XPATH, "//a[normalize-space()='shipping and billing addresses']")
    adit_add = (By.XPATH, "//a[@href='https://practice.automationtesting.in/my-account/edit-address/billing']")
    first_name = (By.ID, "billing_first_name")
    last_name = (By.ID, "billing_last_name")
    country_drop_down = (By.ID, "s2id_billing_country")
    country_input_bar = (By.ID, "s2id_autogen1_search")
    country_list = (By.XPATH, "//*[@id='select2-drop']/ul//li/div")
    state_drop_down = (By.ID, "s2id_billing_state")
    state_input_bar = (By.ID, "s2id_autogen2_search")
    state_list = (By.XPATH, "//*[@id='select2-drop']/ul//li/div")
    save_address_button = (By.XPATH, "//input[@name='save_address']")
    address_bar = (By.ID, "billing_address_1")
    postal_code = (By.ID, "billing_postcode")
    existing_address = (By.XPATH, "//a[normalize-space()='Addresses']")
    saved_add = (By.XPATH, "//div[@class='u-column2 col-2 woocommerce-Address']//address")

    def __init__(self, driver):
        self.driver = driver

    def click_on_address_link(self):
        return self.driver.find_element(*AddAddressPage.address_link).click()

    def click_on_edit_add(self):
        return self.driver.find_element(*AddAddressPage.adit_add).click()

    def enter_first_name(self, input: str):
        return self.driver.find_element(*AddAddressPage.first_name).send_keys(input)

    def enter_last_name(self, input: str):
        return self.driver.find_element(*AddAddressPage.last_name).send_keys(input)

    def get_country_name_list(self, input: str):
        self.driver.find_element(*AddAddressPage.country_drop_down).click()
        self.driver.find_element(*AddAddressPage.country_input_bar).send_keys(input)
        return self.driver.find_elements(*AddAddressPage.country_list)

    def get_sate_list(self, input: str):
        self.driver.find_element(*AddAddressPage.state_drop_down).click()
        self.driver.find_element(*AddAddressPage.state_input_bar).send_keys(input)
        return self.driver.find_elements(*AddAddressPage.state_list)

    def enter_address(self, input: str):
        return self.driver.find_element(*AddAddressPage.address_bar).send_keys(input)

    def click_on_save_button(self):
        return self.driver.find_element(*AddAddressPage.save_address_button).click()

    def check_existing_address(self):
        self.driver.find_element(*AddAddressPage.existing_address).click()

    def check_saved_add(self):
        return self.driver.find_element(*AddAddressPage.saved_add).text

