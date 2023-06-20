import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class CommonOperations:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 180)
        self.element = self.get_element(self.__class__.__name__)

    def get_element(self,file_name):
        with open('../pageObjects/PageElements/' + file_name + ".yaml") as file:
            return yaml.load(file, Loader=yaml.SafeLoader)

    def clear_send_keys(self,element,value):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element.get(element))))
        self.driver.find_element(By.XPATH, self.element.get(element)).clear()
        self.driver.find_element(By.XPATH, self.element.get(element)).send_keys(value)

    def wait_and_click(self,element):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element.get(element))))
        self.driver.find_element(By.XPATH, self.element.get(element)).click()

    def get_text(self,element):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element.get(element))))
        return self.driver.find_element(By.XPATH, self.element.get(element)).text


