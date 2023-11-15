from pages.PageObject import PageObject
from selenium.webdriver.common.by import By


class BuzzyPage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz'
    class_buzz_tittle = 'oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module'
    css_buzzy_input = '.oxd-buzz-post-input'
    xpath_buzz_post = "afa//b[.='Tjeste de post']"
    xpath_btn_post = "//button[@class='oxd-button oxd-button--medium oxd-button--main']"

    def __init__(self, driver):
        super(BuzzyPage, self).__init__(driver=driver)

    # -------------------------- Entrar no módulo de Buzz ------------------------ #

    def click_btn_buzz(self):
        self.wait_visible_element(By.CSS_SELECTOR, "[href='/web/index.php/buzz/viewBuzz']", 15)
        self.driver.find_element(By.CSS_SELECTOR, "[href='/web/index.php/buzz/viewBuzz']").click()

    def is_url_buzzy(self):
        return self.is_url(self.url)

    def has_buzzy_tittle(self):
        return self.wait_visible_element(By.CLASS_NAME, self.class_buzz_tittle, 4)

    # ----------------------------- Fazer um post ---------------------------- #

    def buzzy_post(self, post='Teste de post'):
        self.wait_visible_element(By.CSS_SELECTOR,  self.css_buzzy_input, 5)
        self.driver.find_element(By.CSS_SELECTOR,  self.css_buzzy_input).send_keys(post)
        self.driver.find_element(By.XPATH, self.xpath_btn_post).click()

    def view_post(self):
        return self.wait_visible_element(By.XPATH, self.xpath_buzz_post, 5)

