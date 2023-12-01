from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class AdmPage(PageObject):

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
    select_menu_admin = "//a[.='Admin']"
    button_add_user = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    modal_add_user_forms = ".orangehrm-card-container"
    button_save_user = ".oxd-button--secondary"
    select_user_role = "//div[@class='oxd-form-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[1]//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    select_value_user_role = "//div[@class='oxd-select-wrapper']//span[.='Admin']"
    select_value_user_role_ess = "//div[@class='oxd-select-wrapper']//span[.='ESS']"
    select_user_status = "//div[@class='oxd-form-row']//div[3]//div[@class='oxd-select-text--after']"
    select_value_user_status = "//div[@class='oxd-select-wrapper']//span[.='Enabled']"
    password_input = "//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//input[@class='oxd-input oxd-input--active']"
    input_employee_name = "[placeholder='Type for hints...']"
    select_employee_name = "//div[@class='oxd-autocomplete-wrapper']//span"
    input_username = "//div[4]//input[@class='oxd-input oxd-input--active']"
    password_confirmation = "//div[@class='oxd-form-row user-password-row']//div[@class='oxd-grid-item oxd-grid-item--gutters']//input[@class='oxd-input oxd-input--active']"
    input_search_user_name = "//div[@class='oxd-grid-4 orangehrm-full-width-grid']//input[@class='oxd-input oxd-input--active']"
    first_username_table = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[2]"
    select_user_role_seacrh = "//div[@class='oxd-grid-4 orangehrm-full-width-grid']/div[2]//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    button_search = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    button_reset = "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']"
    validate_users_found = "//span[.='(1) Record Found']"
    delete_button = "//div[@class='oxd-table-body']/div[1]//button[1]"
    modal_confirmation = ".oxd-sheet"
    button_confirm_delete = ".oxd-button--label-danger"
    toast_modal = ".oxd-toast"

    def __init__(self, driver):
        super(AdmPage, self).__init__(driver=driver)

    def is_url_admin(self):
        return self.is_url(self.url)

    def select_menu_admin_page(self):
        self.wait_visible_element(By.XPATH, self.select_menu_admin, 5)
        self.driver.find_element(By.XPATH, self.select_menu_admin).click()

    def click_button_add_user(self):
        self.wait_visible_element(By.XPATH, self.button_add_user, 5)
        self.driver.find_element(By.XPATH, self.button_add_user).click()

    def validate_modal_add_user_is_visible(self):
        self.wait_visible_element(By.CSS_SELECTOR, self.modal_add_user_forms, 5)

    def input_values_user_adm(self):
        self.driver.find_element(By.XPATH, self.select_user_role).click()
        self.wait_visible_element(By.XPATH, self.select_value_user_role, 10)
        self.driver.find_element(By.XPATH, self.select_value_user_role).click()
        self.driver.find_element(By.XPATH, self.select_user_status).click()
        self.wait_visible_element(By.XPATH, self.select_value_user_status, 10)
        self.driver.find_element(By.XPATH, self.select_value_user_status).click()
        self.driver.find_element(By.XPATH, self.password_input).send_keys("Teste@1234")
        self.driver.find_element(By.CSS_SELECTOR, self.input_employee_name).send_keys("A")
        self.wait_visible_element(By.XPATH, self.select_employee_name, 10)
        self.driver.find_element(By.XPATH, self.select_employee_name).click()
        username = self.string_generator(7)
        self.driver.find_element(By.XPATH, self.input_username).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_confirmation).send_keys("Teste@1234")

    def save_button_new_user(self):
        self.click_button(By.CSS_SELECTOR, self.button_save_user, 1)
        self.wait_visible_element(By.XPATH, self.button_add_user, 5)

    def get_only_admin_users(self):
        self.wait_visible_element(By.XPATH, self.first_username_table, 5)
        self.driver.find_element(By.XPATH, self.select_user_role_seacrh).click()
        self.wait_visible_element(By.XPATH, self.select_value_user_role, 10)
        self.driver.find_element(By.XPATH, self.select_value_user_role).click()
        self.driver.find_element(By.XPATH, self.button_search).click()

    def get_only_ess_users(self):
        self.wait_visible_element(By.XPATH, self.first_username_table, 5)
        self.driver.find_element(By.XPATH, self.select_user_role_seacrh).click()
        self.wait_visible_element(By.XPATH, self.select_value_user_role_ess, 10)
        self.driver.find_element(By.XPATH, self.select_value_user_role_ess).click()
        self.driver.find_element(By.XPATH, self.button_search).click()

    def search_user_admin(self):
        self.get_only_admin_users()
        self.wait_visible_element(By.XPATH, self.first_username_table, 5)
        usernamevalue = self.driver.find_element(By.XPATH, self.first_username_table).text
        self.driver.find_element(By.XPATH, self.input_search_user_name).send_keys(usernamevalue)
        self.driver.find_element(By.XPATH, self.button_search).click()
        return usernamevalue

    def search_user_ess(self):
        self.get_only_ess_users()
        self.wait_visible_element(By.XPATH, self.first_username_table, 5)
        usernamevalue = self.driver.find_element(By.XPATH, self.first_username_table).text
        self.driver.find_element(By.XPATH, self.input_search_user_name).send_keys(usernamevalue)
        self.driver.find_element(By.XPATH, self.button_search).click()
        return usernamevalue

    def validate_return_search_user_admin(self):
        self.wait_visible_element(By.XPATH, self.validate_users_found, 5)
        return self.driver.find_element(By.XPATH, self.validate_users_found).text

    def delete_user(self, usernamevalue):
        self.wait_visible_element(By.XPATH, self.delete_button, 5)
        self.driver.find_element(By.XPATH, self.delete_button).click()
        self.wait_visible_element(By.CSS_SELECTOR, self.modal_confirmation, 5)
        self.driver.find_element(By.CSS_SELECTOR, self.button_confirm_delete).click()
        self.wait_visible_element(By.XPATH, self.first_username_table, 5)
        self.driver.find_element(By.XPATH, self.button_reset).click()
        self.wait_visible_element(By.XPATH, self.first_username_table, 5)
        self.driver.find_element(By.XPATH, self.input_search_user_name).send_keys(usernamevalue)
        self.driver.find_element(By.XPATH, self.button_search).click()

    def validate_delete_user(self):
        self.wait_visible_element(By.CSS_SELECTOR, self.toast_modal, 5)
        modaltext = self.driver.find_element(By.CSS_SELECTOR, self.toast_modal).text
        return modaltext
