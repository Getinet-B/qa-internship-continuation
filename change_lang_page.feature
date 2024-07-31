Feature: Test Scenario for changing the language from English to Russian

  Scenario: User can change the language from the page
    Given Open main page
    When Log in to the page
    And Click on Main Menu
    And Change the language to Russian "RU"
    Then Verify the language has changed


