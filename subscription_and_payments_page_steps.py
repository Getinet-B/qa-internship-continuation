from behave import given, when, then
from time import sleep


@when('Click on Subscription & payments option')
def click_subscription_payments_option(context):
    context.app.subscription_and_payments_page.click_subscription_payments_option()


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.subscription_and_payments_page.verify_right_page_opens('/subscription')


@then('Verify title “Subscription & payments” is visible')
def verify_title_subscription_payments_visible(context):
    context.app.subscription_and_payments_page.verify_title_subscription_payments_visible()


@then('Verify “back” and “upgrade plan” buttons are available')
def verify_back_and_upgrade_plan_btn_available(context):
    context.app.subscription_and_payments_page.verify_back_and_upgrade_plan_btn_available()
