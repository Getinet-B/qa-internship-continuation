from behave import given, when, then


@when('Click on support option')
def click_support_option(context):
    context.app.whatsapp_and_telegram_communities_page.click_support_option()


@when('Switch to the new tab')
def switch_to_new_window(context):
    context.app.whatsapp_and_telegram_communities_page.switch_to_new_window()


@then('Verify the right page opens. (The link contains “api.whatsapp.com”). Don’t click on “Continue to Chat”')
def verify_right_page_opens(context):
    context.app.whatsapp_and_telegram_communities_page.verify_right_page_opens('api.whatsapp.com')


@then('Go back')
def go_back(context):
    context.app.whatsapp_and_telegram_communities_page.go_back()


@then('Click on news option. (The link contains “t.me”). Don’t click on “view in telegram”')
def click_news_option(context):
    context.app.whatsapp_and_telegram_communities_page.click_news_option()


@then('Verify the right page opens')
def verify_right_page(context):
    context.app.whatsapp_and_telegram_communities_page.verify_right_page('t.me')
