class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_text_id = "nw_username"
        self.pwd_text_id = "nw_password"
        self.submit_btn_id = "nw_submit"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_text_id).clear()
        self.driver.find_element_by_id(self.username_text_id).send_keys(username)

    def enter_pwd(self, pwd):
        self.driver.find_element_by_id(self.pwd_text_id).clear()
        self.driver.find_element_by_id(self.pwd_text_id).send_keys(pwd)

    def click_submit(self):
        self.driver.find_element_by_id(self.submit_btn_id).click()