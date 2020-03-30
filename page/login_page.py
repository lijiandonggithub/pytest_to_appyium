import page
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class LoginPage(BaseAction):


    # 输入 用户名
    @allure.step(title='登录 输入 用户名')
    def input_username(self, text):
        self.input(page.username_edit_text, text)

    # 输入 密码
    @allure.step(title='登录 输入 密码')
    def input_password(self, text):
        self.input(page.password_edit_text, text)

    # 点击 登录
    @allure.step(title='登录 点击 登录')
    def click_login(self):
        self.click(page.login_button1)