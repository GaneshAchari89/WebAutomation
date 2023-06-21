import os

import pytest

from UI.pageObjects.CommonElements import CommonElements
from UI.pageObjects.LoginPage import LoginPage


class Test_0001_Login(CommonElements):

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setUp):
        self.logger.info("**************** Test_0001_Login ****************")
        self.logger.info("**************** Verifying Home page title ****************")
        self.driver = setUp[0]
        if setUp[1] == "staging":
            self.logger.info("Launching staging url")
            self.driver.get(self.baseUrl_staging)
        elif setUp[1] == "production":
            self.logger.info("Launching production url")
            self.driver.get(self.baseUrl)
        else:
            self.logger.error("Please provide valid environment")
        self.driver.maximize_window()
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            assert True
            self.logger.info("**************** Home Page Title test case is passed ****************")
            self.driver.close()
        else:
            self.save_screenshot()
            self.driver.close()
            self.logger.error("**************** Home Page Title test case is failed ****************")
            assert False

    @pytest.mark.smoke
    def test_login(self, setUp):
        self.logger.info("**************** Verifying Login Test ****************")
        self.driver = setUp[0]
        if setUp[1] == "staging":
            self.logger.info("Launching staging url")
            self.driver.get(self.baseUrl_staging)
            self.driver.maximize_window()
            self.loginPage = LoginPage(self.driver)
            self.loginPage.setUserName(self.username_staging)
            self.loginPage.setPassword(self.password_staging)
        elif setUp[1] == "production":
            self.logger.info("Launching staging url")
            self.driver.get(self.baseUrl)
            self.driver.maximize_window()
            self.loginPage = LoginPage(self.driver)
            self.loginPage.setUserName(self.username)
            self.loginPage.setPassword(self.password)
        else:
            self.logger.error("Please provide valid environment")
        self.loginPage.clickLogin()
        actual_title = self.driver.title
        if actual_title == 'Dashboard / nopCommerce administration':
            assert True
            self.logger.info("**************** Login test case is passed ****************")
            self.driver.close()
        else:
            self.save_screenshot()
            self.logger.error("**************** Login test case is failed ****************")
            self.driver.close()
            assert False
