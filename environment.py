from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from allure_behave.utils import scenario_name
from app.application import Application


from support.logger import logger


#def browser_init(context):


#  Run Behave tests with Allure results
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_app_ui_tests.feature

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    :param context:
    :param scenario_name:
    :return:
    """
    driver_path = ChromeDriverManager().install()
    #driver_path = "C:\\Users\\getin\\OneDrive\\Desktop\\qa-internship-continuation\\chromedriver.exe"
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # context.driver.maximize_window()
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='/Users/svetlanalevinsohn/careerist/18-python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    # options.add_argument('disable-gpu')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### WEB MOBILE MODE ###
    # Initialize the browser driver for mobile emulation
    # mobile_emulation = {"deviceName": "Samsung Galaxy S20 Ultra"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # try:
    #     service = Service(ChromeDriverManager().install())
    #     context.driver = webdriver.Chrome(
    #         options=chrome_options,
    #         service=service
    #     )
    #     context.driver.set_window_size(360, 740)
    #     context.driver.implicitly_wait(6)
    #     context.wait = WebDriverWait(context.driver, timeout=15)
    #     context.app = Application(context.driver)
    # except Exception as e:
    #     logger.error(f"Error initializing the browser: {e}")
    #     raise

    ### BROWSERSTACK ###
    # # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'getinetbogale_RTD9et'
    # bs_key = 'if6pZ2sM64Cm7EbPeAgh'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'osVersion': '13.0',
    #     'deviceName': 'Samsung Galaxy S23',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    #
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
