from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open gettop page')
def open_gettop(context):

    context.app.main_page.open_main_page()

@when("User clicks 'lost your password'link")
def click_link(context):
    context.app.main_page.click_lost_password()
    sleep(5)

@then("verify user is taken to 'My Account'page")
def verify_my_account(context):
    context.app.main_page.verify_password_page('BEST SELLING')
    print ('Test case Passed')
