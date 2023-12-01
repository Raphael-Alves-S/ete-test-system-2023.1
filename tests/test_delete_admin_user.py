from pages.AdmPage import AdmPage


class TestSearchAdminUser:

    def test_search_user_add(self, login_orangehr):
        login_p = login_orangehr
        admpage = AdmPage(login_p.driver)
        admpage.select_menu_admin_page()
        username = admpage.search_user_ess()
        admpage.delete_user(username)
        assert admpage.validate_delete_user() == "Info\nNo Records Found\n×", "Validação da mensagem de retorno está errada"
        



