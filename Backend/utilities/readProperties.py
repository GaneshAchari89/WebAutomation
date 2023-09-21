import configparser

config = configparser.RawConfigParser()
# config_path = "../Backend/configuration/config.ini"
config_path = "/Users/ganeshachari/Desktop/WebAutomation/Backend/configuration/config.ini"
config.read(config_path)


class ReadConfig:

    @staticmethod
    def getBaseUrl():
        return config.get('common info', 'baseUrl')

    @staticmethod
    def getUsersSchema():
        return config.get('schema', 'users_schema')




