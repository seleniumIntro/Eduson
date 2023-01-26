import allure

from pages.pages_gis import PagesGis

@allure.feature('Search meteo in gismeteo')
class TestSnow:
    @allure.testcase('https://testrail.test_org_.com/case_4')
    def test_snow_in_gismeteo(self, driver):
        pages_main = PagesGis(driver, 'https://www.gismeteo.ru/')
        with allure.step('Открыть гисметео'):
            pages_main.open()
        with allure.step('Найти Казань'):
            pages_main.search("Казань")
        with allure.step('Кликнуть на погоду "Завтра"'):
            pages_main.set_tomorrow()
        with allure.step('Кликнуть на снег'):
            pages_main.set_snow()
        with allure.step('Чекнуть высоту снежного покрова'):
            pages_main.get_snow()

