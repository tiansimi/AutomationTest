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
size = driver.get_window_size()  # 是一个字典
time.sleep(5)
print(size)
start_x = size['width'] * 0.5
start_y = size['height'] * 0.8
end_x = size['width'] * 0.5
end_y = size['height'] * 0.2
# 由上往下滑
driver.swipe(start_x, start_y, end_x, end_y, 200)



