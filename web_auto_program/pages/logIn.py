from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from web_auto_program.pages.basePage import BasePage


class Login(BasePage):
    name = (By.ID, 'account')
    pass_word = (By.ID, 'password')
    # 登录按钮
    login_button = (By.XPATH, '/html/body/div[1]/div/div/div[2]/form/button/span')

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def goto_loginPage(self):
        self.driver.get(self.url)

    def login(self, username, psw):
        self.send_keys(self.name, username)
        self.send_keys(self.pass_word, psw)
        time.sleep(1)
        self.click(self.login_button)
        time.sleep(5)
