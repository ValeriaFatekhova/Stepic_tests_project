import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    pass
    # parser.addoption('--language', action='store', default=None,
    #                  help="Choose language: ru or en-gb")


@pytest.fixture(scope="function")
def browser():
    #user_language = request.config.getoption("language")
    #options = Options()
    #options.add_experimental_option('prefs', {'into.accept_languages': user_language})
    #browser = None
    browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
    yield browser
    browser.quit()
