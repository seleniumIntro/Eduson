import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from selenium.webdriver.common.by import By


class PagesYandex:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, limeout=30):
        return Wait(self.driver, limeout).until(EC.visibility_of_element_lacated(locator))

    def login(self, username, password):
        #self.driver.find_element(By.XPATH, '//input[@type=\"submit\"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Войти"]').click()
        self.driver.find_element(By.XPATH, '//button[@data-type=\"login\"]').click()
        self.driver.find_element(By.ID, 'passp-field-login').send_keys(username)
        self.driver.find_element(By.ID, 'passp:sign-in').click()
        self.driver.find_element(By.XPATH, '//input[@data-t=\"field:input-passwd\"]').send_keys(password)
        self.driver.find_element(By.ID, 'passp:sign-in').click()

    def create_bucket(self):
        self.driver.find_element(By.XPATH, '//input[@type=\"submit\"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Войти"]').click()
        self.driver.find_element(By.XPATH, '//button[@data-type=\"login\"]').click()




