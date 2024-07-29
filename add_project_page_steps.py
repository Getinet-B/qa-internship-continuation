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
    context.app.add_project_page.click_settings_option()


@when('Click on Add a project')
def click_add_project(context):
    context.app.add_project_page.click_add_project()


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.add_project_page.verify_right_page_opens()


@then('Add some test information to the input fields')
def add_test_information(context):
    context.app.add_project_page.add_test_information()


@then('Verify the right information is present in the input fields')
def verify_right_information_present(context):
    context.app.add_project_page.verify_right_information_present()


@then('Verify “Send an application” button is available and clickable')
def verify_button_clickable(context):
    context.app.add_project_page.verify_button_clickable()
