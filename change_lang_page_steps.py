from behave import given, when, then
from time import sleep


@given('Open main page')
def open_main(context):
    context.app.home_page.open_main()


@when('Log in to the page')
def log_in_to_the_page(context):
    context.app.login_page.login('kievpetr@tinyios.com', 'Abc1234')
    sleep(6)



@when('Click on Main Menu')
def click_on_main_menu(context):
    context.app.change_language_page.click_on_main_menu()
    sleep(2)


@when('Change the language to Russian "RU"')
def change_language_to_russian(context):
    context.app.change_language_page.change_language_to_russian()


@then('Verify the language has changed')
def verify_language_changed(context):
    context.app.change_language_page.verify_language_changed()



