import allure
from pages.pages_gis import PagesGis
from pages.pages_main import PagesMain

@allure.feature('Get Cold')
class TestGold:
    def test_positive_login(self, driver):
        city = 'Оймякон'

        pages_gis = PagesGis(driver, 'https://www.gismeteo.ru/')
        with allure.step('Перейти на gismeteo'):
            pages_gis.open()
        with allure.step('Найти Оймякон'):
            pages_gis.search(city)
        with allure.step('Клик на Завтра'):
            pages_gis.set_tomorrow()
        with allure.step('Клинуть на снег'):
            pages_gis.set_snow()
        with allure.step('Распечатать высоту снежного покрова'):
            print("kkk")
            print(pages_gis.get_snow)