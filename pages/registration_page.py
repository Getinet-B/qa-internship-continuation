from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://soft.reelly.io/sign-up'

    def open_registration(self):
        print("registration open method called")
        super().open(self.url)

    def click_on_sign_in(self):
        sign_in_button = self.driver.find_element(By.XPATH, "//div[text()='Sign in']")  # Adjust the locator as needed
        sign_in_button.click()
