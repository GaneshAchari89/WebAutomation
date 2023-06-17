import pytest

from UI.pageObjects.CommonElements import CommonElements
from UI.pageObjects.LoginPage import LoginPage
from UI.pageObjects.CustomersPage import CustomersPage


class Test_0002_Customers(CommonElements):

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_customers_search(self, setUp):
        self.logger.info("**************** Test_0002_Customers ****************")
        self.logger.info("**************** Verifying Customer Search Test ****************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()

        self.customer = CustomersPage(self.driver)
        self.customer.navigate_to_customers()
        self.customer.search_email(self.search_email)
        self.customer.click_search()

        actual_search_result = self.customer.validate_search_result()
        if actual_search_result == self.search_email:
            assert True
            self.logger.info("**************** Customer search test case is passed ****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(self.screen_shots_path + "test_customers_search.png")
            self.driver.close()
            self.logger.error("**************** Customer search Title test case is failed ****************")
            assert False
