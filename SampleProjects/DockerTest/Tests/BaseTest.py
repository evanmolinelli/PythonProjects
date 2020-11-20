import unittest
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
    unittest.main()