from web_auto_program.common import filePath  # 导入路径
from web_auto_program.common import logger  # 导入日志模块
import logging


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_element(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except:
            self.path = filePath.path + '/logs/basepage.log'
            self.lg = logger.Logger(self.path)
            self.lg.error('找不到元素%s' % str(loc))

    def send_keys(self, loc, text):
        try:
            self.find_element(*loc).send_keys(text)
        except:
            self.lg.error("输入失败：%s" % text)

    def click(self, loc):  # 点击
        try:
            self.find_element(*loc).click()
        except:
            self.lg.error("点击失败：%loc" % str(loc))
