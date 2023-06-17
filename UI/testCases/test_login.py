import pytest

from UI.pageObjects.CommonElements import CommonElements
from UI.pageObjects.LoginPage import LoginPage


class Test_0001_Login(CommonElements):

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setUp):
        self.logger.info("**************** Test_0001_Login ****************")
        self.logger.info("**************** Verifying Home page title ****************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            assert True
            self.logger.info("**************** Home Page Title test case is passed ****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(self.screen_shots_path + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**************** Home Page Title test case is failed ****************")
            assert False

    @pytest.mark.smoke
    def test_login(self, setUp):
        self.logger.info("**************** Verifying Login Test ****************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        actual_title = self.driver.title
        if actual_title == 'Dashboard / nopCommerce administration':
            assert True
            self.logger.info("**************** Login test case is passed ****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(self.screen_shots_path + "test_login.png")
            self.logger.error("**************** Login test case is failed ****************")
            self.driver.close()
            assert False
