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
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'found')))
        self.driver.find_element(By.XPATH, '//input[@type=\"search\"]').send_keys(Keys.ENTER)

    def set_tomorrow(self):
        self.driver.find_element(By.XPATH, '//a[text()="Завтра"]').click()

    def set_snow(self):
        self.driver.find_element(By.XPATH, '//a[text()="Снег"]').click()
        time.sleep(10)

    def get_snow(self):
        return self.driver.find_element(By.XPATH, '//a[text()="Снег"]').text
        #return self.driver.find_element(By.CLASS_NAME, 'chart.chart-snow)').find_element(By.XPATH, '/div/div[1]').get_attribute('innerHTML')
