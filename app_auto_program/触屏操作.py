import time
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait  # 导入等待
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

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
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc))                # 等待页面元素出现
# 滑动九宫格案例
ele = driver.find_element_by_id('')
# 元素的大小
size = ele.size
# 均分的步长 宽和高一样
step = size['width']/6  # 斜线除法 会取整
# 元素的起点坐标 左上角(x值和y值）
ori = ele.location
point1 = (ori['x'] + step, ori['y'] + step)
point2 = (point1[0] + step * 2, point1[1] + step)   # x轴增加了2step
point3 = (point2[0] + step * 2, point2[1] + step)   # x轴增加了2step

TouchAction(driver).press(x=point1[0],y=point1[1]).wait(200).move_to(x=point2[0],y=point2[1]).wait(200).move_to(x=point3[0],y=point3[1]).wait(200).\
release().perform()









