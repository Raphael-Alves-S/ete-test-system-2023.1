from pages.AdmPage import AdmPage


class TestAddAdminUser:

    def test_add_user(self, login_orangehr):
        login_p = login_orangehr
        admpage = AdmPage(login_p.driver)
        admpage.select_menu_admin_page()
        admpage.click_button_add_user()
        admpage.validate_modal_add_user_is_visible()
        admpage.input_values_user_adm()
        admpage.save_button_new_user()
        assert admpage.is_url_admin(), 'URL da página de admin é invalida'






