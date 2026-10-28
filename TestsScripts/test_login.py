from playwright.sync_api import Page,expect
from Pages.admin_dashboard import AdminDashboard
from constants.constant import login_url
from Utilities.ExcelRead import ExcelReadClass
from Pages.loginpage import LoginPage
import pytest
class TestAdminLogin:
    @pytest.mark.timeout(3000)
    def test_admin_login(self,page:Page):
        page.goto(login_url)
        user = page.get_by_placeholder("username")
        user.fill("admin")
        pwd = page.get_by_placeholder("Password")
        pwd.fill("admin")
        btn = page.locator("//button[text()='Sign In']")
        btn.click()
        page.wait_for_timeout(3000)
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")

    @pytest.mark.order(2)
    def test_admin_login_data_driven(self,page:Page):
        page.goto(login_url)
        obj = ExcelReadClass()
        username1 = obj.read_excel_cell(2,1)
        pwd1 = obj.read_excel_cell(2,2)
        lgn = LoginPage(page)
        lgn.enter_username(username1)
        lgn.enter_password(pwd1)
        lgn.click_login()
        page.wait_for_timeout(3000)
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")
#Test Invalid data login and assertions
    @pytest.mark.order(1)
    def test_admin_logout(self,page:Page):
        page.goto(login_url)
        obj = ExcelReadClass()
        username1 = obj.read_excel_cell(2, 1)
        pwd1 = obj.read_excel_cell(2, 2)
        lgn = LoginPage(page)
        lgn.enter_username(username1)
        lgn.enter_password(pwd1)
        lgn.click_login()
        page.wait_for_timeout(3000)
        admin = AdminDashboard(page)
        admin.click_admin_icon()
        admin.click_logout_field()
        expect(page).to_have_url(login_url)
        page.wait_for_timeout(3000)
    #@pytest.mark.flaky(reruns=2)
    def test_admin_logout_pom_chaining(self,page:Page):
        page.goto(login_url)
        obj = ExcelReadClass()
        username1 = obj.read_excel_cell(2, 1)
        pwd1 = obj.read_excel_cell(2, 2)
        lgn = LoginPage(page)
        lgn.enter_username(username1).enter_password(pwd1).click_login().click_admin_icon().click_logout_field()
        expect(page).to_have_url(login_url)
        page.wait_for_timeout(3000)














