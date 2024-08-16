from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenUserGuidePage(BasePage):
    SETTINGS_LINK = (By.XPATH, "//div[text()='Settings']")
    USER_GUIDE_OPTION = (By.CSS_SELECTOR, "a[href='/user-guide'].page-setting-block.w-inline-block")
    LESSON_TITLES = (By.CSS_SELECTOR, "a[data-sessionlink='feature=player-title']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_settings_option(self):
        setting_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SETTINGS_LINK)
        )
        setting_option.click()

    def click_user_guide_option(self):
        contact_us_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.USER_GUIDE_OPTION)
        )
        contact_us_option.click()

    def verify_right_page_opens(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url),
                        message=f'URL does not contain {expected_partial_url}')

    def all_contain_titles(self):
        lesson_titles = self.driver.find_elements(*self.LESSON_TITLES)

        for title in lesson_titles:
            lesson_titles = title.text
            assert lesson_titles != "", f'A lesson video does not have a title {lesson_titles}'
