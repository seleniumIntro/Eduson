import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from selenium.webdriver.common.by import By


class PagesAmazon:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
        self.driver.find_element(By.ID, 'ap_email').send_keys(username)
        self.driver.find_element(By.ID, 'continue').click()
        self.driver.find_element(By.ID, 'ap_password').send_keys(password)
        self.driver.find_element(By.ID, 'signInSubmit').click()

    def get_login(self):
        return self.driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').text
