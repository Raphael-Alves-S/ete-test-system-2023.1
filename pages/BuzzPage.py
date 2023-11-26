from pages.PageObject import PageObject
from selenium.webdriver.common.by import By


class BuzzyPage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz'
    class_buzz_tittle = 'oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module'
    css_buzzy_input = '.oxd-buzz-post-input'
    xpath_btn_post = "//button[@class='oxd-button oxd-button--medium oxd-button--main']"
    xpath_btn_three_dots = "//div[@class='oxd-grid-1 orangehrm-buzz-newsfeed-posts']/div[1]//div[@class='orangehrm-buzz-post']//button[@class='oxd-icon-button']"
    css_btn_edit_post = '.bi-pencil'
    xpath_buzz_post = "//p[.='Teste de post']"

    xpath_modal_tittle = "//p[.='Edit Post']"
    css_input_edit = '.oxd-buzz-post--composing > .oxd-buzz-post-input'
    xpath_text_area = "//textarea[.='Teste de postEditado']"
    xpath_post_edit = "//div[@class='oxd-form-actions orangehrm-buzz-post-modal-actions']/button[@class='oxd-button oxd-button--medium oxd-button--main']"

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
        self.wait_visible_element(By.CSS_SELECTOR,  self.css_buzzy_input, 7)
        self.driver.find_element(By.CSS_SELECTOR,  self.css_buzzy_input).send_keys(post)
        self.driver.find_element(By.XPATH, self.xpath_btn_post).click()

    def view_post(self):
        self.wait_visible_element(By.XPATH, self.xpath_buzz_post, 7)
        self.driver.find_element(By.XPATH, self.xpath_buzz_post).is_displayed()

    # ----------------------------- Editar um post ---------------------------- #

    def edit_post(self, edit="Editado"):
        self.wait_visible_element(By.XPATH, self.xpath_btn_three_dots, 7)
        self.driver.find_element(By.XPATH, self.xpath_btn_three_dots).click()

        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_edit_post).is_displayed()
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_edit_post).click()

        self.wait_visible_element(By.XPATH, self.xpath_modal_tittle, 7)

        self.wait_visible_element(By.CSS_SELECTOR, self.css_input_edit, 7)
        self.driver.find_element(By.CSS_SELECTOR, self.css_input_edit).send_keys(edit)
        self.wait_visible_element(By.XPATH, self.xpath_text_area, 7)

        self.wait_visible_element(By.XPATH, self.xpath_post_edit, 7)
        self.driver.find_element(By.XPATH, self.xpath_post_edit).click()
