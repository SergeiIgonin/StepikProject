from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver   # аннотация драйвера (для дальнейшего автоподставления его методов)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators


class BasePage:
    'Инициализация объекта драйвера и url для любых страниц'
    def __init__(self, driver, url):
        self.driver: WebDriver = driver  # так Selenium поймет, что driver это экземпляр класса WebDriver (для автоподставления его методов)
        self.url = url

    'Проверка присутствия элемента на странице'
    def is_element_present(self, method, locator):
        try:
            self.driver.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    'Проверка отсутствия элемента на странице (в течении заданного времени)'
    def is_not_element_present(self, method, locator):
        wait = WebDriverWait(self.driver, 5, 1)
        try:
            wait.until(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            return True
        return False

    'Проверка исчезновения элемента со страницы (т.е. когда изначально он есть, а потом исчезает)'
    def is_element_disappeared(self, method, locator):
        wait = WebDriverWait(self.driver, 5, 1)
        try:
            wait.until_not(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            return False
        return True

    'Переход на страницу корзины'
    def go_to_cart(self):
        go_to_cart_button = self.driver.find_element(*BasePageLocators.GO_TO_CART_BUTTON)
        go_to_cart_button.click()

    'Переход на страницу регистрации и авторизации'
    def go_to_login_page(self):
        login_link = self.driver.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    'Открытие страницы'
    def open(self):
        self.driver.get(self.url)

    'Проверка наличия ссылки на страницу логина'
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Отсутствует ссылка на страницу регистрации/авторизации"

    'Проверка того, что пользователь авторизован'
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "Пользователь не авторизован — отсутствует user icon"
