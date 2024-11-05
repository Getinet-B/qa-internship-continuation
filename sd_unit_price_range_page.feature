Feature: Test Scenario for filtering the Secondary deals by Unit price range

  Scenario: User can filter the Secondary deals by Unit price range
  Given Open the main page https://soft.reelly.io
  When Log in to the page
  And Click on "Secondary" option at the left side menu
  Then Verify the right page opens
  And Click on Filters
  And Filter the products by price range from 1200000 to 2000000 AED
  And Click on Apply Filter
  Then Verify the price in all cards is inside the range (1200000 - 2000000)