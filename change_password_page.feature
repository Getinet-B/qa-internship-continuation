Feature: Test Scenario for Opening change password page

  Scenario: User can open change password page
    Given Open the main page https://soft.reelly.io
    When Log in to the page
    And Click on settings option
    And Click on Change password option
    Then Verify the page(s) opens
    And Add some test "password" to the input fields
    Then Verify the "Change password" button is available (but don't click on it)



