import pytest
from UI.pageObjects.CommonElements import CommonElements


class Test_0001_HomePage(CommonElements):

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setUp):
        self.logger.info("**************** Test_0001_HomePage ****************")
        self.logger.info("**************** Verifying Home page title ****************")
        self.setup = setUp
        self.driver=self.launch_url(self.setup)
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



