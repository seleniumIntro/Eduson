import pytest

from configs.config import GlobalConfig
from pages.pages_amazon import PagesAmazon
from pages.pages_gis import PagesGis
from pages.pages_main import PagesMain


@pytest.mark.xdist_group("group1") #декоратор для параллезации
class TestParallel:

    #первый тест для параллельного запуска
    def test_positive_login_mail_ru(self, driver, configuration: GlobalConfig):
        pages_main = PagesMain(driver, 'https://mail.ru/')
        pages_main.open()
        #Login in mail.ru
        pages_main.login(configuration.login, configuration.password)
        #Get email text
        pages_main.get_login()
        #Check email text
        assert configuration.login == pages_main.get_login()

    #второй тест для параллельного запуска
    def test_set_snow(self, driver, configuration: GlobalConfig):
        pages_main = PagesGis(driver, 'https://www.gismeteo.ru/')
        pages_main.set_tomorrow()
        pages_main.set_snow()

    #третий тест для параллельного запуска
    def test_login_in_amazon(self, driver, configuration: GlobalConfig):
        email = 'selenium.introduction@mail.ru'
        password = 123456
        pages_amazon = PagesAmazon(driver, "https://www.amazon.com/")
        pages_amazon.open()
        pages_amazon.login(email, password)
        assert "Hello, test" == pages_amazon.get_login()

