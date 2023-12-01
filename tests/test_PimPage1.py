import pytest

from pages.PimPage import PimPage


class Test_pim_add_employee():
    def test_pim_add(self, login_orangehr):
        login_p = login_orangehr

        pim_p = PimPage(driver=login_p.driver)
        pim_p.navigate_to_pim_module()
        pim_p.add_employee()
