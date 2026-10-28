from playwright.sync_api import Page,expect
import pytest
class TestLoginParametrised:
    @pytest.mark.parametrize("valid_usernames",["standard_user","locked_out_user"])
    def test_login_para(self,page:Page,valid_usernames):
        page.goto("https://www.saucedemo.com/")
        page.locator("#user-name").fill(valid_usernames)
        page.locator("#password").fill("secret_sauce")
        page.locator("//input[@id='login-button']").click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
