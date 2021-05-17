from Test.conftest import browser
from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators
from .main_page import MainPage


class LoginPage(BasePage):
    # def should_be_login_page(self):
    #     self.should_be_login_url()
    #     self.should_be_login_form()
    #     self.should_be_register_form()
    #
    # def should_be_login_url(self):
    #     # реализуйте проверку на корректный url адрес
    #     assert True
    #
    # def should_be_login_form(self):
    #     # реализуйте проверку, что есть форма логина
    #     assert self.is_element_present(*LoginPageLocators.FORM_REGISTER), "Форма регистрации присутствует на странице"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице

        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER), "Форма регистрации присутствует на странице"
