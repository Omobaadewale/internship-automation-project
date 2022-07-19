from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('open gettop page')
def open_gettop(context):

    context.app.main_page.open_main_page()


@given('Open gettop main page')
def open_gettop_main_page(context):
    context.app.main_page.open_gettop_main_page()


@when("User clicks 'lost your password'link")
def click_link(context):
    context.app.main_page.click_lost_password()
    sleep(5)


@when('user hovers over accessories')
def hover_accessories(context):
    context.app.main_page.hover_accessories()



@then("verify {expected_result} text is seen")
def verify_my_account(context, expected_result):
    context.app.main_page.verify_password_page(expected_result)
    print ('Test case Passed')


@then('verify each drop down link is clickable')
def verify_link1_clickable(context):
    context.app.main_page.verify_cases_clickable()
    sleep(5)


@then('verify airpod wireless link is clickable')
def verify_airpod_wireless(context):
    context.app.main_page.verify_airpod_wireless()

@then("verify airpods pro link is clickable")
def verify_airpod_pro(context):
    context.app.main_page.verify_airpod_pro()
    sleep(5)
    print('Test Case Passed')
