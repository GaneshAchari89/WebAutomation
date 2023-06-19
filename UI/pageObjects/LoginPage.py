from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from UI.pageObjects.CommonUtils import CommonUtils


class LoginPage(CommonUtils):

    def setUserName(self, username):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element.get('textbox_username_xpath'))))
        self.driver.find_element(By.XPATH, self.element.get('textbox_username_xpath')).clear()
        self.driver.find_element(By.XPATH, self.element.get('textbox_username_xpath')).send_keys(username)

    def setPassword(self, password):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element.get('textbox_password_xpath'))))
        self.driver.find_element(By.XPATH, self.element.get('textbox_password_xpath')).clear()
        self.driver.find_element(By.XPATH, self.element.get('textbox_password_xpath')).send_keys(password)

    def clickLogin(self):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element.get('button_login_xpath'))))
        self.driver.find_element(By.XPATH, self.element.get('button_login_xpath')).click()

    def clickLogout(self):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element.get('link_logout_xpath'))))
        self.driver.find_element(By.XPATH, self.element.get('link_logout_xpath')).click()
