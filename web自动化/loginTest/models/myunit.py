from selenium import webdriver
import unittest

from models.driver import browser

# 封装浏览器的启动和关闭
class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
