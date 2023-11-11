import pytest

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


@pytest.fixture()
def open_browser(request):
    login_p = LoginPage(driver=None)
    login_p.open_page()
    yield login_p
    login_p.close()


@pytest.fixture()
def login_orangehr(open_browser):
    login_p = open_browser
    login_p.enter_login()
    yield login_p

