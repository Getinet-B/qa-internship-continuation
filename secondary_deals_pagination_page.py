from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecondaryDealsPaginationPage(BasePage):
    SECONDARY_OPTIONS = (By.CSS_SELECTOR, "a[href='/secondary-listings'].menu-button-block.new.w-inline-block")
    CONNECT_BTN = (By.CSS_SELECTOR, ".settings-block-menu .get-free-period.menu")
    FORWARD_BTN = (By.CSS_SELECTOR, "a.pagination__button")  # Assuming this is the "next" button
    BACK_BTN = (By.CSS_SELECTOR, "div[wized='previousPageMLS']")  # Assuming this is the "previous" button

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def click_on_secondary_option(self):
        secondary_option = self.wait.until(
            EC.element_to_be_clickable(self.SECONDARY_OPTIONS)
        )
        secondary_option.click()

    def open_the_right_page(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'URL does not contain {expected_partial_url}'
        )

    def click_pagination_button(self, button_locator, message_on_completion):
        """Reusable method to click a pagination button and handle navigation."""
        while True:
            try:
                button = self.wait.until(EC.element_to_be_clickable(button_locator))
                actions = ActionChains(self.driver)
                actions.move_to_element(button)
                actions.perform()
                button.click()
                # Wait for the button to become stale to ensure the page is loading
                self.wait.until(EC.staleness_of(button))
            except Exception:
                print(message_on_completion)
                break

    def go_to_the_final_page(self):
        self.click_pagination_button(self.FORWARD_BTN,
                                     "Reached the last page, 'Next' button is no longer clickable")

    def go_back_to_first_page(self):
        self.click_pagination_button(self.BACK_BTN,
                                     "Reached the first page, 'Back' button is no longer clickable")