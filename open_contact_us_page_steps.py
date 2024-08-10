from behave import given, when, then
from time import sleep


@given('Open the main page https://soft.reelly.io')
def open_main(context):
    context.app.home_page.open_main()


@when('Log in to the page')
def log_in_to_the_page(context):
    context.app.login_page.login('kievpetr@tinyios.com', 'Abc1234')
    sleep(6)


@when('Click on settings option')
def click_settings_option(context):
    context.app.open_contact_us_page.click_settings_option()


@when('Click on Contact us option')
def click_contact_us_option(context):
    context.app.open_contact_us_page.click_contact_us_option()


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.open_contact_us_page.verify_right_page_opens('/contact-us')


@then('Verify there are at least 4 social media icons')
def four_icons_available(context):
    context.app.open_contact_us_page.four_icons_available()


@then('Verify “Connect the company” button is available and clickable')
def connect_company_btn_available(context):
    context.app.open_contact_us_page.connect_company_btn_available()
