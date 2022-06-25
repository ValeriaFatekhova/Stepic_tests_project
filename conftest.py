import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language: ru or en-gb")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'into.accept_languages': user_language})
    browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe", options=options)
    yield browser
    browser.quit()
