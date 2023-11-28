from selenium.webdriver.common.by import By
from pages.PageObject import PageObject
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
from faker import Faker



class AddEmployee(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'
    xpath_add_employee_btn = '//a[.="Add Employee"]' ##botão de adicionar menu
    class_fist_name = 'firstName'
    class_middle_name = 'middleName'
    class_last_name = 'lastName'
    css_employee_id = '.oxd-input-field-bottom-space[data-v-7fe2d320] .oxd-input'
    css_login_details = '.oxd-switch-input'
    xpath_username = '//div[@class="orangehrm-employee-form"]/div[@class="oxd-form-row"]/div[1]//input[@class="oxd-input oxd-input--active"]'
    xpath_password = '//div[@class="oxd-grid-item oxd-grid-item--gutters user-password-cell"]//input[@class="oxd-input oxd-input--active"]'
    xpath_confirm_password = "//div[@class='oxd-form-row user-password-row']//div[@class='oxd-grid-item oxd-grid-item--gutters']//input[@class='oxd-input oxd-input--active']"
    xpath_status_enable = "//label[.='Enabled']"
    xpath_status_disable = "//label[.='Disabled']"
    css_cancel_btn = ".oxd-button--ghost"
    css_save_btn = ".oxd-button--secondary"


    def __init__(self, driver):
        super(AddEmployee, self).__init__(driver=driver)

    def is_url_AddEmployee(self):
        return self.is_url(self.url)

    def open_menu_addemployee(self):
        self.driver.find_element(By.XPATH, self.xpath_add_employee_btn).click()

    def gerar_id_numeric():
        id_numeric = ''.join(random.choice('0123456789') for _ in range(6))
        return id_numeric

    def add_AddEmployee_not_password(self, fistName='test',middleName='', lastName='',id='')
        self.open_menu_addemployee()
        self.driver.find_element(By.NAME, self.class_fist_name).send_keys(fistName)





