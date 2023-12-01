import pytest

from pages.LoginPage import LoginPage


@pytest.fixture()
def open_browser(request):
    login_p = LoginPage(driver=None)
    login_p.open_page()
    yield login_p


@pytest.fixture()
def login_orangehr(open_browser):
    login_p = open_browser
    login_p.enter_login()
    yield login_p

