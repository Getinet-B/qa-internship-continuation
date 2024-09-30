from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RightNumberUiElementsPage(BasePage):
    NUMBER_OF_OPTIONS = (By.CSS_SELECTOR, "a.page-setting-block.w-inline-block")
    CONNECT_BTN = (By.CSS_SELECTOR, ".settings-block-menu .get-free-period.menu")

    def __init__(self, driver):
        super().__init__(driver)

    def open_the_right_page(self, expected_partial_url):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(expected_partial_url),
            message= f'URL does not contain {expected_partial_url}'
        )

    def verify_the_number_of_options(self, expected_number):
        setting_options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.NUMBER_OF_OPTIONS)
        )
        assert len(
            setting_options) == expected_number, f"Expected {expected_number} settings options, found {len(setting_options)}"

    def verify_company_button_available(self):
        connect_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CONNECT_BTN)
        )
        assert connect_button.is_displayed(), "Connect the company button is not available"
