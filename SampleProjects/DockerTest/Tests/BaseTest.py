import unittest
import HtmlTestRunner
from selenium import webdriver
import os


class BaseTest(unittest.TestCase):

    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), "../driver", "chromedriver.exe"))
        cls.driver.implicitly_wait(20)
        cls.driver.get("https://www.docker.com/")

    def tearDown(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed!")


if __name__ == '__main__':
    #Attempted to store test results in HTML file but not cooperating with Python3 apparently
    outfile = open(os.path.join(os.getcwd(), "reports") + '\TestReport.html', 'wb')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.path.join(os.getcwd(), "reports")), verbosity=1, stream=outfile)
    outfile.close()