import os

from UI.pageObjects.LoginPage import LoginPage
from UI.utilities.customLogger import LogGenerator
from UI.utilities.readProperties import ReadConfig


class CommonElements:
    baseUrl = ReadConfig.getBaseUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    search_email = ReadConfig.getEmail()

    baseUrl_staging = ReadConfig.getBaseUrlStaging()
    username_staging = ReadConfig.getUsernameStaging()
    password_staging = ReadConfig.getPasswordStaging()
    search_email_staging = ReadConfig.getEmailStaging()

    logger = LogGenerator.generateLogger()
    screen_shots_path = "../screenshots/"

    def save_screenshot(self):
        self.driver.save_screenshot(
            self.screen_shots_path + os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0] + ".png")

    def launch_url(self,setup):
        driver = setup[0]
        env= setup[1]
        if env == "staging":
            self.logger.info("Launching staging url")
            driver.get(self.baseUrl_staging)
        elif env == "production":
            self.logger.info("Launching staging url")
            driver.get(self.baseUrl)
        else:
            self.logger.error("Please provide valid environment")
        driver.maximize_window()
        return driver

    def login_application(self,setup):
        driver = setup[0]
        env = setup[1]
        loginPage = LoginPage(driver)
        if env == "staging":
            loginPage.setUserName(self.username_staging)
            loginPage.setPassword(self.password_staging)
        elif env == "production":
            loginPage.setUserName(self.username)
            loginPage.setPassword(self.password)
        else:
            self.logger.error("Please provide valid environment")
        loginPage.clickLogin()
        return driver

