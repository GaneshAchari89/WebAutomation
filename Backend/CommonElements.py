import os

from Backend.utilities.readProperties import ReadConfig
from Backend.utilities.customLogger import LogGenerator


class CommonElements():
    baseUrl = ReadConfig.getBaseUrl()

    logger = LogGenerator.generateLogger()
    screen_shots_path = "../Backend/screenshots/"

    def save_screenshot(self):
        self.driver.save_screenshot(
            self.screen_shots_path + os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0] + ".png")
