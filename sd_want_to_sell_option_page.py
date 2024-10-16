from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FilterSecondaryDeals(BasePage):
    SECONDARY_OPTIONS = (By.CSS_SELECTOR, "a[href='/secondary-listings'].menu-button-block.new.w-inline-block")
    FILTERS_BTN = (By.CSS_SELECTOR, "div[wized='openFiltersWindow'].filter-button")
    WANT_TO_SELL_OPTION = (By.CSS_SELECTOR, "div[wized='ListingTypeSell']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "a[wized='applyFilterButtonMLS']")
    FOR_SALE_TAG = (By.CSS_SELECTOR, "div[wized='saleTagMLS']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def click_on_secondary_option(self):
        secondary_option = self.wait.until(
            EC.element_to_be_clickable(self.SECONDARY_OPTIONS)
        )
        secondary_option.click()

    def verify_right_page_opens(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'URL does not contain {expected_partial_url}'
        )

    def click_on_filters(self):
        click_filters_btn = self.wait.until(
            EC.element_to_be_clickable(self.FILTERS_BTN)
        )
        click_filters_btn.click()

    def filter_by_want_to_sell(self):
        want_to_sell_btn = self.wait.until(
            EC.element_to_be_clickable(self.WANT_TO_SELL_OPTION)
        )
        want_to_sell_btn.click()

    def click_on_apply_filter(self):
        apply_filter_btn = self.wait.until(
            EC.element_to_be_clickable(self.APPLY_FILTER_BTN)
        )
        apply_filter_btn.click()

    def verify_all_cards_with_sale_tag(self):
        cards = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.FOR_SALE_TAG)
        )
        for card in cards:
            card_text = card.text.lower()
            print(f"Card text: {card_text}")
            assert "for sale" in card_text, "Card does not have 'for sale' tag"