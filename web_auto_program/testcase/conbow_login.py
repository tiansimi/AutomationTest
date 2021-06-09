from selenium import webdriver
import unittest
from web_auto_program.common.filePath import path
from web_auto_program.pages.logIn import Login
from web_auto_program.common.logger import Logger
import logging
import HTMLTestRunner


class ConbowLogin(unittest.TestCase):

    def test_conbowlogin(self):
        self.driver = webdriver.Chrome()
        self.conbowlogin = Login(self.driver, url="https://test-steward-saas.goodaa.com.cn/user/passwordLogin")
        self.driver.implicitly_wait(10)  # 10s加载完毕，自动进行下一步
        self.conbowlogin.goto_loginPage()
        self.conbowlogin.login('tianqi', '123456')
        self.lg = Logger(path + '/logs/conbowlogin.log')

        # self.lg.info('登录成功！')


if __name__ == "__main__":
    casepath = path + '/testcase/conbow_login.py'
    discover = unittest.defaultTestLoader.discover(start_dir=casepath,
                                                   pattern='test*.py',
                                                   top_level_dir=None)
    # 报告路径地址
    file_name = path + '/report/result.html'

    fp = open(file_name, 'wb')
    # 定义报告模板
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='执行详情：')
    runner.run(discover)
    fp.close()
