import random
import string

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class PageObject:

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()

    def is_url(self, url):
        return self.driver.current_url == url

    def click_button(self, by, value, waittime):
        self.wait_visible_element(by, value, waittime)
        self.driver.find_element(by, value).click()

    def select_element(self, by, value, text):
        select_element = self.driver.find_element(by, value)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def string_generator(self, size, chars=string.ascii_uppercase + string.ascii_lowercase):
        password = ''.join(random.choice(chars) for _ in range(size))
        return password

    def wait_visible_element(self, by, value, timeout):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((by, value)))
        except TimeoutException:
            return False
        return element.is_displayed()

    def is_title(self, title_text):
        title_element_text = self.driver.find_element(By.CLASS_NAME, self.class_title_page).text
        return title_element_text == title_text

    def is_page(self, url, title_text):
        return self.is_title(title_text) and self.is_url(url)

    def close(self):
        self.driver.quit()
