from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from UI.pageObjects.CommonUtils import CommonUtils


class CustomersPage(CommonUtils):

    def navigate_to_customers(self):
        self.driver.find_element(By.XPATH, self.element.get('link_main_customers_xpath')).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element.get('link_sub_customers_xpath'))))
        self.driver.find_element(By.XPATH, self.element.get('link_sub_customers_xpath')).click()

    def search_email(self, email):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element.get('text_search_email_xpath'))))
        self.driver.find_element(By.XPATH, self.element.get('text_search_email_xpath')).send_keys(email)

    def click_search(self):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element.get('button_search_xpath'))))
        self.driver.find_element(By.XPATH, self.element.get('button_search_xpath')).click()

    def validate_search_result(self):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element.get('text_search_result_email_xpath'))))
        return self.driver.find_element(By.XPATH, self.element.get('text_search_result_email_xpath')).text
