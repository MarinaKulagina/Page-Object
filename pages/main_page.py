from selenium.webdriver.common.by import By
from .locators import MainPageLocators

from .base_page import BasePage

class MainPage(BasePage):

    # Переход на страницу логина
    def __init__(self, browser, link, timeout=10):
        super().__init__(browser, link, timeout=10)
        self.should_be_register_form = None

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

     #метод проверяет наличие ссылки авторизации на странице (проверка css селектора)
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Селектора не существует"
