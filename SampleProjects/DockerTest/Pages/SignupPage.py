class SignupPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_text_id = "username"
        self.email_text_id = "email"
        self.pwd_text_id = "password"
        self.submit_btn_id = "submit"
        self.recapture_error_class_name = "styles__errorMessage___XzWOy"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_text_id).clear()
        self.driver.find_element_by_id(self.username_text_id).send_keys(username)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_text_id).clear()
        self.driver.find_element_by_id(self.email_text_id).send_keys(email)

    def enter_pwd(self, pwd):
        self.driver.find_element_by_id(self.pwd_text_id).clear()
        self.driver.find_element_by_id(self.pwd_text_id).send_keys(pwd)

    def click_submit(self):
        self.driver.find_element_by_id(self.submit_btn_id).click()

    def error_message_for_recapture(self):
        res = self.driver.find_element_by_class_name(self.recapture_error_class_name).is_displayed()
        return res