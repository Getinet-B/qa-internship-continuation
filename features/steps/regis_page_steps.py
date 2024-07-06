from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open the registration page')
def open_registration_page(context):
    context.app.regis_page.open_registration_page()


@when('Enter information in the input fields')
def registration_input(context):
    context.app.regis_page.registration_input()
    sleep(6)


@then('Verify the right information is present')
def verify_input(context):
    context.app.regis_page.verify_input()
