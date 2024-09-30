from behave import given, when, then


@then('Verify the right page opens')
def open_the_right_page(context):
    context.app.right_number_ui_elements_page.open_the_right_page('/settings')


@then('Verify there are {num_elements} options for the settings')
def verify_the_number_of_options(context, num_elements):
    context.app.right_number_ui_elements_page.verify_the_number_of_options(int(num_elements))


@then('Verify “connect the company” button is available')
def verify_company_button_available(context):
    context.app.right_number_ui_elements_page.verify_company_button_available()
