import yaml

from UI.utilities.customLogger import LogGenerator
from UI.utilities.readProperties import ReadConfig


class CommonElements:
    baseUrl = ReadConfig.getBaseUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGenerator.generateLogger()
    search_email = ReadConfig.getEmail()

    screen_shots_path = "../screenshots/"

    @staticmethod
    def get_element(file_name):
        with open('../pageObjects/PageElements/' + file_name + ".yaml") as file:
            return yaml.load(file, Loader=yaml.SafeLoader)






