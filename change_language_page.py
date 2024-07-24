from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ChangeLanguagePage(BasePage):
    MAIN_MENU = (By.XPATH, "//div[text()='Main menu']")
    LANGUAGE = (By.CSS_SELECTOR, "[id='w-dropdown-toggle-0']")
    CHANGE_TO_RUSSIAN = (By.XPATH, "//a[@tabindex ='0' and text()='RU']")
    MENU_TITLE = (By.XPATH, "//h1[@class='h1-menu' and text()='Главное меню']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_main_menu(self):
        main_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MAIN_MENU)
        )
        main_menu.click()

    def change_language_to_russian(self):
        self.click(*self.LANGUAGE)
        self.wait_until_clickable_click(self.LANGUAGE)
        self.click(*self.CHANGE_TO_RUSSIAN)

    def verify_language_changed(self, expected_title="Главное меню"):
        try:
            print("Searching for elements matching the expected title...")
            header_elements = self.driver.find_elements(*self.MENU_TITLE)

            actual_titles = [element.text for element in header_elements]
            print(f"Actual titles found: {actual_titles}")

            if expected_title in actual_titles:
                print(f"Verification successful: Expected title '{expected_title}' is present.")
            else:
                raise AssertionError(f"Expected title '{expected_title}', but got '{actual_titles}'")

        except AssertionError as e:
            print(f"Title verification failed: {str(e)}")
        except Exception as e:
            print(f"There is an error found while verifying the title: {str(e)}")
            