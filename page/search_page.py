import time

import page
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class SearchPage(BaseAction):

    # 输入 关键字
    @allure.step(title='搜索页面 输入 关键字')
    def input_keyword(self, text):
        self.input(page.keyword_edit_text, text)

    # 点击 搜索
    @allure.step(title='搜索页面 点击 搜索')
    def click_search(self):
        self.click(page.search_button1)
        time.sleep(2)

    # 点击 搜索记录的删除
    @allure.step(title='搜索页面 点击 删除搜索记录')
    def click_search_del(self):
        self.click(page.search_del_button)

    def is_keyword_exist(self, keyword):
        xpath = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/keyayout']/*/*[@text='%s']" % keyword
        # xpath = By.XPATH, "//*[@text='%s']" % keyword
        return self.is_feature_exist(xpath)

    def is_search_record_empty(self):
        feature = By.XPATH, "//*[@text='暂无搜索历史']"
        return self.is_feature_exist(feature)


