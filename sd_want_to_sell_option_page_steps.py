from behave import given, when, then


@when('Click on "Secondary" option at the left side menu')
def click_on_secondary_option(context):
    context.app.sd_want_to_sell_option_page.click_on_secondary_option()


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.sd_want_to_sell_option_page.verify_right_page_opens('/secondary-listings')


@then('Click on Filters')
def click_on_filters(context):
    context.app.sd_want_to_sell_option_page.click_on_filters()


@then('Filter the products by "want to sell"')
def filter_by_want_to_sell(context):
    context.app.sd_want_to_sell_option_page.filter_by_want_to_sell()


@then('Click on Apply Filter')
def click_on_apply_filter(context):
    context.app.sd_want_to_sell_option_page.click_on_apply_filter()


@then('Verify all cards have "for sale" tag')
def verify_all_cards_with_sale_tag(context):
    context.app.sd_want_to_sell_option_page.verify_all_cards_with_sale_tag()
