import allure

from pages.pages_gis import PagesGis


class TestSnow:

    def test_snow_in_gismeteo(self, driver, set_city_kazan, set_city_sochi):
        pages_main = PagesGis(driver, 'https://www.gismeteo.ru/')
        #pages_main.open()
        #pages_main.search("Казань")
        pages_main.set_tomorrow()
        pages_main.set_snow()











