from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'oppp k5'
desired_caps['appPackage'] = 'com.ijourney.conbow'
desired_caps['appActivity'] = 'com.ijourney.conbow.MainActivity'
desired_caps['noReset'] = True
desired_caps['udid'] = '2529c2e6'

# 连接Appium server
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element_by_id()
driver.find_element_by_class_name()
driver.find_element_by_accessibility_id()   # content-desc
driver.find_element_by_android_uiautomator('new UiSelector().text("柠檬社区")') # 柠檬社区要用双引号，因为是Java语言
