from pages.pages_main import PagesMain


class TestLogin:
    def test_send_mail(self, driver):
        username = 'selenium.introduction@mail.ru'
        password = 'qwerty@2020'
        pages_main = PagesMain(driver, 'https://mail.ru/')
        pages_main.open()
        pages_main.login(username, password)
        pages_main.get_login()
        pages_main.create_male()
