import allure
from pages.pages_yandex import PagesYandex


class TestYandex:
    @allure.feature('Example tests')
    def test_order(self, driver):
        username = 'selenium.introduction@mail.ru'
        password = 'qwerty@2020'
        pages_ya = PagesYandex(driver, 'https://market.yandex.ru/')
        pages_ya.open()
        with allure.step('Go to page "Orders".'):
            pages_ya.login(username, password)
        #pages_ya.create_bucket()


