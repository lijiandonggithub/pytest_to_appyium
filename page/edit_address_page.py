import random
import time

import page
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class EditAddressPage(BaseAction):


    # 输入 收件人
    @allure.step(title='编辑地址 输入 收件人')
    def input_name(self, text):
        self.input(page.name_edit_text, text)

    # 输入 手机号
    @allure.step(title='编辑地址 输入 手机号')
    def input_phone(self, text):
        self.input(page.phone_edit_text, text)

    # 输入 详细地址
    @allure.step(title='编辑地址 输入 详细地址')
    def input_info(self, text):
        self.input(page.info_edit_text, text)

    # 输入 邮编
    @allure.step(title='编辑地址 输入 邮编')
    def input_post_code(self, text):
        self.input(page.post_code_edit_text, text)

    # 点击 设为默认地址
    @allure.step(title='编辑地址 点击 默认地址')
    def click_default_address(self):
        self.click(page.default_address_button)

    # 点击 所在地区
    @allure.step(title='编辑地址 点击 所在地区')
    def click_region(self):
        self.click(page.region_button)

    # 进入 所在地区 并且选择一个随机的区域
    @allure.step(title='选择区域')
    def choose_region(self):
        self.click_region()
        time.sleep(1)
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            # 所有的可选你的省市区
            areas = self.find_elements(page.area_feature)
            # 所有的可选的个数
            areas_count = len(areas)
            # 随机数下标
            area_index = random.randint(0, areas_count - 1)
            # 获取随机的城市
            areas[area_index].click()

            time.sleep(1)

    # 点击 保存
    def click_save(self):
        self.click(page.save_button)

