import time
import allure
import page

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):


    @allure.step(title='我 获取 昵称')
    def get_nick_name_text(self):
        return self.find_element(page.nick_name_text_view).text

    @allure.step(title='我 点击 设置')
    def click_setting(self):
        self.find_element_with_scroll(page.setting_button).click()

    @allure.step(title='我 点击 加入vip')
    def click_be_vip(self):
        self.find_element_with_scroll(page.be_vip_button).click()
        time.sleep(2)