import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class LoginPage(PageObject):

    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.WebDriverWait = None

    def open_page(self):
        self.driver.get(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, '.oxd-button').click()

    def is_url_login(self):
        return self.is_url(self.url)

    # def has_login_error_message(self):
    #     error_message = self.driver.find_element(By.CLASS_NAME, 'error-message-container').text
    #     return error_message == 'Epic sadface: Username is required'

    # def is_page(self, url, title_text):
    #     raise Exception('Essa página nao tem titutlo')

    def enter_login(self, user_name='Admin', password='admin123'):
        self.wait_visible_element(By.NAME, 'username', 10)
        self.driver.find_element(By.NAME, 'username').send_keys(user_name)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.click_login_btn()

