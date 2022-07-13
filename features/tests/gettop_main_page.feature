# Created by Adewale at 7/10/2022
Feature: A test to verify gettop main page

  #Scenario: Opening loggin page
  #Given     open gettop page
   # When    User clicks 'lost your password'link
   # Then    verify BEST SELLING text is seen

    Scenario: Accessories link verification
      Given   Open gettop main page
      When    user hovers over accessories
      Then    verify each drop down link is clickable
      When    user hovers over accessories
      Then    verify airpod wireless link is clickable
      When    user hovers over accessories
      Then    verify airpods pro link is clickable