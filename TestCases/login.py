import time


from PageObjects.login_pages import Login


class Test_Login:
    url = 'https://opensource-demo.orangehrmlive.com/'

    def test_login_dtt(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(5)
        self.lp = Login(self.driver)

        self.lp.login_user_name()
        time.sleep(5)
        self.lp.login_user_password()
        time.sleep(5)
        self.lp.login_user_click()
        tile = self.driver.title
        assert tile == 'OrangeHR'
