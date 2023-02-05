from pages.pages_amazon import PagesAmazon


class TestAmazon:
    def test_auth_amazon(self, driver):
        email = 'selenium.introduction@mail.ru'
        password = 123456
        pages_amazon = PagesAmazon(driver, "https://www.amazon.com/")
        pages_amazon.open()
        pages_amazon.login(email, password)
        assert "Hello, test" == pages_amazon.get_login()