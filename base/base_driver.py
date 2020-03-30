from appium import webdriver


def init_driver(no_reset=True):
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'  # 指定类型
    desired_caps['platformVersion'] = '6.0.1'  # 模拟器版本
    desired_caps['deviceName'] = '127.0.0.1:7555'  # 模拟器名      android的可以随意写（安全起见，按照标准来），ios必须写标准
    desired_caps['appPackage'] = 'com.yunmall.lc'  # apk名
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    # toast/
    desired_caps['automationName'] = 'Uiautomator2'
    # 是否重置应用 True:不重置 False:重置
    desired_caps['noReset'] = no_reset

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

