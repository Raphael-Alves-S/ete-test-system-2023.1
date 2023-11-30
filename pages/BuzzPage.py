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
    xpath_input_edit = "//div[@class='oxd-buzz-post oxd-buzz-post--active oxd-buzz-post--composing']/textarea[@class='oxd-buzz-post-input']"
    xpath_text_area = "//textarea[.='Teste de postEditado']"
    xpath_post_edit = "//div[@class='oxd-form-actions orangehrm-buzz-post-modal-actions']/button[@class='oxd-button oxd-button--medium oxd-button--main']"

    css_btn_delete_post = '.bi-trash'

    xpath_title_modal_delete = "//p[@class='oxd-text oxd-text--p oxd-text--card-title']"
    xpath_btn_confirm_delete = "//i[@class='oxd-icon bi-trash oxd-button-icon']"

    def __init__(self, driver):
        super(BuzzyPage, self).__init__(driver=driver)

    # -------------------------- Entrar no módulo de Buzz ------------------------ #

    def click_btn_buzz(self):
        self.wait_visible_element(By.CSS_SELECTOR, "[href='/web/index.php/buzz/viewBuzz']", 10)
        self.driver.find_element(By.CSS_SELECTOR, "[href='/web/index.php/buzz/viewBuzz']").click()

    def is_url_buzzy(self):
        return self.is_url(self.url)

    def has_buzzy_tittle(self):
        return self.wait_visible_element(By.CLASS_NAME, self.class_buzz_tittle, 10)

    # ----------------------------- Fazer um post ---------------------------- #

    def buzzy_post(self, post='Teste de post'):
        self.wait_visible_element(By.CSS_SELECTOR,  self.css_buzzy_input, 10)
        self.driver.find_element(By.CSS_SELECTOR,  self.css_buzzy_input).send_keys(post)
        self.driver.find_element(By.XPATH, self.xpath_btn_post).click()

    def view_post(self):
        self.wait_visible_element(By.XPATH, self.xpath_buzz_post, 10)
        self.driver.find_element(By.XPATH, self.xpath_buzz_post).is_displayed()

    # ----------------------------- Editar um post ---------------------------- #

    def edit_post(self, edit="Editado"):

        self.wait_visible_element(By.XPATH, self.xpath_btn_three_dots, 10)
        self.driver.find_element(By.XPATH, self.xpath_btn_three_dots).click()

        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_edit_post).is_displayed()
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_edit_post).click()

        self.wait_visible_element(By.XPATH, self.xpath_modal_tittle, 10)

        self.wait_visible_element(By.XPATH, self.xpath_input_edit, 10)
        self.driver.find_element(By.XPATH, self.xpath_input_edit).send_keys(edit)
        self.wait_visible_element(By.XPATH, self.xpath_text_area, 10)

        self.wait_visible_element(By.XPATH, self.xpath_post_edit, 10)
        self.driver.find_element(By.XPATH, self.xpath_post_edit).click()

        # ----------------------------- Excluir um post ---------------------------- #

    def delete_post(self):
        self.wait_visible_element(By.XPATH, self.xpath_btn_three_dots, 15)
        self.driver.find_element(By.XPATH, self.xpath_btn_three_dots).click()

        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_delete_post).is_displayed()
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_delete_post).click()

        self.wait_visible_element(By.XPATH, self.xpath_title_modal_delete, 15)

        self.wait_visible_element(By.XPATH, self.xpath_btn_confirm_delete, 15)
        self.driver.find_element(By.XPATH, self.xpath_btn_confirm_delete).click()


