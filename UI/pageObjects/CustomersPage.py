import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class CustomersPage:
    link_main_customers_xpath = "//div[@class='os-content']//ul[contains(@class,nav-sidebar)]//i[contains(@class,'user')]//following-sibling::p[contains(text(),'Customers')]"
    link_sub_customers_xpath = "//div[@class='os-content']//ul[contains(@class,nav-sidebar)]//a[contains(@href,'List')]//following-sibling::p[contains(text(),'Customers')]"
    text_search_email_xpath = "//input[@id='SearchEmail']"
    button_search_xpath = "//button[@id='search-customers']"
    text_search_result_email_xpath = "//table[@id='customers-grid']//tr[@class='odd']//td[2]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 180)

    def navigate_to_customers(self):
        self.driver.find_element(By.XPATH, self.link_main_customers_xpath).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.link_sub_customers_xpath)))
        self.driver.find_element(By.XPATH, self.link_sub_customers_xpath).click()

    def search_email(self, email):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.text_search_email_xpath)))
        self.driver.find_element(By.XPATH, self.text_search_email_xpath).send_keys(email)

    def click_search(self):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.button_search_xpath)))
        self.driver.find_element(By.XPATH, self.button_search_xpath).click()

    def validate_search_result(self):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.text_search_result_email_xpath)))
        return self.driver.find_element(By.XPATH, self.text_search_result_email_xpath).text
