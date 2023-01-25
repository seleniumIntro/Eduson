import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from selenium.webdriver.common.by import By


class PagesGis:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def search(self, city):
        self.driver.find_element(By.XPATH, '//input[@type=\"search\"]').send_keys(city)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//input[@type=\"search\"]').send_keys(Keys.ENTER)

    def set_tomorrow(self):
        self.driver.find_element(By.XPATH, '//a[text()="Завтра"]').click()

    def set_snow(self):
        self.driver.find_element(By.XPATH, '//a[text()="Снег"]').click()

    def get_snow(self):
        return self.driver.find_element(By.XPATH, '/html/body/section[2]/div[1]/section[9]/div/div[3]/div/div[3]/div/div/div[1]')\
            .text
