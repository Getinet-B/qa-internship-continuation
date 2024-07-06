from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RegisPage(BasePage):
    FULLNAME = (By.CSS_SELECTOR, "input[id='Full-Name']")
    PHONE = (By.CSS_SELECTOR, "input[id='phone2']")
    EMAIL = (By.CSS_SELECTOR, "input[id='Email-3']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='field']")
    COMPANY = (By.ID, "Company-website")
    ROLE = (By.ID, "Role")
    POSITION = (By.ID, "Position")
    COUNTRY = (By.ID, "country-select")
    COMPANY_SIZE = (By.ID, "Agents-amount-2")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "a[wized='createaccountButtonSignup']")

    def open_registration_page(self):
        self.open('https://soft.reelly.io/sign-up')
        # calls base page method directly, passes url

    def __init__(self, driver):
        super().__init__(driver)

        # Define test data and locators
        self.inputs = {
            "fullname": ("Getinet Bogale", self.FULLNAME),
            "phone": ("571-111-1111", self.PHONE),
            "email": ("getinet@gmail.com", self.EMAIL),
            "password": ("abc1234", self.PASSWORD),
            "company": ("test", self.COMPANY),
            "role": ("Developer", self.ROLE),
            "position": ("Seller", self.POSITION),
            "country": ("United States of America", self.COUNTRY),
            "company-size": ("I work alone", self.COMPANY_SIZE),
        }

    def registration_input(self):
        wait = WebDriverWait(self.driver, 10)
        for field, (value, locator) in self.inputs.items():
            try:
                input_element = wait.until(EC.element_to_be_clickable(locator))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", input_element)

                # Ensure the element is interactable
                input_element = wait.until(EC.element_to_be_clickable(locator))

                # Clear the input using JavaScript
                self.driver.execute_script("arguments[0].value = '';", input_element)

                input_element.send_keys(value)
            except Exception as e:
                print(f"Error interacting with field {field}: {e}")
                raise

        # After setting the input, verify the fields
        self.verify_input()

    def verify_input(self):
        wait = WebDriverWait(self.driver, 10)
        for field, (expected_value, locator) in self.inputs.items():
            if field == "password":
                # Skip verification for the password field due to typical restrictions
                continue

            input_element = wait.until(EC.presence_of_element_located(locator))
            actual_value = input_element.get_attribute("value")

            assert actual_value == expected_value, f"Expected {field} '{expected_value}', but got '{actual_value}'"

    def create_account_button(self):
        wait = WebDriverWait(self.driver, 10)
        create_account_btn = wait.until(EC.element_to_be_clickable(self.CREATE_ACCOUNT))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", create_account_btn)
        create_account_btn.click()
