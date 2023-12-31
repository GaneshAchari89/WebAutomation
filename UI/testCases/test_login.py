import pytest
from UI.pageObjects.CommonElements import CommonElements


class Test_0002_Login(CommonElements):

    @pytest.mark.smoke
    def test_login(self, setUp):
        self.logger.info("**************** Test_0002_Login ****************")
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

