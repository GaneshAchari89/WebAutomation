from UI.utilities.customLogger import LogGenerator
from UI.utilities.readProperties import ReadConfig


class CommonElements:
    baseUrl = ReadConfig.getBaseUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGenerator.generateLogger()
    search_email = ReadConfig.getEmail()

    screen_shots_path = "../screenshots/"
