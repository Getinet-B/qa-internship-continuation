from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException


class AddProjectPage(BasePage):
    SETTINGS_BUTTON = (By.XPATH, "//div[text()='Settings']")
    ADD_PROJECT_BUTTON = (By.XPATH, "//div[text()='Add a project']")
    VERIFY_PAGE_OPEN = (By.CSS_SELECTOR, "h1[class='h1-add']")
    YOUR_NAME = (By.ID, 'Your-name')
    COMPANY_NAME = (By.ID, 'Your-company-name')
    ROLE_IN_COMPANY = (By.ID, 'Role')
    AGE_OF_COMPANY = (By.ID, 'Age-of-the-company')
    COUNTRY_FOR_PROJECT = (By.ID, 'Country')
    NAME_OF_PROJECT_HOS = (By.ID, 'Name-project')
    PHONE = (By.ID, 'Phone')
    EMAIL = (By.ID, 'Email-add-project')
    SEND_APPLICATION_BTN = (By.CSS_SELECTOR, "input[value='Send an application']")

    def __init__(self, driver):
        super().__init__(driver)
        self.inputs = {
            "your_name": ("Getinet Bogale", self.YOUR_NAME),
            "company_name": ("Reelly", self.COMPANY_NAME),
            "role_in_company": ("QA Automation Engineer", self.ROLE_IN_COMPANY),
            "age_of_company": ("15", self.AGE_OF_COMPANY),
            "country_for_project": ("ITALY", self.COUNTRY_FOR_PROJECT),
            "name_of_project_hos": ("Automation Development", self.NAME_OF_PROJECT_HOS),
            "phone": ("15555555555", self.PHONE),
            "email": ("kievpetr@tinyios.com", self.EMAIL)
        }

    def click_settings_option(self):
        settings_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SETTINGS_BUTTON)
        )
        settings_button.click()

    def click_add_project(self):
        add_project = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_PROJECT_BUTTON)
        )
        add_project.click()

    def verify_right_page_opens(self):
        right_page = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.VERIFY_PAGE_OPEN)
        )
        right_page.is_displayed()

    def add_test_information(self):
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

    def verify_right_information_present(self):
        for field, (expected_value, locator) in self.inputs.items():
            input_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            actual_value = input_element.get_attribute("value")
            print(f"Checking value for {field}: expected {expected_value}, got {actual_value}")
            assert actual_value == expected_value, f"Expected {field} '{expected_value}', but got '{actual_value}'"

    def verify_button_clickable(self):
        send_app_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEND_APPLICATION_BTN)
        )
        assert send_app_button.is_displayed(), "Send application button is not available"
        assert send_app_button.is_enabled(), "Send application button is not clickable"

