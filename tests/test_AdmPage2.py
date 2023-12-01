from pages.AdmPage import AdmPage


class TestSearchAdminUser:

    def test_search_user_add(self, login_orangehr):
        login_p = login_orangehr
        admpage = AdmPage(login_p.driver)
        admpage.select_menu_admin_page()
        admpage.search_user_admin()
        assert admpage.validate_return_search_user_admin() == "(1) Record Found", "Validação da mensagem de retorno está errada"
        



