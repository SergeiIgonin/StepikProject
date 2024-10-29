from pages.login_page import LoginPage


def test_should_be_login_page(driver):
    url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    login_page = LoginPage(driver, url)
    login_page.open()
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()
