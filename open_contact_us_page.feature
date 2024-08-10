Feature: Test Scenario for Opening the Contact us page

  Scenario: User can open the Contact us page
    Given Open the main page https://soft.reelly.io
    When Log in to the page
    And Click on settings option
    And Click on Contact us option
    Then Verify the right page opens
    Then Verify there are at least 4 social media icons
    Then Verify “Connect the company” button is available and clickable