import time
import pytest

from UI.pageObjects.CommonElements import CommonElements
from UI.pageObjects.LoginPage import LoginPage
from UI.utilities import excelUtil


class Test_0002_ddt_Login(CommonElements):
    path = "../testData/LoginData.xlsx"

    @pytest.mark.smoke
    def test_login_ddt(self, setUp):
        self.logger.info("**************** Test_0002_ddt_Login ****************")
        self.logger.info("**************** Verifying Login Test ****************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.loginPage = LoginPage(self.driver)

        self.rows = excelUtil.getRowCount(self.path, 'Sheet1')

        status_list = []  # To store test result

        for r in range(2, self.rows + 1):
            self.username = excelUtil.readData(self.path, 'Sheet1', r, 1)
            self.password = excelUtil.readData(self.path, 'Sheet1', r, 2)
            self.expected = excelUtil.readData(self.path, 'Sheet1', r, 3)
            self.loginPage.setUserName(self.username)
            self.loginPage.setPassword(self.password)
            self.loginPage.clickLogin()
            time.sleep(5)
            actual_title = self.driver.title
            expected_title = 'Dashboard / nopCommerce administration'

            if actual_title == expected_title:
                if self.expected == 'Pass':
                    self.logger.info("**************** Login test case is passed ****************")
                    self.loginPage.clickLogout()
                    status_list.append("Pass")
                elif self.expected == 'Fail':
                    self.logger.info("**************** Login test case is failed ****************")
                    self.loginPage.clickLogout()
                    status_list.append("Fail")
            else:
                if self.expected == 'Pass':
                    self.logger.info("**************** Login test case is failed ****************")
                    status_list.append("Fail")
                elif self.expected == 'Fail':
                    self.logger.info("**************** Login test case is Passed ****************")
                    status_list.append("Pass")

        if "Fail" not in status_list:
            self.logger.info("**************** All Login test cases are passed ****************")
            self.driver.close()
            assert True
        else:
            self.logger.info("**************** Login test case is failed ****************")
            self.driver.close()
            assert False
