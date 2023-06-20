import os

from UI.utilities.customLogger import LogGenerator
from UI.utilities.readProperties import ReadConfig


class CommonElements:
    baseUrl = ReadConfig.getBaseUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGenerator.generateLogger()
    search_email = ReadConfig.getEmail()

    screen_shots_path = "../screenshots/"

    def take_and_save_screenshot(self):
        self.driver.save_screenshot(self.screen_shots_path + os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]+".png")








