class DockerMainPage():

    def __init__(self, driver):
        self.driver = driver

        self.search_toggle_id = "searchToggle"
        self.search_textbox_id = "searchText"
        self.sign_in_link_text = "Sign In"
        self.search_result_form_id = "search-form"

    def click_signin(self):
        self.driver.find_element_by_link_text('Sign In').click()

    def click_sign_up_btn(self):
        self.driver.find_element_by_link_text('Sign Up').click()

    def search_topic(self, topic):
        self.driver.find_element_by_id(self.search_toggle_id).click()
        self.driver.find_element_by_id(self.search_textbox_id).send_keys(topic)
        self.driver.find_element_by_id(self.search_toggle_id).click()

    def search_form_confirm(self):
        res = self.driver.find_element_by_id(self.search_result_form_id).is_displayed()
        return res