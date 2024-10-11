from behave import given, when, then


@when('Click on Secondary option at the left side menu')
def click_on_secondary_option(context):
    context.app.secondary_deals_pagination_page.click_on_secondary_option()


@then('Verify the right page opens')
def open_the_right_page(context):
    context.app.secondary_deals_pagination_page.open_the_right_page('/secondary-listings')


@then('Go to the final page using the pagination button')
def go_to_the_final_page(context):
    context.app.secondary_deals_pagination_page.go_to_the_final_page()


@then('Go back to the first page using the pagination button')
def go_back_to_first_page(context):
    context.app.secondary_deals_pagination_page.go_back_to_first_page()
