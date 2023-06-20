from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from UI.pageObjects.CommonOperations import CommonOperations


class CustomersPage(CommonOperations):

    def navigate_to_customers(self):
        self.driver.find_element(By.XPATH, self.element.get('link_main_customers_xpath')).click()
        self.wait_and_click("link_sub_customers_xpath")

    def search_email(self, email):
        self.clear_send_keys("text_search_email_xpath",email)

    def click_search(self):
        self.wait_and_click("button_search_xpath")

    def validate_search_result(self):
        self.get_text("text_search_result_email_xpath")
