import inspect
import logging
import random
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class SetupClass:


    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger
    def verify_locater_present(self, locater: str):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, locater)))

    def get_the_list_of_items(self, locater: str):
        return self.driver.find_elements(By.XPATH, locater)

    def generate_random_username(self):
        random_val = random.choices("12345667", k=8)
        return "user_" + "".join(random_val) + "@centime.com"

