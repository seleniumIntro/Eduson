import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from selenium.webdriver.common.by import By


class PagesYandex:
    def __init__(self, driver, url, cart, order):
        self.driver = driver
        self.url = url
        self.order_url = order
        self.cart_url = cart

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, limeout=30):
        return Wait(self.driver, limeout).until(EC.visibility_of_element_lacated(locator))

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div[2]/div/div/div[1]/input').click()
        #self.driver.find_element(By.XPATH, '//*[@type=\"submit\"]')
        self.driver.find_element(By.XPATH, '//span[text()="Войти"]').click()
        self.driver.find_element(By.XPATH, '//button[@data-type=\"login\"]').click()
        self.driver.find_element(By.ID, 'passp-field-login').send_keys(username)
        self.driver.find_element(By.ID, 'passp:sign-in').click()
        self.driver.find_element(By.XPATH, '//input[@data-t=\"field:input-passwd\"]').send_keys(password)
        self.driver.find_element(By.ID, 'passp:sign-in').click()

    def use_search(self):
        self.driver.find_element(By.ID, 'header-search').send_keys("Nocord NCD-20.2.15.C")
        self.driver.find_element(By.XPATH, '//span[text()="Найти"]').click()
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@title=\'Аккумуляторная дрель-шуруповерт Nocord, 20В, 2х1.5 А·ч Li-Ion, в кейсе + 24 предмета оснастки, NCD-20.2.15.C\']'))).click()
        #self.driver.find_element(By.XPATH, '//a[@title=\'Аккумуляторная дрель-шуруповерт Nocord, 20В, 2х1.5 А·ч Li-Ion, в кейсе + 24 предмета оснастки, NCD-20.2.15.C\']').click()

    def get_url(self):
        return self.driver.current_url

    def check_elements_by_text(self, text):
        try:
            self.driver.find_element(By.XPATH, '//span[text()='+text+']')
        except NoSuchElementException:
            return False
        return True








