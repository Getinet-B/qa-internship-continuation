from behave import given, when, then
from time import sleep


@given('Open main page')
def open_main(context):
    context.app.home_page.open_main()


@when('Log in to the page')
def log_in_to_the_page(context):
    context.app.login_page.login('kievpetr@tinyios.com', 'Abc1234')
    sleep(6)


@when('Click on settings option')
def click_settings_option(context):
    context.app.open_community_page.click_settings_option()


@when('Click on Community option')
def click_community_option(context):
    context.app.open_community_page.click_community_option()


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.open_community_page.verify_right_page_opens('/community')


@then('Verify "Contact support" button is available and clickable')
def cs_button_available(context):
    context.app.open_community_page.cs_button_available()
