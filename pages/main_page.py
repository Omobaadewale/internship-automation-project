from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    LOST_PASSWORD = (By.LINK_TEXT, 'Lost your password?')
    BEST_SELLING = (By.XPATH, "//span[text()='Best Selling']")
    excpected_result = 'BEST SELLING'

    def open_main_page(self):
        self.open_page()

    def click_lost_password(self):
        self.click(*self.LOST_PASSWORD)


    def verify_password_page(self, expected_result):
        excpected_result = 'BEST SELLING'
        actual_result = self.driver.find_element(*self.BEST_SELLING).text
        assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected{expected_result}'


