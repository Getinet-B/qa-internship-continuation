from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class OpenCommunityPage(BasePage):
    SETTINGS_LINK = (By.XPATH, "//div[text()='Settings']")
    COMMUNITY_LINK = (By.CSS_SELECTOR, "a[href*='/community'].page-setting-block.w-inline-block")
    CONTACT_SUPPORT_BTN = (By.CSS_SELECTOR, ".support-fixed-button.w-inline-block")

    def __init__(self, driver):
        super().__init__(driver)

    def click_settings_option(self):
        logger.info("Attempting to click on Settings option")
        setting_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SETTINGS_LINK)
        )
        setting_option.click()
        logger.info("Clicked on Settings option")

    def click_community_option(self):
        logger.info("Attempting to click on community option")
        community_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.COMMUNITY_LINK)
        )
        community_option.click()
        logger.info("Clicked on community option")

    def verify_right_page_opens(self, expected_partial_url):
        self.logger.info(f'Verifying URL contains: {expected_partial_url}')
        self.wait.until(EC.url_contains(expected_partial_url),
                        message=f'URL does not contain {expected_partial_url}')

    def cs_button_available(self):
        logger.info("Checking if 'Contact support' button is available and clickable")
        contact_support_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTACT_SUPPORT_BTN)
        )
        assert contact_support_button.is_displayed(), "contact_support button is not available"
        assert contact_support_button.is_enabled(), "contact_support button is not clickable"
        logger.info("Clicked on 'Contact support' button")

