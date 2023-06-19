import yaml
from selenium.webdriver.support.wait import WebDriverWait


class CommonUtils:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 180)
        self.element = self.get_element(self.__class__.__name__)

    @staticmethod
    def get_element(file_name):
        with open('../pageObjects/PageElements/' + file_name + ".yaml") as file:
            return yaml.load(file, Loader=yaml.SafeLoader)
