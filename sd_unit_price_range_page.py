from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import BasePage


class UnitPriceRange(BasePage):
    SECONDARY_OPTIONS = (By.CSS_SELECTOR, "a[href='/secondary-listings'].menu-button-block.new.w-inline-block")
    FILTERS_BTN = (By.CSS_SELECTOR, "div[wized='openFiltersWindow'].filter-button")
    UNIT_PRICE_FROM = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    UNIT_PRICE_TO = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "a[wized='applyFilterButtonMLS'].button-filter.w-button")
    VERIFY_PRICE_RANGE = (By.CSS_SELECTOR, "div[wized='unitPriceMLS'].number-price-text")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 30)

    def click_on_secondary_option(self):
        secondary_option = self.wait.until(EC.element_to_be_clickable(self.SECONDARY_OPTIONS))
        secondary_option.click()

    def verify_right_page_opens(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url), message=f'URL does not contain {expected_partial_url}')

    def click_on_filters(self):
        filters_button = self.wait.until(EC.element_to_be_clickable(self.FILTERS_BTN))
        filters_button.click()

    def filter_price_range(self, min_price, max_price):
        # Ensure the inputs are visible and fill them
        self.wait.until(EC.element_to_be_clickable(self.UNIT_PRICE_FROM)).send_keys(str(min_price))
        self.wait.until(EC.element_to_be_clickable(self.UNIT_PRICE_TO)).send_keys(str(max_price))

    def click_on_apply_filter(self):
        apply_filter_button = self.wait.until(EC.element_to_be_clickable(self.APPLY_FILTER_BTN))
        apply_filter_button.click()

    def verify_price_in_all_cards(self):
        prices = self.driver.find_elements(*self.VERIFY_PRICE_RANGE)
        for price_element in prices:
            price_text = price_element.text.replace("AED ", "").replace(",", "").strip()

            # Skip if price_text is empty or not a valid integer
            if not price_text.isdigit():
                print(f"Skipping invalid or empty price: '{price_text}'")
                continue

            price = int(price_text)
            assert 1200000 <= price <= 2000000, f'Price {price} is out of range.'