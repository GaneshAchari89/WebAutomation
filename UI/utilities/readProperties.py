import configparser

config = configparser.RawConfigParser()
config_path = "../configuration/config.ini"
config.read(config_path)


class ReadConfig:

    @staticmethod
    def getBaseUrl():
        return config.get('common info', 'baseUrl')

    @staticmethod
    def getUsername():
        return config.get('common info', 'username')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')

    @staticmethod
    def getEmail():
        return config.get('common info', 'search_email')

    @staticmethod
    def getBaseUrlStaging():
        return config.get('common info', 'baseUrl_staging')

    @staticmethod
    def getUsernameStaging():
        return config.get('common info', 'username_staging')

    @staticmethod
    def getPasswordStaging():
        return config.get('common info', 'password_staging')

    @staticmethod
    def getEmailStaging():
        return config.get('common info', 'search_email_staging')


