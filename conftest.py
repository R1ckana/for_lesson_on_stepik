import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose languages: es or fr')
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or edge')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    print('\nstart browser for tests...')
    yield browser
    print('\nquit browser...')
    browser.quit()
