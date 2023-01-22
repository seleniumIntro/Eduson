import allure
import pytest

from configs.config import GlobalConfig
from pages.pages_main import PagesMain
from pages.pages_yandex import PagesYandex


#pytest.mark.xdist_group("group1")
class TestParallel:

    def test_order(self, driver, configuration: GlobalConfig):
        pages_ya = PagesYandex(driver, 'https://market.yandex.ru/')
        pages_ya.open()
        with allure.step('Login'):
            pages_ya.login(configuration.login, configuration.password)


    def test_positive_login_mail_ru(self, driver, configuration: GlobalConfig):
        pages_main = PagesMain(driver, 'https://mail.ru/')
        pages_main.open()
        with allure.step('Login in mail.ru'):
            pages_main.login(configuration.login, configuration.password)
        with allure.step('Get email text'):
            pages_main.get_login()
        with allure.step('Check email text'):
            assert configuration.login == pages_main.get_login()
