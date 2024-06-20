import time
import pytest
from selenium import webdriver

from PageObject.HomePage import HomePage
from PageObject.UserProfile import UserProfile


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    else:
        driver = webdriver.Firefox()
    driver.get("https://practice.automationtesting.in/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture()
def login_user():
    home_page = HomePage(driver)
    login_page = home_page.my_account_fun()
    login_page.login_email_fun("test123@centime.com")
    login_page.login_pass_fun("Temp@password.123")
    time.sleep(3)
    login_page.login_button_fun()
    yield
    home_page.my_account_fun()
    user_profile = UserProfile(driver)
    user_profile.sign_out_user()
