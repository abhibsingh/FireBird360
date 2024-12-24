from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AppiumHelper:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find(self, by, locator, timeout=20):
        """Wait for an element to appear and return it."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))

    def click_element(self, by, locator):
        """Click an element."""
        self.wait_and_find(by, locator).click()

    def enter_text(self, by, locator, text):
        """Enter text into an input field."""
        element = self.wait_and_find(by, locator)
        element.clear()
        element.send_keys(text)
