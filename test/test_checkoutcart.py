import time
import pytest
from selenium.webdriver.common.by import By

from PageObject.CheckOutPage import CheckOutPage
from PageObject.UserProfile import UserProfile
from utilities.SetupClass import SetupClass


class TestCart(SetupClass):

    @pytest.mark.usefixtures("login_user")
    def test_save_items_to_cart(self):
        """
        This API is used to test the saving items into cart operation
        :return:
        """
        log = self.getLogger()
        product_list = []
        user_profile = UserProfile(self.driver)
        user_profile.shop_button_fun()
        item_list = self.get_the_list_of_items("//div[@id='content']//li")
        for item in item_list:
            product_list.append(item.find_element(By.XPATH, "a/h3").text)
            try:
                item.find_element(By.XPATH, "a[contains(text(),'Add to basket')]").click()
            except Exception as e:
                log.error(e)

        time.sleep(5)
        user_profile.check_cart_box()
        product_in_cart = self.get_the_list_of_items("//table/tbody/tr/td[@class='product-name']")
        for i in product_in_cart:
            if i.text not in product_list:
                log.warning(f"Product {i.text} not showing in the cart")
            else:
                log.info("Items sucessfully added")

    @pytest.mark.usefixtures("login_user")
    def test_delete_items_to_cart(self):
        """
        This API is used to test the deletion operation from the cart
        :return:
        """
        log = self.getLogger()
        user_profile = UserProfile(self.driver)
        checkout_page = CheckOutPage(self.driver)
        user_profile.check_cart_box()
        existing_product = self.get_the_list_of_items("//table/tbody/tr/td[@class='product-name']")
        if existing_product:
            delete_buttons = self.get_the_list_of_items("//tbody/tr/td/a[@class='remove']")
            log.info(delete_buttons)
            for i in range(len(delete_buttons)):
                checkout_page.delete_product_from_cart()
                time.sleep(2)
        product_after_deleting = self.get_the_list_of_items("//table/tbody/tr/td[@class='product-name']")
        if not product_after_deleting:
            log.info("Verified")
