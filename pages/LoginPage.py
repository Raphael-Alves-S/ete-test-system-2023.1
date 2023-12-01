from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class LoginPage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    css_selec_login_button = '.oxd-button'
    selector_by_name_username = 'username'
    selector_by_name_password = 'password'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver=driver)

    def open_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def is_url_login(self):
        return self.is_url(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selec_login_button).click()

    def enter_login(self, user_name='Admin', password='admin123'):
        self.wait_visible_element(By.NAME, self.selector_by_name_username, 10)
        self.driver.find_element(By.NAME, self.selector_by_name_username).send_keys(user_name)
        self.driver.find_element(By.NAME, self.selector_by_name_password).send_keys(password)
        self.click_login_btn()

