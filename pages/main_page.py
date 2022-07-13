from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(Page):
    LOST_PASSWORD = (By.LINK_TEXT, 'Lost your password?')
    BEST_SELLING = (By.XPATH, "//span[text()='Best Selling']")
    PRODUCT_ACCESSORY = (By.XPATH, "//a[text()='Accessories'and@class='nav-top-link']")
    CASES  = (By.CSS_SELECTOR, "#menu-item-485")
    AIRPODS_WIRELESS = (By.CSS_SELECTOR, "#menu-item-387")
    AIRPODS_PRO = (By.CSS_SELECTOR, "#menu-item-386")


    def open_main_page(self):
        self.open_page()


    def open_gettop_main_page(self):
        self.open_page()


    def click_lost_password(self):
        self.click(*self.LOST_PASSWORD)


    def verify_password_page(self, expected_result):
        actual_result = self.driver.find_element(*self.BEST_SELLING).text
        assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected{expected_result}'


    def hover_accessories(self):
        actions = ActionChains(self.driver)
        accessory = self.find_element(*self.PRODUCT_ACCESSORY)
        actions.move_to_element(accessory)
        actions.perform()


    def verify_cases_clickable(self):
        self.wait_for_element_appear(*self.CASES).click()


    def verify_airpod_wireless(self):
        self.wait_for_element_appear(*self.AIRPODS_WIRELESS).click()


    def verify_airpod_pro(self):
        self.wait_for_element_appear(*self.AIRPODS_PRO).click()






