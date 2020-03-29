from appium import webdriver

def get_driver(noReset=True):
    desired_caps = {}
    desired_caps['platformName'] = 'Android' 		#指定类型
    desired_caps['platformVersion'] = '6.0.1'		#模拟器版本
    desired_caps['deviceName'] = '127.0.0.1:7555'	#模拟器名      android的可以随意写（安全起见，按照标准来），ios必须写标准
    desired_caps['appPackage'] = 'com.yunmall.lc'#apk名
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'		#首启动
    desired_caps['noReset'] = noReset                 #True 不重置应用
    return webdriver.Remote('http://localhost:4723/wd/hub',desired_caps) #默认的值

