import allure

from configs.config import GlobalConfig
from pages.pages_yandex import PagesYandex


@allure.feature('Yandex  tests')
class TestYandex:

    def test_search(self, driver, configuration: GlobalConfig, clear_bucket):
        pages_ya = PagesYandex(driver, configuration.base_url, configuration.cart_url, configuration.goods_0)
        pages_ya.open()
        with allure.step('Login'):
            pages_ya.login(configuration.login, configuration.password)
        with allure.step('Search goods'):
            pages_ya.use_search()
        with allure.step('Check cart'):
            pages_ya.get_url()
        with allure.step('Check print'):
            print("hi allure")

