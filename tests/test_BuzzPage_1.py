import pytest

from pages.BuzzPage import BuzzyPage

class TestBuzzPage1:

    def test_buzz_post(self, login_orangehr):
        login_p = login_orangehr

        leave_p = BuzzyPage(driver=login_p.driver)
        leave_p.click_btn_buzz()
        leave_p.is_url_buzzy()
        leave_p.has_buzzy_tittle()

        leave_p.buzzy_post()
        leave_p.view_post()
