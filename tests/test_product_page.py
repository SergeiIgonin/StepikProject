import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import time


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(driver):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    url2 = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.should_be_button_add_to_cart()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_correct_product_name()
    product_page.should_be_correct_product_price()


def test_guest_cant_see_success_message_before_adding_product_to_cart(driver):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="Пример падающего теста, т.к. success_message присутствует")
def test_guest_should_see_success_message_after_adding_product_to_cart(driver):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="Пример падающего теста, т.к. в данном случае на странице ничего не исчезает")
def test_message_disappeared_after_adding_product_to_cart(driver):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_see_element_disappear()


def test_guest_should_see_login_link_on_product_page(driver):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.go_to_login_page()


'Запуск параметризованного теста'
# по итогу проверок тот параметр, на котором тест падает мы пометили как ожидаемо падающий (типа его никак не пофиксят)'
params = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]


@pytest.mark.parametrize('param', params)
def test_guest_can_add_product_to_cart_with_param(driver, param):
    url = param
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.should_be_button_add_to_cart()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_correct_product_name()
    product_page.should_be_correct_product_price()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(driver):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    product_page = ProductPage(driver, url)
    product_page.open()
    product_page.go_to_cart()
    time.sleep(20)
    cart_page = CartPage(driver, driver.current_url)
    cart_page.present_text_about_empty_cart()
    cart_page.is_cart_empty()


@pytest.mark.like_user
class TestUserAddToCartFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        url = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "Qw!"
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.register_new_user(email, password)  # в аргументах передаем переменные (они же входящие параметры для вызываемого метода)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, driver):
        url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        product_page = ProductPage(driver, url)
        product_page.open()
        time.sleep(5)
        product_page.should_be_button_add_to_cart()
        product_page.add_product_to_cart()
        product_page.should_be_correct_product_name()
        product_page.should_be_correct_product_price()

    def test_user_cant_see_success_message_before_adding_product_to_cart(self, driver):
        url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(driver, url)
        product_page.open()
        product_page.should_not_be_success_message()
