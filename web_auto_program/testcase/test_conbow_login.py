from selenium import webdriver
import unittest
from web_auto_program.common.filePath import path
from web_auto_program.pages.logIn import Login
from web_auto_program.common.logger import Logger
import time
from selenium.webdriver.support.wait import WebDriverWait


class ConbowLogin(unittest.TestCase):

    def test_conbowlogin(self):
        self.driver = webdriver.Chrome()
        self.conbowlogin = Login(self.driver, url="https://test-steward-saas.goodaa.com.cn/user/passwordLogin")
        self.driver.implicitly_wait(10)  # 10s加载完毕，自动进行下一步
        self.conbowlogin.goto_loginPage()
        self.conbowlogin.login('tianqi', '123456')
        self.lg = Logger(path + '/logs/conbowlogin.log')
        time.sleep(10)
        self.assertIn('首页', self.driver.title, '登录失败')




