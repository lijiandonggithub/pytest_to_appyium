import page
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class HomePage(BaseAction):


    # 点击 我
    @allure.step(title='主页 点击 我')
    def click_me(self):
        self.click(page.me_button)

    # 点击 分类
    @allure.step(title='主页 点击 分类')
    def click_category(self):
        self.click(page.category_button)

    # 点击 购物车
    @allure.step(title='主页 点击 购物车')
    def click_shop_cart(self):
        self.click(page.shop_cart_button)

    # 点击 首页
    @allure.step(title='主页 点击 首页')
    def click_home(self):
        self.click(page.home_button)

    # 点击 放大镜
    @allure.step(title='主页 点击 放大镜')
    def click_search(self):
        self.click(page.search_button)

    @allure.step(title='主页 登录（如果没有登录的话）')
    def login_if_not(self, page):
        # 判断登录状态
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return

        # 没有登录，就去登录
        # 点击 已有账号
        page.register.click_login()
        # 输入 用户名
        page.login.input_username("itheima_test")
        # 输入 密码
        page.login.input_password("itheima")
        # 点击 登录
        page.login.click_login()
