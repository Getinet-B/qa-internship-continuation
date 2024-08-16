from behave import given, when, then
from time import sleep


@when('Click on settings option')
def click_settings_option(context):
    context.app.user_guide_page.click_settings_option()


@when('Click on User Guide option')
def click_user_guide_option(context):
    context.app.user_guide_page.click_user_guide_option()


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.user_guide_page.verify_right_page_opens('/user-guide')


@then('Verify all lesson videos contain titles')
def all_contain_titles(context):
    context.app.user_guide_page.all_contain_titles()
