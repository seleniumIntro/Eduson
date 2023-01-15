from pages.pages_main import PagesMain


class TestLogin:
    def test_positive_login(self, driver):
        username = 'selenium.introduction@mail.ru'
        password = 'qwerty@2020'
        pages_main = PagesMain(driver, 'https://mail.ru/')
        pages_main.open()
        pages_main.login(username, password)
        pages_main.get_login()
        assert username == pages_main.get_login()
