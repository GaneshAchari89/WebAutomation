import pytest

from UI.pageObjects.CommonElements import CommonElements
from UI.pageObjects.LoginPage import LoginPage
from UI.pageObjects.CustomersPage import CustomersPage


class Test_0005_Customers(CommonElements):

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_customers_search(self, setUp):
        self.logger.info("**************** Test_0005_Customers ****************")
        self.logger.info("**************** Verifying Customer Search Test ****************")
        self.setup = setUp
        self.launch_url(self.setup)
        self.driver = self.login_application(self.setup)
        self.customer = CustomersPage(self.driver)
        self.customer.navigate_to_customers()
        self.customer.search_email(self.search_email_staging)
        self.customer.click_search()

        actual_search_result = self.customer.validate_search_result()
        if actual_search_result == self.search_email_staging:
            assert True
            self.logger.info("**************** Customer search test case is passed ****************")
            self.driver.close()
        else:
            self.save_screenshot()
            self.driver.close()
            self.logger.error("**************** Customer search Title test case is failed ****************")
            assert False
