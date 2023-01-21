import pytest
import json

import urllib3
from urllib3 import exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


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
    #return f'{Settings.CONFIGS_PATH}/{Settings.CONFIGS.get(environ)}'


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
def clear_bucket():
    """
    Фикстура для очистки корзины
    """
    return 14


#@pytest.fixture()
#def clear_bucket_on_failure(self, request):
 #   yield

#    self.bucket.highlight_and_make_screenshot()
#    if request.session.testsfailed:
 #       self.cart.open_page()
 #       self.cart.empty_bucket()


def read_config_file(file_path) -> dict:
    with open(file_path) as config_file:
        data = json.load(config_file)

    return data


@pytest.fixture(scope='session', autouse=True)
def disable_request_warnings() -> None:
    """
    Отключает варнинги со стороны urllib3 для работы requests по протоколу https.
    Почитать тут: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
    """
    urllib3.disable_warnings(exceptions.InsecureRequestWarning)
