Feature: Test Scenario for Accessing Whatsapp and Telegram Communities

  Scenario: User can access Whatsapp and Telegram communities
  Given Open the main page https://soft.reelly.io
  When Log in to the page
  And Click on settings option
  And Click on support option
  And Switch to the new tab
  Then Verify the right page opens. (The link contains “api.whatsapp.com”). Don’t click on “Continue to Chat”
  And Go back
  And Click on news option. (The link contains “t.me”). Don’t click on “view in telegram”
  Then Verify the right page opens