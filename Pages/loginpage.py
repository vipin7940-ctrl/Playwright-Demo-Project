class LoginPage:
    def __init__(self,page):
        self.page = page
        self.username = page.get_by_placeholder("username")
        self.password = page.get_by_placeholder("Password")
        self.login = page.locator("//button[text()='Sign In']")
    def enter_username(self,user1):
        self.username.fill(user1)
        return self
    def enter_password(self,pwd):
        self.password.fill(pwd)
        return self
    def click_login(self):
        from Pages.admin_dashboard import AdminDashboard
        self.login.click()
        return AdminDashboard(self.page)




