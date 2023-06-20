from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from UI.pageObjects.CommonOperations import CommonOperations


class LoginPage(CommonOperations):

    def setUserName(self, username):
        self.clear_send_keys("textbox_username_xpath",username)

    def setPassword(self, password):
        self.clear_send_keys("textbox_password_xpath",password)

    def clickLogin(self):
        self.wait_and_click("button_login_xpath")

    def clickLogout(self):
        self.wait_and_click("link_logout_xpath")
