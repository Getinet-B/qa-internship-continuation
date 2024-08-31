from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenChangePasswordPage(BasePage):
    SETTINGS_OPTION = (By.XPATH, "//div[text()='Settings']")
    CHANGE_PASSWORD_OPTION = (By.CSS_SELECTOR, "a[href='/set-new-password']")
    ENTER_NEW_PASSWORD = (By.ID, "Enter-new-password")
    REPEAT_NEW_PASSWORD = (By.ID, "Repeat-password")
    CHANGE_PASSWORD_BTN = (By.CSS_SELECTOR, "a[wized='changePasswordButton']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_settings_option(self):
        setting_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SETTINGS_OPTION)
        )
        setting_option.click()

    def click_on_change_password_option(self):
        change_password_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.CHANGE_PASSWORD_OPTION)
        )
        change_password_option.click()

    def verify_right_page_opens(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url),
                        message=f'URL does not contain {expected_partial_url}')

    def add_test_password(self, password):
        new_password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ENTER_NEW_PASSWORD)
        )
        #password_input.clear()
        new_password.send_keys(password)

        repeat_password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.REPEAT_NEW_PASSWORD)
        )
        repeat_password.send_keys(password)

    def verify_cp_btn_available(self):
        change_password_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CHANGE_PASSWORD_BTN)
        )
        assert change_password_btn.is_displayed(), "change password button is not available"

