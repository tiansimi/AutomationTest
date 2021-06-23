from appium import webdriver

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
