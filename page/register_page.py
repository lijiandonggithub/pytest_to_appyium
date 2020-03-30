import page
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class RegisterPage(BaseAction):


    # 点击 已有账号，去登陆
    @allure.step(title='注册 点击 登录页面')
    def click_login(self):
        self.click(page.login_button)
