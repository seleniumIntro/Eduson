import time

from selenium.webdriver.common.by import By


class PagesAmazon:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def login(self, login, password):
        self.driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
        self.driver.find_element(By.XPATH, "//input[@type=\"email\"]").send_keys(login)
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "ap_password").send_keys(password)
        self.driver.find_element(By.ID, "signInSubmit").click()


    def get_login(self):
        return self.driver.find_element(By.ID, "nav-link-accountList-nav-line-1").text


