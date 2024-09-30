Feature: Test Scenario for Accessing settings and seeing the right number of UI elements

  Scenario: User can go to settings and see the right number of UI elements
  Given Open the main page https://soft.reelly.io
  When Log in to the page
  And Click on settings option
  Then Verify the right page opens
  Then Verify there are 12 options for the settings
  Then Verify “connect the company” button is available
    