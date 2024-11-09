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
    print("\nstart chrome browser for test..")
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit driver..")
    driver.quit()


# "Запуск тестов на выбор и в разных языковых версиях сайта и/или в разных браузерах (Chrome, Firefox) командами"
# "pytest -sv --browser_name=firefox/ pytest -sv --language=es"
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default="chrome",
#                      help="Choose browser: chrome or firefox")
#     parser.addoption('--language', action='store', default=None,
#                      help="Select browser language")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     lang = request.config.getoption("language")
#     browser = None
#     if browser_name == "chrome":
#         options = Options()
#         options.add_experimental_option('prefs', {'intl.accept_languages': lang})
#         browser = webdriver.Chrome()
#         browser = webdriver.Chrome(options=options)
#         print(f"\nstart chrome browser with language '{lang}' for test...")
#     elif browser_name == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.set_preference('intl.accept_languages', lang)
#         browser = webdriver.Firefox(options=options)
#         print(f"\nstart firefox browser with language '{lang}' for test...")
#     else:
#         raise pytest.UsageError("--browser should be chrome or firefox")
#
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
