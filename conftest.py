import time

import pytest
import json

import urllib3
from urllib3 import exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from configs.config import GlobalConfig
from pages.pages_gis import PagesGis
from pages.pages_yandex import PagesYandex


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def cfg_file_path() -> str:
    return r'C:\Users\andsb\Eduson\configs\prod.json'
    # return f'{Settings.CONFIGS_PATH}/{Settings.CONFIGS.get(environ)}'


@pytest.fixture(scope='session', autouse=True)
def get_config_data(cfg_file_path: str) -> dict:
    """
    Фикстура для получени данных из конфиг файла или из переменных окружения.

    :param feature_branch_name: name of the feature branch needed for urls update
    :type: String

    :return: возвращает данные из конфиг файла.
    :rtype: Dict
    """
    return read_config_file(file_path=cfg_file_path)

@pytest.fixture(scope='function')
def print_city():
    yield
    print("Ульяновск")




@pytest.fixture()
def set_city(driver):
    pages_main = PagesGis(driver, 'https://www.gismeteo.ru/')

    pages_main.open()
    pages_main.search("Казань")


@pytest.fixture()
def clear_bucket(driver, configuration):
    pages_ya = PagesYandex(driver, configuration.base_url, configuration.cart_url, configuration.goods_0)
    pages_ya.open()



@pytest.fixture
def set_city_kazan(driver):
    pages_main = PagesGis(driver, 'https://www.gismeteo.ru/')
    pages_main.open()
    pages_main.search("Казань")

@pytest.fixture
def set_city_sochi(driver):
    pages_main = PagesGis(driver, 'https://www.gismeteo.ru/')
    yield pages_main.open()
    pages_main.search("Сочи")
    time.sleep(5)





@pytest.fixture(scope='session')
def test_print():
    print("очистка")
    """
    Фикстура для очистки корзины
    """


def read_config_file(file_path) -> dict:
    with open(file_path) as config_file:
        data = json.load(config_file)

    return data


@pytest.fixture(scope='session')
def configuration(get_config_data) -> GlobalConfig:
    test_configuration = GlobalConfig(get_config_data)

    return test_configuration


@pytest.fixture(scope='session', autouse=True)
def disable_request_warnings() -> None:
    """
    Отключает варнинги со стороны urllib3 для работы requests по протоколу https.
    Почитать тут: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
    """
    urllib3.disable_warnings(exceptions.InsecureRequestWarning)
