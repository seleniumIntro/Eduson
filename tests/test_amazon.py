from pages.pages_amazon import PagesAmazon


class TestLogin:
    def test_positive_login(self, driver):
        username = 'selenium.introduction@mail.ru'
        password = '123456'
        pages_amazon = PagesAmazon(driver, 'https://amazon.com/')
        pages_amazon.open()
        pages_amazon.login(username, password)
        assert "Hello, test" == pages_amazon.get_login()
