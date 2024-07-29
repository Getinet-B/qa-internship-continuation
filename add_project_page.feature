Feature: Test Scenario for Adding a Project Through the Settings Page

  Scenario: User can add a project through the settings
    Given Open main page
    When Log in to the page
    And Click on settings option
    And Click on Add a project
    Then Verify the right page opens
    And Add some test information to the input fields
    Then Verify the right information is present in the input fields
    Then Verify “Send an application” button is available and clickable