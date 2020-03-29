#ModuleNotFoundError: No module named 'base' 当使用pytest框架运行时出现导包错误，使用下面两句话
import os,sys
sys.path.append(os.getcwd())
import pytest
from base.base_driver import get_driver
from time import sleep

class TestLogin():

    def setup(self):
        self.driver=get_driver(True)

    def teardown(self):
        sleep(5)
        self.driver.quit()
        pass


    def test_login(self):
        print("aaa")