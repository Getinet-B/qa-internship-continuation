Feature: Test Scenario for Opening User guide page

  Scenario: User can open User guide page
    Given Open the main page https://soft.reelly.io
    When Log in to the page
    And Click on settings option
    And Click on User Guide option
    Then Verify the right page opens
    Then Verify all lesson videos contain titles

