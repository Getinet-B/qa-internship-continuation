from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then


@given('Open registration page')
def open_registration(context):
    context.app.registration_page.open_registration()


@then('Click on "Sign in" link')
def click_on_sign_in(context):
    context.app.registration_page.click_on_sign_in()


@when('Enter Information in the Input fields')
def input_in_fields(context):
    context.app.login_page.login('getinet12183@gmail.com', 'Gb12345678%/?')
    sleep(6)


@then('Verify the right information is present')
def verify_right_information(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[text()='Total projects']").text
    assert "Total projects" in actual_text, f'Error! Text "Total projects" not in {actual_text}'
