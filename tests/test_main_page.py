import pytest
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.smoke
@pytest.mark.login_guest
class TestLoginFromMainPage():

    'Пример проверочного метода с переключением на др. стр. (т.е. поочередная работа со стр.)'

    def test_guest_can_go_to_login_page_from_login_page(self, driver):      # в атрибут передаем фикстуру 'driver' из conftest.py
        url = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(driver, url)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_url()

    def test_guest_should_see_login_link_on_main_page(self, driver):
        url = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(driver, url)
        main_page.open()
        main_page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_main_page(driver):  # для функций вне классов не нужно передавать параметр self
    url = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_cart()
    cart_page = CartPage(driver, driver.current_url)
    cart_page.present_text_about_empty_cart()
    cart_page.is_cart_empty()
