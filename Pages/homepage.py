class HomePage:
    def __init__(self, page):
        self.page = page
        self.new_user_button = page.locator("a[class='btn btn-rounded btn-danger']")
        self.username_field = page.locator("input[name='username']")
        self.password_field = page.locator("input[name='password']")
        self.usertype_field = page.locator("//select[@name='user_type']")
        self.save_button_field = page.locator("//button[@name='Create']")
        self.popup_field = page.locator("//div[contains(@class,'alert-danger')]")
        self.popup_field_new = page.locator("//div[contains(@class,'alert-success')]")
    def click_new_button(self):
        self.new_user_button.click()
        return self
    def enter_username_new(self,user1):
        self.username_field.fill(user1)
        return self
    def enter_password_new(self,pwd1):
        self.password_field.fill(pwd1)
        return self
    def enter_user_type(self):
        self.usertype_field.select_option("staff")
        return self
    def enter_save_btn(self):
        self.save_button_field.click()
        return self
#this method is for username already exists case [based on alert-danger]
    def isPopupVisible(self):
        print(self.popup_field.text_content())
# this method is for user created successfulyy case [based on alert-success]
    def isPopupVisible_new_user(self):
        print(self.popup_field_new.text_content())

