import time
import os
import pytest
import logging
import random
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_random_email():
    """Generate a random email address for testing."""
    random_number = random.randint(1000, 9999)
    return f"test+{random_number}@gmail.com"

@pytest.fixture(scope="session") 
def driver():
    
    """
    Sets up the Appium driver.
    """

    # Configuration for Appium
    desired_capabilities = {
    "platformName": "Android",
    "deviceName": "test_avd",  # Matches the AVD created in the Dockerfile
    "automationName": "UiAutomator2",
    "appPackage": "com.firebird.artist360.uat",
    "appActivity": "com.firebird.artist360.MainActivity",
    "noReset": True,

   
    "unicodeKeyboard": True,
}

   

   

    # Initialize the Appium driver
    logger.info("Starting Appium session...")
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    return driver

def test_account_creation(driver):
    """
    Test case 1: Automate the account creation flow.
    """
    try:
        # Wait for the app to load
        time.sleep(5)

        # Step 1: Click on "Create Account" button
        logger.info("Locating 'Create Account' button...")

        create_account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Create Account"]'))
        )
        create_account_button.click()
        logger.info("Navigated to 'Create Account'.")

        # Step 2: Enter first name
        logger.info("Locating first name input field...")
        first_name_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]"))
        )
        first_name_field.click()
        first_name_field.send_keys("John")
        logger.info("First name entered.")

        # Step 3: Enter surname
        logger.info("Locating surname input field...")
        surname_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]"))
        )
        surname_field.click()
        surname_field.send_keys("Doe")
        logger.info("Surname entered.")

        # Step 4: Enter date of birth
        logger.info("Locating date of birth input field...")
        dob_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]"))
        )
        dob_field.click()
        dob_field.send_keys("12/12/1999")
        logger.info("Date of birth entered.")

        # Step 5: Generate and enter a unique email
        random_email = generate_random_email()
        logger.info(f"Generated email: {random_email}")
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[4]"))
        )
        email_field.click()
        email_field.send_keys(random_email)
        logger.info("Email entered.")

        # Step 6: Enter password
        logger.info("Locating password input field...")
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[5]"))
        )
        password_field.click()
        password_field.send_keys("@1b2c3D4e5")
        logger.info("Password entered.")

        # Step 7: Click "Create My Account" button
        logger.info("Clicking 'Create My Account' button...")
        create_my_account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Create my account"]'))
        )
        create_my_account_button.click()
        logger.info("Account creation submitted.")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

def test_navigate_to_manager(driver):
    """
    Test case 2: Navigate to the Manager section.
    """
    try: 
        # Step 8: Click on "Manager" icon
        logger.info("Clicking on the 'Manager' icon...")
        manager_icon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ImageView[2]"))
        )
        manager_icon.click()

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise


def test_continue_manager_flow(driver):
    """
    Test case 3: Continue through the initial Manager flow.
    """
    try:
        # Step 9: Click "Continue" button
        logger.info("Clicking on 'Continue' button...")
        continue_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Continue']"))
        )
        continue_button.click()

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

def test_search_artist(driver):
    """
    Test case 4: Search for an artist in the Manager section.
    """
    try:
        # Step 10: Search for "Taylor"
        logger.info("Searching for artist 'Taylor'...")
        search_artist_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Search for artist name']"))
        )
        search_artist_button.click()

        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText"))
        )
        search_field.click()
        search_field.send_keys("Taylor")
        logger.info("Artist name 'Taylor' entered.")

        first_result = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[contains(@content-desc, 'Taylor')]"))
        )
        first_result.click()
        logger.info("Selected the first search result.")

        continue_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Continue']"))
        )
        continue_button.click()

        # Step 11: Click "Go to the app" button
        go_to_app_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Go to the app']"))
        )
        go_to_app_button.click()
        logger.info("Navigated to the app.")
        logger.info("Clicking on 'Skip the tutorial' button...")

        go_to_app_tour = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Explore My 360"]'))
        )
        go_to_app_tour.click()
        logger.info("Touring  the app.")
        logger.info("Clicking on 'tour the app' button...")

        go_to_app_next = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Next"]'))
        )
        go_to_app_next.click()
        logger.info("next button.")
        logger.info("Clicking on 'next button of  the app'...")
        go_to_app_next = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Next"]'))
        )
        go_to_app_next.click()
        logger.info("next button.")
        logger.info("Clicking on 'next button of  the app'...")
        go_to_app_done = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Done"]'))
        )
        go_to_app_done.click()
        logger.info("done button.")
        logger.info("Clicking on 'done button of  the app'...") 

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

def test_verify_app_content(driver):
    """
    Test case 5: Verify app content after navigating from Manager.
    """
    try:
        time.sleep(10)

        #Step 9: Scroll up and down
        logger.info("Scrolling up and down to verify Spotify element...")
        touch_action = TouchAction(driver)
        touch_action.press(x=500, y=1000).move_to(x=500, y=200).release().perform()  # Scroll down
        time.sleep(1)
        touch_action.press(x=500, y=200).move_to(x=500, y=1000).release().perform()  # Scroll up

        # Step 10: Check for Spotify element
        logger.info("Verifying presence of Spotify element...")
        element = driver.find_element(By.XPATH, "//android.widget.ImageView[@content-desc='7 days']")
        assert element.is_displayed(), "Element containing 'Followers' not found!"
        if element:
            logger.info("Spotify element found!")
        else:
            logger.error("Spotify element NOT found!")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise
def test_add_artist_and_validate_highlights(driver):
    try:
        # Step 0: Relaunch the app
        logger.info("Relaunching the app for this test case.")
        driver.close_app()  # Close the app
        driver.launch_app()  # Relaunch the app
        time.sleep(20)  # Wait for 20 seconds before starting execution

        # Step 1: Click on the dropdown menu for artist selection
        logger.info("Attempting to locate the dropdown menu.")
        dropdown_menu = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[starts-with(@content-desc, 'Taylor Taylor')]/android.widget.ImageView[1]"))
        )
        dropdown_menu.click()
        logger.info("Dropdown menu clicked.")

        # Step 2: Click on the '+ Add profile' button
        add_profile_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='+ Add profile']"))
        )
        add_profile_button.click()
        logger.info("+ Add profile button clicked.")

        # Step 3: Click on the 'Search for artist name' button
        search_artist_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Search for artist name']"))
        )
        search_artist_button.click()
        logger.info("Search for artist name button clicked.")

        # Step 4: Enter the artist name "Shreya Ghoshal"
        search_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText"))
        )
        search_field.click()
        search_field.send_keys("Shreya Ghoshal")
        logger.info("Entered artist name 'Shreya Ghoshal'.")

        # Step 5: Select the artist from the dropdown
        artist_result = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/(//android.view.View[contains(@content-desc, 'shreya-ghoshal')])[1]"))
        )
        artist_result.click()
        logger.info("Selected artist 'Shreya Ghoshal'.")

        # Step 6: Click on the 'Continue' button
        continue_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Continue']"))
        )
        continue_button.click()
        logger.info("Clicked 'Continue' button.")

        # Step 7: Validate presence of highlight cards after scrolling
        touch_action = TouchAction(driver)
        touch_action.press(x=500, y=1000).move_to(x=500, y=200).release().perform()  # Scroll down
        time.sleep(1)
        touch_action.press(x=500, y=200).move_to(x=500, y=1000).release().perform()  # Scroll up # Scroll down
        time.sleep(1)
        logger.info("Scrolled down to check highlight cards.")

       
    except Exception as e:
        logger.error(f"An error occurred during the test: {e}")
        raise

def test_switch_artist(driver):
    """
    Test case: Switch from one artist to another in the dropdown menu.
    """
    try:
        # Step 1: Click on the dropdown menu for the artist "Shreya Ghoshal"
        logger.info("Clicking on 'Shreya Ghoshal' artist dropdown menu...")
        shreya_ghoshal_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[starts-with(@content-desc, 'Shreya Ghoshal')]/android.widget.ImageView[1]"))
            
            
        )
        shreya_ghoshal_dropdown.click()
        logger.info("Clicked on 'Shreya Ghoshal' dropdown menu.")

        # Step 2: Select "Taylor Taylor Artist Team" from the dropdown
        

    except Exception as e:
        logger.error(f"An error occurred during the artist switch test: {str(e)}")
        raise




def teardown_driver(driver):
    """
    Tears down the Appium driver.
    """
    logger.info("Ending Appium session...")
    driver.quit()

if __name__ == "__main__":
    driver = driver()
    try:
        test_account_creation(driver)
        test_navigate_to_manager(driver)
        test_continue_manager_flow(driver)
        test_search_artist(driver)
        test_verify_app_content(driver)
        test_add_artist_and_validate_highlights(driver)
        test_switch_artist(driver) 
    finally:
        teardown_driver(driver)