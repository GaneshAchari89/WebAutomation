import pytest

from UI.pageObjects.CommonElements import CommonElements
from UI.pageObjects.LoginPage import LoginPage
from UI.pageObjects.CustomersPage import CustomersPage


class Test_0006_Login_Customers(CommonElements):

    @pytest.mark.smoke
    @pytest.mark.dependency()
    def test_login_customer(self, setUp):
        self.logger.info("**************** Test_0006_Login_Customers ****************")
        self.logger.info("**************** Verifying Login Test ****************")
        self.setup = setUp
        self.launch_url(self.setup)
        self.driver = self.login_application(self.setup)
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

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.dependency(depends=["Test_0006_Login_Customers::test_login_customer"])
    def test_customers_add(self, setUp):
        self.logger.info("**************** Test_0005_Customers ****************")
        self.logger.info("**************** Verifying Customer add new button Test ****************")
        self.setup = setUp
        self.launch_url(self.setup)
        self.driver = self.login_application(self.setup)
        self.customer = CustomersPage(self.driver)
        self.customer.navigate_to_customers()
        if self.customer.validate_add_new_button():
            assert True
            self.logger.info("**************** Customer add new button test case is passed ****************")
            self.driver.close()
        else:
            self.save_screenshot()
            self.driver.close()
            self.logger.error("**************** Customer add new button test case is failed ****************")
            assert False

