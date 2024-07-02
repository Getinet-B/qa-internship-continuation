Feature: Test Scenario for entering info into input fields on registration page

  Scenario: The user can enter the information into the input fields on the registration page
    Given Open registration page
    Then Click on "Sign in" link
    When Enter Information in the Input fields
    Then Verify the right information is present