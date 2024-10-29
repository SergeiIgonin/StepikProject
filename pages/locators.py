
class BasePageLocators:
    GO_TO_CART_BUTTON = ("xpath", "//a[@class='btn btn-default']")
    LOGIN_LINK = ("xpath", "//a[@id='login_link']")
    LOGIN_LINK_INVALID = ("xpath", "//a[@id='mogin_link']")  # пример кривого локатора для демонстрации падающего теста
    USER_ICON = ("xpath", "//i[@class='icon-user']")


class LoginPageLocators:
    LOGIN_FORM = ("xpath", "//form[@id='login_form']")
    REGISTER_FORM = ("xpath", "//form[@id='register_form']")
    REG_EMAIL_FIELD = ("xpath", "//input[@id='id_registration-email']")
    REG_PASSWORD_FIELD1 = ("xpath", "//input[@id='id_registration-password1']")
    REG_PASSWORD_FIELD2 = ("xpath", "//input[@id='id_registration-password2']")
    REG_BUTTON = ("xpath", "//button[@value='Register']")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = ("xpath", "//button[contains(@class, 'add-to-basket')]")
    SUCCESS_MESSAGE = ("xpath", "(//div[@class='alertinner '])[1]")
    PRODUCT_NAME_MSG = ("xpath", "(//div/strong)[3]")
    PRODUCT_NAME_REAL = ("xpath", "//div/h1")
    PRODUCT_PRICE_MSG = ("xpath", "(//div/p/strong)[2]")
    PRODUCT_PRICE_REAL = ("xpath", "//div/p[@class='price_color']")


class CartPageLocators:
    CART_MSG = ("xpath", "//div[@id='content_inner']/p")
    PRODUCT_AVAILABILITY_MSG = ("xpath", "//h2[@class='col-sm-6 h3']")
    QUANTITY_OF_GOODS_FIELD = ("xpath", "//div/input[@id='id_form-0-quantity']")
