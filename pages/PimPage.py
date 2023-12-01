from pages.PageObject import PageObject
from selenium.webdriver.common.by import By


class PimPage(PageObject):
    xpath_menu_pim = "//a[@href='/web/index.php/pim/viewPimModule']/span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']"
    xpath_add_employee_btn = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"  ##botão de adicionar
    name_fist_name = "firstName"
    name_middle_name = 'middleName'
    name_last_name = "lastName"
    css_employee_id = '.oxd-input-field-bottom-space[data-v-7fe2d320] .oxd-input'
    css_login_details = '.oxd-switch-input'
    xpath_username = '//div[@class="orangehrm-employee-form"]/div[@class="oxd-form-row"]/div[1]//input[@class="oxd-input oxd-input--active"]'
    xpath_password = '//div[@class="oxd-grid-item oxd-grid-item--gutters user-password-cell"]//input[@class="oxd-input oxd-input--active"]'
    xpath_confirm_password = "//div[@class='oxd-form-row user-password-row']//div[@class='oxd-grid-item oxd-grid-item--gutters']//input[@class='oxd-input oxd-input--active']"
    xpath_status_enable = "//label[.='Enabled']"
    xpath_status_disable = "//label[.='Disabled']"
    css_cancel_btn = ".oxd-button--ghost"
    css_save_btn = ".oxd-button--secondary"
    xpath_employee_list = "//a[.='Employee List']"
    css_search_employee = ".orangehrm-left-space"
    xpath_employee_name_search = "//div[@class='oxd-grid-4 orangehrm-full-width-grid']/div[1]//input[1]"
    xpath_employee_edit_save = "//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    xpath_employee_link_edit_user = "//div[@class='oxd-table-body']/div[1]//i[@class='oxd-icon bi-pencil-fill']"
    css_employee_id_search = ".oxd-grid-4 .oxd-input"

    def __init__(self, driver):
        super(PimPage, self).__init__(driver=driver)

    def navigate_to_pim_module(self):
        self.wait_visible_element(By.XPATH, self.xpath_menu_pim, 10)
        self.driver.find_element(By.XPATH, self.xpath_menu_pim).click()

    def add_employee(self, first_name="FirstName", last_name="LastName"):
        self.wait_visible_element(By.XPATH, self.xpath_add_employee_btn, 10)
        self.driver.find_element(By.XPATH, self.xpath_add_employee_btn).click()
        self.wait_visible_element(By.NAME, self.name_fist_name, 10)
        self.driver.find_element(By.NAME, self.name_fist_name).send_keys(first_name)
        self.driver.find_element(By.NAME, self.name_last_name).send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, self.css_save_btn).click()

    def search_employee(self, employee_name="FirstName"):
        self.wait_visible_element(By.XPATH, self.xpath_employee_list, 10)
        self.driver.find_element(By.XPATH, self.xpath_employee_name_search).send_keys(employee_name)
        self.driver.find_element(By.CSS_SELECTOR, self.css_search_employee).click()

    def edit_employee_details(self, new_first_name="NewName", new_last_name="NewLast"):
        self.wait_visible_element(By.XPATH, self.xpath_employee_link_edit_user, 10)
        self.driver.find_element(By.XPATH, self.xpath_employee_link_edit_user).click()
        self.wait_visible_element(By.NAME, self.name_fist_name, 10)
        self.driver.find_element(By.NAME, self.name_fist_name).clear()
        self.driver.find_element(By.NAME, self.name_fist_name).send_keys(new_first_name)
        self.driver.find_element(By.NAME, self.name_last_name).clear()
        self.driver.find_element(By.NAME, self.name_last_name).send_keys(new_last_name)
        self.driver.find_element(By.XPATH, self.xpath_employee_edit_save).click()
