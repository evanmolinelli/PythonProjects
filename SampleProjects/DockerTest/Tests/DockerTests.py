import time
from DockerTest.Tests.BaseTest import BaseTest
from DockerTest.Pages.LoginPage import LoginPage
from DockerTest.Pages.SignupPage import SignupPage
from DockerTest.Pages.HomePage import HomePage
from DockerTest.Pages.DockerMainPage import DockerMainPage

username = "evantester"
pwd = "evantester12345"


class DockerTests(BaseTest):

    #Picked this test case in order to navigate between Docker main page, login page,
    # and then Docker home page as well.
    def test_login_valid(self):
        driver = self.driver
        mainPage = DockerMainPage(driver)
        mainPage.click_signin()

        login = LoginPage(driver)
        login.enter_username(username)
        login.enter_pwd(pwd)
        login.click_submit()
        time.sleep(3)

        homepage = HomePage(driver)
        homepage.logout()

        res = driver.find_element_by_id("log_in").is_displayed()
        assert res, 'element not displayed!'

    #I chose to do an invalid sign up test case for a new user primarily because the reCAPTCHA
    # is very difficult to automate.
    def test_sign_up_invalid(self):
        driver = self.driver
        mainPage = DockerMainPage(driver)
        mainPage.click_signin()
        mainPage.click_sign_up_btn()

        signupPage = SignupPage(driver)
        signupPage.enter_username("invalidUser789")
        signupPage.enter_email("invaliduser789@hotmail.com")
        signupPage.enter_pwd("invaliduser789")
        signupPage.click_submit()

        res = signupPage.error_message_for_recapture()
        assert res, 'error message not displayed!'

    #I chose an easy search topic in the Docker main page because it is more difficult to find elements
    # such as icons when trying to automate tests with selenium when dynamic webpages are constantly manipulated
    # and changing with updates to the UI.
    def test_search_bar(self):
        driver = self.driver
        mainPage = DockerMainPage(driver)
        time.sleep(2)
        topic = "development"
        mainPage.search_topic(topic)
        mainPage.search_form_confirm()
