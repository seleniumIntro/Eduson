import allure

from configs.config import GlobalConfig
from pages.pages_yandex import PagesYandex


class TestYandex:
    @allure.feature('Example tests')
    def test_order(self, driver, configuration: GlobalConfig):
        #username = 'selenium.introduction@mail.ru'
        #password = 'qwerty@2020'

        pages_ya = PagesYandex(driver, 'https://market.yandex.ru/')
        pages_ya.open()
        with allure.step('Go to page "Orders".'):
            pages_ya.login(configuration.login, configuration.password)
        #pages_ya.create_bucket()


