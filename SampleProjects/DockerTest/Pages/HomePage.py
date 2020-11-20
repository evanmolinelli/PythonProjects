class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.logout_btn_id = "logoutButton"

    def logout(self):
        self.driver.find_element_by_css_selector("#loggedInMenu > div > div.styles__expandable___1RB6Z > svg").click()
        self.driver.find_element_by_id(self.logout_btn_id).click()
