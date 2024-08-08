Feature: Test Scenario for opening the community page

  Scenario: User can open the community page
    Given Open main page
    When Log in to the page
    And Click on settings option
    And Click on Community option
    Then Verify the right page opens
    Then Verify "Contact support" button is available and clickable
