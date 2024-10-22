from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class FilterWantToBuyOption(BasePage):
    SECONDARY_OPTIONS = (By.CSS_SELECTOR, "a[href='/secondary-listings'].menu-button-block.new.w-inline-block")
    FILTERS_BTN = (By.CSS_SELECTOR, "div[wized='openFiltersWindow'].filter-button")
    WANT_TO_BUY_OPTION = (By.CSS_SELECTOR, "div.switcher-button.active.switcher-button")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "a[wized='applyFilterButtonMLS']")
    WANT_TO_BUY_TAG = (By.XPATH, "//div[@wized='saleTagMLS' and text()='Want to buy']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 20)

    def click_on_secondary_option(self):
        secondary_option = self.wait.until(EC.element_to_be_clickable(self.SECONDARY_OPTIONS))
        secondary_option.click()

    def verify_right_page_opens(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url),
                        message=f'URL does not contain {expected_partial_url}')

    def click_on_filters(self):
        filters_btn = self.wait.until(EC.element_to_be_clickable(self.FILTERS_BTN))
        filters_btn.click()

    def filter_by_want_to_buy(self):
        elements = self.driver.find_elements(*self.WANT_TO_BUY_OPTION)
        print(f"Found {len(elements)} elements for 'Want to Buy' option")
        if len(elements) == 0:
            raise Exception("No 'Want to Buy' option found")

        want_to_buy_option = self.wait.until(
            EC.visibility_of_element_located(self.WANT_TO_BUY_OPTION)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", want_to_buy_option)
        want_to_buy_option.click()

    def click_on_apply_filter(self):
        apply_filter_btn = self.wait.until(EC.element_to_be_clickable(self.APPLY_FILTER_BTN))
        apply_filter_btn.click()

    def verify_all_want_to_buy_tags(self):
        cards = self.wait.until(EC.visibility_of_all_elements_located(self.WANT_TO_BUY_TAG))
        for card in cards:
            card_text = card.text.lower()
            print(f"Card text: {card_text}")
            assert "want to buy" in card_text, "Card does not have 'Want to buy' tag"