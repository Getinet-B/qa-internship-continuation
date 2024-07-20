Feature: Test Scenario for going to settings and edit the personal information

  Scenario: User can go to settings and edit the person information
    Given Open main page
    When Log in to the page
    And Click on settings option
    And Click on Edit profile option
    And Enter some test information in the input fields
    Then Check the right information is present in the input fields
    Then Check “Close” and “Save Changes” buttons are available and clickable

