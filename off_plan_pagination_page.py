from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OffPlanPage(BasePage):
    OFF_PLAN_OPTION = (By.CSS_SELECTOR, "a[aria-current='page']._1-link-menu.w-inline-block")
    PAGINATION_NEXT = (By.CSS_SELECTOR, "a[wized='nextPageProperties']")
    PAGINATION_PREVIOUS = (By.CSS_SELECTOR, "div[wized='previousPageProperties'].pagination__button")
    CURRENT_PAGE = (By.CSS_SELECTOR, "span.current-page")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def click_on_off_plan_option(self):
        self.wait.until(EC.element_to_be_clickable(self.OFF_PLAN_OPTION)).click()

    def verify_off_plan_page_opens(self, expected_partial_url):
        assert expected_partial_url in self.driver.current_url, f"Expected URL to contain {expected_partial_url}"

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
                (print(message_on_completion))
                break

    def go_to_final_page(self):
        self.click_pagination_button(self.PAGINATION_NEXT,
                                     "Reached the last page, 'Next' button is no longer clickable")

    def go_back_to_first_page(self):
        self.click_pagination_button(self.PAGINATION_PREVIOUS,
                                     "Reached the first page, 'Back' button is no longer clickable")


