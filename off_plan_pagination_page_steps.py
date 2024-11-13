from behave import given, when, then


@when('Click on "Off Plan" option at the left side menu')
def click_on_off_plan_option(context):
    context.app.off_plan_pagination_page.click_on_off_plan_option()


@then("Verify the Off Plan page opens")
def verify_off_plan_page_opens(context):
    context.app.off_plan_pagination_page.verify_off_plan_page_opens('soft.reelly.io')


@then("Go to the final page using the pagination button")
def go_to_final_page(context):
    context.app.off_plan_pagination_page.go_to_final_page()


@then("Go back to the first page using the pagination button")
def go_back_to_first_page(context):
    context.app.off_plan_pagination_page.go_back_to_first_page()