
from pages.pages_yandex import PagesYandex


class TestYandex:
    def test_order(self, driver, clear_bucket_on_failure):
        username = 'selenium.introduction@mail.ru'
        password = 'qwerty@2020'
        pages_ya = PagesYandex(driver, 'https://market.yandex.ru/')
        pages_ya.open()
        pages_ya.login(username, password)


