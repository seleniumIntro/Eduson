import allure
import pytest

from configs.config import GlobalConfig
from pages.pages_yandex import PagesYandex


class TestParallel:
    @allure.feature('yandex cart test')
    def test_search(self, driver, configuration: GlobalConfig):
        pages_ya = PagesYandex(driver, configuration.base_url, configuration.cart_url, configuration.goods_0)
        pages_ya.open()
        with allure.step('Login'):
            pages_ya.login(configuration.login, configuration.password)
        with allure.step('Search goods'):
            pages_ya.use_search()
        #with allure.step('Check cart'):
            #print(pages_ya.get_url())

