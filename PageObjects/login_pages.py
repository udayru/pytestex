
class Login:
    user_name = 'Admin'
    user_password = 'admin123'

    def __init__(self, driver):
        self.driver = driver

    def login_user_name(self):
        self.driver.find_element_by_id('txtUsername').send_keys(self.user_name)

    def login_user_password(self):
        self.driver.find_element_by_id('txtPassword').send_keys(self.user_name)

    def login_user_click(self):
        self.driver.find_element_by_id('btnLogin').click()
