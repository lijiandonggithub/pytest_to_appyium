import page
from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure

class VipPage(BaseAction):


    @allure.step(title='vip页面 输入 邀请码')
    def input_invite(self, text):
        self.input(page.invite_edit_text, text)

    @allure.step(title='vip页面 输入 成为会员')
    def click_be_vip(self):
        self.click(page.be_vip_button)