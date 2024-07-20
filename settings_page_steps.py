from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('Open main page')
def open_main(context):
    context.app.home_page.open_main()


@when('Log in to the page')
def log_in_to_the_page(context):
    context.app.login_page.login('kievpetr@tinyios.com', 'Abc1234')
    sleep(6)


@when('Click on settings option')
def click_setting_option(context):
    context.app.settings_page.click_setting_option()
    sleep(6)


@when('Click on Edit profile option')
def click_edit_profile(context):
    context.app.settings_page.click_edit_profile()


@when('Enter some test information in the input fields')
def enter_input_fields(context):
    context.app.settings_page.enter_input_fields()


@then('Check the right information is present in the input fields')
def check_right_information(context):
    context.app.settings_page.check_right_information()


@then('Check “Close” and “Save Changes” buttons are available and clickable')
def check_buttons_available(context):
    context.app.settings_page.check_buttons_available()
