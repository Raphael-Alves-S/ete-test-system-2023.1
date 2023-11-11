import pytest


class Test1:

    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_click_login_button(self, run_all_browser):
        login_p = run_all_browser
        login_p.enter_login()


