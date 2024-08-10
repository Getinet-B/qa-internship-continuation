from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenContactUsPage(BasePage):
    SETTINGS_LINK = (By.XPATH, "//div[text()='Settings']")
    CONTACT_US_OPTION = (By.CSS_SELECTOR, "a[href*='/contact-us'].page-setting-block.w-inline-block")
    CONTACT_SUPPORT_BTN = (By.CSS_SELECTOR, ".support-fixed-button.w-inline-block")
    INSTAGRAM_ICON = (By.CSS_SELECTOR, "a[href='https://www.instagram.com/reelly.io/']")
    TELEGRAM_ICON = (By.CSS_SELECTOR, "a[href='https://t.me/reellydxb'].contact-button.w-inline-block")
    YOUTUBE_ICON = (By.CSS_SELECTOR, "a[href='https://www.youtube.com/@reelly826']")
    LINKEDIN_ICON = (By.CSS_SELECTOR, "a[href='https://www.linkedin.com/company/reelly-io/']")
    CONNECT_THE_COMPANY = (By.CSS_SELECTOR, "#w-node-_3e5a3d2d-27b1-b6a3-63ba-8fa23fdaf2c2-7f66debb")

    def __init__(self, driver):
        super().__init__(driver)

    def click_settings_option(self):
        setting_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SETTINGS_LINK)
        )
        setting_option.click()

    def click_contact_us_option(self):
        contact_us_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.CONTACT_US_OPTION)
        )
        contact_us_option.click()

    def verify_right_page_opens(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url),
                        message=f'URL does not contain {expected_partial_url}')

    def four_icons_available(self):
        instagram_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.INSTAGRAM_ICON)
        )
        telegram_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TELEGRAM_ICON)
        )
        youtube_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.YOUTUBE_ICON)
        )
        linkedin_icon = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LINKEDIN_ICON)
        )
        assert instagram_button.is_displayed(), "Instagram button is not available"
        assert telegram_button.is_displayed(), "Telegram button is not available"
        assert youtube_button.is_displayed(), "YouTube button is not available"
        assert linkedin_icon.is_displayed(), "Linkedin icon is not available"

    def connect_company_btn_available(self):
        connect_company_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONNECT_THE_COMPANY)
        )
        assert connect_company_button.is_displayed(), "connect_the_company button is not available"
        assert connect_company_button.is_enabled(), "connect_the_company button is not clickable"
