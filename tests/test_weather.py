from conftest import test_print
from pages.pages_main import PagesMain


class TestWeather:
    def test_weather(self, driver, test_print):
        pages_main = PagesMain(driver, 'https://mail.ru/')
        pages_main.open()
        assert pages_main.get_weather() is not None