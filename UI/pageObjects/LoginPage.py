from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    textbox_username_xpath = "//input[@type='email']"
    textbox_password_xpath = "//input[@type='password']"
    button_login_xpath = "//button[@type='submit' and text()='Log in']"
    link_logout_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 180)

    def setUserName(self, username):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.textbox_username_xpath)))
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.textbox_password_xpath)))
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.link_logout_xpath)))
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
