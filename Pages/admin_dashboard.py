class AdminDashboard:
    def __init__(self,page):
        self.page = page
        self.admin_icon = page.locator("//a[@data-toggle='dropdown']")
        self.logout_field = page.locator("//a[@class='dropdown-item']").nth(1)
        self.more_info_link = page.locator("//a[@class='small-box-footer']").nth(1)

    def click_admin_icon(self):
        self.admin_icon.click()
        return self

    def click_logout_field(self):
        from Pages.loginpage import LoginPage
        self.logout_field.click()
        return LoginPage(self.page) #Circular import happens when Pom's are working in relation to each other

    def click_more_info_link(self):
        from Pages.homepage import HomePage
        self.more_info_link.click()
        return HomePage(self.page)
