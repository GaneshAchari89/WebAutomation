import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture
def setUp(browser, env):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome Browser.........")
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print("Launching firefox Browser.........")
    else:
        driver = webdriver.Ie(IEDriverManager().install())
        print("Launching IE Browser.........")
    print("Running test cases on {} environment".format(env.title()))
    return driver, env.lower()


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")
    parser.addoption("--env")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def env(request):
    return request.config.getoption("--env")


############## PyTest HTML Report #################
def pytest_configure(config):
    config._metadata['Project Name'] = 'Automation UI'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ganesh'


# It will delete/modify environment info in HTML report
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
