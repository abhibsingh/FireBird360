from helpers import AppiumHelper
from locators import LOCATORS
from selenium.webdriver.common.by import By

class AccountCreation:
    def __init__(self, driver):
        self.helper = AppiumHelper(driver)

    def create_account(self, first_name, surname, dob, email, password):
        """Perform account creation."""
        self.helper.click_element(By.XPATH, LOCATORS["create_account_button"])
        self.helper.enter_text(By.XPATH, LOCATORS["first_name"], first_name)
        self.helper.enter_text(By.XPATH, LOCATORS["surname"], surname)
        self.helper.enter_text(By.XPATH, LOCATORS["dob"], dob)
        self.helper.enter_text(By.XPATH, LOCATORS["email"], email)
        self.helper.enter_text(By.XPATH, LOCATORS["password"], password)
        self.helper.click_element(By.XPATH, LOCATORS["create_my_account_button"])
