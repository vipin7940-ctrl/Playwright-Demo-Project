from playwright.sync_api import Page,expect
from Pages.admin_dashboard import AdminDashboard
from constants.constant import login_url
from Utilities.ExcelRead import ExcelReadClass
from Pages.loginpage import LoginPage
class TestAdminDashboard:
    def test_admin_adduser(self,page:Page):
        page.goto(login_url)
        obj = ExcelReadClass()
        username1 = obj.read_excel_cell(2, 1)
        pwd1 = obj.read_excel_cell(2, 2)
        lgn = LoginPage(page)
        page.wait_for_timeout(3000)
        lgn.enter_username(username1).enter_password(pwd1).click_login().click_more_info_link().click_new_button().enter_username_new("Vip").enter_password_new("Vip").enter_user_type().enter_save_btn()


