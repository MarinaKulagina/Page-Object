from selenium.common.exceptions import NoSuchElementException

class BasePage:

    #добавляем метод конструктор - метод вызывается при создании
#объекта. В него передаем экземаляр драйвера и url.
    # def __init__(self, browser, url):
    #     self.browser = browser
    #     self.url = url

    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    # Открытие страницы в браузере
    # def open(self):
    #     self.browser.get(self.url)

    def open(self):
        self.browser.get(self.link)

    # Проверка исключений, вывод адекватного сообщения
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

