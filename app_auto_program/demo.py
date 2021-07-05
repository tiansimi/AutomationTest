import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait  # 导入等待

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'oppp k5'
desired_caps['appPackage'] = 'com.ijourney.conbow'
desired_caps['appActivity'] = "com.ijourney.conbow.MainActivity"
desired_caps['noReset'] = True
desired_caps['udid'] = 'SJE0217329001578'

# 连接Appium server
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("请输入手机号")')
WebDriverWait(driver, 30).until()                # 等待页面元素出现
# print(desired_caps)
# driver.find_element_by_id()
# driver.find_element_by_class_name()
# driver.find_element_by_accessibility_id()   # content-desc
# driver.find_element_by_android_uiautomator('new UiSelector().text("柠檬社区")')  # 柠檬社区要用双引号，因为是Java语言
# 输入账号和密码
driver.find_element_by_android_uiautomator('new UiSelector().text("请输入手机号")').send_keys('17310520712')
driver.find_element_by_android_uiautomator('new UiSelector().text("请输入4位验证码")').send_keys('9456')
time.sleep(1)
driver.find_element_by_android_uiautomator('new UiSelector().text("绑定手机并登录")').click()   # 点击登录按钮
