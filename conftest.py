import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language')


@pytest.fixture(scope="function")
def driver(request):
    user_language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
