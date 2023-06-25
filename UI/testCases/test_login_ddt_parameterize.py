import time
import pytest

from UI.pageObjects.CommonElements import CommonElements
from UI.pageObjects.LoginPage import LoginPage
from UI.utilities import excelUtil


class Test_0004_ddt_login_parameterize(CommonElements):

    @pytest.mark.smoke
    @pytest.mark.parametrize("username,password",[('admin@yourstore.com','admin'),('admin@yourstore.com','ad')])
    def test_login_ddt_parameterize(self, setUp,username,password):
        self.logger.info("**************** Test_0004_ddt_login_parameterize ****************")
        self.logger.info("**************** Verifying Login Test ****************")
        self.setup = setUp
        self.driver = self.launch_url(self.setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(username)
        self.loginPage.setPassword(password)
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
