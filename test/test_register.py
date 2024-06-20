import time
import pytest

from PageObject.HomePage import HomePage
from PageObject.UserProfile import UserProfile
from utilities.SetupClass import SetupClass


class TestLoginRegister(SetupClass):

    def test_register_user(self):
        """
        This API is used to test user register operations
        :return:
        """

        home_page = HomePage(self.driver)
        login_page = home_page.my_account_fun()
        user_email = self.generate_random_username()
        login_page.reg_email_fun(user_email)
        login_page.reg_pass_fun("Temp@password.123")
        time.sleep(10)
        if self.verify_locater_present(login_page.password_check):
            self.getLogger().info("Password strength check fails")
        login_page.reg_button_fun()
        if self.verify_locater_present(login_page.hello_message):
            self.getLogger().info("Registered sucessfull")
        user_profile = UserProfile(self.driver)
        user_profile.sign_out_user()

    @pytest.mark.usefixtures("login_user")
    def test_login_user(self):
        """
        This API is used to test user Login operation
        :return:
        """

        home_page = HomePage(self.driver)
        login_page = home_page.my_account_fun()
        if self.verify_locater_present(login_page.hello_message):
            self.getLogger().info("sucessfully logged in")
