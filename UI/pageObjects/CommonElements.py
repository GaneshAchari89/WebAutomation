import os

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
        self.driver.save_screenshot(self.screen_shots_path + os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]+".png")








