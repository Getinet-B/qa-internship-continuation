from behave import given, when, then
from time import sleep


@when('Click on Change password option')
def click_on_change_password_option(context):
    context.app.change_password_page.click_on_change_password_option()


@then('Verify the page(s) opens')
def verify_right_page_opens(context):
    context.app.change_password_page.verify_right_page_opens('/set-new-password')


@then('Add some test "{password}" to the input fields')
def add_test_password(context, password):
    context.app.change_password_page.add_test_password(password)


@then('Verify the "Change password" button is available (but don\'t click on it)')
def verify_cp_btn_available(context):
    context.app.change_password_page.verify_cp_btn_available()
