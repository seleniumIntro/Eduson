from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from selenium.webdriver.common.by import By


class PagesMain:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, limeout=30):
        return Wait(self.driver, limeout).until(EC.visibility_of_element_lacated(locator))

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id=\"mailbox\"]/div[1]/button').click()

        iframe = self.driver.find_element(By.CLASS_NAME, "ag-popup__frame__layout__iframe")

        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.XPATH, '//input[@name=\"username\"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@data-test-id=\"next-button\"]').click()
        self.driver.find_element(By.XPATH, '//input[@name=\"password\"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@data-test-id=\"submit-button\"]').click()
        self.driver.switch_to.default_content()


    def get_login(self):
        wait = WebDriverWait(self.driver, 30)
        login = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ph-project__user-name'))).text
        return login

    def create_male(self):
        self.driver.find_element(By.CLASS_NAME, 'compose-button__txt').click()


    def get_weather(self):
        return self.driver.find_element(By.XPATH, '//span[@data-testid=\"weather-temp\"]').text

    def get_dzen_result(self):
        iframe = self.driver.find_element(By.CLASS_NAME, "yandex-frame")
        self.driver.switch_to.frame(iframe)
        cat = self.driver.find_element(By.CLASS_NAME, "serp-title").text
        return cat

    def use_search(self):
        iframe = self.driver.find_element(By.CLASS_NAME, "search-arrow__frame")

        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.CLASS_NAME, 'arrow__input').send_keys('Котики')
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CLASS_NAME, 'search-arrow__button').click()



