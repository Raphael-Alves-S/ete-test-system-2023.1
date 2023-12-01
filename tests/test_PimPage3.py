from pages.PimPage import PimPage


class Test_pim_search_employee():
    def test_pim_search(self, login_orangehr):
        login_p = login_orangehr

        pim_p = PimPage(driver=login_p.driver)
        pim_p.navigate_to_pim_module()
        pim_p.edit_employee_details()
