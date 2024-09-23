from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccessWhatsappTelegramCommunitiesPage(BasePage):
    SUPPORT_OPTION = (By.CSS_SELECTOR, "a[href*='https://api.whatsapp.com']")
    NEWS_OPTION = (By.CSS_SELECTOR, "a[href='https://t.me/reellydxb'].page-setting-block")

    def __init__(self, driver):
        super().__init__(driver)

    def click_support_option(self):
        support_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUPPORT_OPTION)
        )
        support_option.click()

    def switch_to_new_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])  # Switch to new tab

    def verify_right_page_opens(self, expected_partial_url):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(expected_partial_url),
            message=f'URL does not contain {expected_partial_url}'
        )

    def go_back(self):
        self.driver.close()  # Close current tab
        original_window = self.driver.window_handles[0]
        self.driver.switch_to.window(original_window)

    def click_news_option(self):
        news_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEWS_OPTION)
        )
        news_option.click()

    def verify_right_page(self, expected_partial_url):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(expected_partial_url),
            message=f'URL does not contain {expected_partial_url}'
        )