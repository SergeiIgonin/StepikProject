from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    'Проверка того, что открыта именно страница регистрации/авторизации'
    def should_be_login_url(self):
        assert "pythonanywhere" in self.driver.current_url, "Ошибка в URL"

    'Проверка наличия формы авторизации'
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Отсутствует форма логина"

    'Проверка наличия формы регистрации'
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Отсутствует форма регистрации"

    'Регистрация нового пользователя'
    def register_new_user(self, email, password):  # метод принимает на вход email и password, которые мы передадим в тесте, в методе setup
        email_field = self.driver.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        password_field1 = self.driver.find_element(*LoginPageLocators.REG_PASSWORD_FIELD1)
        password_field2 = self.driver.find_element(*LoginPageLocators.REG_PASSWORD_FIELD2)
        reg_button = self.driver.find_element(*LoginPageLocators.REG_BUTTON)
        email_field.send_keys(email)
        password_field1.send_keys(password)
        password_field2.send_keys(password)
        reg_button.click()
