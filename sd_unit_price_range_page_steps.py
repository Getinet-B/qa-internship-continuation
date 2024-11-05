from behave import given, when, then


@when('Click on "Secondary" option at the left side menu')
def click_on_secondary_option(context):
    context.app.sd_unit_price_range_page.click_on_secondary_option()


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.sd_unit_price_range_page.verify_right_page_opens('/secondary-listings')


@then('Click on Filters')
def click_on_filters(context):
    context.app.sd_unit_price_range_page.click_on_filters()


@then('Filter the products by price range from 1200000 to 2000000 AED')
def filter_price_range(context):
    context.app.sd_unit_price_range_page.filter_price_range(1200000, 2000000)


@then('Click on Apply Filter')
def click_on_apply_filter(context):
    context.app.sd_unit_price_range_page.click_on_apply_filter()


@then("Verify the price in all cards is inside the range (1200000 - 2000000)")
def verify_price_in_all_cards(context):
    context.app.sd_unit_price_range_page.verify_price_in_all_cards()

