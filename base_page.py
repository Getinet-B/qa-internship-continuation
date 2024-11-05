from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = logging.getLogger(__name__)

    def open(self, url):
        #self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find_element(self, *locator):
        self.logger.info(f'Searching for element by {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        self.logger.info(f'Searching for elements by {locator}')
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.logger.info(f'Clicking on element by {locator}')
        self.find_element(*locator).click()
        by, value = locator  # Unpack the tuple
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def input_text(self, text, *locator):
        self.logger.info(f'Entering text "{text}" into element by {locator}')
        self.find_element(*locator).send_keys(text)

    def type(self, text, *locator):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def wait_until_clickable_click(self, *locator):
        self.logger.info(f'Waiting for element to be clickable by {locator}')
        self.wait.until(
            EC.element_to_be_clickable(*locator),
            f'Element not clickable by {locator}'
        ).click()

    def wait_until_visible(self, *locator):
        self.logger.info(f'Waiting for element to be visible by {locator}')
        self.wait.until(
            EC.visibility_of_element_located(*locator),
            f'Element not visible by {locator}'
        )

    def wait_until_disappear(self, *locator):
        self.logger.info(f'Waiting for element to disappear by {locator}')
        self.wait.until(
            EC.invisibility_of_element_located(*locator),
             f'Element still visible by {locator}'
        )

    def get_current_window(self):
        current_window = self.driver.current_window_handle
        self.logger.info(f'Current window handle: {current_window}')
        self.logger.info(f'All window handles: {self.driver.window_handles}')
        return current_window

    def switch_to_new_window(self):
        self.logger.info('Switching to new window')
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        self.logger.info(f'All windows: {all_windows}')
        self.logger.info(f'Switching to window: {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])

    def switch_new_window_by_id(self, window_id):
        self.logger.info(f'Switching to window by id: {window_id}')
        self.driver.switch_to.window(window_id)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_partial_url):
        self.logger.info(f'Verifying URL contains: {expected_partial_url}')
        self.wait.until(EC.url_contains(expected_partial_url), message=f'URL does not contain {expected_partial_url}')

    def verify_url(self, expected_url):
        self.logger.info(f'Verifying URL matches: {expected_url}')
        self.wait.until(EC.url_matches(expected_url), message=f'URL does not match {expected_url}')

    def save_screenshot(self, name):
        self.logger.info(f'Saving screenshot with name: {name}')
        self.driver.save_screenshot(f'{name}.png')

    def close(self):
        self.logger.info('Closing browser')
        self.driver.close()
