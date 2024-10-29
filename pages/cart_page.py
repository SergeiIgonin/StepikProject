from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):

    'Проверка того, что корзина пуста'
    def is_cart_empty(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_AVAILABILITY_MSG), "Корзина не пуста, есть текст 'Товары в корзине'"
        assert self.is_not_element_present(*CartPageLocators.QUANTITY_OF_GOODS_FIELD),  "Корзина не пуста, есть поле с количеством товаров"

    'Проверка наличия подтверждающего сообщения о пустой корзине'
    def present_text_about_empty_cart(self):
        cart_message = self.driver.find_element(*CartPageLocators.CART_MSG)
        assert "корзина пуста" or "basket is empty" in cart_message.text, "Корзина не пуста"
