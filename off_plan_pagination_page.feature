Feature: User can navigate through the Off Plan page and use pagination

  Scenario: User can open the Off Plan page and go through the pagination
    Given Open the main page https://soft.reelly.io
    When Log in to the page
    And Click on "Off Plan" option at the left side menu
    Then Verify the Off Plan page opens
    And Go to the final page using the pagination button
    And Go back to the first page using the pagination button