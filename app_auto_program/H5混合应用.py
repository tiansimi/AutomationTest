import time
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait  # 导入等待
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'oppp k5'
desired_caps['appPackage'] = 'com.ijourney.conbow'
desired_caps['appActivity'] = "com.ijourney.conbow.MainActivity"
desired_caps['noReset'] = True
desired_caps['udid'] = '2529c2e6'

# 连接Appium server
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
loc = 'new UiSelector().text("全程班")'
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR, loc)))
driver.find_element_by_android_uiautomator(loc).click()
# 等待webview 元素出现 -html   uc-dectool 工具识别html页面，定位元素
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.CLASS_NAME, 'android.webkit,WebView')))
# 确保切换到H5
time.sleep(1)
# 先列出所有的context(上下文）
cons = driver.contexts

# 2切换至webView 要确保chromedriver的版本要与Webview的版本匹配，也要放置在对应的位置
driver.switch_to.context(cons[-1])
# 等待元素可见
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.XPATH, '//button[]@class="bottom-btn buy"')))
driver.find_element_by_xpath('//button[@class="bottom-btn buy"]').click()

