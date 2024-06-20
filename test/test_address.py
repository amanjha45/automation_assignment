import time
import pytest

from PageObject.AddressPage import AddAddressPage
from utilities.SetupClass import SetupClass


class TestCart(SetupClass):

    @pytest.mark.usefixtures("login_user")
    def test_add_address(self):
        """
        This API is created to test add address functionality
        :return:
        """
        add_page = AddAddressPage(self.driver)
        add_page.click_on_address_link()
        add_page.click_on_edit_add()
        add_page.enter_first_name("Test")
        add_page.enter_last_name("data")
        country_list = add_page.get_country_name_list("United States (US)")

        for country in country_list:
            if "United States (US)" == country.text:
                time.sleep(3)
                country.click()
                break

        add_page.enter_address("fvf")
        states = add_page.get_sate_list("Alaska")
        for state in states:
            if state.text == "Alaska":
                state.click()
                break

        add_page.click_on_save_button()

    @pytest.mark.usefixtures("login_user")
    def test_to_check_saved_address(self):
        """
        This API is used to validate the Saved address
        :return:
        """
        add_page = AddAddressPage(self.driver)
        add_page.check_existing_address()
        add = add_page.check_saved_add()
        log = self.getLogger()
        if not add:
            log.error("Address not saved")
        else:
            log.info("Address saved")
