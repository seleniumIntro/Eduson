from pages.pages_main import PagesMain


class TestSeach:
    def test_positive_search(self, driver):
        pages_main = PagesMain(driver, 'https://mail.ru/')
        pages_main.open()
        pages_main.use_search()
        assert 'Кошка' == pages_main.get_dzen_result()
