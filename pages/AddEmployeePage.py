from selenium.webdriver.common.by import By
from pages.PageObject import PageObject
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddEmployee(PageObject):

    xpath_add_employee_btn = '//a[.="Add Employee"]' ##botão de adicionar
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




