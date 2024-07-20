from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException


class SettingsPage(BasePage):
    SETTINGS_OPTION = (By.XPATH, "//div[text()='Settings']")
    EDIT_PROFILE = (By.XPATH, "//div[text()='Edit profile']")
    FULLNAME = (By.ID, "Fullname")
    PHONE = (By.ID, "number")
    COMPANY = (By.ID, "Company-name")
    CONTACT_EMAIL = (By.ID, "Email-2")
    LANGUAGES = (By.ID, "Languages")
    SAVE_CHANGES = (By.CSS_SELECTOR, "div[wized='saveButtonProfile']")
    CLOSE = (By.CSS_SELECTOR, "a[class='close-button w-button']")

    def __init__(self, driver):
        super().__init__(driver)
        self.inputs = {
            "fullname": ("Getinet Bogale", self.FULLNAME),
            "phone": ("11111111111", self.PHONE),
            "company": ("Test", self.COMPANY),
            "contact_email": ("kievpetr@tinyios.com", self.CONTACT_EMAIL),
            "languages": ("English", self.LANGUAGES)
        }

    def click_setting_option(self):
        setting_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SETTINGS_OPTION)
        )
        setting_option.click()

    def click_edit_profile(self):
        edit_profile = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.EDIT_PROFILE)
        )
        edit_profile.click()

    def enter_input_fields(self):
        for field, (value, locator) in self.inputs.items():
            try:
                input_element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(locator)
                )
                self.driver.execute_script("arguments[0].scrollIntoView();", input_element)

                # Check if the input is interactable
                if not input_element.is_enabled() or input_element.get_attribute("readonly"):
                    print(f"Element {field} is not enabled or is readonly, using JavaScript to set the value")
                    self.driver.execute_script("arguments[0].value = '';", input_element)
                    self.driver.execute_script("arguments[0].value = arguments[1];", input_element, value)
                else:
                    print(f"Clearing and setting value for {field}")
                    input_element.clear()
                    input_element.send_keys(value)

                # Verify that the value was set correctly
                actual_value = input_element.get_attribute("value")
                print(f"After setting, {field} set to {actual_value}")
                if actual_value != value:
                    print(f"JavaScript fallback for {field}")
                    self.driver.execute_script("arguments[0].value = '';", input_element)
                    self.driver.execute_script("arguments[0].value = arguments[1];", input_element, value)
                    actual_value = input_element.get_attribute("value")
                    print(f"After JavaScript fallback, {field} set to {actual_value}")

            except (TimeoutException, WebDriverException) as e:
                print(f"Error while interacting with {field}: {e}")
                input_element = self.driver.find_element(*locator)
                self.driver.execute_script("arguments[0].value = '';", input_element)
                self.driver.execute_script("arguments[0].value = arguments[1];", input_element, value)

    def check_right_information(self):
        for field, (expected_value, locator) in self.inputs.items():
            input_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            actual_value = input_element.get_attribute("value")
            print(f"Checking value for {field}: expected {expected_value}, got {actual_value}")
            assert actual_value == expected_value, f"Expected {field} '{expected_value}', but got '{actual_value}'"

    def check_buttons_available(self):
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SAVE_CHANGES)
        )
        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CLOSE)
        )
        assert save_button.is_displayed(), "Save Changes button is not available"
        assert save_button.is_enabled(), "Save Changes button is not clickable"
        assert close_button.is_displayed(), "Close button is not available"
        assert close_button.is_enabled(), "Close button is not clickable"
