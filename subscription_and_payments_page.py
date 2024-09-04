from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenSubscriptionPaymentPage(BasePage):
    SETTINGS_OPTION = (By.XPATH, "//div[text()='Settings']")
    SUBSCRIPTION_PAYMENTS_OPTION = (By.CSS_SELECTOR, "a[href='/subscription']")
    TITLE = (By.XPATH, "//div[text()='Subscription & payments']")
    UPGRADE_PLAN_BTN = (By.CSS_SELECTOR, "a[href='/prosub']")
    BACK_BTN = (By.CSS_SELECTOR, "a[class*='button-verify margin']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_settings_option(self):
        setting_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SETTINGS_OPTION)
        )
        setting_option.click()

    def click_subscription_payments_option(self):
        subscription_payments_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SUBSCRIPTION_PAYMENTS_OPTION)
        )
        subscription_payments_option.click()

    def verify_right_page_opens(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url),
                        message=f'URL does not contain {expected_partial_url}')

    def verify_title_subscription_payments_visible(self):
        actual_title = self.driver.find_elements(*self.TITLE)

        for title in actual_title:
            actual_title = title.text
            assert actual_title != "", f'This page does not have a title {actual_title}'

    def verify_back_and_upgrade_plan_btn_available(self):
        upgrade_plan_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.UPGRADE_PLAN_BTN)
        )
        assert upgrade_plan_btn.is_displayed(), "upgrade plan button is not available"

        back_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.BACK_BTN)
        )
        assert back_btn.is_displayed(), "back button is not available"
