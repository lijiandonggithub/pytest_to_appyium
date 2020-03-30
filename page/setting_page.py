import page
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class SettingPage(BaseAction):

    # 点击 关于百年奥莱
    @allure.step(title='设置 点击 关于百年奥莱')
    def click_about(self):
        self.find_element_with_scroll(page.about_button).click()

    # 点击 清理缓存
    @allure.step(title='设置 点击 清理缓存')
    def click_clear_cache(self):
        self.find_element_with_scroll(page.clear_cache_button).click()

    # 点击 地址管理
    @allure.step(title='设置 点击 地址管理')
    def click_address_list(self):
        self.find_element_with_scroll(page.address_list_button).click()