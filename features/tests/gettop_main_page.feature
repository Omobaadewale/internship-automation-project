# Created by Adewale at 7/10/2022
Feature: A test to verify gettop main page

  Scenario: Opening loggin page
  Given     open gettop page
    When    User clicks 'lost your password'link
    Then    verify user is taken to 'My Account'page