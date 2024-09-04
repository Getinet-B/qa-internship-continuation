Feature: Test Scenario for Opening Subscription & payments page

  Scenario: User can open Subscription & payments page
    Given Open the main page https://soft.reelly.io
    When Log in to the page
    And Click on settings option
    And Click on Subscription & payments option
    Then Verify the right page opens
    Then Verify title “Subscription & payments” is visible
    Then Verify “back” and “upgrade plan” buttons are available