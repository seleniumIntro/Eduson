import pytest

from pages.pages_main import PagesMain


class TestSeach:
    def test_positive_search(self, driver):
        pages_main = PagesMain(driver, 'https://mail.ru/')
        pages_main.open()
        pages_main.use_search()
        assert 'Кошка' == pages_main.get_dzen_result()





testparams = [
    (7, 2, 3, 4, 5, 6, 7),
    (7, 6, 5, 4, 3, 2, 1),
    (7, 6, 5, 4, 3, 2, 1),
    (1, 6, 5, 4, 3, 2, 1),
]

@pytest.mark.parametrize('a, b, c, d, e, f, g', testparams)
def test_many_args(a, b, c, d, e, f, g):
    assert d == 4
    assert a == 7
